%define upstream_name    YAML-LibYAML
%define upstream_version 0.35

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    An XS Wrapper Module of libyaml
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/YAML/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:     YAML-LibYAML-0.35-fix-format-errors.patch

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Filter::Util::Call)
BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
Kirill Siminov's 'libyaml' is arguably the best YAML implementation. The C
library is written precisely to the YAML 1.1 specification. It was
originally bound to Python and was later bound to Ruby.

This module is a Perl XS binding to libyaml which offers Perl the best YAML
support to date.

This module exports the functions 'Dump' and 'Load'. These functions are
intended to work exactly like 'YAML.pm''s corresponding functions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1 -b .format-error

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


