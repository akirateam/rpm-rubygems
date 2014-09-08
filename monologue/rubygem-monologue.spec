%global gem_name monologue

Name: rubygem-%{gem_name}
Version: 0.4.1
Release: 1%{?dist}
Summary: Monologue is a basic blogging engine. It is a Rails mountable engine so it can be mounted in any 4.0.X + apps
Group: Development/Languages
License: MIT-LICENSE 
URL: http://github.com/jipiboily/monologue
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(rails) >= 4.0.4
Requires: rubygem(bcrypt) => 3.1.7
Requires: rubygem(bcrypt) < 3.2
Requires: rubygem(coffee-rails) => 4.0.0
Requires: rubygem(coffee-rails) < 4.1
Requires: rubygem(sass-rails) => 4.0.0
Requires: rubygem(sass-rails) < 4.1
Requires: rubygem(truncate_html) 
Requires: rubygem(jquery-rails) 
Requires: rubygem(ckeditor) => 4.0.11
Requires: rubygem(ckeditor) < 4.1
Requires: rubygem(select2-rails) => 3.2
Requires: rubygem(select2-rails) < 4
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
# BuildRequires: rubygem(rspec-rails) => 2.8
# BuildRequires: rubygem(rspec-rails) < 3
# BuildRequires: rubygem(factory_girl_rails) => 1.4.0
# BuildRequires: rubygem(factory_girl_rails) < 1.5
# BuildRequires: rubygem(capybara) => 1.1.4
# BuildRequires: rubygem(capybara) < 1.2
# BuildRequires: rubygem(capybara-webkit) 
# BuildRequires: rubygem(shoulda) 
# BuildRequires: rubygem(guard-rspec) 
# BuildRequires: rubygem(database_cleaner) => 0.9.1
# BuildRequires: rubygem(database_cleaner) < 0.10
# BuildRequires: rubygem(mysql2) 
# BuildRequires: rubygem(sqlite3) 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Monologue is a basic blogging engine. It is a Rails mountable engine so it can
be mounted in any 4.0.X + apps.


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
* Fri Sep 05 2014 Roberto Akira Yokota <bob69xxx at gmail.com> - 0.4.1-1
- Initial package
