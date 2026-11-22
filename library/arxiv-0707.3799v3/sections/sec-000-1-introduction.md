---
doc_id: arxiv-0707.3799v3
doc_title: "Equivariant Satake category and Kostant-Whittaker reduction"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-3
source_pdf: 0707.3799v3.pdf
source_sha256: 0b29cbced7939f72
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.996
doc_brief: "Equivariant Satake category and Kostant-Whittaker reduction — 24 sections: Front matter; Introduction; Notation and statements of the res"
---
Let $G$ be a semi-simple algebraic group over an algebraically closed characteristic zero field $\mathsf k$. The fundamental object of the geometric Langlands duality theory is the so-called *Satake category ${Perv_{{\bf G_O}}(\Gr)}$*. The latter is defined as the category of perverse sheaves on the affine (loop) Grassmannian $\Gr$ equivariant with respect to the group of regular loops ${\bf G_O}$.

It turns out that convolution provides ${Perv_{{\bf G_O}}(\Gr)}$ with a tensor structure, and the celebrated geometric Satake isomorphism theorem establishes an equivalence between ${Perv_{{\bf G_O}}(\Gr)}$ and the category of representations of the Langlands dual group ${\check{G}}$.

By its very definition ${Perv_{{\bf G_O}}(\Gr)}$ arises as the heart of the t-structure on a monoidal triangulated category -- the equivariant derived category ${D_{{\bf G_O}}(\Gr)}$. It is a natural question (raised, in particular, by V. Drinfeld) to describe ${D_{{\bf G_O}}(\Gr)}$ in terms of the dual group. Drinfeld has also noticed that at least some form of the answer[^1] follows from the results of V. Ginzburg's preprint [@G]. In the present paper we reproduce this description and extend it to a description of the *loop rotation equivariant* derived Satake category ${D_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr)}$.

The description of ${D_{{\bf G_O}}(\Gr)}$ links it to *conjugation equivariant coherent sheaves* on the Langlands dual Lie algebra. The additional $S^1$ (or ${{\mathbb G}_m}$) equivariance is connected to quantization of these to Harish-Chandra bimodules (see Theorem [\[bone\]](#bone){reference-type="ref" reference="bone"} for a precise formulation).

The argument follows the strategy of [@G]; it is based on another result of Ginzburg [@G0], which reduces the question to computation of the global equivariant cohomology of IC sheaves as modules over the global equivariant cohomology algebra $H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr)$. By an explicit calculation we show that $H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr)$ is related to the tensor square of the center of the enveloping of the dual Lie algebra $\check{\mathfrak g}{}$, while the global cohomology modules correspond to the bimodules, which describe twisting with a finite dimensional ${\check{G}}$-modules on the category of *Whittaker modules*.

This allows us to relate ${D_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr)}$ to Harish-Chandra bimodules, so that the global cohomology is identified with the Kostant-Whittaker reduction.

As an application we prove a conjecture of [@BFM] which identifies the algebra of global equivariant homology of $\Gr$ equipped with the convolution algebra structure with the quantized Toda lattice (Theorem [\[TodaTh\]](#TodaTh){reference-type="ref" reference="TodaTh"}). Note that the quantized Toda lattice also appears in the apparently related computations by Givental, Kim and others of quantum $D$-module (quantum cohomology) of the flag variety of $G$, see e.g. [@Kim].

D. Ben-Zvi and D. Nadler have informed us that they have a more conceptual proof of some of our results, see [@BN].

**Acknowledgements.** As should be clear from the above, this modest token of gratitude to Victor Ginzburg is largely an outgrowth of his own works. Throughout the mathematical biography of the authors his ingenuity, generosity and enthusiasm have been an important source of support and inspiration. We wish Vitya many happy returns of the day and a lot of exciting mathematics ahead!

This paper was partly inspired by discussions with V. Drinfeld around 2001, and some of the techniques were explained to us by L. Positselski around 1998. We also benefited a lot from explanations by A. Beilinson, D. Gaitsgory, J. Lurie and V. Lafforgue. We gratefully acknowledge all these contributions. We also thank D. Ben-Zvi and D. Nadler for their interest in this work and for sharing their related preprint [@BN].

Work on this project has been partially supported by a DARPA grant HR0011-04-1-0031. R.B. was partially supported by Sloan Foundation and NSF grant DMS-0625234, and visited Independent University of Moscow during the work; M.F. was partially supported by the CRDF award RUM1-2694, and the ANR program "GIMP", contract number ANR-05-BLAN-0029-01, and visited MSRI during the work.

[^1]: We do not address Drinfeld's problem to find a more natural derivation of the description, making compatibility with finer structures transparent. We understand that D. Gaitsgory and J. Lurie have made a significant progress in this direction.
