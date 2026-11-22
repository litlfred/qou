---
doc_id: arxiv-0812.2426v1
doc_title: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS"
section_id: sec-006-15-coends
section_title: "Coends"
section_number: 1.5
pages: 4-4
source_pdf: 0812.2426v1.pdf
source_sha256: df1eb953bc2c6c63
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 1.0
doc_brief: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS — A theorem of M¨uger asserts that the center Z(C) of a spherical k-linear category C is a modular category if k is an algebraically closed ﬁeld"
---
[]{#sect-coend label="sect-coend"} Let $\mathcal{C}$, $\mathcal{D}$ be categories and $F\colon\mathcal{C}^\mathrm{op}\times \mathcal{C}\to \mathcal{D}$ be a functor.

A *dinatural transformation* from the functor $F$ to an object $D$ of $\mathcal{D}$ is family $d=\{d_X \colon F(X,X) \to D\}_{X \in
\mathrm{Ob}(\mathcal{C})}$ of morphisms in $\mathcal{D}$ satisfying the dinaturality condition: $$d_X F(f, \mathrm{id}_X)=d_Y F(\mathrm{id}_Y,f)$$ for every morphism $f\colon X \to Y$ in $\mathcal{C}$.

A *coend* of $F$ consists of an object $C$ of $\mathcal{D}$ and a dinatural transformation $i$ from $F$ to $C$ which is *universal*, that is, for every dinatural transformation $d$ from $F$ to an object $D$ of $\mathcal{D}$, there exists a unique morphism $\phi\colon C \to D$ such that $d_X=\phi \circ i_X$.

If $F$ admits a coend $(C,i)$, then it is unique (up to unique isomorphism) and one denotes $C=\int^{X\in \mathcal{C}} F(X,X)$. See [@ML1] for details.
