%global tl_name pdfsync
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Provide links between source and PDF
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pdfsync
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfsync.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfsync.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package runs with pdfTeX or XeTeX, and creates an auxiliary file
with geometrical information to permit references back and forth between
source and PDF, assuming a conforming editor and PDF viewer.

