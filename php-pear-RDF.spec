%define		_status		alpha
%define		_pearname	RDF
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - Port of the core RAP API
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0ceb2b28bc35fdf101973778c7be59fc
URL:		http://pear.php.net/package/RDF/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.571
Requires:	php(core) >= 4.2.0
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.0-0.b1
Suggests:	php-pear-MDB
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(MDB.*)

%description
This package is a port of the core components of the RDF API for PHP
(aka RAP): <http://www.wiwiss.fu-berlin.de/suhl/bizer/rdfapi/>.

In PEAR status of this package is: %{_status}.

%prep
%pear_package_setup

mv docs/%{_pearname}/docs/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_examplesdir}/%{name}-%{version}}
%pear_package_install

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/RDF.php
%{php_pear_dir}/RDF

%{php_pear_dir}/data/%{_pearname}

%{_examplesdir}/%{name}-%{version}
