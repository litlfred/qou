---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-021-33-the-link-with-integrals
section_title: "The link with integrals"
section_number: 3.3
pages: 11-12
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.946
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — We show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼ = νA1[d]."
---
[]{#xxsec3.3 label="xxsec3.3"}

We need two fundamental observations. The first is due to Feng and Tsygan [@FT Corollary (2.5)] (see also [@HK1 Proposition 2.3]):

::: proposition
[@FT] Let $A$ be a Hopf algebra and let $M$ be an $A$-bimodule. Then, for all $i\geq 0$, there are vector space isomorphisms $$H_i(A,M)\cong \mathop{\mathrm{Tor}}_i^{A^e}(A,M)\cong \mathop{\mathrm{Tor}}^A_i(M',k).$$ Consequently, $\mathop{\mathrm{tHdim}}A\leq \mathop{\mathrm{gldim}}A$.
:::

::: proof
*Proof.* By [@We Lemma 9.1.3], $H_i(A,M)\cong \mathop{\mathrm{Tor}}_i^{A^e}(A,M)$. To see the second isomorphism we use the fact that $A\otimes_{A^e}
M\cong M'\otimes_{A}k$ and that the functor $(-)':A^e$-$\mathop{\mathrm{{\sf Mod}}}\to
A^{\sf op}$-$\mathop{\mathrm{{\sf Mod}}}$ preserves projectives and is exact. Finally, $\mathop{\mathrm{tHdim}}A\leq \mathop{\mathrm{gldim}}A$ follows from the isomorphisms. ◻
:::

The second observation is a version of Poincaré duality for AS-regular Hopf algebras, which, as we shall note in Section 6, is sufficient to retrieve some classical results:

::: lemma
Let $A$ be an augmented AS-regular algebra of global dimension $d$. Then for any right $A$-module $N$, $$\mathop{\mathrm{Tor}}_{d-i}^A(N,k)\quad \cong \quad \mathop{\mathrm{Ext}}^{i}_{A^{\sf op}}(\textstyle \int^l,N)$$ for all $i$.
:::

::: proof
*Proof.* The isomorphism follows from Ischebeck's spectral sequence (3.2.1), taking $M=k$, together with the Artin-Schelter condition (AS2). ◻
:::

Noting (3.2.1), and combining the above proposition and lemma, we immediately deduce the following partial Poincaré duality for the Hochschild homology of AS-regular Hopf algebras.

::: corollary
Let $A$ be an AS-regular Hopf algebra of global dimension $d$. Let $M$ be an $A$-bimodule. Then, for every integer $i$, $$H_{d-i}(A,M) \; \cong \; \mathop{\mathrm{Ext}}^i_{A^{\sf op}}
(\textstyle \int^l,(M)').$$ As a consequence, if $\sigma$ is an algebra automorphism of $A$, then, for every $i$, $$H_{d-i}(A,{^\sigma A}) \; \cong \;
\mathop{\mathrm{Ext}}^i_{A^{\sf op}} (\textstyle \int^l,( ^{\sigma}A)').$$
:::

::: remark
When $S$ is bijective, this corollary can be deduced from Van den Bergh's general Poincaré duality result Proposition [\[xxsec5.1\]](#xxsec5.1){reference-type="ref" reference="xxsec5.1"} -- see Corollary [\[xxsec5.2\]](#xxsec5.2){reference-type="ref" reference="xxsec5.2"}. However it is unknown at present whether $S$ is bijective in general, so it seems worth recording this corollary.
:::
