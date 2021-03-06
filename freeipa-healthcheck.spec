%define oname python3-module-freeipa-healthcheck
%define docname ipahealthcheck
%def_with check

Name: %oname
Version: 0.5
Release: alt1

Summary: Check the health of a FreeIPA installation
License: GPLv3
Group: System/Base
Url: https://github.com/freeipa/freeipa-healthcheck

Source0: %name-%version.tar.gz

BuildArch: noarch

#%%define

Requires: freeipa-server
Requires: python3-module-freeipa
Requires: python3-module-ipaserver
Requires: anacron
Requires: logrotate

BuildRequires: python3-dev
BuildRequires: libsystemd-devel
BuildRequires: python3-module-pytest-runner
BuildRequires: python3-module-freeipa
BuildRequires: python3-module-ipaserver
BuildRequires: python3-module-lib389
BuildRequires: python3-module-sss_nss_idmap

%if_with check
BuildRequires: python3(tox)
BuildRequires: python3(virtualenv)
%endif

%description
FreeIPA-healthcheck is a framework which is needed to assist with the
identification, diagnosis and potentially repair of problems.


%prep
%setup

%build
%python3_build

%install
%python3_install
%__mkdir_p %buildroot/etc/ipahealthcheck
%__cat << EOF > %buildroot/etc/ipahealthcheck/ipahealthcheck.conf
[default]
EOF
%__mkdir_p %buildroot/usr/libexec/ipa
%__cat << EOF > %buildroot/usr/libexec/ipa/ipa-healthcheck.sh
#!/bin/sh
LOGDIR=/var/log/ipa/healthcheck
\n
/usr/bin/ipa-healthcheck --output-file $LOGDIR/healthcheck.log
EOF
%__mkdir_p %buildroot%_unitdir
%__cat << EOF > %buildroot%_unitdir/ipa-healthcheck.service
[Unit]
Description=Execute IPA Healthcheck

[Service]
Type=simple
ExecStart=/usr/libexec/ipa/ipa-healthcheck.sh

[Install]
WantedBy=multi-user.target
EOF
%__cat << EOF > %buildroot%_unitdir/ipa-healthcheck.timer
[Unit]
Description=Execute IPA Healthcheck every day at 4AM

[Timer]
OnCalendar=*-*-* 04:00:00
Unit=ipa-healthcheck.service

[Install]
WantedBy=multi-user.target
EOF

#%%post_service ipa-healthcheck.service

%check
sed -i '/\[testenv\]/a whitelist_externals =\
   \/bin\/cp\
   \/bin\/sed\
commands_pre =\
   \/bin\/cp %_bindir\/py.test3 \{envbindir\}\/pytest\
   \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' tox.ini
export PIP_NO_INDEX=YES
export TOX_TESTENV_PASSENV='PIP_NO_INDEX'
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -v

%files
%doc COPYING README.md
#%%python3_sitelibdir_noarch/%docname
#%%python3_sitelibdir_noarch/ipahealthcheck-%version-py%_python3_version.egg-info/
%_bindir/ipa-healthcheck
%python3_sitelibdir/%docname
%python3_sitelibdir/ipahealthcheck-%version-py%_python3_version.egg-info/
%_sysconfdir/ipahealthcheck/
%_sysconfdir/ipahealthcheck/ipahealthcheck.conf
%_unitdir/
#python3_sitelibdir_noarch
%_target_libdir_noarch/python3/site-packages/
%_unitdir/ipa-healthcheck.service
%_unitdir/ipa-healthcheck.timer

#_libexecdir=/usr/lib
#%%_libexecdir/

#_prefix=/usr
%_prefix/libexec/ipa/ipa-healthcheck.sh

#_unitdir=/lib/systemd/system

%changelog
* Fri Feb 07 2020 Ivan Alekseev <qwetwe@altlinux.org> 0.5-alt1
- Initial build

