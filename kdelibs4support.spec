%define major 5
%define libname %mklibname KF5KDELibs4Support %{major}
%define devname %mklibname KF5KDELibs4Support -d
%define debug_package %{nil}

Name: kdelibs4support
Version: 4.99.0
Release: 3
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/%{version}/%{name}-%{version}.tar.xz
Patch0: kdelibs4support-find-NetworkManager.patch
Summary: Porting aid from KDELibs4
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(FFmpeg)
BuildRequires: cmake(Eigen2)
BuildRequires: cmake(Blitz)
BuildRequires: cmake(OpenEXR)
BuildRequires: cmake(GStreamer)
BuildRequires: cmake(LCMS)
BuildRequires: cmake(GObject)
BuildRequires: cmake(Flac)
BuildRequires: cmake(Xmms)
BuildRequires: cmake(AGG)
BuildRequires: cmake(QImageBlitz)
BuildRequires: cmake(Xine)
BuildRequires: cmake(ENCHANT)
BuildRequires: cmake(PCRE)
BuildRequires: cmake(USB)
BuildRequires: cmake(BlueZ)
BuildRequires: cmake(QCA2)
BuildRequires: cmake(LibArt)
BuildRequires: cmake(Sqlite)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(NetworkManager)
BuildRequires: cmake(OpenSSL)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5DesignerPlugin)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5UnitConversion)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(Qt5)
BuildRequires: pkgconfig(sm)
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

%description
Porting aid from KDELibs4

%package -n %{libname}
Summary: Porting aid from KDELibs4
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Porting aid from KDELibs4

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Delibs4support library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 Delibs4support library

%prep
%setup -q
%apply_patches
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}

%files
%{_sysconfdir}/xdg/colors
%{_sysconfdir}/xdg/kdebug*
%{_sysconfdir}/xdg/ksslcalist
%{_bindir}/kdebugdialog5
%{_datadir}/kservices5/*
%{_datadir}/kservicetypes5/*
%{_datadir}/kf5/locale
%{_datadir}/kf5/widgets/pics/*
%{_datadir}/locale/kf5_all_languages
%{_datadir}/locale/*/kf5_entry.desktop
%{_libdir}/libexec/kf5/*
%{_libdir}/plugins/*.so
%{_libdir}/plugins/designer/*.so
%{_datadir}/dbus-1/*/*
%{_datadir}/kf5/kdoctools/*
%{_datadir}/kf5/kssl
%{_mandir}/man1/*
%doc %{_docdir}/HTML/en/kdebugdialog5

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_bindir}/kf5-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KDELibs4
%{_libdir}/cmake/KF5*
