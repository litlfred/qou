---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-007-31-a-criterion-for-real-stability
section_title: "A criterion for real stability."
section_number: 3.1
pages: 8-10
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.661
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
For $f\in\CC[\x]$ and $\{i,j\}\subseteq[m]$, let
$$
\Delta_{ij}f
= \partial_i f \cdot \partial_j f - f \cdot \partial_i\partial_j f.
$$
Notice that for $f\in\CC[\x]^\ma$,
$$
\Delta_{ij}f
=
f_{i}^{j} f_{j} - f^{j} f_{ij}
=
\Wr_{i}[f^{j},f_{j}] = -\Wr_{i}[f_{j},f^{j}],
$$
and
$$
\Delta_{ij}f = f_{i}^{j} f_{j}^{i} - f^{ij} f_{ij}.
$$

\begin{theorem}[Theorem 5.6 of \cite{B} and Theorem 3 of \cite{WW}]
Let $f\in\RR[\x]^\ma$ be multiaffine.  The following are equivalent:\\
\textup{(a)}\ $f$ is real stable.\\
\textup{(b)}\ For all $\{i,j\}\subseteq[m]$ and all $\a\in\RR^m$,
$\Delta_{ij}f(\a)\geq 0$.\\
\textup{(c)}\ Either $m=1$, or there exists $\{i,j\}\subseteq[m]$ such that
$f_{i}$, $f^{i}$, $f_{j}$ and $f^{j}$ are real stable, and
$\Delta_{ij}f(\a)\geq 0$ for all $\a\in\RR^m$.
\end{theorem}
\begin{proof}
To see that (a) implies (b), fix $\{i,j\}\subseteq[m]$.
Proposition 2.7(a) shows that $f_{j}\ll f^{j}$, and from the
calculation above and Corollary 2.10, it follows that
$\Delta_{ij}f(\a)  = -\Wr_{i}[f_{j},f^{j}](\a)\geq 0$
for all $\a\in\RR^m$.

We show that (b) implies (a) by induction on $m$, the base
case $m=1$ being trivial.  For the induction step let $f$
be as in part (b), let $a\in\RR$, and let $g=f|_{x_{m}=a}$.
For all $\{i,j\}\subseteq[m-1]$ and $\a\in\RR^{m-1}$,
$\Delta_{ij}g(\a) = \Delta_{ij}f(\a,a)\geq 0$.  By induction,
$g = f^{m} + a f_{m}$ is real stable for all $a\in\RR$; it
follows that $a f_{m} + b f^{m}\in\StabR[x_{1},\ldots,x_{m-1}]$
for all $a,b\in\RR$.  Furthermore, for all $j\in[m-1]$ and
$\a\in\RR^{m-1}$,
$\Wr_{j}[f_{m},f^{m}](\a) = -\Delta_{jm} f(\a,1)\leq 0$.
This verifies condition (c) of Corollary 2.10 for the pair
$(f_{m},f^{m})$, and it follows that $f= f^{m}+ x_{m} f_{m}
\in\StabR[\x]$, completing the induction.

It is clear that (a) and (b) imply (c) -- we show that (c) implies (b) below.
This is clear if $m\leq 2$,  so assume that $m\geq 3$.  To begin with, let
$\{h,i,j\}\subseteq[m]$ be three distinct indices, and consider $\Delta_{ij}f$
as a polynomial in $x_{h}$.  That is, $\Delta_{ij}f =
A_{hij} x_{h}^{2} + B_{hij} x_{h} + C_{hij}$ in which
\showon
A_{hij} &=& f_{hi}^{j} f_{hj}^{i} - f_{h}^{ij} f_{hij} = \Delta_{ij}f_{h},\\
B_{hij} &=& f_{hi}^{j} f_{j}^{hi} - f_{h}^{ij} f_{ij}^{h}
+ f_{i}^{hj} f_{hj}^{i} - f^{hij} f_{hij},\ \mathrm{and}\\
C_{hij} &=& f_{i}^{hj} f_{j}^{hi} - f^{hij} f_{ij}^{h} = \Delta_{ij} f^{h}.
\showoff
If $\Delta_{ij}f(\a)\geq 0$ for all $\a\in\RR^{m}$ then this
quadratic polynomial in $x_{h}$:
$$
\Delta_{ij}f(a_{1},\ldots,a_{h-1},x_{h},a_{h+1},\ldots,a_{m})
$$
has a nonpositive discriminant for all $\a\in\RR^m$.  That is,
$D_{hij} = B_{hij}^{2}-4A_{hij}C_{hij}$
is such that $D_{hij}(\a)\leq 0$ for all $\a\in\RR^{m}$.

