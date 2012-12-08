Summary:	Enabling/disabling Powersaving mode for AMD processors
Name:		athcool
Version:	0.3.12
Release:	%mkrel 7
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


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.12-6mdv2011.0
+ Revision: 662885
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.12-5mdv2011.0
+ Revision: 603476
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.12-4mdv2010.1
+ Revision: 522109
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.3.12-3mdv2010.0
+ Revision: 413119
- rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.3.12-2mdv2009.0
+ Revision: 220464
- rebuild

* Sat Dec 15 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.12-1mdv2008.1
+ Revision: 120301
- new version
- do not package COPYING file
- new license policy
- spec file clean

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 0.3.11-6mdv2008.0
+ Revision: 69907
- kill file require on chkconfig

* Tue Jun 05 2007 Christiaan Welvaart <spturtle@mandriva.org> 0.3.11-5mdv2008.0
+ Revision: 35272
- Import athcool



* Fri Jul 14 2006 Emmanuel Andry <eandry@mandriva.org> 0.3.11-5mdv2007.0
- rebuild

* Sun Jan  8 2006 Olivier Blin <oblin@mandriva.com> 0.3.11-4mdk
- convert parallel init to LSB
- fix initscript perms
- convert Prereq to Requires

* Thu Jan 05 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.3.11-3mdk
- drop patch 0 (no more needed with pciutils-2.2.1-2mdk)

* Tue Jan 03 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.3.11-2mdk
- source 1: add support for parallel init
- patch 0: fix build with new pciutils

* Fri Aug 26 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.3.11-1mdk
- new release

* Thu Feb 24 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.3.10-1mdk
- new release

* Sat Jan 08 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.3.9-1mdk
- 0.3.9

* Mon Jul 5 2004 Tibor Pittich <Tibor.Pittich@mandrake.org> 0.3.7-1mdk
- 0.3.7

* Fri May 21 2004 Tibor Pittich <Tibor.Pittich@mandrake.org> 0.3.5-1mdk
- 0.3.5
- description improved, added man page
- added SysV start script

* Mon Oct 13 2003 Tibor Pittich <Tibor.Pittich@phuture.sk> 0.3.1-1mdk
- initial mdk contrib import
- spec cleanup

* Tue Sep 23 2003 Osamu Kayasono <jacobi@jcom.home.ne.jp> 0.3.1
 - Released as 0.3.1
 - add WARNING message	
 - add 'DESTDIR' variable in Makefile
 - merge Mr. Zuckschwerdt's patch
   - fix compilation problem with gcc-3.3

* Sat Jun 21 2003 Osamu Kayasono <jacobi@jcom.home.ne.jp> 0.3.0
 - Released as 0.3.0
 - add SiS 748 support (not tested)
 - display values before and after changing the register
 - merge Mr. Nakata's patch
	( http://www.nakata-jp.org/ [ written in Japanese ])
   - fix bug which may fail in recognition of a chipset
   - clean up whole codes for improving readability and removing hidden bugs

* Sat Mar  1 2003 Osamu Kayasono <jacobi@jcom.home.ne.jp> 0.2.0
 - Released as 0.2.0
 - add listing supported chipsets
 - add nVIDIA nForce/nForce2 support (not tested)
 - separate Chipset ID and Register configuration 
   (because some chipsets has different ID, but same config)

* Sat Oct 12 2002 Osamu Kayasono <jacobi@jcom.home.ne.jp> 0.1.1
 - Released as 0.1.1
 - fix a bug (cannot disable powersaving)
