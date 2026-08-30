---
doc_id: arxiv-1004.1533v3
doc_title: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT"
section_id: sec-012-8-invariants-of-extended-3-manifolds
section_title: "Invariants of extended 3-manifolds"
section_number: 8
pages: 27-34
source_pdf: 1004.1533v3.pdf
source_sha256: 95c1544431e6bf37
doc_brief: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT — In this paper we show how one can extend Turaev-Viro invarian ts, deﬁned for an arbitrary spherical fusion category C, to 3-manifolds with cor- ners."
---
We begin by generalizing the deﬁnition of a polytope decomposition to e xtended
3-manifolds as deﬁned in Deﬁnition 6.3.
Deﬁnition 8.1. A combinatorial extended 3-manifold M is an extended PL 3-
manifold with a polytope decomposition such that
• For an open tube Tα , its interior is a single 3-cell of the decomposition.
Moreover, the interior of the “bottom disk” B0 =ϕ α ({0} ×D2) is a single
2-cell of the decomposition, and the marked point P on the boundary of
the bottom disk is a vertex of the decomposition, and similarly for the top
disk B1 =ϕ α ({1} ×D2).
28 BENJAMIN BALSAM AND ALEXANDER KIRILLOV, JR.
• For a closed tube Tα , the interior of the disk Bα =ϕ α ({0} ×D2) is a single
2-cell of the decomposition, the marked point Pα ∈∂B α is a vertex of the
decomposition, and the complement Int( Tα ) −Bα is a single 3-cell of the
decomposition.
Note that this implies that the restriction of such a polytope decomp osition to
the boundary of ∂M satisﬁes the conditions of Deﬁnition 7.1 and thus deﬁnes on
∂M the structure of a combinatorial extended surface. It also this im plies that
M contains two kinds of 3-cells: usual cells (which are not contained in a ny tube)
and “tube cells”, i.e. cells contained in one of the tubes. The boundar y of a
usual 3-cell is a union of usual 2-cells; the boundary of a 3-cell cor responding to an
open tube contains usual 2-cells and two embedded disks; the boun dary of a 3-cell
corresponding to a closed tube contains usual 2-cells and two copie s of the disk Bα
with opposite orientation.
Finally, note that we have imposed no restriction on the longitude of t he tube:
it is allowed (and usually will) intersect the edges of the decomposition o f the
boundary tubes.
The following theorem is an analog of Theorem 3.4.
Theorem 8.2. Let M be an extended 3-manifold. Then any two polytope decom-
positions M′, M′′ of M which satisfy the conditions of Deﬁnition 8.1 and agree on
∂M can be obtained from each other by a sequence of moves M1—M3 an d their
inverses such that all intermediate decompositions also sa tisfy the conditions of
Deﬁnition 8.1 and agree with M′, M′′ on ∂M .
Proof. Let us consider the manifold ˜M obtained by removing from M the interior
of every tube and also the interior of the embedded disks on the bou ndary of M .
Then ˜M is a manifold with boundary
∂ ˜M = (∂M − ∪ Int(Dα )) ∪∂ ˜Mf ree
where the “free boundary” ∂ ˜Mf ree is the union of side surfaces I ×∂D 2 of the tubes
(for closed tubes, S1 ×∂D 2).
Obviously, polytope decompositions M′, M′′ satisfying the conditions of the
theorem determine decomposition of ˜M which agree on the subset X = (∂M −
∪ Int(Dα )) ⊂∂ ˜M . Now the result follows from Theorem 3.7. □
Recall that for usual oriented 3-cell F and a choice of edge labeling l, we have
deﬁned the vector ZT V (F,l ) ∈ H(∂F,l ) deﬁned by (4.4). We can now generalize
it to tube cells. Namely, let l be an edge coloring of an extended combinatorial
3-manifold M and let Tα ⊂ M be an open tube, with the longitude γα and color
Yα ∈Z(C). Since T is homeomorphic to [0 , 1] ×D2 ≃D3— a 3-ball, the boundary
∂T is homeomorphic toS2; thus, the polytope decomposition of T deﬁnes a polytope
decomposition of S2.
Let Γ be the dual graph of this cell decomposition. We can connect t he marked
points on the top and bottom disks to the vertex of the dual graph corresponding
to these disks; together with the longitude γ, this gives an oriented arc on the
surface of the sphere whose endpoints are two distinct vertices o f Γ. For every
2-cell C ∈ ∂F (including the embedded disks), choose a vector vC ∈ H(C,l )∗.
Thus, we get a graph ˆΓ of the type considered in Section 2, i.e. colored graph Γ
on the surface of the sphere together with a colored framed arc in side as shown in
Figure 26. By Theorem 2.4 this deﬁnes a number ZRT (ˆΓ); as before, we let
TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT 29
Figure 26. Dual graph for a tube cell. The longitude is shown
by double green line.
(8.1) ( Z(F,l ), ⊗vC ) = ZRT (ˆΓ).
In a similar way we deﬁne the invariant for closed tubes.
We can now generalize the constructions of Section 4 to extended 3 -manifolds.
Deﬁnition 8.3. Let M be an extended combinatorial 3-manifold with boundary
and C – a spherical category. Then for any edge coloring l and a coloring Yα of the
tubes Tα ⊂ M, deﬁne the vector
ZT V (M, {Yα },l ) ∈H(∂M, {Yα },l )
by
ZT V (M,l ) = ev
(⨂
F
Z(F,l )
)
where
• F runs over all 3-cells in M (including the tube cells), each taken with the
induced orientation, so that
⨂
F
Z(F,l ) ∈
⨂
F
H(∂F,l ) = H(∂M,l ) ⊗
⨂
c
H(c′,l ) ⊗H(c′′,l )
(compare with Lemma 3.2)
• c runs over all unoriented 2-cells in the interior of M , including the disks
Bα inside the closed tubes, and c′,c ′′ are the two orientations of such a cell,
so that c′ =
c′′.
30 BENJAMIN BALSAM AND ALEXANDER KIRILLOV, JR.
• ev is the tensor product over all c of evaluation maps H(c′,l ) ⊗H(c′′,l ) =
H(c′,l ) ⊗H(c′,l )∗ → k
Finally, we deﬁne
(8.2) ZT V (M, {Yα }) = D−2v(M) ∑
l
(
ZT V (M, {Yα },l )
∏
e
dne
l(e)
)
where
• the sum is taken over all equivalence classes of simple labellings of M,
• e runs over the set of all (unoriented) edges of M
• D is the dimension of the category C (see (1.1)), and
v(M) = number of internal vertices of M + 1
2 (number of vertices on ∂M)
• dl(e) is the categorical dimension of l(e) and
ne =
{
1, e is an internal edge
1
2, e ∈∂M
Note that in this deﬁnition, edges and vertices on the boundary of t he tubes are
considered internal unless they are also on ∂M.
Theorem 8.4.
(1) ZT V (M) satisﬁes the gluing axiom: if M is an extended combinatorial
3-manifold with boundary ∂M = N0 ∪ N ∪ N , and M′ is the manifold
obtained by identifying boundary components N, N of∂M with the obvious
cell decomposition (if N contains embedded disks, then we may need to
erase them so that the interior of resulting tubes have exact ly one 3-cell ),
then we have
ZT V (M′) = ev H(N )ZT V (M) =
∑
α
(ZT V (M),ϕ α ⊗ϕ α ),
where ev is the evaluation map H(N ) ⊗H(N ) → k, and ϕ α ∈ H(N ),
ϕ α ∈H(N ) are dual bases.
(2) If a M is an extended PL 3-manifold, and M′, M′′ are two polytope de-
compositions of M which agree on the boundary, then Z(M′, {Yα }) =
Z(M′′, {Yα }).
(3) For a combinatorial 2-manifold N , deﬁne A : H(N ) →H(N ) by
(8.3) A =ZT V (N × I)
Then A is a projector: A2 =A.
(4) For a combinatorial extended 2-manifold N , deﬁne the vector space
(8.4) ZT V (N ) = Im(A : H(N ) →H(N ))
where A is the projector (8.3). Then the space ZRT (N ) is an invariant
of PL manifolds: if N ′, N ′′ are two diﬀerent polytope decompositions of
the same extended PL manifold N , then one has a canonical isomorphism
Z(N ′) ≃Z(N ′′).
Proof. The proof is parallel to the proof of Theorem 4.4. The only new ingred ient
is in the proof of part (1), i.e. the gluing axiom for 3-manifolds: if the c omponent
of boundary along which we are gluing contains embedded disks, we ne ed to erase
TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT 31
them so that in the resulting manifold, interior of each tube is exactly one 3-cell.
Thus, we need to check that our that Z(M) is unchanged under this operation. The
proof of this is similar to invariance under M3 move proved in Section 5. Details
are left to the reader.
□
Finally, we also note that our extended theory satisﬁes the gluing ax iom for
extended surfaces.
Theorem 8.5. Under the assumptions of Theorem 7.3, one has a natural isomor-
phism
Z(N ′, {Yα }α ∈D′) =
⨁
Z∈Irr(Z(C))
Z(N, {Yα }α ∈D′,Z,Z ∗)
where objects Z,Z ∗ are assigned to embedded disks a,b .
Proof. Recall that by Theorem 7.3, one has an isomorphism
G :
⨁
Z∈Irr(Z(C))
H(N, {Yα }α ∈D′,Z,Z ∗)
∼
− →H(N ′, {Yα }α ∈D′)
Since Z(N ) is deﬁned as the image of the projector A : H(N ) →H(N ), and simi-
larly for Z(N ′), it suﬃces to prove that the following diagram is commutative:
H(N,Z,Z ∗) H(N ′)
H(N,Z,Z ∗) H(N ′)
G
G
A A′
or equivalently, that for any ϕ ∈H(N,Z,Z ∗), ϕ ′ ∈H(N,Z,Z ∗), we have
(Z(N × I,Z,Z ∗),ϕ ⊗ϕ ′) = (Z(N ′ ×I),G (ϕ ) ⊗G(ϕ ′)).
Comparing both sides, we see that the only diﬀerence is that N × I contains a
pair of cylinders Da ×I,D b ×I:
ADa A′
k
l
B DbB′
32 BENJAMIN BALSAM AND ALEXANDER KIRILLOV, JR.
whereas N ′×I contains instead a single cellC×I, whereC is the cylinder connecting
boundary circles ∂D a,∂D b:
A A′
i
j
k
l
BB′
Thus, it suﬃces to prove that for any collection
ϕ a ∈H(Da) = ⟨A,Z ⟩, ϕ b ∈H(Db) = ⟨B,Z ∗⟩,
ϕ ′
a ∈H(Da)∗ = ⟨(A′)∗,Z ∗⟩, ϕ b ∈H(Db)∗ = ⟨(B′)∗,Z ⟩,
ψ a ∈H(∂D a ×I) = ⟨Xk,A ′,X ∗
k,A ∗⟩, ψ b ∈H(∂D b ×I) = ⟨Xl,B ′,X ∗
l,B ∗⟩
we have
Z(Da ×I,ϕ a ⊗ϕ ′
a ⊗ψ a) ·Z(Db ×I,ϕ b ⊗ϕ ′
b ⊗ψ b)
=
∑
i,j
√
di
√
dj Z(C ×I,ψ a,ψ b,G (ϕ a ⊗ϕ b),G (ϕ ′
a ⊗ϕ ′
b))
(the factors √
di,
√
dj appear because N ′ ×I contains two extra edges on the
boundary, labeled i,j .)
The left hand side is given by
LHS = ψ a
ϕ ′
a
ϕ a
Z
A′
A
k
· ψ b
ϕ ′
b
ϕ b
Z ∗
B′
B
l
Combining explicit computation given in Section 9.1 with the formula for g luing in
Lemma 7.4, we see that the right hand side is given by
RHS =
∑
i,j
didjdZ
D2 ψ a ϕ ψ b ϕ ∗
ϕ ′
a
ϕ ′
b
ϕ a ϕ b
Z
Z ∗
k l lA′ B′
i
A Bj
k
TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT 33
Using Lemma 1.1, we can rewrite it as
RHS =
∑
j
djdZ
D2 ψ a ψ b
ϕ ′
a
ϕ ′
b
ϕ a ϕ b
A′ B′
j
A B
k l
Since it follows from Lemma 2.2 that for any simple Z ∈ ObjZ(C) and a morphism
Φ ∈ HomC(Z,Z ), we have
1
D2
∑
j
dj Φ
Z
Z
j
= 1
dZ
tr(Φ) id Z
this easily implies that the LHS is equal to RHS.
□
Example 8.6. Let N be the sphere with n embedded disks, colored by objects
Y1,...,Y n ∈ ObjZ(C) (see Example 7.2). Then
Z(N,Y 1,...,Y n) = Hom Z(C)(1,Y 1 ⊗Y2 ⊗ · · · ⊗Yn).
Indeed, by Example 7.2, we have
H(N,Y 1,...,Y n) =
⨁
i1,...,i n∈Irr(C)
⟨Xi1,Y 1,X ∗
i1,...,X in,Y n,X ∗
in ⟩.
34 BENJAMIN BALSAM AND ALEXANDER KIRILLOV, JR.
By a direct computation done in Section 9, we see that the operator A =Z(N ×
I) :H(N ) →H(N ) is given by
ϕ ↦→ 1
D2(n+1)
∑
l,j 1,...,j n∈Irr(C)
dl
n∏
a=1
√
dia
√
dja
ϕ
Y1 Yni1
j1
in
jn
ll
...
Consider now the subspace W ⊂ H(N,Y 1,...,Y n) spanned by elements of the
form
⨁
j1,...,j n
n∏
a=1
√
dja
ψ
Y1 Yn
j1 jn
...
ψ ∈ HomZ(C)(1,Y 1 ⊗ · · · ⊗Yn)
Clearly,W ≃ HomZ(C)(1,Y 1 ⊗ · · · ⊗Yn).
Now, it follows from the previous computation and Lemma 2.2 that for any
ϕ ∈ H(N,Y 1,...,Y n), we have Aϕ ∈ W ; on the other hand, it is immediate that
if ψ ∈W , then Aψ =ψ . Therefore, A is the projector onto W ≃ HomZ(C)(1,Y 1 ⊗
· · · ⊗Yn).
