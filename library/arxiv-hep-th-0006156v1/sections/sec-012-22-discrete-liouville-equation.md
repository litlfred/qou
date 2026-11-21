---
doc_id: arxiv-hep-th-0006156v1
doc_title: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality"
section_id: sec-012-22-discrete-liouville-equation
section_title: "Discrete Liouville equation"
section_number: 2.2
pages: 8-8
source_pdf: 0006156v1.pdf
source_sha256: b799d4ef150291cf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 1.0
doc_brief: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality — The quantum discrete Liouville model in the strongly cou- pled regime, 1 < c < 25, is formulated as a well"
---
It not only ideologically justifies the chosen discretization but also helps make the following action more entertaining. In continuum, the Liouville equation may be considered as a compatibility condition for the Liouville formula overloaded with Möbius-invariance. It ought to be just the same on the lattice, so let us find out what "equation of motion" the $\chi$'s might solve. We pick four of them next to each other to figure out that they are four cross-ratios made from the total of six $\alpha$'s and $\beta$'s. That is one too many: 4 $\chi$'s + 3 symmetry parameters -- 3 $\alpha$'s -- 3 $\beta$'s = 1. The missing one turns out to be $$\label{lle}
   \chi_{j,k+1}\chi_{j,k-1}=\frac{\chi_{j-1,k}
   \chi_{j+1,k}}{(1+\chi_{j-1,k})
   (1+\chi_{j+1,k})}\qquad j+k\equiv0\!\!
   \pmod2\!\!\!\!\!\!\!\!\!$$ which so becomes our favourite lattice Liouville equation --- replacing Hirota's original $$h_{j,k+1}h_{j,k-1}=\frac{h_{j-1,k}h_{j+1,k}}
{1+h_{j-1,k}h_{j+1,k}} .$$ The two are connected by a simple change of variables $$\chi_{jk}=h_{j-1,k}h_{j+1,k}    ,$$ which quarters the $h$'s in the empty sites of our lattice of course. However, that change would also split cross-ratios, which we want to avoid, at least in this paper.

The stress-energy connection ([\[se\]](#se){reference-type="ref" reference="se"}) also lends itself to a cross-ratio treatment. The Schwarz derivative inevitably becomes another cross-ratio [@fadtak1] $$u_n=4\frac{(\alpha_{n+2}-\alpha_{n+1})
  (\alpha_{n}-\alpha_{n-1})}{(\alpha_{n+2} -\alpha_{n-1})(\alpha_{n+1}-\alpha_{n-1})} ,$$ then another counting argument leads to $$\label{lse}
   \frac4{u_{\frac12(j-k)}}=\left(1+\chi_{j,k-1}
   +\dfrac{\chi_{j,k-1}}{\chi_{j-1,k}}\right)
   \left(1+\chi_{j+1,k}+\dfrac{\chi_{j+1,k}}
   {\chi_{j+2,k-1}}\right) \;.$$
