# spec file for package nodejs-nodejs-string_decoder
%{?scl:%scl_package nodejs-nodejs-string_decoder}
%{!?scl:%global pkg_name %{name}}

%global npm_name string_decoder
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-string_decoder
Version:	0.10.31
Release:	4%{?dist}
Summary:	The string_decoder module from Node core
Url:		https://github.com/rvagg/string_decoder
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm}} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel
#BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:	npm(tap)
%endif

%description
The string_decoder module from Node core

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
tap test/simple/*.js
%endif

%files
%{nodejs_sitelib}/string_decoder

%doc README.md LICENSE

%changelog
* Mon Jul 03 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.10.31-4
- rh-nodejs8 rebuild

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.10.31-3
- rebuilt

* Sat Feb 13 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.10.31-2
- rebuilt

* Thu Aug 13 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.10.31-1
- Initial build
