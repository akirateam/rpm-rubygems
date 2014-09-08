%global gem_name truncate_html

Name: rubygem-%{gem_name}
Version: 0.9.2
Release: 1%{?dist}
Summary: Uses an API similar to Rails' truncate helper to truncate HTML and close any lingering open tags
Group: Development/Languages
License: MIT-LICENSE 
URL: https://github.com/hgimenez/truncate_html
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby >= 1.9
# BuildRequires: rubygem(rspec-rails) => 2.9
# BuildRequires: rubygem(rspec-rails) < 3
# BuildRequires: rubygem(rails) => 3.0.3
# BuildRequires: rubygem(rails) < 3.1
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Truncates html so you don't have to.


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
* Sun Sep 07 2014 Roberto AKira Yokota <bob69xxx at gmail.com> - 0.9.2-1
- Initial package
