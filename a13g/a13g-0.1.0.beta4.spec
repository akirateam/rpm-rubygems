# Generated from a13g-0.1.0.beta4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name a13g

Name: rubygem-%{gem_name}
Version: 0.1.0.beta4
Release: 1%{?dist}
Summary: Event-driven architecture for your applications
Group: Development/Languages
License: 
URL: http://github.com/kriss/a13g
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) > 1.3.1
Requires: rubygem(activesupport) >= 2.0.0
BuildRequires: ruby(release)
BuildRequires: rubygems-devel > 1.3.1
BuildRequires: ruby 
# BuildRequires: rubygem(rspec) >= 1.2.9
# BuildRequires: rubygem(yard) 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A13g allows you to use event-driven architecture in your applications It can
be
used for enterprise integration with frameworks like JMS and products 
such as ActiveMQ. .


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
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.rdoc

%changelog
* Wed Sep 10 2014 root - 0.1.0.beta4-1
- Initial package
