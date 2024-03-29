#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-qdox
Version  : 2.0.m2
Release  : 7
URL      : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/2.0-M2/qdox-2.0-M2.jar
Source0  : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/2.0-M2/qdox-2.0-M2.jar
Source1  : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/1.12.1/qdox-1.12.1.jar
Source2  : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/1.12.1/qdox-1.12.1.pom
Source3  : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/2.0-M10/qdox-2.0-M10.jar
Source4  : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/2.0-M10/qdox-2.0-M10.pom
Source5  : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/2.0-M2/qdox-2.0-M2.pom
Source6  : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/2.0-M5/qdox-2.0-M5.jar
Source7  : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/2.0-M5/qdox-2.0-M5.pom
Source8  : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/2.0-M7/qdox-2.0-M7.jar
Source9  : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/2.0-M7/qdox-2.0-M7.pom
Source10  : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/2.0-M8/qdox-2.0-M8.jar
Source11  : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/2.0-M8/qdox-2.0-M8.pom
Source12  : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/2.0-M9/qdox-2.0-M9.jar
Source13  : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/2.0-M9/qdox-2.0-M9.jar
Source14  : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/2.0-M9/qdox-2.0-M9.pom
Source15  : https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/2.0-M9/qdox-2.0-M9.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-qdox-data = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
No detailed description available

%package data
Summary: data components for the mvn-qdox package.
Group: Data

%description data
data components for the mvn-qdox package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M2
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M2/qdox-2.0-M2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/1.12.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/1.12.1/qdox-1.12.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/1.12.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/1.12.1/qdox-1.12.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M10
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M10/qdox-2.0-M10.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M10
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M10/qdox-2.0-M10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M2
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M2/qdox-2.0-M2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M5
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M5/qdox-2.0-M5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M5
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M5/qdox-2.0-M5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M7
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M7/qdox-2.0-M7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M7
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M7/qdox-2.0-M7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M8
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M8/qdox-2.0-M8.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M8
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M8/qdox-2.0-M8.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M9
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M9/qdox-2.0-M9.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M9
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M9/qdox-2.0-M9.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M9
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M9/qdox-2.0-M9.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M9
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M9/qdox-2.0-M9.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/1.12.1/qdox-1.12.1.jar
/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/1.12.1/qdox-1.12.1.pom
/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M10/qdox-2.0-M10.jar
/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M10/qdox-2.0-M10.pom
/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M2/qdox-2.0-M2.jar
/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M2/qdox-2.0-M2.pom
/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M5/qdox-2.0-M5.jar
/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M5/qdox-2.0-M5.pom
/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M7/qdox-2.0-M7.jar
/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M7/qdox-2.0-M7.pom
/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M8/qdox-2.0-M8.jar
/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M8/qdox-2.0-M8.pom
/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M9/qdox-2.0-M9.jar
/usr/share/java/.m2/repository/com/thoughtworks/qdox/qdox/2.0-M9/qdox-2.0-M9.pom
