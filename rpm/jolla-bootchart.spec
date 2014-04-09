Name:       jolla-bootchart
Summary:    Enabler for systemd boot chart
Version:    1.20
Release:    1
Group:      Development/Tools
License:    LGPLv2.1+
BuildArch:  noarch
URL:        http://cgit.freedesktop.org/systemd/systemd/
Source0:    bootchartd.active

%description
Enabler for systemd boot time graph generator

%install
install -d -m 755 %{buildroot}/etc
install -m 644 %{SOURCE0} %{buildroot}/etc/

%files
%defattr(-,root,root,-)
%config /etc/bootchartd.active
