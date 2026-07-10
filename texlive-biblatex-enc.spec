%global tl_name biblatex-enc
%global tl_revision 73019

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	BibLaTeX style for the Ecole nationale des chartes (Paris)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-enc
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-enc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-enc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a citation and bibliography style for use with
BibLaTeX. It conforms to the bibliographic standards used at the Ecole
nationale des chartes (Paris), and may be suitable for a more general
use in historical and philological works. The package was initially
derived from historische-zeitschrift, with the necessary modifications.

