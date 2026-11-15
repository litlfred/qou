---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-002-21-links-and-link-diagrams
section_title: "Links and link diagrams"
section_number: 2.1
pages: 5-6
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.961
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Links are represented by diagrams; we assume diagrams are
oriented (though sometimes orientation is not relevant).

A crossing $p$ in a link diagram $D$ is called \em{reducible} (or
nugatory) if it looks like on the left of figure \reference{figred}.
$D$ is called reducible if it has a reducible crossing, else it is
called \em{reduced}. The reducing of the reducible crossing $p$
is the move depicted on figure \reference{figred}. Each diagram $D$
can be (made) reduced by a finite number of these moves.

\begin{figure}[htb]
\begin{eqn}\label{eqred}
\diag{6mm}{4}{2}{
  \picrotate{-90}{\rbraid{-1 2}{1 1.4}}
  
  
  \picputtext[u]{2 0.7}{$p$}
  \picscale{1 -1}{
    \picfilledcircle{0.7 -1}{0.8}{$P$}
  }
  \picfilledcircle{3.3 1}{0.8}{$Q$}
} \qquad\lra\qquad
\diag{6mm}{4}{2}{
  \piccirclearc{2 0.5}{1.3}{45 135}
  \piccirclearc{2 1.5}{1.3}{-135 -45}
  \picfilledcircle{1 1}{0.8}{$P$}
  \picfilledcircle{3 1}{0.8}{$Q$}
} 
\end{eqn}
\caption{\label{figred}}
\end{figure}

We assume in the following all diagrams reduced, unless otherwise
stated.

The diagram on the right of figure \reference{figtan}
is called \em{connected sum} $A\# B$ of the diagrams $A$ and $B$.
If a diagram $D$ can be represented as the connected sum of 
diagrams $A$ and $B$, such that both $A$ and $B$ have at least one
crossing, then $D$ is called \em{disconnected} (or composite), else
it is called \em{connected} (or prime). $K$ is \em{prime} if whenever
$D=A\# B$ is a composite diagram of $K$, one of $A$ and $B$
represent an unknotted arc (but not both; the unknot is
not considered to be prime per convention).

By $c(D)$ we denote the
\em{number of crossings} of $D$, $n(D)$ the number of components
of $D$ (or $K$, $1$ if $K$ is a knot), and $s(D)$ the \em{number
of Seifert circles} of $D$. The \em{crossing number} $c(K)$ of a
knot or link $K$ is the minimal crossing number of all diagrams
$D$ of $K$.
$!D$ is the \em{mirror image} of $D$, and $!K$ is the mirror image
of $K$. Clearly $g(!D)=g(D)$ and $g(!K)=g(K)$.

\begin{figure}[htb]
\[
\diag{6mm}{3}{2}{
  \piccirclearc{1.8 1}{0.5}{-120 120}
  \picfilledcircle{1 1}{0.8}{$A$}
}\, \#\,
\diag{6mm}{3}{2}{
  \piccirclearc{1.2 1}{0.5}{60 300}
  \picfilledcircle{2 1}{0.8}{$B$}
}\quad =\quad
\diag{6mm}{4}{2}{
  \piccirclearc{2 0.5}{1.3}{45 135}
  \piccirclearc{2 1.5}{1.3}{-135 -45}
  \picfilledcircle{1 1}{0.8}{$A$}
  \picfilledcircle{3 1}{0.8}{$B$}
} 
\]
\caption{\label{figtan}}
\end{figure}

The \em{Seifert graph} $\Gm(D)$ of a diagram $D$ is defined to
be the graph whose vertices are the Seifert circles of $D$ and
whose edges are the crossings. The \em{reduced Seifert graph}
$\Gm'(D)$ is defined by removing multiple copies of an edge
between two vertices in $\Gm(D)$, so that a simple edge
remains. (See \cite{MurPrz,MurPrz2} for example.)

The \em{(Seifert) genus} $g(K)$ resp.\ \em{Euler characteristic}
$\chi(K)$ of a knot or link $K$ is said to be the minimal genus
resp.\ maximal Euler characteristic of Seifert surface of $K$.
For a diagram $D$ of $K$, $g(D)$ is defined to be the genus
of the Seifert surface obtained by Seifert's algorithm on $D$,
and $\chi(D)$ its Euler characteristic. We have $\chi(D)=s(D)-c(D)$
and $2g(D)=2-n(D)-\chi(D)$.

The numbering of knots we use is as in the tables of \cite
[appendix]{Rolfsen} for prime knots of crossing number $\le 10$,
and as in \cite{KnotScape} for those of crossing number $11$
to $16$. KnotScape's numbering is reorganized so that for
given crossing number non-alternating knots are appended after
alternating ones, instead of using `a' and `n' superscripts.
