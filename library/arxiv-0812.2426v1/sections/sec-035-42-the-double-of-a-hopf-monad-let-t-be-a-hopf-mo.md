---
doc_id: arxiv-0812.2426v1
doc_title: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS"
section_id: sec-035-42-the-double-of-a-hopf-monad-let-t-be-a-hopf-mo
section_title: "The double of a Hopf monad. Let T be a Hopf monad on an autonomous"
section_number: 4.2
pages: 14-16
source_pdf: 0812.2426v1.pdf
source_sha256: df1eb953bc2c6c63
doc_brief: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS — A theorem of M¨ uger asserts that the center Z(C) of a spherical k-linear category C is a modular category if k is an algebraically closed ﬁeld"
---
category C. Assume T is centralizable, that is, such that the coend:
ZT (X) =
∫ Y ∈C
∨T (Y ) ⊗X ⊗Y
exists for every object X of C. Denote iX,Y : ∨T (Y )⊗X ⊗Y →ZT (X) the associated
universal dinatural transformation. By the parameter theorem for coends, ZT is
an endofunctor of C and iX,Y is natural in X and dinatural in Y .
In [BV08], we construct an explicit a Hopf monad structure on ZT , inherited
from that of T . The Hopf monad ZT is called the centralizer of T .
CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INV ARIANTS 15
Now, since T preserves colimits (see [BV07, Remark 3.13]) and so coends, T (i)
is a universal dinatural transformation. Therefore we can deﬁne a natural trans-
formation Ω : TZ T →ZTT by:
Ω XT (iX,Y ) = iT (X),T (Y )
(∨µYsl
T (Y )T (∨µY ) ⊗T2(X,Y )
)
T2(∨T (Y ),X ⊗Y ),
where η and u the units of T and ZT respectively, and sl is the left antipode of T .
Theorem 4.1 ([BV08]). Ω : TZ T → ZTT is a bijective comonoidal distributive
law5.
The distributive law Ω is called the canonical distributive law of T over ZT .
Since Ω is a comonoidal distributive law, we get that DT = ZT ◦Ω T is a Hopf
monad on C (whose underlying endofunctor is ZT ◦T ). We call DT the double ofT ,
as justiﬁed by the following theorem:
Theorem 4.2 ([BV08]). Let T be a centralizable Hopf monad on an autonomous
category C. Then the forgetful functor U : Z(T - C) → C , given by
(
(M,r ),σ
)
↦→M ,
is monadic with monad the double DT of T . Furthermore:
RX,Y = (uT (Y ) ⊗ZT (ηX )
)
(idT (Y ) ⊗iX,Y )(coevY ⊗ idX )
is a R-matrix for DT , making the Hopf monad DT quasitriangular, and
Z(T - C) ∼
=DT - C
as braided categories.
Remark 4.3. Let C be an autonomous category which is centralizable, that is, such
that the trivial Hopf monad 1 C is centralizable. In that case, the centralizer Z =Z1C
and the double D1C of 1 C coincide. Then, by Theorem 4.2, Z is a quasitriangular
Hopf monad on C such that Z(C) ∼
=Z- C as braided category. In particular Z(C) is
seen as the category of modules over a quasitriangular Hopf monad . In Section 5.1,
we explicitly describe Z in terms of C when C is a fusion category.
Example 4.4. LetH be a ﬁnite-dimensional Hopf algebra over a ﬁeld k. Then the
Hopf monad T =? ⊗kH on vect k is centralizable. We have: ZT =? ⊗kH ∗ and so
DT =? ⊗kH ⊗kH ∗. From Theorem 4.2, the vector space D(H) = H ⊗kH ∗ inherits
a quasitriangular Hopf algebra structure from the quasitriangular Hopf monad DT .
In particular the algebra structure on D(H) is a twist of that of H ⊗H ∗ by an
isomorphismH ∗ ⊗H →H ⊗H ∗ coming from the distributive law Ω : TZ T →ZTT .
This quasitriangular Hopf algebra D(H) is precisely the Drinfeld double of H.
Furthermore, since T - vectk = repH and DT - vectk = repD(H), one recovers that
Z(repH) ∼
= repD(H) as braided categories.
The previous example may be generalized to Hopf algebras in braided c ategories.
Indeed, let C be a braided category which admits a coend:
C =
∫ Y ∈C
∨Y ⊗Y.
Recall C is then a Hopf algebra in C (see Section 1.5). Let A be a Hopf algebra
in C. Then the Hopf monad ? ⊗A on C is centralizable and we have:
Z?⊗A =? ⊗ ∨A ⊗C, D ?⊗A =? ⊗A ⊗ ∨A ⊗C.
From Theorem 4.2, we get that the object D(A) = A ⊗ ∨A ⊗C is a quasitriangu-
lar Hopf algebra in C, whose structure is inherited from the quasitriangular Hopf
monad D?⊗A. Here D(A) quasitriangular means that there exists a R-matrix:
R : C ⊗C →D(A) ⊗D(A)
5A comonoidal distributive law between two Hopf monads makes their composition a Hopf
monad.
