%define _unpackaged_files_terminate_build 1

Name: freeipa-healthcheck
Version: 0.5
Release: alt0

Summary: Check the health of a freeIPA installation
License: GPLv3
Group: System/Base

Url: https://www.freeipa.org/page/V4/Healthcheck

# https://github.com/freeipa/freeipa-healthcheck
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
