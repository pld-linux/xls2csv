# $Revision: 1.1 $ $Date: 2001-08-24 16:19:35 $
Summary:	M$ Excel XLS to CSV converter
Summary(pl):	Konwerter plików M$ Excel XLS to CSV
Name:		xls2csv
Version:	0.0.1
Release:	1
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Source0:	http://www.nie-pamietam-use-google.com/%{name}-%{version}.tar.gz
URL:		http://www.nie-pamietam-use-google.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
M$ Excel XLS to CSV converter.

%description -l pl
Konwerter plików M$ Excel XLS to CSV.

%prep
%setup -q

%build
%{__make} CC="%{__cc}" DEBUG_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
