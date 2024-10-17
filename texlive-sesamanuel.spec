Name:		texlive-sesamanuel
Version:	36613
Release:	2
Summary:	Class and package for sesamath books or paper
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sesamanuel
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sesamanuel.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sesamanuel.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sesamanuel.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package contains a sesamanuel class which could be used to
compose a student's classroom book with LaTeX, and also a
sesamanuelTIKZ style to be used for TikZ pictures in the
sesamath book.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/sesamanuel
%{_texmfdistdir}/tex/latex/sesamanuel
%doc %{_texmfdistdir}/doc/latex/sesamanuel

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
