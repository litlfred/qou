---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-016-43-the-flip
section_title: "The flip"
section_number: 4.3
pages: 36-37
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.727
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
[]{#sec:flip label="sec:flip"}

Just as $2-3$ moves change the internal triangulation of a 3-manifold, the flips described in Section [\[sec:geom23\]](#sec:geom23){reference-type="ref" reference="sec:geom23"} can change the triangulation of its (geodesic) boundary. This has a very simple effect on a theory $T_{M,\Pi}$.

For example, suppose that $T_{M,\Pi}$ has an operator $\mathcal{O}_X$, charged under a global symmetry $U(1)_X$, that corresponds to an external edge with position coordinate $X$. We want to add a tetrahedron $\Delta_Z$ to flip this edge, as in Figure [\[fig:flip\]](#fig:flip){reference-type="ref" reference="fig:flip"}. Following our gauge theory dictionary, this means that we form the combined theory $T_{M,\Pi}\otimes T_{\Delta_Z,\Pi_Z}$, and add a superpotential coupling

$$\mathcal{W}= \mathcal{O}_X\phi_Z\,. \label{Wflip}$$

The new theory now has a chiral operator $\phi_Z$ that transforms under the anti-diagonal subgroup of $U(1)_X\times U(1)_Z$ that is unbroken by [\[Wflip\]](#Wflip){reference-type="eqref" reference="Wflip"}.

This transformation simply describes the $F$ operation of Section [\[sec:F\]](#sec:F){reference-type="ref" reference="sec:F"}. Just as $F^2$ is a trivial operation on a 3d SCFT, flipping a diagonal twice is a trivial operation on the boundary of a 3-manifold.
