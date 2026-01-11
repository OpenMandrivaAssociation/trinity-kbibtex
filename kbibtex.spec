%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg kbibtex
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Epoch:			%{tde_epoch}
Version:        0.2.3
Release:		%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:        A BibTeX editor for TDE
Group:          Applications/Internet
URL:            http://www.unix-ag.uni-kl.de/~fischer/kbibtex/download.html

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/office/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DBUILD_DOC=ON
BuildOption:    -DBUILD_TRANSLATIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig

# ACL support
BuildRequires:  pkgconfig(libacl)

# IDN support
BuildRequires:	pkgconfig(libidn)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

# XSLT support
BuildRequires:  pkgconfig(libxslt)

# YAZ support
BuildRequires:	pkgconfig(yaz)

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

%description
KBibTeX is a BibTeX editor for TDE to edit bibliographies used with LaTeX.
KBibTeX is released under the GNU Public License (GPL) version 2 or any later version.


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README.md TODO ChangeLog
%{tde_prefix}/bin/kbibtex
%{tde_prefix}/%{_lib}/trinity/libkbibtexpart.la
%{tde_prefix}/%{_lib}/trinity/libkbibtexpart.so
%{tde_prefix}/share/applications/tde/kbibtex.desktop
%{tde_prefix}/share/apps/kbibtex/
%dir %{tde_prefix}/share/apps/kbibtexpart
%{tde_prefix}/share/apps/kbibtexpart/kbibtex_part.rc
%dir %{tde_prefix}/share/apps/kbibtexpart/xslt
%{tde_prefix}/share/apps/kbibtexpart/xslt/MARC21slim2MODS3.xsl
%{tde_prefix}/share/apps/kbibtexpart/xslt/MARC21slimUtils.xsl
%{tde_prefix}/share/apps/kbibtexpart/xslt/UNIMARC2MODS3.xsl
%{tde_prefix}/share/apps/kbibtexpart/xslt/html.xsl
%{tde_prefix}/share/icons/hicolor/*/apps/kbibtex.png
%{tde_prefix}/share/services/kbibtex_part.desktop
%{tde_prefix}/share/man/man1/kbibtex.1*
%{tde_prefix}/share/doc/tde/HTML/en/kbibtex/

