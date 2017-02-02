Name:           rpm-opt-hooks
Version:        3
Release:        1%{?dist}
Summary:        RPM dependency generator hooks for packages in /opt

License:        MIT
BuildArch:      noarch

Source0:        opt.attr
Source1:        optlibsymlink.attr
Source2:        opt.prov
Source3:        opt.req
Source4:        opt.common
Source5:        LICENSE
Source6:        README.md

%description
RPM dependency generator hooks for packages installed in /opt.  This package
should be added to the buildroot or a package's BuildRequires.


%prep
%setup -c -T
cp -a %SOURCE5 %SOURCE6 .


%install
install -Dpm 0644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/fileattrs/opt.attr
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/fileattrs/optlibsymlink.attr
install -Dpm 0755 %{SOURCE2} %{buildroot}%{_rpmconfigdir}/opt.prov
install -Dpm 0755 %{SOURCE3} %{buildroot}%{_rpmconfigdir}/opt.req
install -Dpm 0644 %{SOURCE4} %{buildroot}%{_rpmconfigdir}/opt.common


%files
%license LICENSE
%doc README.md
%{_rpmconfigdir}/fileattrs/opt.attr
%{_rpmconfigdir}/fileattrs/optlibsymlink.attr
%{_rpmconfigdir}/opt.common
%{_rpmconfigdir}/opt.prov
%{_rpmconfigdir}/opt.req


%changelog
* Thu Feb 2 2017 Orion Poplawski <orion@cora.nwra.com> 3-1
- Handle compiler-only deps for MPI packages

* Wed Mar 2 2016 Orion Poplawski <orion@cora.nwra.com> 2-1
- Try to limit requires to same prefix to allow building for multiple prefixes
  on the same machine/buildroot

* Mon Dec 21 2015 Orion Poplawski <orion@cora.nwra.com> 1-1
- Initial package
