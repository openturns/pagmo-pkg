Name:           pagmo 
Version:        2.18.0
Release:        1%{?dist}
Summary:        Perform parallel computations of optimisation tasks
Group:          System Environment/Libraries
License:        GPL3
URL:            https://esa.github.io/pagmo2/
Source0:        https://github.com/esa/pagmo2/archive/v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  gcc-c++, cmake, eigen3-devel, tbb-devel, boost-devel
Requires:       libpagmo

%description
Perform parallel computations of optimisation tasks.

%package -n libpagmo
Summary:        Perform parallel computations of optimisation tasks
Group:          Development/Libraries/C and C++

%description -n libpagmo
Perform parallel computations of optimisation tasks (binaries)

%package devel
Summary:        Perform parallel computations of optimisation tasks
Group:          Development/Libraries/C and C++
Requires:       libpagmo = %{version}
Requires:       eigen3-devel
Requires:       boost-devel

%description devel
Perform parallel computations of optimisation tasks (development files)

%prep
%setup -q -n %{name}2-%{version}

%build
%cmake -DPAGMO_WITH_EIGEN3=ON
%cmake_build

%install
%cmake_install

%post -n libpagmo -p /sbin/ldconfig
%postun -n libpagmo -p /sbin/ldconfig

%files -n libpagmo
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/pagmo/
%{_includedir}/pagmo/
%{_libdir}/*.so
%dir %{_libdir}/cmake/pagmo/
%{_libdir}/cmake/pagmo/*.cmake

%changelog
* Tue Feb 22 2022 Julien Schueller <schueller at phimeca dot com> 2.18.0-1
- Initial package creation