It is a surprising fact that as a polynomial in
$\{x_{k}:\ k\in[m]\drop\{h,i,j\}\}$, $D_{hij}$ is invariant under all
six permutations of its indices, as is seen by direct calculation:
\showon
D_{hij}
&=&
(f_{h}^{ij}f_{ij}^{h})^{2} + 
(f_{i}^{hj}f_{hj}^{i})^{2} +
(f_{j}^{hi}f_{hi}^{j})^{2} +
(f_{hij}f^{hij})^{2}\\
& &
-2( f_{h}^{ij}f_{ij}^{h}f_{i}^{hj}f_{hj}^{i}
+ f_{i}^{hj}f_{hj}^{i}f_{j}^{hi}h_{hi}^{j}
+ f_{j}^{hi}f_{hi}^{j}f_{h}^{ij}f_{ij}^{h} )\\
& &
-2 (f_{h}^{ij}f_{ij}^{h} + f_{i}^{hj}f_{hj}^{i} +
f_{j}^{hi} f_{hi}^{j}) f^{hij}f_{hij}\\
& & 
+ 4 f_{ij}^{h} f_{hj}^{i} f_{hi}^{j} f^{hij} 
+ 4 f_{h}^{ij} f_{i}^{hj} f_{j}^{hi} f_{hij}.
\showoff

Now for the proof that (c) implies (b) when $m\geq 3$.
Consider any $h\in[m]\drop\{i,j\}$.  Then
$$
\Delta_{hi}f = A_{jhi} x_{j}^{2} + B_{jhi} x_{j} + C_{jhi}
$$
has discriminant $D_{jhi}=D_{hij}$.  Since $f_{j}$ and
$f^{j}$ are real stable, we have
$A_{jhi}(\a)=\Delta_{hi}f_{j}(\a)\geq 0$ and
$C_{jhi}(\a)=\Delta_{hi}f^{j}(\a)\geq 0$ for all $\a\in\RR^{m}$.
Since $\Delta_{ij} f(\a)\geq 0$ for all $\a\in\RR^{m}$
it follows that $D_{jhi}(\a)=D_{hij}(\a)\leq 0$ for all
$\a\in\RR^{m}$.  It follows that $\Delta_{hi}f(\a)\geq 0$
for all $\a\in\RR^{m}$.  (Note that if $B^{2}-4AC\leq 0$
and either $A=0$ or $C=0$, then $B=0$.)  A similar
argument using the fact that $f_{i}$ and $f^{i}$ are real
stable shows that $\Delta_{hj}f(\a)\geq 0$ for all $\a\in\RR^{m}$.

It remains to show that $\Delta_{hk}f(\a)\geq 0$ for all
$\a\in\RR^{m}$ when $\{h,k\}$ is disjoint from $\{i,j\}$.
We have seen that $\Delta_{hi}f(\a)\geq 0$ for all $\a\in\RR^{m}$,
and we know that both $f_{i}$ and $f^{i}$ are real stable.
The argument above applies once more:\ $\Delta_{hi}f(\a)\geq 0$
for all $\a\in\RR^{m}$, so that $D_{ihk}(\a)=D_{khi}(\a)\leq 0$
for all $\a\in\RR^{m}$, and then since $A_{ihk}(\a)\geq 0$
and $C_{ihk}(\a)\geq 0$ for all $\a\in\RR^{m}$ it follows that
$\Delta_{hk} f(\a)\geq 0$ for all $\a\in\RR^{m}$.  Thus
(c) implies (b).
\end{proof}
\noindent
