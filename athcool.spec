Summary:	Enabling/disabling Powersaving mode for AMD processors
Name:		athcool
Version:	0.3.12
Release:	%mkrel 5
License:	GPLv2+
Group:		System/Configuration/Hardware
URL:		http://members.jcom.home.ne.jp/jacobi/linux/softwares.html
Source0:	http://members.jcom.home.ne.jp/jacobi/linux/files/%name-%version.tar.bz2
Source1:	%{name}.init
Buildrequires:	pciutils-devel
Requires(post,preun):	chkconfig, rpm-helper
ExclusiveArch:	%{ix86}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Athcool is a small utility, enabling/disabling Powersaving mode
for AMD Athlon/Duron processors.

Since enabling Powersaving mode, you can save power consumption, 
lower CPU temprature when CPU is idle.

Powersaving works if your kernel support ACPI (APM not work),
because athcool only set/unset "Disconnect enable when STPGNT detected"
bits in the Northbridge of Chipset.
To really save power, someone has to send the STPGNT signal when idle.
This is done by the ACPI subsystem when C2 state entered.

!!!WARNING!!!
Depending on your motherboard and/or hardware components,
enabling powersaving mode may cause that:

 * noisy or distorted sound playback
 * a slowdown in harddisk performance
 * system locks or instability

If you met those problems, you should not use athcool.
Please use athcool AT YOUR OWN RISK.

%prep
%setup -q

%build

%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
%makeinstall_std

install -D -m755 %{SOURCE1} %{buildroot}%{_initrddir}/athcool

%clean
rm -rf %{buildroot}

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_initrddir}/athcool
%{_sbindir}/athcool
%{_mandir}/man8/*
