# Created by pyp2rpm-3.2.3
%global pypi_name pbr

Name:           python-%{pypi_name}
Version:        3.1.1
Release:        1%{?dist}
Summary:        Python Build Reasonableness

License:        None
URL:            http://docs.openstack.org/developer/pbr/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
Introduction PBR is a library that injects some useful and sensible default
behaviors into your setuptools run. It started off life as the chunks of code
that were copied between all of the OpenStack_ projects. Around the time that
OpenStack hit 18 different projects each with at least 3 active branches, it
seemed like a good time to make that code into a proper reusable library.PBR is
only...

%package -n     python2-%{pypi_name}
Summary:        Python Build Reasonableness

Requires:       python2-setuptools
%description -n python2-%{pypi_name}
Introduction PBR is a library that injects some useful and sensible default
behaviors into your setuptools run. It started off life as the chunks of code
that were copied between all of the OpenStack_ projects. Around the time that
OpenStack hit 18 different projects each with at least 3 active branches, it
seemed like a good time to make that code into a proper reusable library.PBR is
only...

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        Python Build Reasonableness

Requires:       python%{python3_pkgversion}-setuptools
%description -n python%{python3_pkgversion}-%{pypi_name}
Introduction PBR is a library that injects some useful and sensible default
behaviors into your setuptools run. It started off life as the chunks of code
that were copied between all of the OpenStack_ projects. Around the time that
OpenStack hit 18 different projects each with at least 3 active branches, it
seemed like a good time to make that code into a proper reusable library.PBR is
only...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%{__python3} setup.py install --skip-build --root %{buildroot}
cp %{buildroot}/%{_bindir}/pbr %{buildroot}/%{_bindir}/pbr-3
ln -sf %{_bindir}/pbr-3 %{buildroot}/%{_bindir}/pbr-%{python3_version}

%{__python2} setup.py install --skip-build --root %{buildroot}
cp %{buildroot}/%{_bindir}/pbr %{buildroot}/%{_bindir}/pbr-2
ln -sf %{_bindir}/pbr-2 %{buildroot}/%{_bindir}/pbr-%{python2_version}


%files -n python2-%{pypi_name}
%doc README.rst pbr/tests/testpackage/README.txt
%{_bindir}/pbr
%{_bindir}/pbr-2
%{_bindir}/pbr-%{python2_version}
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.rst pbr/tests/testpackage/README.txt
%{_bindir}/pbr-3
%{_bindir}/pbr-%{python3_version}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Wed Jan 24 2018 Brian J. Murrell <brian.murrell@intel.com> - 3.1.1-1
- Initial package.
- Massage resulting spec to change python?_sitearch to
  python?_sitelib.
