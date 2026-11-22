---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-034-93-computational-consequences-of-the-birkhoff-gu
section_title: "Computational consequences of the Birkhoff-Guenther normal form"
section_number: 9.3
pages: 47-48
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.893
latex_coverage_ratio: 0.875
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:computnormalform label="subsection:computnormalform"}

Let $A_{0}$ be as in [\[eqn:formestandarddiagonaleentiere\]](#eqn:formestandarddiagonaleentiere){reference-type="eqref" reference="eqn:formestandarddiagonaleentiere"} and $A_{U} = A$ as in [\[eqn:formestandardtriangulaireentiere\]](#eqn:formestandardtriangulaireentiere){reference-type="eqref" reference="eqn:formestandardtriangulaireentiere"}. Looking for $\hat{F} \in {\mathfrak{G}}({{\mathbf C}((z))})$ such that $\hat{F}[A_{0}] = A$ amounts, with notation [\[eqn:isoplat\]](#eqn:isoplat){reference-type="eqref" reference="eqn:isoplat"}, to solving the system: $$\forall (i,j), 1 \leq i < j \leq k ~,~
(\sigma_qF_{i,j}) (z^{\mu_{j}} A_{j}) =
(z^{\mu_{i}} A_{i}) F_{i,j} + \sum_{\ell = i+1}^{j-1} U_{i,\ell} F_{\ell,j} + U_{i,j}.$$ This is triangular in the sense that the equation in $F_{i,j}$ depends on previously found $F_{\ell,j}$ with $\ell > i$.\
Assume that $A$ is in Birkhoff-Guenther normal form (definition [\[defi:BirkhoffGuenthernormalform\]](#defi:BirkhoffGuenthernormalform){reference-type="ref" reference="defi:BirkhoffGuenthernormalform"}). Then we can write $U_{i,j} = z^{\mu_{i}} U'_{i,j}$, where $U'_{i,j}$ has coefficients in ${\mathbf C}[z]$. The previous equation becomes: $$(\sigma_qF_{i,j}) (z^{\mu_{j} - \mu_{i}} A_{j}) =
A_{i} F_{i,j} + \sum_{\ell = i+1}^{j-1} U'_{i,\ell} F_{\ell,j} + U'_{i,j}.$$ Assume by induction that all $F_{\ell,j}$ have coefficients in ${{\mathbf C}[[z]]}$. Then one may write the above equation as: $$F_{i,j} = U'' + z^{\delta} A_{i}^{-1} (\sigma_qF_{i,j}) A_{j},$$ where $U''$ has coefficients in ${{\mathbf C}[[z]]}$ and $\delta \in {\mathbf N}^{*}$. This is a fixpoint equation for an operator that is contracting in the $z$-adic topology of ${{\mathbf C}[[z]]}$ and so it admits a unique formal solution. Therefore we find a unique $\hat{F} \in {\mathfrak{G}}({{\mathbf C}[[z]]})$ such that $\hat{F}[A_{0}] = A$.\
A noteworthy consequence is that the inclusions ${{\mathbf C}\{z\}}\subset {{\mathbf C}(\{z\})}$ and ${{\mathbf C}[[z]]}\subset {{\mathbf C}((z))}$ induce a natural identification: $${\mathfrak{G}}^{A_{0}}({{\mathbf C}[[z]]})/{\mathfrak{G}}({{\mathbf C}\{z\}}) \simeq {\mathfrak{G}}^{A_{0}}({{\mathbf C}((z))})/{\mathfrak{G}}({{\mathbf C}(\{z\})}),$$ and, as a corollary, a bijection: $${\mathfrak{G}}^{A_{0}}({{\mathbf C}[[z]]})/{\mathfrak{G}}({{\mathbf C}\{z\}}) \rightarrow {\mathcal{F}}(P_{1},\ldots,P_{k}).$$
