Summary: Install Debian, Slackware, and Stampede packages with rpm.
Name: alien
Packager: Joey Hess <joey@kitenet.net>
Version: 8.95.8
Release: 1
Source: ftp://kitenet.net/pub/code/debian/alien_8.95.8.tar.gz
License: GPL
Group: Utilities/File
Buildroot: /tmp/alien-8.95.8.build
Requires: perl
BuildArchitectures: noarch

%description
Alien allows you to convert Debian, Slackware, and Stampede Packages into Red
Hat packages, which can be installed with rpm.

It can also generate Slackware, Debian and Stampede packages.

This is a tool only suitable for binary packages.

%prep
%setup -n alien
rm -rf /tmp/alien-8.95.8.build

%install
perl Makefile.PL PREFIX=$RPM_BUILD_ROOT/usr
make
make pure_install VARPREFIX=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -not -type d -printf "/%%P\n" | \
	sed '/\/man\//s/$/\*/' > manifest

%files -f manifest
%defattr(-,root,root)
%doc debian/changelog GPL README alien.lsm
