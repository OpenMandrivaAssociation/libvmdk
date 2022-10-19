%global sname	vmdk

%global	major 1
%global libname		%mklibname %{sname}
%global develname	%mklibname %{sname} -d
%global pyname		python-py%{sname}

%bcond_without	python
# unpackaged yet
%bcond_with		libbfio
%bcond_with		libcdata
%bcond_with		libcerror
%bcond_with		libcfile
%bcond_with		libcnotify
%bcond_with		libcpath
%bcond_with		libcsplit
%bcond_with		libcthreads
%bcond_with		libfcache
%bcond_with		libfdata
%bcond_with		libfvalue
%bcond_with		libuna

Summary: 	Library and tools to access the VMware Virtual Disk (VMDK) format
Name:		lib%{sname}
Version:	20210807
Release:	1
License:	LGPLv3+ and GPLv3+
Group:		File tools
URL:		https://github.com/libyal/%{name}
Source0:	https://github.com/libyal/%{name}/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz

BuildRequires:  intltool

%{?with_python:
BuildRequires:	pkgconfig(python3)
}

%description
libvmdk is a library to access the VMware Virtual Disk (VMDK) format.

Read supported extent file formats:

* RAW (flat)
* COWD version 1 (sparse)
* VMDK version 1, 2 and 3 (sparse)

Supported VMDK format features:

* delta links
* grain compression (as of version 20131209)
* data markers (as of version 20140416)

VMDK format features not supported at the moment:

* images that use a physical device
* changed block tracking (CBT) (supported by VMDK version 3 (sparse)) / change tracking file

Work in progress:

* Dokan library support
* Thread-safety in handle API functions

#---------------------------------------------------------------------------

%package -n %{sname}
Summary:	Library for %{name}
Group:		System/Libraries

%description -n %{sname}
libvmdk is a library to access the VMware Virtual Disk (VMDK) format.

Read supported extent file formats:

* RAW (flat)
* COWD version 1 (sparse)
* VMDK version 1, 2 and 3 (sparse)

Supported VMDK format features:

* delta links
* grain compression (as of version 20131209)
* data markers (as of version 20140416)

VMDK format features not supported at the moment:

* images that use a physical device
* changed block tracking (CBT) (supported by VMDK version 3 (sparse)) / change tracking file

Work in progress:

* Dokan library support
* Thread-safety in handle API functions

This package provides some useful tools.

%files -n %{sname}
%license COPYING COPYING.LESSER
%{_bindir}/%{sname}info
%{_bindir}/%{sname}mount
%{_mandir}/man1/%{sname}info.1.*

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for %{name}
Group:		System/Libraries

%description -n %{libname}
The %libname package contains library for %{name}.

%files -n %{libname}
%{_libdir}/lib%{sname}.so.%{major}*

#---------------------------------------------------------------------------

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}

%description -n %{develname}
The %{develname} package contains libraries and header files for
developing applications that use %{name}.

%files -n %{develname}
%license COPYING COPYING.LESSER
%doc AUTHORS NEWS README
%{_includedir}/lib%{sname}/
%{_includedir}/lib%{sname}.h
%{_libdir}/lib%{sname}.so
%{_libdir}/pkgconfig/lib%{sname}.pc
%{_mandir}/man3/lib%{sname}.3.zst*

#---------------------------------------------------------------------------

%{?with_python:
%package -n %{pyname}
Summary:        Python binding for the %{name}
Group:          Development/Libraries

%description -n %{pyname}
Python3 bindings for %name.

%files -n %{pyname}
%license COPYING COPYING.LESSER
%{py_platsitedir}/py%{sname}.so
#%%{py_platsitedir}/py%{sname}-*-py%{py_ver}.egg-info
}

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
	--disable-python2 \
	--enable-wide-character-type \
	%{?with_python:--enable-python3}%{!?with_python:--disable-python3} \
	%{?with_libbfio:--enable-libbfio}%{!?with_libbfio:--disable-libbfio} \
	%{?with_libcdata:--enable-libcdata}%{!?with_libcdata:--disable-libcdata} \
	%{?with_libcerror:--enable-libcerror}%{!?with_libcerror:--disable-libcerror} \
	%{?with_libcfile:--enable-libcfile}%{!?with_libcfile:--disable-libcfile} \
	%{?with_libcnotify:--enable-libcnotify}%{!?with_libcnotify:--disable-libcnotify} \
	%{?with_libcpath:--enable-libcpath}%{!?with_libcpath:--disable-libcpath} \
	%{?with_libcsplit:--enable-libcsplit}%{!?with_libcsplit:--disable-libcsplit} \
	%{?with_libcthreads:--enable-libcthreads}%{!?with_libcthreads:--disable-libcthreads} \
	%{?with_libfcache:--enable-libfcache}%{!?with_libfcache:--disable-libfcache} \
	%{?with_libfdata:--enable-libfdata}%{!?with_libfdata:--disable-libfdata} \
	%{?with_libfvalue:--enable-libfvalue}%{!?with_libfvalue:--disable-libfvalue} \
	%{?with_libuna:--enable-python3}%{!?with_libuna:--disable-libuna}
%make_build

%install
%make_install

