Name:       jolla-bootchart
Summary:    Enabler for systemd boot chart
Version:    1.21
Release:    1
License:    LGPLv2+
BuildArch:  noarch
URL:        https://github.com/systemd/systemd
Source0:    %{name}-%{version}.tar.gz
Source1:    bootchartd.active
Requires:   systemd-bootchart

%description
Enabler for systemd boot time graph generator

%prep
%setup -q -n %{name}-%{version}

%build

%install
install -d -m 755 %{buildroot}/etc
install -m 644 %{SOURCE1} %{buildroot}/etc/

%files
%defattr(-,root,root,-)
%license LICENSE.LGPL2.1
%config /etc/bootchartd.active
