Name:           rpm-opt-hooks
Version:        1
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
cp -a %SOURCE5 .


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
* Mon Dec 21 2015 Orion Poplawski <orion@cora.nwra.com> 1.0-1
- Initial package
