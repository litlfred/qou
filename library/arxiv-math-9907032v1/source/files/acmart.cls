%% 
%% This is file `acmart.cls', generated on <1996/4/26> 
%% with the docstrip utility (2.2i).
%% 
%% The original source files were:
%% 
%% acmart.dtx  (with options: `cls,2e,bib,trans')
%% 
%% IMPORTANT NOTICE:
%% You are not allowed to distribute this file.
%% For distribution of the original source see
%% the copyright notice in the file acmart.dtx .
%% 
%% \CharacterTable
%%  {Upper-case    \A\B\C\D\E\F\G\H\I\J\K\L\M\N\O\P\Q\R\S\T\U\V\W\X\Y\Z
%%   Lower-case    \a\b\c\d\e\f\g\h\i\j\k\l\m\n\o\p\q\r\s\t\u\v\w\x\y\z
%%   Digits        \0\1\2\3\4\5\6\7\8\9
%%   Exclamation   \!     Double quote  \"     Hash (number) \#
%%   Dollar        \$     Percent       \%     Ampersand     \&
%%   Acute accent  \'     Left paren    \(     Right paren   \)
%%   Asterisk      \*     Plus          \+     Comma         \,
%%   Minus         \-     Point         \.     Solidus       \/
%%   Colon         \:     Semicolon     \;     Less than     \<
%%   Equals        \=     Greater than  \>     Question mark \?
%%   Commercial at \@     Left bracket  \[     Backslash     \\
%%   Right bracket \]     Circumflex    \^     Underscore    \_
%%   Grave accent  \`     Left brace    \{     Vertical bar  \|
%%   Right brace   \}     Tilde         \~}
\def\fileversion{v1.3h beta}
\def\filedate{1996/4/19}
\def\docdate {23 August 1995}
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{acmart}[\filedate\space\fileversion\space ACM
article class (dmj)]
\newif\if@faircopy
\@faircopyfalse

\DeclareOption{faircopy}{\@faircopytrue}

\DeclareOption{preprint}{\@faircopyfalse}

\DeclareOption{twocolumn}{%
    \PackageWarningNoLine{acmart}{twocolumn mode is not supported}%
}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}

\ProcessOptions\relax

\LoadClass{article}
\renewcommand{\normalsize}{%
    \@setfontsize\normalsize\@xpt\@xiipt
    \abovedisplayskip 6\p@ \@plus2\p@ \@minus\p@
    \belowdisplayskip \abovedisplayskip
    \abovedisplayshortskip 6\p@ \@minus 3\p@
    \belowdisplayshortskip 6\p@ \@minus 3\p@
    \let\@listi\@listI
}
\renewcommand{\small}{%
    \@setfontsize\small\@ixpt{11}%
    \abovedisplayskip 5\p@ \@plus 2\p@ \@minus \p@
    \belowdisplayskip \abovedisplayskip
    \abovedisplayshortskip 5\p@ \@minus 2\p@
    \belowdisplayshortskip 5\p@ \@minus 2\p@
    \def\@listi{%
        \leftmargin\leftmargini
        \topsep 5\p@ \@plus 2\p@ \@minus \p@
        \parsep \z@ \@plus .7\p@
        \itemsep 1.6\p@ \@plus .8\p@
    }%
}

\renewcommand{\footnotesize}{%
    \@setfontsize\footnotesize\@viiipt{9.5}%
    \abovedisplayskip 4\p@ \@plus \p@
    \belowdisplayskip \abovedisplayskip
    \abovedisplayshortskip 4\p@ \@minus \p@
    \belowdisplayshortskip 4\p@ \@minus \p@
    \def\@listi{%
        \leftmargin\leftmargini
        \topsep 4\p@ \@plus \p@
        \parsep \z@ \@plus .5\p@
        \itemsep \p@ \@plus .7\p@
    }%
}
\renewcommand{\scriptsize}{\@setfontsize\scriptsize\@viipt\@viipt}
\renewcommand{\tiny}{\@setfontsize\tiny\@vpt\@vpt}
\renewcommand{\large}{\@setfontsize\large\@xiipt\@xiipt}
\renewcommand{\Large}{\@setfontsize\Large\@xivpt\@xivpt}
\renewcommand{\LARGE}{\@setfontsize\LARGE\@xviipt\@xviipt}
\renewcommand{\huge}{\@setfontsize\huge\@xxpt\@xxpt}
\renewcommand{\Huge}{\@setfontsize\Huge\@xxvpt\@xxvpt}
\let\rom\textup
\normalsize

\oddsidemargin .75in
\evensidemargin .75in
\marginparwidth .5in
\marginparsep .125in
\topmargin .25in
\headheight 12pt
\headsep 16pt
\footskip 15pt

\textheight 47pc
\textwidth 30pc
\columnsep 10pt
\columnseprule 0pt

\footnotesep 7pt
\skip\footins 15pt plus 4pt minus 3pt

\floatsep 12pt plus 2pt minus 2pt
\textfloatsep \floatsep

\intextsep 1pc plus 1pc


\dblfloatsep 12pt plus 2pt minus 2pt

\dbltextfloatsep 20pt plus 2pt minus 4pt


\@fptop 0pt plus 1fil

\@fpsep 1pc plus 2fil

\@fpbot 0pt plus 1fil

\@dblfptop 0pt plus 1fil

\@dblfpsep 8pt plus 2fil

\@dblfpbot 0pt plus 1fil

\marginparpush 6pt

\parskip 0pt plus .1pt



\partopsep 0pt
\clubpenalty\@M
\widowpenalty\@M

\newif\if@uchead
\@ucheadfalse

\def\part{%
    \@startsection{part}{9}{\z@}{-10\p@ \@plus -4\p@ \@minus -2\p@}
        {4\p@}{\normalsize\sf\@ucheadtrue}%
}
\def\section{%
    \@startsection{section}{1}{\z@}{-10\p@ \@plus -4\p@ \@minus -2\p@}%
    {4\p@}{\normalsize\sf\@ucheadtrue}%
}
\def\subsection{%
    \@startsection{subsection}{2}{\z@}{-8\p@ \@plus -2\p@ \@minus -\p@}
    {4\p@}{\normalsize\sf}%
}
\def\subsubsection{%
    \@startsection{subsubsection}{3}{\parindent}{6\p@ \@plus \p@}%
    {-5\p@}{\normalsize\it}%
}
\def\paragraph{%
    \@startsection{paragraph}{3}{\parindent}{6\p@ \@plus \p@}%
    {-5\p@}{\normalsize\it}%
}
\let\@period=.
\def\@startsection#1#2#3#4#5#6{%
    \if@noskipsec
        \global\let\@period\@empty
        \leavevmode
        \global\let\@period.%
    \fi
    \par
    \@tempskipa #4\relax
    \@afterindenttrue
    \ifdim \@tempskipa <\z@
        \@tempskipa -\@tempskipa
        \@afterindentfalse
    \fi
    \if@nobreak
        \everypar{}%
    \else
        \addpenalty\@secpenalty
        \addvspace\@tempskipa
    \fi
    \@ifstar
        {\@ssect{#3}{#4}{#5}{#6}}
        {\@dblarg{\@sect{#1}{#2}{#3}{#4}{#5}{#6}}}%
}
\def\@sect#1#2#3#4#5#6[#7]#8{%
    \ifnum #2>\c@secnumdepth
        \let\@svsec\@empty
    \else
        \refstepcounter{#1}%
        \protected@edef\@svsec{%
            \textup{\csname the#1\endcsname}%
            \ifnum #2=1\relax .\fi
            \hskip .5em
        }%
    \fi
    \@tempskipa #5\relax
    \ifdim \@tempskipa>\z@
        \begingroup
            #6\relax
            \@hangfrom{\hskip #3\relax\@svsec}%
            \begingroup
                \interlinepenalty \@M
                \if@uchead
                    \uppercase{#8}%
                \else
                    #8%
                \fi
                \par
            \endgroup
        \endgroup
        \csname #1mark\endcsname{#7}%
        \addcontentsline{toc}{#1}{%
            \ifnum #2>\c@secnumdepth \else
                \protect\numberline{\csname the#1\endcsname}%
            \fi
            #7%
        }%
    \else
        \def\@svsechd{%
            #6%
            \hskip #3\relax
            \@svsec
            \if@uchead
                \uppercase{#8}%
            \else
                #8%
            \fi
            \csname #1mark\endcsname{#7}%
            \addcontentsline{toc}{#1}{%
                \ifnum #2>\c@secnumdepth \else
                    \protect\numberline{\csname the#1\endcsname}%
                \fi
                #7%
            }%
        }%
    \fi
    \@xsect{#5}%
}
\def\@xsect#1{%
    \@tempskipa #1\relax
    \ifdim \@tempskipa>\z@
        \par
        \nobreak
        \vskip \@tempskipa
        \@afterheading
    \else
        \global\@nobreakfalse
        \global\@noskipsectrue
        \everypar{%
            \if@noskipsec
                \global\@noskipsecfalse
                \clubpenalty\@M
                \hskip -\parindent
                \begingroup
                    \@svsechd
                    \@period
                \endgroup
                \unskip
                \@tempskipa #1\relax
                \hskip -\@tempskipa
            \else
                \clubpenalty \@clubpenalty
                \everypar{}%
            \fi
        }%
    \fi
    \ignorespaces
}
\def\@trivlist{%
    \@topsepadd\topsep
    \if@noskipsec
        \global\let\@period\@empty
        \leavevmode
        \global\let\@period.%
    \fi
    \ifvmode
        \advance\@topsepadd\partopsep
    \else
        \unskip
        \par
    \fi
    \if@inlabel
        \@noparitemtrue
        \@noparlisttrue
    \else
        \@noparlistfalse
        \@topsep\@topsepadd
    \fi
    \advance\@topsep \parskip
    \leftskip\z@skip
    \rightskip\@rightskip
    \parfillskip\@flushglue
    \par@deathcycles\z@
    \@setpar{%
        \if@newlist
            \advance\par@deathcycles\@ne
            \ifnum\par@deathcycles>\@m
                \@noitemerr{\@@par}%
            \fi
        \else
            {\@@par}%
        \fi
    }%
    \global\@newlisttrue
    \@outerparskip\parskip
}
\newcommand{\apbf}{\small\bf}
%% \newfont{\apbf}{cmbx9}
\def\@withappendix#1{\rm A--\number #1}
\def\appenheader{%
    \suppressfloats[t]%
    \begin{@float}{figure}[!b]
        \footnotesize
        \newfont{\sc}{cmcsc10}% %%* ACK!
        \parindent\z@
        \null
        \vskip -\textfloatsep
        \vskip 11\p@
        \hrule \@height .2\p@ \@width 30pc
        \vskip 2\p@
        \rule{\z@}{10\p@}%
        \ignorespaces
}

\def\endappenheader{%
    \end{@float}
    \global\let\appendixhead\@empty
}
\long\def\appendixhead#1#2#3#4{%
    \section*{Appendix}

    An appendix to this paper is available in electronic form
    (PostScript$^{\mbox{\tiny TM}}$).  Any of the following methods
    may be used to obtain it; or see the inside back cover of a
    current issue for up-to-date instructions.

    \begin{itemize}
    \item By anonymous ftp from {\apbf acm.org}, file
    {\apbf [pubs.journals.#1.append]p#2.ps}
    \item Send electronic mail to {\apbf mailserve@acm.org} containing
    the line\\ {\apbf send~[anonymous.pubs.journals.#1.append]p#2.ps}
    \item By {\it Gopher} from {\apbf acm.org}
    \item By anonymous ftp from {\apbf ftp.cs.princeton.edu},
    file {\apbf pub/#1/append/p#2.ps}
    \item Hardcopy from {\it Article Express}, for a fee: phone
    800-238-3458, fax 201-216-8526, or write P.O.~Box~1801, Hoboken NJ
    07030; and request {\sc acm-#1-appendix-{\small #2}}.
    \end{itemize}

    \clearpage
    \pagenumbering{withappendix}
    \appendix
    \par
    \noindent{\sc this document is the appendix to the following
    paper:}
    \hfill
    \vskip 1em
    \vbox{\sf \parindent\z@\@title}%
    \vskip .5em
    \vbox{\sf \parindent\z@\@author}%
    \vskip .5em\noindent
    \vskip 10\p@\noindent #4
    \vskip 11\p@\noindent
    \hrule \@height .2\p@
    \par
    \begin{bottomstuff}
    \permission
    \copyright #3 ACM
    \par
    \end{bottomstuff}
}
\def\appendix{%
    \par
    \part{Appendix}%
    \par
    \setcounter{section}{0}%
    \setcounter{subsection}{0}%
    \def\thesection{\Alph{section}}%
    \def\thesubsection{\thesection.\arabic{subsection}}%
}
\labelsep 5pt

\settowidth{\leftmargini}{(9)}
\addtolength\leftmargini\labelsep

\settowidth{\leftmarginii}{(b)}
\addtolength\leftmarginii\labelsep

\leftmarginiii  \leftmarginii
\leftmarginiv   \leftmarginii
\leftmarginv    \leftmarginii
\leftmarginvi   \leftmarginii
\leftmargin     \leftmargini

\labelwidth\leftmargini
\advance\labelwidth-\labelsep
\def\@listI{%
    \leftmargin\leftmargini
    \parsep \z@ \@plus \p@
    \topsep 6\p@ \@plus 2\p@ \@minus 2\p@
    \itemsep 2\p@ \@plus \p@ \@minus .5\p@
}

\let\@listi\@listI

\@listi
\def\@listii{%
    \leftmargin\leftmarginii
    \labelwidth\leftmarginii
    \advance\labelwidth-\labelsep
    \topsep \z@ \@plus \p@
    \parsep \z@ \@plus .5\p@
    \itemsep \parsep
}
\def\@listiii{%
    \leftmargin\leftmarginiii
    \labelwidth\leftmarginiii
    \advance\labelwidth-\labelsep
    \topsep \z@ \@plus \p@
    \parsep \z@ \@plus .5\p@
    \itemsep \parsep
}
\def\@listiv{%
    \leftmargin\leftmarginiv
    \labelwidth\leftmarginiv
    \advance\labelwidth-\labelsep
}
\def\@listv{%
    \leftmargin\leftmarginv
    \labelwidth\leftmarginv
    \advance\labelwidth-\labelsep
}
\def\@listvi{%
    \leftmargin\leftmarginvi
    \labelwidth\leftmarginvi
    \advance\labelwidth-\labelsep
}
\def\enumerate{%
    \ifnum \@enumdepth >3
        \@toodeep
    \else
        \advance\@enumdepth \@ne
        \edef\@enumctr{enum\romannumeral\the\@enumdepth}%
        \list{\csname label\@enumctr\endcsname}{%
            \usecounter{\@enumctr}%
            \def\makelabel##1{##1\hss}%
        }%
    \fi
}

\let\endenumerate\endlist
\def\longenum{%
    \ifnum \@enumdepth >3
        \@toodeep
    \else
        \advance\@enumdepth \@ne
        \edef\@enumctr{enum\romannumeral\the\@enumdepth}%
        \list{\csname label\@enumctr\endcsname}{%
            \usecounter{\@enumctr}%
            \labelwidth\z@
        }%
    \fi
}

\let\endlongenum\endlist
\def\labelenumi{\rom{(\arabic{enumi})}}
\def\theenumi{\arabic{enumi}}
\def\labelenumii{\rom{(\alph{enumii})}}
\def\theenumii{\alph{enumii}}
\def\p@enumii{\rom{\theenumi}}
\def\labelenumiii{\rom{\roman{enumiii}.}}
\def\theenumiii{\roman{enumiii}}
\def\p@enumiii{\rom{\theenumi(\theenumii)}}
\def\labelenumiv{\rom{\Alph{enumiv}.}}
\def\theenumiv{\Alph{enumiv}}
\def\p@enumiv{\rom{\p@enumiii\theenumiii}}
\def\itemize{%
    \list{---\hskip -\labelsep}{%
        \settowidth{\leftmargin}{---}%
        \labelwidth\leftmargin
        \addtolength{\labelwidth}{-\labelsep}%
    }%
}

\let\enditemize\endlist
\def\longitem{%
    \list{---}{%
        \labelwidth\z@
        \leftmargin\z@
        \itemindent\parindent
        \advance\itemindent\labelsep
    }%
}

\let\endlongitem\endlist
\def\verse{%
    \let\\=\@centercr
    \list{}{%
        \leftmargin 2pc
        \itemindent -1.5em
        \listparindent \itemindent
        \rightmargin\leftmargin
        \advance\leftmargin 1.5em
    }%
    \item[]
}

\let\endverse\endlist
\def\quotation{%
    \list{}{%
        \leftmargin 2pc
        \listparindent .5em
        \itemindent\listparindent
        \rightmargin\leftmargin
        \parsep \z@ \@plus \p@
    }%
    \item[]
}

\let\endquotation=\endlist
\def\quote{%
    \list{}{%
        \leftmargin 2pc
        \rightmargin\leftmargin
    }%
    \item[]
}

\let\endquote=\endlist
\def\description{%
    \list{}{%
        \listparindent\parindent
        \labelwidth\z@
        \leftmargin\z@
        \itemindent\parindent
        \advance\itemindent\labelsep
        \def\makelabel##1{\it ##1.}%
    }%
}

\let\enddescription\endlist
\def\describe#1{%
    \list{}{%
        \listparindent\parindent
        \settowidth{\labelwidth}{#1}%
        \leftmargin\labelwidth
        \addtolength\leftmargin\labelsep
        \def\makelabel##1{##1\hfil}%
    }%
}

\let\enddescribe\endlist

\def\program{%
    \ifdim\f@size pt=10pt
        \small
    \else
        \rm
    \fi
    \tabbing
}

\let\endprogram\endtabbing
\def\@begintheorem#1#2{%
    \trivlist
    \item[%
        \hskip \parindent
        \hskip \labelsep
        {\sc #1\enskip #2.}%
    ]\it
}
\def\@opargbegintheorem#1#2#3{%
    \trivlist
    \item[%
        \hskip \parindent
        \hskip \labelsep
        \begingroup
            \savebox\@tempboxa{\sc #3}%
            {\sc #1}%
            \enskip #2%
            \ifdim \wd\@tempboxa>\z@
                \enskip
                (\box\@tempboxa)%
            \fi.%
        \endgroup
    ]\it
}
\newif\if@qeded
\global\@qededfalse
\def\proof{%
    \global\@qededfalse
    \@ifnextchar[{\@xproof}{\@proof}%
}

\def\endproof{%
    \if@qeded\else\qed\fi
    \endtrivlist
}
\def\@proof{%
    \trivlist
    \item[%
        \hskip \parindent
        \hskip \labelsep
        {\sc Proof.}%
    ]
    \ignorespaces
}
\def\@xproof[#1]{%
    \trivlist
    \item[\hskip\parindent \hskip\labelsep{\sc Proof #1.}]%
    \ignorespaces
}
\def\qed{%
    \unskip
    \kern 10\p@
    \begingroup
        \unitlength\p@
        \linethickness{.4\p@}%
        \framebox(6,6){}%
    \endgroup
    \global\@qededtrue
}
\def\newdef#1#2{%
    \expandafter\@ifdefinable\csname #1\endcsname
        {\@definecounter{#1}%
         \expandafter\xdef\csname the#1\endcsname{\@thmcounter{#1}}%
         \global\@namedef{#1}{\@defthm{#1}{#2}}%
         \global\@namedef{end#1}{\@endtheorem}%
    }%
}
\def\@defthm#1#2{%
    \refstepcounter{#1}%
    \@ifnextchar[{\@ydefthm{#1}{#2}}{\@xdefthm{#1}{#2}}%
}
\def\@xdefthm#1#2{%
    \@begindef{#2}{\csname the#1\endcsname}%
    \ignorespaces
}
\def\@ydefthm#1#2[#3]{%
    \trivlist
    \item[%
        \hskip \parindent
        \hskip \labelsep
        \begingroup
            \savebox\@tempboxa{\it #3}%
            {\it #2}%
            \enskip \csname the#1\endcsname
            \ifdim \wd\@tempboxa>\z@
                \enskip
                \rom(\box\@tempboxa\rom)%
            \fi.%
        \endgroup
    ]%
    \ignorespaces
}
\def\@begindef#1#2{%
    \trivlist
    \item[%
        \hskip \parskip
        \hskip \labelsep
        {\it #1\enskip \rom{#2}.}%
    ]%
}
\def\theequation{\arabic{equation}}
\def\titlepage{%
    \@restonecolfalse
    \if@twocolumn
        \@restonecoltrue
        \onecolumn
    \else
        \newpage
    \fi
    \thispagestyle{empty}%
    \c@page\z@
}

\def\endtitlepage{%
    \if@restonecol
        \twocolumn
    \else
        \newpage
    \fi
}
\arraycolsep 2.5pt

\def\thebibliography#1{%
    \par
    \footnotesize
    \@startsection{subsection}{2}{\z@}{16\p@ \@plus 2\p@ \@minus \p@}
        {2\p@}{\sf}*{\uppercase{\refname}}
    \list{\arabic{enumi}.}{%
        \settowidth\labelwidth{99.}%
        \leftmargin\labelwidth
        \advance\leftmargin\labelsep
        \topsep \z@
        \parsep \z@ \@plus .1\p@
        \itemsep \parsep
        \usecounter{enumi}%
    }%
    \def\newblock{\hskip .11em \@plus .33em \@minus .07em}%
    \sloppy
    \widowpenalty4500
    \clubpenalty4500
    \sfcode`\.=1000
    \relax
}

