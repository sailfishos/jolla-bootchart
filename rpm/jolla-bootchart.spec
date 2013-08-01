Name:       jolla-bootchart
Summary:    Boot time graph generator
Version:    1.20
Release:    1
Group:      Development/Tools
License:    GPLv2
URL:        http://github.com/sofar/bootchart
Source0:    jolla-bootchart-%{version}.tar.gz
Source1:    bootchartd.conf

Conflicts:  bootchart

%description
Monitors where the system spends its time at start, creating a graph of all processes, disk utilization, and wait time.

%prep
%setup -q

%build
cd bootchart
./autogen.sh
%configure
make %{?jobs:-j%jobs}

%install
cd bootchart
rm -rf %{buildroot}
%make_install
install -d -m 755 %{buildroot}/etc
install -m 644 %{SOURCE1} %{buildroot}/etc/

%files
%defattr(-,root,root,-)
%config /etc/bootchartd.conf
/usr/sbin/bootchartd
%{_datadir}/doc/bootchart/bootchartd.conf.example
