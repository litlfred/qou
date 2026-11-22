---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-036-63-enveloping-algebras
section_title: "Enveloping algebras"
section_number: 6.3
pages: 23-23
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 0.972
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — We show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼ = νA1[d]."
---
[]{#xxsec6.3 label="xxsec6.3"}

In this subsection we drop the hypothesis that $k$ is algebraically closed.

::: proposition
Let $\mathfrak{g}$ be a Lie algebra over $k$ of finite dimension $d$, and let $A$ be its universal enveloping algebra $U(\mathfrak{g}).$

1.  $S^2=\operatorname{id}_A$.

2.  $A$ is an AS-regular Hopf algebra with $\mathop{\mathrm{gldim}}A = d.$

3.  [@Ye2] The rigid dualising complex of $A$ is $(A \otimes \bigwedge^d \mathfrak{g})[d].$ Thus the Nakayama automorphism $\nu = {\xi}$ of $A$ is the inverse of the winding automorphism $\Xi[\chi]$, where $\chi$ is the representation of $\mathfrak{g}$ on $\bigwedge^d \mathfrak{g}.$ That is, $$\nu(x) \;= \; x + \mathrm{tr}
    (\mathrm{ad}_{\mathfrak{g}}(x))$$ for $x \in \mathfrak{g}.$

4.  If $\mathrm{tr}(\mathrm{ad}_{\mathfrak{g}}(x))\neq 0$, then $\nu$ is not diagonalisable.

5.  If $\mathfrak{g}$ is semisimple, then $\nu$ is the identity and hence $\mathop{\mathrm{Hdim}}A=\mathop{\mathrm{Hcdim}}A=d$.

6.  $H_d(A,{A^{\nu}})  \cong  Z(A) \neq 0,$ and $H^d(A,{^{\nu}A}) \cong  A/[A,A],$ so that $\mathop{\mathrm{tHcdim}}A = \mathop{\mathrm{tHdim}}A= d.$ The twisted Poincaré duality of Corollary [\[xxsec5.2\]](#xxsec5.2){reference-type="ref" reference="xxsec5.2"} holds for $A$.
:::

::: proof
*Proof.* (a) Recall that the antipode is given by $S(x) = -x$ for $x \in \mathfrak{g}$, so $S^2$ the identity.

\(b\) That the global dimension is $d$ is [@CE Theorem XIII.8.2]. It is well-known that $A$ is Auslander-regular for all $\mathfrak{g}$. The assertion follows from Lemma [\[xxsec6.1\]](#xxsec6.1){reference-type="ref" reference="xxsec6.1"}.

\(c\) The description of rigid dualising complex of $A$ is the main result of [@Ye2].

\(d\) This follows from (c).

\(e\) If $\mathfrak{g}$ is semisimple, then $\mathrm{tr}
(\mathrm{ad}_{\mathfrak{g}}(x))=0$ for all $x\in {\mathfrak{g}}$. By (c), $\nu$ is the identity. The assertion follows from Theorems [\[xxsec3.4\]](#xxsec3.4){reference-type="ref" reference="xxsec3.4"}(c) and [\[xxsec5.3\]](#xxsec5.3){reference-type="ref" reference="xxsec5.3"}(c).

\(f\) This follows from Corollaries [\[xxsec5.1\]](#xxsec5.1){reference-type="ref" reference="xxsec5.1"} and [\[xxsec5.2\]](#xxsec5.2){reference-type="ref" reference="xxsec5.2"}. ◻
:::

::: remark
Twisted Poincaré duality at the level of ordinary Lie algebra homology and cohomology follows for $U(\mathfrak{g})$ from Lemma [\[xxsec3.3\]](#xxsec3.3){reference-type="ref" reference="xxsec3.3"}. This retrieves the classical duality for Lie algebra (co)homology which dates back to the work of Koszul [@Ko] and Hazewinkel [@Ha].
:::
