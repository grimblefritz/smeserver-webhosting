%define name smeserver-webhosting
%define version 0.0.3
%define release 2 

Name: %{name}
Version: %{version}	
Release: %{release}%{?dist}
Summary: allow to change php/apache settings to ibays, only yet for sme9	

Group:	SMEserver/addon
License: GNU GPL version 2	
URL:		 http://www.contribs.org
Source:	 %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArchitectures: noarch
BuildRequires:	e-smith-devtools
Requires:	e-smith-release >= 9.0
AutoReqProv: no

%description
allow to change php/apache settings to ibays, only yet for sme9

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"  >> %{name}-%{version}-filelist

%clean
cd ..
rm -rf %{name}-%{version}

%pre
%preun
%post
%postun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%changelog
* Sun Jun 01 2014 Stephane de Labrusse <stephdl@de-labrusse.fr> -0.01-1
- Initial Release
 
