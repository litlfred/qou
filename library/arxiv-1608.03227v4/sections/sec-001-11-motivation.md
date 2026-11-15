---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-001-11-motivation
section_title: "Motivation"
section_number: 1.1
pages: 3-4
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.993
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
In recent years there was a lot of interest in establishing a connection between knot homology, Macdonald polynomials and Hilbert schemes of points on a plane

[@AS],[@Ch],[@GN],[@GORS],[@ORS]. In particular, there are many conjectural formulas expressing the knot homology of torus knots in terms of Macdonald polynomials or in terms of spaces of sections of special sheaves on the Hilbert schemes of points [@ORS],[@GORS],[@GN]. An agreement between these formulas is an interesting result at the intersection of algebra and geometry.

When this paper was posted and its results were announced, the attempts to attack these conjectures directly, without a new computational method, were not succeeding. More recently, a version of a categorical localization was developed and applied to some of these conjectures in [@Ho; @EHo; @Me].

The current mathematical construction of triply graded homology based on Soergel bimodules is not related to Hilbert schemes of points. Hence the approach of [@Ho; @EHo; @Me] is to compute the Soergel-based knot homology explicitly

and compare the answer with the homology of sheaves on the Hilbert scheme where the answer is known. One would still like to find a more direct link between the knot homology and sheaves on the Hilbert scheme of points on the plane.

Around the time of posting of this paper the authors of [@GNR] proposed a conjectural connection between the Soergel bimodules and the category of coherent sheaves on the Hilbert scheme of points.

Our approach is different from that of [@GNR]. Roughly speaking, to a braid $\beta\in\Brgrn$ we associate a sheaf $\calS_{\beta}$ on the Hilbert scheme $\SymbolPrint{\Hilb_n}$ of $n$ points on $\CC^2$. The space of global sections of $\calS_\beta$ is the homology of the link $L(\beta)$ which is the closure of $\beta$.

The construction of $\calS_\beta$ is quite involved and relies on a homomorphism from the braid group $\Brgrn$ to the convolution algebra of a category of matrix factorizations on an auxiliary space. We expect this homomorphism to be injective, but we neither prove nor use this fact in the paper.

Compared to Soergel bimodule construction, our approach is more complicated conceptually, but it is more geometric and, surprisingly, in some important cases it is less computationally challenging.

For example, in a subsequent paper [@OR] we show that adding a full twist $\SymbolPrint{Tw}$ to the braid results in the twisting of $\calS_{\beta}$ by a special line bundle: $\calS_{\beta\cdot Tw}=\calS_{\beta}\otimes L$. Existence of a knot theory with such property was predicted in [@ORS].
