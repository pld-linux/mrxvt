Summary:	mrxvt - tabbed terminal emulator in an X Window System
Summary(pl):	mrxvt - emulator terminala dla X Window System
Summary(pt_BR):	Um emulador de vt102 colorido
Name:		mrxvt
Version:	0.3.13
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/materm/%{name}-%{version}.tar.gz
# Source0-md5:	880bc53d17af9f177cc68d7ce1abd1a2
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://materm.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	utempter-devel
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

%description -l pl
Mrxvt to wielozak³adkowy emulator terminala kolorowego vt102 dla X
Window System. Obs³uguje wiele zak³adek, szybkie pseudoprzezroczyste
t³o, wy¶wietlanie wybranych przez u¿ytkownika obrazków XPM/JPEG/PNG
jako t³o, cieniowanie, wygaszanie przy utracie "focusu", cienie
tekstu, paski przewijania w stylu NeXT/Rxvt/Xterm/SGI/Plain, XIM i
wiele jêzyków (chiñski/koreañski/japoñski) oraz logowanie.

Mrxvt NIE wymaga ¶rodowiska KDE ani GNOME.

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
%{__cc} $CFLAGS doc/settitle.c -o settitle

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
%doc ChangeLog README README.configure FAQ AUTHORS TODO
%doc doc/README.* doc/TIPS doc/xdefaults-sample.txt doc/xterm.seq doc/menu
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/settitle
%{_mandir}/man1/%{name}.1*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_pixmapsdir}/%{name}-csh.png
%{_pixmapsdir}/%{name}-root.png