\let\endthebibliography=\endlist
\def\footnoterule{%
    \kern-3\p@
    \hrule \@width 47\p@ %\@height .004\p@
    \kern 2.6\p@
}
\long\def\@makefntext#1{%
    \parindent 1em
    \noindent $^{\@thefnmark}$#1%
}
\def\topfraction{.92}
\setcounter{bottomnumber}{0}
\def\bottomfraction{0}
\def\textfraction{.086}
\def\floatpagefraction{.6}
\long\def\@makecaption#1#2{%
    \vskip 1pc
    \setbox\@tempboxa\hbox{#1.\quad #2}%
    \ifdim \wd\@tempboxa >\hsize
        #1.\quad #2\par
    \else
        \centerline{\box\@tempboxa}%
    \fi
}
\def\nocaption{%
    \refstepcounter\@captype
    \par
    \vskip 1pc
    \centerline{\footnotesize \csname fnum@\@captype \endcsname}%
}
\def\thefigure{\@arabic\c@figure}
\def\fps@figure{tp}
\def\ftype@figure{1}
\def\ext@figure{lof}
\def\figurename{Fig.}
\def\fnum@figure{\figurename~\thefigure}
\def\figfilename{\gdef\@figfilename}
\let\@figfilename\@empty
\if@faircopy
    \renewenvironment{figure}[1][p]{%
        \let\normalsize\footnotesize
        \normalsize
        \@float{figure}[p]%
    }{\end@float
        \global\setbox\@currbox\vbox to\textheight{%
            \vskip\@fptop
            \unvbox\@currbox
            \vskip\@fpbot
            \noindent \fnum@figure
            \ifx\@figfilename\@empty\else
                : {\tt \@figfilename}%
                \global\let\@figfilename\@empty
            \fi
        }%
    }
