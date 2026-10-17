---
doc_id: arxiv-2010.12445v1
doc_title: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION"
section_id: sec-005-12-generalized-frame-bundles
section_title: "Generalized frame bundles"
section_number: 1.2
pages: 6-10
source_pdf: 2010.12445v1.pdf
source_sha256: 16e9ca22ecc1f296
toc_source: outline
doc_brief: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION — Given a quasi-compact category ﬁbered in groupoids X and a monoidal subcat- egory C of its category of locally free sheaves Vect(X), we are"
---
Generalized frame bundles. In this section we study frame bundles of general vector
bundles. We ﬁx a category X ﬁbered in groupoids over R.
Deﬁnition 1.8. Given a subset K ⊆N we set
D(K) =
G
n∈K
Spec R
and denote by Q(K) the vector bundle on D(K) which is free of rank n over the copy of Spec R
corresponding to n ∈K. More generally given a collection K∗: I →P(N), where P(N) is the
set of subsets of N, we set D(K∗) = Q
i D(Ki) as a sheaf over R.
Let E ∈Vect(X) be a locally free sheaf on X. We set
ranks(E) = {n ∈N | ∃s: Spec L →X with rk s∗E = n}, D(E) = D(ranks(E)), Q(E) = Q(ranks(E))
There is a map rE : X →D(E), the rank function, and we set
Fr(E) = IsoX (E, r∗
EQ(E)) →X
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION
7
If I is a set and E∗: I →Vect(X) is a collection of vector bundles we set D(E∗) = D(ranks(E∗)) =
Q
i D(Ei) and Fr(E∗) = Q
i Fr(Ei), where the products are taken over R and X respectively.
Remark 1.9. The scheme D(K), thought of as a sheaf, is the constant sheaf associated with K.
Instead D(K∗) as sheaf Aﬀ/R →(Sets) is
D(K∗)(U) = {s: U →
Y
i∈I
Ki with locally constant factors U →Ki}
The map X →D(E∗) maps ξ : U →X to the map Q
i rk(ξ∗Ei): U →Q
i∈I ranks(Ei).
Remark 1.10. The scheme D(K) is aﬃne if and only if K is ﬁnite. If K∗: I →P(N) is a collection
such that all the Ki are ﬁnite, then D(K∗) →Spec R is also aﬃne and faithfully ﬂat. This is the
case, for instance, if X is quasi-compact and K∗= ranks(E∗). Otherwise D(K∗) is just thought
of as a sheaf over R.
Lemma 1.11. Let K∗: I →P(N) be a map and ni ∈Ki for all i. Then the map Spec R →
D(K∗) given by the constant function (ni)i : Spec R →Q
i∈I Ki is a closed immersion and
representable by localizations of aﬃne schemes. In particular if E∗: I →Vect(X) is a collection
of vector bundles then the locus X ′ →X where the sheaves Ei have rank ni enjoys the same
property.
Proof. Let Spec B →D(K∗) be any map, given by locally constant functions hi : Spec B →Ki.
Set Z = Spec B ×D(K∗) Spec R.
We have to show that Z →Spec B is a closed immersion
and a localization. By deﬁnition of ﬁber product we see that Z is the locus in Spec B where
the hi are constant and equal to ni. In other words if Ui = h−1
i (ni) then Z = ∩iUi. Notice
that any intersections of the Ui is an open and closed subscheme of Spec B and, in particular, a
localization. Since Z can be written as a ﬁltered intersection of open and closed subsets of Spec B,
it is elementary to check that Z →Spec B is both a closed immersion and a localization.
□
Proposition 1.12. Let K ⊆N. The stack BD(K) GL(Q(K)) →D(K) is equivalent to the stack
over D(K) whose ﬁber over a Spec B →D(K), given by h: Spec B →K, is the groupoid of
locally free sheaves on Spec B that have rank n on h−1(n) for all n ∈K.
Let K∗: I →P(N) and
G =
Y
i
GL(Q(Ki)) =
Y
i
(GL(Q(Ki)) ×D(Ki) D(K∗)) →D(K∗)
where the products are taken over R and D(K∗) respectively. Then G →D(K∗) is an aﬃne and
faithfully ﬂat relative group scheme and the stack BD(K∗) G →D(K∗) is equivalent to the stack
over D(K∗) whose ﬁber over a Spec B →D(K∗), given by hi : Spec B →Ki, is the groupoid of
(Gi)i where Gi is a locally free sheaf on Spec B that have rank n on h−1(n) for all n ∈Ki.
Proof. The ﬁrst statement reduced easily to the case of GLn. For the second part set Gi =
GL(Q(Ki)) ×D(Ki) D(K∗). Everything follows because G = Q
i Gi and therefore
BD(K∗) G =
Y
i
BD(K∗) Gi
where the products are taken over D(K∗).
□
Lemma 1.13. Let E ∈Vect(X). Then there is a Cartesian diagram
Fr(E)
D(E)
X
BD(E)(GL(Q(E)))
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION
8
where X →BD(E) GL(Q(E)) is induced by E as in 1.12. In particular Fr(E) →X is a torsor
under the aﬃne group scheme GL(Q(E)) →D(E) and it is aﬃne, smooth and surjective.
Let E∗: I →Vect(X) be a collection of sheaves and consider G = Q
i GL(Q(Ei)) →Q
i D(Q(Ei)) =
D(E∗). Then there is a Cartesian diagram
Fr(E∗)
D(E∗)
X
BD(E∗)(G)
where X →BD(E∗) G is induced by the (Ei)i as in 1.12. In particular Fr(E∗) →X is aﬃne and
faithfully ﬂat as well.
Proof. It follows from the deﬁnition of Fr and the description in 1.12.
□
Lemma 1.14. Let E be a locally free sheaf on X of rank n and set V for the free R-module of
rank n with basis v1, . . . , vn. Then the map
γ : det E →Symn(V ⊗E), γ(x1 ∧· · · ∧xn) =
X
σ∈Sn
(−1)σ Y
k
(vσ(k) ⊗xk)
is well deﬁned and has locally free cokernel. In particular its dual Symn(V ⊗E)∨→det E∨is
surjective. Moreover, if E is free with basis e1, . . . , enthen e1 ∧· · · ∧en ∈det E is sent to the
determinant of the matrix (vi ⊗ej)ij, which lies in Symn(V ⊗E).
Proof. Consider the lift ˜γ : E⊗n →(V ⊗E)⊗n →Symn(V ⊗E) of γ.
This is certainly well
deﬁned. In order to show that it factors through the quotient det E, so that γ would be well
deﬁned, we can assume that E is free with basis e1, . . . , en. Set yij = vi ⊗ej ∈V ⊗E and
eω = eω(1) ⊗· · · ⊗eω(n) ∈E⊗n for any map ω: {1, . . . , n} →{1, . . . , n}. We have
˜γ(eω) =
X
σ∈Sn
(−1)σ Y
k
yσ(k)ω(k) = det(yi,ω(j))
It follows that eγ(eω) = 0 if ω is not a permutation, that eγ(eτω) = −eγ(eω) if τ is a transposition
and that eγ(eid) = det(vi ⊗ej), as required.
We now show that the cokernel of γ is locally free. This is equivalent to the surjectivity of
Symn(V ⊗E)∨→det E∨and it can be check locally. Consider e: Symn(V ⊗E) →R given by
e(yij) = δij, the Kronecker symbol. We see that the composition det E →Symn(V ⊗E)
e
−→R
maps e1 ∧· · · ∧en →det(I) = 1, where I = (δij) is the identity matrix.
□
Lemma 1.15. Let E be a vector bundle on a ﬁbered category X over R then:
1) the sheaf det E is a quotient of a direct sum of the E⊗m for m ∈N;
2) if X is deﬁned over Q then (Symq E)∨is a quotient of (E∨)⊗q.
3) the sheaf Symq(E ⊗M)∨, for a locally free R-module M, is a quotient of a direct sum of
ﬁnite tensor products of the Syma(E)∨for a ∈N.
Proof. We can assume that X is a Zariski stack. Set I = ranks(E) and denote by Xn for n ∈I
the locus in X where E has rank n, so that ⊔nXn = X.
1). There are surjective maps
M
n∈I
E⊗n →
M
n∈I
(E⊗n)|Xn →
M
n∈I
det(E|Xn) ≃det E
2) There is a surjective map
(E∨)⊗q →Symq(E∨) ≃(Symq E)∨
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION
9
3) Write M ⊕N = Rl. We use the formula
Symq(A ⊕B) =
M
u+v=q
Symu(A) ⊗Symv(B)
We have
Symq(E ⊗Rl) = Symq(E ⊗M) ⊕P =⇒Symq(E ⊗Rl)∨։ Symq(E ⊗M)∨
Moreover Symq(E ⊗Rl)∨can be written as a quotient of a direct sum of ﬁnite tensor products
of theSyma(E)∨for a ∈N.
□
Lemma 1.16. Let I be a set and E∗: I →Vect(R) be any map. Set
GL(E∗) =
Y
i∈I
GL(Ei) →Spec R
and Fi for the locally free sheaf on B GL(E∗) coming from the universal one on B GL(Ei), that
is the R-module Ei with the natural action of GL(Ei). Consider the following sets:
R1 = {det Fi, (Symm Fi)∨}i∈I,m∈N, R2 = {Fi, (Symm Fi)∨}i∈I,m∈N, R3 = {Fi, F∨
i }i∈I
Then the subcategory of Vect(B GL(E∗)) consisting of all tensor products of sheaves in R1 (resp.
R2) generates QCoh(B GL(E∗)).
If R is a Q-algebra then we can replace (Symm Fi)∨by F∨
i in the statement above.
Proof. Denote by C ⊆QCoh(B GL(E∗)) the full subcategory generated by the sheaves Ri in the
statement (here i can be 1, 2, 3 depending on the hypothesis). We have to show that C generates
QCoh(B GL(E∗)), so that, a posteriori, C = QCoh(B GL(E∗)). We claim that R[GL(E∗)] is a
direct limit of representations whose dual belongs to C. By [Ton20, Prop 8.2] this will ends the
proof.
The representation R[GL(E∗)] is a direct limit of tensor products of the regular representations
R[GL(Ei)] for i ∈I. This allows us to reduce to the case of GL(E) when E is a vector bundle
on E (i.e. I has one element). Call F the universal locally free sheaf on B GL(E), that is F = E
with the action of GL(E). Recall that for any locally free representation H of R[GL(E)] there is
a canonical isomorphism of R-modules HomGL(E)(H, R[GL(E)]) ≃H∨(see [Ton20, Rem 8.1]) So
there are equivariant maps
F ⊗HomGL(E)(F, R[GL(E)]) ≃F ⊗E∨→R[GL(E)]
and, for m ∈N,
(det F)−⊗m ⊗HomGL(E)((det F)−⊗m, R[GL(E)]) ≃(det F)−⊗m ⊗(det E)⊗m →R[GL(E)]
Consider the equivariant maps
Am = [
2mn
M
q=0
Symq(F ⊗E∨)] ⊗[(det F)−⊗m ⊗(det E)⊗m] −→R[GL(E)] ⊗R[GL(E)] →R[GL(E)]
We claim that those maps are injective and their images form an increasing sequence of sub
representations saturating R[GL(E)]. This statement is local, so we can assume E = On
X , so that
GL(E) = GLn. As usual we can write R[GLn] = R[Xuv]det for 1 ≤u, v ≤n, where det is the
determinant polynomial. In this case F ⊗E∨→R[GLn] is an isomorphism onto the R-submodule
generated by all the Xu,v, while (det F)−⊗m ⊗(det E)⊗m →R[GL(E)] is an isomorphism onto
the R-submodule generated by det−m. Thus Am →R[GLn] is an isomorphism onto the set of
fractions f/ detm where f is a polynomial of degree less or equal to 2nm. It is now easy to see
that ∪mAm = R[GLn].
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION
10
We come back to the general setting. We need to show that A∨
m ∈C for all m. The last
statement follows from the ﬁrst thanks to 1.15, 2). Since C is closed under tensor product and
direct sum, we have to show that
(Symq(F ⊗E∨))∨for q > 0, (det F ⊗det E−1) ∈C
For the ﬁrst sheaf it follows from 1.15, 3). For the second, since det E−1 is a quotient of a free
R-module, it is enough to show that det F ∈C. For R1 is clear. For R2 we use 1.15, 1).
□
