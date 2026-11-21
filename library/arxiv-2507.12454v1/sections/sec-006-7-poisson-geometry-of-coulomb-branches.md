---
doc_id: arxiv-2507.12454v1
doc_title: "Cohomology rings of character varieties"
section_id: sec-006-7-poisson-geometry-of-coulomb-branches
section_title: "Poisson geometry of Coulomb branches"
section_number: 7
pages: 20-21
source_pdf: 2507.12454v1.pdf
source_sha256: 156fd9080847b4e7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.94
doc_brief: "Cohomology rings of character varieties — In this talk I give an introduction and present some recent progress towards understanding the cohomology rings of character varieties of Riemann surfaces"
---
We would like to conclude by explaining a curious formalism which hints at how Conjectures [\[conj:iso vector spaces\]](#conj:iso vector spaces){reference-type="ref" reference="conj:iso vector spaces"}--[\[conj:iso rings\]](#conj:iso rings){reference-type="ref" reference="conj:iso rings"} can be extended to surfaces of higher genus. First, observe that, in view of [\[eq:geometric engineering\]](#eq:geometric engineering){reference-type="eqref" reference="eq:geometric engineering"}, we should consider the bundle of multiforms, i.e. the $g$-fold tensor product of the bundle of differential forms on the Hilbert scheme. How does the Lie algebra $\mathscr{H}_2 \otimes H^*(C)$ act? Quite naturally, in fact. Take a function $f\in R_{x,y}^+$, for instance $f=\sum_{i=1}^n x_i^s y_i^r$. Symplectic geometry associates to $f$ the Hamiltonian vector field $H_f$. Let $$\psi_f(\mathrm{pt}) := \text{multiplication by $f$},$$ $$\psi_f(1) := \text{Lie derivative along $H_f$}.$$ This is what we had in genus $0$. But with multiforms, additional operations arise. For $i=1,\ldots,g$ set $$\psi_f(\sigma_i) = (d f)^{(i)}.$$ This is the operation of multiplication by $df$ acting on the $i$-th component in the $g$-fold tensor product. Set $$\psi_f(\sigma_{i+g}) = \iota^{(i)}_{H_f},$$ the operation of insertion of $H_f$ into the $i$-th component. From $$\psi_{fg}(1) = \mathrm{Lie}_{f H_g + g H_f}, \qquad
    \mathrm{Lie}_{f H_g} = f \mathrm{Lie}_{H_g} + \sum_{i=1}^g (d f)^{(i)} \iota^{(i)}_{H_g}$$ we obtain the following identity: $$\psi_{fg}(1) = \psi_f(1) \psi_g(\mathrm{pt}) + \psi_f(\mathrm{pt}) \psi_g(1) + \sum_{i=1}^{2g} \psi_f(\sigma_i) \psi_g(\sigma_i^*).$$ This formula precisely matches the Künneth decomposition of the diagonal class in $H^2(C\times C)$, which confirms the consistency of the formalism. Okounkov observed that our formalism essentially coincides with the Clifford algebras considered in [@kazhdan2024l].
