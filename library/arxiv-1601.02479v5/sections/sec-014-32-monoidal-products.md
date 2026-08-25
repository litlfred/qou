---
doc_id: arxiv-1601.02479v5
doc_title: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras"
section_id: sec-014-32-monoidal-products
section_title: "Monoidal products"
section_number: 3.2
pages: 28-32
source_pdf: 1601.02479v5.pdf
source_sha256: 52c2dcd4adf2e72b
doc_brief: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras — This paper concerns the cohomological aspects of Donaldson – Thomas theory for Jacobi algebras and"
---
erties of the categoriﬁcation of the quantum torus from reﬁned D T theory.
Deﬁnition 3.4. Let F ∈ D (MMHM(X)) for X a scheme. We say that F is locally
ﬁnite if for each Z ∈π 0(X)
(1) for each n ∈ Z, the element ⨁
i∈Z GrW
n (Hi(F )|Z ) belongs to Db(MMHM(Z))
(2) For n ≪ 0, we have GrW
n (Hi(F )|Z ) = 0 for all i ∈ Z.
Denote by D≥,lf (MMHM(X)) ⊂ D ≥(MMHM(X)) the full subcategory of locally
ﬁnite objects.
The category D≥,lf (MMHM(NQ0 )) is going to play the role of the categoriﬁcation
of the motivic quantum torus of [28, Sec.6.2]. For now we remark that this quantum
torus is a power series ring with coeﬃcients in Z((q1/2)) and variables xd for d ∈
NQ0 , and if ζ is a generic stability condition then the subring of power series in
variables xd for d ∈Λζ
µ is commutative, while the whole quantum torus in general
is not. The categoriﬁcation of this picture, then, should be a monoid al category, for
which the monoidal product cannot be upgraded to a symmetric mon oidal product,
except on ﬁxed subcategories indexed by the slope µ , for which we should deﬁne a
symmetric monoidal product.
The moduli scheme Mζ -ss
µ carries a symmetric monoidal structure given by the
direct sum, and the product
Mζ -ss
µ × Mζ -ss
µ
⊕
− → Mζ -ss
µ
is a ﬁnite morphism of schemes (see [35, Lem.2.1]). By Remark 2.10 the c ategory
D≥,lf (MMHM(Mζ -ss)) carries a monoidal product
F ⊠⊕ G := ⊕∗(π ∗
1F ⊗π ∗
2G)
deﬁned as in (27).
Proposition 3.5. The monoidal product ⊠⊕ is biexact and preserves the weight
ﬁltration.
COHAS AND QUANTUM ENVELOPING ALGEBRAS 29
Proof. Let F ∈ MMHM(X) and G ∈ MMHM(Y ) for two algebraic varieties X and
Y . We deﬁne their external tensor product
F ⊠ G := (p : X × Y × A1 × A1 idX×Y ×+
− − − − − − − →X × Y × A1)∗(pr∗
1,3 F ⊗ pr∗
2,4 G).
as in Remark 2.10. Then by [30, Lem.1], there is an isomorphism in D(MMHM(X ×
Y ))
p!
(
pr∗
1,3 F ⊗ pr∗
2,4 G
)
→ p∗
(
pr∗
1,3 F ⊗ pr∗
2,4 G
)
and so since p! : D(MHM(X × A1 × Y × A1)) → D (MHM(X × Y × A1)) is left exact,
and decreases weights, while p∗ is right exact and increases weights, we deduce that
the external tensor product
⊠ : D(MMHM(X)) × D(MMHM(Y )) → D (MMHM(X × Y ))
is exact and preserves weights.
Since the map ⊕ : Mζ -ss
µ × Mζ -ss
µ → Mζ -ss
µ is ﬁnite, the direct image functor ⊕∗
is exact and preserves weights. The result follows. □
The monoidal unit in D≥,lf (MMHM(Mζ -ss)) is QMζ -ss
0
, the constant pure Hodge
module supported on Mζ -ss
0 ∼
= pt, the unit of the monoid Mζ -ss
µ .
We brieﬂy summarize the results of Maxim, Saito and Sch¨ urmann [34 ], dealing
with exterior products and symmetric group actions on mixed Hodge modules. Let
Xi, i ∈ I be a ﬁnite set of algebraic varieties, let Li be objects of D≥,lf (MHM(Xi))
for each i ∈ I, and let fi : Xi → Yi be a set of morphisms of algebraic varieties.
Set f =∐
i∈I fi. While [34] treats the bounded derived category, and certainly it
makes no sense to apply their results at the generality of the unbou nded derived
category, their arguments extend without modiﬁcation to the cas e of the categories
D≥,lf (MHM(Xi)). They show that external tensor product commutes with the
direct image, that is, there is a natural isomorphism
⊠i∈I fi,∗Li ∼
= f∗ (⊠i∈ILi) .
Furthermore, if Xi = X for all i, and Yi = Y for all i, then there is an action of the
symmetric group SI on both external products, which is respected by the above
natural isomorphism.
Remark 3.6. This is the usual action, incorporating the Koszul sign rule — when
we consider cohomological Hall algebras later, we will have cause to modify this ac-
tion, to express commutativity results for the cohomologic al Hall algebra. However,
for the purposes of Theorems A and B we may equivalently use th e default action
of [34] as we are only interested in the isomorphism classes of under lying objects
(see Proposition 6.2).
Now let Li = L for all i, and let I = {1, . . . , n}. The authors then deﬁne
Symn(L) := (̟∗ ⊠n L)Sn , where ̟ : X n → Symn X is the natural map, and show
that there is a canonical isomorphism
H(Symn X, Symn L) ∼
= Symn(H(X, L)).
Furthermore, they show that the Kunneth isomorphism
H(X n, ⊠nL) ∼
=
n⨂
H(X, L)
is an isomorphism of Sn-representations.
30 BEN DA VISON AND SVEN MEINHARDT
Now let L ∈ D ≥,lf (MMHM(X)). Since there is a commutative diagram
(X × A1)n
̟X×A1
/d15/d15
idn
X ×+ /d47/d47
X n × A1
̟X ×idA1
/d15/d15
Symn(X × A1) r /d47/d47 Symn X × A1
we obtain a Sn-action on ̟X,∗(⊠nL) by taking r∗ of the action deﬁned in [34],
and we can deﬁne Sym nL to be the Sn-invariant summand. Similarly, we deﬁne
the functor
Symn
⊠⊕ : D≥,lf (MMHM(Mζ -ss
µ )) → D ≥,lf (MMHM(Mζ -ss
µ ))
F ↦→(⊕∗F ⊠n)Sn.
We then deﬁne
Sym⊠⊕ : D≥(MMHM(Mζ -ss
µ \ Mζ -ss
0 )) → D ≥(MMHM(Mζ -ss
µ ))(47)
F ↦→
⨁
n≥0
Symn
⊠⊕ F .
This functor is well deﬁned, since
π 0(⊕) :π 0(M) ×π 0(M) →π 0(M)
has ﬁnite ﬁbers. The same fact implies the following lemma:
Lemma 3.7. The functor (47) restricts to a functor
Sym⊠⊕ : D≥,lf (MMHM(Mζ -ss
µ \ Mζ -ss
0 )) → D ≥,lf (MMHM(Mζ -ss
µ )).
Proposition 3.8. The functor Sym⊠⊕ takes pure objects to pure objects.
Proof. Let F ∈ MMHM(Mζ -ss
µ ) be pure. Let
⊕n : Mζ -ss
µ × . . . × Mζ -ss
µ → Mζ -ss
µ
be the n-fold monoid map. Then ⊕n is ﬁnite by [35, Lem.2.1], and so
G = ⊕n
∗ (F ⊠ . . . ⊠ F ) ∈ MMHM(Mζ -ss
µ )
is pure. On the other hand, Sym n
⊠⊕ F ⊂ G is the isotrivial direct summand under
the Sn-action, and is therefore pure. We deduce that Sym ⊠⊕ F is a direct sum of
pure objects, and is therefore pure. □
We deﬁne a new monoidal structure on D≥,lf (MMHM(Mζ -ss)) by setting
(48) F ⊠tw
⊕ G :=
⨁
d′,d′′∈NQ0
L⟨d′′,d′⟩/2 ⊗ (⊕∗(Fd′ ⊠ Gd′′ )) ,
where F =⨁
d′∈NQ0 Fd′ for Fd′ ∈ D (MMHM(Mζ -ss
d′ )) and G =⨁
d′′∈NQ0 Gd′′ for
Gd′′ ∈ D (MMHM(Mζ -ss
d′′ )). Since we are twisting by a pure twist, this monoidal
product again preserves weights. If ζ isµ -generic, the restriction of ⊠tw
⊕ to D≥(MMHM(Mζ -ss
µ ))
is naturally isomorphic to the untwisted symmetric monoidal product ⊠⊕, but in
general there is no symmetrizing natural isomorphism of bifunctor s making ⊠tw
⊕
into a symmetric monoidal product.
The associator natural isomorphism for the monoidal structure ⊠⊕ is the one
induced from the usual monoidal structure on the derived catego ries of constructible
sheaves and D-modules. We have to take some care in deﬁning the signs for the
COHAS AND QUANTUM ENVELOPING ALGEBRAS 31
associator for ⊠tw
⊕ . Let F (h) ∈ D ≥,lf (MMHM(Mζ -ss
d(h) )) for h = 1, 2, 3. Consider the
composition of natural transformations
ηF (1),F (2),F (3) : L⟨d(3) + d(2),d(1)⟩/2 ⊗
(
F (1) ⊠⊕
(
L⟨d(3),d(2)⟩/2 ⊗ (F (2) ⊠⊕ F (3))
))
∼
=− →L⟨d(3) + d(2),d(1)⟩/2+⟨d(3),d(2)⟩ ⊗
(
F (1) ⊠⊕
(
F (2) ⊠⊕ F (3)
))
∼
=− →L⟨d(3) + d(2),d(1)⟩/2+⟨d(3),d(2)⟩/2 ⊗
((
F (1) ⊠⊕ F (2)
)
⊠⊕ F (3)
)
∼
=− →L⟨d(3),d(2) + d(1)⟩/2 ⊗
(
L⟨d(2),d(1)⟩/2 ⊗
(
F (1) ⊠⊕ F (2)
)
⊠⊕ F (3)
)
The resulting natural isomorphism F (1) ⊠tw
⊕ (F (2) ⊠tw
⊕ F (3)) → (F (1) ⊠tw
⊕ F (2)) ⊠tw
⊕
F (3)) does not satisfy the pentagon identity. We deﬁne instead
(49) η′
F (1),F (2),F (3) := (−1)⟨d(2),d(3)⟩χ (d(1),d(1))ηF (1),F (2),F (3)
to produce a valid associator natural isomorphism.
In a little more detail, the diagram
((F (1) ⊠tw
⊕ F (2)) ⊠tw
⊕ F (3)) ⊠tw
⊕ F (4)
α/d115/d115❢❢❢❢❢❢❢❢❢❢❢❢❢❢❢❢❢❢❢❢❢❢
δ
/d15/d15
(F (1) ⊠tw
⊕ (F (2) ⊠tw
⊕ F (3))) ⊠tw
⊕ F (4)
β
/d15/d15
(F (1) ⊠tw
⊕ F (2)) ⊠tw
⊕ (F (3) ⊠tw
⊕ F (4))
ǫ
/d15/d15
F (1) ⊠tw
⊕ ((F (2) ⊠tw
⊕ F (3)) ⊠tw
⊕ F (4))
γ /d47/d47
F (1) ⊠tw
⊕ (F (2) ⊠tw
⊕ (F (3) ⊠tw
⊕ F (4)))
(50)
fails to commute if the morphisms are all deﬁned using η•,•,•. The trouble is in
the deﬁnition of δ: in swapping L⟨d(4),d(3)⟩/2 with ( F (1) ⊠tw
⊕ F (2)) we pick up an
extra sign ( −1)⟨d(4),d(3)⟩⟨d(2),d(1)⟩ because of the half Tate twist in the deﬁnition of
(F (1) ⊠tw
⊕ F (2)). Modifying all of the morphisms in (50) via the rule (49) introduces
an overall parity change of
⟨d(2), d(3)⟩χ(d(1), d(1)) + ⟨d(2) + d(3), d(4)⟩χ(d(1), d(1))
+⟨d(3), d(4)⟩χ(d(2), d(2)) + ⟨d(3), d(4)⟩χ(d(1) + d(2), d(1) + d(2))
+⟨d(2), d(3) + d(4)⟩χ(d(1), d(1)) = ⟨d(4), d(3)⟩⟨d(2), d(1)⟩ (modulo 2)
as required. The terms in the sum are the contributions from α ,β ,γ ,δ, ǫ respec-
tively. We extend η′
•,•,• via linearity to triples of objects in D≥,lf (MMHM(Mζ -ss))
to deﬁne the associator natural isomorphism for the monoidal str ucture ⊠tw
⊕ .
We deﬁne the monoidal product on D≥,lf (MMHM(NQ0 )) by setting
(51) F ⊠tw
+ G :=
⨁
d′,d′′∈NQ0
L⟨d′′,d′⟩/2 ⊗ (+∗(Fd′ ⊠ Gd′′ ))
and constructing the associator natural isomorphism as in (51). T he map
dim∗ : D≥,lf (MMHM(Mζ -ss)) → D ≥,lf (MMHM(NQ0 ))
is a monoidal functor, and the restriction
dimµ ,∗ : D≥,lf (MMHM(Mζ -ss
µ )) → D ≥,lf (MMHM(Λζ
µ ))
is a symmetric monoidal functor for ζ-genericµ .
32 BEN DA VISON AND SVEN MEINHARDT
Remark 3.9. By skew symmetry of ⟨•, •⟩Q and ﬁniteness of the maps of schemes
⊕ and +, there are natural isomorphisms of bifunctors
Dmon(F ⊠tw
⊕ G) ∼
= DmonG ⊠tw
⊕ DmonF
Dmon(F ⊠tw
+ G) ∼
= DmonG ⊠tw
+ DmonF .
Note the swap of arguments.
