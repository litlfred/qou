---
doc_id: arxiv-1004.1533v3
doc_title: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT"
section_id: sec-003-2-preliminaries-ii-drinfeld-center
section_title: "Preliminaries II: Drinfeld Center"
section_number: 2
pages: 6-10
source_pdf: 1004.1533v3.pdf
source_sha256: 95c1544431e6bf37
doc_brief: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT — In this paper we show how one can extend Turaev-Viro invarian ts, deﬁned for an arbitrary spherical fusion category C, to 3-manifolds with cor- ners."
---
We will also need the notion of Drinfeld center of a spherical fusion ca tegory. Re-
call that the Drinfeld center Z(C) of a fusion category C is deﬁned as the category
whose objects are pairs ( Y,ϕ Y ), where Y is an object of C and ϕ Y – a functo-
rial isomorphism Y ⊗ − → − ⊗ Y satisfying certain compatibility conditions (see
[M¨ ug2003a]).
As before, we will frequently use graphical presentation of morph isms which
involve objects both of C and Z(C). In these diagrams, we will show objects of
Z(C) by double green lines and the half-braiding isomorphism ϕ Y : Y ⊗V →V ⊗Y
by crossing as in Figure 4.
Y V
Figure 4. Graphical presentation of the half-braiding ϕ Y : Y ⊗
V →V ⊗Y ,Y ∈ ObjZ(C),V ∈ Obj C
We list here main properties of Z(C), all under the assumption that C is a
spherical fusion category over an algebraically closed ﬁeld of chara cteristic zero.
Theorem 2.1. [M¨ ug2003b]Z(C) is a modular category; in particular, it is semisim-
ple with ﬁnitely many simple objects, it is braided and has a p ivotal structure which
coincides with the pivotal structure on C.
We have an obvious forgetful functor F : Z(C) → C . To simplify the notation,
we will frequently omit it in the formulas, writing for example Hom C(Y,V ) in-
stead of Hom C(F (Y ),V ), for Y ∈ ObjZ(C), V ∈ Obj C. Note, however, that
if Y,Z ∈ ObjZ(C), then Hom Z(C)(Y,Z ) is diﬀerent from Hom C(Y,Z ): namely,
HomZ(C)(Y,Z ) is a subspace in Hom C(Y,Z ) consisting of those morphisms that
commute the with the half-braiding. The following lemma will be useful in the
future.
Lemma 2.2. LetY,Z ∈ ObjZ(C). Deﬁne the operator
P : Hom C(Y,Z ) → HomC(Y,Z ) by the following formula:
Pψ = 1
D2
∑
X∈Irr(C)
dX ψ
Y
Z
X
Then P is a projector onto the subspace HomZ(C)(Y,Z ) ⊂ HomC(Y,Z ).
Proof. It is immediate from the deﬁnition that if ψ ∈ HomZ(C)(Y,Z ), then Pψ =ψ .
On the other hand, using Lemma 1.1, we get that for any ψ ∈ HomC(Y,Z ), one has
TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT 7
(Pψ )ϕ Y =ϕ Z(Pψ ):
(Pψ )ϕ Y = 1
D2
∑
j
dj ψ
Y
Z
j
W
= 1
D2
∑
i,j
didj ψ
Y
Z
ϕ ϕ ∗
j
i
W
W
= 1
D2
∑
i
di ψ
Y
Z
i
W
=ϕ Z (Pψ ),
(as before, we are using convention (1.8)). □
The following theorem is a reﬁnement of [ENO2005, Proposition 5.4].
Theorem 2.3. Let F : Z(C) → C be the forgetful functor and I : C → Z(C) the
(left) adjoint of F : HomZ(C)(I(V ),X ) = Hom C(V,F (X)). Then for V ∈ Obj C,
one has
(2.1) I(V ) =
⨁
i∈Irr(C)
Xi ⊗V ⊗X ∗
i
with the half braiding given by
⨁
i,j ∈Irr(C)
√
di
√
dj
V
ϕ ϕ ∗
i
jW
i
j
W
Figure 5. Half-braiding I(V ) ⊗W →W ⊗I(V ).
Note that instead of normalizing factor √di
√
dj we could have used di or dj —
each of this would give an equivalent deﬁnition.
Proof. Denote Y = ⨁
i∈Irr(C)Xi ⊗V ⊗X ∗
i . It follows from Lemma 1.1 that the
morphismsY ⊗W →W ⊗Y deﬁned by Figure 5 satisfy the compatibility relations
8 BENJAMIN BALSAM AND ALEXANDER KIRILLOV, JR.
required of half braiding and thus deﬁne on Y a structure of an object of Z(C).
Now, deﬁne for any Z ∈ ObjZ(C), maps
HomZ(C)(Y,Z ) → HomC(V,Z )
Ψ ↦→Ψ ◦P0 =
Ψ
V
11
Z
where P0 is the embedding V = 1 ⊗V ⊗ 1 →Y = ⨁ Xi ⊗V ⊗X ∗
i and
HomC(V,Z ) → HomZ(C)(Y,Z )
Φ ↦→
⨁
i∈Irr(C)
√
di Φ
V
Z
i
It follows from Lemma 2.2 that these two maps are inverse to each ot her. Com-
position in one direction is easy. First suppose Φ ∈ HomC(V,Z ). The computation
is shown below.
Φ →
⨁
i
√
di Φ
V
Z
i
→ Φ.
The composition in opposite order is as follows:
Ψ → Ψ
V
11
Z
→
⨁
i
√
di Ψ
V
Z
i
11
=
⨁
i
√
di
√
dj Ψ
ϕ ϕ ∗
V
Z
i i
j∗
1
j
1
= Ψ
V
Z
The ﬁrst equality holds by functoriality of the half-braiding and Figur e 5. The
second equality is obvious. Therefore, the two maps are inverses t o one another
and we have Hom Z(C)(Y,Z ) = Hom C(V,Z ); thus, Y =I(V ). □
An easy generalization of Theorem 1.4 allows us to consider graphs in w hich
some of the edges are labeled by objects of Z(C).
Let ˆΓ be a graph which consists of a usual graph Γ embedded in S2 as in The-
orem 1.4 and a ﬁnite collection of non-intersecting oriented arcs γi such that end-
points of each arc γ are vertices of graph Γ, and each vertex has a neighborhood in
which arcs γi do not intersect edges of Γ; however, arcs γi are allowed to intersect
edges of Γ away from vertices. Note that this implies that for each v ertex v, we
TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT 9
have a natural cyclic order on the set of all edges of ˆΓ (including arcs γi) adjacent
to v.
Let us color such diagram, labeling each edge of Γ by an object of C, each arc
γ by an object of Z(C), and each vertex v by a vector ϕ v ∈ ⟨V ±(e1),...,V ±(en)⟩
wheree1,...,e n are edges of ˆΓ adjacent to v (including the arcs γi), and the signs
are chosen as in Theorem 1.4.
C
A B
D E
F
Figure 6. Diagram ˆΓ on the sphere and its ﬂattening to the plane.
Arc γ is shown by a double line.
As before, by removing a point from S2 and choosing a linear order of edges
(including the arcs) at every vertex, we get a diagram in the plane; h owever, now
the projections of arcs γi can intersect edges of Γ as shown in Figure 6. Let us
turn this into a tangle diagram by replacing each intersection by a pict ure where
the arch γi goes under the edges of Γ, as shown in Figure 6.
Such a diagram deﬁnes a number ZRT (ˆΓ) deﬁned in the usual way, with the
extra convention shown in Figure 4.
Theorem 2.4. The number ZRT (ˆΓ) ∈ k does not depend on the choice of a point
to remove from S2 orand thus deﬁnes an invariant of colored graphs on the spher e.
Moreover, this number is invariant under homotopy of arcs γi.
Proof. The fact that it is independent of the choice of point to remove and t hus
is an invariant of a graph on the sphere immediately follows from Theor em 1.4:
replacing every crossing by a coupon colored by half-braiding ϕ Y gives a graph as
in Theorem 1.4. Invariance under homotopy of arcs γ follows from compatibility
conditions on half-braiding shown in Figure 7.
□
Finally, we will need one more useful construction.
For any Y ∈ ObjZ(C), we deﬁne a functor functor C⊠n → Vec by
(2.2) ⟨V1,...,V n⟩Y = Hom C(1,Y ⊗V1 ⊗ · · · ⊗Vn)
10 BENJAMIN BALSAM AND ALEXANDER KIRILLOV, JR.
ϕ
...
...
= ϕ
...
...
Figure 7. Invariance under homotopy
for any collection V1,...,V n of objects of C. As before, we have functorial isomor-
phisms
(2.3) zY : ⟨V1,...,V n⟩Y ≃ ⟨Vn,V 1,...,V n−1⟩Y
obtained as composition
⟨Y,V 1,...,V n⟩ → ⟨Vn,Y,V 1,...,V n−1⟩ → ⟨Y,V n,V 1,...,V n−1⟩
(the ﬁrst isomorphism is the cyclic isomorphism (1.3), the second one is the inverse
of half-braiding ϕ Y ). Note however that in general we do not have zn
Y = id.
