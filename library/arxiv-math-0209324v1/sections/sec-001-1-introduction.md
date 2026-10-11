---
doc_id: arxiv-math-0209324v1
doc_title: "Cyclotomic completions of polynomial rings"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 0209324v1.pdf
source_sha256: ae2ea5024a0a45e8
doc_brief: "Cyclotomic completions of polynomial rings — The main object of study in this paper is the completion Z[q]N = lim←− n Z[q]/ ((1− q)(1− q2)···(1− qn)) of the polynomial ring Z[q], which arises from"
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
---
\label{sec:introduction}
The main object of study in this paper is the completion
\begin{equation}
  \label{eq:3}
  \ZqN = \varprojlim_{n\ge 0} \modZ [q] /((q)_n)
\end{equation}
of the polynomial ring $\modZ [q]$ in an indeterminate $q$, where we use
the notation
\[
(q)_n =(1-q)(1-q^2)\cdots(1-q^n)\in \modZ [q], \quad n\ge 0.
\]
Each element $a\in \ZqN$ is expressed as an infinite sum
\begin{equation}
  \label{eq:17}
  a = \sum_{n\ge 0} a_n(q)_n,
\end{equation}
where $a_n\in \modZ [q]$ for $n\ge 0$.

Some specific instances of the series~\eqref{eq:17} and some variants
which can define elements of $\ZqN$ can be found in the literature.
Zagier \cite{Zagier} studied the series $\sum_{n\ge 0}(q)_n$, which was
introduced by Kontsevich, and observed that it can be expanded in
$q-\zeta $ for any root $\zeta $ of unity.  Clearly, this is the case also for
any elements of $\ZqN$.  Some of the formulae given by Lawrence and
Zagier~\cite{Lawrence-Zagier} and by Le~\cite{Le} for the values of the
$sl_2$ Witten-Reshetikhin-Turaev invariants \cite{Reshetikhin-Turaev}
\cite{Witten} of some particular $3$-manifolds, including the
Poincar\`e homology sphere, were expressed as infinite series similar
to~\eqref{eq:17}, and have well-defined values at the roots of unity.

The ring $\ZqN$ arises from the new invariant $I(M)$ of an
integral homology $3$-sphere $M$ that we announced
in~\cite{Habiro:rims2001} (see also~\cite{Ohtsuki:problemlist}).  (The
ring $\ZqN$ is denoted $\widehat{\modZ [q]}$ in~\cite{Habiro:rims2001}.)
The invariant $I(M)$ takes values in $\ZqN$ and unifies all the $sl_2$
Witten-Reshetikhin-Turaev
invariants $\tau _\zeta (M)$ defined at various roots $\zeta $ of unity; i.e.,
for any root $\zeta $ of unity we have
\[
  I(M)|_{q=\zeta }=\tau _\zeta (M).
\]
As we explained in \cite{Habiro:rims2001}, the existence of the invariant
$I(M)$ generalizes the previous integrality results \cite{Lawrence}
\cite{Murakami} \cite{Ohtsuki} \cite{Rozansky} on the
Witten-Reshetikhin-Turaev invariant for integral homology spheres.

The present paper was at first intended to provide the results on the
ring $\ZqN$ announced in~\cite{Habiro:rims2001} and those necessary
for the future papers \cite{Habiro:in-preparation} in which we will
prove the existence of $I(M)$.  From purely algebraic interests,
however, we will also study some generalizations of $\ZqN$ as follows.

Let $R$ be a commutative ring with unit, and let $R[q]$ denote the
polynomial ring over $R$ in an indeterminate $q$.  For each
$n\in \modN =\{1,2,\ldots\}$ let $\Phi _n(q)$ denote the $n$th cyclotomic
polynomial
\[
  \Phi _n(q)=\prod_{(i,n)=1}(q-\zeta ^i)\in \modZ [q],
\]
where $\zeta $ is a primitive $n$th root of unity.  If $S\subset \modN $ is a
subset, we set
\[
\PHI_S=\{\Phi _n(q)\zzzvert n\in S\}\subset \modZ [q],
\]
and let $\PHI_S^*$ denote the multiplicative set in $\modZ [q]$ generated
by $\PHI_S$, which we will regard as a directed set with respect to
the divisibility relation $|$.  The principal ideals $(f(q))\subset R[q]$
for $f(q)\in \PHI_S^*$ define a linear topology of the ring $R[q]$.
Define a commutative $R$-algebra $\RqS$ by
\begin{equation}
  \label{eq:1}
  \RqS = \varprojlim_{f(q)\in \PHI_S^*} R[q]/(f(q)),
\end{equation}
which we will call the {\em ($S$-)cyclotomic completion\/} of $R[q]$.
Since the sequence $(-1)^n(q)_n$, $n\ge 0$, is cofinal to the directed
set $\PHI_\modN ^*$, the definition~\eqref{eq:1} is consistent
with~\eqref{eq:3}.  Note that if $S$ is finite, then $\RqS$ is
identified with
the $(\prod\PHI_S)$-adic completion
of $R[q]$, where $\prod\PHI_S =
\prod_{f\in \PHI_S}f=\prod_{n\in S}\Phi _n(q)$.  In particular, we have
$\Rq{\{1\}}\simeq R[[q-1]]$ and $\Rq{\{2\}}\simeq R[[q+1]]$.  In
general, we have a natural isomorphism
\[
\ZqS\simeq\varprojlim_{S'\subset S, |S'|<S}\Zq{S'},
\]
where $S'$ runs through all the finite subsets of $S$.

We are interested in the behavior of natural homomorphisms among the
cyclotomic completions
$\RqS$ for various $R$ and $S$, and also those among the $\RqS$ and some
other rings.  First of all, if $g\zzzcolon R\rightarrow R'$ is a ring homomorphism, then
for each $S\subset \modN $ the homomorphism $g_q\zzzcolon R[q]\rightarrow R'[q]$, induced by $g$,
induces a ring homomorphism $g_S\zzzcolon \RqS\rightarrow \xq{R'}S$.  If $g$ is
injective (resp.  surjective), then so is $g_S$ (see
Lemma~\ref{lem:1}).

More interesting homomorphisms among cyclotomic completions
 are induced by inclusions
$S'\subset S\subset \modN $.  In this case, $\PHI_{S'}^*$ is a directed subset of
$\PHI_S^*$, and hence $\id_{R[q]}$ induces an $R$-algebra homomorphism
\[
\rho ^R_{S,S'}\zzzcolon \RqS\rightarrow \Rq{S'}.
\]
The rings $\RqS$ for $S\subset \modN $ and the homomorphisms $\rho ^R_{S,S'}$ form
a presheaf of rings over the set $\modN $ with the discrete topology;
i.e., we have $\Rq{\emptyset}=\{0\}$ and
$\rho ^R_{S,S''}=\rho ^R_{S',S''}\rho ^R_{S,S'}$ if $S''\subset S'\subset S\subset \modN $.

We will state a sufficient condition for $\rho ^R_{S,S'}$ to be injective
using a certain graph defined on the set $S$.  For each subset $S\subset \modN $, let
$\Gamma _R(S)$ denote the graph (with loop-edges) whose set of vertices
is $S$, and in which two elements $n,n'\in S$ are adjacent if and
only if either
\begin{enumerate}
\item $n=n'$,
\item $n/n'$ is an integer power of a prime $p$ such that $R$ is
$p$-adically separated, i.e., $\bigcap_{j\ge 0}p^jR=(0)$, or
\item $R=\{0\}$.
\end{enumerate}
If either one of the above conditions holds, then we write $n\Leftrightarrow _Rn'$.
For example, in $\Gamma _\modZ (\modN )$ two vertices $n,n'$ are adjacent if and
only if $n/n'$ is an integer power of a prime, and hence the graph
$\Gamma _\modZ (\modN )$ is connected; while the graph $\Gamma _\modQ (\modN )$ is discrete,
i.e., two distinct vertices are never adjacent.  Theorem~\ref{thm:17}
states that if $S'\subset S\subset \modN $ are subsets such that for any $n\in S$ there
is a sequence $S'\ni n'\Leftrightarrow _R\cdots\Leftrightarrow _Rn$ in $S$, then the homomorphism
$\rho ^R_{S,S'}$ is injective.
A nonempty subset
$S\subset \modN $ is said to be {\em $\Leftrightarrow _R$-connected} if the graph $\Gamma _R(S)$ is
connected.  It follows that
if $S\subset \modN $ is $\Leftrightarrow _R$-connected, then for any nonempty subset $S'\subset S$
the homomorphism $\rho ^R_{S,S'}$ is injective.
In particular, since $\modN $ is $\Leftrightarrow _\modZ $-connected, for each $n\in \modN $ the
homomorphism
\[
  \rho ^\modZ _{\modN ,\{n\}}\zzzcolon \ZqN\rightarrow  \Zq{\{n\}}
  \bigl(= \varprojlim_{j\ge 0} \modZ [q]/(\Phi _n(q)^j)\bigr)
\]
is injective.

If $\zeta $ is a primitive $n$th root of unity, then the
homomorphism
\[
\sigma ^\modZ _{\modN ,\zeta }\zzzcolon \ZqN\rightarrow \modZ [\zeta ][[q-\zeta ]],
\]
which is induced by the inclusion $\modZ [q]\subset \modZ [\zeta ][q]$ and factors
through $\rho ^\modZ _{\modN ,\{n\}}$, is injective (Theorem~\ref{thm:13}).  In
other words, each element of $\ZqN$ is uniquely determined by its
power series expansion in $q-\zeta $.  In particular, the invariant $I(M)$
of an integral homology sphere $M$ is completely determined by its
expansion in $q-\zeta $ for one root $\zeta $ of unity,
which in the case $\zeta =1$ is the Ohtsuki
series~\cite{Ohtsuki}.  Since $\modZ [\zeta ][[q-\zeta ]]$ is an integral domain,
it follows that so is $\ZqN$ (Corollary~\ref{thm:8}).

We are also interested in the homomorphism
\[
  \tau ^R_{S,T}\zzzcolon \RqS \rightarrow  P_T(R) = \prod_{n\in T}R[q]/(\Phi _n(q))
\]
for $T\subset S\subset \modN $, induced by the homomorphism $R[q]\rightarrow P_T(R)$,
$f(q)\mapsto(f(q)\mod(\Phi _n(q)))_{n\in T}$, where $R$ is a subring of the
field $\bar\modQ $ of algebraic numbers.  If $S$ is $\Leftrightarrow _R$-connected, and
for some $n\in S$ there are infinitely many elements $m\in T$ with
$m\Leftrightarrow _Rn$, then $\tau ^R_{S,T}$ is injective (Theorem~\ref{thm:3}).  In
particular, if $T\subset \modN $
contains infinitely many prime powers, then
$\tau ^\modZ _{\modN ,T}\zzzcolon \ZqN\rightarrow P_T(\modZ )$ is injective.  Hence it follows that if
$Z$ is a set of roots of unity containing infinitely many elements
of prime power order, then the homomorphism
\[
\tau ^R_{S,Z}\zzzcolon \ZqS \rightarrow  P_Z(\modZ ) = \prod_{\zeta \in Z}\modZ [\zeta ],
\]
induced by $\modZ [q]\rightarrow P_Z(\modZ )$, $f(q)\mapsto(f(\zeta ))_{\zeta \in Z}$, is
injective (Theorem~\ref{thm:2}).  In other words, each element in
$\ZqN$ is uniquely determined by its values at roots of unity in such
a set $Z$.  In particular, it follows that the invariant $I(M)$ of an
integral homology sphere $M$ is completely determined by the
Witten-Reshetikhin-Turaev invariants $\tau _\zeta (M)$ with $\zeta \in Z$.

Recall that a holomorphic function defined in a region is determined
either by the power series expansion at one point or by its values at
any infinitely many points contained in a compact set in the region.
The properties of $\ZqN$ described above may be interpreted that
$\ZqN$ behaves like the ring of ``holomorphic functions defined in
the set of the roots of unity''.  These properties are not as obvious as
they might first appear; the ring $\QqN$, which contains $\ZqN$ as a
subring, is quite contrasting.  We have an isomorphism
\[
\QqN \simeq \prod_{n\in \modN } \Qqn,
\]
see Section~\ref{sec:structure-qqh}.  It follows that
$\rho ^\modQ _{\modN ,\{n\}}$ for $n\in \modN $ and $\tau ^\modQ _{\modN ,\modN }$ are {\em not\/}
injective (but surjective), and that $\QqN$ is {\em not\/} an integral
domain.

The results stated above are more or less generalized in the later
sections.

The rest of the paper is organized as follows.  In
Section~\ref{sec:preliminaries} we fix some notations.
Section~\ref{sec:lemma-compl-polyn} deals with what we might call
``monic completions'' of $R[q]$, which are generalizations of
cyclotomic completions defined using monic polynomials instead of
cyclotomic polynomials.  In Section~\ref{sec:injectivity-rs-s} we
apply the results in Section~\ref{sec:lemma-compl-polyn} to cyclotomic
completions, and study the conditions for the homomorphisms
$\rho ^R_{S,S'}$ to be injective.  In Section~\ref{sec:z-cycl-compl} we
consider the power series expansion of the elements of $\RqS$ in
$q-\zeta $ with $\zeta \in R$ root of unity of order contained in $S$.  In
Section~\ref{sec:values-at-roots} we study the homomorphisms
$\tau ^R_{S,T}$ and $\tau ^R_{S,Z}$.  In Section~\ref{sec:some-remarks} we
give some remarks.
