---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-041-33-the-thick-subcategory-of-negligible-objects-4
section_title: "The thick subcategory of negligible objects 49"
section_number: 3.3
pages: 57-59
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
It has been shown in [41, prop. 3.6.1] that these quotient constructions
are compatible with each other in the sense that the perverset-structure
on D induces on the triangulated quotient categoryD a t-structure whose
core is naturally equivalent to the abelian quotient categoryP. So we have
a commutative diagram
P   //

D

P   // D
where the rows are embeddings of full subcategories and the columns are
the quotient functors. It turns out that convolution behaves well with respect
to the above quotient constructions in the following sense.
LEMMA 3.7. Let K,M∈ D.
(a) The cone of the morphism K∗! M−→K∗∗ M lies inT.
(b) If K or M lies inT, then K∗! M and K∗∗ M are also inT.
(c) If both K and M are perverse, thenpHn(K∗! M) and pHn(K∗∗ M)
lie in the Serre subcategoryS for all n⁄= 0.
Proof. (a)LetC be the cone of the morphismK∗!M→K∗∗M. We want
to show thatH•(X,Cχ) = 0 for a generic characterχ∈ Π(X). Lemma 3.4
implies that for any characterχ the twistCχ is isomorphic to the cone of
the twisted morphism
Kχ∗! Mχ−→Kχ∗∗ Mχ,
so it sufﬁces to check that the induced morphism
H•(X,Kχ∗! Mχ)−→H•(X,Kχ∗∗ Mχ)
is an isomorphism for genericχ. By corollary 3.3 we can replace the left
hand side by the compactly supported hypercohomology ofKχ∗! Mχ. So
we must see that the forget support map
fKχ⊠Lχ : H•
c (X×k X,Kχ⊠Mχ)−→H•(X×k X,Kχ⊠Mχ)
is an isomorphism for genericχ. For this we go back to the deﬁnition
of compactly supported hypercohomology. For simplicity of notation we
will suppress the character twist in what follows, replacingK and L by
their twistsKχ and Lχ. Let j : X ↪→ X be a compactiﬁcation, and consider
the following diagram where all the horizontal arrows are forget support
50 Chapter 3 – Perverse sheaves on semiabelian varieties
morphisms (the vertical arrows will be discussed below).
H•c (X×k X,K⊠L) fK⊠L // H•(X×k X,K⊠L)
H•(X×k X,(j, j)!(K⊠L)) //
(1)
H•(X×k X,R(j, j)∗(K⊠L))
H•(X×k X, j!(K)⊠ j!(L)) //
OO
(2)
H•(X×k X,R j∗(K)⊠R j∗(L))
OO
H•(X, j!(K))⊗H•(X, j!(L)) //
OO
(3)
H•(X,R j∗(K))⊗H•(X,R j∗(L))
OO
H•c (X,K)⊗H•c (X,L) fK⊗fL //
(4)
H•(X,K)⊗H•(X,L)
The horizontal arrowfK⊗ fL on the bottom line is the tensor product of
the forget support morphisms forK and L, hence by corollary 3.3 it is an
isomorphism for genericχ. On the other hand, the horizontal arrowfK⊠L
on the top line is the forget support morphism we are interested in. So we
will be ﬁnished if we can show that the above diagram commutes and that
all the vertical arrows (to be deﬁned yet) are isomorphisms.
The squares (1) and (4) are commutative by the very deﬁnition offK⊠L
and fK⊗ fL. The vertical arrows in (3) are the K¨unneth isomorphisms for
the proper morphismX→ Spec(k), and the commutativity of this square
follows from the fact that the K¨unneth morphisms are natural in the involved
complexes. Finally, the square (2) is induced by the square
(j, j)!(K⊠L) // R(j, j)∗(K⊠L)
j!(K)⊠ j!(L) //
ad−1
!
OO
R j∗(K)⊠R j∗(L)
ad∗
OO
where the morphisms
ad! : (j, j)!(K⊠L)−→ j!(K)⊠ j!(L)
ad∗ : R j∗(K)⊠R j∗(L)−→R(j, j)∗(K⊠L)
are the natural morphisms which correspond via adjunction to the identity
morphism of
K⊠L = ( j, j)!(j!(K)⊠ j!(L)) = ( j, j)∗(R j∗(K)⊠R j∗(L)).
Note thatad! is an isomorphism and that overU = X×k X ↪→ X×k X all
the morphisms in the above diagram restrict to the identity. In particular,
