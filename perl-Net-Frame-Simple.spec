%define upstream_name    Net-Frame-Simple
%define upstream_version 1.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:    BSD loopback layer object
License:    Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Bit::Vector)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Net::IPv6Addr)
BuildRequires: perl(Socket6)
BuildRequires: perl(Net::Frame)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
*Net::Frame* is a fork of *Net::Packet*. The goal here was to greatly
simplify the use of the frame crafting framework. *Net::Packet* does many
things undercover, and it was difficult to document all the thingies.

Also, *Net::Packet* may suffer from unease of use, because frames were
assembled using layers stored in L2, L3, L4 and L7 attributes. *Net::Frame*
removes all this, and is splitted in different modules, for those who only
want to use part of the framework, and not whole framework.

Finally, anyone can create a layer, and put it on his CPAN space, because
of the modularity *Net::Frame* offers. For an example, see
*Net::Frame::Layer::ICMPv4* on my CPAN space.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
make test verbose=1

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


