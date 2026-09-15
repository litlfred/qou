---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-016-43-symmetric-functions-and-bubbles
section_title: "Symmetric functions and bubbles"
section_number: 4.3
pages: 27-32
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a high er categorical level."
---
is remarkably rich. A prominent role is played by the non-nested dott ed bubbles of a ﬁxed orientation
since any closed diagram in the graphical calculus for UQ(sln) can be reduced to composites of such
diagrams.
There is a beautiful analogy between dotted bubbles in the graphica l calculus and various bases for
the ring of symmetric functions. In [37] it is shown that there is an is omorphism
ψλ : Sym − → Z(λ) = UQ(sl2)(1λ, 1λ)(4.35)
hr ↦→
i
/d15/d15/d77/d77
•
♠+r
λ
28 ANNA BELIAKOV A, ZAUR GULIYEV, KAZUO HABIRO, AND AARON D. L AUDA
(−1)ses ↦→
i
/d81/d81/d15/d15
•
♠+s
λ
where Sym denotes the ring of symmetric functions, hr denotes the complete symmetric function of
degree r, and es denotes the elementary symmetric function of degree s. In fact, under this isomor-
phisms the well known relationship between complete and elementary symmetric functions becomes
the inﬁnite Grassmannian equation (4.24).
It is well known that for a partition λ = (λ1,...,λ n) with λ1 ≥ λ2 ≥ · · · ≥ λn, products of
elementary symmetric functions eλ =eλ1...e λn form a basis for Sym, see for example [46]. Likewise,
products of complete symmetric functions also provide a basis for S ym. This mirrors the fact that any
closed diagram in the graphical calculus for UQ(sl2) can be reduced to a product on non-nested bubbles
of a given orientation.
In the sln calculus of the 2-category U(sln), we have the isomorphism
ψλ :
∏
i∈I
Sym − → Z(λ) = UQ(sln)(1λ, 1λ)
since any closed diagram can still be reduced to products of non-ne sted closed bubbles labelled by
i ∈I.
In what follows, it will be interesting to consider which products of clo sed diagrams correspond to
the basis of Sym given by the power sum pr symmetric functions. Using a formula that expresses power
sum symmetric functions in terms of products of complete and eleme ntary symmetric functions, we
can denote by pi,r(λ) for r> 0, the image of the power symmetric polynomial on i-labelled strands in
Z(λ):
(4.36)
pi,r(λ) :=
∑
a+b=r
(a + 1)
i
/d15/d15/d77/d77
•
♠+a
i
/d81/d81/d15/d15
•
♠+b
λ
= −
∑
a+b=r
(b + 1)
i
/d15/d15/d77/d77
•
♠+a
i
/d81/d81/d15/d15
•
♠+b
λ
= −
∑
a+b=r
a
i
/d15/d15/d77/d77
•
♠+b
i
/d81/d81/d15/d15
•
♠+a
λ
For later convenience we set pi,0(λ) = λi.
Exercise 18. Using the bubble slide formulas from exercise 17, show that
pi,r(λ) =



−
λ
/d80/d80/d15/d15
i
•
♠+r
/d15/d15/d79/d79
i
•
♠+0
if λi ≥ 0
λ
/d15/d15/d77/d77
i
•
♠+r
/d79/d79/d15/d15
i
•
♠+0
if λi ≤ 0,
so that the formulas deﬁning pr(λ) can be obtained by simplifying a degree r bubble with one orientation
nested inside of a degree zero bubble with the opposite orien tation.
TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR 29
Note that other interesting basis for symmetric functions also hav e natural graphical analogs. In
[34] diagrams corresponding to the basis of Schur functions are giv en.
Exercise 19. Using the bubble sliding equations from exercise 17, prove t he following power sum slide
rules
λ −αj
/d79/d79
j
pi,r(λ −αj) =



λ
/d79/d79
j
pi,r(λ) − 2
λ
/d79/d79
j
•r if i =j,
λ
/d79/d79
j
pi,r(λ) if i ·j = 0,
λ
/d79/d79
j
pi,r(λ) − (−t−1
ij tji)r
λ
/d79/d79
j
•r if i ·j = −1
(4.37)
λ
/d79/d79
j
pi,r(λ +αj) =



