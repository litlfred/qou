---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-008-the-gross-taylor-expansion
section_title: "The Gross-Taylor Expansion"
section_number: null
pages: 12-13
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.917
latex_coverage_ratio: 0.996
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
[]{#GTExpansion label="GTExpansion"} Consider the fixed-degree correlator [\[ExactCorrelators\]](#ExactCorrelators){reference-type="eqref" reference="ExactCorrelators"}. It features a sum over Young diagrams of the Fourier transform of conjugacy classes weighted by a generalized Plancherel measure -- it seems it can be interpreted as a complicated Hurwitz correlator. Nevertheless, there is an obstacle to this interpretation, namely that the sum over Young diagrams runs only over diagrams with less than $N$ rows. If we wish to reach a symmetric group correlator interpretation furthermore to be identified with a string correlation function, it is imperative to take the large $N$ limit first. Therefore, we turn to the study of the large $N$ asymptotic expansion of Yang-Mills theory. We will explain how to perform the expansion as well as its regime of validity. We thus prepare the ground for the following sections where we will match the perturbative expansion of Yang-Mills theory with the correlators of a perturbatively defined string theory.

To produce the asymptotic expansion, we expand each $N$-dependent term inside the sum over partitions in equation [\[ExactCorrelators\]](#ExactCorrelators){reference-type="eqref" reference="ExactCorrelators"}. However, on Riemann surfaces of genus $G\leq 1$, this expansion only captures a chiral half of the full theory. Indeed, the Young diagrams with $N$ boxes or more appear to be exponentially suppressed in the expansion, because the factor $q^d$ is of order $\mathcal{O}(e^{-N g_{YM}^2 A})$ for these diagrams.[^1] Yet some of these representations are then wrongfully convicted: they are only exponentially suppressed as an artifact of our splitting of the exponential term ([\[Splitting\]](#Splitting){reference-type="ref" reference="Splitting"}). Indeed, for certain special diagrams [@Gross:1993hu], the terms $dN$ and $2f_{2}(\lambda)$ conspire to give a result of order $N$ and thus an exponential term of order $1$, even though both of these terms are of order $N^2$. This can be seen explicitly by expanding the term $f_{2}(\lambda)$ [@Gross:1993hu]. We define the chiral theory as the naive asymptotic expansion of the full two-dimensional Yang-Mills theory.

In [@Gross:1993hu], all representations with a Casimir of order $\mathcal{O}(N)$ were identified, and it was argued that (the asymptotic expansion of) the full theory can be encoded into two coupled copies of a chiral theory. In this paper, we do not discuss the full Yang-Mills theory on Riemann surfaces of genus $G\leq 1$ any further -- we shall focus instead on deriving a string dual for the chiral Yang-Mills theory.

The situation is different for higher genus Riemann surfaces [@Gross:1992tu]. There, representations indexed by diagrams comprising $N$ boxes or more are exponentially suppressed regardless of whether we split the Casimir term in two. Indeed, for each value of $d$, the dominant term in the asymptotic expansion in $N$ is of order $N^{-d}$. Therefore, diagrams with $d\sim N$ boxes are exponentially suppressed as $e^{-N \log N}$. The perturbation theory of the chiral and non-chiral Yang-Mills theory therefore coincide.

In summary, the perturbative string theory we introduce in this paper is dual to the full Yang-Mills theory on Riemann surfaces of genus $G>1$, and to a chiral half of the Yang-Mills theory for $G\leq 1$.

We only provided a perturbative definition of the chiral Yang-Mills theory in its large $N$ limit.[^2] Accordingly, our method to derive a string dual is to look for a string theory whose correlators match this asymptotic expansion. To that effect, we attempt in the next section to interpret the right-hand side of equation [\[ExactCorrelators\]](#ExactCorrelators){reference-type="eqref" reference="ExactCorrelators"} as Hurwitz numbers. This requires lifting the constraint on the number of rows in the Young diagram $$\sum_{\lambda\in Y^d_N} \rightarrow \sum_{\lambda\in Y^d}\, ,$$ which is synonymous with adding infinitely many exponentially suppressed terms. Many of the added diagrams are ill-defined, because the value of the exponential distance operator $\Omega^{-1}_{1/N}(\lambda)$ diverges on Young diagrams $\lambda$ with more than $N$ rows.[^3]

This divergence must be regularized. This may be done by shifting the parameter $u=1/N$ of the exponential distance operator by $\epsilon$, discarding the exponentially suppressed terms in the large $N$ limit, then taking $\epsilon$ to $0$. We implicitly adopt this prescription throughout the remainder of the paper.

Finally, if either the area or the coupling vanishes, it is no longer true that certain representations of the unitary group are exponentially suppressed.[^4]

Therefore, in the topological limit, the chiral theory and the full theory coincide. As a result, the topological limit of the string theory we introduce in this paper is dual to the full topological Yang-Mills theory in two dimensions.

[^1]: The nature of the instantonic correction is interesting. It is both similar to a world-sheet instanton correction with exponent proportional to the area, but also to a non-perturbative correction in the string coupling because the wrapping number is of order $N=1/g_s$. Using also the identification [\[StringTension\]](#StringTension){reference-type="eqref" reference="StringTension"}, the correction can be interpreted as due to a D-brane instanton.

[^2]: A non-perturbative definition of the chiral theory can perhaps be achieved by restricting the sum over degrees $d$ in equation [\[NotYetChiral\]](#NotYetChiral){reference-type="eqref" reference="NotYetChiral"} to degrees bounded above by $d\leq N$.

[^3]: The only observables which are not affected by this divergence are the partition functions on the sphere and the torus, as well as the one and two point functions on the sphere.

[^4]: Nevertheless, our prescription to regularize the asymptotic expansion holds, at least on Riemann surfaces of genus $G>1$, because diagrams with $N$ boxes or more are exponentially suppressed by factors $N^{-N}$, as explained above.
