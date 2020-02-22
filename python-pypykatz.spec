# Created by pyp2rpm-3.3.3
%global pypi_name pypykatz

Name:           python-%{pypi_name}
Version:        0.3.4
Release:        1%{?dist}
Summary:        Python implementation of Mimikatz

License:        None
URL:            https://github.com/skelsec/pypykatz
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(aiowinreg) >= 0.0.2
Requires:       python3dist(minidump) >= 0.0.12
Requires:       python3dist(minikerberos) >= 0.0.11
Requires:       python3dist(msldap) >= 0.1.1
Requires:       python3dist(setuptools)
Requires:       python3dist(winsspi) >= 0.0.3
%description -n python3-%{pypi_name}



%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{_bindir}/pypykatz
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Feb 22 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.3.4-1
- Initial package.
