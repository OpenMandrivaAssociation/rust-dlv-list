%define debug_package %{nil}
%bcond_without check

%global crate dlv-list

Name:           rust-%{crate}
Version:        0.3.0
Release:        1
Summary:        Semi-doubly linked list implemented using a vector

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/dlv-list
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Semi-doubly linked list implemented using a vector.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(dlv-list) = 0.3.0
Requires:       cargo

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc RELEASES.md README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(dlv-list/default) = 0.3.0
Requires:       cargo
Requires:       crate(dlv-list) = 0.3.0

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
