---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-025-6-studying-alternating-links-by-braid-index
section_title: "Studying alternating links by braid index"
section_number: 6
pages: 38-42
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.927
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
The combination of the identity \eqref{p21} and the skein-Jones
substitution \eqref{VPsub} was already used in \S\reference{Js}
to translate the determination of the 3-braid link genus from
$P$ to $V$. A similar line of thought will now enable us to
extend the other main result in \cite{3br}, the description
of alternating links of braid index 3. This result was
motivated by the work of Murasugi \cite{Murasugi},
and Birman's problem in \cite{MortonPb} how to
relate braid representations and diagrammatic properties
of links. We will see how via \eqref{VPsub} and 
the famous Kauffman-Murasugi-Thistlethwaite theorem
\cite{Kauffman2,Murasugi3,Thistle2} the Jones polynomial
enters in a new way into the braid representation picture.
The argument will lead to the braid index 3
result surprisingly easily, and then also to the
classification for braid index 4 (which seems out of scope
with the methods in \cite{3br} alone). We also obtain a
good description of the general (braid index) case.

Our starting point is the following general result concerning the
MWF-bound \eqref{mwfb}. A diagram is called special if it
has no separating Seifert circles; see \cite{Cromwell}.
The number of Seifert circles of $D$ is denoted by $s(D)$.

\begin{theorem}\label{_ty}
Assume $L$ is a non-trivial non-split alternating link, and $MWF(L)=
k$. Then an alternating (reduced) diagram $D$ of $L$ has $s(D)\le 2k-
2$ Seifert circles, and equality holds only if $D$ is special.
\end{theorem}

\proof As $L$ is non-trivial and non-split, we have $1-\chi(L)> 0$.
It is also well known, that $\Md_zP(L)=1-\chi(L)$ (see
\cite{Cromwell}). Now $\spn_v P(L)\le 2k-2$ by assumption. Under
the substitution in \eqref{mwfb} this translates to 
\begin{eqn}\label{sV}
\spn V(L)\le 1-\chi(L)+2k-2\,.
\end{eqn}
On the other hand, by \cite{Kauffman2,Murasugi3,Thistle2},
$\spn V(L)=c(D)$, and also $1-\chi(L)=c(D)-s(D)+1$.
So
\begin{eqn}\label{ff}
c(D)\le c(D)-s(D)+1+2k-2\,,
\end{eqn}
and then $s(D)\le 2k-1$. Now if this is an equality, then
so is \eqref{sV}. Then one easily sees that $P(L)$ must have
non-zero coefficients in both monomials $z^{\Md_zP}v^{\Md_vP}$
and $z^{\Md_zP}v^{\md_vP}$. Now under the substitution in \eqref{p21},
both these monomials give a non-cancelling contribution,
and one of them is not in ($v$-)degree 0, so the identity
\eqref{p21} cannot hold. Moreover, if \eqref{sV} fails
just by one, then still one of the two coefficients must
be non-zero. In order its (non-cancelling) contribution on
the left of \eqref{p21} to be in degree $0$, we see that
either $\Md_zP=\md_vP$, or $\Md_zP=-\Md_vP$. Using \cite
{Cromwell}, one concludes then that these are precisely the cases of a
(positively or negatively) special alternating link. \qed

Using \cite{Yamada} and \cite{Vogel} we have some simple
estimate on the unsharpness of MWF for alternating links.

\begin{corr}
For an alternating non-trivial non-split link $L$, we have
$b(L)\le 2MWF(L)-2$. \qed
\end{corr}

Of course, for many (in particular alternating) links
$b(L)=MWF(L)$ (that is, MWF is exact), or at least $b-MWF$
is small. So the above estimate should be considered as
a worst-case-analysis. Even if not strikingly sharp,
it is still far from trivial, in view of what we
already know can occur for non-alternating knots. Namely,
using the construction in \cite{Kanenobu2} and the work
in \cite{BirMen3} (see remark \reference{rfn} below),
one can find sequences of knots $(K_i)$ for which $MWF$
(in fact the full $P$ polynomial) is constant, but
$b(K_i)\to\infty$.

Another observation is that one can now extend the outcome
of the work in \cite{SV} by replacing crossing number of
an alternating knot by its braid index.

\begin{corr}
Let $n_{g,b}$ denote the number of alternating knots of
braid index $b$ and genus $g$. Then $n_{g,b}$ is finite.
Moreover, for $g$ fixed, we have that
$\lim_{b\to \infty} n_{g,b}/b^{6g-4}=C_g$ is a constant.
\end{corr}

