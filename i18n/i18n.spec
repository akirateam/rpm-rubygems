%global gem_name i18n

Name: rubygem-%{gem_name}
Version: 0.7.0.beta1
Release: 1%{?dist}
Summary: New wave Internationalization support for Ruby
Group: Development/Languages
License: MIT
URL: http://github.com/svenfuchs/i18n
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) >= 1.3.5
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.5
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
New wave Internationalization support for Ruby.


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
* Tue Sep 09 2014 Roberto Akira Yokota <bob69xxx at gmail.com>- 0.7.0.beta1-1
- Initial package
