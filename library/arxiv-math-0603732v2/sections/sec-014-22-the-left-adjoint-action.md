---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-014-22-the-left-adjoint-action
section_title: "The left adjoint action"
section_number: 2.2
pages: 6-6
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.906
latex_coverage_ratio: 0.935
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — We show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼ = νA1[d]."
---
[]{#xxsec2.2 label="xxsec2.2"}

The algebra homomorphism $\operatorname{id}_A\otimes S: A\otimes
A\to A\otimes A^{\sf op}=A^e$ induces a functor $$F_{\operatorname{id}_A\otimes S}\; : \; A^e - \mathop{\mathrm{{\sf Mod}}}\; \to \;
(A\otimes A) - \mathop{\mathrm{{\sf Mod}}}.$$ If $S$ is bijective, then $F_{\operatorname{id}_A\otimes S}$ is an invertible functor. The *left adjoint functor* $L$ [@Mo Definition 3.4.1(1)] is defined to be $$L = \mathrm{Res}_A\circ F_{\operatorname{id}_A\otimes S}\; :\;
A^e-\mathop{\mathrm{{\sf Mod}}}\; \to \; A-\mathop{\mathrm{{\sf Mod}}}.$$ Let $M$ be an $A$-bimodule. Then $L(M)$ is a left $A$-module defined by the action $$a\cdot m\; = \; \sum a_1 m S(a_2).$$ In a similar way to Lemma [\[xxsec2.1\]](#xxsec2.1){reference-type="ref" reference="xxsec2.1"}, one can prove:

::: lemma
Let $A$ be a Hopf algebra and $L$ be the left adjoint functor defined above.

1.  $L$ is an exact functor.

2.  $L$ preserves projectives.

3.  $L(A^e)$ is a free $A$-module.

4.  If $S$ is bijective, then $L$ preserves injectives.
:::

::: remark
If $S$ is not bijective, it is unclear to us whether $L$ preserves injectives. That's why we need bijectivity of $S$ for Lemma [\[xxsec2.4\]](#xxsec2.4){reference-type="ref" reference="xxsec2.4"}(d).
:::
