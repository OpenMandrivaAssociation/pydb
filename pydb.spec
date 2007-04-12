Summary:	Extended debugger for python
Name:		pydb
Version:	1.21
Release:	%mkrel 1
License:	GPL
Group:		Development/Python
Url:		http://bashdb.sourceforge.net/pydb/
Source0:	http://downloads.sourceforge.net/bashdb/%{name}-%{version}.tar.bz2
BuildRequires:	python-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
An enhanced Python command-line debugger Pydb is a command-line
debugger for Python. It is based on the standard Python debugger pdb,
but has a number of added features. Particularly, it is suitable for
use with DDD, a graphical debugger front end.

%prep
%setup -q

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS ChangeLog THANKS
%dir %{_libdir}/python2.5/site-packages/%{name}
%attr(755,root,root) %{_bindir}/%{name}
%{_libdir}/python2.5/site-packages/%{name}/*.py*
%{_libdir}/python2.5/site-packages/%{name}/*.doc
#%exclude %{_datadir}/emacs/site-lisp/*.el*
%{_mandir}/man1/pydb.1.bz2


