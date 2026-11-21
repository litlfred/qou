---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-031-55-computation-using-localization
section_title: "Computation using localization"
section_number: 5.5
pages: 53-55
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.981
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnation of the Hecke category, a fundamental object in representation theory."
---
\label{subsec-compute}


Each object $B_{\un{x}}$ in $\DC$ splits in $\Kar(\DC_Q)$ as the sum of $Q_\eb$ over all subsequences $\eb$ of ${\un{x}}$. Here, $Q_\eb$ denotes the object which is the tensor product of $Q_{{\un{x}}_k}$
when $\eb_k=1$ and $\1$ when $\eb_k=0$. Given a graph expressing a morphism from a sequence $B_{\un{x}}$ of length $d$ to a sequence $B_{{\un{x}}'}$ of length $d'$, we can localize to obtain a $2^{d'} \times 2^d$ matrix of maps
between reflection sequences. Since Hom spaces between standard bimodules are always either rank 1 or 0, this matrix is actually populated with polynomials in $Q$, and is fairly sparse
(because many Hom spaces are zero a priori). Computing any term in this matrix consists of applying the appropriate projection and inclusion maps to the top and bottom of the graph, and
using the diagrammatics of $\Kar(\DC_Q)$ to reduce the graph to a dashed graph with the desired polynomial on the left. That is, given $({\un{x}},\eb)$ and $({\un{x}}',\eb')$, the coefficient of the
map $Q_\eb \to Q_{\eb'}$ of a map $\phi$ is given by reducing the following diagram $\phi_\eb^{\eb'}$.

\igc{2}{localizingamap}

There is no sign issue in this convention, even though a mixed graph represents a morphism only up to sign. For any Soergel graph $\phi$ we start with, we can choose a representative of
the isotopy class, and add idempotents as above to obtain a specific representative of the mixed graph. Different representatives of $\phi$ will give different mixed graphs, but they
differ only by isotopy of the solid part of the graph, and therefore have the same sign when viewed as morphisms in $\Kar(\DC_Q)$.

Note that by \eqref{slidebivalentthru2m}, the coefficient associated to $\eb=(1,1,\ldots,1)$ and $\eb' = (1,1,\ldots,1)$ of a $2m$-valent vertex is precisely $1$. Therefore, for any rex
move, this ``highest" coefficient will be $1$.

One can check if two maps in $\DC$ are equal by computing these two matrices and comparing the terms. More combinatorially, one can compute once and for all the ``basic" matrices
attached to the generating morphisms. For instance, the dot gives a $2 \times 1$ matrix, the trivalent vertex a $4 \times 2$ matrix, and the $2m$-valent vertex a $2^m \times 2^m$ matrix.
Computing a more general map consists merely of multiplying these basic matrices and annoying bookkeeping. Computers excel at such tasks.

We have not yet proven it, but the passage $\DC \to \DC_Q$ is faithful. Not knowing this, the equality of two matrices only implies that the original maps are equal modulo $R$-torsion.
However, location is injective in the bimodule world, because Hom spaces are free left $R$-modules. In other words, all $R$-torsion is in the kernel of the functor $\FC$. Therefore we can
calculate whether two Soergel graphs have the same image under $\FC$ by localizing $\DC \to \Kar(\DC_Q)$ and computing the matrices above. This is a powerful tool.

For instance, we want to know whether both sides of the $B_3$ relation \eqref{B3} correspond to the same map between Bott-Samelson bimodules. One need only compute by hand the matrices
associated to the 4-valent, 6-valent, and 8-valent vertices, and then plug in two appropriate formulae into a computer. Checking that two sparse matrices of size $2^8 \times 2^8$ are equal
is trivial. If we knew what the $H_3$ relation \eqref{H3} should be, then checking it would require calculating the 10-valent vertex (which is easy), and then computation of a pair of
$2^{15} \times 2^{15}$ matrices (which is quite time-consuming). Unfortunately, backsolving for the coefficients in the H3 relation would require doing linear algebra with a large number
$N$ of unknowns (at least $70$). There is an equation for each nonzero term in a sparse $2^{15} \times 2^{15}$ matrix, and the coefficients come from $N$ different such matrices which need
to be computed. Neither the author's computers nor their brains appear to be up to the task.

Finally, we provide the alternative proof of faithfulness.

\begin{prop} $\StdF$ is faithful. \label{stdfisfaithful2}\end{prop}

\begin{proof} In fact, the techniques we have developed allow us to construct a quasi-inverse for $\StdF$. We construct a functor $\GC$ from $\Kar(\DC_Q)$ to $\DStd_Q$ as follows. Let
$\GC$ send reflection sequences to themselves, and normal sequences to the corresponding formal direct sum of reflection sequences. On morphisms, $\GC$ will send standard graphs to
themselves. The generating morphisms which are not standard graphs are sent as follows: a bivalent vertex is sent to the appropriate inclusion or projection; a dot or trivalent vertex or
$2m$-valent vertex is sent to the appropriate matrix of standard diagrams. It is trivial to check that all the relations hold, so this functor is well-defined, and is obviously a
quasi-inverse to $\StdF$. \end{proof}

Remember that diagrams and their linear combinations are only useful for displaying morphisms between tensor products of generators, not for \emph{direct sums} of those. To talk about a
morphism between direct sums, we need to use matrices of diagrams. Thus we do not expect there to be an actual diagram in $\DStd_Q$ corresponding to a solid graph.

This proof that $\Kar(\DC_Q) \cong \DStd_Q$ was entirely diagrammatic, and no mention of bimodules was required.
