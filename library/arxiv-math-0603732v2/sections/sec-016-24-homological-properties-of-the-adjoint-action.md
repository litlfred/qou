---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-016-24-homological-properties-of-the-adjoint-action
section_title: "Homological properties of the adjoint action"
section_number: 2.4
pages: 8-8
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.946
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — We show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼ = νA1[d]."
---
[]{#xxsec2.4 label="xxsec2.4"}

For us, the usefulness of $L$ rests in its role linking homological algebra over $A$ with that over $A^e$, thus permitting the calculation of Hochschild cohomology. The key lemma is the following result of Ginzburg and Kumar [@GK Proposition p.197]:

::: lemma
[@GK] Let $A$ be a Hopf algebra and let $M$ be an $A$-bimodule.

1.  $\mathop{\mathrm{Hom}}_{A^e}(A,M)=\mathop{\mathrm{Hom}}_A(k,L(M))=Z(M)$.

2.  If $S$ is bijective, $\mathop{\mathrm{Ext}}^i_{A^e}(A,M)=\mathop{\mathrm{Ext}}^i_A(k,L(M))$ for all $i$.
:::

::: proof
*Proof.* (a) This was proved in [@GK Proposition p.197]. We offer a proof following the line of the proof of [@Mo Lemma 5.7.2(1)]. By definition, $$\mathop{\mathrm{Hom}}_{A^e}(A,M)\; =\; \{m\in M\;|\; am=ma, \forall \; a\in A\}
\; =\;  Z(M)$$ and $$\mathop{\mathrm{Hom}}_{A}(k,L(M))\; =\; \{m\in M\;|\; \sum a_1 mS(a_2)=\epsilon
(a)m, \forall \; a\in A\}.$$ If $\sum a_1 mS(a_2)=\epsilon(a) m$ for all $a\in A$, then $$am\;=\; \sum a_1 m \epsilon(a_2)\;=\; \sum a_1m S(a_2) a_3
\;=\; \sum \epsilon(a_1) ma_2\;=\; ma.$$ Conversely, if $am=ma$ for all $a\in A$, then $$\sum a_1 mS(a_2)\;=\; \sum a_1S(a_2) m\;=\; \epsilon(a)m.$$ Thus (a) follows.

\(b\) Let $I$ be an injective $A^e$-resolution of $M$. Since $L$ is exact and preserves injective modules by Lemma [\[xxsec2.2\]](#xxsec2.2){reference-type="ref" reference="xxsec2.2"}(d), $L(I)$ is an injective resolution of $L(M)$. Therefore (b) follows from (a) by replacing $M$ by its injective resolution. ◻
:::

::: remark
In [@GK] part (b) was stated for any Hopf algebra. But it seems to us that the bijectivity of $S$ is needed. This should also be compared to Proposition [\[xxsec3.3\]](#xxsec3.3){reference-type="ref" reference="xxsec3.3"} in which case the bijectivity is not needed.
:::
