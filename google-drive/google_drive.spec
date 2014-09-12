%global gem_name google_drive

Name: rubygem-%{gem_name}
Version: 0.3.10
Release: 1%{?dist}
Summary: A library to read/write files/spreadsheets in Google Drive/Docs
Group: Development/Languages
License: New BSD
URL: https://github.com/gimite/google-drive-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(nokogiri) >= 1.4.4
Requires: rubygem(nokogiri) < 1.5.1
Requires: rubygem(nokogiri) > 1.5.1
Requires: rubygem(nokogiri) < 1.5.2
Requires: rubygem(nokogiri) > 1.5.2
Requires: rubygem(oauth) >= 0.3.6
Requires: rubygem(oauth2) >= 0.5.0
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A library to read/write files/spreadsheets in Google Drive/Docs.


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
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/doc_src/google_drive/acl.rb
%doc %{gem_instdir}/doc_src/google_drive/acl_entry.rb

%changelog
* Fri Sep 12 2014 Roberto Akira Yokota <bob69xxx @gmail.com> - 0.3.10-1
- Initial package
