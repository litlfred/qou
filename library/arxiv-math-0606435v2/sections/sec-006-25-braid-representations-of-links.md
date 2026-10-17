---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-006-25-braid-representations-of-links
section_title: "Braid representations of links"
section_number: 2.5
pages: 9-11
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.97
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
By a theorem of Alexander \cite{Alexander}, any link is the \em{closure}
$\hat\bt$ of a braid $\bt$. The \em{braid index} $b(L)$ of a link $L$
is the smallest number of strands of a braid $\be$ whose closure
$\hat\be$ is $L$. See \cite{Morton,WilFr,Murasugi}. Such $\bt$ are
also called \em{braid representations} of $L$. The closure operation
gives for a particular braid word $\bt$ a link diagram $D=\hat\bt$.
Then we have for example $w(\hat\bt)=[\bt]$, $c(\bt)=c(\hat\bt)$,
$c_\pm(\bt)=c_\pm(\hat\bt)$, and $s(\hat\bt)$
is the number of strings of $\bt$ (i.e. $n$ for $\bt\in B_n$).

Many properties of braid words we will deal with
relate to the corresponding properties of their link diagrams.
For example, a braid word is called \em{positive} if it contains no
$\sg_i^{-1}$, or in other words, its closure diagram is positive.
A braid is positive if it has a positive braid word.
In a similar fashion, we say that braid is ($A$/$B$-)adequate if
it has an ($A$/$B$-)adequate word representation, and a word is
adequate if the link diagram obtained by its closure is adequate. 

If a braid word $\bt$ is written as $\sg_1^{\pm 1}\ap\sg_1^p\ap'$,
where $p\in\bZ$ and none of $\ap$ and $\ap'$ contains a syllable of
index $1$, then the diagram admits a \em{flype}, which exchanges
the syllables of index $1$ in $\bt$, so that we obtain $\sg_1^p
\ap\sg_1^{\pm 1}\ap'$. This operation preserves the isotopy
type of the closure link $\hat\bt$, but in general changes
the braid conjugacy class. The phenomenon is explained in
\cite{BirMen}. In the context of general link diagrams,
the flype has been studied also extensively, most prominently
in \cite{MenThis}.

Alternatively to the standard Artin generators, one
considers also a representation of the braid groups by
means of an extended set of generators (and their inverses)
\[
\sg_{i,j}^{\pm 1}=\sg_i\dots\sg_{j-2}\sg_{j-1}^{\pm 1}
\sg_{j-2}^{-1}\dots\sg_i^{-1}
\]
for $1\le i<j\le n$. Note that 
\begin{eqn}\label{op}
\sg_i=\sg_{i,i+1}\,.
\end{eqn}
A representation of a braid $\bt$, and its closure link $L=\hat\bt$,
as word in $\sg_{i,j}^{\pm 1}$ is called a \em{band representation}
\cite{BKL}. A band representation of $\bt$ spans naturally a
Seifert surface of the link $L$ as in figure \ref{figbd}: one
glues disks into the strands, and connects them by half-twisted
bands along the $\sg_{i,j}$. The resulting surface is called
\em{braided Seifert surface} of $L$. A minimal genus Seifert
surface of $L$, which is a braided Seifert surface, is also
called a \em{Bennequin surface} \cite{BirMen2}.

In this paper we will deal exclusively with band representations
in $B_3$. Then we have three band generators $\sg_{i,i\bmod 3+1}$
(where $i=1,2,3$, and `$\bmod$' is taken with values between $0$ and
$2$). With \eqref{op}, we have $\sg_1=\sg_{1,2}$ and $\sg_2=\sg_{2,3}$,
and with the special meaning of $\sg_3\in B_3$ introduced above,
$\sg_3=\bar\sg_{1,3}$, where bar denotes the mirror image.
(This mirroring is used here for technical reasons related to
Xu's normal form, as explained below.)

If a band representation contains only positively half-twisted bands
(i.e. no $\sg_{i,j}^{-1}$ occur), it is called \em{band-positive}
or \em{strongly quasi-positive}. A link with a strongly quasi-positive
band (braid) representation is called strongly quasi-positive.
Such links have an importance in connection to algebraic curves;
see \cite{Rudolph2}.

Using the skein polynomial, define a quantity by
\begin{eqn}\label{mwfb}
MWF(L)\,=\,\frac 12\,\big(\Md_vP-\md_vP\big)+1\,.
\end{eqn}
The \em{Morton-Williams-Franks braid index inequality}
\cite{Morton,WilFr} (abbreviated as MWF) states that
\begin{eqn}
b(L)\ge MWF(L)
\end{eqn}
for every link $L$. This inequality is often exact (i.e. an
equality). The study of links where it is exact or not
has occupied a significant part of previous literature.
Most noteworthy is the work of Murasugi \cite{Murasugi}
and Murasugi-Przytycki \cite{MurPrz2}.

The Morton-Williams-Franks 
results from two other inequalities, due to Morton,
namely that for a diagram $D$, we have
\begin{eqn}\label{mq}
1-s(D)+w(D)\,\le\,\md_lP(D)\,\le\,\Md_lP(D)\,\le\,s(D)-1+w(D)\,.
\end{eqn}
Williams-Franks showed these inequalities for the case of braid
representations (i.e. when $D=\hat\bt$ for some braid $\bt$).
Later it was observed from the
algorithm of Yamada \cite{Yamada} and Vogel \cite{Vogel}
that the braid version is actually equivalent to (and not just
a special case of) the diagram version.

These inequalities were later improved in \cite{MurPrz2} in a way 
that allows to settle the braid index problem for many links
(see \S\ref{Sfg} or also \cite{Ohyama}). 

In the special case of $3$-braids (and with the special meaning
of $\sg_3$ as described above), Xu \cite{Xu} gives a normal form
of a conjugacy class in $\sg_{1,2,3}$. By Xu's algorithm, each
$\bt\in B_3$ can be written in one of the two forms
{\def\theenumi{\Alph{enumi}}
\def\labelenumi{(\theenumi)}
\begin{enumerate}
\item\label{itA} $[21]^kR$ or $L^{-1}[21]^{-k}$ ($k\ge 0$), or
\item\label{itB} $L^{-1}R$,
\end{enumerate}
}where $L$ and $R$ are positive words in $\sg_{1,2,3}$ with (cyclically)
non-decreasing indices (i.e. each $\sg_i$ is followed by $\sg_i$
or $\sg_{i\bmod 3+1}$, with `$\bmod$' taken with values between $0$
and $2$). Since the form \reference{itB} must be cyclically
reduced, we may assume that $L$ and $R$ do not start or end with
the same letter. This form is the shortest word in $\sg_{1,2,3}$
of a conjugacy class. By Bennequin's aforementioned result, the
braided surface is then a minimal genus (or Bennequin) surface.


