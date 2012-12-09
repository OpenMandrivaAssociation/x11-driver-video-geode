# Module is dynamically loaded and references to X Server, and other
# modules resolved at runtime.
%define _disable_ld_no_undefined 1

%define name		x11-driver-video-%{chipset}
%define chipset		geode
# 20081113
%define snapshot	0
%define version		2.11.14
%define rel		1
%if %snapshot
%define release		4.%{snapshot}.%{rel}
%define distname	xf86-video-%{chipset}-%{snapshot}
%else
%define release		%{rel}
%define distname	xf86-video-%{chipset}-%{version}
%endif

Name: %{name}
Version: %{version}
Release: %{release}
Summary: X.org driver for AMD Geode GX and LX Processors
Group: System/X11
URL: http://xorg.freedesktop.org
# git://anongit.freedesktop.org/git/xorg/driver/xf86-video-geode
# git archive --format=tar --prefix=xf86-video-geode-$(date +%Y%m%d)/ master |
#   bzip2 > ../xf86-video-geode-$(date +%Y%m%d).tar.bz2
Source: http://xorg.freedesktop.org/releases/individual/driver/%{distname}.tar.bz2
Patch0: xf86-video-geode-2.9.0-scale-display.patch
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
#ExclusiveArch: %{ix86}
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.3.0
# geode replaces amd driver (renamed in order to prevent confusion after AMD/ATI
# merge), and cyrix and nsc drivers
# (http://lists.freedesktop.org/archives/xorg/2008-July/036970.html)
Provides: x11-driver-video-amd
Provides: x11-driver-video-cyrix
Provides: x11-driver-video-nsc
Obsoletes: x11-driver-video-amd
Obsoletes: x11-driver-video-cyrix <= 1.1.0-7mdv2008.1
Obsoletes: x11-driver-video-nsc <= 2.8.3-5mdv2009.0
Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
This is the X graphics driver for the AMD Geode GX and LX processors.
The GX driver features XAA and EXA support for graphics acceleration,
and the LX driver supports EXA (including compositing).  Both drivers
suppport dynamic rotation with XRandR, and Xv overlay support.

%prep
%setup -q -n %{distname}
# used on Guillemot eCafe
#%patch0 -p1 -b .sds
%if %snapshot
./autogen.sh
%endif

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO
%{_libdir}/xorg/modules/drivers/ztv_drv.so
%{_libdir}/xorg/modules/drivers/geode_drv.so




%changelog

* Thu Sep 13 2012 tv <tv> 2.11.13-4.20120913.5.mga3
+ Revision: 293571
- new snapshot (support for newer x11-server)
- rebuild for new x11-server
- rebuild for new xserver
- rebuild for new xserver

* Wed Jun 06 2012 tmb <tmb> 2.11.13-4.mga3
+ Revision: 256388
- rebuild for core/release

* Sat Jun 02 2012 tv <tv> 2.11.13-3.mga3
+ Revision: 253189
- rebuild b/c of ia32 failure
- rebuild b/c of ia32 failure

* Wed May 30 2012 tv <tv> 2.11.13-2.mga3
+ Revision: 249945
- rebuild for new X.org server

* Tue Jan 17 2012 tv <tv> 2.11.13-1.mga2
+ Revision: 197669
- new release

* Tue Dec 06 2011 tmb <tmb> 2.11.12-4.mga2
+ Revision: 177733
- submit to core/release

* Mon Nov 28 2011 tmb <tmb> 2.11.12-3.mga2
+ Revision: 173769
- rebuild against new x11-server

* Fri Mar 04 2011 tv <tv> 2.11.12-2.mga1
+ Revision: 64442
- rebuild for new xserver-1.10

* Fri Feb 18 2011 tv <tv> 2.11.12-1.mga1
+ Revision: 53915
- new release

* Fri Feb 11 2011 tmb <tmb> 2.11.11-1.mga1
+ Revision: 50209
- imported package x11-driver-video-geode

