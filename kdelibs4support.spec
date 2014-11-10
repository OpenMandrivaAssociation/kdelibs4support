%define major 5
%define libname %mklibname KF5KDELibs4Support %{major}
%define devname %mklibname KF5KDELibs4Support -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kdelibs4support
Version: 5.4.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/portingAids/%{name}-%{version}.tar.xz
Summary: Porting aid from KDELibs4
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: qt5-designer
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
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
BuildRequires: cmake(KDED)
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
BuildRequires: pkgconfig(NetworkManager)
BuildRequires: pkgconfig(libnm-util)
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
Development files for the KDE Frameworks 5 Delibs4support library

%prep
%setup -q
%apply_patches
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}

%find_lang kdelibs4support

# The version of FindGettext.cmake included here is obsolete and broken
# (causes Baloo build to fail).
# Since we get a working version from cmake itself, we can and should
# just remove it.
rm -f %{buildroot}%{_libdir}/cmake/KF5KDELibs4Support/FindGettext.cmake

%files -f kdelibs4support.lang
%{_sysconfdir}/xdg/colors
%{_sysconfdir}/xdg/kdebug*
%{_sysconfdir}/xdg/ksslcalist
%{_bindir}/kdebugdialog5
%{_datadir}/kservices5/*
%{_datadir}/kservicetypes5/*
%{_datadir}/kf5/locale
%{_datadir}/kf5/widgets/pics/*
%{_datadir}/locale/kf5_all_languages
%{_libdir}/libexec/kf5/*
%{_libdir}/plugins/*.so
%{_libdir}/plugins/designer/*.so
%{_libdir}/plugins/kf5/kded/*.so
%{_libdir}/plugins/kf5/kio/*.so
%{_datadir}/dbus-1/*/*
%{_datadir}/kf5/kdoctools/*
%{_datadir}/kf5/kssl
%{_mandir}/man1/*
%doc %{_docdir}/HTML/en/kdebugdialog5
%lang(de) %doc %{_docdir}/HTML/de/kdebugdialog5
%lang(nl) %doc %{_docdir}/HTML/nl/kdebugdialog5
%lang(pt_BR) %doc %{_docdir}/HTML/pt_BR/kdebugdialog5
%lang(sv) %doc %{_docdir}/HTML/sv/kdebugdialog5
%lang(uk) %doc %{_docdir}/HTML/uk/kdebugdialog5
%lang(de) %{_mandir}/de/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(pt_BR) %{_mandir}/pt_BR/man1/*
%lang(sv) %{_mandir}/sv/man1/*
%lang(uk) %{_mandir}/uk/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_bindir}/kf5-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KDELibs4
%{_libdir}/cmake/KF5*
