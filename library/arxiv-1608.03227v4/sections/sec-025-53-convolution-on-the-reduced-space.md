---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-025-53-convolution-on-the-reduced-space
section_title: "Convolution on the reduced space"
section_number: 5.3
pages: 26-26
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
consider the space X 3 := b×G2× n with the following B3-action
(b1,b 2,b 3)· (X,g 12,g 23,Y ) = (Ad b1 (X),b 1g12b−1
2 ,b 2g23b−1
3 , Adb3 (Y )).
There are the following maps ¯πij : X 3→ X 2:
¯π12(X,g 12,g 13,Y ) = (X,g 12, Adg23 (Y )++),
¯π23(X,g 12,g 13,Y ) = (Ad −1
g12 (X)+,g 23,Y ),
¯π13(X,g 12,g 13,Y ) = (X,g 12g23,Y ).
Proposition 5.3. ¯π∗
12(W ) + ¯π∗
23(W ) = ¯π∗
13(W ).
Proof. Indeed we have
¯π∗
12(W ) + ¯π∗
23(W ) = Tr(XAdg12 (Adg23 (Y )++)) + Tr(Ad−1
g12 (X)+Adg23 (Y )) =
Tr(Ad−1
g12 (X)Adg23 (Y )++) + Tr(Ad−1
g12 (X)+Adg23 (Y )).
Thus the statement follows is implied by
Tr(AB++) + Tr(A+B) = Tr(AB)− Tr(AB−) + Tr(A+B−)
= Tr(AB) + Tr(A−B−) = Tr(AB).
✷
For givenF,G∈ MFsc
B×B(X 2,W ) it is tempting to deﬁne
(5.12) F ¯⋆G := ¯π13∗(CEn(2) (¯π∗
12(F )⊗ ¯π∗
23(G))))T (2)
,
where n(2), T (2) are the subalgebras of the middle factor in b3 acting on X 3. The only issue with this
deﬁnition is that the maps ¯π12 and ¯π23 are not B3 equivariant. Thus we have to deﬁne the B3-equivariant
structure on the pull back ¯π∗
12(F )⊗ ¯π∗
23(G) and we do it below.
