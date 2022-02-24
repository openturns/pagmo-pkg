# norootforbuild

%define __cmake %{_bindir}/cmake
%define _cmake_lib_suffix64 -DLIB_SUFFIX=64
%define cmake \
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ; \
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ; \
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS ; \
%__cmake \\\
-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \\\
%if "%{?_lib}" == "lib64" \
%{?_cmake_lib_suffix64} \\\
%endif \
-DBUILD_SHARED_LIBS:BOOL=ON

Name:           pagmo 
Version:        2.18.0
Release:        1%{?dist}
Summary:        Perform parallel computations of optimisation tasks
Group:          System Environment/Libraries
License:        GPL2
URL:            https://esa.github.io/pagmo2/
Source0:        https://github.com/esa/pagmo2/archive/v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  gcc-c++, cmake, boost-devel, eigen3-devel, tbb-devel
Requires:       libpagmo2

%description
Perform parallel computations of optimisation tasks.

%package -n libpagmo2
Summary:        Perform parallel computations of optimisation tasks
Group:          Development/Libraries/C and C++

%description -n libpagmo2
Perform parallel computations of optimisation tasks (binaries)

%package devel
Summary:        Perform parallel computations of optimisation tasks
Group:          Development/Libraries/C and C++
Requires:       libpagmo2 = %{version}
Requires:       eigen3-devel

%description devel
Perform parallel computations of optimisation tasks (development files)

%prep
%setup -q -n %{name}2-%{version}

%build
%cmake -DPAGMO_WITH_EIGEN3=ON .
make %{?_smp_mflags} 

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%post -n libpagmo2 -p /sbin/ldconfig
%postun -n libpagmo2 -p /sbin/ldconfig

%files -n libpagmo2
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
