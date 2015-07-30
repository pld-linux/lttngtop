Summary:	Interface for reading and browsing LTTng traces
Summary(pl.UTF-8):	Interfejs do odczytu i przeglądania śladów LTTng
Name:		lttngtop
Version:	0.3
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://lttng.org/files/lttngtop/%{name}-%{version}.tar.bz2
# Source0-md5:	ff5e0d282d6571746f29ce1cbef6d773
URL:		http://lttng.org/
BuildRequires:	babeltrace-devel
BuildRequires:	glib2-devel >= 1:2.22.0
BuildRequires:	libuuid-devel
BuildRequires:	lttng-tools-devel
BuildRequires:	ncurses-devel
BuildRequires:	ncurses-ext-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
Requires:	glib2 >= 1:2.22.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# babeltrace module with callbacks to lttngtop binary
%define		skip_post_check_so	libbabeltrace-lttngtop-live.so.*

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
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libbabeltrace-lttngtop-live.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/lttngtop
%attr(755,root,root) %{_bindir}/lttngtoptrace
%attr(755,root,root) %{_libdir}/libbabeltrace-lttngtop-live.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbabeltrace-lttngtop-live.so.0
%attr(755,root,root) %{_libdir}/libbabeltrace-lttngtop-live.so
%{_mandir}/man1/lttngtop.1*
%{_mandir}/man1/lttngtoptrace.1*
