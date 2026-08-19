---
doc_id: arxiv-1208.2521v1
doc_title: "1. Introduction Several possible q-analogues of the Bessel function (1.1) Jα (x) := (−1)k (x/ 2)α +2k k! Γ( α + k + 1) have been considered in the literature. Best known are two re"
section_id: sec-009-12-tom-h-koornwinder-and-ren-e-f-sw-arttouw
section_title: "TOM H. KOORNWINDER AND REN ´E F. SW ARTTOUW"
section_number: 12
pages: 12-14
source_pdf: 1208.2521v1.pdf
source_sha256: 8d0281aa84043865
doc_brief: "ON q-ANALOGUES OF THE FOURIER — For the third q-Bessel function (ﬁrst introduced by F. H. Jackson, later rediscovered by W. Hahn in a special case and by H."
---
Formula (4.5) is a q-analogue of the addition formula
(4.6)
∞∑
k=−∞
sk Jn+k(y) Jk(x) =
( y − s− 1x
y − sx
) n/ 2
Jn
( √
(y − s− 1x)(y − sx)
)
,
due to Graf (cf. [15, §11.3 (1)]). The special case n = 0 of (4.5) is a q-analogue
of Neumann’s addition formula for Bessel functions J0 (cf. [15, §11.2 (1)]). In the
special case x = y, s = 1 the right-hand side of (4.5) becomes yn δn, 0, so then (4.5)
reduces to the orthogonality relations (2.10).
When we apply the symmetries (2.5) and (4.3) to the left-hand side of (4.5) and
also apply (2.3) to the right-hand side of (4.5), and replace n by n − m and next k
by k + m then we obtain an equivalent identity:
Proposition 4.2. For |sxy| < 1 and x2, y 2 ⁄= q− l (l = 0, 1, 2, . . . ), we have
(4.7)
∞∑
k=−∞
sk yn+k (y2; q)∞
(q; q)∞
1φ 1(0; y2; q, q n+k+1) xm+k (x2; q)∞
(q; q)∞
1φ 1(0; x2; q, q m+k+1)
=







s− m yn− m (s− 1xy− 1, y 2; q)∞
(sxy, q ; q)∞
2φ 1
[ qsx− 1y, sxy
y2 ; q, q n− ms− 1xy− 1
]
,
s− n xm− n (s− 1yx− 1, x 2; q)∞
(sxy, q ; q)∞
2φ 1
[ qsxy − 1, sxy
x2 ; q, q m− ns− 1yx− 1
]
,
where the ﬁrst expression on the right-hand side can be chose n if s− 1xy− 1 and
qn− ms− 1xy− 1 are not equal to a non-positive integer power of q, and where the sec-
ond expression on the right-hand side can be chosen if s− 1yx− 1 and qm− ns− 1yx− 1
are not equal to a non-positive integer power of q. Thus in the generic case both
expressions on the right-hand side are equal.
See Appendix B for the detailed proof. Observe the special ca se x = y of (4.7):
(4.8)
∞∑
k=−∞
sk zn+k (z2; q)∞
(q; q)∞
1φ 1(0; z2; q, q n+k+1) zm+k (z2; q)∞
(q; q)∞
1φ 1(0; z2; q, q m+k+1)
=







s− m zn− m (s− 1, z 2; q)∞
(sz2, q ; q)∞
2φ 1
[ qs, sz 2
z2 ; q, q n− ms− 1
]
,
s− n zm− n (s− 1, z 2; q)∞
(sz2, q ; q)∞
2φ 1
[ qs, sz 2
z2 ; q, q m− ns− 1
]
,
where |sz2| < 1, z2 is not a non-positive integer power of q and the expression on
the right-hand side has to be chosen similarly as in Proposit ion 4.2. This can be
considered as a kind of Poisson kernel for the orthogonal sys tem with orthogonality
ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS 13
relations (2.11). Inspection of the right-hand side of (4.8 ) shows that this kernel is
positive if 0 < z < 1 and 1 < s < min{q− 1, z − 2}.
Let us look for the classical analogue of formula (4.7). In (4 .7) ﬁrst replace q by
q2, then x, y, s by qα +1, q β +1, q − γ − 1, respectively. Then, with the notation (3.3),
formula (4.7) can be rewritten as
∞∑
k=−∞
qk(− γ +1) Jα (qm+k; q2) Jβ (qn+k; q2)
=



















qnβ qm(γ − β − 1) (qα − β +γ +1, q 2β +2; q2)∞
(qα +β − γ +1, q 2; q2)∞
× 2φ 1(qβ − α − γ +1, q α +β − γ +1; q2β +2; q2, q 2n− 2m+α − β +γ +1),
qmα qn(γ − α − 1) (qβ − α +γ +1, q 2α +2; q2)∞
(qα +β − γ +1, q 2; q2)∞
× 2φ 1(qα − β − γ +1, q α +β − γ +1; q2α +2; q2, q 2m− 2n+β − α +γ +1),
where ℜ(α + β − γ + 1) > 0, α, β are not equal to a negative integer, and where
we can choose the ﬁrst expression on the right-hand side if ( α − β + γ + 1)/ 2 and
n−m+(α −β +γ +1)/ 2 are not a non-positive integer and we can choose the second
expression on the right-hand side if ( β − α + γ + 1)/ 2 and m − n + (β − α + γ + 1)/ 2
are not a non-positive integer.
Now replace qk by qk(1 − q) (with log(1− q)
log q ∈ Z) and let m, n depend on q such
that, as q ↑ 1, qm tends to a and qn tends to b. Depending on whether b < a
or b > a , make the formal limit transition q ↑ 1 in the ﬁrst or second identity,
respectively. Then, for ℜ(α + β − γ + 1) > 0, ℜγ > −1, we obtain the discontinuous
integral of Weber and Schafheitlin:
2γ
∫ ∞
0
x− γ Jα (ax) Jβ (bx) dx
=



















aγ − β − 1 bβ Γ(( α + β − γ + 1)/ 2)
Γ(( α − β + γ + 1)/ 2) Γ( β + 1)
×2F1((β − α − γ + 1)/ 2, (α + β − γ + 1)/ 2; β + 1; b2/a 2) if b < a ,
aα bγ − α − 1 Γ(( α + β − γ + 1)/ 2)
Γ(( β − α + γ + 1)/ 2) Γ( α + 1)
×2F1((α − β − γ + 1)/ 2, (α + β − γ + 1)/ 2; α + 1; a2/b 2) if a < b ,
(cf. [15, §13.4 (2)]). Note that the two analytic expressions at the rig ht-hand side
are no longer equal, as they were in the q-case.
