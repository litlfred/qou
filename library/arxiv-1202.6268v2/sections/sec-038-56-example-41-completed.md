---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-038-56-example-41-completed
section_title: "Example: 41 completed"
section_number: 5.6
pages: 37-37
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.927
latex_coverage_ratio: 1.0
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sec.41Sn label="sec.41Sn"}

We may demonstrate the power of the Feynman-diagram approach by computing the first two subleading corrections $S_{\mathcal{T},2}$ and $S_{\mathcal{T},3}$ for the figure-eight knot complement.

We can use the same Neumann-Zagier datum described in Section [\[sec.41triang\]](#sec.41triang){reference-type="ref" reference="sec.41triang"}, along with the generalized flattening of Section [\[sec.utor41\]](#sec.utor41){reference-type="ref" reference="sec.utor41"}. Let us specialize to representations $\rho_m$ on the geometric component of the character variety. Then the two shapes $z,\,w$ are expressed as functions on the A-polynomial curve,

$$\label{zw412} z = -\frac{m^2-m^{-2}}{1+m^2\ell} \,,\qquad w= \frac{m^2+\ell}{m^2-m^{-2}}\,,$$

as in [\[zw41m\]](#zw41m){reference-type="eqref" reference="zw41m"}.

The 2-loop invariant is explicitly given in [\[2loopexplicit\]](#2loopexplicit){reference-type="eqref" reference="2loopexplicit"} of the Introduction. Evaluating this expression in `Mathematica`, we find

$$\notag S_{\mathbf{4_1},2}=-\frac{w^3 (z+1)+w^2 ((11-8 z) z-4)+w (z-1) (z (z+12)-5)+(z-2) (z-1)^2}{12 (w+z-1)^3}\,.$$

Upon using [\[zw412\]](#zw412){reference-type="eqref" reference="zw412"} to substitute rational functions for $z$ and $w$, the answer may be most simply expressed as

$$\widetilde S_{\mathbf{4_1},2}= \frac{S_{\mathbf{4_1},2}+1/8}{\tau_{\mathbf{4_1}}^3} = -\frac{1}{192}\big(m^{-6}-m^{-4}-2m^{-2}+15-2m^2-m^4+m^6\big)\,,$$

where we have divided by a power of the torsion as suggested in [\[tordivide\]](#tordivide){reference-type="eqref" reference="tordivide"} of the Introduction. (We have also absorbed a constant $1/8$, recalling that our formula is only well defined modulo $\mathbb Z/24$.

In a similar way, we may calculate the 3-loop invariant, finding unambiguously

$$\widetilde S_{\mathbf{4_1},3} = \frac{S_{\mathbf{4_1},3}}{\tau_{\mathbf{4_1}}^6}=\frac{1}{128}\big(m^{-6}-m^{-4}-2m^{-2}+5-2m^2-m^4+m^6\big)\,.$$

These answers agree perfectly with the findings of [@DGLZ], and the comparison there to the asymptotics of the colored Jones polynomials at general $u$. Moreover, at the discrete faithful representation we obtain

$$S_{\mathbf{4_1},2} = \frac{11i}{72\sqrt{3}}= -\frac{11}{192\,\tau_{\mathbf{4_1}}^{3}}\,,\qquad S_{\mathbf{4_1},3}=-\frac1{54} = \frac{1}{128\,\tau_{\mathbf{4_1}}^{6}}\,,$$

in agreement with known asymptotics of the Kashaev invariant.
