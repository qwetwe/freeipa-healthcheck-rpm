%define oname freeipa-healthcheck

Name: %oname
Version: 0.5
Release: alt0

Summary: Check the health of a freeIPA installation
License: GPLv3
Group: System/Base
Url: https://github.com/freeipa/freeipa-healthcheck

Source0: v%version.tar.gz

BuildRequires: python3-module-livereload
BuildRequires: python3-module-mkdocs >= 1.0.4-alt2


%description
Arpeggio is a recursive descent parser with memoization based on PEG
grammars (aka Packrat parser).

%prep
%setup -n Arpeggio-%version

%build
%python3_build_debug -b build3

mkdocs build

%install
rm -rf build && ln -sf build3 build
%python3_install

%files
%doc site examples
%python3_sitelibdir_noarch/%oname
%python3_sitelibdir_noarch/Arpeggio-*.egg-info

%changelog
