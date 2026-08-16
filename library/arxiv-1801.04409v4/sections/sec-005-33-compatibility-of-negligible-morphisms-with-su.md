---
doc_id: arxiv-1801.04409v4
doc_title: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES"
section_id: sec-005-33-compatibility-of-negligible-morphisms-with-su
section_title: "Compatibility of negligible morphisms with surjective tensor functors"
section_number: 3.3
pages: 14-15
source_pdf: 1801.04409v4.pdf
source_sha256: db61d011e3775aca
doc_brief: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES — We develop the theory of semisimpliﬁcations of ten- sor categories deﬁned by Barrett and Westbury."
---
sor functors. Let C, D be ﬁnite spherical tensor categories ([EGNO],
Section 6), and F : C → D a surjective tensor functor ([EGNO], Sub-
section 6.3). Let I : D → C be the right adjoint of F . Note that I
is exact since F maps projectives to projectives, ([EGNO], Theorem
6.1.16).
Deﬁnition 3.18. The index of F is d := dimI(1).
Deﬁnition 3.19. Let us say that I is dimension-scaling if dimI(V ) =
d dimV for all V ∈ D .
Proposition 3.20. If F has a nonzero index and I is dimension-
scaling then
(i) dimF (Y ) = dim Y for all Y ∈ C ;
(ii) for any negligible morphism f in C, the morphism F (f ) is neg-
ligible in D.
Proof. We have a functorial isomorphism εY : I(F (Y )) → I(1) ⊗Y .
Indeed,
Hom(X,I (F (Y ))) = Hom(F (X),F (Y )) = Hom(F (X) ⊗F (Y )∗, 1) =
Hom(F (X ⊗Y ∗), 1) = Hom(X ⊗Y ∗,I (1)) = Hom(X,I (1) ⊗Y ).
Since I is dimension-scaling, we have
d dimF (Y ) = dim I(F (Y )) = dim(I(1) ⊗Y ) = d dimY.
Since d ⁄= 0, this implies (i).
Now let us prove (ii). For this, note that if f :X →Y is a morphism
in C thenεY ◦I(F (f )) ◦ε−1
X = IdI(1) ⊗f . Hence the morphism I(F (f ))
is negligible.
14
Lemma 3.21. If h : V → V is a morphism in D then one has
Tr(I(h)) = dTr(h).
Proof. By decomposing V into generalized eigenobjects of h, we may
assume that h has a single eigenvalue λ. Then h =λId +h0, where h0
is nilpotent, so I(h) = λId +I(h0). Since I(h0) is nilpotent, the desired
statement reduces to the identity dim I(V ) = d dimV for all V ∈ D ,
which holds since I is dimension-scaling. □
Now let g :F (Y ) →F (X) be a morphism. Then by Lemma 3.21,
dTr(F (f ) ◦g) = Tr(I(F (f ) ◦g)) = Tr(I(F (f )) ◦I(g)).
But this is zero, since I(F (f )) is negligible. Since d ⁄= 0, this implies
that Tr(F (f ) ◦g) = 0, i.e., F (f ) is negligible, yielding (ii). □
Proposition 3.20 immediately implies
Corollary 3.22. If F has a nonzero index and I is dimension-scaling
then F descends to a tensor functor F : C → D.
Now let H be an involutive ﬁnite dimensional Hopf algebra over any
algebraically closed ﬁeld k (i.e.,S2 = Id, where S is the antipode of H),
and K be a Hopf subalgebra in H; for example, H is cocommutative
(e.g., a group algebra). Then C = Rep H and D = Rep K are ﬁnite
spherical tensor categories, where dimensions are the usual dime nsions
(projected to k). Restriction from H to K deﬁnes a surjective tensor
functor F : C → D . Let I : Rep(K) → Rep(H) be the right adjoint to
this functor, i.e., the induction functor, I(V ) = HomK(H,V ).
Recall that by the Nichols-Zoeller theorem [NZ], H is a free K-
module, of some rank d.
Corollary 3.23. Assume that d ⁄= 0 in k. Then any negligible mor-
phism f : X → Y of H-modules is also negligible as a morphism of
K-modules. Thus, F deﬁnes a tensor functor: RepH → RepK.
Proof. We have dimI(V ) = d dimV , i.e., I is dimension-scaling. Thus,
