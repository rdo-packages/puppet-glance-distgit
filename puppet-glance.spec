%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-glance
Version:        9.5.0
Release:        1%{?dist}
Summary:        Puppet module for OpenStack Glance
License:        Apache-2.0

URL:            https://launchpad.net/puppet-glance

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

Patch0001:      0001-Ensure-that-swiftclient-is-installed.patch

BuildArch:      noarch

Requires:       puppet-inifile
Requires:       puppet-keystone
Requires:       puppet-openstacklib
Requires:       puppet-oslo
Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Puppet module for OpenStack Glance

%prep
%setup -q -n openstack-glance-%{upstream_version}

#TODO(karelyatin) remove when merged https://review.openstack.org/#/c/471197/
patch0001 -p1

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/glance/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/glance/



%files
%{_datadir}/openstack-puppet/modules/glance/


%changelog
* Thu Feb 02 2017 Alfredo Moralejo <amoralej@redhat.com> 9.5.0-1
- Update to 9.5.0

* Thu Sep 29 2016 Alfredo Moralejo <amoralej@redhat.com> 9.4.0-1
- Update to 9.4.0

* Wed Sep 21 2016 Haikel Guemar <hguemar@fedoraproject.org> 9.3.0-1
- Update to 9.3.0

* Fri Sep 16 2016 Haikel Guemar <hguemar@fedoraproject.org> 9.2.0-1
- Update to 9.2.0