\proof The finiteness of $n_{g,b}$ follows by \eqref{ff}.
When $\chi(L)$ is fixed, and $c(L)\to\infty$, one easily
sees from \eqref{ff} that $MWF(L)$ behaves asymptotically
(up to an $O(1)$, i.e. bounded, term)
at least like $c(D)/2$. Now Ohyama's result \cite{Ohyama}
implies that $b(L)$ (and $MWF(L)$ as well) behave asymptotically
exactly as $c(L)/2$. So from \cite{SV} we have the result.
\qed

\begin{rem}\label{rfn}
Of course we could also gain, as in \cite{SV}, an estimate on the
$C_g$ and its asymptotics for $g\to \infty$, it would just multiply
by $2^{6g-4}$. One should also note that the finiteness of
$n_{g,b}$, which one sees from \eqref{ff}, is not necessarily
clear \em{a priori}. In fact, however, Birman-Menasco proved
\cite{BirMen3} that $n_{g,b}$ is a finite number even for \em{general}
(i.e. without restriction to alternating) knots. Their methods seem,
though, quite unhelpful to estimate these numbers properly.
\end{rem}

Theorem \ref{_ty} immediately leads to the first slight sharpening
of the description of alternating links of braid index 3 in
\cite{3br}. (The case of $MWF=2$ is even more obvious, and omitted.)

\begin{corr}\label{opi}
An alternating link has $MWF=3$ if and only if it has braid index 3.
\end{corr}

\proof If $MWF(L)\le 3$, then the alternating diagram has at
most 4 Seifert circles, and exactly 4 only if it is special.
Apart from connected sums (which are easily handled), we obtain
the diagrams of closed alternating 3-braids and the $(p,q,r,s)$-
pretzel diagrams. By direct calculation of $P$ we saw in
\cite{3br} that if $\min(p,q,r,s)\ge 2$, then $MWF\ge 4$,
and that otherwise the pretzel link has braid index 3. \qed

The case of 4-braids is now not too much more difficult.



\begin{theorem}\label{tty}
Let $L$ be a prime non-split alternating link. The following 3
conditions are equivalent:
\begin{enumerate}
\item\label{Xa} $MWF(L)=4$
\item\label{Xb} $b(L)=4$
\item\label{Xc} $L$ is one of the links, whose reduced 
alternating diagrams are described (up to mirror images) as follows
\begin{enumerate}
\item\label{Ya} The Murasugi (or connected) sum of three
  $(2,n_i)$-torus links (with $|n_i|>1$),
\item\label{Yb} The Murasugi (or connected) sum of a $(2,n)$-torus
  link with a $(p,q,r,s)$-pretzel link, with one of $p,q,r,s$ equal
  to 1, or its mirror image, or
\item\label{Yc} a special diagram whose Seifert graph
(see \S\ref{Sdg}) is as shown in figure \reference{figSG}.
\end{enumerate}
\end{enumerate}
\end{theorem}

\proof $\reference{Xb}\So \reference{Xa}$. This follows from
corollary \ref{opi}.

$\reference{Xc}\So \reference{Xb}$. That the links in
\reference{Xc} have braid index at least 4 follows from the
description of the links with $b(L)\le 3$ in \cite{3br}
(which also comes out of the proof of corollary \eqref{opi}).
It is also not too hard to check that for all these links
$b=4$ by exhibiting a diagram $D$ with $s(D)=4$. The most
systematic way seems to apply the graph index inequality of
Murasugi-Przytycki \cite{MurPrz2} (see also \cite{Ohyama}).

$\reference{Xa}\So \reference{Xc}$. By applying theorem
\reference{_ty}, we need to deal with non-special
diagrams of at most 5 and special diagrams of at most 6
Seifert circles.

First consider the non-special diagrams.

For the fibered links (the reduced Seifert graph is a tree),
Murasugi's result \cite{Murasugi} leads directly to case
\reference{Ya}. For non-fibered links, the Seifert graph
must have a cycle, which must be of length at least 4 (the
Seifert graph is bipartite). Then the only option
that remains is case \reference{Yb}. We must still
argue why one of $p,q,r,s$ must be $\pm 1$. This can
be done using Murasugi-Przytycki's work, but one easily
sees it also by a direct skein theoretic argument, which
we explain.

Let $L(p,q,r,s)$ be the corresponding link and $P(p,q,r,s)$
its skein polynomial. Look first at $p=0$, $q,r,s\ge 2$. Then
$L(p,q,r,s)$ a connected sum of two $(2,n)$-torus
links, and a closed alternating 3-braid. So
$MWF(L(p,q,r,s))=5$. Now since the case $p=1$, $q,r,s\ge 2$ has
$MWF(L(1,q,r,s))\le b(L(1,q,r,s))=4$, the skein relation \eqref{srel}
easily shows that the maximal degree coefficient $\Mc_vP(p,q,r,s)$
of $v$ in $P$ (which is a polynomial in $z$) for $p=2$ is inherited
from $p=0$. Then further applications of \eqref{srel} show that
the $z$-degree of $\Mc_vP(p,q,r,s)$ increases with $p$, so 
in particular this term never vanishes, and so $MWF(L(p,q,r,s))=5$.

