---
doc_id: arxiv-math-0006051v1
doc_title: "Finite and p-adic polylogarithms"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 0006051v1.pdf
source_sha256: 10483e75bd3655ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.973
doc_brief: "Finite and p-adic polylogarithms — 4 sections: Front matter; Introduction; The proof"
---
[]{#sec:intro label="sec:intro"} The finite logarithm was introduced by Kontsevich (under the name "The $1\frac{1}{2}$ logarithm") in [@Kon99]. The finite logarithm is the case $n=1$ of the $n$-th polylogarithm $\operatorname{li}_n\in \mathbb{Z}/p[z]$ defined by $\operatorname{li}_n(z)= \sum_{k=1}^{p-1} z^k/k^n$. In loc. cit. Kontsevich proved that the finite logarithm satisfies a 4-term functional equation, known as the fundamental equation of information theory. The same functional equation is satisfied by the so called infinitesimal dilogarithm $-(x\log|x|+(1-x)\log|1-x|)$. Cathelineau [@Cat96] defined general infinitesimal polylogarithms and found that they satisfy interesting functional equations. It was the idea of Elbaz-Vincent and Gangl [@Elb-Gan99] that these functional equations should be satisfied by finite polylogarithms (The name "finite polylogarithm" is due to them). Inspired by their work, Kontsevich raised the idea that the finite polylogarithm could be a reduction of an infinitesimal version of the $p$-adic polylogarithm, as defined by Coleman [@Col82]. If such a connection is established, it makes sense to hope that functional equations of the infinitesimal $p$-adic polylogarithm can be established in a similar way to its complex counterpart and that these then imply by reduction the functional equations of the finite polylogs. A conjectural formula for the precise $p$-adic polylog whose "derivative", in the sense to be explained below, reduces to the finite polylog was formulated by Kontsevich and proved by him for small $n$. The purpose of this short note is to prove such a connection between $p$-adic polylogarithms and finite polylogarithms.

To state the main result we recall that Coleman defined $p$-adic polylogarithms, $\operatorname{Li}_n:\mathbb{C}_p \to \mathbb{C}_p$. These functions are locally analytic in the sense that they are given by a convergent power series on each residue disc in $\mathbb{C}_p$. We define the differential operator $D$ by $D=z(1-z) d/dz$. Let $\bar{\mathbb{F}}_p$ be the algebraic closure of the finite field with $p$ elements and let $W=W(\bar{\mathbb{F}}_p)$ be the ring of Witt vectors of $\bar{\mathbb{F}}_p$, so $W$ is the ring of integers of the maximal unramified extension of $\mathbb{Q}_p$. Let $\sigma:\bar{\mathbb{F}}_p \to \bar{\mathbb{F}}_p$ be the automorphism which is the inverse of the $p$-power map. Let $X=\{z\in W:\quad
|z|=|z-1|=1\}$. Our main result is then:

::: theorem
[]{#thetheorem label="thetheorem"} For every $n>1$ let $$F_n(z) = \sum_{k=0}^{n-1} a_k \log^k(z) \operatorname{Li}_{n-k}(z)\;,$$ with $a_0=-n$ and $$a_k= \frac{(-1)^{k}}{(k-1)!} +\frac{(-1)^{k+1}n}{k!}\;,$$ for $k>0$. Then the following holds for every $p>n+1$: One has $DF_n(X) \subset p^{n-1} W$ and for every $z\in X$ one has $p^{1-n} DF_n(z) \equiv \operatorname{li}_{n-1}(\sigma(z)) \pmod{p}$. Furthermore, the choice of the coefficients $a_k$ is the unique choice of coefficients in $\mathbb{Q}$ for which the theorem holds for all $p>n+1$.
:::

We remark that for a given $p$ there will be many other choices of coefficients, for example those which are sufficiently congruent to the $a_k$.

The author would like to thank Kontsevich for explaining the conjecture to him and to Gangl for various comments and corrections. He would also like to thank Nekovář who first suggested to him the idea of a connection between finite and $p$-adic polylogarithms.