\else
    \renewenvironment{figure}{%
        \let\normalsize\footnotesize
        \normalsize
        \@float{figure}
    }{\end@float}
\fi
\expandafter\let\csname figure*\endcsname\figure
\expandafter\let\csname endfigure*\endcsname\endfigure
\renewenvironment{table}{%
    \let\normalsize\footnotesize
    \normalsize
    \@float{table}%
}{\end@float}
\expandafter\let\csname table*\endcsname\table
\expandafter\let\csname endtable*\endcsname\endtable
\def\thetable{\@Roman\c@table}
\def\fps@table{tp}
\def\ftype@table{2}
\def\ext@table{lot}
\def\tablename{Table}
\def\fnum@table{\tablename~\thetable}
\newdimen\@narrowfig
\newbox\@nfigbox
\newbox\@nfcapbox
\newif\if@nfeven
\def\acmtable#1{%
    \@narrowfig #1\relax
    \let\caption\@atcap
    \let\nocaption\@atnocap
    \@ifnextchar[{\@ntab}{\@ntab[\fps@table]}%
}

\def\@ntab[#1]{%
    \expandafter\table\expandafter[#1]%
    \setbox\@nfigbox\vbox\bgroup
        \hsize \@narrowfig
        \@parboxrestore
}

\def\endacmtable{%
    \hb@xt@\textwidth{%
        \hfil
        \vbox{%
            \hsize \@narrowfig
            \box\@nfcapbox{%
                \baselineskip 4\p@
                \hbox{\vrule \@height .4\p@ \@width \hsize}%
            }%
            \vskip -\p@
            \box\@nfigbox
            \vskip -\p@
            \begingroup
                \baselineskip 4\p@
                \hbox{\vrule \@height .4\p@ \@width \hsize}%
            \endgroup
        }%
        \hfil
    }%
    \end@float
}
\def\@atmakecap#1#2{%
    \setbox\@tempboxa\hbox{#1.\quad #2}%
    \ifdim \wd\@tempboxa >\hsize
        \sloppy #1.\quad #2 \par
    \else
        \centerline{\box\@tempboxa}%
    \fi
}
\def\@atcap{%
        \par
    \egroup
    \refstepcounter\@captype
    \@dblarg{\@atcapx\@captype}%
}
\long\def\@atcapx#1[#2]#3{%
    \addcontentsline{\csname ext@#1\endcsname}{#1}{%
        \protect\numberline{\csname the#1\endcsname}{\ignorespaces #2}%
    }%
    \setbox\@nfcapbox\vbox{%
        \hsize \wd\@nfigbox
        \@parboxrestore
        \@atmakecap{\csname fnum@#1\endcsname}{\ignorespaces #3}%
        \par
    }%
}
\def\@atnocap{%
    \egroup
    \refstepcounter\@captype
    \setbox\@nfcapbox\vbox{%
        \hsize \wd\@nfigbox
        \centerline{\footnotesize \fnum@table}
    }%
}
\def\narrowfig#1{%
    \@narrowfig #1\relax
    \let\caption\@nfcap
    \let\nocaption\@nfnocap
    \@ifnextchar[{\@nfig}{\@nfig[\fps@figure]}%
}

\def\@nfig[#1]{%
    \expandafter\figure\expandafter[#1]%
    \setbox\@nfigbox\vbox\bgroup
        \hsize\@narrowfig
        \@parboxrestore
}

\def\endnarrowfig{%
    \hb@xt@\textwidth{%
        \if@nfeven
            \box\@nfcapbox  \hfil   \box\@nfigbox
        \else
            \box\@nfigbox   \hfil   \box\@nfcapbox
        \fi
    }%
    \endfigure
}
\def\@nfcap{%
        \par
    \egroup
    \refstepcounter\@captype
    \@dblarg{\@nfcapx\@captype}%
}
\def\@nfmakecap #1#2{%
    \setbox\@tempboxa\hbox{#1.\quad #2}%
    \ifdim \wd\@tempboxa >\hsize
        \sloppy #1.\quad #2 \par
    \else
        \@@line{%
            \if@nfeven\else\hfil\fi
            \box\@tempboxa
            \if@nfeven\hfil\fi
        }%
    \fi
}
\long\def\@nfcapx#1[#2]#3{%
    \addcontentsline{\csname ext@#1\endcsname}{#1}{%
        \protect\numberline{\csname the#1\endcsname}{\ignorespaces #2}%
    }%
    \@seteven
    \setbox\@nfcapbox\vbox to \ht\@nfigbox{%
        \hsize \textwidth
        \advance\hsize -2pc
        \advance\hsize -\wd\@nfigbox
        \@parboxrestore
        \vfil
        \@nfmakecap{\csname fnum@#1\endcsname}{\ignorespaces #3}%
        \par
        \vfil
    }%
}
\def\@nfnocap{%
    \egroup
    \refstepcounter\@captype
    \@seteven
    \setbox\@nfcapbox\vbox to \ht\@nfigbox{%
        \hsize \textwidth
        \advance\hsize -2pc
        \advance\hsize -\wd\@nfigbox
        \@parboxrestore
        \vfil
        \@@line{%
            \if@nfeven\else\hfil\fi
            \footnotesize \fnum@figure
            \if@nfeven\hfil\fi
        }%
        \vfil
    }%
}
\def\@seteven{%
    \@nfeventrue
    \@ifundefined{r@@nf\thefigure}{}{%
        \edef\@tmpnf{\csname r@@nf\thefigure\endcsname}%
        \edef\@tmpnf{\expandafter\@cdr\@tmpnf\@nil}%
        \ifodd\@tmpnf\relax
            \@nfevenfalse
        \fi
    }%
    \label{@nf\thefigure}%
    \edef\@tmpnfx{\if@nfeven e\else o\fi}%
    \edef\@tmpnf{%
        \write\@unused{%
            \noexpand\ifodd \noexpand\c@page
                \noexpand\if \@tmpnfx e%
                    \noexpand\@nfmsg{\thefigure}
                \noexpand\fi
            \noexpand\else
                \noexpand\if \@tmpnfx o%
                    \noexpand\@nfmsg{\thefigure}%
                \noexpand\fi
            \noexpand\fi
        }%
    }%
    \@tmpnf
}

\def\@nfmsg#1{%
    \PackageWarning{acmart}{Bad narrowfig: Figure #1 on page \thepage}%
}
\newdimen\@narrowfig
\newbox\@nfigbox
\newbox\@nfcapbox
\newif\if@nfeven
\newenvironment{authinfo}{%
    \newcommand{\name}[1] {Name: ##1\newline }
    \newcommand{\address}[1] {Address: ##1\newline }
    \newcommand{\affiliation}[1]  {Affiliation: ##1\newline }
    \newcommand{\biography}[1]  {Biography: ##1\newline}
}{}
\newenvironment{sponsor}[2]{%
    Sponsor: #1\strut\newline
    \parbox{3.in}{#2}%
}{\newline}
\def\and{\\ and\\}


\def\maketitle{%
    \newpage
    \thispagestyle{titlepage}%
    \suppressfloats[t]%
    \begingroup
        \lineskip \z@
        \null
        \vskip -30\p@\relax
        \parindent\z@
        \begingroup
            \LARGE
            \raggedright
            \hyphenpenalty\@M
            \sf \@title
            \par
        \endgroup
        \vskip 13.5\p@
        %vskip 13.5pt between title and author
        \begingroup
            \addtolength{\baselineskip}{2\p@}%
            \sf
            \@author\par
        \endgroup
        \begingroup
            \footnotesize
            \medskip
            \rule{\textwidth}{.2\p@}%
            \ifvoid\@abstract
                \PackageWarning{acmart}{an abstract is required}%
            \else
                \vskip 8.5\p@
                \box\@abstract
            \fi
            \ifx\@categories\@empty \else
                \vskip 4\p@\relax %vskip8.5 space above abstract
                \def\and{\unskip\textup; }%
                Categories and Subject Descriptors: \@categories\par
            \fi
            \ifx\@terms\@empty\else
                \vskip 4\p@
                General Terms: \ignorespaces
                \@terms
                \par
            \fi
            \ifx\@keywords\@empty\else
                \vskip 4\p@
                Additional Key Words and Phrases: \ignorespaces
                \@keywords
                \par
            \fi
        \endgroup
        \label{@firstpg}%
        \rule{\textwidth}{.2\p@}%
        \vskip 23\p@
    \endgroup
    \let\maketitle\relax
    \global\let\@categories\@empty
    \global\let\@terms\@empty
    \global\let\@keywords\@empty
}
\newbox\@abstract
\def\abstract{%
    \everypar{}%
    \global\setbox\@abstract\vbox\bgroup
        \footnotesize
        \trivlist\item[]\ignorespaces
}

\def\endabstract{%
        \endtrivlist
    \egroup
    \ifx\maketitle\relax
        \PackageWarning{acmart}{%
            the abstract must be specified before the \MessageBreak
            \string\maketitle\space command%
        }%
        \box\@abstract
    \fi
}
\def\terms{\gdef\@terms}

\let\@terms\@empty
\def\keywords{\gdef\@keywords}

\let\@keywords\@empty
\def\category#1#2#3{%
    \@ifnextchar [{\@category{#1}{#2}{#3}}{\@category{#1}{#2}{#3}[]}%
}
\def\@category#1#2#3[#4]{%
    \edef\@tempa{\ifx \@categories\@empty \else ; \fi}%
    \begingroup
        \let\protect\@unexpandable@protect
        \let\and\relax
        \xdef\@categories{%
            \@categories
            \@tempa
            #1 [{\bf #2}]%
            \if!#4!%
                \if!#3!\else : #3\fi
            \else
                :\space
                \if!#3!\else #3\kern\z@---\hskip\z@\fi
                {\it #4}%
            \fi
        }%
    \endgroup
}

\let\@categories\@empty
\def\bottomstuff{%
    \enlargethispage{-\baselineskip}%
    \suppressfloats[t]%
    \@float{figure}[!b]
        \footnotesize
        \parindent\z@
        \null
        \vskip -\textfloatsep
        \vskip 10\p@
        \hrule \@height .2\p@ \@width 30pc
        \vskip 4\p@
        \ignorespaces
}
\let\endbottomstuff\end@float
\long\def\permission{\par
    Permission to make digital or hard copies of part or all of this
    work for personal or classroom use is granted without fee provided
    that copies are not made or distributed for profit or direct
    commercial advantage and that copies show this notice on the first
    page or initial screen of a display along with the full citation.
    Copyrights for components of this work owned by others than ACM
    must be honored. Abstracting with credit is permitted. To copy
    otherwise, to republish, to post on servers, to redistribute to
    lists, or to use any component of this work in other works,
    requires prior specific permission and/or a fee.  Permissions may
    be requested from Publications Dept, ACM Inc., 1515 Broadway, New
    York, NY 10036 USA, fax +1 (212) 869-0481, or {\tt
    permissions@acm.org}.
    \par
}
\newenvironment{acks}{%
    \@startsection{subsection}{2}{\z@}{-16\p@ \@plus -2\p@ \@minus -\p@}
        {2\p@}{\sf}*{\footnotesize ACKNOWLEDGMENTS}%
}{\par}
\newenvironment{received}{%
    \par
    \footnotesize
    \addvspace{18\p@ \@minus 4\p@}%
    \parindent\z@
}{%
    \label{@lastpg}%
    \par
}
\mark{{}{}}
\def\ps@myheadings{%
    \let\@mkboth\@gobbletwo
    \def\@oddhead{%
        \hfill\small\sf\rightmark
        \hskip 19\p@
        {\Large$\cdot$}%
        \hskip 17\p@
        \thepage
    }%
    \def\@oddfoot{\null\hfill\tiny\@runningfoot}
    \def\@evenhead{%
        \small\sf\thepage
        \hskip 17\p@
        {\Large$\cdot$}%
        \hskip 19\p@
        \leftmark
        \hfill
    }%
    \def\@evenfoot{\tiny\@runningfoot \hfill\null}%
    \let\partmark\@gobble
    \let\sectionmark\@gobble
    \let\subsectionmark\@gobble
}
\def\runningfoot#1{\def\@runningfoot{#1}}

\let\@runningfoot\@empty

\def\firstfoot#1{\def\@firstfoot{#1}}

\let\@firstfoot\@empty

\def\pages{\pageref{@firstpg}--\pageref{@lastpg}}
\def\ps@titlepage{%
    \let\@mkboth\@gobbletwo
    \let\@oddhead\@empty
    \def\@oddfoot{\null\hfill\tiny\@firstfoot}%
    \let\@evenhead\@empty
    \def\@evenfoot{\tiny\@firstfoot\hfill\null}%
}
\def\today{%
    \ifcase\month \or
    January\or
    February\or
    March\or
    April\or
    May\or
    June\or
    July\or
    August\or
    September\or
    October\or
    November\or
    December
    \fi
    \space\number\day, \number\year
}
\def\marray{%
    \arraycolsep 2.5\p@
    \let\@acol\@arrayacol
    \let\@classz\@marrayclassz
    \let\@classiv\@marrayclassiv
    \let\\\@arraycr
    \let\@halignto\@empty
    \@tabarray
}

\let\endmarray\endarray
\def\@marrayclassiv{\@addtopreamble{$\displaystyle \@nextchar$}}

\def\@marrayclassz{%
    \ifcase \@lastchclass
    \@acolampacol
    \or \@ampacol
    \or
    \or
    \or \@addamp
    \or \@acolampacol
    \or \@firstampfalse \@acol
    \fi
    \edef\@preamble{%
        \@preamble
        \ifcase \@chnum
            \hfil$\relax\displaystyle\@sharp$\hfil
            \or $\relax\displaystyle\@sharp$\hfil
            \or \hfil$\relax\displaystyle\@sharp$%
        \fi
    }%
}
\ps@myheadings

\pagenumbering{arabic}

\onecolumn


\parindent 10pt
\typeout{Using ACM bibliography style}
\newcommand\bibyear[2]{%
    \unskip\quad\ignorespaces#1\unskip
    \if#2..\quad \else \quad#2\relax \fi
}
\let\bibemph\emph
\let\bibemphic\emph
\let\bibsc\textsc
\def\@normalcite{%
    \def\@cite##1##2{[##1\if@tempswa , ##2\fi]}%
}
\def\@citeNB{%
    \def\@cite##1##2{##1\if@tempswa , ##2\fi}%
}
\def\@citeRB{%
    \def\@cite##1##2{##1\if@tempswa , ##2\fi]}%
}
\def\start@cite#1#2{%
    \edef\citeauthoryear##1##2##3{%
        ###1%
        \ifnum#2=\z@ \else\ ###2\fi
    }%
    \ifnum#1=\thr@@
        \let\@@cite\@citeyear
    \else
        \let\@@cite\@citenormal
    \fi
    \@ifstar{\@citeNB\@@cite}{\@normalcite\@@cite}%
}
\def\cite{\start@cite23}
\def\citeNP{\cite*}
\def\citeA{\start@cite10}
\def\citeANP{\citeA*}
\def\shortcite{\start@cite23}
\def\shortciteNP{\shortcite*}
\def\shortciteA{\start@cite20}
\def\shortciteANP{\shortciteA*}
\def\citeyear{\start@cite30}
\def\citeyearNP{\citeyear*}
\def\citeN{%
    \@citeRB
    \def\citeauthoryear##1##2##3{##1\ [##3%
        \def\reserved@a{##1}%
        \def\citeauthoryear####1####2####3{%
            \def\reserved@b{####1}%
            \ifx\reserved@a\reserved@b
                ####3%
            \else
                \PackageError{acmart}{author mismatch in \string\citeN}%
            \fi
        }%
    }%
    \@ifstar\@citeyear\@citeyear
}
\def\shortciteN{%
    \@citeRB
    \def\citeauthoryear##1##2##3{##2\ [##3%
        \def\reserved@a{##2}%
        \def\citeauthoryear####1####2####3{%
            \def\reserved@b{####2}%
            \ifx\reserved@a\reserved@b
                ####3%
            \else
                \PackageError{acmart}{%
                    author mismatch in \string\shortciteN
                }%
            \fi
        }%
    }%
    \@ifstart\@citeyear\@citeyear
}
\def\@citenormal{%
    \@ifnextchar [{\@tempswatrue\@citex;}
                  {\@tempswafalse\@citex;[]}%
}
\def\@citeyear{%
    \@ifnextchar [{\@tempswatrue\@citex,}%
                  {\@tempswafalse\@citex,[]}%
}
\def\@citex#1[#2]#3{%
    \let\@citea\@empty
    \@cite{%
        \@for\@citeb:=#3\do{%
            \@citea
            \def\@citea{#1 }%
            \edef\@citeb{\expandafter\@iden\@citeb}%
            \if@filesw
                \immediate\write\@auxout{\string\citation{\@citeb}}%
            \fi
            \@ifundefined{b@\@citeb}{%
                {\reset@font\bfseries ?}%
                \G@refundefinedtrue
                \@latex@warning{%
                    Citation `\@citeb' on page \thepage\space undefined%
                }%
            }%
            {\csname b@\@citeb\endcsname}%
        }%
    }{#2}%
}
\let\@biblabel\@gobble
\newdimen\bibindent
\bibindent=1.5em
\def\thebibliography#1{%
    \footnotesize
    \section*{%
        \refname
        \@mkboth{\uppercase{\refname}}{\uppercase{\refname}}%
    }%
    \list{[\arabic{enumi}]}{%
        \settowidth\labelwidth{[#1]}%
        \leftmargin\labelwidth
        \advance\leftmargin\labelsep
        \advance\leftmargin\bibindent
        \itemindent -\bibindent
        \listparindent \itemindent
        \parsep \z@
        \usecounter{enumi}%
    }%
    \let\newblock\@empty
    \sloppy
    \sfcode`\.=1000\relax
}
\endinput
%% 
%% End of file `acmart.cls'.
