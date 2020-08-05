%global debug_package %{nil}

Name:           memavaild
Version:        0.4.1
Release:        1%{?dist}
Summary:        Improve responsiveness during intense swapping: keep amount of available memory

License:        MIT
URL:            https://github.com/hakavlad/memavaild
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source10:       %{name}.sysusers

Patch0:         %{name}-rpm-drop-not-required-sections-from-install.patch

BuildArch:      noarch

BuildRequires:  systemd

%description
Improve responsiveness during intense swapping: keep amount of available memory.


%prep
%autosetup


%build
# Not required


%install
%make_install PREFIX=%{_prefix} SYSCONFDIR=%{_sysconfdir} SYSTEMDUNITDIR=%{_unitdir}


%pre
%sysusers_create_package %{name} %{SOURCE10}


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service



%files
%license LICENSE
%doc README.md
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_datadir}/%{name}/%{name}.conf




%changelog
* Wed Aug 05 2020 ElXreno <elxreno@gmail.com> - 0.4.1-1
- Update to version 0.4.1

* Sat Aug 01 2020 ElXreno <elxreno@gmail.com> - 0.3-1
- Update to version 0.3

* Tue Jul 28 2020 ElXreno <elxreno@gmail.com> - 0.2.1-1
- Update to version 0.2.1

* Tue Jul 28 2020 ElXreno <elxreno@gmail.com> - 0.2-1
- Update to version 0.2

* Wed Jul 22 2020 ElXreno <elxreno@gmail.com>
- Initial packaging
