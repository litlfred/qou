---
doc_id: ant-v14-n7-s-p05
doc_title: "Motivic Gauss–Bonnet formulas"
section_id: sec-003-1-txb1xb-xπx6txb-p11xb-xπx-p1-p
section_title: "TX/B(1X×B X))≃πX♯6−TX/B p1♯(1X×B X)≃πX! p1♯ p∗"
section_number: 1
pages: 10-13
source_pdf: ant-v14-n7-s-p05.pdf
source_sha256: 1c8e94ff62a8d920
doc_brief: "Motivic Gauss–Bonnet formulas — 18 sections: Duality and Euler characteristics; TX/B(1X×B X); TX/B(p∗"
---
2(1X)
(base change)
≃ πX!π∗
XπX♯(1X)≃πX!(1X∧Xπ∗
X(X/B))
(projection formula)
≃ πX!(1X)∧B(X/B)= X/BB.M.∧B X/B.
The base change isomorphisms follow from [Hoyois 2017, Theorem 6.18(3)] and the projection formula
is [Hoyois 2017, Theorem 6.18(7)]. □
Construction 2.12. LetπX: X→ B be an object of SmB that is proper (i.e., a smooth projective scheme
over B). We recall (from [Hoyois 2017], but see also the constructions of [Riou 2005; Ayoub 2007]) the
construction of a duality between the objects X/B and X/BB.M. in SH(B).
We ﬁrst construct the coevaluation mapδX/B: 1B→ X/B∧B X/BB.M.. Applying the functoriality of
(−)/BB.M. from Remark 2.9 to the proper map πX gives the map
π∗
X: 1B= B/BB.M.→ X/BB.M.=πX!(1X)≃πX♯(6−TX/B(1X))
in SH(B), and the diagonal1X/B: X→ X×B X induces via the functoriality of(−)/ X: SmX→ SH(X)
the map
1X/B∗:=1X/B/ X: 1X= X/ X→ X×B X/ X
in SH(X). We may put together these two maps to obtain the composition
1B
π∗
X−→πX♯(6−TX/B(1X)) πX♯6−TX/B(1X/B∗)−−−−−−−−−−→πX♯6−TX/B(X×B X/ X),
Using the identiﬁcation πX♯6−TX/B(X×B X/ X)≃ X/B∧B X/BB.M. from Lemma 2.11, this gives the
desired mapδX/B.
Motivic Gauss–Bonnet formulas 1811
We now construct the evaluation mapϵX/B: X/BB.M.∧B X/B→ 1B (which does not require properness
ofπX). Here we apply the functoriality of (−)/ XB.M. to the proper map1X/B to obtain the map
1∗
X/B: X×B X/ XB.M.→ X/ XB.M.= 1X
in SH(X), and the functoriality of (−)/B to the mapπX to obtain the map
πX∗: X/B→ B/B= 1B.
Putting these together yields the composition
πX♯(X×B X/ XB.M.) πX/B♯(1∗)−−−−−→πX/B♯(1X)= X/B πX∗−→1B.
Now using the identiﬁcation X/BB.M.∧B X/B≃πX♯(X×B X/ XB.M.) from Lemma 2.11, we get the
desired mapϵX/B.
It is shown in [Hoyois 2017, Corollary 6.13] that the triple (X/BB.M.,δ X/B,ϵ X/B) is the dual of X/B
in SH(B). Using our notation for Thom spaces, we have
X/BB.M.=πX!(1X)≃πX#◦6−TX/B(1X)= ThX(−TX/B)/B,
the coevaluation map is
δX/B: 1B→ X/B∧B ThX(−TX/B)/B
and the evaluation map is
ϵX/B: ThX(−TX/B)/B∧B X/B→ 1B
The dualizability of X/B as above allows one to deﬁne an Euler characteristic for smooth projective
schemes:
Deﬁnition 2.13. For X→ B in SmB and proper, the Euler characteristicχ( X/B)∈ EndSH(B)(1B) is the
composition
1B
δX/B−−→X/B∧B ThX(−TX/B)/B τ→ ThX(−TX/B)/B∧B X/B ϵX/B−−→1B,
whereτ denotes the symmetry isomorphism, and δX/B andϵX/B are as in Construction 2.12.
To ﬁnish this section, we give an alternative characterization of the Euler characteristic χ( X/B) just
deﬁned (Lemma 2.15 below). We proved this result in the case B= Spec k for k a ﬁeld in [Levine 2017b];
the proof in this more general setting is exactly the same.
Construction 2.14. We consider X×B X as a smooth X-scheme via the projection p2. The diagonal
1X: X→ X×B X gives a section to p2. Let q: X×B X→ X×B X/(X×B X\1X(X)) be the quotient
map. We have the Morel–V oevodsky purity isomorphism [1999, Theorem 3.2.23], which gives the
isomorphism in H•(X)
mv1: X×B X/(X×B X\1X(X))−→∼ ThX(N1X).
1812 Marc Levine and Arpon Raksit
Composing the 0-sectionsN: X→N1X with the quotient mapN1X→Th(N1X) deﬁnes¯sN: X→ThX(N1X).
It follows from the proof of the purity isomorphism that we have the commutative diagram in H•(X)
X×B X+
q // X×B X/(X×B X\1X(X))
mv1 // ThX(N1X)
X+
q◦1X
OO
¯sN
55
1X
hh
(2.14.1)
Finally, we have the isomorphism N1X≃ TX/B of vector bundles over X furnished by the composition
TX/B−→∼ 1∗
X p∗
2TX/B
i2→1∗
X(p∗
1TX/B⊕ p∗
2TX/B)≃1∗
X TX×B X/B
π→ N1X,
whereπ:1∗
X TX×B X/B→ N1X is the canonical projection. Putting these maps together gives us the
composition in H•(X)
X+
1X−→ X×B X q→ X×B X/(X×B X\1X(X)) mv1−−→ThX(N1X)−→∼ ThX(TX/B);
the commutativity of (2.14.1) shows that this composition is equal to the map ¯sTX/B: X+→ ThX(TX/B),
induced as for¯sN1X by the zero-section sTX/B: X→ TX/B.
Applying6−TX/B6∞
P1(−) and the isomorphism
6−TX/B Th(TX/B)≃6−TX/B◦6TX/B(1X)≃ 1X
gives the morphism
˜βX/B:6−TX/B(1X)→ 1X
in SH(X). Finally, applyingπX# gives the morphism
βX/B: Th(−TX/B)→ X/B
in SH(B).
Summarizing our construction,βX/B is given by applyingπX# to the composition in SH(X)
6−TX/B(1X) 6−TX/B(1X)−−−−−−→6−TX/B(X×B X/ X) 6−TX/B(q)−−−−−→6−TX/B([X×B X/(X×B X\1X)]/ X)
6−TX/B(mv1X)
−−−−−−−→6−TX/B(ThX(N1X))≃6−TX/B(ThX(TX/B))≃6−TX/B◦6TX/B(1X)≃ 1X (2.14.2)
or equivalently, to the composition
6−TX/B(1X)
6−TX/B(¯sTX/B)
−−−−−−−→6−TX/B(ThX(TX/B))≃6−TX/B◦6TX/B(1X)≃ 1X (2.14.3)
Lemma 2.15. For X smooth and proper over B, χ( X/B) is equal to the composition
1B
π∗
X−→Th(−TX/B)
βX/B
−−→X/B
πX∗
−→1B
Motivic Gauss–Bonnet formulas 1813
Proof. Let pi: X×B X→ X, i= 1, 2, be the projections. The map
evX: X/B∨∧B X/B→ 1B
is the composition
X/B∨∧B X/B= Th(−TX/k)∧B X/B= Th(−p∗
1TX/k) q→ Th(−p∗
1TX/B)/Th(− j∗ p∗
1TX/B)
≃ Th(−TX/B⊕ N1X)≃ Th(−TX/B⊕ TX/B)≃ X/B πX−→1B.
From our description of βX/B asπX# applied to the composition (2.14.2), we see that πX∗◦βX/B=
evX/B◦ Th(1X). Also, π∗
X=π∨
X andπ∨
X is given by
1B
δX/B−−→X/B∧B X/B∨= Th(−p∗
2TX/B) p2−→Th(−TX/B)
It follows from the construction of the map δX/B described above that
δX/B= Th(1X)◦π∗
X.
This gives us the commutative diagram
X/B∧B X/B∨ τX,X∨
// X/B∨∧B X/B
evX
’’1B
δX/B
77
π∗
X ’’
Th(−p∗
2TX/B)
τX,X∨
// Th(−p∗
1TX/B) 1B
Th(−TX/B)
Th(1X)
55
Th(1X)
OO
βX/B
// X/B
πX∗
77
□
