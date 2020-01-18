Name:		pps-tools
Version:	0
Release:	0.9.20120407git0deb9c%{?dist}
Summary:	LinuxPPS user-space tools

Group:		System Environment/Base
License:	GPLv2+
URL:		https://github.com/ago/pps-tools

# git clone git://github.com/ago/pps-tools; cd pps-tools
# git archive --prefix=pps-tools/ 0deb9c | xz > pps-tools-20120407git0deb9c.tar.xz
Source0:	pps-tools-20120407git0deb9c.tar.xz

%description
This package includes the LinuxPPS user-space tools.

%package devel
Summary: LinuxPPS PPSAPI header file
Group: Development/System

%description devel
This package includes the header needed to compile PPSAPI (RFC-2783)
applications.

%prep
%setup -q -n %{name}

%build
CFLAGS="$RPM_OPT_FLAGS" make %{?_smp_mflags} 

%install
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/sys}
install -m755 -t $RPM_BUILD_ROOT%{_bindir} ppsctl ppsfind ppstest ppswatch
install -p -m644 -t $RPM_BUILD_ROOT%{_includedir}/sys timepps.h

%files
%doc COPYING debian/README debian/copyright
%{_bindir}/pps*

%files devel
%doc COPYING debian/copyright
%{_includedir}/sys/timepps.h

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0-0.9.20120407git0deb9c
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0-0.8.20120407git0deb9c
- Mass rebuild 2013-12-27

* Tue Apr 02 2013 Miroslav Lichvar <mlichvar@redhat.com> 0-0.7.20120407git0deb9c
- update to 20120407git0deb9c
- move timepps.h to sys (#852950)
- include license files in devel subpackage
- remove obsolete macros

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.20120215gitac0aa6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.20120215gitac0aa6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 01 2012 Miroslav Lichvar <mlichvar@redhat.com> 0-0.4.20120215gitac0aa6
- update to 20120215gitac0aa6

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.20100413git74c32c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 09 2011 Miroslav Lichvar <mlichvar@redhat.com> 0-0.2.20100413git74c32c
- include README and copyright (#692069) 
- provide also <sys/timepps.h>

* Wed Mar 30 2011 Miroslav Lichvar <mlichvar@redhat.com> 0-0.1.20100413git74c32c
- initial release
