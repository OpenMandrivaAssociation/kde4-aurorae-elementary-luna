%define	oname	ElementaryLunaAurorae
Summary:	Elementary Luna, an Aurorae theme for KDE 4
Name:		kde4-aurorae-elementary-luna
Version:	1.5
Release:	1
Source0:	%{oname}-%{version}.tar.gz
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		http://www.rosalinux.com
BuildArch:	noarch

%description
This is a port of the Elementary Luna window decoration to Aurorae, for KDE
users. It even includes the huge drop shadows!

All artistic credit goes to Dan Rabbit and the Elementary team.

%prep
%setup -q -n %{oname}

%build

%install
install -d %{buildroot}%{_datadir}/apps/aurorae/themes/%{oname}
cp -a * %{buildroot}%{_datadir}/apps/aurorae/themes/%{oname}/

%files
%dir %{_datadir}/apps/aurorae/themes/%{oname}
%{_datadir}/apps/aurorae/themes/%{oname}/*
