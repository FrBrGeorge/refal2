Name:		refal2
Version:	0.2.3
Release:	alt2
Summary:	Functional programming language, oriented on symbolic information processing
Group:		Development/Functional
License:	BSD-like
URL:		https://github.com/FrBrGeorge/refal2
Source:		%name-%version.tar.gz

# Automatically added by buildreq on Sat Jun 15 2019
# optimized out: i586-glibc-core i586-glibc-devel i586-libgcc1 python-base sh4
BuildRequires: gcc
%ifarch x86_64
BuildRequires: i586-gcc8
%filter_from_requires s/^\/lib\/lib/lib/
%endif

%description
Refal (REcursive Function Agorithmic Language) is a functional
programming language, oriented on symbolic information processing. It
was created in 60-s of XX century by V.F.Turchin (in former the USSR) as
"metalanguage" to describe other languages semantics. But the language
also proved to be an useful working instrument for programmers, who
solved the applied problems in various spheres of human activity.

Refal history is closely connected   with dramatic events in life of his
author, famous physicist, V.F.Turchin. You can get to know in detail
about Refal and about its author from site "Refal/Supercompilation
Community" www.refal.net (mirror www.refal.org).

After some time of calm, Refal begins to attract attention again as
convenient and elegant programming language, free from excessive
details, with simple and natural mechanism of pattern matching. Here and
further, if contrary won't be fixed, Refal-5 System will be considered
as definitive realization of Refal language

%prep
%setup

%build
make

%install
%makeinstall libdir=%buildroot%prefix/lib

%files
%doc doc *.txt
%_bindir/*
%_prefix/lib/*.*
%_includedir/*
%_datadir/%name


%changelog
* Sun Jun 16 2019 Fr. Br. George <george@altlinux.ru> 0.2.3-alt2
- Upstream switch to https://github.com/FrBrGeorge/refal2

* Sun Jun 16 2019 Fr. Br. George <george@altlinux.ru> 0.2.3-alt1
- Initial build for ALT

