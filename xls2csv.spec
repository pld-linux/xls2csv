Summary:	MS Excel XLS to CSV converter
Summary(pl):	Konwerter plików MS Excel XLS do CSV
Name:		xls2csv
Version:	0.0.1
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.fe.msk.ru/~vitus/catdoc/%{name}-%{version}.tar.gz
URL:		http://www.fe.msk.ru/~vitus/catdoc/xls2csv.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MS Excel XLS to CSV converter.

%description -l pl
Konwerter plików MS Excel XLS do CSV.

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
