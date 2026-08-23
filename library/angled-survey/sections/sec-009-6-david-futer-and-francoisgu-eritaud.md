---
doc_id: angled-survey
doc_title: "From angled triangulations to hyperbolic structures"
section_id: sec-009-6-david-futer-and-francoisgu-eritaud
section_title: "DAVID FUTER AND FRANC¸OISGU ´ERITAUD"
section_number: 6
pages: 6-7
source_pdf: angled-survey.pdf
source_sha256: 8b49e682a39848bc
doc_brief: "From angled triangulations to hyperbolic structures — This survey paper contains an elementary exposition of Casson and Rivin’s technique for ﬁnding the hyperbolic metric on a 3–manifoldM with"
---
z1
z2
z3
z4 z5
z6
z7
z8
Figure 2. A normal pathσ passing through the tessellation of a
torus by boundary triangles.
parameter (see Figure 2). Letz1,...,z k be the sequence of shape parameters cor-
responding to the segments ofσ. Then theholonomy of σ is deﬁned to be
(2.2) H(σ)=
k∑
i=1
ϵi log(zi),
where ϵi = 1 for corners of triangles to the left of σ and ϵi = −1 for corners
of triangles to the right of σ. We always choose the branch of the log where
0 < arg(zi) <π for Im(zi) > 0.
Definition 2.4. Thurston’s gluing equations for a triangulationτ require, in
brief, that the holonomy of every curveσ ⊂ ∂M should be trivial. More pre-
cisely, the system consists ofedge equationsand completeness equations.T h ee d g e
equation for an edgee of τ requires that all the shape parameters adjacent toe
satisfy
(2.3)
k∑
i=1
log(zi)=2 πi.
The completeness equationsrequire that, if∂M consists ofk tori, there should be a
collection of simple closed normal curvesσ1,...,σ 2k spanning H1(∂M), such that
(2.4) H(σj)=0 ∀j.
As the name suggests, the completeness equations ensure we obtain a complete
metric.
Proposition 2.5. Let τ be an ideal triangulation ofM. Suppose that each
ideal tetrahedron ofτ is assigned a non-degenerate hyperbolic shape with positive
imaginary part, as above. If the shape parameters of the tetrahedra satisfy the edge
gluing equations, these metric tetrahedra can be glued together to obtain a (possibly
incomplete) hyperbolic metric onM/integerdivide∂M. This metric will be complete if and only
if the completeness equations are satisﬁed.
Proof. Because all hyperbolic ideal triangles are isometric, there is no ob-
struction to gluing the tetrahedra isometrically along the interiors of their faces.
If the edge equation is satisﬁed for every edge of τ, then this isometric gluing
along faces ofτ extends continuously across the edges. Thus we obtain a (possibly
incomplete) hyperbolic metric onM/integerdivide∂Mand a developing mapD : ~M → H
3.
If the metric onM is complete, thenD : ~M → H3 is an isometry. It is well-
known that the deck transformations corresponding to a component of∂M must be
parabolic isometries ofH3. In particular, if a cusp ofM is lifted to∞ in the upper
164
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
FROM ANGLED TRIANGULATIONS TO HYPERBOLIC STRUCTURES 7
half-space model ofH3, the parabolic isometries preserving that cusp are Euclidean
translations of C. But a simple closed curveσ ⊂ ∂M realizes a translation ofC
precisely when its holonomy isH(σ) = 0. Thus equation (2.4) holds for all cusps
of M.
Conversely, suppose that the completeness equations (2.4) are satisﬁed for a
basis ofH1(∂M). Then, for every cusp torusC ⊂ ∂M, the boundary triangles ofC
can be developed to tile a horosphere inH3. In other words, the developing image
of a collar neighborhood ofC is a horoball inH3, which is complete. But if we
remove the collar neighborhoods of every boundary torus inM, the remaining set
is compact, hence also complete. Thus the metric onM is complete. □
