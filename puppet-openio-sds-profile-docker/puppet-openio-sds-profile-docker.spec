Name:		puppet-openio-sds-profile-docker
Version:	%(date +"%Y%m%d")
Release:	1%{?dist}
Summary:	OpenIO profile for Docker

Group:		openio
License:	Apache 2.0
URL:		http://www.openio.io/
Source0:	https://github.com/open-io/puppet-openiosds-profile-docker/archive/master.tar.gz
BuildArch:	noarch

#BuildRequires:	
Requires:	puppet-openio-sds-profile


%description
OpenIO profile using Puppet for Docker.


%prep
%setup -q -n puppet-openiosds-profile-docker-master


%build


%install
%{__mkdir_p} $RPM_BUILD_ROOT/%{_datarootdir}/puppet/modules/openiosds/profiles/docker
%{__cp} -a * $RPM_BUILD_ROOT/%{_datarootdir}/puppet/modules/openiosds/profiles/docker


%files
%defattr(-,root,root,-)
%{_datarootdir}/puppet/modules/openiosds/profiles/docker


%changelog
* Wed Sep 02 2015 - 20150902-1 - Romain Acciari <romain.acciari@openio.io>
- New release
* Thu Jun 18 2015 - 20150618-1 - Romain Acciari <romain.acciari@openio.io>
- Initial release
