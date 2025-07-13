Name:           bagre
Version:        1.0
Release:        1%{?dist}
Summary:        Navegador Bagre for GNOME com GTK e WebKit2

License:        MIT
URL:            https://bagremedicina.netlify.app/
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       python3
Requires:       python3-gobject
Requires:       gtk4
Requires:       webkit2gtk4

%description
Aplicativo GTK em Python que abre o site Bagre Medicina usando WebKit2.

%prep
%autosetup

%build
# nenhum build necessário

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 bagre.py %{buildroot}/usr/bin/bagre

%files
%license LICENSE
/usr/bin/bagre

%changelog
* Dom Jul 13 2025 Victor <batatasdeliciosas2000@gmail.com> - 1.0-1
- Primeira versão do Bagre navegador GTK Python como RPM
