%global gem_name select2-rails

Name: rubygem-%{gem_name}
Version: 3.5.9.1
Release: 1%{?dist}
Summary: Integrate Select2 javascript library with Rails asset pipeline
Group: Development/Languages
License: MIT
URL: https://github.com/argerim/select2-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(thor) => 0.14
Requires: rubygem(thor) < 1
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
# BuildRequires: rubygem(rails) >= 3.0
# BuildRequires: rubygem(httpclient) => 2.2
# BuildRequires: rubygem(httpclient) < 3
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Select2 is a jQuery based replacement for select boxes. It supports searching,
remote data sets, and infinite scrolling of results. This gem integrates
Select2 with Rails asset pipeline for easy of use.


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
* Sun Sep 07 2014 Roberto Akira Yokota <bob69xxx at gmail.com> - 3.5.9.1-1
- Initial package
