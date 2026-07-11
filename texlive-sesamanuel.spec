%global tl_name sesamanuel
%global tl_revision 36613

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6
Release:	%{tl_revision}.1
Summary:	Class and package for sesamath books or paper
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sesamanuel
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sesamanuel.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sesamanuel.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sesamanuel.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package contains a sesamanuel class which could be used to compose a
student's classroom book with LaTeX, and also a sesamanuelTIKZ style to
be used for TikZ pictures in the sesamath book.

