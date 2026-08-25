---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-006-21-face-pairing-permutations
section_title: "Face pairing permutations"
section_number: 2.1
pages: 7-8
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
dered simplex with S4.
Deﬁnition 2.4. Let ∆0 and ∆1 be ordered simplices and let ψ from face f0 of ∆0 to face
f1 of ∆1 be a face pairing. The face pairing permutation corresponding to ψ is the unique
permutation σ∈ S4 such that ψ takes vertex v of ∆0 to vertex σ(v) of ∆ 1 whenever v is a
vertex in f0.
Note that if we identify ∆ 0 and ∆1 via the unique order preserving isomorphism, σ is the
unique extension of ψ to a symmetry of ∆ 0. See Figure 6.
8 STA VROS GAROUF ALIDIS, MATTHIAS GOERNER, AND CHRISTIAN K. ZICKERT
3. Thurston’s gluing equations
In this section we brieﬂy review Thurston’s gluing equations. For details we refer to
Thurston [17] or Neumann-Zagier [15].
LetT be an oriented triangulation of M. The gluing equations are given in terms of a
variablez∆∈ C\{ 0, 1}, called a shape coordinate, for each simplex ∆ of M. To deﬁne the
equations, assign to each edge of each simplex ∆ of M one of three shape parameters, see
Figure 3. The shape parameters are given in terms of the shape coordinate z∆ by
(3.1) z∆, z ′
∆ = 1
1−z∆
, z ′′
∆ = 1− 1
z∆
=−1−z∆
z∆
.
Figure 3. Assigning shape parameters to the edges of a simplex.
The gluing equations consist of edge equations and cusp equations . There is an edge
equation for each edge cyclee ofT , obtained by setting the product of the shape parameters
assigned to each edge in e equal to 1. Each edge equation thus has the form
(3.2)
∏
∆
za∆
∆
∏
∆
z′b∆
∆
∏
∆
z′′c∆
∆ = 1,
where a∆, b∆ and c∆ are integers.
The cusp equations consist of an equation for each generator of the fundamental group of
each boundary component. If γ is a peripheral (normal) curve, we obtain a cusp equation
by setting the product of the shape parameters (or their inverses) of edges passed by γ equal
to 1 (γ passes an edge E of a simplex ∆ if it enters and exits ∆ through faces intersecting
in E). A shape parameter appears with its inverse if and only if γ passes e in a clockwise
direction viewed from the cusp. The cusp equations have the same form as (3.2).
The following result is well known. We will generalize this to representations in PGL(n, C)
below.
Theorem 3.1. A solution to the edge equations with all shape coordinates in C\{ 0, 1}
uniquely (up to conjugation) determines a representation ρ: π1(M)→ PGL(2, C). If the
solution also satisﬁes the cusp equations, ρ is boundary-unipotent, i.e. takes peripheral curves
to a conjugate of N.
