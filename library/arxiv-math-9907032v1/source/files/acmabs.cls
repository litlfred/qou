%%% ====================================================================
%%%  @LaTeX-file{
%%%     filename        = "acmabs.cls",
%%%     version         = "1.00",
%%%     date            = "12 September 1995",
%%%     time            = "13:37:29 EDT",
%%%     author          = "David M. Jones",
%%%     address         = "Journal of the ACM
%%%                        MIT Laboratory for Computer Science
%%%                        Room NE43-316
%%%                        545 Technology Square
%%%                        Cambridge, MA 02139
%%%                        USA",
%%%     telephone       = "(617) 253-5936",
%%%     FAX             = "(617) 253-3480",
%%%     checksum        = "62308 187 417 5324",
%%%     email           = "jacm@theory.lcs.mit.edu",
%%%     codetable       = "ISO/ASCII",
%%%     keywords        = "",
%%%     supported       = "yes",
%%%     docstring       = "The checksum field above contains a CRC-16
%%%                        checksum as the first value, followed by the
%%%                        equivalent of the standard UNIX wc (word
%%%                        count) utility output of lines, words, and
%%%                        characters.  This is produced by Robert
%%%                        Solovay's checksum utility.",
%%%  }
%%% ====================================================================

\def\fileversion{v1.0}
\def\filedate{1995/09/12}
\def\docdate {12 September 1995}

\NeedsTeXFormat{LaTeX2e}

\ProvidesClass{acmabs}[\filedate\space\fileversion\space ACM abstract
class (dmj)]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}

\ProcessOptions\relax

\LoadClass{article}

\textheight 47pc
\textwidth 30pc

\parindent\z@

\newcommand{\refkey}{\gdef\@refkey}
\let\@refkey\@empty

\newcommand{\Journal}{\gdef\@journal}
\let\@journal\@empty

\newcommand{\Pages}{\gdef\@pages}
\let\@pages\@empty

\newcommand{\Month}{\gdef\@month}
\let\@month\@empty

\newcommand{\Year}{\gdef\@year}
\let\@year\@empty

\newcommand{\Volume}{\gdef\@volume}
\let\@volume\@empty

\newcommand{\Number}{\gdef\@number}
\let\@number\@empty

\newcommand{\Received}{\gdef\@received}
\let\@received\@empty

\newcommand{\note}{\gdef\@note}
\let\@note\@empty

\newcount\@numands

\renewcommand{\and}{%
    \par
    \advance\@tempcnta\@ne
    \ifnum\@tempcnta=\@numands
        \bigskip
        AND
        \bigskip
    \else
        \bigskip
    \fi
    \par
}

\pagestyle{empty}

\def\@oddhead{%
    \begingroup
        \normalfont
        \footnotesize
        Journal of the Association for Computing Machinery,\space
        \ifx\@volume\@empty
            (To appear. Final manuscript received \@received)%
        \else
            Vol.\ \@volume, No.\ \@number, \@month\ \@year
            \ifx\@pages\@empty \else , pp.\ \@pages. \fi
            \ifx\@note\@empty \else \ (\@note) \fi
        \fi
    \endgroup
    \hfill
}

\renewcommand{\maketitle}{%
    \par
    \suppressfloats[t]%
    \begingroup
        \bfseries\Large\raggedright
        \@title\par\bigskip
    \endgroup
    \begingroup
        \@numands\z@
        \def\and{\global\advance\@numands\@ne}%
        \setbox\z@\hbox{\@author}%
        \let\and\relax
    \endgroup
    \begingroup
        \@tempcnta\z@
        \expandafter\uppercase\expandafter{\@author}%
    \endgroup
    \begin{figure}[!b]\small
    Copyright \@year\ by ACM, Inc.
    Permission to make digital or hard copies of part or all of this
    work for personal or classroom use is granted without fee provided
    that copies are not made or distributed for profit or direct
    commercial advantage and that copies bear this notice and the full
    citation on the first page. Copyrights for components of this work
    owned by others than ACM must be honored. Abstracting with credit
    is permitted. To copy otherwise, to republish, to post on servers,
    or to redistribute to lists, requires prior specific permission
    and/or a fee. Request permissions from Publications Dept, ACM
    Inc., fax +1 (212) 869-0481, or \texttt{permissions@acm.org}.
    \end{figure}
}

\renewenvironment{abstract}
               {\trivlist
                \parskip \z@ \@plus\p@
                \parindent10\p@
                \small
                \item[\hskip\labelsep Abstract.]\ignorespaces}
               {\endtrivlist}

\newenvironment{categories}
               {\trivlist
                \parskip \z@ \@plus\p@
                \parindent10\p@
                \small
                \emergencystretch5\p@
                \item[%
                    \hskip\labelsep
                    Categories and Subject Descriptors.%
                ]%
                        \ignorespaces
               }
               {\endtrivlist}

\newenvironment{terms}
               {\trivlist
                \parskip \z@ \@plus\p@
                \parindent10\p@
                \small
                \item[\hskip\labelsep General Terms.]\ignorespaces}
               {\endtrivlist}

\newenvironment{keywords}
               {\trivlist
                \parskip \z@ \@plus\p@
                \parindent10\p@
                \small
                \item[%
                    \hskip\labelsep
                    Additional Key words and Phrases.%
                ]%
                \ignorespaces}
               {\endtrivlist}


\nofiles

\endinput
