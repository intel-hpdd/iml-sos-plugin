%global pypi_name iml_sos_plugin

%{?dist_version: %global source https://github.com/intel-hpdd/%{pypi_name}/archive/%{dist_version}.tar.gz}
%{?dist_version: %global archive_version %{dist_version}}
%{?!dist_version: %global source https://pypi.python.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz}
%{?!dist_version: %global archive_version %{version}}

Name:           %{pypi_name}
Version:        2.1.0
Release:        1%{?dist}
Summary:        A sosreport plugin for collecting IML data.
License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{source}

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python2-setuptools_scm

Requires:       sos
Obsoletes:      chroma-diagnostics

%description
A sosreport plugin for collecting IML data.

%prep
%if %{?dist_version:1}%{!?dist_version:0}
%setup -n %{pypi_name}-%{archive_version}
%else
%setup -c -n %{rpm_name}-%{version}
# Remove bundled egg-info
rm -rf %{rpm_name}.egg-info
%endif

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
mkdir -p %{buildroot}/%{python2_sitelib}/sos/plugins/
mv %{buildroot}/%{python2_sitelib}/iml_sos_plugin/iml.py* %{buildroot}/%{python2_sitelib}/sos/plugins/

%files
%{_bindir}/iml-diagnostics
%{_bindir}/chroma-diagnostics
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{python2_sitelib}/sos/plugins/iml.py*

%changelog
* Mon Mar 5 2018 Joe Grund <joe.grund@intel.com> 2.1.0-1
- Add Multipath info and more lustre debug (@utopiabound)

* Wed Nov 15 2017 Will Johnson <william.c.johnson@intel.com> 2.0.4-1
- Obsoletes chroma-diagnostics
- Remove zfs plugin

* Thu Oct 12 2017 Joe Grund <joe.grund@intel.com> 2.0.2-1
- Fix log-size param to dash-case.

* Wed Oct 11 2017 Joe Grund <joe.grund@intel.com> 2.0.1-1
- Add yum plugin to iml-diagnostics.
- Ensure no log tailing is performed for chroma log collection.

* Tue Sep 12 2017 Joe Grund <joe.grund@intel.com> 2.0.0-1
- Update to work with sos 3.4

* Thu Sep 7 2017 Joe Grund <joe.grund@intel.com> 1.0.2-1
- Add some more file collections.
- Forward args to sosreport.

* Thu Sep 7 2017 Joe Grund <joe.grund@intel.com> 1.0.1-1
- Initial Relase
