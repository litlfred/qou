%%
%% This is file `sl2ams.cls',
%% generated with the docstrip utility.
%%
%% The original source files were:
%%
%% sl2ams.dtx  (with options: `class')
%% 
%% This is a generated file.
%% 
%% Copyright (C) 2024 Calvin McPhail-Snyder
%% 
%% --------------------------------
%% 
%% This file may be distributed and/or modified under the
%% conditions of the LaTeX Project Public License, either version 1.3
%% of this license or (at your option) any later version.
%% The latest version of this license is in:
%% 
%% 
%% http://www.latex-project.org/lppl.txt
%% 
%% and version 1.3c or later is part of all distributions of LaTeX
%% version 2008-05-04 or later.
%% 
\NeedsTeXFormat{LaTeX2e}[2023-11-01]
\ProvidesExplClass{sl2ams}{2024-02-12}{v0.1}{a compatibility layer for using AMS article style}
\RequirePackage{expl3,l3keys2e}
\keys_define:nn{ sl }
  {
    draft .bool_set:N = \g_sl_draft_bool,
    draft .initial:n = false,
    draft .default:n = true,
    margincite .bool_set:N = \g_sl_margincite_bool,
    margincite .initial:n = true,
    margincite .default:n = true,
    titlepage .bool_set:N = \g_sl_titlepage_bool,
    titlepage .initial:n = true,
    titlepage .default:n = true,
  }
\ProcessKeysOptions{ sl }
\LoadClass[12pt]{amsart}
\RequirePackage[T1]{fontenc}
\RequirePackage{microtype}
\RequirePackage{xcolor}
\definecolor{accent}{HTML}{914E0F}
\definecolor{link}{HTML}{105C9C}
\definecolor{slred}{HTML}{FA3F2D}
\definecolor{slyellow}{HTML}{F08813}
\definecolor{slgreen}{HTML}{01F556}
\definecolor{slblue}{HTML}{30A4FF}
\definecolor{slpurple}{HTML}{AD2BF0}
\NewDocumentCommand{\defemph}{m}{{\emph{#1}}}
\NewDocumentCommand{\note}{m}{\footnote{#1}}
\NewDocumentEnvironment{marginfigure}{ o }{\begin{figure}}{\end{figure}}
\NewDocumentEnvironment{margintable}{ o }{\begin{table}}{\end{table}}
\RequirePackage[style=numeric]{biblatex}
\RequirePackage{amsthm,amssymb,mathtools}
\RequirePackage{thmtools}
\declaretheoremstyle[
  spaceabove=\topsep,
  spacebelow=\topsep,
  bodyfont=\itshape,
  headfont=\bfseries,
  headpunct={.},
  postheadspace={5pt plus 1pt minus 1pt},
  parent=section,
]{theorem}
\declaretheoremstyle[
  spaceabove=\topsep,
  spacebelow=\topsep,
  bodyfont=\itshape,
  headfont=\bfseries,
  headpunct={.},
  postheadspace={5pt plus 1pt minus 1pt},
]{bigtheorem}
\declaretheoremstyle[
  spaceabove=\topsep,
  spacebelow=\topsep,
  headfont=\bfseries,
  headpunct={.},
  postheadspace={5pt plus 1pt minus 1pt},
  parent=section,
  qed=$\lrcorner$,
]{definition}
\RequirePackage{hyperref}
\hypersetup{
  colorlinks=true,
  citecolor=link,
  linkcolor=link,
  menucolor=link,
  linktocpage=true,
  urlcolor=link,
  draft=false
}

\RequirePackage[noabbrev,capitalize]{cleveref}
\crefname{equation}{equation}{equations}
\Crefname{equation}{Equation}{Equations}

\endinput
%%
%% End of file `sl2ams.cls'.
