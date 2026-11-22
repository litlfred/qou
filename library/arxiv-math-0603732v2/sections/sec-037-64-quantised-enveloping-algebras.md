---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-037-64-quantised-enveloping-algebras
section_title: "Quantised enveloping algebras"
section_number: 6.4
pages: 23-24
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.958
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — We show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼ = νA1[d]."
---
[]{#xxsec6.4 label="xxsec6.4"}

For the definition of the quantised enveloping algebra $U_q(\mathfrak{g})$ of the semisimple Lie algebra $\mathfrak{g}$, see for example [@BG2 I.6.3] or [@Ja 4.3]. The results in this case are already known; the details are as follows.

::: proposition
Let $\ell$ be an odd positive integer greater than 2. Let $q$ denote either a primitive $\ell$th root of one in $\mathbb{C}$, or an indeterminate over $\mathbb{C}$; let $k$ be $\mathbb{C}$ in the first case, or $\mathbb{C}(q)$ in the second case. Let $\mathfrak{g}$ be a semisimple complex Lie algebra of dimension $d$, and let $A$ be the corresponding quantised enveloping algebra $U_q(\mathfrak g)$. (If $\mathfrak{g}$ has a summand of type $G_2$ assume that 3 does not divide $\ell.$)

1.  $S^2$ is inner.

2.  $A$ is AS-regular of global dimension $d$.

3.  The left integral of $A$ is trivial, i.e., $\int^l_A \; \cong\; k$ as $A$-bimodule. Thus ${\xi}= \nu =
    \operatorname{id}_A$.

4.  $A$ has rigid dualising complex $A[d]$.

5.  $\mathop{\mathrm{Hdim}}A = \mathop{\mathrm{Hcdim}}A = d$ and Poincaré duality holds.
:::

::: proof
*Proof.* (a) See [@KS Proposition 6, p. 164] or [@Ja (4.9)(1)].

(b,c) That $A$ has finite global dimension was proved in [@BG1 Proposition 2.2]. Then AS-regularity follows from [@Ch Proposition], and her result shows also that $\mathop{\mathrm{gldim}}A$ is $d$ for all values of the parameter $q,$ and that $\int_A^l\cong k$. The triviality of $\nu$ now follows from (a) and Proposition [\[xxsec4.5\]](#xxsec4.5){reference-type="ref" reference="xxsec4.5"}.

\(d\) This is the main theorem of [@Ch]. (Of course it follows also from (c) and Proposition [\[xxsec4.5\]](#xxsec4.5){reference-type="ref" reference="xxsec4.5"}(b).)

\(e\) This is immediate from Theorems [\[xxsec3.4\]](#xxsec3.4){reference-type="ref" reference="xxsec3.4"}(c) and [\[xxsec5.3\]](#xxsec5.3){reference-type="ref" reference="xxsec5.3"}(c), and Corollary [\[xxsec5.2\]](#xxsec5.2){reference-type="ref" reference="xxsec5.2"}, and the fact that $\nu=\operatorname{id}_A$. ◻
:::
