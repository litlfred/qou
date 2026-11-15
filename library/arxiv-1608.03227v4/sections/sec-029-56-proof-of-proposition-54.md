---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-029-56-proof-of-proposition-54
section_title: "Proof of proposition 5.4"
section_number: 5.6
pages: 30-31
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
sion for π∗
12(Φ(F)♯) ⊗π∗
23(Φ(G)♯):
(5.18)
π∗
12(¯π∗(F♯) ⊗CC) ⊗π∗
23(¯π∗(G♯) ⊗CC)
= (π12 ◦¯π)∗(F♯) ⊗(π23 ◦¯π)∗(G♯) ⊗π∗
12(CC) ⊗π∗
23(CC).
The last factor is the Koszul complex
î
( ˜X2
−−)
(Y2 −Adg23(Y3)++)
ó
hence we can use row transformations
of second type to eliminate variables Y2 from the matrix factorization (5.18). More precisely, use the row
transformations of the second type to eliminate Y2 from the ﬁrst factor (π12 ◦¯π)∗(F) and from the second
to last factors π∗
12(CC).
We can apply the second type of row transformation because (π12 ◦¯π)∗(F♯) and π∗
12(CC) are the factors
of π∗
12(Φ(F)♯), thus diﬀerentials in these matrix factorizations commute with the diﬀerentials from the factor
π∗
23(Φ(G)♯) and hence the admissibility condition (5.17) is satisﬁed. On the other hand, the second factor
(π23 ◦¯π)∗(G♯) has no dependence on Y2.
The result of elimination of Y2 from the factor before the last is
CC123 = [ ˜X1,−−, Y1 −Adg12(Adg23(Y3)++)++]
and the ﬁrst two factors are
π∗
12(¯π∗(F))|Y2=Adg23 (Y3)++ = F|Y =Adg23 (Y3)++,X+= ˜
X1,+ = ¯π∗
con(¯π∗
12(F))
π∗
23(¯π∗(G))|Y2=Adg23(Y3)++ = G|Y =Y3,X+=Ad−1
g12 ( ˜
X1)+,
where (X+, g12, g23, Y ) are coordinates on X 3. After the elimination the only term that has dependence
on Y2 is the Koszul complex
î
G
(Y2 −Adg23(Y3)++)
ó
and since π∗
13(W) does not depend on Y2 and the
correction correction diﬀerentials ∂, which could depend on Y2 does not contribute the square of the total
diﬀerential, the element G must vanish.
As the next step we use the complex CC123 to eliminate dependence on ˜X1,−−from the other terms in
the tensor product (5.18). For that we use the ﬁrst type of row transformation and we do not need to worry
about the admissibility of our eliminations. The term ¯π∗
con(¯π∗
12(F)) has no dependence on ˜X1,−−so it is not
aﬀected by this elimination. On the other hand the second term becomes:
G|Y =Y3,X+=Ad−1
g12 ( ˜
X1)+, ˜
X1,−−=0 = G|Y =Y3,X+=Ad−1
g12 ( ˜
X1,+)+ = ¯π∗(¯π∗
23(G)).
After this round of elimination the only dependence on ˜X1,−−in (5.18) comes from the Koszul complex
[ ˜X1,−−, G′] hence G′ must be the derivative of π∗
13(W) by ˜X1,−−that is G′ = Y1 −Ad−1
g13(Y3). That is after
the eliminations Y2, ˜X1,−−we obtain the complex
(5.19)
¯π∗(¯π∗
12(F) ⊗¯π∗
23(G)) ⊗[Y2 −Adg23(Y3)++, 0] ⊗π∗
13(CC)
as we claimed in the proposition.
30