\subsection{Gau\ss{} sum invariants}

We recall briefly the definition of Gau\ss{} sum invariants.
They were introduced first in \cite{Fied} for braids, and later
\cite{Fied2,VirPol} for knots. It is known that all
they give formulas for Vassiliev invariants.

\begin{defi}(\protect\cite{Fied2})\ 
A Gau\ss{} diagram of a knot diagram is an oriented circle with
arrows connecting points on it mapped to a crossing and
oriented from the preimage of the undercrossing (underpass)
to the preimage of the overcrossing (overpass).
\end{defi}

We will call a pair of crossings whose arrows intersect in
the Gau\ss{} diagram a \em{linked} pair.

\begin{exam}
As an example, figure \ref{fig6_2} shows the knot $6_2$ in its
commonly known projection and the corresponding Gau\ss{} diagram.
\end{exam}

\begin{figure}[htb]
{
\[
\begin{array}{c@{\qquad}c}
     \diag{2cm}{2.0}{2.0}{
  \picputtext[dl]{0 0}{\autoepsffalse\epsfs{4cm}{6_2}}
  \picputtext[u]{1.25 1.65}{$1$} 
  \picputtext[u]{0.8 1.65}{$2$} 
  \picputtext[u]{0.6 0.6}{$3$} 
  \picputtext[u]{1.0 0.35}{$4$} 
  \picputtext[u]{1.3 0.9}{$5$} 
  \picputtext[u]{0.9 1.3}{$6$} 
	}
 & 
\diag{1.6cm}{2.4}{2.4}{\pictranslate{1.2 1.2}{
\piclinewidth{60}
\piccircle{0 0}{1}{}
\labar{240}{ 30}{1}
\labar{ 60}{210}{2}
\labar{300}{ 90}{3}
\labar{120}{330}{4}
\labar{  0}{150}{5}
\labar{180}{270}{6}
} 
} 
\end{array}
\]}
\caption{The standard diagram of the knot $6_2$ and its Gau\ss{}
diagram.\label{fig6_2}}
\end{figure}

The simplest (non-trivial) Vassiliev knot invariant is the
\em{Casson invariant} $v_2$, with $v_2=\Dl''(1)/2=-V''(1)/6$,
for which Polyak-Viro
\cite{VirPol,VirPol2} gave the simple Gau\ss{} sum formula
\begin{eqn}\label{pv2_}
v_2\,=\,\GD{\arrow{225}{45}
\arrow{315}{135}
\picfillgraycol{0}\picfilledcircle{1 90 polar}{0.09}{}
}\,.
\end{eqn}
Here the point on the circle corresponds to a point on the
knot diagram, to be placed arbitrarily except on a crossing.
(The expression does not alter with the position of the
basepoint; we will hence have, and need, the freedom to place
it conveniently.)

We will use the symmetrized version of \eqref{pv2_}
w.r.t. taking the mirror image of the knot diagram:
\begin{eqn}\label{pv2}
v_2\,=\,\frac{1}{2}\es\left(
\GD{\arrow{225}{45}
\arrow{315}{135}
\picfillgraycol{0}\picfilledcircle{1 90 polar}{0.09}{}
}+
\GD{\arrow{45}{225}
\arrow{135}{315}
\picfillgraycol{0}\picfilledcircle{1 90 polar}{0.09}{}
}\right)\,.
\end{eqn}


\section{Xu's form and Seifert surfaces\label{SA}}

We studied the relation of Xu's algorithm and the skein
polynomial in \cite{3br}, and here we will go further to
connect fiberedness, the and Alexander and Jones polynomial
to Xu's form.
