Summary:	Extended debugger for Python
Name:		pydb
Version:	1.26
Release:	4
License:	GPLv3
Group:		Development/Python
Url:		http://bashdb.sourceforge.net/pydb/
Source0:	http://downloads.sourceforge.net/bashdb/%{name}-%{version}.tar.bz2
BuildRequires:	python-devel
BuildArch: 	noarch

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
%makeinstall_std
ln -sf %{py_sitedir}/%{name}/%{name}.py %{buildroot}%{_bindir}/%{name} 
rm -rf %{buildroot}%{_datadir}/emacs
rm -f %{buildroot}%{py_sitedir}/%{name}/%{name}.doc
chmod 755 %{buildroot}%{py_sitedir}/%{name}/%{name}.py

%files
%defattr(-,root,root,-)
%doc README AUTHORS NEWS ChangeLog THANKS pydb/pydb.doc
%attr(755,root,root) %{_bindir}/%{name}
%{py_sitedir}/%{name}/*.py*
%{_mandir}/man1/pydb.1.*


%changelog
* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.26-2mdv2010.1
+ Revision: 543215
- rebuild for mdv 2010.1

* Mon Apr 20 2009 Lev Givon <lev@mandriva.org> 1.26-1mdv2010.0
+ Revision: 368438
- Update to 1.26.

* Mon Dec 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.25-1mdv2009.1
+ Revision: 321014
- update to new version 1.25

* Wed Dec 10 2008 Lev Givon <lev@mandriva.org> 1.24-1mdv2009.1
+ Revision: 312568
- Update to 1.24.

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.23-3mdv2009.0
+ Revision: 269017
- rebuild early 2009.0 package (before pixel changes)

* Sun Jun 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.23-2mdv2009.0
+ Revision: 216839
- Patch0: add upstream fix from the pydb's author
- new license policy

* Tue Jun 03 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.23-1mdv2009.0
+ Revision: 214572
- update to new version 1.23

* Mon May 19 2008 Lev Givon <lev@mandriva.org> 1.22-4mdv2009.0
+ Revision: 209100
- Fix problem that caused Python files to be installed in arch-specific
  directory location and revert the package to noarch.

* Sun May 11 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.22-3mdv2009.0
+ Revision: 205684
- Should not be noarch ed

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 08 2007 Lev Givon <lev@mandriva.org> 1.22-2mdv2008.1
+ Revision: 106886
- Fix path typo.

* Sat May 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.22-1mdv2008.0
+ Revision: 31461
- fix file list

  + Lev Givon <lev@mandriva.org>
    - Fix package build issues.
      Update to 1.22.


* Wed Feb 28 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.21-1mdv2007.0
+ Revision: 127154
- Import pydb

