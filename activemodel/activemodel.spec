%global gem_name activemodel

Name: rubygem-%{gem_name}
Version: 4.0.9
Release: 1%{?dist}
Summary: A toolkit for building modeling frameworks (part of Rails)
Group: Development/Languages
License: MIT
URL: http://www.rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(activesupport) = 4.0.9
Requires: rubygem(builder) => 3.1.0
Requires: rubygem(builder) < 3.2
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby >= 1.9.3
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A toolkit for building modeling frameworks like Active Record. Rich support
for attributes, callbacks, validations, observers, serialization,
internationalization, and testing.


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




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{gem_dir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Mon Sep 08 2014 Roberto Akira Yokota <bob69xxx at gmail.com> - 4.0.9-1
- Initial package
