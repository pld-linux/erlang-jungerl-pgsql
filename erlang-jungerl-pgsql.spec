# TODO: more subpackages with stuff from lib
%define	_snap	20060611
Summary:	A jungle of Erlang code: Postgresql library
Name:		erlang-jungerl-pgsql
Version:	0.1
Release:	0.%{_snap}.1
License:	distributable
Group:		Development/Languages
Source0:	%{name}-%{_snap}.tar.gz
# Source0-md5:	6208c2678c9fe34766ad4eff642b50f0
URL:		http://jungerl.sourceforge.net/
BuildRequires:	erlang
Requires:	erlang
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jungerl: A jungle of Erlang code. Postgresql library

%prep
%setup -q -n %{name}

%build
%{__make} -C src

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/erlang/lib/pgsql-%{version}
cp -a ebin src $RPM_BUILD_ROOT%{_libdir}/erlang/lib/pgsql-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%{_libdir}/erlang/lib/pgsql-*
