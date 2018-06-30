#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pydot
Version  : 1.2.4
Release  : 13
URL      : http://pypi.debian.net/pydot/pydot-1.2.4.tar.gz
Source0  : http://pypi.debian.net/pydot/pydot-1.2.4.tar.gz
Summary  : Python interface to Graphviz's Dot
Group    : Development/Tools
License  : MIT
Requires: pydot-python3
Requires: pydot-python
Requires: graphviz
Requires: pyparsing
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyparsing

BuildRequires : python3-dev
BuildRequires : setuptools

%description
A Python interface to GraphViz and the DOT language.
        
        This package includes an interface to GraphViz [1], with classes to represent
        graphs and dump them in the DOT language [2], and a parser from DOT.

%package python
Summary: python components for the pydot package.
Group: Default
Requires: pydot-python3

%description python
python components for the pydot package.


%package python3
Summary: python3 components for the pydot package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pydot package.


%prep
%setup -q -n pydot-1.2.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1514243421
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
