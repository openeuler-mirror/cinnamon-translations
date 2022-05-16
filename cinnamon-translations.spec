%global _trans_version 2018.12.11

Name:           cinnamon-translations
Version:        5.2.2
Release:        1
Summary:        Translations for Cinnamon and Nemo
License:        GPLv2+
URL:            https://github.com/linuxmint/%{name}
Source0:        https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        http://packages.linuxmint.com/pool/main/m/mint-translations/mint-translations_%{_trans_version}.tar.xz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  make

%description
Translations for Cinnamon, Nemo and Mintlocale.

%prep
%autosetup -a 1 -p 1

%build
%{make_build}
%{make_build} -C mint-translations

%install
# install mint translations for mintlocale
%{_bindir}/find mint-translations -not -name 'mintlocale.mo' -type f -delete
%{_bindir}/find . -name 'cinnamon-bluetooth.mo' -type f -delete
%{__cp} -pr mint-translations/%{_datadir}/linuxmint/locale .%{_datadir}
%{__cp} -pr .%{_prefix} %{buildroot}

%find_lang cinnamon
%find_lang mintlocale
%find_lang nemo
%find_lang nemo-extensions
%find_lang cinnamon-control-center
%find_lang cinnamon-screensaver
%find_lang cinnamon-session
%find_lang cinnamon-settings-daemon

%files -f cinnamon.lang -f mintlocale.lang -f nemo.lang -f nemo-extensions.lang -f cinnamon-control-center.lang -f cinnamon-screensaver.lang -f cinnamon-session.lang -f cinnamon-settings-daemon.lang
%license COPYING

%changelog
* Fri May 6 2022 lin zhang <lin.zhang@turbolinux.com.cn> - 5.2.2-1
- Upgrade to 5.2.2

* Mon Jul 27 2020 wangyue <wangyue92@huawei.com> - 4.4.2-1
- package init
