Summary:	Extremely addictive realtime worms shoot-em-up
Name:		openlierox
Version:	0.58_rc3
Release:	3
Group:		Games/Arcade
License:	LGPLv2
URL:		https://openlierox.sourceforge.net/
Source:		OpenLieroX_%{version}.src.tar.bz2
Patch0:		openlierox-0.58_rc1-curl.patch
Patch1:		openlierox-0.58_rc3-fstat.patch
Patch2:		openlierox-0.58_rc3-gcc4.7.patch
BuildRequires:	libgd-devel
BuildRequires:	libhawknl-devel
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libzip)
BuildRequires:	pkgconfig(zlib)
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
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
SYSTEM_DATA_DIR=%{_gamesdatadir} \
BIN_DIR=%{_gamesbindir} \
./compile.sh

%install
mkdir -p %{buildroot}%{_gamesbindir}
SYSTEM_DATA_DIR=%{buildroot}%{_gamesdatadir} \
BIN_DIR=%{buildroot}%{_gamesbindir} \
DOC_DIR=%{buildroot}%{_docdir} \
	./install.sh

chmod -R o+rX %{buildroot}%{_gamesdatadir}/OpenLieroX
rm -rf %{buildroot}%{_docdir}

mkdir -p %{buildroot}%{_iconsdir}
cp -p %{buildroot}%{_gamesdatadir}/OpenLieroX/data/icon.png %{buildroot}%{_iconsdir}/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=OpenLieroX
Comment=Extremely addictive realtime worms shoot-em-up
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%files
%doc COPYING.LIB VERSION doc
%{_gamesbindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png

%files gamedata
%{_gamesdatadir}/OpenLieroX

