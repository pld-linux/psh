%include	/usr/lib/rpm/macros.perl
Summary:	Perl Shell
Summary(pl):	Perl Shell
Name:		psh
Version:	0.008
Release:	1
Copyright:	Artistic License
Group:		Shells
Group(pl):	Pow³oki
Source0:	%name-%version.tar.gz
URL:		http://www.focusresearch.com/gregor/psh/index.html
#URL:		http://sourceforge.net/project/?group_id=475
BuildRequires:	perl >= 5.6.0
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Perl Shell (psh) combines aspects of bash and other shells with
the power of Perl scripting. As author says: " It aspirate to be Your
primary login shell"

%description -l pl
Perl shell (psh) jest pow³ok± która ³±czy w sobie mo¿liwo¶ci Bash'a i
innych pow³ok z mo¿liwo¶ciami Perla. Autor twierdzi, ¿e pow³oka ta
mo¿e aspirowaæ do bycia podstawow± pow³ok± pracy.

%prep
%setup -q

%build
perl Makefile.PL
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGES.pod README* TODO HACKING RELEASE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES.pod,README,README.perl5.004,TODO,HACKING,RELEASE}.gz
%attr(755,root,root) %{_bindir}/psh
%{perl_sitearch}/*
%{perl_sitelib}/Psh.pm
%{perl_sitelib}/Psh
%{_mandir}/man1/*
%{_mandir}/man3/*
