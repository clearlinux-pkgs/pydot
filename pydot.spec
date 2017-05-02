#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pydot
Version  : 1.2.3
Release  : 2
URL      : https://pypi.python.org/packages/ae/e6/2c0b7c142c18fb89b294734d45d4264a71269686090af69404df211754c3/pydot-1.2.3.tar.gz
Source0  : https://pypi.python.org/packages/ae/e6/2c0b7c142c18fb89b294734d45d4264a71269686090af69404df211754c3/pydot-1.2.3.tar.gz
Summary  : Python interface to Graphviz's Dot
Group    : Development/Tools
License  : MIT
Requires: pydot-python
Requires: chardet
Requires: graphviz
Requires: nose
Requires: pyparsing
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyparsing
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
[![Build Status][build_img]][travis]
About
=====
`pydot`:
- is an interface to [Graphviz][1]
- can parse and dump into the [DOT language][2] used by GraphViz,
- is written in pure Python,

%package python
Summary: python components for the pydot package.
Group: Default

%description python
python components for the pydot package.


%prep
%setup -q -n pydot-1.2.3

%build
export LANG=C
export SOURCE_DATE_EPOCH=1490031058
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1490031058
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
