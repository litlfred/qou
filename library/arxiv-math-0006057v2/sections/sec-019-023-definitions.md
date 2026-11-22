---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-019-023-definitions
section_title: "Definitions"
section_number: 0.23
pages: 27-28
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.931
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
::: definition
[]{#semisimple and C* label="semisimple and C*"} A quantum groupoid is said to be *semisimple* (resp., *$*$- or $C^*$-quantum groupoid*) if its algebra $H$ is semisimple (resp., a $*$-algebra over a field $k$ with involution, or finite-dimensional $C^*$-algebra over the field $\mathbb{C}$ and $\Delta$ is a $*$-homomorphism).
:::

Groupoid algebras and their duals give examples of commutative and cocommutative semisimple quantum groupoids (Corollary [\[kG is semisimple\]](#kG is semisimple){reference-type="ref" reference="kG is semisimple"}), which are $C^*$-quantum groupoids if the ground field is $\mathbb{C}$ (in which case $g^*=g^{-1}$ for all $g\in G$).

We will describe the class of quantum groupoids possessing *Haar integrals*, i.e., normalized two-sided integrals (note that if such an integral exists then it is unique and is an $S$-invariant idempotent).

::: definition
([@W], 1.2.1). []{#W-index label="W-index"} Given an inclusion of unital $k$-algebras $N\subset M$, a *conditional expectation* $E:M\to N$ is an $N-N$ bimodule map $E$ such that $E(1)=1$. A *quasi-basis* for $E$ is an element $\sum_i x_i\otimes y_i\in M\otimes_k M$ such that $$\sum_i E(mx_i)y_i=m=\sum_i x_iE(y_i m), \qquad \mbox{ for all } m\in M.$$

One can check that $\mbox{Index}\,E=\sum_i x_i y_i\in Z(M)$ does not depend on a choice of a quasi-basis; this element is called the *index* of $E$.

One can apply this definition to a non-degenerate functional $f$ on $H$. If $(l,\lambda)$ is a dual pair of left integrals, then $l_{(2)}\otimes S^{-1}(l_{(1)})$ is a quasi-basis for $\lambda$ and $$\mbox{Index}\,\lambda=S^{-1}\cdot\varepsilon_t(l)\in H_s\cap Z(H).$$ So a non-degenerate left integral is normalized iff its dual has index $1$.
:::
