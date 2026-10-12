---
doc_id: arxiv-hep-th-0006156v1
doc_title: "arXiv:hep-th/0006156v1 20 Jun 2000"
section_id: sec-001-1-recollecting-the-facts
section_title: "Recollecting the facts"
section_number: 1
pages: 2-3
source_pdf: 0006156v1.pdf
source_sha256: b799d4ef150291cf
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.946
---
In this section we remind in appropriate form some facts about the Liouville model and the technique of its discretization.

## Liouville formula and Möbius-invariance

Liouville formula makes solutions, all of them in fact, from pairs of arbitrary functions of one variable "moving" in light-cone directions $$\label{lf}
   -e^{-2\phi(x,t)}=\frac{\alpha'(x-t)\beta'(x+t)}
   {(\alpha(x-t)-\beta(x+t))^2}  \;  .$$ The right hand side of eqn ([\[lf\]](#lf){reference-type="ref" reference="lf"}) is invariant under simultaneous point-wise Möbius transformations $$\alpha\mapsto\alpha\triangleleft M=\frac{m_{21}+\alpha m_{11}}{m_{22}
  +\alpha m_{12}}\qquad\qquad\beta\mapsto\beta\triangleleft M$$ of the "chiral halves" $\alpha$ and $\beta$. Accordingly, if those are "Möbius-periodic" $$\alpha(x+2\pi)=\alpha(x)\triangleleft T\qquad\qquad
\beta(x+2\pi)=\beta(x)\triangleleft T ,$$ with the same monodromy matrix $T$ in both chiralities of course, the solution comes out periodic in the spatial direction $$\phi(x+2\pi,t)=\phi(x,t)    .$$ From now on, this will be the only boundary condition in use.

Because of this hidden Möbius-symmetry, the chiral halves cannot be uniquely restored from a given solution, but their Schwarz derivatives can, for they are Möbius-invariant as well. In particular, that of $\alpha$ (times minus one half) $$\textstyle u=-\frac12\left(\frac{\alpha'''}{\alpha'}
  -\frac32(\frac{\alpha''}{\alpha'})^2\right)$$ doubles as the (chiral component of the) stress-energy tensor $$\label{se}\textstyle
   u(x-t)=\frac14(\phi_x-\phi_t)^2+\frac12
   (\phi_{xx}-\phi_{tx})+e^{-2\phi} .$$ We will now pay less attention the parallel, or rather perpendicular, $\beta$-chirality.
