Summary:	mrxvt - tabbed terminal emulator in an X Window System
Summary(pl):	mrxvt - emulator terminala dla X Window System
Summary(pt_BR):	Um emulador de vt102 colorido
Name:		mrxvt
Version:	0.3.6
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/materm/%{name}-%{version}.tgz
# Source0-md5:	c05153e69ecc3c3156c5e32b2356b2e6
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
system. It features multi-tab support, fast pseudo-transparent
background, user supplied XPM/JPEG/PNG images for background, tinting,
off-focus fading, text shadow, NeXT/Rxvt/Xterm/SGI/Plain style
scrollbars, XIM and multi-languages (Chinese/Korea/Japanese), and
logging.

Mrxvt does NOT require KDE or GNOME desktop environment.

%prep
%setup -q

%build
LDFLAGS="%{rpmldflags} -lutempter -L%{_libdir}"
export LDFLAGS
%configure \
	--enable-everything \
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
	--enable-xgetdefault \
	--enable-xgetdefault \
	--enable-xft \
	--enable-menubar \
	--enable-backspace-key \
	--enable-delete-key \
	--enable-resources  \
	--enable-swapscreen

CFLAGS="%{rpmcflags}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.configure FAQ AUTHORS TODO
%doc doc/README.* doc/TIPS doc/xdefaults-sample.txt doc/xterm.seq
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png