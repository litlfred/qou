---
doc_id: arxiv-1811.05376v4
doc_title: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres"
section_id: sec-005-3-a-resurgence-formula-for-the-gppv-invariant
section_title: "A resurgence formula for the GPPV invariant"
section_number: 3
pages: 19-20
source_pdf: 1811.05376v4.pdf
source_sha256: a486709d0a78d19c
toc_source: outline
doc_brief: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres — For a Seifert ﬁbered homology sphere X we show that the q-series invariant ˆZ0(X; q) introduced by"
---
A resurgence formula for the GPPV invariant
We now turn to the q-series invariant ˆZ0(X, q). We follow [28]. Let (Γ, m) be an ordered weighted
tree, i.e. Γ is a tree together with an ordering of its set of vertices V and m is a map m : V →Z.
Set s = |V | and let M = M(Γ, m) be the s × s matrix with entries given by
Mi,j =





mv
if vi = vj = v,
1
if vi and vj are joined by an edge,
0
otherwise.
We say M is weakly negative deﬁnite if M is invertible and M −1 is negative deﬁnite on the subspace
of Zs spanned by vertices of degree at most 3. Let Y = Y (Γ, m) be the oriented three manifold with
surgery data L = L(Γ, m) constructed as follows. For each vertex v the link L has an unknotted
component Lv with framing mv, and Lv is chained together with Lw if and only if v and w are
joined by an edge. We call Y a plumbed manifold with plumbing graph Γ.
We recall that two plumbed three manifolds Y and Y ′ are diﬀeomorphic if and only their
plumbing graphs are related by Neumann moves.
When Y is a plumbed manifold with weakly negative deﬁnite plumbing graph and Y is not
necessarily a homology 3-sphere, the q-series invariant ˆZa(Y, q) depend on a label a, whose precise
meaning is subtle. Originally, these labels where thought to be abelian ﬂat connections, later Spinc
structures, and for mapping tori of genus one mapping classes one has include "almost abelian" ﬂat
connections (see [13]). As X = Σ(p1, ..., pn) is a homology three sphere, we have a = 0, and need
not go deeper into this discussion. For the sake of completeness however, we recall the GPPV-
formula deﬁnition as it is stated in terms of Spinc-structures. First we recall how Spinc-structures
can be described in terms of the adjacency matrix M. This is thorougly explained in [28]. Let Y be
a plumbed three manifold with plumbing graph Γ. Let s = |V |. Let⃗m ∈Zs be the weight vector,
i.e. mj = m(vj). Let⃗δ ∈Zs, be the degree vector i.e. δj = deg(vj). We have isomorphisms
Spinc(Y ) ≃(Zs +⃗m)/2MZs ≃(Zs +⃗δ)/2MZs.
These isomorphisms are compatible with Neumann moves as explained in [28]. We now recall the
GPPV-formula (49).
Deﬁnition 1 ([29]). Let Y be a plumbed three manifold with weakly deﬁnite plumbing graph Γ.
Let φ denote the number of positive eigenvalues of M and let σ denote the signature of M. Let
a = [⃗a] ∈(Zs +⃗δ)/2MZs ≃Spinc(Y ). The ˆZ-invariant of (Y, a) is given by
ˆZa(Y ; q) = (−1)φq
3σ−P
v mv
4
· v.p.
I
|zv|=1
Y
v∈V
dzv
2πizv

zv −1
zv
2−deg(v)
Θ−M
a
(⃗z)
(49)
where v.p. denotes the principal value and
Θ−M
a
(⃗z) =
X⃗
l∈2MZs+⃗a
q−(⃗l,M−1⃗l))
4
Y
v∈V
zlv
v
Remark 2. The invariance of (49) under Neumann moves is proved by Gukov and Manulescu in
[28].
We recall that the principal value v.p. is deﬁned such that for every suﬃciently small ϵ > 0 we
have
v.p.
I
|z|=1
= 1
2
 I
|z|=1+ϵ
+
I
|z|=1−ϵ
!
.
