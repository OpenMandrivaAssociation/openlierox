Name:		openlierox
Version:	0.58_rc3
Release:	%mkrel 1
Source:		OpenLieroX_%{version}.src.tar.bz2
URL:		http://openlierox.sourceforge.net/
Group:		Games/Arcade
License:	LGPLv2
Summary:	Extremely addictive realtime worms shoot-em-up
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	libhawknl-devel
BuildRequires:	libgd-devel
BuildRequires:	zlib-devel
BuildRequires:	libxml2-devel
BuildRequires:	libzip-devel
BuildRequires:	curl-devel
Requires:	%{name}-gamedata = %{version}-%{release}

%description
OpenLierox is an extremely addictive realtime worms shoot-em-up backed
by an active gamers community. Dozens of levels and mods are available
to provide endless gaming pleasure.

%package	gamedata
Summary:	Game data for %{name}
License:	LGPLv2
Group:		Games/Arcade
# We split game data to separate package to make it noarch and thus save
# bandwidth and space on distribution media.
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}

%description	gamedata
Game data for %{name}.

%prep
%setup -q -n OpenLieroX

%build
SYSTEM_DATA_DIR=%{_gamesdatadir} \
BIN_DIR=%{_gamesbindir} \
./compile.sh

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_gamesbindir}
SYSTEM_DATA_DIR=%{buildroot}%{_gamesdatadir} \
BIN_DIR=%{buildroot}%{_gamesbindir} \
DOC_DIR=%{buildroot}%{_docdir} \
	./install.sh
%__chmod -R o+rX %{buildroot}%{_gamesdatadir}/OpenLieroX
%__rm -rf %{buildroot}%{_docdir}

%__mkdir_p %{buildroot}%{_iconsdir}
%__cp -p %{buildroot}%{_gamesdatadir}/OpenLieroX/data/icon.png %{buildroot}%{_iconsdir}/%{name}.png

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=OpenLieroX
Comment=Extremely addictive realtime worms shoot-em-up
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING.LIB VERSION doc
%{_gamesbindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png

%files gamedata
%defattr(-,root,root)
%{_gamesdatadir}/OpenLieroX

