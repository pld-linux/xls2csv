Summary:	MS Excel XLS to CSV converter
Summary(pl):	Konwerter plików MS Excel XLS do CSV
Name:		xls2csv
Version:	0.0.1
Release:	1
License:	GPL
Group:		Applications/Text
#Source0:	http://www.45.free.net/~vitus/ice/catdoc/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	f86f307c581c08de40293bfd3ceaae3b
URL:		http://www.45.free.net/~vitus/ice/catdoc/
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
