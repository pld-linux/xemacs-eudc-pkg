### Comment
# This file is modified automatically by 'xemacs-adapter' script
# from PLD-project CVS repository: cvs.pld.org.pl, module SPECS
# For more details see comments in this script
### EndComment

Summary: 	Emacs Unified Directory Client (LDAP, PH).
Summary(pl):	Emacs Unified Directory Client (LDAP, PH).

Name:    	xemacs-eudc-pkg
%define 	srcname	eudc
Version: 	1.31
Release:	1

Patch0: 	xemacs-eudc-pkg-info.patch

### Preamble
License:	GPL
Group:    	Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
URL:      	http://www.xemacs.org
Source:   	ftp://ftp.xemacs.org/packages/%{srcname}-%{version}-pkg.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires: 	xemacs
Requires: 	xemacs-fsf-compat-pkg
Requires: 	xemacs-base-pkg
Requires: 	xemacs-bbdb-pkg
Prereq:  	/usr/sbin/fix-info-dir
### EndPreamble

%description


%description -l pl 


### Main
%prep
%setup -q -c
%patch0 -p1

%build
(cd man/eudc; awk '/^\\input texinfo/ {print FILENAME}' * | xargs makeinfo)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
install -d $RPM_BUILD_ROOT%{_infodir}
mv -f  $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info/*.info* $RPM_BUILD_ROOT%{_infodir}
rm -fr $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info
gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*.info*
gzip -9nf lisp/eudc/ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT
### EndMain

### PrePost
%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
### EndPrePost

### Files
%files
%defattr(644,root,root,755)
%{_infodir}/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
%doc lisp/eudc/ChangeLog.gz 
### EndFiles
