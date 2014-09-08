%global gem_name bcrypt

Name: rubygem-%{gem_name}
Version: 3.1.7
Release: 1%{?dist}
Summary: OpenBSD's bcrypt() password hashing algorithm
Group: Development/Languages
License: MIT
URL: https://github.com/codahale/bcrypt-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby-devel 
# BuildRequires: rubygem(rake-compiler) => 0.9.2
# BuildRequires: rubygem(rake-compiler) < 0.10
# BuildRequires: rubygem(rspec) >= 3
Provides: rubygem(%{gem_name}) = %{version}

%description
bcrypt() is a sophisticated and secure hash algorithm designed by The
OpenBSD project
for hashing passwords. The bcrypt Ruby gem provides a simple wrapper for
safely handling
passwords.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}/lib
#mkdir -p %{buildroot}%{gem_libdir}
# TODO: move the extensions
mv %{buildroot}%{gem_instdir}/lib/bcrypt_ext.so %{buildroot}%{gem_extdir_mri}/lib/
#mv %{buildroot}%{gem_instdir}/lib/shared_object.so %{buildroot}%{gem_libdir}
# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/



# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{gem_dir}
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/lib/bcrypt.rb
%doc %{gem_instdir}/lib/bcrypt/error.rb
%doc %{gem_instdir}/lib/bcrypt/password.rb
%doc %{gem_instdir}/lib/bcrypt/engine.rb

%changelog
* Mon Sep 08 2014 Roberto Akira Yokota <bob69xxx at gmail.com> - 3.1.7-1
- Initial package
