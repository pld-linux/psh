%include	/usr/lib/rpm/macros.perl
Summary:	Perl Shell
Summary(pl.UTF-8):	Powłoka Perla
Name:		psh
Version:	1.0
Release:	3
License:	Artistic
Group:		Applications/Shells
Source0:	http://dl.sourceforge.net/psh/%{name}-%{version}.tar.gz
# Source0-md5:	73ada6747732c9abdfec2d6ad5c477c6
Patch0:		%{name}-dirty_Makefile.patch
URL:		http://sourceforge.net/projects/psh/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Provides:	perl(Psh::StrategyBunch)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(import)'

%description
The Perl Shell (psh) combines aspects of bash and other shells with
the power of Perl scripting. As author says: "It aspirate to be Your
primary login shell"

%description -l pl.UTF-8
Powłoka Perla (psh) łączy w sobie możliwości basha i innych powłok z
możliwościami Perla. Autor twierdzi, że powłoka ta może aspirować do
bycia podstawową powłoką pracy.

%prep
%setup -q
%patch0 -p0

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
%doc CHANGES.pod COPYRIGHT INSTALL README* TODO HACKING RELEASE postinstall.pl
%attr(755,root,root) %{_bindir}/psh
%{perl_vendorlib}/Psh.pm
%{perl_vendorlib}/Psh
%{_mandir}/man1/*
%{_mandir}/man3/*
