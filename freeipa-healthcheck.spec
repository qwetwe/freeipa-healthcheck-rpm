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
%_bindir/ipa-healthcheck
%python3_sitelibdir/%docname
%python3_sitelibdir/ipahealthcheck-%version-py%_python3_version.egg-info/
#%%python3_sitelibdir_noarch/ipahealthcheck-%version-py%_python3_version.egg-info/

%changelog
* Fri Feb 07 2020 Ivan Alekseev <qwetwe@altlinux.org> 0.5-alt1
- Initial build

