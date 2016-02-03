# Created by pyp2rpm-2.0.0
%global pypi_name riak

Name:           python-%{pypi_name}
Version:        2.4.0
Release:        1%{?dist}
Summary:        Python clients for Riak

License:        ASL 2.0 
URL:            https://github.com/basho/riak-python-client
Source0:        https://github.com/basho/riak-python-client/archive/%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx
#BuildRequires:  python-cryptography
#BuildRequires:  protobuf-python
#BuildRequires:  pyOpenSSL
#BuildRequires:  libffi
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
#BuildRequires:  python3-cryptography
#BuildRequires:  python3-pyOpenSSL

%description
Python clients for Riak

%package -n     python2-%{pypi_name}
Summary:        Python clients for Riak
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-six >= 1.8.0
%description -n python2-%{pypi_name}
Python clients for Riak

%package -n     python3-%{pypi_name}
Summary:        Python clients for Riak
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-six >= 1.8.0
%description -n python3-%{pypi_name}
Python clients for Riak

%package -n python-%{pypi_name}-doc
Summary:        riak documentation
%description -n python-%{pypi_name}-doc
Documentation for riak

%prep
%autosetup -n riak-python-client-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
cat << EOF > PKG-INFO
Metadata-Version: 1.1
Name: riak
Version: 2.4.0
Summary: Python client for Riak
Home-page: https://github.com/basho/riak-python-client
Author: Basho Technologies
Author-email: clients@basho.com
License: Apache 2
Description: UNKNOWN
Platform: Platform Independent
Classifier: License :: OSI Approved :: Apache Software License
Classifier: Intended Audience :: Developers
Classifier: Operating System :: OS Independent
Classifier: Programming Language :: Python :: 2.7
Classifier: Programming Language :: Python :: 3.3
Classifier: Programming Language :: Python :: 3.4
Classifier: Programming Language :: Python :: 3.5
Classifier: Topic :: Database
Requires: six(>=1.8.0)
Requires: python3_protobuf(>=2.4.1, <2.6.0)
EOF

%build
%py2_build
%py3_build
# generate html docs 
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install

%py2_install


%check
#this requires a riak cluster, not doing it.

%files -n python2-%{pypi_name} 
%doc README.rst LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name} 
%doc README.rst LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Wed Feb 03 2016 Pete Travis <me@petetravis.com> - 2.4.0-1
- Initial package
- Sources from upstream working repository.
