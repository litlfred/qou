---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-018-511-the-morton-williams-franks-bound
section_title: "The Morton-Williams-Franks bound"
section_number: 5.1.1
pages: 26-27
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.995
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
For the proof of theorem \reference{thg} we will need to study
the behaviour of the bound \eqref{mwfb} in the Morton-Williams-Franks
inequality (we abbreviate as MWF) on positive
braids. This was begun by Nakamura \cite{Nakamura},
who settled the case $MWF=2$ in the suggestive way: such braids
represent only the $(2,n)$-torus links. (The case $MWF=1$ is
trivial.) We will introduce a method that considerably simplifies
his proof (but still makes use of some of his ideas), and
then go on to deal with $MWF=3$. The example of non-sharp
MWF inequality, $13_{9365}$ in \cite{KnotScape} (the connected
2-cable of the trefoil), given in \cite{MorSho}, is in fact
only among a small family of exceptional cases.

\begin{theorem}\label{thmwf}
If $b(\hat\bt)>MWF(\hat\bt)=3$, then $\bt$ reduces to a 4-braid,
and is given by one of the following forms (assuming that $3*$
denotes a sequence of at least one letter $3$, and $11*$
resp.\ $22*$ sequences of at least two letters $1$ or $2$):\\
\[
[22*3*122*11*23211*], \quad\mbox{and}\quad [22*3122*11*23*211*].
\]
\end{theorem}


We will reduce the proof to a finite number of words to
check, which is done by calculation using the program of
\cite{MorSho}. Since a direct computation is more reliable
than an increasingly difficult mathematical argument, we have
not tried to minimize the calculation by all means. However,
we point out that for the sake of theorem \reference{thg}
alone (rather than its refinement, theorem \reference{thmwf}),
the following weaker statement is sufficient, for which
a considerable part of the case-by-case calculations can
be dropped. This corollary requires the notion of
semiadequacy \cite{LickThis}, and can be deduced from theorem
\reference{thmwf} by direct check of the exceptional words.
(We will sometimes write $MWF(\bt)$ for $MWF(\hat\bt)$.)

\begin{corr}\label{cort}
If $\bt$ is a positive braid word, and $MWF(\bt)=3$, then $\bt$
reduces (up to Markov equivalence) to a positive 4-braid word $\bt'$,
and the diagram $\hat\bt'$ is not $B$-adequate.
\end{corr}

Here the notions of $A$-adequate and $B$-adequate for diagrams
and braids are as explained in \S\ref{brD} and \S\ref{brt}. We
note, as a consequence of \cite{Thistle}, that a braid is ($A$/
$B$-)adequate if and only if some, or equivalently any,
minimal length word of a braid in its conjugacy class it is so.

We will thus prove theorem \reference{thg} only using corollary
\reference{cort}, and indicate in the proof of theorem \reference{thmwf}
the point where the corollary follows (and the rest of the argument
is not needed). The argument that elegantly replaces the remaining
case-by-case checks requires theorem \reference{thq}. Since (by
taking again the full extent of our proof) theorem \reference{thq}
is nonetheless not indispensable, we permit ourselves to defer its
proof to a separate paper \cite{ntriv}.

















\proof[of theorem \reference{thg}]
If $MWF(\bt)\le 2$, then we are done. So assume $MWF(\bt)=3$.
Assume first $L$ has an $A$-adequate 3-braid. Since $A$-adequate
diagrams minimize the number of negative crossings, and $L$ has
a positive (braid) diagram, the $A$-adequate 3-braid diagram is
positive, and we are done. So let $L$ have a $B$-adequate 3-braid
diagram $\hat\bt'$. Now by corollary \reference{cort}, we find
that $L$ reduces to a positive 4-braid $\bt$
with $c_+(\bt)$ positive crossings, and $\bt$ is not $B$-adequate.
Since $\bt'$ is $B$-adequate and $B$-adequate diagrams
minimize the number of positive crossings, $c_+(\bt')<c_+(\bt)$.
On the other hand, $MWF(L)=3$ and the inequalities of MWF for the
$v$-degree of $P$ show that $\bt'$ must have exponent sum
$[\bt']=c_+(\bt)-1$. Since $[\bt']\le c_+(\bt')$, we must have
equality, so $\bt'$ is positive. \qed

Note the following easy and useful consequence of theorem 
\reference{thg}:

\begin{corr}
A link which is a closure of a positive braid of at most 4 strings,
has a minimal crossing diagram as a closed positive braid, and a
minimal string positive braid representation.
\end{corr}

\proof The case of the braid representation is straightforward,
and it implies the minimal crossing diagram statement by
looking at $\Md_zP$ and using Morton's inequalities. \qed

The examples in \cite{posex_bcr}, mentioned after theorem \ref{thg},
show that the corollary is not true in case of positive 5-braids at
least for the positive minimal braid representation. So far no examples
are known where no minimal crossing positive braid diagram exists
(it was known to exist from \cite{WilFr,Murasugi} for closed
positive braids with a full twist, which include the torus links,
and from \cite{posex_bcr} for positive braid knots of at most
16 crossings), but the pathologies for minimal strings hint to caution.
It was shown in \cite{posex_bcr} that one, and in \cite{ntriv} that
infinitely many fibered positive knots
have no minimal crossing positive diagram.
