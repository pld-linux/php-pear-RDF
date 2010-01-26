%include	/usr/lib/rpm/macros.php
%define		_class		RDF
%define		_subclass	%{nil}
%define		_status		alpha
%define		_pearname	RDF
%define		subver	alpha1
%define		rel		1
Summary:	%{_pearname} - Port of the core RAP API
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	0.%{subver}.%{rel}
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	ab1c1df4069f3e9c6e25995ecceac355
URL:		http://pear.php.net/package/RDF/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(MDB.*)'

%description
This package is a port of the core components of the RDF API for PHP (aka RAP):
<http://www.wiwiss.fu-berlin.de/suhl/bizer/rdfapi/>.

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

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/RDF.php
%{php_pear_dir}/RDF

%{php_pear_dir}/data/%{_pearname}

%{_examplesdir}/%{name}-%{version}
