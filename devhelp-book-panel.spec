Summary:	DevHelp book: GNOME panel
Summary(pl):	Ksi��ka do DevHelpa o panelu GNOME
Name:		devhelp-book-panel
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/panel.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp

%description
DevHelp book about GNOME panel.

%description -l pl
Ksi��ka do DevHelpa o panelu GNOME.

%prep
%setup -q -c -n panel

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/gnome-panel,specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/panel.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/gnome-panel

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*