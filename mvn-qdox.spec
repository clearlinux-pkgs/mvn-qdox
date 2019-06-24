#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-qdox
Version  : 2.0.m2
Release  : 1
URL      : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/2.0-M2/qdox-2.0-M2.jar
Source0  : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/2.0-M2/qdox-2.0-M2.jar
Source1  : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/2.0-M2/qdox-2.0-M2.pom
Source2  : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/2.0-M7/qdox-2.0-M7.jar
Source3  : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/2.0-M7/qdox-2.0-M7.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-qdox-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-qdox package.
Group: Data

%description data
data components for the mvn-qdox package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M2
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M7
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M7
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M7


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M2/qdox-2.0-M2.jar
/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M2/qdox-2.0-M2.pom
/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M7/qdox-2.0-M7.jar
/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M7/qdox-2.0-M7.pom
