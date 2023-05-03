Name: dnfdrake
Version: 3.6.7
Release: 1
Packager: Astragalo
License: GPL
Group: Graphical desktop/KDE
Summary: DnfDrake  is a frontend for DNF
Url: https://mib.pianetalinux.org/
Source: %{name}-%{version}.tar.gz

Requires: sudo
Requires: gambas3-runtime
Requires: gambas3-gb-form
Requires: gambas3-gb-image
Requires: gambas3-gb-gui
Requires: gambas3-gb-qt5
Requires: gambas3-gb-gtk3
Requires: gambas3-gb-dbus
Requires: gambas3-gb-form-stock
Requires: hicolor-icon-theme
Requires: dnf-utils
Requires: lsb-release
Requires: createrepo_c
Requires: python-dnf-plugin-versionlock
Requires: xrandr
Requires:dnfdraketray

BuildArch: noarch

Conflicts:  gambas3-runtime  > 3.18.1

%description
DnfDrake  is a frontend for DNF package manager
Powerful like a terminal and simple like a GUI!

%prep
%autosetup -n %{name}

%build
gbc3
sleep 2
gba3


%install

install -Dm 755 dnfdrake.gambas -t %{buildroot}/%{_bindir}/
install -Dm 755 FILE-EXTRA/dnfdrake.desktop -t %buildroot/%_datadir/applications/
install -Dm 644 FILE-EXTRA/license -t %{buildroot}/%{_datadir}/dnfdrake/
install -Dm 644 FILE-EXTRA/dnfdrake-COMMAND -t %{buildroot}/%{_datadir}/dnfdrake/
install -Dm 644 FILE-EXTRA/dnfdrake-*-* -t %{buildroot}/%{_datadir}/dnfdrake/
install -Dm 644 dnfdrake.svg  -t %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/

%files
%{_bindir}/dnfdrake.gambas
%{_datadir}/applications/dnfdrake.desktop
%{_datadir}/icons/hicolor/32x32/apps/dnfdrake.svg
%{_datadir}/dnfdrake/license
%{_datadir}/dnfdrake/dnfdrake-COMMAND
%{_datadir}/dnfdrake/dnfdrake-*-*