λ
/d79/d79
j
pi,r(λ) + 2
λ
/d79/d79
j
•r if i =j,
λ
/d79/d79
j
pi,r(λ) + ( −t−1
ij tji)r
λ
/d79/d79
j
•r if i ·j = −1
(4.38)
4.4. Kar , K0 and Tr for 2-categories. We can extend many of the constructions from section 3
deﬁned for (additive) linear categories to the 2-categorical sett ing. A 2-category C is linear if the
categories C(x,y ) are linear for all x,y ∈ Ob(C) and the composition functor preserves the linear
structure (see [10] for more details). Similarly, an additive linear 2-c ategory is a linear 2-category in
which the categories C(x,y ) are also additive and composition is given by an additive functor.
The following deﬁnitions extend the Karoubi envelope, split Grothen dieck group, and trace to the
2-categorical setting.
• Given an additive linear 2-category C, deﬁne the split Grothendieck group K0(C) of C to
be the linear category with Ob( K0(C)) = Ob( C) and with K0(C)(x,y ) := K0(C(x,y )) for
any two objects x,y ∈ Ob(C). For [ f ]∼= ∈ Ob(K0(C)(x,y )) and [ g]∼= ∈ Ob(K0(C)(y,z )) the
composition in K0(C) is deﬁned by [ g]∼= ◦ [f ]∼= := [g ◦f ]∼=.
• The trace Tr( C) of a linear 2-category is the linear category with Ob(Tr( C)) = Ob( C) and
with Tr( C)(x,y ) := Tr( C(x,y )) for any two objects x,y ∈ Ob(C). For σ ∈ EndC(x,y) and
τ ∈ EndC(y,z), we have [τ ] ◦ [σ] = [τ ◦σ]. The identity morphism for x ∈ Ob(Tr(C)) = Ob( C)
is given by [1 Ix].
• The Karoubi envelope Kar(C) of a linear 2-category C is the linear 2-category with Ob(Kar( C)) =
Ob(C) and with hom categories Kar( C)(x,y ) := Kar( C(x,y )). The composition functor
Kar(C)(y,z ) × Kar(C)(x,y ) → Kar(C)(x,z ) is induced by the universal property of the
Karoubi envelope from the composition functor in C. The fully-faithful additive functors
C(x,y ) → Kar(C(x,y )) combine to form an additive 2-functor C → Kar(C) that is universal
with respect to splitting idempotents in the Hom-categories C(x,y ).
30 ANNA BELIAKOV A, ZAUR GULIYEV, KAZUO HABIRO, AND AARON D. L AUDA
For categoriﬁcation using K0 it is necessary to consider the 2-category Kar( U(sln)). We will denote
by ˙U the Karoubi envelope of U.
The homomorphisms hC(x,y) taken over all objects x,y ∈ Ob(C) give rise to a linear functor
(4.39) hC : K0(C) → Tr(C)
which is the identity map on objects and sends K0(C)(x,y ) → Tr(C)(x,y ) via the homomorphism
hC(x,y). It is easy to see that this assignment preserves composition since
hC([g]∼= ◦ [f ]∼=) = hC([g ◦f ]∼=) = [1 g◦f ] = [1 g ◦ 1f ] = [1 g] ◦ [1f ] = hC([g]∼=) ◦hC([f ]∼=).(4.40)
In the following sections we study the trace and K0 for the 2-categories ˙U(sln).
4.5. Two categoriﬁcations of Lusztig’s integral form A ˙U(sl2). Here we present the results of
[37, 34] computing K0 and of [8] computing Tr of U(sl2).
The algebra A ˙U(sl2) has a well-known basis, called Lusztig’s canonical basis B consisting of
(i) E(a)F (b)1n for a,b ≥ 0, n ∈ /CI , n ≤b −a,
(ii) F (b)E(a)1n for a,b ≥ 0, n ∈ /CI , n ≥b −a,
where E(a)F (b)1b−a =F (b)E(a)1b−a. Let mBn be set of elements in B belonging to 1 m(A ˙U)1n.
We associate to each x ∈ B a 1-morphism in ˙U as follows:
x ↦→ E(x) :=
{ E (a)F (b)1n if x =E(a)F (b)1n,
F (b)E (a)1n if x =F (b)E(a)1n.
Let B = {E(x) |x ∈ B} and mBn = {E(x) |x ∈ mBn}.
The ﬁrst categoriﬁcation of A ˙U was given in [37] where the decategoriﬁcation functor is given by
K0. The original proof worked with the 2-category ˙U(sl2) deﬁned over a ﬁeld /CZ , so that spaces of
2-morphisms formed vector spaces and the Krull-Schmidt propert y could be utilized. In rank one the
choice of scalars Q does not enter the deﬁnition. Later this result was enhanced in [34] to prove the
result when working over the integers. Unique decomposition for sp aces of 2-morphisms follows as a
corollary of these results, implying that the category U
/CI
(sl2) is Krull-Schmidt. Very recently, it was
shown in [8] that ˙U
/CI
also categoriﬁes A ˙U via the alternative trace decategoriﬁcation functor Tr.
Theorem 4.2. ([34], [8]) For sl2, B is the strongly upper triangular basis of ˙U
/CI
. The maps
γ : A ˙U − → K0( ˙U
/CI
)
x ↦→ [E(x)]∼=
and h ˙U
/CI
: K0( ˙U
/CI
) − → Tr(U
/CI
)
x ↦→ [1x]
are isomorphisms of graded linear categories, providing two catego riﬁcations of A ˙U.
4.5.1. Strategy of the Proof. In section 6 of [8], based on the results of [34] we give an explicit prese n-
tation of the subcategory ˙U(n,m )
/CI
|mBn by generators and relations, which shows that this category
is strongly upper triangular. Hence, the indecomposable 1-morphis ms from B generates K0 and, by
Proposition 3.9, also Tr as /CI [q,q −1]-modules. In [34] explicit isomorphisms in ˙U
/CI
are given lifting the
the deﬁning relations of A ˙U, showing that γ is an isomorphism of graded categories. Since the functor
h ˙U :K0( ˙U
/CI
) → Tr( ˙U
/CI
) preserves composition. Finally, we use that Tr( ˙U) = Tr(U), the result follows.
4.6. Two categoriﬁcations of A ˙U(sln). Here we present the results of [33] computing K0 and of [7]
computing Tr for general n.
There is a special choice of scalars, where all ti j = 1 for 1 ≤i < n− 1. In this case, the graphical
calculus is cyclic with respect to the biadjoint structure, so that iso topic diagrams represent the same
2-morphism. This will be our default choice of Q in sections unless explicitly stated otherwise. We will
omit explicitly mentioning Q in the notation when no confusion is likely to arise.
TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR 31
Theorem 4.2 was possible because the explicit isomorphisms construc ted in [34] provide decompo-
sitions of arbitrary 1-morphisms into indecomposables. However, t he lack of an explicit description
of the canonical basis for A ˙U beyond sl2 presents an obstacle to generalizing this result beyond sl2.
However, if one works with the 2-category U(sln) deﬁned over a ﬁeld /CZ of characteristic 0, then one
can utilize various connections between this category and known ge ometric constructions to prove the
following result.
Theorem 4.3. ([33], [7]) Let /CZ be a ﬁeld of characteristic 0. For sln, the 2-category ˙U is strongly
upper triangular (see Remark 15). Moreover,
K0( ˙U ) = A ˙U
as graded linear categories and
Tr(U) = K0( ˙U ) ⊗
/CI
/CZ , HHi(U) = 0 for i> 0.
Following a recommendation of the ﬁrst author, the sl3 case of this theorem was studied in [65].
4.6.1. Strategy of the Proof. Let us make few remarks about the proof. The result about K0 was proved
in [33]. It relies on the fact that ˙U is Krull-Schmidt. To control the size of K0 an action of ˙U was
deﬁned on the cohomology rings of partial ﬂag varieties. Even when for n > 2, the explicit form of
the Lusztig canonical basis is not known, but the results of [61] and [63] allows us to deduce that ˙U is
strongly upper triangular. The full argumentation will be given in [7].
4.6.2. Applications. In [40, 54] it was shown that sln link homology theories can be obtained from
˙U(slm) by means of the so-called foamation functors F , ﬁrst studied in [48]. More precisely, there is an
extended version 2BFoam of the Bar-Natan foam category introd uced by Blanchet [9]. (The advantage
of Blanchet’s version is that it is functorial with respect to link cobor disms, when Bar-Natan version is
functorial up to sign.) In [40, 54] an analog nBFoam of the Blanchet foam category for sl2 is deﬁned for
sln and families of 2-representations F for were deﬁned from ˙U (slm) into the foam categories nBFoam.
A general procedure was laid out by Cautis [17] using categorical sk ew Howe duality to pull back
complexes associated to a tangle to a complex in Kom( ˙U). Combining this with the foamation functors
allows one to pull back the complexes of foams associated to a tangle to a complex in Kom( ˙U). It
was shown that all of the foam relations used for sln-link homology arise from relations in ˙U (slm)
via foamation functors. These foamation functors categorify a s kew Howe functor deﬁned at the
decategoriﬁed level by Cautis, Kamnitzer, and Morrison that realiz e web relations from relations in
the quantum group ˙Uq(slm) [18].
Recall that we have two ﬂavors of Euler characteristic associated with K0 and Tr,
χtr : Kom(F( U)) → Tr(F(U))
χ : Kom(F( ˙U)) → K0(F( ˙U )).
Below is one of the applications of Theorem 4.3.
Corollary 4.4. In sln link homologies theories, we have
χtr =χ.
Remark 20. The sl2 case of Corollary 4.4 was ﬁrst proven by Cooper-Krushkal [21, Sec tion 3].
Proof. Let C :=F ( ˙U(slm)). We have the Chern character map hC :K0(C) → Tr(C) sending [x]∼= → [1x].
The induced map χ →χtr is surjective, since χtr uses trace classes of the identity maps only. It remains
to show that this map is injective. Note that K0( ˙U) is freely generated by indecomposables and h ˙U is
an isomorphism after tensoring with any ﬁeld of zero characteristic by Theorem 4.3, so h ˙U is injective.
Hence, F (K0( ˙U )) = F (h ˙U (K0( ˙U ))). The fact that any linear functor commutes with K0 implies the
result. □
32 ANNA BELIAKOV A, ZAUR GULIYEV, KAZUO HABIRO, AND AARON D. L AUDA
