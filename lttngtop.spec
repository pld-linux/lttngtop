Summary:	Interface for reading and browsing LTTng traces
Summary(pl.UTF-8):	Interfejs do odczytu i przeglądania śladów LTTng
Name:		lttngtop
Version:	0.2
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://lttng.org/files/lttngtop/%{name}-%{version}.tar.bz2
# Source0-md5:	6d957f2395c3a2fd550822b81252e9e7
URL:		http://lttng.org/
BuildRequires:	babeltrace-devel
BuildRequires:	glib2-devel >= 1:2.22.0
BuildRequires:	libuuid-devel
BuildRequires:	ncurses-devel
BuildRequires:	ncurses-ext-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
Requires:	glib2 >= 1:2.22.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LTTngTop is an ncurses interface for reading and browsing traces
recorded by the LTTng tracer and displaying various statistics. As of
now, the CPU usage, per file/process I/O bandwidth and perf counters
are displayed. This version currently only supports offline traces,
but a live version is in alpha and will be available for testing soon.

%description -l pl.UTF-8
LTTngTop to oparty na ncurses interfejs do odczytu i przeglądania
śladów zapisanych przez LTTng oraz wyświetlania różnych statystyk.
Obecnie wyświetlane jest wykorzystanie procesora, wykorzystanie we/wy
dla pliku/procesu oraz liczniki perf. Ta wersja obsługuje tylko ślady
offline, ale wersja działająca na żywo jest w stadium alfa i będzie
wkrótce dostępna do testów.

%prep
%setup -q

%build
CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses"
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/lttngtop
%{_mandir}/man1/lttngtop.1*
