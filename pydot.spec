#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pydot
Version  : 1.4.1
Release  : 29
URL      : https://files.pythonhosted.org/packages/5f/e2/23e053ccf5648153959ea15d77fb90adb2b1f9c9360f832f39d6d6c024e2/pydot-1.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/5f/e2/23e053ccf5648153959ea15d77fb90adb2b1f9c9360f832f39d6d6c024e2/pydot-1.4.1.tar.gz
Summary  : Python interface to Graphviz's Dot
Group    : Development/Tools
License  : MIT
Requires: pydot-license = %{version}-%{release}
Requires: pydot-python = %{version}-%{release}
Requires: pydot-python3 = %{version}-%{release}
Requires: chardet
Requires: graphviz
Requires: pyparsing
BuildRequires : buildreq-distutils3
BuildRequires : chardet
BuildRequires : graphviz
BuildRequires : pyparsing

%description
[![Build Status](https://www.travis-ci.com/pydot/pydot.svg?branch=master)](https://www.travis-ci.com/pydot/pydot)
[![PyPI](https://img.shields.io/pypi/v/pydot.svg)](https://pypi.org/project/pydot/)

%package license
Summary: license components for the pydot package.
Group: Default

%description license
license components for the pydot package.


%package python
Summary: python components for the pydot package.
Group: Default
Requires: pydot-python3 = %{version}-%{release}

%description python
python components for the pydot package.


%package python3
Summary: python3 components for the pydot package.
Group: Default
Requires: python3-core
Provides: pypi(pydot)
Requires: pypi(pyparsing)

%description python3
python3 components for the pydot package.


%prep
%setup -q -n pydot-1.4.1
cd %{_builddir}/pydot-1.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603400323
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pydot
cp %{_builddir}/pydot-1.4.1/LICENSE %{buildroot}/usr/share/package-licenses/pydot/618fabcc77955d5e8e8999bf326d8327bdbb0963
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pydot/618fabcc77955d5e8e8999bf326d8327bdbb0963

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
