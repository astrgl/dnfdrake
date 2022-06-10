%define name dnfdrake
%define version 3.1.2
%define release %mkrel 3

Name: %{name}
Version: %{version}
Release: %{release}
Packager: Astragalo
License: GPL
Group: Graphical desktop/KDE
Summary: DnfDrake  is a frontend for DNF
Url: https://mib.pianetalinux.org/
Source: %{name}-%version.tar.gz
Requires:	sudo
Requires: gambas3-runtime 
Requires: gambas3-gb-form
Requires: gambas3-gb-image
Requires: gambas3-gb-gui
Requires: gambas3-gb-qt5
Requires: gambas3-gb-gtk3
Requires: gambas3-gb-dbus
Requires: hicolor-icon-theme
Requires: dnf-utils
Requires:  python-dnf-plugin-versionlock
BuildArch:	noarch
Conflicts:  gambas3-runtime  > 3.16.3


BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
DnfDrake  is a frontend for DNF package manager
Powerful like a terminal and simple like a GUI!

%prep
%setup -n dnfdrake

%install
rm -rf %{buildroot}

mkdir %buildroot
mkdir %buildroot/usr
mkdir %buildroot/%_bindir
mkdir %buildroot/%_datadir
mkdir %buildroot/%_datadir/applications
mkdir %buildroot/%_datadir/icons
mkdir %buildroot/%_datadir/icons/hicolor
mkdir %buildroot/%_datadir/icons/hicolor/32x32
mkdir %buildroot/%_datadir/icons/hicolor/32x32/apps
mkdir %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake.gambas %buildroot/%_bindir/
install -Dm 755 dnfdraketray.gambas %buildroot/%_bindir/
install -Dm 755 dnfdrake.desktop %buildroot/%_datadir/applications
install -Dm 755 license %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-COMMAND %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-*-* %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdraketray.gambas.desktop %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake.svg  %buildroot/%_datadir/icons/hicolor/32x32/apps

%clean
rm -rf %{buildroot}

%files
%_bindir/dnfdrake.gambas
%_bindir/dnfdraketray.gambas
%_datadir/applications/dnfdrake.desktop
%{_datadir}/icons/hicolor/32x32/apps/dnfdrake.svg
%_datadir/dnfdrake/license
%_datadir/dnfdrake/dnfdrake-COMMAND
%_datadir/dnfdrake/dnfdrake-*-*
%_datadir/dnfdrake/dnfdraketray.gambas.desktop
