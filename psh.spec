%include	/usr/lib/rpm/macros.perl
Summary:	Perl Shell
Summary(pl):	Pow³oka Perla
Name:		psh
Version:	0.010pre1
Release:	4
License:	Artistic
Group:		Applications/Shells
Source0:	http://dl.sourceforge.net/psh/%{name}-%{version}.tar.gz
# Source0-md5:	41262a3d360466e7ee0d1d3a39ded562
URL:		http://sourceforge.net/projects/psh/
BuildRequires:	perl-devel >= 5.6.0
BuildRequires:	rpm-perlprov >= 4.0.2-24
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	perl(Psh::StrategyBunch)

%define		_noautoreq	"perl(import)"

%description
The Perl Shell (psh) combines aspects of bash and other shells with
the power of Perl scripting. As author says: "It aspirate to be Your
primary login shell"

%description -l pl
Pow³oka Perla (psh) ³±czy w sobie mo¿liwo¶ci basha i innych pow³ok z
mo¿liwo¶ciami Perla. Autor twierdzi, ¿e pow³oka ta mo¿e aspirowaæ do
bycia podstawow± pow³ok± pracy.

%prep
%setup -q

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.pod COPYRIGHT README* TODO HACKING RELEASE
%attr(755,root,root) %{_bindir}/psh
%{perl_vendorlib}/Psh.pm
%{perl_vendorlib}/Psh
%{_mandir}/man1/*
%{_mandir}/man3/*
