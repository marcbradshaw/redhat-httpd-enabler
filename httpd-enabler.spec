Summary: Apache configuration, debian style
Name: httpd-enabler
Version: 0.1
Release: 4%{?dist}
License: None
URL: None
Group: System Environment/Daemons
Source0: %{name}-%{version}.tgz
# Taken from an active debian install
# see the Get.sh script in the archive.
BuildRoot: %{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Requires: httpd

%description
Framework for the debian style, provides
sites-available sites-enabled mods-available mods-enabled
and associated util scripts.


%prep
%setup -q
sed -ir "s|/etc/apache2|/etc/httpd|" a2enmod
sed -ir "s|/etc/init.d/apache2 |service httpd |" a2enmod
sed -ir "s|/usr/sbin/apache2|/usr/sbin/httpd|" a2enmod
sed -ir "s|/usr/share/doc/apache2.2-common/README.Debian.gz|Docs|" a2enmod
gzip a2*.8

%build


%install
rm -rf %{buildroot}
mkdir -p -m0755 %{buildroot}%{_sbindir}
mkdir -p -m0755 %{buildroot}%{_mandir}/man8
mkdir -p -m0755 %{buildroot}%{_sysconfdir}/httpd/conf.d
mkdir -p -m0755 %{buildroot}%{_sysconfdir}/httpd/sites-available
mkdir -p -m0755 %{buildroot}%{_sysconfdir}/httpd/sites-enabled
mkdir -p -m0755 %{buildroot}%{_sysconfdir}/httpd/mods-available
mkdir -p -m0755 %{buildroot}%{_sysconfdir}/httpd/mods-enabled
install -m 0644 httpd-enabler.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/
install -m 0755 a2enmod %{buildroot}%{_sbindir}
ln -s %{_sbindir}/a2enmod %{buildroot}%{_sbindir}/a2dismod
ln -s %{_sbindir}/a2enmod %{buildroot}%{_sbindir}/a2ensite
ln -s %{_sbindir}/a2enmod %{buildroot}%{_sbindir}/a2dissite
install -m 0644 a2enmod.8.gz %{buildroot}%{_mandir}/man8/
install -m 0644 a2dismod.8.gz %{buildroot}%{_mandir}/man8/
install -m 0644 a2ensite.8.gz %{buildroot}%{_mandir}/man8/
install -m 0644 a2dissite.8.gz %{buildroot}%{_mandir}/man8/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%config %dir %{_sysconfdir}/httpd/sites-*
%config %dir %{_sysconfdir}/httpd/mods-*
%config(noreplace) %dir %{_sysconfdir}/httpd/conf.d/*
%{_sbindir}/*
%{_mandir}/man8/*


%post


%changelog
* Mon Dec 07 2009 Marc Bradshaw <marc@marcbradshaw.co.uk> 0.1-4%{?dist}
- Minor fixes

* Mon Dec 07 2009 Marc Bradshaw <marc@marcbradshaw.co.uk> 0.1-3%{?dist}
- New upstream code from svn, major rewrite

* Tue Jul 28 2009 Marc Bradshaw <marc@marcbradshaw.co.uk> 0.1-2%{?dist}
- Minor revision

* Tue Dec 18 2007 Marc Bradshaw <marc@marcbradshaw.co.uk> 0.1-1%{?dist}
- Initial release
