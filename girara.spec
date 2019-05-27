#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : girara
Version  : 0.3.2
Release  : 1
URL      : https://github.com/pwmt/girara/archive/0.3.2.tar.gz
Source0  : https://github.com/pwmt/girara/archive/0.3.2.tar.gz
Summary  : User interface library focused on simplicity and minimalism
Group    : Development/Tools
License  : BSD-3-Clause
Requires: girara-lib = %{version}-%{release}
Requires: girara-license = %{version}-%{release}
Requires: girara-locales = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : doxygen
BuildRequires : glib-dev
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(json-c)

%description
girara - user interface library
===============================
girara is a library that implements a user interface that focuses on simplicity
and minimalism. It consists of three main components: The view is a widget that
represents the actual application (e.g.: a web site or a document). The input
bar is used to execute commands of the application, while the status bar
notifies the user with current information. It is designed to replace and the
enhance the user interface that is used by zathura.

%package dev
Summary: dev components for the girara package.
Group: Development
Requires: girara-lib = %{version}-%{release}
Provides: girara-devel = %{version}-%{release}
Requires: girara = %{version}-%{release}
Requires: girara = %{version}-%{release}

%description dev
dev components for the girara package.


%package lib
Summary: lib components for the girara package.
Group: Libraries
Requires: girara-license = %{version}-%{release}

%description lib
lib components for the girara package.


%package license
Summary: license components for the girara package.
Group: Default

%description license
license components for the girara package.


%package locales
Summary: locales components for the girara package.
Group: Default

%description locales
locales components for the girara package.


%prep
%setup -q -n girara-0.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1558966606
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/girara
cp LICENSE %{buildroot}/usr/share/package-licenses/girara/LICENSE
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang libgirara-gtk3-3

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/girara/callbacks.h
/usr/include/girara/commands.h
/usr/include/girara/completion.h
/usr/include/girara/config.h
/usr/include/girara/datastructures.h
/usr/include/girara/entry.h
/usr/include/girara/girara-version.h
/usr/include/girara/girara.h
/usr/include/girara/input-history.h
/usr/include/girara/log.h
/usr/include/girara/macros.h
/usr/include/girara/session.h
/usr/include/girara/settings.h
/usr/include/girara/shortcuts.h
/usr/include/girara/statusbar.h
/usr/include/girara/template.h
/usr/include/girara/types.h
/usr/include/girara/utils.h
/usr/lib64/libgirara-gtk3.so
/usr/lib64/pkgconfig/girara-gtk3.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgirara-gtk3.so.3
/usr/lib64/libgirara-gtk3.so.3.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/girara/LICENSE

%files locales -f libgirara-gtk3-3.lang
%defattr(-,root,root,-)

