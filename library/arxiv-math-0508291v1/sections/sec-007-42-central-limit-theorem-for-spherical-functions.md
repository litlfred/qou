---
doc_id: arxiv-math-0508291v1
doc_title: "Stein’s Method and Random Character Ratios"
section_id: sec-007-42-central-limit-theorem-for-spherical-functions
section_title: "Central limit theorem for spherical functions"
section_number: 4.2
pages: 18-23
source_pdf: 0508291v1.pdf
source_sha256: d2d541426aaec742
doc_brief: "Stein’s Method and Random Character Ratios — Stein’s method is used to prove limit theorems for random character ratios."
---
subsection is to prove a central limit theorem for the random variable W
deﬁned byW (i) = |Ku|1/ 2
|K|1/ 2 ωi(gu). Here gu is ﬁxed satisfying KguK =Kg −1
u K
andi is random from the Plancherel measure of the Gelfand pair ( G,K ). It
is not assumed that the Gelfand pair ( G,K ) is symmetric.
To construct an exchangeable pair to be used for Stein’s meth od, it is
helpful to deﬁne a Markov chain on the set of spherical functi ons of (G,K ).
To do this ﬁx t with 1 ≤ t ≤ s such that the spherical function ωt is real-
valued. Let Lt be the Markov chain on the set {ω0, · · ·,ω s} which transitions
from ωi to ωj with probability
Lt(ωi,ω j) := dj
|G|
s∑
r=0
|Kr|ωi(gr)ωt(gr)ωj(gr).
As in the group case, one typically wants to choose ωt as close as possible
to the trivial spherical function.
Lemma 4.6 veriﬁes that Lt is a Markov chain which is reversible with
respect to Plancherel measure.
Lemma 4.6. Let t with 0 ≤ t ≤ s be such that the spherical function
ωt is real-valued. Then the transition probabilities of Lt are real and non-
negative and sum to 1. Moreover the chain Lt is reversible with respect to
the Plancherel measure of the pair (G,K ).
Proof. From page 396 of [Mac], if ak
it are deﬁned by
ωiωt =
s∑
k=0
ak
itωk
(where the notation ωiωj denotes the pointwise product), then ak
it are real
and non-negative. Hence Lemma 4.2 implies that Lt(ωi,ω j) is real and non-
negative. Since ωj(g0) = 1 for all j, Lemma 4.3 gives that
s∑
j=0
Lt(ωi,ω j) =
s∑
r=0
|Kr|ωi(gr)ωt(gr) 1
|G|
s∑
j=0
djωj(g0)ωj(gr) = 1.
19
Reversibility ofLt with respect to Plancherel measure is equivalent to show-
ing that
didj|K|
|G|
s∑
r=0
|Kr|ωi(gr)ωt(gr)ωj(r) = didj|K|
|G|
s∑
r=0
|Kr|ωj(gr)ωt(gr)ωi(r).
Both sides are real by the previous paragraph, so the result f ollows by the
assumption that ωt is real valued. □
An exchangeable pair ( W,W ′) to be used in a Stein’s method approach
to studying W can be constructed from the chain Lt in the usual way. First
choosei from Plancherel measure, then choose j with probability Lt(ωi,ω j),
and ﬁnally let ( W,W ′) = (W (ωi),W (ωj)).
Lemma 4.7. E(W ′|W ) = ωt(gu)W .
Proof. From the deﬁnitions and Lemma 4.3,
E(W ′|ωi) = |Ku|1/ 2
|K|1/ 2
s∑
j=0
dj
|G|
s∑
r=0
|Kr|ωi(gr)ωt(gr)ωj(gr)ωj(gu)
= |Ku|1/ 2
|K|1/ 2
s∑
r=0
|Kr|ωi(gr)ωt(gr)
s∑
j=0
dj
|G|ωj(gu)ωj(gr)
= ωt(gu)W (ωi).
The result follows since this depends on ωi only through W . □
Corollary 4.8 is not needed in the sequel but is interesting.
Corollary 4.8. The eigenvalues of Lt areωt(gr) for 0 ≤r ≤s. The func-
tions ψr(ωi) = |Kgr |1/ 2
|K|1/ 2 ωi(gr) are a basis of eigenvectors of Lτ , orthonormal
with respect to the inner product
⟨f1,f 2⟩ =
s∑
i=0
f1(ωi)f2(ωi)di|K|
|G| .
Proof. By the proof of Lemma 4.7, ψr is an eigenvector of Lt with eigenvalue
ωt(gr). The orthonormality assertion follows from Lemma 4.3, and the basis
assertion follows since the number of spherical functions i s equal to the
number of K double cosets of G. □
Lemma 4.9. E(W ′ −W )2 = 2(1 −ωt(gu)).
Proof. This is immediate from Lemmas 2.3 and 4.7. □
Lemma 4.10. E((W ′)2|ωi) = |Ku|
|K|
∑ s
r=0ωi(gr)ωt(gr)p2(Kr).
20
Proof. From the deﬁnitions,
E((W ′)2|ωi) = |Ku|
|K|
s∑
j=0
dj
|G|
s∑
r=0
|Kr|ωi(gr)ωt(gr)ωj(gr)ωj(gu)2
= |Ku|
|K|
s∑
r=0
|Kr|ωi(gr)ωt(gr) 1
|G|
s∑
j=0
djωj(gu)2ωj(gr).
The result follows from Lemma 4.4. □
Note that the sum in Lemma 4.11 begins at r = 1 and so excludes the
r = 0 term which corresponds to the trivial spherical function .
Lemma 4.11.
Var (E[(W ′ −W )2|ωi]) = |Ku|2
|K|
s∑
r=1
p2(Kr)2
|Kr| (ωt(gr) + 1 − 2ωt(gu))2.
Proof. It follows from Lemmas 4.10, 4.9, and 4.7 that
Var (E[(W ′ −W )2|ωi])
= E(E((W ′ −W )2|ωi)2) − 4(1 −ωt(gu))2
= |Ku|2
|K|2 E
[ s∑
r=0
p2(Kr)ωi(gr)ωt(gr) + (1 − 2ωt(gu))ωi(gu)2
] 2
−4(1 −ωt(gu))2
= T1 +T2 +T3 − 4(1 −ωt(gu))2
where
T1 = |Ku|2
|K|2 E
( s∑
r=0
p2(Kr)ωi(gr)ωt(gr)
) 2
T2 = |Ku|2
|K|2 2(1 − 2ωt(gu))
s∑
r=0
p2(Kr)ωt(gr)E
(
ωi(gr)ωi(gu)2)
T3 = |Ku|2
|K|2 (1 − 2ωt(gu))2E(ωi(gu)4).
For reasons similar to the ﬁnite group case, there are useful simpliﬁcations.
Lemma 4.3 implies that
T1 = |Ku|2
|K|
s∑
r=0
p2(Kr)2ωt(gr)2
|Kr| .
Lemma 4.4 gives that
T2 = |Ku|2
|K| 2(1 − 2ωt(gu))
s∑
r=0
p2(Kr)2ωt(gr)
|Kr| .
21
Also, one can write
T3 = |Ku|2
|K|2 (1 − 2ωt(gu))2p4(K0) = |Ku|2
|K| (1 − 2ωt(gu))2
s∑
r=0
p2(Kr)2
|Kr| .
The ﬁrst equality used Lemma 4.4 and the second equality used the assump-
tion that KguK =Kg −1
u K. Hence
T1 +T2 +T3 = |Ku|2
|K|
s∑
r=0
p2(Kr)2
|Kr| (ωt(gr) + 1 − 2ωt(gu))2,
which implies the result since the r = 0 term is 4(1 −ωt(gu))2. □
Lemma 4.12. Letk be a positive integer.
(1) E(W ′ −W )k is equal to
( |Ku|
|K|
) k/ 2 k∑
m=0
(−1)k−m
( k
m
) s∑
r=0
|K|
|Kr|ωt(gr)pm(Kr)pk−m(Kr).
(2) E(W ′ −W )4 = |Ku|2
|K|
∑ s
r=0 [8 (1 −ωt(gu)) − 6 (1 −ωt(gr))] p2(Kr)2
|Kr| .
Proof. For the ﬁrst assertion, note that E((W ′ −W )k|ωi) is equal to
( |Ku|
|K|
) k/ 2 s∑
j=0
dj
|G|
s∑
r=0
|Kr|ωi(gr)ωt(gr)ωj(gr) (ωj(gu) −ωi(gu))k
=
( |Ku|
|K|
) k/ 2 s∑
j=0
dj
|G|
s∑
r=0
|Kr|ωi(gr)ωt(gr)ωj(gr)
·
k∑
m=0
(−1)k−m
( k
m
)
ωj(gu)mωi(gu)k−m
=
( |Ku|
|K|
) k/ 2 k∑
m=0
(−1)k−m
( k
m
)
ωi(gu)k−m
·
s∑
r=0
|Kr|ωi(gr)ωt(gr)
s∑
j=0
dj
|G|ωj(gu)mωj(gr)
=
( |Ku|
|K|
) k/ 2 k∑
m=0
(−1)k−m
( k
m
)
ωi(gu)k−m
s∑
r=0
ωi(gr)ωt(gr)pm(Kr),
22
where the last equality is Lemma 4.4. Hence
E(W ′ −W )k = E(E((W ′ −W )k|ωi))
=
( |Ku|
|K|
) k/ 2 k∑
m=0
(−1)k−m
( k
m
)
·
s∑
r=0
ωt(gr)pm(Kr)
s∑
i=0
di|K|
|G| ωi(gr)ωi(gu)k−m.
The ﬁrst assertion follows from Lemma 4.4 and the fact that ωi(gu) is real.
For the second assertion, one knows from the ﬁrst assertion t hat
E(W ′ −W )4 =
( |Ku|
|K|
) 2 4∑
m=0
(−1)m
( 4
m
) s∑
r=0
|K|
|Kr|ωt(gr)pm(Kr)p4−m(Kr).
The special case t = 0 gives the equation
0 =
( |Ku|
|K|
) 2 4∑
m=0
(−1)m
( 4
m
) s∑
r=0
|K|
|Kr|pm(Kr)p4−m(Kr).
Hence in general, E(W ′ −W )4 is equal to
− |Ku|2
|K|2
4∑
m=0
(−1)m
( 4
m
) s∑
r=0
|K|
|Kr| (1 −ωt(gr))pm(Kr)p4−m(Kr).
Them = 0, 4 terms both vanish since p0(Kr) = 0 if r ⁄= 0. The m = 2 term
is equal to
− 6|Ku|2
|K|
s∑
r=0
(1 −ωt(gr))p2(Kr)2
|Kr| .
Them = 1, 3 terms are equal and together contribute
8|Ku|2
|K|
s∑
r=0
(1 −ωt(gr))p1(Kr)p3(Kr)
|Kr| = 8|Ku|
|K| (1 −ωt(gu))p3(Ku)
= 8|Ku|2
|K|2 (1 −ωt(gu))p4(K0)
= 8|Ku|2
|K| (1 −ωt(gu))
s∑
r=0
p2(Kr)2
|Kr| .
This completes the proof of the second assertion. □
Arguing as in the proof of Theorem 3.13, and using the above le mmas,
one obtains the following result.
Theorem 4.13. Let (G,K ) be a Gelfand pair, and ﬁx a double coset Ku =
KguK of G satisfying KguK = Kg −1
u K. Let ωt be a nontrivial spherical
23
function which is real valued. Choosing ωi from the Plancherel measure of
the pair (G,K ), let W = |Ku|1/ 2
|K|1/ 2 ωi(gu). Then for all real x0,
⏐
⏐
⏐
⏐P(W ≤x0) − 1
√
2π
∫ x0
−∞
e− x2
2 dx
⏐
⏐
⏐
⏐
≤ |Ku|
a|K|
/radicaltp
/radicalvertex
/radicalvertex
√
s∑
r=1
|K|p2(Kr)2
|Kr| (ωt(gr) + 2a − 1)2
+ 1
(π)1/ 4
|Ku|1/ 2
|K|1/ 2
[ s∑
r=0
(
8 − 6(1 −ωt(gr))
a
) |K|p2(Kr)2
|Kr|
] 1/ 4
,
wherea = 1 −ωt(gu).
