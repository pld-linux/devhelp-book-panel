Summary:	DevHelp book: panel
Summary(pl):	Ksi±¿ka do DevHelp'a o panel
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

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about panel

%description -l pl
Ksi±¿ka do DevHelp o panel

%prep
%setup -q -c panel -n panel

%build
mv -f book panel
mv -f book.devhelp panel.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/gnome-panel
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install panel.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install panel/* $RPM_BUILD_ROOT%{_prefix}/books/gnome-panel

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
