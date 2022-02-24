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
Summary:        A hierarchical matrix C/C++ library
Group:          System Environment/Libraries
License:        GPL2
URL:            https://github.com/jeromerobert/hmat-oss
Source0:        https://github.com/jeromerobert/hmat-oss/archive/%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  gcc-c++, cmake, eigen3-devel
Requires:       libpagmo2

%description
A hierarchical matrix C/C++ library including a LU solver.

%package -n libpagmo2
Summary:        A hierarchical matrix C/C++ library 
Group:          Development/Libraries/C and C++

%description -n libpagmo2
A hierarchical matrix C/C++ library (binaries) 

%package devel
Summary:        A hierarchical matrix C/C++ library 
Group:          Development/Libraries/C and C++
Requires:       libpagmo2 = %{version}
Requires:       eigen3-devel

%description devel
A hierarchical matrix C/C++ library (development files)

%prep
%setup -q

%build
%cmake .
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
* Sat Nov 22 2014 Julien Schueller <schueller at phimeca dot com> 1.0-1
- Initial package creation