\begin{figure}[htb]
{\small
\[
\begin{array}{c}
  \diag{6mm}{3}{2}{
  \pictranslate{0 0.5 x}{
    \diag{6mm}{3}{2}{
      \cycl{0.5 2}{0.5 0.5}{2 0.5}{2 2}
    }
  }
  \picputtext{1.75 0}{\scriptsize (all multiplicities $\ge 2$)}
  }
  \qquad
  \diag{6mm}{3}{2}{
    \cycl{1.3 2}{0 1}{1.1 0}{1.5 1}
    \cycl{1.3 2}{2.8 1}{1.1 0}{1.5 1}
    \picputtext{2.5 0.4}{$1$}
  }
  \qquad
  \diag{6mm}{3}{2}{
    \pictranslate{0 0.5}{
    \xcycl{0 0}{1.5 0}{3 0}{3 1.5}{1.5 1.5}{0 1.5}
    \picputtext{0.75 -0.3 x}{$1$}
    \picputtext{0.75 -0.3}{$1$}
    }
  }
  \qquad
  \diag{6mm}{3}{2}{
    \pictranslate{0 0.5}{
    \xcycl{0 0}{1.5 0}{3 0}{3 1.5}{1.5 1.5}{0 1.5}
    \picline{1.5 1.5}{1.5 0}
    \picputtext{2.25 -0.3}{$1$}
    \picputtext{0.75 -0.3}{$1$}
    }
  }
  \qquad
  \diag{6mm}{4}{2.5}{
    \pictranslate{0 0.5}{
    \xcycl{0 0}{1.5 0}{3 0}{3 1.5}{1.5 1.5}{0 1.5}
    \picline{1.5 1.5}{1.5 0}
    \picputtext{2.25 1.8}{$1$}
    \picputtext{0.75 -0.3}{$1$}
    \opencurvepath{0 1.5}{0 2}{0.5 2.5}{3 2.5}{4 2}{4 0.5}{3.5 0}{3 0}{}
    }
  }
  \\[5mm]
\end{array}
\]
}
\caption{The reduced Seifert graphs of the alternating diagrams
of special alternating links of braid index 4. Simple edges
have their multiplicity (1) attached, and the other edges (of
multiplicity one or more) are unlabelled. In the first graph,
exceptionally, all edges have multiplicity at least 2.\label{figSG}}
\end{figure}


Now consider the special diagrams. For them one considers the
Seifert graph, and needs to write
down all bipartite planar graphs on at most 6 vertices, which
have no cut vertex. Since the diagram $D$ is special, the placement
of multiple copies of an edge give diagrams equivalent up to
flypes, so it is enough to consider simple graphs (the reduced
Seifert graph), and have the multiplicities of an edge written
as its label. The graphs can be easily compiled using the observation
that they must contain a cycle of length 4 or 6; see figure
\reference{figSG}. By direct inspection we see that the edge
multiplicities must be as specified in the figure. (In fact if an
edge is multiple it turns out irrelevant what its multiplicity
is, so in this case we just omit the label.) We rule out the
remaining multiplicities by a skein theoretic calculation,
similar to the one explained for case \reference{Yb}.

Let w.l.o.g. (up to mirroring) $D$ be positive. For each edge
$e$ in $\Gm(D)$ of variable multiplicity $\ge i$ (where $i=1,2$)
we calculate the skein polynomial of the diagram that
corresponds to $\Gm$ for multiplicities $i$ and $i+1$ of $e$.
That is, if $\Gm(D)$ has $l$ edges of variable multiplicity,
we have $2^l$ polynomials to calculate. Then we check for
each such set of $2^l$ polynomials that $Q=P_{v^{9-\chi(D)}}$
is non-zero, and $\Md_zP-\Md_zQ$ as well as $\Mc_zQ$ is
constant within this set of $2^l$ polynomials. Then
by \eqref{srel} this property is inherited to diagrams
$D$ whose $\Gm(D)$ have edges of higher multiplicity,
and in particular $MWF\ge 5$.

There is one more graph,
\[
\diag{6mm}{3}{2}{
  \cycl{2.0 2}{0 1}{1.8 0}{1.2 1}
  \cycl{2.0 2}{2.4 1}{1.8 0}{3.5 1}
}
\]
not included in figure \reference{figSG}. In that
case (by the method we just explained we verify that)
$MWF\ge 5$ for all non-zero edge multiplicities. \qed

