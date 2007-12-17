Name:		openlierox
Version:	0.57_beta3
Release:	%mkrel 1
Source:		OpenLieroX_%{version}.src.tar.bz2
URL:		http://openlierox.sourceforge.net/
Group:		Games/Arcade
License:	LGPL+
Summary:	Extremely addictive realtime worms shoot-em-up
BuildRequires:	libSDL-devel libSDL_mixer-devel libSDL_image-devel
BuildRequires:	libhawknl-devel libgd-devel zlib-devel libxml2-devel
%description
OpenLierox is an extremely addictive realtime worms shoot-em-up backed
by an active gamers community. Dozens of levels and mods are available
to provide endless gaming pleasure.

%prep
%setup -q -n OpenLieroX

%build
./compile.sh

%install
%{__rm} -Rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
SYSTEM_DATA_DIR=%{buildroot}%{_datadir} \
BIN_DIR=%{buildroot}%{_bindir} \
DOC_DIR=%{buildroot}%{_docdir} \
	./install.sh
%{__chmod} -R o+rX %{buildroot}%{_datadir}/OpenLieroX
%{__rm} -Rf %{buildroot}%{_docdir}

%{__mkdir_p} %{buildroot}%{_datadir}/applications
%{__cat} > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=Extremely addictive realtime worms shoot-em-up
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
EOF

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%doc COPYING.LIB VERSION doc
%{_datadir}/OpenLieroX/
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
