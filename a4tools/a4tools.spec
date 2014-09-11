# Generated from a4tools-1.2.7.gem by gem2rpm -*- rpm-spec -*-
%global gem_name a4tools

Name: rubygem-%{gem_name}
Version: 1.2.7
Release: 1%{?dist}
Summary: It's dangerous to go alone! Take this
Group: Development/Languages
License: Proprietary
URL: http://github.com/acres4/a4tools
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(io) 
Requires: rubygem(io-console) 
Requires: rubygem(json) => 1.7
Requires: rubygem(json) < 2
Requires: rubygem(logger) => 1.2
Requires: rubygem(logger) < 2
Requires: rubygem(trollop) => 2.0
Requires: rubygem(trollop) < 3
Requires: rubygem(eventmachine) => 1.0
Requires: rubygem(eventmachine) < 2
Requires: rubygem(colorize) = 0.7
Requires: rubygem(jebediah) => 1.0
Requires: rubygem(jebediah) < 2
Requires: rubygem(faye-websocket) = 0.7
Requires: rubygem(talk) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A series of tools to make life better at Acres 4.0.


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


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{_bindir}/deploy_latest_clients
%{_bindir}/devsite_config_server
%{_bindir}/netshell
%{_bindir}/update_server
%{_bindir}/usher
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Thu Sep 11 2014 root - 1.2.7-1
- Initial package
