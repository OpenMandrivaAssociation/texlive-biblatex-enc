Name:		texlive-biblatex-enc
Version:	44627
Release:	2
Summary:	BibLaTeX style for the Ecole nationale des chartes (Paris)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-enc
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-enc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-enc.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a citation and bibliography style for use
with BibLaTeX. It conforms to the bibliographic standards used
at the Ecole nationale des chartes (Paris), and may be suitable
for a more general use in historical and philological works.
The package was initially derived from historische-zeitschrift,
with the necessary modifications.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-enc
%doc %{_texmfdistdir}/doc/latex/biblatex-enc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
