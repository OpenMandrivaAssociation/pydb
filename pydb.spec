Summary:	Extended debugger for Python
Name:		pydb
Version:	1.24
Release:	%mkrel 1
License:	GPLv3
Group:		Development/Python
Url:		http://bashdb.sourceforge.net/pydb/
Source0:	http://downloads.sourceforge.net/bashdb/%{name}-%{version}.tar.lzma
BuildRequires:	python-devel
BuildArch: 	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Pydb is an enhanced command-line debugger for Python. It is based on
the standard Python debugger pdb, but has a number of added
features. It is suitable for use with DDD, a graphical debugger front
end.

%prep
%setup -q

%build
%configure2_5x --with-site-packages=%{py_sitedir}
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std
ln -sf %{py_sitedir}/%{name}/%{name}.py %{buildroot}%{_bindir}/%{name} 
rm -rf %{buildroot}%{_datadir}/emacs
rm -f %{buildroot}%{py_sitedir}/%{name}/%{name}.doc

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS ChangeLog THANKS pydb/pydb.doc
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{py_sitedir}/%{name}/%{name}.py
%{py_sitedir}/%{name}/*.py*
%{_mandir}/man1/pydb.1.*
