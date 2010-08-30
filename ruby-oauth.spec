
%define gitrev d8dbd6f
%define gitauthor mojodna
%define gitname oauth

Summary:	Ruby library for doing OAuth
Name:		ruby-oauth
Version:	0.3.6
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://download.github.com/%{gitauthor}-%{gitname}-v%{version}-0-g%{gitrev}.tar.gz
# Source0-md5:	32491813dd124e2214d36fe6d1e66227
#Patch0: %{name}-nogems.patch
URL:		http://oauth.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby
BuildRequires:	ruby-modules
BuildRequires:	setup.rb = 3.4.1
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
Requires:	ruby-hmac
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a library for implementing both OAuth clients and servers in
Ruby applications.

%prep
%setup -q -n %{gitauthor}-%{gitname}-%{gitrev}
#%patch0 -p1
cp %{_datadir}/setup.rb .
ruby setup.rb config \
	--installdirs=std
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oauth
%{ruby_rubylibdir}/oauth.rb
%{ruby_rubylibdir}/oauth
