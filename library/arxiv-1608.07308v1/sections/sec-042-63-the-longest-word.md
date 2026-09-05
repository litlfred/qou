---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-042-63-the-longest-word
section_title: "The longest word"
section_number: 6.3
pages: 50-52
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
word inS3. Remark that the following equation holds for alla andb:
(6.10) Tr(σ1σ2σ1La
2Lb
3) = Tr(σ2σ1σ1La
2Lb
3),
sinceσ1 commutes both withL2 andL3 and the trace satisﬁes Tr(σσ′) = Tr(σ′σ). By Corol-
lary 3.4, these traces are isomorphic up to a twist by a permutation (1 2). In particular, the
left hand side of (6.10) is supported on {x1 = x3}, while the right hand side is supported on
{x2 =x3}. Furthermore,
ι∗(σ2σ1σ1) =L2⊗ι∗(σ2) =L2⊗O FHilb(2∼3).
Note that in the notations of Section 6, FHilb(2∼ 3) =Z2∪Z5. There is a natural involution
j12 on FHilb3 which exchangesx1 andx2 inZ1, acts trivially on Z2 andZ3 and permutes Z4
andZ5. We arrive at the following conjecture:
Conjecture 6.4. One hasι∗(σ1σ2σ1) =j∗
12(L2⊗OZ2∪Z5).
6.4. The ﬁgure eight knot. In this section we describe a sheaf for the braidβ =σ1σ−1
2 σ1σ−1
2
representing the ﬁgure eight knot. There is a skein exact sequence relatingBβ with the follow-
ing objects in SBim3:
σ1σ2σ1σ−1
2 =σ2σ1,σ 1σ1σ−1
2 =L2σ−1
2 .
More precisely, there is an exact sequence:
(6.11) 0← −σ2σ1← −Cone
[
L2σ−1
2
x1−x2
←−−−L2σ−1
2
]
← −Bβ← −0.
FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY 51
Proposition 6.5. The following identity holds:
ι∗ Cone
[
σ−1
2
x1−x2
←−−−σ−1
2
]
≃
[
L2L−1
3 ⊕qtL−1
3
]
Z2
.
Proof. By (3.49) one has:
OFHilb(1∼2)≃ [OFHilb3(C)
x1−x2
←−−−qOFHilb3(C)
y21
←−qtL−1
2 |FHilb(1∼2)]
(note that this is also a skein exact sequence forσ−1
1 , 1,σ 1) and
ι∗(σ−1
2 ) =L2L−1
3 ⊗O FHilb(2∼3).
SinceOFHilb(2∼3)⊗O FHilb(1∼2) =OZ2, one has an exact sequence:
0←L 2L−1
3 |Z2← −ι∗ Cone
[
σ−1
2
x1−x2
←−−−σ−1
2
]
← −qtL−1
3 |Z2← −0.
It remains to notice that
ExtZ2(L2L−1
3 ,L−1
3 ) =H∗(Z2,L−1
2 ) =H∗(P1,O(−1)) = 0.
□
Proposition 6.6. Consider the braidβ =σ1σ−1
2 σ1σ−1
2 representing the ﬁgure eight knot. Then,
assuming Conjecture 1.1 and 3.26, one has
ι∗(β) =OP1⊕qtL2L−1
3 .
Proof. By (6.11) and Proposition 6.5 one has:
0← −OZ2
α
← −
[
L2
2L−1
3 ⊕qtL2L−1
3
]
Z2
← −qt(ι∗Bβ)← −0.
Let us compute the mapα. Remark that:
HomZ2(L2L−1
3 ,O) =H0(Z2,L−1
2 L3) =H0(P1,O(1)⊕qtO(−2)),
HomZ2(L2
2L−1
3 ,O) =H0(Z2,L−2
2 L3) =H0(P1,O⊕ qtO(−3)).
Thereforeα is the unique degree 1 mapL2
2L−1
3 →O and vanishes onL2L−1
3 , so
ι∗Bβ≃L 2L−1
3 ⊕q−1t−1 Cone[O
α
← −L2
2L−1
3 ]≃O P1⊕L 2L−1
3 .
□
Using this result, we can compute the reduced homology of β· FTa
2FTb
3 by computing the
homology of each summand individually. Since FHilb3(point) is a blowup of the punctual
Hilbert scheme of 3 points, and P1 is the exceptional divisor, the tautological bundle is trivial
on P1:T 3⊗O P1≃ (q +t)OP1. Similarly, FT3⊗O P1≃qtOP1. We get the following equation:
(6.12)
∫
FHilb3(point)
OP1⊗ FTa
2FTb
3⊗∧•T
∨
3 = (1 +aq−1)(1 +at−1)(qt)b
∫
P1
O(a).
Equations (6.12) and (6.7) can be used to compute the homology ofβ·La
2Lb
3 for alla andb.
In particular:
H∗(FHilb3(point),L2L−1
3 ) =H∗(FHilb3(point),L−1
3 ) = 0,
H∗(FHilb3(point),L−2
3 ) =H∗+1(P1,O(−1)) = 0,
H∗(FHilb3(point),L2L−2
3 ) =H∗+1(P1,O) = C[1],
so ∫
FHilb3(point)
L2L−1
3 ⊗∧•T
∨
3 =aC[1],
52 EUGENE GORSKY, ANDREI NEGUT , , AND JACOB RASMUSSEN
and
HHH(β) = (1 +aq−1)(1 +at−1) +a√qt.
One can compare this with [21, Table 5.7].
7. C ATEGORICAL IDEMPOTENTS AND EQUIVARIANT LOCALIZATION
