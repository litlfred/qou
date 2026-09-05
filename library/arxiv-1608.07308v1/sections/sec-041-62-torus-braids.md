---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-041-62-torus-braids
section_title: "Torus braids"
section_number: 6.2
pages: 49-50
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
three-strand torus braids. The remainder of this Section provides explicit computations that
follow from Conjectures 1.1 and 3.26.
Proposition 6.1. The sheaves on FHilb3 associated to torus braids on 3 strands are:
(6.5) ι∗(σ1σ2)k =ι∗(σ2σ1)k =



Lm
2Lm
3 k = 3m,
Lm
2Lm
3 ⊗OZ2 k = 3m + 1,
Lm+1
2 Lm
3 ⊗OZ2 k = 3m + 2.
Herem (and hencek) is allowed to be either positive or negative.
Proof. Clearly, (σ1σ2)3 = (σ2σ1)3 = FT3 = ι∗(L2L3), so in virtue of the projection formula
(3.17) it is sufﬁcient to consider the cases k = 0, 1, 2. For k = 0 , Conjecture 1.1 states that
ι∗(1) =OFHilb3, which is precisely the content of (6.5). For k = 1, Conjecture 3.26 implies
ι∗(σ1σ2) =OZ2. Furthermore, for alla,b∈ N one has:
(6.6) Tr(σ2σ1La
2Lb
3) = Tr(σ1σ2La
2Lb
3),
since σ1 commutes with both L2 andL3, and the trace map enjows the property Tr(σσ′) =
Tr(σ′σ). By virtue of the deﬁnition (3.22) of the sheaves associated to the braidsσ1σ2 andσ2σ1,
formula (6.6) implies that ι∗(σ2σ1) = ι∗(σ1σ2). The case k = 2 of (6.5) follows analogously,
because:
(σ1σ2)2 =L2σ2σ1, (σ2σ1)2 =σ1σ2L2.
□
To compute the Khovanov-Rozansky homology of torus braids, one needs to compute the
homology of the resulting line bundles either on FHilb3, or on Z2 = FHilb3(point)× C. For
simplicity, we will consider only the latter case, which corresponds to knots:
Proposition 6.2. The following equations hold: Hi(FHilb3(point),La
2Lb
3) =
(6.7) =



Hi(P1,O(a)⊗Sb(O(2)⊕qtO(−1)) ifb≥ 0,
0 ifb =−1,
Hi+1
(
P1,O(a−1)
qt ⊗S−b−2
(
O(−2)⊕O(1)
qt
))
ifb≤− 2.
Proof. Letπ : FHilb3(point)→ FHilb2(point) = P1 be the natural projection. By (6.4) we
have FHilb3(point) = Proj
(
S∗
P1(O(2)⊕qtO(−1))
)
. The following properties hold:
Riπ∗
(
Lb
3
)
=



Sb(O(2)⊕qtO(−1)) ifi = 0 andb≥ 0,
O(−1)
qt ⊗S−b−2
(
O(−2)⊕O(1)
qt
)
ifi = 1 andb≤− 2,
0 otherwise
50 EUGENE GORSKY, ANDREI NEGUT , , AND JACOB RASMUSSEN
Indeed, the second formula follows from the ﬁrst and Serre duality. This completes the proof.
□
Corollary 6.3. Putting together (6.5), (6.7) and the well-known formula for the cohomology of
line bundles on P1, we have the following formulas for allm≥ 0.
(6.8) HHH
(
(σ1σ2)3m+1)
=H∗(FHilb3(point),Lm
2Lm
3 ) =
=H0
(
P1,
m⨁
i=0
(qt)iO(3m− 3i)
)
=
m∑
i=0
3m−3i∑
j=0
qi+jt3m−2i−j
(6.9) HHH
(
(σ1σ2)3m+2)
=H∗(FHilb3(point),Lm+1
2 Lm
3 ) =
=H0
(
P1,
m⨁
i=0
(qt)iO(3m− 3i + 1)
)
=
m∑
i=0
3m−3i+1∑
j=0
qi+jt3m−2i−j+1
This agrees with thea = 0 part of the Khovanov-Rozansky homology of (3, 3m + 1) and of
(3, 3m + 2) torus knots, conjectured in [32, Section 5.2]. To recover the fulla dependence, we
need to twist the right hand sides of (6.8) and (6.9) by the exterior power:
∧•T∨
3 =∧•(L3“⊕ ”L2⊕O )∨
where the symbol “⊕” refers to the fact thatT3 is a non-trivial extension ofL2⊕O byL3. Note
that all of our computations can be easily extended to “twisted torus knots” in the sense of [14],
which are presented by the braids (σ1σ2)k⊗ι∗(La
2). We leave the corresponding computation
to the interested reader.
