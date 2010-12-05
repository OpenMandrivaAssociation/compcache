Name:    compcache
Version: 0.6.2
Release: %mkrel 3
Summary: Compcache (compressed caching) provides the ability to use part of the RAM as compressed swap
License: BSD and GPLv2
URL:     http://code.google.com/p/compcache/
Group:   System/Kernel and hardware
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Source0: http://compcache.googlecode.com/files/%{name}-%{version}.tar.gz
Source1: compcache.init
Source2: compcache.sysconfig

%description
Compcache (compressed caching) provides the ability to use part of the RAM as
compressed swap. In other words, you can take a portion of your RAM (default
25%) and use it as swap, compressing the data before moving it into swap, and
decompressing it when moving it out of swap. This is a classic time-space
trade-off. You effectively get more memory, but some of it is slower than
normal RAM due to the CPU time required to compress and decompress the swapped
pages.

%prep
%setup -q
install -m0755 %{SOURCE1} compcache.init
install -m0755 %{SOURCE2} compcache.sysconfig

%build
%make -C sub-projects/rzscontrol/

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_initrddir}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m0755 compcache.init %{buildroot}%{_initrddir}/%{name}
install -m0755 compcache.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -m0755 sub-projects/rzscontrol/rzscontrol %{buildroot}%{_sbindir}
install -m0755 sub-projects/rzscontrol/rzscontrol %{buildroot}%{_sbindir}
install -m0644 sub-projects/rzscontrol/man/rzscontrol.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changelog
%{_initrddir}/%name
%config %{_sysconfdir}/sysconfig/%name
%{_sbindir}/rzscontrol
%{_mandir}/man1/rzscontrol.1*
