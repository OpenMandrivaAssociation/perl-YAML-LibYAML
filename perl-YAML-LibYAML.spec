%define upstream_name    YAML-LibYAML
%define upstream_version 0.41

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 0.41
Release:	3

Summary:    An XS Wrapper Module of libyaml
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/YAML/YAML-LibYAML-0.41.tar.gz
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




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.350.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.350.0-1
+ Revision: 654618
- new version
  update format errors patch

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.340.0-1mdv2011.0
+ Revision: 596718
- update to 0.34

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.330.0-2mdv2011.0
+ Revision: 555424
- rebuild

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 0.330.0-1mdv2010.1
+ Revision: 536218
- update to 0.33

* Sat May 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.320.0-1mdv2010.0
+ Revision: 381345
- import perl-YAML-LibYAML


* Sat May 30 2009 cpan2dist 0.32-1mdv
- initial mdv release, generated with cpan2dist


