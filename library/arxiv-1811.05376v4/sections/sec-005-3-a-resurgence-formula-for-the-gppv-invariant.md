---
doc_id: arxiv-1811.05376v4
doc_title: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres"
section_id: sec-005-3-a-resurgence-formula-for-the-gppv-invariant
section_title: "A resurgence formula for the GPPV invariant"
section_number: 3
pages: 19-20
source_pdf: 1811.05376v4.pdf
source_sha256: a486709d0a78d19c
doc_brief: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres — For a Seifert ﬁbered homology sphereX we show that the q-series invariant ˆZ0(X;q) introduced by Gukov-Pei-Putrov-Vafa"
---
We now turn to theq-series invariantˆZ0(X,q ). We follow [28]. Let(Γ,m ) be an ordered weighted
tree, i.e. Γ is a tree together with an ordering of its set of verticesV and m is a mapm :V → Z.
Set s =|V| and letM =M(Γ,m ) be thes×s matrix with entries given by
Mi,j =



mv if vi =vj =v,
1 if vi and vj are joined by an edge,
0 otherwise.
Resurgence Analysis of Quantum Invariants 20
We sayM is weakly negative deﬁnite ifM is invertible andM−1 is negative deﬁnite on the subspace
of Zs spanned by vertices of degree at most3. LetY =Y (Γ,m ) be the oriented three manifold with
surgery dataL =L(Γ,m ) constructed as follows. For each vertexv the linkL has an unknotted
component Lv with framingmv, and Lv is chained together withLw if and only ifv and w are
joined by an edge. We callY a plumbed manifold with plumbing graphΓ.
We recall that two plumbed three manifoldsY and Y′ are diﬀeomorphic if and only their
plumbing graphs are related by Neumann moves.
When Y is a plumbed manifold with weakly negative deﬁnite plumbing graph andY is not
necessarily a homology3-sphere, theq-series invariantˆZa(Y,q ) depend on a labela, whose precise
meaning is subtle. Originally, these labels where thought to be abelian ﬂat connections, laterSpinc
structures, and for mapping tori of genus one mapping classes one has include "almost abelian" ﬂat
connections (see [13]). AsX = Σ(p1,...,p n) is a homology three sphere, we havea = 0, and need
not go deeper into this discussion. For the sake of completeness however, we recall the GPPV-
formula deﬁnition as it is stated in terms ofSpinc-structures. First we recall howSpinc-structures
can be described in terms of the adjacency matrixM. This is thorougly explained in [28]. LetY be
a plumbed three manifold with plumbing graphΓ. Let s =|V|. Let ⃗ m∈ Zs be the weight vector,
i.e. mj =m(vj). Let⃗δ∈ Zs, be the degree vector i.e.δj = deg(vj). We have isomorphisms
Spinc(Y )≃ (Zs + ⃗ m)/2M Zs≃ (Zs +⃗δ)/2M Zs.
These isomorphisms are compatible with Neumann moves as explained in [28]. We now recall the
GPPV-formula (49).
Deﬁnition 1([29]). Let Y be a plumbed three manifold with weakly deﬁnite plumbing graphΓ.
Let φ denote the number of positive eigenvalues ofM and let σ denote the signature ofM. Let
a = [⃗ a]∈ (Zs +⃗δ)/2M Zs≃ Spinc(Y ). The ˆZ-invariant of (Y,a ) is given by
ˆZa(Y ;q) = (−1)φq
3σ−∑
vmv
4 ·v.p.
∮
|zv|=1
∏
v∈V
dzv
2πizv
(
zv− 1
zv
)2−deg(v)
Θ−M
a (⃗ z) (49)
wherev.p. denotes the principal value and
Θ−M
a (⃗ z) =
∑
⃗l∈2M Zs+⃗ a
q− (⃗l,M−1⃗l))
4
∏
v∈V
zlv
v
Remark 2. The invariance of(49) under Neumann moves is proved by Gukov and Manulescu in
[28].
We recall that the principal valuev.p. is deﬁned such that for every suﬃciently smallϵ> 0 we
have
v.p.
∮
|z|=1
= 1
2
(∮
|z|=1+ϵ
+
∮
|z|=1−ϵ
)
.
