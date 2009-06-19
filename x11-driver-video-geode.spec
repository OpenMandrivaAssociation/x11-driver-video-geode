#   Module is dynamically loaded and references to X Server, and other
# modules resolved at runtime.
%define _disable_ld_no_undefined 1

%define name		x11-driver-video-%{chipset}
%define chipset		geode
# 20081113
%define snapshot	0
%define version		2.11.3
%define rel		1
%if %snapshot
%define release		%mkrel 2.%{snapshot}.%{rel}
%define distname	xf86-video-%{chipset}-%{snapshot}
%else
%define release		%mkrel %{rel}
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
ExclusiveArch: %{ix86}
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
# geode replaces amd driver (renamed in order to prevent confusion after AMD/ATI merge),
# and cyrix and nsc drivers (http://lists.freedesktop.org/archives/xorg/2008-July/036970.html)
Provides: x11-driver-video-amd 
Provides: x11-driver-video-cyrix
Provides: x11-driver-video-nsc
Obsoletes: x11-driver-video-amd
Obsoletes: x11-driver-video-cyrix <= 1.1.0-7mdv2008.1
Obsoletes: x11-driver-video-nsc <= 2.8.3-5mdv2009.0

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
autoreconf -v --install
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO
%{_libdir}/xorg/modules/drivers/ztv_drv.la
%{_libdir}/xorg/modules/drivers/ztv_drv.so
%{_libdir}/xorg/modules/drivers/geode_drv.la
%{_libdir}/xorg/modules/drivers/geode_drv.so
