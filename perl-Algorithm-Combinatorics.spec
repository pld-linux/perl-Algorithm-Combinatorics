#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%define		pdir	Algorithm
%define		pnam	Combinatorics
Summary:	Efficient generation of combinatorial sequences 
Name:		perl-Algorithm-Combinatorics
Version:	0.27
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Algorithm/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bada976399f9edfe364d6fcf9e0bcde2
URL:		http://search.cpan.org/dist/Algorithm-Combinatorics/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl(Scalar::Util)
%if %{with tests}
BuildRequires:	perl(Test::More)
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Algorithm::Combinatorics is an efficient generator of combinatorial
sequences. Algorithms are selected from the literature (work in
progress, see "REFERENCES"). Iterators do not use recursion, nor
stacks, and are written in C.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}"
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Algorithm/Combinatorics.pm
%dir %{perl_vendorarch}/auto/Algorithm/Combinatorics
%attr(755,root,root) %{perl_vendorarch}/auto/Algorithm/Combinatorics/Combinatorics.so
%{_mandir}/man3/*.3pm.gz
