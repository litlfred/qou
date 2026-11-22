---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-034-61-some-general-properties
section_title: "Some general properties"
section_number: 6.1
pages: 21-21
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.967
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — We show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼ = νA1[d]."
---
[]{#xxsec6.1 label="xxsec6.1"}

To apply the results of Sections [\[xxsec3\]](#xxsec3){reference-type="ref" reference="xxsec3"} and [\[xxsec5\]](#xxsec5){reference-type="ref" reference="xxsec5"} to a particular Hopf algebra $A$, we need to check that

\(1\) $A$ is AS-regular, and

\(2\) the antipode $S$ of $A$ is bijective.

In all examples in this section the antipode $S$ is bijective, thanks either to known descriptions of the antipode, or to Skryabin's result Proposition [\[xxsec1.1\]](#xxsec1.1){reference-type="ref" reference="xxsec1.1"}, so (2) will present no difficulties. All the examples considered here are Auslander-Gorenstein, and other than the group rings of ([\[xxsec6.7\]](#xxsec6.7){reference-type="ref" reference="xxsec6.7"}), all the examples are Cohen-Macaulay. (See for example [@BG1] for the definitions of these concepts.) So AS-regularity follows from the next lemma.

::: lemma
Let $A$ be a noetherian Hopf algebra. If $A$ is Auslander-Gorenstein (respectively, Auslander regular) and Cohen-Macaulay, then it is AS-Gorenstein (respectively, AS-regular).
:::

::: proof
*Proof.* Let $d$ be the injective dimension of $A$. Since $\mathop{\mathrm{GKdim}}k=0$, the Cohen-Macaulay condition forces $\mathop{\mathrm{Ext}}^i_A(k,A)=0$ for all $i\neq
d,$ and then $\mathop{\mathrm{Ext}}^d_A(k,A)\neq 0$ by [@ASZ1 Theorem 2.3(2)]. Now the Auslander condition and the Cohen-Macaulay conditions applied to this latter module show that $\mathop{\mathrm{Ext}}^d_A(k,A)$ has GK-dimension zero; that is, it is finite dimensional over $k$. The lemma now follows from Lemma [\[xxsec3.2\]](#xxsec3.2){reference-type="ref" reference="xxsec3.2"}. ◻
:::

Let $\nu$ be the Nakayama automorphism of $A$. By ([\[xxsec3.1\]](#xxsec3.1){reference-type="ref" reference="xxsec3.1"}.1), to connect twisted Hochschild homologies $HH^{\nu}_i(A)$ with $H_i (A,{^{\nu} A})$, one has to check that

\(3\) $\nu$ is diagonalisable.

In general, this condition will fail - see, for instance, Proposition [\[xxsec6.3\]](#xxsec6.3){reference-type="ref" reference="xxsec6.3"}(d). We will review the situation for each class of algebras in turn.

Finally, even when $\nu$ is not the identity, we sometimes nevertheless find that

\(4\) $\mathop{\mathrm{Hdim}}A=\mathop{\mathrm{Hcdim}}A=\mathop{\mathrm{gldim}}A$.

We will discuss when this is true.
