---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-038-73-generators-of-the-braid-group
section_title: "Generators of the braid group"
section_number: 7.3
pages: 41-42
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
g =
ñ
g11 g12
g21 g22
ô
, X =
ñ
x11 x12
0 x22
ô
, Y =
ñ
0 y12
0 0
ô
A direct computation shows that it factors:
W (X,g,Y ) = y12(g11(x11−x22) +g21x12)g21/∆ , ∆ = det( g).
If n = 2 then the unit matrix factorization from section 7.1 is:
C‖ = Φ(
î
g21∆ −1 y12(g11(x11−x22) +g21x12)
ó
),
Let also introduce the matrix factorizations C+,C•:
C• = Φ(
î
y12∆ −1 g21(g11(X11−X22) +g21X12)
ó
),
(7.21) C+ = Φ(
î
g21y12∆ −1 (g11(x11−x22) +g21x12)
ó
).
The complex C+, as we will see later, correspond to the positive crossing of two str ands in the braid. To
deﬁne the complex corresponding to the negative crossing we need to shift the weights of B2 action onC+.
Let χ1,χ 2 be the generators of the group of characters of B:
χ1
Çñ
a b
0 c
ôå
=a, χ 2
Çñ
a b
0 c
ôå
=c.
Bellow we use convention that F⟨χ′,χ ′′⟩∈ MFsc
B2(X2(G2),W ) is obtained from the complex F by twisting
the action of the ﬁrst factor in B2 by the character χ′ and the action of the second copy is twisted by the
character χ′′. With these conventions in mind we have the following formula for the c omplex of negative
crossing.
(7.22) C− :=C+⟨−χ1,χ 2⟩.
We postpone the description of the Tsc-equivariant structure of matrix factorizations from above till th e
section 9. In the section 9 we show that the convolution of C+ andC− is homotopic to C‖ .
To deﬁne the generators of Brn for general n we use our induction functor:
C(i)
± := Ind ii+1(C±), C(i)
‖ := Ind ii+1(C‖ ).
It is elementary to check that C(i)
‖ is independent of i and is a unit in the convolution algebra (see next
section for the proof). The main result of the ﬁrst part of the pap er is the following theorem
Theorem 7.6. The complexesC(i)
± satisfy the braid relations
C(i)
+ ⋆C(i)
− ∼C ‖,(7.23)
C(i)
+ ⋆C(i+1)
+ ⋆C(i)
+ ∼C (i+1)
+ ⋆C(i)
+ ⋆C(i+1)
+ ,(7.24)
C(i)
+ ⋆C(j)
+ ∼C (j)
+ ⋆C(i)
+ , |i−j|> 1.(7.25)
where∼ is the homotopy equivalence.
Proof. The relation (7.23) is proven for two strand braids in lemma 9.6. Hence by corollary 7.3 the relation
(7.23) holds in general. The equation (7.24) is proven for three stra nd braids in corollary 11.6. Finally, the
commuting relation (7.25) follows from the corollary 7.5. ✷
41
For a given element β =σǫ1
i1··· σǫℓ
iℓ we introduce the following notations:
Cβ =C(i1)
ǫ1 ⋆... C(iℓ)
ǫℓ , ¯Cβ = ¯C(i1)
ǫ1 ¯⋆... ¯⋆ ¯C(iℓ)
ǫℓ .
