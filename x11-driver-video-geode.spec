%define _disable_ld_no_undefined 1

Summary:	X.org driver for AMD Geode GX and LX Processors
Name:		x11-driver-video-geode
Version:	2.11.15
Release:	3
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-geode-%{version}.tar.bz2
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)
# geode replaces amd driver (renamed in order to prevent confusion after AMD/ATI
# merge), and cyrix and nsc drivers
# (http://lists.freedesktop.org/archives/xorg/2008-July/036970.html)
Provides:	x11-driver-video-amd
Provides:	x11-driver-video-cyrix
Provides:	x11-driver-video-nsc

%description
This is the X graphics driver for the AMD Geode GX and LX processors.
The GX driver features XAA and EXA support for graphics acceleration,
and the LX driver supports EXA (including compositing).  Both drivers
suppport dynamic rotation with XRandR, and Xv overlay support.

%prep
%setup -qn xf86-video-geode-%{version}
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README TODO
%{_libdir}/xorg/modules/drivers/ztv_drv.so
%{_libdir}/xorg/modules/drivers/geode_drv.so

