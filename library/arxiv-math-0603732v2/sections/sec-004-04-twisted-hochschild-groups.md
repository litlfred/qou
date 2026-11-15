---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-004-04-twisted-hochschild-groups
section_title: "Twisted Hochschild groups"
section_number: 0.4
pages: 2-3
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.987
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — We show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼ = νA1[d]."
---
[]{#xxsec0.4 label="xxsec0.4"} Hochschild (co)homology with coefficients in a twisted bimodule arises naturally when one studies the twisted (co)homology introduced by Kustermans, Murphy and Tuset [@KMT]. Thus, let $B$ be an algebra of finite global homological dimension, let $\sigma$ be an algebra automorphism of $B$ and let $HH^\sigma_i(B)$ be the $i$th $\sigma$-twisted Hochschild homology of $B$ (see [@KMT] or [@HK1] for details). By [@HK1 Proposition 2.1], when $\sigma$ is diagonalisable, one has $$HH^\sigma_i(B)\; \cong \; H_i(B,{^\sigma B}),$$ where the right hand side denotes Hochschild homology with coefficients in $^\sigma B^1$. We define the *twisted Hochschild dimension* of $B$ to be $$\mathop{\mathrm{tHdim}}B\; =\; \max\{i\;|\; H_{i}(B,{^\sigma B})\neq 0
\quad \text{for some automorphism $\sigma$ of $B$}\}.$$ Similarly twisted Hochschild codimension, denoted by $\mathop{\mathrm{tHcdim}}$, is defined by using twisted Hochschild cohomology; the definition is in ([\[xxsec5.1\]](#xxsec5.1){reference-type="ref" reference="xxsec5.1"}). The phenomenon described in ([\[xxsec0.1\]](#xxsec0.1){reference-type="ref" reference="xxsec0.1"}) is a special case of the following theorem, a central result of this paper.

::: theorem
Let $A$ be a noetherian AS-Gorenstein Hopf algebra of finite global dimension $d$, with bijective antipode, and let $\nu$ be its Nakayama automorphism.

Then

1.  $H_d(A,A^\nu ) \cong Z(A) \neq 0$. As a consequence $\mathop{\mathrm{tHdim}}A=d$.

2.  $H^d(A,{^\nu A}) \cong A/[A,A] \neq 0$. As a consequence $\mathop{\mathrm{tHcdim}}A=d$.
:::

In fact, there is a Poincaré duality connecting the homology and cohomology of the algebras $A$ of the above theorem. This is a consequence of a result of Van den Bergh [@VdB1], which applies in the present context because of Theorem [\[xxsec0.2\]](#xxsec0.2){reference-type="ref" reference="xxsec0.2"}. The following result is obtained as Corollary [\[xxsec5.2\]](#xxsec5.2){reference-type="ref" reference="xxsec5.2"}.

::: corollary
Let $A$ be as in Theorem [\[xxsec0.4\]](#xxsec0.4){reference-type="ref" reference="xxsec0.4"}. For every $A$-bimodule $M$ and for all $i$, $$H^i(A,M)=H_{d-i}(A,{^{\nu}M}).$$
:::
