Name:       jolla-bootchart
Summary:    Enabler for systemd boot chart
Version:    1.20
Release:    1
License:    LGPLv2+
BuildArch:  noarch
URL:        http://cgit.freedesktop.org/systemd/systemd/
Source0:    %{name}-%{version}.tar.gz
Source1:    bootchartd.active

%description
Enabler for systemd boot time graph generator

%install
install -d -m 755 %{buildroot}/etc
install -m 644 %{SOURCE1} %{buildroot}/etc/

%files
%defattr(-,root,root,-)
%license LICENSE.LGPL2.1
%config /etc/bootchartd.active
