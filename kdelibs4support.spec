%define major 5
%define libname %mklibname KF5KDELibs4Support %{major}
%define devname %mklibname KF5KDELibs4Support -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

# We don't care about Windoze specific stuff...
%global __requires_exclude ^.*cmake\\(KDEWin\\).*$

Name: kdelibs4support
Version: 5.116.0
Release: 1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/portingAids/%{name}-%{version}.tar.xz
Source1: %{name}.rpmlintrc
Summary: Porting aid from KDELibs4
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: qt5-designer
BuildRequires: appstream
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: cmake(Qt5Designer)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5PrintSupport)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5DesignerPlugin)
BuildRequires: cmake(KF5Emoticons)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KDED)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5UnitConversion)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5Completion)
BuildRequires: docbook-dtd42-xml
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(libnm)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(libntrack)
BuildRequires: perl(URI::Escape)
BuildRequires: rootcerts
# cmake files act up when running into obsolete-ish Qt5Declarative
BuildConflicts:	pkgconfig(Qt5Declarative)
Requires: %{libname} = %{EVRD}
Requires: rootcerts

%description
Porting aid from KDELibs4.

%package -n %{libname}
Summary: Porting aid from KDELibs4
Group: System/Libraries

%description -n %{libname}
Porting aid from KDELibs4.

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Delibs4support library
Group: Development/KDE and Qt
Requires: %{name} = %{EVRD}
Requires: %{libname} = %{EVRD}
# List of dependencies is from KF5KDELibs4SupportConfig.cmake (search for find_dependency)
Requires: cmake(KF5Auth)
Requires: cmake(KF5ConfigWidgets)
Requires: cmake(KF5CoreAddons)
Requires: cmake(KF5Crash)
Requires: cmake(KF5DesignerPlugin)
Requires: cmake(KF5DocTools)
Requires: cmake(KF5Emoticons)
Requires: cmake(KF5GuiAddons)
Requires: cmake(KF5IconThemes)
Requires: cmake(KF5ItemModels)
Requires: cmake(KF5Init)
Requires: cmake(KF5Notifications)
Requires: cmake(KF5Parts)
Requires: cmake(KF5TextWidgets)
Requires: cmake(KF5UnitConversion)
Requires: cmake(KF5WindowSystem)
Requires: cmake(Qt5DBus)
Requires: cmake(Qt5Xml)
Requires: cmake(Qt5PrintSupport)

%description -n %{devname}
Development files for the KDE Frameworks 5 Delibs4support library.

%prep
%autosetup -p1
# (tpg) fix some strange bug on i586
%global optflags %optflags -Wno-c++11-narrowing

%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kdelibs4support --with-html --with-man --all-name

# The version of FindGettext.cmake included here is obsolete and broken
# (causes Baloo build to fail).
# Since we get a working version from cmake itself, we can and should
# just remove it.
rm -f %{buildroot}%{_libdir}/cmake/KF5KDELibs4Support/FindGettext.cmake

## use ca-certificates' ca-bundle.crt, symlink as what most other
## distros do these days (http://bugzilla.redhat.com/521902)
if [  -f %{buildroot}%{_kde5_datadir}/kf5/kssl/ca-bundle.crt -a -f /etc/pki/tls/certs/ca-bundle.crt ]; then
    ln -sf /etc/pki/tls/certs/ca-bundle.crt %{buildroot}%{_kde5_datadir}/kf5/kssl/ca-bundle.crt
fi

# Let's not conflict with kio...
rm -f %{buildroot}%{_docdir}/HTML/*/kcontrol5/webshortcuts/index.cache.bz2

%files -f kdelibs4support.lang
%{_sysconfdir}/xdg/colors
%{_sysconfdir}/xdg/kdebug*
%{_sysconfdir}/xdg/ksslcalist
%{_bindir}/kf5-config
%{_bindir}/kdebugdialog5
%{_datadir}/kservices5/*
%{_datadir}/kservicetypes5/*
%{_datadir}/kf5/locale
%{_datadir}/kf5/widgets/pics/*
%{_datadir}/locale/kf5_all_languages
%{_libdir}/libexec/kf5/*
%{_libdir}/qt5/plugins/*.so
%{_libdir}/qt5/plugins/designer/*.so
%{_libdir}/qt5/plugins/kf5/kded/*.so
%{_libdir}/qt5/plugins/kf5/kio/*.so
%{_datadir}/kf5/kdoctools/*
%{_datadir}/kf5/kssl
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KDELibs4
%{_libdir}/cmake/KF5*
%{_datadir}/dbus-1/*/*
