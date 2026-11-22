---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-030-310-correspondences
section_title: "Correspondences"
section_number: 3.10
pages: 30-30
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.875
latex_coverage_ratio: 0.926
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:nakajima label="sub:nakajima"}

Formula [\[eqn:markov 0\]](#eqn:markov 0){reference-type="eqref" reference="eqn:markov 0"} can be expressed in terms of the complexes of sheaves: $$\mathcal{F}( \sigma ) = \nu_*(\mathcal{B}(\sigma)) \ \in \ D^b(\mathrm{Coh}_{\mathbb{C}^{*} \times \mathbb{C}^*}(\mathrm{Hilb}_n))$$ of [\[eqn:sheaf on hilb\]](#eqn:sheaf on hilb){reference-type="eqref" reference="eqn:sheaf on hilb"}, where $\nu: \mathrm{FHilb}_n^\text{dg}\rightarrow \mathrm{Hilb}_n$ is the map [\[eqn:map to hilb\]](#eqn:map to hilb){reference-type="eqref" reference="eqn:map to hilb"}. Specifically, we have the spaces: $$\includegraphics{sec_3_10.png}$$ where $\mathrm{Hilb}_{n,n+1} = \{I \in \mathrm{Hilb}_n, I' \in \mathrm{Hilb}_{n+1}, I \supset I' \text{ with quotient supported on } \{y=0\} \}$ are the correspondences studied by Nakajima and Grojnowski to describe the cohomology groups of Hilbert schemes. At the categorified level, their construction gives rise to a functor: $$D^b(\mathrm{Coh}_{\mathbb{C}^{*} \times \mathbb{C}^*}(\mathrm{Hilb}_n)) \stackrel{\alpha}\longrightarrow D^b(\mathrm{Coh}_{\mathbb{C}^{*} \times \mathbb{C}^*}(\mathrm{Hilb}_{n+1})), \qquad \alpha = p_{2*}p_1^*$$ To establish [\[eqn:nakajima 1\]](#eqn:nakajima 1){reference-type="eqref" reference="eqn:nakajima 1"}, note that $\mathcal{F}(i(\sigma))$ equals: $$\nu_{n+1 *}(\mathcal{B}(i(\sigma))) = p_{2*}(r_*(\mathcal{B}(i(\sigma)))) = p_{2*}(r_*(q^*(\mathcal{B}(\sigma)))) = p_{2*}(p_1^*(\nu_{n*}(\mathcal{B}(\sigma)))) = \alpha(\mathcal{F}(\sigma))$$ where the second equality follows from [\[eqn:markov 0\]](#eqn:markov 0){reference-type="eqref" reference="eqn:markov 0"}, and the third equality follows from the fact that the rhombus is cartesian. This latter fact may seem obvious at the level of closed points, but scheme-theoretically it only holds because we have replaced the badly behaved scheme $\mathrm{FHilb}_n$ with the nicely behaved dg scheme $\mathrm{FHilb}_n^\text{dg}$.
