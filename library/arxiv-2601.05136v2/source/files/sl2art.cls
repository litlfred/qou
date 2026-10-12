%%
%% This is file `sl2art.cls',
%% generated with the docstrip utility.
%%
%% The original source files were:
%%
%% sl2art.dtx  (with options: `class')
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
\ProvidesExplClass{sl2art}{2024-04-28}{v0.3}{a one-and-a-half-column article class for mathematics}
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
\LoadClass[10pt,oneside]{article}
\RequirePackage[
  includeall,
  marginparwidth=2in,
  marginparsep=0.25in,
  width=7.5in,
  height=9in
]{geometry}
\RequirePackage[T1]{fontenc}
\RequirePackage{microtype}
\RequirePackage{cochineal}
\RequirePackage[scaled=0.80]{beramono}
\RequirePackage{xcolor}
\definecolor{accent}{HTML}{914E0F}
\definecolor{link}{HTML}{105C9C}
\definecolor{slred}{HTML}{FA3F2D}
\definecolor{slyellow}{HTML}{F08813}
\definecolor{slgreen}{HTML}{01F556}
\definecolor{slblue}{HTML}{30A4FF}
\definecolor{slpurple}{HTML}{AD2BF0}
\NewDocumentCommand{\defemph}{m}{{\color{accent}\emph{#1}}}
\RequirePackage[oneside]{sidenotes}
\RequirePackage{marginfix}
\NewDocumentCommand{\note}{m}{
  \sidenote{
    \def\@captype{sidenote}
    \footnotesize #1
    \undef\@captype
  }
}
\RequirePackage{titletoc}
\titlecontents{part}[1.5em]
  {\vspace{2pt}}
  {\scshape \contentslabel{2.3em}}
  {\scshape Part }
  {\titlerule*[1pc]{}\contentspage}[\vspace{2pt}]
\titlecontents{section}[3.8em] % ie, 1.5em (part) + 2.3em
  {}
  {\contentslabel{2.3em}}
  {\hspace*{-2.3em}}
  {\titlerule*[1pc]{}\contentspage}
\titlecontents{subsection}[5.3em] % ie, 3.8em (section) + 2.3em
  {}
  {\contentslabel{2.3em}}
  {\hspace*{-2.3em}}
  {\titlerule*[1pc]{}\contentspage}
\titlecontents{subsubsection}[7.6em] % ie, 5.3em (subsection) + 2.3em
  {}
  {\contentslabel{2.3em}}
  {\hspace*{-2.3em}}
  {\titlerule*[1pc]{}\contentspage}

\RequirePackage[pagestyles]{titlesec}
\titleformat{\part}{\scshape}{Part \thepart:\@}{.5em}{}
\titleformat{\section}{\scshape }{\color{accent} \thesection.\@}{.5em}{\color{accent}}
\titleformat{\subsection}{\itshape }{\color{accent} \thesubsection.\@}{.5em}{\color{accent}}
\titleformat{\subsubsection}[runin]{}{\color{accent} \thesubsubsection.\@}{.5em}{\color{accent}}

\newpagestyle{main}{
  \sethead[][][]{\scshape \ifthesection{\thesection.}{}~\sectiontitle}{}{\thepage}
}
\pagestyle{main}
\renewcommand{\descriptionlabel}[1]{\hspace{\labelsep}\scshape{#1}}
\bool_if:NTF \g_sl_margincite_bool
{
  \RequirePackage[style=alphabetic-side,maxnames=5,minnames=5]{biblatex}
}
{
  \RequirePackage[style=alphabetic,maxnames=5,minnames=5]{biblatex}
}
\RequirePackage{amsthm,amssymb}
\RequirePackage{thmtools}
\declaretheoremstyle[
  headfont=\scshape,
  qed=$\lrcorner$,
  parent=section,
]{theorem}
\declaretheoremstyle[
  headfont=\scshape,
  qed=$\lrcorner$,
  name='Theorem'
]{bigtheorem}
\declaretheoremstyle[
  headfont=\scshape,
  parent=section,
]{definition}
\tl_new:N \g_sl_title_tl
\RenewDocumentCommand{\title}{o m}{ \tl_set:Nn \g_sl_title_tl {#2} }

\tl_new:N \g_sl_subjclass_tl
\tl_new:N \g_sl_subjclassYear_tl
\NewDocumentCommand{\subjclass}{O{2020} m}{
  \tl_set:Nn \g_sl_subjclass_tl {#2}
  \tl_set:Nn \g_sl_subjclassYear_tl {#1}
}

\tl_new:N \g_sl_keywords_tl
\NewDocumentCommand{\keywords}{m}{ \tl_set:Nn \g_sl_keywords_tl {#1} }

\tl_new:N \g_sl_abstract_tl
\RenewDocumentEnvironment{ abstract }{ +b }{ \tl_gset:Nn \g_sl_abstract_tl {#1} }{ }
\seq_new:N \g_sl_author_seq
\seq_new:N \g_sl_address_seq
\seq_new:N \g_sl_email_seq
\RenewDocumentCommand{\author}{m}{
  \seq_put_right:Nn \g_sl_author_seq {#1}
  \seq_put_right:Nn \g_sl_address_seq {}
  \seq_put_right:Nn \g_sl_email_seq {}
}
\NewDocumentCommand{\address}{m}{
  \seq_set_item:Nnn \g_sl_address_seq {-1} {#1}
}
\NewDocumentCommand{\email}{m}{
  \seq_set_item:Nnn \g_sl_email_seq {-1} {#1}
}
\tl_new:N \l_sl_curr_author_tl
\tl_new:N \l_sl_curr_address_tl
\tl_new:N \l_sl_curr_email_tl
\cs_gset:Nn \g_sl_maketitle:
{
  \bool_if:NTF \g_sl_titlepage_bool
  {
    \begin{titlepage}
    \newgeometry{margin=1.5in}
  }{}
    \thispagestyle{empty}
    \parindent=0pt
    \parskip=12pt
    { \large \scshape \g_sl_title_tl }
    \par

    \begin{minipage}{\textwidth}
      \bool_until_do:nn {\seq_if_empty_p:N \g_sl_author_seq} {
        \seq_pop_left:NN \g_sl_author_seq {\l_sl_curr_author_tl}
        \seq_pop_left:NN \g_sl_address_seq {\l_sl_curr_address_tl}
        \seq_pop_left:NN \g_sl_email_seq {\l_sl_curr_email_tl}
        \l_sl_curr_author_tl
        \tl_if_empty:NTF \l_sl_curr_address_tl {} {
          \par
          {\scshape \l_sl_curr_address_tl}
        }
        \tl_if_empty:NTF \l_sl_curr_email_tl {} {
          \par
          \href{mailto:\l_sl_curr_email_tl}{\l_sl_curr_email_tl}
        }
        \\[10pt]
      }
      \vspace{-2em}
    \end{minipage}


    \tl_if_empty:NTF \g_sl_abstract_tl {} {
      \begin{center}
      \begin{minipage}{4in}
      {\centering \scshape \color{accent} Abstract \\ }
        \g_sl_abstract_tl
      \end{minipage}
      \end{center}
    }
    \bool_if:NTF \g_sl_draft_bool {
      \begin{center}
        {\color{slred} \large DRAFT:~Not~for~distribution }
      \end{center}
    } {}
  \bool_if:NTF \g_sl_titlepage_bool {\vfill}{\par}
  \tl_if_empty:NTF \g_sl_subjclass_tl {} {
    {\itshape {\g_sl_subjclassYear_tl}~Mathematics~Subject~Classification:~}
    \g_sl_subjclass_tl
    \par
  }
  \tl_if_empty:NTF \g_sl_keywords_tl {} {{\itshape Key~words~and~phrases:}~ \g_sl_keywords_tl }
  \bool_if:NTF \g_sl_titlepage_bool
  {
    \end{titlepage}
  }{}
  \parskip=0pt
  \parindent=1.5em
}
\RenewDocumentCommand{\maketitle}{}{\g_sl_maketitle:}
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
\endinput
%%
%% End of file `sl2art.cls'.
