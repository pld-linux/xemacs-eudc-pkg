Summary:	Emacs Unified Directory Client (LDAP, PH)
Summary(pl):	Emacs Unified Directory Client (LDAP, PH)
Name:		xemacs-eudc-pkg
%define 	srcname	eudc
Version:	1.34
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
Patch0:		xemacs-eudc-pkg-info.patch
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-fsf-compat-pkg
Requires:	xemacs-base-pkg
Requires:	xemacs-bbdb-pkg
URL:		http://www.xemacs.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl 

%prep
%setup -q -c
%patch0 -p1

%build
(cd man/eudc; awk '/^\\input texinfo/ {print FILENAME}' * | xargs makeinfo)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages,%{_infodir}}

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
mv -f  $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info/*.info* $RPM_BUILD_ROOT%{_infodir}
rm -fr $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*.info* \
	lisp/eudc/ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc lisp/eudc/ChangeLog.gz 
%{_infodir}/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
