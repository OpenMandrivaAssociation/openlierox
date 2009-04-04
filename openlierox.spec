Name:		openlierox
Version:	0.57_beta8
Release:	%mkrel 1
Source:		OpenLieroX_%{version}.src.tar.bz2
URL:		http://openlierox.sourceforge.net/
Group:		Games/Arcade
License:	LGPL+
Summary:	Extremely addictive realtime worms shoot-em-up
BuildRoot:	%{_tmppath}/%{name}-%{version}
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

%{__mkdir_p} %{buildroot}%{_iconsdir}
cp -p %{buildroot}%{_datadir}/OpenLieroX/data/icon.png %{buildroot}%{_iconsdir}/%{name}.png

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

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc COPYING.LIB VERSION doc
%{_datadir}/OpenLieroX/
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
