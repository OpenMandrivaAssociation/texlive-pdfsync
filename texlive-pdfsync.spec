# revision 20373
# category Package
# catalog-ctan /macros/latex/contrib/pdfsync
# catalog-date 2010-11-08 21:04:31 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-pdfsync
Version:	20101108
Release:	1
Summary:	Provide links between source and PDF
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdfsync
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfsync.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfsync.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package runs with pdfTeX or XeTeX, and creates an auxiliary
file with geometrical information to permit references back and
forth between source and PDF, assuming a conforming editor and
PDF viewer.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pdfsync/pdfsync.sty
%doc %{_texmfdistdir}/doc/latex/pdfsync/README
%doc %{_texmfdistdir}/doc/latex/pdfsync/pdfsync-doc.pdf
%doc %{_texmfdistdir}/doc/latex/pdfsync/pdfsync-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
