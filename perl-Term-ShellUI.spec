#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Term-ShellUI
Version  : 0.92
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/B/BR/BRONSON/Term-ShellUI-0.92.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BR/BRONSON/Term-ShellUI-0.92.tar.gz
Summary  : ~
Group    : Development/Tools
License  : MIT
Requires: perl-Term-ShellUI-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Term::ShellUI
Term::ShellUI makes it easy to implement a comprehensive Bash or
GDB-like command line user interface.  It supports history,
autocompletion, quoting, escaping, pretty much everything you would
expect of a decent shell.

%package dev
Summary: dev components for the perl-Term-ShellUI package.
Group: Development
Provides: perl-Term-ShellUI-devel = %{version}-%{release}
Requires: perl-Term-ShellUI = %{version}-%{release}

%description dev
dev components for the perl-Term-ShellUI package.


%package perl
Summary: perl components for the perl-Term-ShellUI package.
Group: Default
Requires: perl-Term-ShellUI = %{version}-%{release}

%description perl
perl components for the perl-Term-ShellUI package.


%prep
%setup -q -n Term-ShellUI-0.92
cd %{_builddir}/Term-ShellUI-0.92

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Term::ShellUI.3
/usr/share/man/man3/Text::Shellwords::Cursor.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
