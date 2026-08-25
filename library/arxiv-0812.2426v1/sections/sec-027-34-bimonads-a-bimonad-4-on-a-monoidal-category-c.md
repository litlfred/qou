---
doc_id: arxiv-0812.2426v1
doc_title: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS"
section_id: sec-027-34-bimonads-a-bimonad-4-on-a-monoidal-category-c
section_title: "Bimonads. A bimonad 4 on a monoidal category C is a monad ( T,µ,η ) on C"
section_number: 3.4
pages: 12-13
source_pdf: 0812.2426v1.pdf
source_sha256: df1eb953bc2c6c63
doc_brief: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS — A theorem of M¨ uger asserts that the center Z(C) of a spherical k-linear category C is a modular category if k is an algebraically closed ﬁeld"
---
endowed with a natural transformation T2(X,Y ) :T (X ⊗Y ) →T (X) ⊗T (Y ) and
a morphism T0 : T (
/BD ) → /BD satisfying:
(idT (X) ⊗T2(Y,Z ))T2(X,Y ⊗Z) = (T2(X,Y ) ⊗ idT (Z))T2(X ⊗Y,Z );
(idT (X) ⊗T0)T2(X, /BD ) = id T (X) = (T0 ⊗ idT (X))T2(/BD ,X );
T2(X,Y )µX⊗Y = (µX ⊗µY )T2(T (X),T (Y ))T (T2(X,Y ));
T0µ
/BD
=T0T (T0); T2(X,Y )ηX⊗Y = (ηX ⊗ηY ); T0η
/BD
= id
/BD
;
for all objects X,Y,Z of C.
3.5. Antipodes. Let (T,µ,η ) be a bimonad on a monoidal category C.
If C is left autonomous, then a left antipode for T is a natural transformation
sl = {sl
X : T (∨T (X)) → ∨X}X∈Ob(C) satisfying:
T0T (evX )T (∨ηX ⊗ idX ) = ev T (X)(sl
T (X)T (∨µX ) ⊗ idT (X))T2(∨T (X),X );
(ηX ⊗ id∨ X )coevXT0 = (µX ⊗sl
X )T2(T (X), ∨T (X))T (coevT (X)).
Likewise, if C is right autonomous, then a right antipode for T is a natural
transformation sr = {sr
X : T (T (X)∨) →X ∨}X∈Ob(C) satisfying:
T0T ( ~evX )T (idX ⊗η∨
X ) = ~evT (X)(idT (X) ⊗sr
T (X)T (µ∨
X ))T2(X,T (X)∨);
(idX ∨ ⊗ηX ) ~coevXT0 = (sr
X ⊗µX )T2(T (X)∨,T (X))T ( ~coevT (X)).
As in the classical case, left and right antipodes are ‘anti-(co)multip licative’,
see [BV07, Theorem 3.7].
Note that if a left (resp. right) antipode exists, then it is unique. Fu rthermore,
when they exist, the left antipode sl and the right antipode sr are ‘inverse’ to
each other in the sense that id T (X) = sr
∨ T (X)T ((sl
X )
∨
) = sl
T (X)∨T (∨(sr
X )) for any
object X of C.
3This is not standard terminology: pairs ( M, r) are usually called T -algebras in the literature.
However pairs ( M, r) are considered here as the analogues of modules over an alge bra, and so the
term ‘algebra’ would be awkward in this context.
4This notion of bimonad coincides exactly with the notion of ‘ Hopf monad’ introduced in
[Moe02]. However, by analogy with the notions of bialgebra a nd Hopf algebra, we prefer to
reserve the term ‘Hopf monad’ for bimonads with antipodes (s ee Section 3.6)
CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INV ARIANTS 13
