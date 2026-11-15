---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-019-512-maximal-subwords
section_title: "Maximal subwords"
section_number: 5.1.2
pages: 27-28
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.985
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Here we start the technical considerations needed to prove 
theorem \reference{thmwf}. We consider the form \eqref{wd},
now with all $l_i>0$.

\begin{defi}
We define \em{summit syllables} in \eqref{wd}:
\def\theenumi{\alph{enumi}}
\def\labelenumi{\theenumi)}
\begin{enumerate}
\item All $\sg_{n-1}^{l_i}$ are summit syllables, and
\item if $\ap=\sg_k^{l_i}$ and $\ap'=\sg_k^{l_j}$ are summit
syllables, with no $\sg_{k'}^{l'}$ for $k'\ge k$ occurring between
$\ap$ and $\ap'$, then all $\sg_{k-1}^{l'}$ occurring between $\ap$
and $\ap'$ are summit syllables.
\end{enumerate}
\end{defi}

Note that, according to definition \reference{dfext}, we
consider syllables in cyclic order. The relation ``between'' in
the above definition should also be understood in that sense:
a syllable occurring after the last index $i$ syllable
$\ap$ and/or before the first index $i$ syllable $\ap'$ is
considered to be between $\ap$ and $\ap'$.

For the following considerations it is (not necessary but) helpful
to visualize $\bt$ by the braid scheme explained in \cite{bind}.

Separate $\bt$ in
\eqref{wd} into subwords $\ap_1\dots \ap_n$, such that $\ap_i$
contains only syllables of odd or even index, and this parity
changes between $\ap_i$ and $\ap_{i+1}$. Then for a syllable
$\sg_k^l$ occurring in $\ap_i$, put the integer $l$ at the point
$(k,i)\in \bN\times \bN\subset \bR^2$ in the plane. Here $(k,i)$
is the point in the $i$-th row and $k$-th column, with rows
numbered (as in Cartesian coordinates) from bottom to top and
columns from left to right.

One obtains a certain checkerboard pattern of integers we call
\em{braid scheme} of $\bt$. (If we do not put any integer on
a point $(k,i)$, we assume its ``content'' is zero, or it is
``empty''. So for all non-empty points $(k,i)$ in the scheme,
$i+k$ is always even or always odd.)

One can \em{reduce} the
scheme by moving an integer $l$ at $(k,i)$ to $(k,i-2)$ if $i>2$
and the points $(k\pm 1,i-1)$ are empty. We call the scheme
reduced if it does not admit any such move. Then in a reduced
scheme, summit syllables of $\bt$ are those, whose entries in
the scheme are ``on top'' when viewing the scheme from the left.
{}From this viewangle the following ``geographic'' choice of
terminology becomes more plausible.


\begin{defi}
Summit syllables still have a cyclic order from \eqref{wd}. We call
the subword $\bt'$ of $\bt$ in \eqref{wd} made of summit syllables
the \em{maximal subword}. The subword made of non-summit syllables
(i.e. the subword obtained by deleting in $\bt$ all syllables in
$\bt'$) is called \em{non-maximal subword}. 

Note that neighbored summit syllables have indices $k_i$ differing
by $\pm 1$. We say that a summit syllable is \em{minimal} resp.
\em{maximal} if its both neighbors have higher resp.\ lower index.

We call $\bt$ \em{summit reduced} if all its minimal summit syllables
are non-trivial.  We call $\bt$ \em{index reduced} if it is
non-singular and its index sum $\sum_{i=1}^n k_i\cdot l_i$ cannot be
reduced by a Yang-Baxter relation, i.e. $\bt$ contains no
$\sg_{i+1}\sg_i\sg_{i+1}$ as subword.
\end{defi}

\begin{lemma}
Index reduced $\So$ summit reduced. In particular a summit reduced
form always exists.\qed
\end{lemma}

Recall that a positive resolution tree is a rooted tree with directed 
edges,
whose vertices (nodes) contain positive braid words, the root labelled
by $\bt$. Every vertex has exactly one incoming edge, except the
root that has none, and zero or two outoutgoing edges. In former
case it is labelled by an unlink (terminal node).
In latter case it is labelled by
a word of the form $\ap\sg_i^2\ap'$, with $\ap,\ap'$ positive
words, and the two vertices connected by the outgoing edges 
are labelled by $\ap\sg_i\ap'$ and $\ap\ap'$, or positive words
obtained therefrom by Markov equivalence (isotopy of the closure link).

In \cite{Nakamura} the following fact was observed, and used
decisively, and we shall do the same here.

\begin{theorem}(Nakamura \cite{Nakamura})
$MWF(\bt)$ is the maximal number of components of a (link in a) node
in a positive resolution tree for $\bt$.
\end{theorem}

In particular, $MWF$ is monotonous (does not decrease) under word
extension, and does not depend on the exponent of non-trivial
syllables.

\begin{lemma}\label{lemh}
If $\bt$ is \em{summit reduced}, and $\bt'$ is obtained from $\bt$
by removing all summit syllables, then there is a positive resolution
tree for $\bt$ that contains $\bt'$ as a node.
\end{lemma}

\proof Since minimal syllables are non-trivial, one can delete them
in the resolution tree. The two neighbors in the maximal subword
join to a non-trivial new minimal syllable, and so one iterates the
procedure. \qed

Since all $\sg_{n-1}^{l'}$, $\sg_{n-2}^{l'}$ in \eqref{wd} occur as
summit syllables, $\bt'$ has split last two strands, and so we have
a quick proof of Nakamura's main result.

\begin{corr}(Nakamura \cite{Nakamura})
Any summit reduced positive word on $n\ge 3$ strands has $MWF\ge 3$.
\qed
\end{corr}

In particular any positive braid representation of a $(2,n)$-torus
link can be reduced to the standard one by index-decreasing YB
relations and removals of nugatory crossings.
