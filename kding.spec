Summary:	KDE frontend for Ding, a dictionary lookup program
Summary(pl.UTF-8):   Frontend KDE dla Dinga - programu do wyszukiwania słów w słownikach
Name:		kding
Version:	0.3
Release:	0.1
License:	GPL v2
Group:		Applications/Dictionaries
Source0:	http://www.rexi.org/downloads/kding/%{name}-%{version}.tar.bz2
# Source0-md5:	825bc68ea7fb123a18d54d42b1fd2876
Patch0:		%{name}-desktop.patch
URL:		http://www.rexi.org/software/kding/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDing is a KDE frontend for Ding, a dictionary lookup program. It sits
in KDE's system tray and can translate the current clipboard content.
Users can also enter single words or phrases for translation. It is
intended to be used for translating between German and English, but
can be used with every language for which a word list is available for
Ding.

%description -l pl.UTF-8
KDing to frontend KDE dla Dinga - programu do wyszukiwania słów w
słownikach. Umieszcza się w zasobniku systemowym KDE i potrafi
tłumaczyć aktualną zawartość schowka. Użytkownicy mogą także wpisywać
pojedyncze słowa lub frazy do tłumaczenia. Program był tworzony z
myślą o tłumaczeniu między językiem niemieckim a angielskim, ale może
być używany z każdym językiem, dla którego jest dostępna lista słów
dla Dinga.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	shelldesktopdir=%{_desktopdir} \

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/apps/%{name}.png
%{_datadir}/apps/%{name}
