%global gem_name google-api-client

Name: rubygem-%{gem_name}
Version: 0.7.1
Release: 1%{?dist}
Summary: Package Summary
Group: Development/Languages
License: Apache 2.0
URL: https://github.com/google/google-api-ruby-client
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(signet) >= 0.5.0
Requires: rubygem(addressable) >= 2.3.2
Requires: rubygem(uuidtools) >= 2.1.0
Requires: rubygem(autoparse) >= 0.3.3
Requires: rubygem(faraday) >= 0.9.0
Requires: rubygem(multi_json) >= 1.0.0
Requires: rubygem(extlib) >= 0.9.15
Requires: rubygem(jwt) >= 0.1.5
Requires: rubygem(retriable) >= 1.4
Requires: rubygem(launchy) >= 2.1.1
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
# BuildRequires: rubygem(rspec) >= 2.11.0
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
The Google API Ruby Client makes it trivial to discover and access supported
APIs.


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
%doc %{gem_instdir}/README.md

%changelog
* Fri Sep 12 2014 Roberto Akira Yokota <bob69xxx @gmail.com> - 0.7.1-1
- Initial package
