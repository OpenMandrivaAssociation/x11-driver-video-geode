#   Module is dynamically loaded and references to X Server, and other
# modules resolved at runtime.
%define _disable_ld_no_undefined 1

Name: x11-driver-video-geode
Version: 2.9.0
Release: %mkrel 2
Summary: The X.org driver for AMD Geode GX and LX Processors
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-geode-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
ExclusiveArch: %{ix86}
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
# filename conflict was fixed in this version
Conflicts: x11-driver-video-amd < 2.7.7.7-2mdv

%description
This is the X graphics driver for the AMD Geode GX and LX processors.
The GX driver features XAA and EXA support for graphics acceleration,
and the LX driver supports EXA (including compositing).  Both drivers
suppport dynamic rotation with XRandR, and Xv overlay support.

%prep
%setup -q -n xf86-video-geode-%{version}

%build
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
