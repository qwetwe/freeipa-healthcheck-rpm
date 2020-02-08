%define oname freeipa-healthcheck
%define version 0.5

Name: %oname
Version: 0.5
Release: alt0

Summary: Check the health of a FreeIPA installation
License: GPLv3
Group: System/Base
Url: https://github.com/freeipa/freeipa-healthcheck

Source: %name-%version.tar.gz

#Requires: freeipa-server
Requires: freeipa-server

#Requires: python3-ipalib
Requires: python3-module-freeipa

#Requires:       python3-ipaserver
Requires: python3-module-ipaserver

#Requires:       anacron
Requires: anacron

#Requires:       logrotate
Requires: logrotate

#Requires(post): systemd-units
#Requires:       %{name}-core = %{version}-%{release}
#Requires(post): systemd-units
#Requires: 


#BuildRequires:  python3-devel
BuildRequires: python3-dev
#BuildRequires:  systemd-devel
BuildRequires: libsystemd-devel

#BuildRequires:  python3-pytest-runner
BuildRequires: python3-module-pytest-runner
#BuildRequires:  python3-ipalib
BuildRequires: python3-module-freeipa
#BuildRequires:  python3-ipaserver
BuildRequires: python3-module-ipaserver
#BuildRequires:  python3-lib389
BuildRequires: python3-module-lib389
#BuildRequires:  python3-libsss_nss_idmap
BuildRequires: python3-module-sss_nss_idmap


%description
FreeIPA-healthcheck is a framework which is needed to assist with the
identification, diagnosis and potentially repair of problems.


%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc COPYING README.md
#%%python3_sitelibdir_noarch/%oname

%changelog
* Fri Feb 07 2020 Ivan Alekseev <qwetwe@altlinux.org> 0.5-alt0
- Initial build

