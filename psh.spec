%include	/usr/lib/rpm/macros.perl
Summary:	Perl Shell
Summary(pl):	Perl Shell
Name:		psh
Version:	0.010pre1
Release:	1
License:	Artistic License
Group:		Applications/Shells
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/psh/%{name}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/psh/
BuildRequires:	perl >= 5.6.0
BuildRequires:	rpm-perlprov >= 4.0.2-24
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	"perl(import)"

%description
The Perl Shell (psh) combines aspects of bash and other shells with
the power of Perl scripting. As author says: "It aspirate to be Your
primary login shell"

%description -l pl
Perl shell (psh) jest pow³ok± która ³±czy w sobie mo¿liwo¶ci Bash'a i
innych pow³ok z mo¿liwo¶ciami Perla. Autor twierdzi, ¿e pow³oka ta
mo¿e aspirowaæ do bycia podstawow± pow³ok± pracy.

%prep
%setup -q

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGES.pod COPYRIGHT README* TODO HACKING RELEASE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/psh
%{perl_sitelib}/Psh.pm
%{perl_sitelib}/Psh
%{_mandir}/man1/*
%{_mandir}/man3/*
