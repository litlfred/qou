---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-059-114-end-of-the-proof-of-the-theorem-76
section_title: "End of the proof of the theorem 7.6"
section_number: 11.4
pages: 66-66
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.983
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
::: corollary
[]{#cor: cubic label="cor: cubic"} There is a homotopy realizing relation: $$\bcalC^{(1)}_+\bar{\star}\bcalC^{(2)}_+\bar{\star}\bcalC^{(1)}_+\sim\bcalC_+^{(2)}\bar{\star}\bcalC_+^{(1)}\bar{\star}\bcalC^{(2)}.$$
:::

::: proof
*Proof.* From the previous discussion we see that the complexes $C_{121}$ and $\mathrm{D}(C_{121})$ are minimal resolutions of the modules $R/I_{121}$ and $R/I_{212}$. The ideals $I_{212}$ and $I_{121}$ are isomorphic hence there are morphism $\psi,\theta: R^4\rightarrow R^4$ such that $\Psi_{<2}=(1,\psi_1)$ and $\Theta_{<2}=(1,\theta_1)$ are morphisms between the truncated complexes $[C_{121}]_{<2}=[R\xleftarrow{d} R^4]$, $[\mathrm{D}(C_{121})]_{<2}=[R\xleftarrow{\mathrm{D}(d)} R^4]$ and $\Psi_{<2}\circ \Theta_{<2}=1$, $\Theta_{<2}\circ \Psi_{<2}=1$. The morphisms could be extended to some morphism $\Psi_{<k},\Theta_{<k}$ of $[C_{121}]_{<k}$ and $[C_{212}]_{<k}$. Moreover, any such extensions satisfy $\Psi_{<k}\circ \Theta_{<k}\sim 1$, $\Theta_{<k}\circ \Psi_{<k}\sim 1$. Let us explain an inductive construction for the first homotopy.

Suppose constructed $\Psi_{<k+1}=\Psi_{<k}+\psi_k$, $\Theta_{<k+1}=\Theta_{<k}+\theta_k$ and homotopy $\chi_{<k}$ such that $\Psi_{<k}\circ \Theta_{<k}-1=D\circ \chi_{<k}-
\chi_{<k}\circ D$. Then $D\circ \Psi_{<k+1}\circ\Theta_{<k+1}-D=-D\circ\chi_{<k}\circ D+D\circ \psi_k\circ \theta_k$ hence $D\circ\psi_k\circ \theta_k=D$ as map $[C_{121}]_k\to [C_{212}]_{k+1}$. Thus there is $\chi_k$ such that $D\circ\chi_k=\psi_k\circ\theta_k$ and we can set $\chi_{<k+1}=\chi_{<k}+\chi_k$.

Thus we have a homotopy equivalence $C_{121}\sim C_{212}$. The matrix factorizations $\bcalC_+^{(1)}\bar{\star}\bcalC_+^{(2)}\bar{\star}\bcalC^{(1)}_+$ and $\bcalC_+^{(2)}\bar{\star}\bcalC_+^{(1)}\bar{\star}\bcalC^{(2)}_+$ are lifts of the complexes $C_{121}$ and $C_{212}$. Since the complexes $C_{121},C_{212}$ satisfy the conditions of the lemma [\[lem: ext mor\]](#lem: ext mor){reference-type="ref" reference="lem: ext mor"} we lift the homotopy between $C_{121}$ and $C_{212}$ to the homotopy in the statement of corollary. ◻
:::

The main conclusion of the computations in the last two section is a construction of the braid group action on the category of matrix factorizations:

::: corollary
The assignment $$\sigma_i\mapsto \bcalC^{(i)}_+\bar{\star},\quad \sigma_{i}^{-1}\mapsto \bcalC^{(i)}_-\bar{\star}$$ extends to the homomorphism $\Brgr_n\to End(\MF_{B^2}(\calXr_2,\Wr)).$
:::
