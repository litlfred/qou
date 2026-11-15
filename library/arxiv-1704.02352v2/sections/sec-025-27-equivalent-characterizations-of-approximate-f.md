---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-025-27-equivalent-characterizations-of-approximate-f
section_title: "Equivalent characterizations of approximate factorization of characters"
section_number: 2.7
pages: 18-20
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.869
latex_coverage_ratio: 0.98
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Young diagrams which can be regarded as a natural one-parameter deformation of some classi- cal"
---
The following result, [\[def:approx-factorization-charactersB\]](#def:approx-factorization-charactersB){reference-type="ref" reference="def:approx-factorization-charactersB"}, is the key tool for the purposes of the current paper. Its main content is part [\[item:afp2\]](#item:afp2){reference-type="ref" reference="item:afp2"}; roughly speaking, it states that each of the four families of numbers [\[eq:AFPPartitions\]](#eq:AFPPartitions){reference-type="eqref" reference="eq:AFPPartitions"}--[\[eq:AFPDisjointCumulants\]](#eq:AFPDisjointCumulants){reference-type="eqref" reference="eq:AFPDisjointCumulants"} can be transformed into the others. Each of these four families describes some convenient aspect of the characters $\chi_n$ in the limit $n\to\infty$. To be more specific:

-   The family [\[eq:AFPCumulants\]](#eq:AFPCumulants){reference-type="eqref" reference="eq:AFPCumulants"} (and its subset, the family [\[eq:AFPCumulants-characters\]](#eq:AFPCumulants-characters){reference-type="eqref" reference="eq:AFPCumulants-characters"}) has a direct probabilistic meaning. It contains information about the cumulants of some random variables which might be handy while proving probabilistic statements such as Central Limit Theorem or Law of Large Numbers.

-   On the other hand, the cumulants appearing in the families [\[eq:AFPPartitions\]](#eq:AFPPartitions){reference-type="eqref" reference="eq:AFPPartitions"} and [\[eq:AFPDisjointCumulants\]](#eq:AFPDisjointCumulants){reference-type="eqref" reference="eq:AFPDisjointCumulants"} are purely algebraic and do *not* have any direct probabilistic meaning. However, their merit lies in the fact that in many concrete applications (such as the ones from [@DolegaSniady-examples-AFP]) it is much simpler to verify algebraic conditions [\[item:AFP-A\]](#item:AFP-A){reference-type="ref" reference="item:AFP-A"} and [\[item:disjoint-cumulants\]](#item:disjoint-cumulants){reference-type="ref" reference="item:disjoint-cumulants"} than their probabilistic counterparts [\[item:cumulants-classic-characters\]](#item:cumulants-classic-characters){reference-type="ref" reference="item:cumulants-classic-characters"} and [\[item:cumulants-classic-polynomial\]](#item:cumulants-classic-polynomial){reference-type="ref" reference="item:cumulants-classic-polynomial"}.

::: theorem
[]{#def:approx-factorization-charactersB label="def:approx-factorization-charactersB"} Assume that $\alpha=\alpha(n)$ is such as in [\[sec:hypothesis-double-scaling\]](#sec:hypothesis-double-scaling){reference-type="ref" reference="sec:hypothesis-double-scaling"}. Assume also that for each integer $n\geq 1$ we are given a reducible Jack character $\chi_n\colon\mathcal{P}_{n}\to\mathbb{R}$.

1.  []{#item:afp2 label="item:afp2"} *Equivalent characterization of approximate factorization property.*

    Then the following four conditions are equivalent:\

    1.  []{#item:AFP-A label="item:AFP-A"} for each integer $\ell \geq 1$ and all integers $l_1,\dots,l_\ell\geq 2$ the limit

        $$\label{eq:AFPPartitions}
                    \lim_{n\to\infty} k^{\chi_n}_\ell (l_1, \dots, l_\ell) \ 
                    n^{\frac{l_1+\cdots+l_\ell+\ell-2}{2}}$$ exists and is finite;

    2.  []{#item:cumulants-classic-characters label="item:cumulants-classic-characters"} for each integer $\ell\geq 1$ and all $x_1,\dots,x_\ell\in\{\mathop{\mathrm{Ch}}_1,\mathop{\mathrm{Ch}}_2,\dots\}$ the limit $$\label{eq:AFPCumulants-characters}
                    \lim_{n\to\infty}    \kappa^{\chi_n}_{\ell}(x_{1},\dots,x_{\ell})\ 
                    n^{- \frac{\deg x_1+ \cdots + \deg x_\ell - 2(\ell-1)}{2}}$$ exists and is finite;

    3.  []{#item:cumulants-classic-polynomial label="item:cumulants-classic-polynomial"} for each integer $\ell\geq 1$ and all $x_1,\dots,x_\ell\in\mathscr{P}$ the limit $$\label{eq:AFPCumulants}
                    \lim_{n\to\infty}    \kappa^{\chi_n}_{\ell}(x_{1},\dots,x_{\ell})\ 
                    n^{- \frac{\deg x_1+ \cdots + \deg x_\ell - 2(\ell-1)}{2}}$$ exists and is finite;

    4.  []{#item:disjoint-cumulants label="item:disjoint-cumulants"} for each integer $\ell\geq 1$ and all $x_1,\dots,x_\ell\in\mathscr{P}_\bullet$ the limit $$\label{eq:AFPDisjointCumulants}
                    \lim_{n\to\infty}    \kappa^{\chi_n}_{\bullet\ell}(x_{1},\dots,x_{\ell})\ 
                    n^{- \frac{\deg x_1+ \cdots + \deg x_\ell - 2(\ell-1)}{2}}$$ exists and is finite.

2.  []{#item:equivalent-enhanced label="item:equivalent-enhanced"}

    Assume that the conditions from part [\[item:afp2\]](#item:afp2){reference-type="ref" reference="item:afp2"} hold true. Furthermore, assume that for $\ell=1$ the rate of the convergence of *any* of the four expressions under the limit symbol in [\[eq:AFPPartitions\]](#eq:AFPPartitions){reference-type="eqref" reference="eq:AFPPartitions"}--[\[eq:AFPDisjointCumulants\]](#eq:AFPDisjointCumulants){reference-type="eqref" reference="eq:AFPDisjointCumulants"} is of the form $$\label{eq:nice-limit}
            \operatorname{const}_1+ \frac{\operatorname{const}_2+o(1)}{\sqrt{n}}$$ in the limit $n \to \infty$ and all choices of $l_1$ (respectively, for all choices of $x_1$); the constants depend on the choice of $l_1$ (respectively, $x_1$).

    Then for $\ell=1$ the rate of convergence of *each* of the four expressions [\[eq:AFPPartitions\]](#eq:AFPPartitions){reference-type="eqref" reference="eq:AFPPartitions"}--[\[eq:AFPDisjointCumulants\]](#eq:AFPDisjointCumulants){reference-type="eqref" reference="eq:AFPDisjointCumulants"} is of the form [\[eq:nice-limit\]](#eq:nice-limit){reference-type="eqref" reference="eq:nice-limit"}.
:::

When $\alpha=1$, part [\[item:afp2\]](#item:afp2){reference-type="ref" reference="item:afp2"} of the above result corresponds to [@Sniady2006c Theorem and Definition 1]. The proof is postponed to [1](#sec:proof-of-key-tool-short){reference-type="ref" reference="sec:proof-of-key-tool-short"}.

# Proof of [\[def:approx-factorization-charactersB\]](#def:approx-factorization-charactersB){reference-type="ref" reference="def:approx-factorization-charactersB"} {#sec:proof-of-key-tool-short}

In the current section we shall prove the key tool, [\[def:approx-factorization-charactersB\]](#def:approx-factorization-charactersB){reference-type="ref" reference="def:approx-factorization-charactersB"}.

Additionally, concerning part [\[item:afp2\]](#item:afp2){reference-type="ref" reference="item:afp2"} of [\[def:approx-factorization-charactersB\]](#def:approx-factorization-charactersB){reference-type="ref" reference="def:approx-factorization-charactersB"} we shall discuss the exact relationship between the limits of the quantities [\[eq:AFPPartitions\]](#eq:AFPPartitions){reference-type="eqref" reference="eq:AFPPartitions"}--[\[eq:AFPDisjointCumulants\]](#eq:AFPDisjointCumulants){reference-type="eqref" reference="eq:AFPDisjointCumulants"} in the case $\ell\in\{1,2\}$. This relationship provides the information about the limit shape of random Young diagrams in [\[theo:lln\]](#theo:lln){reference-type="ref" reference="theo:lln"} as well as about the covariance of the limit Gaussian process describing the fluctuations in [\[theo:clt\]](#theo:clt){reference-type="ref" reference="theo:clt"}.

Concerning part [\[item:equivalent-enhanced\]](#item:equivalent-enhanced){reference-type="ref" reference="item:equivalent-enhanced"} of [\[def:approx-factorization-charactersB\]](#def:approx-factorization-charactersB){reference-type="ref" reference="def:approx-factorization-charactersB"} we shall discuss the exact relationship between the constants which describe the fine asymptotics [\[eq:nice-limit\]](#eq:nice-limit){reference-type="eqref" reference="eq:nice-limit"} of the quantities [\[eq:AFPPartitions\]](#eq:AFPPartitions){reference-type="eqref" reference="eq:AFPPartitions"}--[\[eq:AFPDisjointCumulants\]](#eq:AFPDisjointCumulants){reference-type="eqref" reference="eq:AFPDisjointCumulants"} in the case $\ell=1$. This relationship provides the information about the mean value $\mathbb{E}\Delta_\infty$ of the limit Gaussian process from [\[eq:weak-topology\]](#eq:weak-topology){reference-type="ref" reference="eq:weak-topology"}.
