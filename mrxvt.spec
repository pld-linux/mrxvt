Summary:	mrxvt - tabbed terminal emulator in an X Window System
Summary(pl.UTF-8):	mrxvt - emulator terminala dla X Window System
Summary(pt_BR.UTF-8):	Um emulador de vt102 colorido
Name:		mrxvt
Version:	0.5.4
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/materm/%{name}-%{version}.tar.gz
# Source0-md5:	0232c8868484751dcb931a28f0756f69
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://materm.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	utempter-devel
BuildRequires:	xorg-lib-libX11-devel
Requires:	terminfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mrxvt is a multi-tabbed color vt102 terminal emulator for X Window
System. It features multi-tab support, fast pseudo-transparent
background, user supplied XPM/JPEG/PNG images for background, tinting,
off-focus fading, text shadow, NeXT/Rxvt/Xterm/SGI/Plain style
scrollbars, XIM and multi-languages (Chinese/Korea/Japanese), and
logging.

Mrxvt does NOT require KDE or GNOME desktop environment.

%description -l pl.UTF-8
Mrxvt to wielozakładkowy emulator terminala kolorowego vt102 dla X
Window System. Obsługuje wiele zakładek, szybkie pseudoprzezroczyste
tło, wyświetlanie wybranych przez użytkownika obrazków XPM/JPEG/PNG
jako tło, cieniowanie, wygaszanie przy utracie "focusu", cienie
tekstu, paski przewijania w stylu NeXT/Rxvt/Xterm/SGI/Plain, XIM i
wiele języków (chiński/koreański/japoński) oraz logowanie.

Mrxvt NIE wymaga środowiska KDE ani GNOME.

%prep
%setup -q

%build
export LDFLAGS="%{rpmldflags} -lutempter -L%{_libdir}"
export CFLAGS="%{rpmcflags}"

%configure \
	%{?debug:--enable-debug} \
	--enable-rxvt-scroll \
	--enable-next-scroll \
	--enable-xterm-scroll \
	--enable-transparency \
	--enable-xpm-background \
	--enable-fading \
	--enable-utmp \
	--enable-wtmp \
	--enable-mousewheel \
	--enable-slipwheeling \
	--enable-smart-resize \
	--enable-ttygid \
	--enable-256-color \
	--enable-xim \
	--enable-shared \
	--enable-keepscrolling \
	--enable-xft \
	--disable-xgetdefault \
	--enable-menubar \
	--enable-backspace-key \
	--enable-delete-key \
	--enable-resources  \
	--enable-swapscreen

%{__make}
%{__cc} $CFLAGS share/scripts/settitle.c -o settitle

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install settitle $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS NEWS TODO
%doc doc/README.*
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/settitle
%{_sysconfdir}/mrxvt
%{_mandir}/man1/%{name}.1*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_pixmapsdir}/%{name}-csh.png
%{_pixmapsdir}/%{name}-root.png
