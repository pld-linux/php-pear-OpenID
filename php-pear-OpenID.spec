%define		status		alpha
%define		pearname	OpenID
%define		php_min_version 5.2.0
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - PHP implementation of OpenID 1.1 and 2.0
Name:		php-pear-OpenID
Version:	0.4.0
Release:	1
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	9c8dc4ff7d77f747e3fb1cdb65a6105b
URL:		http://pear.php.net/package/OpenID/
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(dom)
Requires:	php(filter)
Requires:	php(hash)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php(xml)
Requires:	php-pear
Requires:	php-pear-Cache_Lite
Requires:	php-pear-Crypt_DiffieHellman
Requires:	php-pear-HTTP_Request2 >= 0.5.1
Requires:	php-pear-Net_URL2 >= 0.2.0
Requires:	php-pear-Services_Yadis >= 0.5.1
Suggests:	php-pear-HTTP_OAuth
Suggests:	php-pear-Log
Suggests:	php-pear-MDB2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_pear Log MDB2 HTTP/OAuth/.*

%description
OpenID is a free and easy way to use a single digital identity across
the Internet. See http://openid.net for details.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/OpenID/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/OpenID.php
%{php_pear_dir}/OpenID
%{php_pear_dir}/data/OpenID