In \cite{MurPrz2}, Murasugi-Przytycki define a certain
quantity $\inx(D)$, assigned to a link diagram $D$,
called \em{index}. (We omit here the detailed discussion;
one can consult also \cite{Ohyama} or \cite{gener}.)
Their motivation was to give an upper estimate 
\begin{eqn}\label{mp}
b(L)\le s(D)-\inx(D)
\end{eqn}
for the braid index of the underlying link $L$. Their origin
of \eqref{mp} consists in an appropriate move (see
figure 8.2 in \cite{MurPrz}) which reduces
the number of Seifert circles of the diagram.
Murasugi-Przytycki conjectured that for an alternating
diagram $D$, the inequality \eqref{mp} is exact. This
conjecture is also confirmed for alternating links up
to braid index 4. 

Based on the Murasugi-Przytycki procedure, we can re-enter
the Bennequin surface topic.

\begin{corr}\label{cfT}
Alternating links of braid index at most 4 carry a Bennequin
surface on a minimal string braid.
\end{corr}

\proof In \cite{gener} it was explained how to apply
restrictedly the Seifert circle reduction move of
Murasugi-Przytycki (and then those of Yamada \cite{Yamada})
so as to obtain a braided surface. This modified reduction
is easily checked to lead to the minimal number of strings for the
links in question. \qed




\begin{corr}
Let $L$ be an alternating link of braid index $4$. Then
$|\Mc\Dl(L)|\le 5$, and if $|\Mc\Dl(L)|>2$, then $L$ is
special alternating.
\end{corr}

\proof It is well known, that $|\Mc\Dl(L)|$ is multiplicative
under Murasugi sum and for a special diagram depends only
on the reduced Seifert graph. The result follows by calculation
for the specific types. \qed

The proof of this corollary, and the extension of the multiplicativity
of $\Mc\Dl$ to $\Mc_zP$ for diagrammatic Murasugi sum \cite{MurPrz}
demonstrates also the following more general principle:

\begin{corr}\label{cSG}
For any given braid index, there are only finitely many values of
$\Mc\Dl$ and $\Mc_zP$ among Alexander and skein polynomials of
alternating links of that braid index. \qed
\end{corr}

We saw that for $\Dl$ this statement is wrong for non-alternating
links even among 3-braids. On the other hand, by \cite{3br},
it is true for $P$, and we do not know if it remains true for
(closed) braids on more strings. (One could also ask if
infinitely many leading coefficients of $\Dl$ occur if $\Md\Dl
=1-\chi$, but we se no deeper meaning in this question, so will
not dwell further upon it here.)

The following is also worth observing. Call a subclass
$\cC'$ of a class $\cC$ of links \em{generic} in $\cC$ if
\[
\lim_{n\to\infty}\,\frac{\#\,\{L\in \cC'\,:\,c(L)=n\,\}}
{\#\,\{L\in \cC\,:\,c(L)=n\,\}}\,=\,1\,.
\]

\begin{corr}
The number of special alternating links of given braid index
grows polynomially in the crossing number. In particular,
a generic alternating link of given braid index is not
special alternating.
\end{corr}

\proof A special alternating link is determined by the Seifert
($=$ checkerboard) graph of its alternating diagram. The number
of such graphs with a fixed number of vertices grows polynomially
in the number of edges. The second claim in the corollary
follows because it is easy to see that in contrast the number
of non-special alternating links grows exponentially (due to
exponentially many, in the crossing number, ways to perform the
Murasugi sum at a separating Seifert circle of the alternating
diagram). \qed

\begin{rem}
Note that in contrast we showed in \cite{SV} that a generic
alternating knot (and the case of links is analogous) of given
\em{genus is} special alternating. This shows from yet another
point of view the opposition between genus and braid index.
\end{rem}

Another immediate and useful consequence of theorem \ref{tty}
and the preceding remarks is

\begin{corr}\label{cft}
If an alternating link $L$ has $MWF(L)\le 4$ (in particular
if $b(L)\le 4$), then the MWF inequality is exact
(i.e. an equality) for $L$. \qed
\end{corr}

This gives a nice complement to the MWF exactness results in
\cite{Murasugi,MurPrz2}. (As another such amplification, we 
proved the case of \em{knots} and genus $\le 4$ in \cite{gener}.)

Note that at MWF bound 5 we hit already at the Murasugi-Przytycki
examples \cite{MurPrz2} of non-exact MWF (with $b=6$). So corollary
\reference{cft} is not true for $MWF\ge 5$ or $b\ge 6$. We do
not know about the case $b=5$. However, ruling out braid index
$5$ for the Murasugi-Przytycki family is a serious computational
problem (only two specific members were dealt with, a 4-component
15 crossing link and an 18 crossing knot; see \cite[\S 19]
{MurPrz2}). Already with this circumstance in mind,
one cannot expect to easily extend the corollary (or theorem
\reference{tty}) for $b=5$ either, even if it may be true.

On the other hand, leaving these troublesome exceptions aside,
the above discussion should fairly clearly explain how
the general picture continues for alternating links with MWF
bound 5 and more.
