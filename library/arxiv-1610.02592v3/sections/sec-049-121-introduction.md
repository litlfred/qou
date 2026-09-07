---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-049-121-introduction
section_title: "Introduction"
section_number: 12.1
pages: 377-378
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
A connected Riemannian manifoldM ishomogeneous if for everyp,q ∈M
there is an isometry ofM sending p to q, and isisotropic if at each pointp
every isometry ofTpM is realised by an isometry ofM. It is easy to prove that
a complete isotropic manifold is also homogeneous and has constant sectional
curvature: the fundamental examples of isotropic spaces areSn, Rn, and Hn.
The homogeneous condition alone (without isotropy) is more relaxed and
produces manifolds that may not have constant sectional curvature. We intro-
duce in this chapter eight important homogeneous simply-connected complete
Riemannian 3-manifolds:
S3, R3, H3, S2× R, H2× R, Nil, Sol, ~SL2.
The ﬁrst three manifolds are also isotropic and have constant sectional curva-
ture, the other ﬁve are not.
LetM be one of these eight model manifolds. We say that a Riemannian
3-manifoldN has ageometric structure modelled onM ifN is locally isometric
to M, that is if every pointp∈ N has an open neighbourhood isometric to
some open set inM. This implies thatN is locally homogeneous: every two
points p,q ∈N have isometric neighbourhoodsU(p)∼=U(q), both isometric
to anε-ball at any point ofM.
369
370 12. THE EIGHT GEOMETRIES
χ> 0 χ = 0 χ< 0
e = 0 S2× R R 3 H2× R
e⁄= 0 S3 Nil ~SL2
Table 12.1. The closed manifolds modelled on six geometries are pre-
cisely the six commensurable classes of Seifert manifolds, distinguished by
the numberse andχ.
IfN iscomplete, thedevelopingmapconstructionofTheorem3.1.2applies
also in this context and shows thatN = M/Γ for some discrete groupΓ <
Isom(M) acting freely.
We now start a long journey through these eight geometries. The ﬁnal
goal of this chapter is to prove the following.
Theorem 12.1.1.A closed orientable 3-manifold has a geometric structure
modelled on one of the following six geometries:
S3, R3, S2× R, H2× R, Nil, ~SL2
if and only if it is a Seifert manifold of the appropriate commensurability class,
as prescribed by Table 12.1. It has aSol geometric structure if and only if it
is a torus (semi-)bundle of Anosov type.
It is a surprising (and maybe disappointing) fact that, despite its elegance
and generality, the only known proof of this theorem available today works
by investigating each geometry separately and carefully, often employing quite
diﬀerent techniques. We start with the elliptic case.
