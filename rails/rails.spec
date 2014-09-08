%global gem_name rails

Name: rubygem-%{gem_name}
Version: 4.0.9
Release: 1%{?dist}
Summary: Full-stack web application framework
Group: Development/Languages
License: MIT
URL: http://www.rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) >= 1.8.11
Requires: rubygem(activesupport) = 4.0.9
Requires: rubygem(actionpack) = 4.0.9
Requires: rubygem(activerecord) = 4.0.9
Requires: rubygem(actionmailer) = 4.0.9
Requires: rubygem(railties) = 4.0.9
Requires: rubygem(bundler) >= 1.3.0
Requires: rubygem(bundler) < 2.0
Requires: rubygem(sprockets-rails) => 2.0
Requires: rubygem(sprockets-rails) < 3
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.8.11
BuildRequires: ruby >= 1.9.3
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Ruby on Rails is a full-stack web framework optimized for programmer happiness
and sustainable productivity. It encourages beautiful code by favoring
convention over configuration.


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
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Mon Sep 08 2014 Roberto Akira Yokota <bob69xxx at gmail.com> - 4.0.9-1
- Initial package
