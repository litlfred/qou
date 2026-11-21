---
doc_id: arxiv-math-9909027v1
doc_title: "Planar Algebras, I"
section_id: sec-002-positivity
section_title: "Positivity"
section_number: null
pages: 25-27
source_pdf: 9909027v1.pdf
source_sha256: e6cd544cdc141d3b
toc_source: inferred
doc_brief: "Planar Algebras, I — We introduce a notion of planar algebra, the simplest example of which is a vector space of tensors, closed under planar contractions."
---
For the rest of this section suppose the ﬁeld is R or C.
Suppose we are given an involution R →R∗on the set of labels L. Then
P(L) becomes a ∗-algebra as follows. If T is a tangle in Tk(L) we reﬂect the
underlying unlabelled tangle in the line y = 1
2 and reverse all the orientations
of the strings. The ﬁrst boundary point for a box in the reﬂected unlabelled
tangle is the one that was the last boundary point for that box in the original
unlabelled tangle.The new tangle T ∗is then obtained by assigning the label
R∗to a box that was labelled R. This operation is extended sesquilinearly
to all of Pk(L). If Φ presents a general planar algebra, ∗preserves ker Φ and
deﬁnes a ∗-algebra structure on Φ(Pk(L)). The operation ∗on T0(L) also
gives a well-deﬁned map on isotopy classes of planar networks and we say an
invariant Z is sesquilinear if Z(N ∗) = Z(N ).
Deﬁnition 1.32. A ∗-algebra P is called a (general) planar ∗-algebra
if it is presented by a Φ on P(L), L with involution ∗, such that Φ is a
∗-homomorphism.
Note that if P is planar, Z is sesquilinear. Moreover if Z is a sesquilinear
multiplicative invariant, the construction of 1.24 yields a planar ∗-algebra.
The partition function on a planar algebra will be called positive if trL(x∗x) ≥
0 for x ∈Pk, k arbitrary.
25
Proposition 1.33 Let P be a planar ∗-algebra with positive partition func-
tion Z. The following are equivalent:
(i) P is non-degenerate (Def. 1.24).
(ii) trR(x∗x) > 0 for x̸ = 0.
(iii) trL(x∗x) > 0 for x̸ = 0.
Proof.
For (ii)⇔(iii), argue ﬁrst that δ1 = trR( ↑) > 0 and δ2 =
Z(
) =
1
δ1trR( ↑↓) > 0 and then deﬁne antiautomorphisms j of P2n by
j( R ) =
R
, so that j(x∗) = j(x)∗and trL(j(x)) = trR(x).
(ii)⇒(i) is immediate since trR(x∗x) = P λiAi(x∗) where Ai ∈Ak,0 is the
annular tangle of ﬁgure 1.34,
Ri
Figure 1.34
writing x = Φ( P
i λi Ri ) ∈Bk.
(i)⇒(ii) Suppose x ∈Pk satisﬁes trR(x∗x) = 0. Then if A ∈Ak,0, we may
26
isotope A(x) so it looks like Figure 1.35
x
y
Figure1.35
where y ∈Pn, n ≥k. Thus Z(A(x)) = trR(˜xy) where ˜x denotes x with
n −k vertical straight lines to the right and left of it.
By the Cauchy-
Schwartz inequality, |trR(˜xy)| ≤
p
trR(˜x∗˜x)
p
trR(y∗y), so if trR(x∗x) = 0,
Z(A(x)) = 0.
□
We will call a general planar algebra P ﬁnite-dimensional if dim Pk < ∞
for all k.
Corollary 1.36 If P is a non-degenerate ﬁnite-dimensional planar ∗-algebra
with positive partition function then Pk is semisimple for all k, so there is a
unique norm ∥∥on Pk making it into a C∗-algebra.
Proof. Each Pk is semisimple since tr(x∗x) > 0 means there are no
nilpotent ideals. The rest is standard.
□
Deﬁnition 1.37. We call a planar algebra (over R or C) a C∗-planar
algebra if it satisﬁes the conditions of corollary 1.34.
