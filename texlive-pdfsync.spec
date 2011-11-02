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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package runs with pdfTeX or XeTeX, and creates an auxiliary
file with geometrical information to permit references back and
forth between source and PDF, assuming a conforming editor and
PDF viewer.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
