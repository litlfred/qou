---
doc_id: arxiv-math-0508291v1
doc_title: "Stein’s Method and Random Character Ratios"
section_id: sec-016-62-central-limit-theorem-for-the-spectrum
section_title: "Central limit theorem for the spectrum"
section_number: 6.2
pages: 44-49
source_pdf: 0508291v1.pdf
source_sha256: d2d541426aaec742
doc_brief: "Stein’s Method and Random Character Ratios — Stein’s method is used to prove limit theorems for random character ratios."
---
is to study Plancherel measure of association schemes, whic h chooses i ∈
{0, · · ·,n } with probability µ i
|X| . More precisely, for s ﬁxed, a central limit
theorem is proved for the random variable W whose value at i ∈ {0, · · ·,n }
is φ s(i)√vs
.
Given t ∈ { 0, · · ·,n }, we deﬁne a Markov chain Lt on the set {0, · · ·,n }
which moves from i to j with probability
Lt(i,j ) := µj
|X|
n∑
r=0
φr(i)φr(t)φr(j)
(vr)2 .
Lemma 6.5. The transition probabilities of Lt are real and non-negative
and sum to 1. Moreover the chain Lt is reversible with respect to Plancherel
measure.
45
Proof. By Theorems 3.6 and 3.8 of [BaI], the Lt(i,j ) are non-negative real
numbers. Next, observe that
n∑
j=0
Lt(i,j ) = 1
|X|
n∑
r=0
φr(i)φr(t)
(vr)2
n∑
j=0
µjφr(j).
Since φ0(j) = 1 for all j, Lemma 6.2 implies that
n∑
j=0
Lt(i,j ) = v0
n∑
r=0
φr(i)φr(t)
(vr)2 δr, 0 = 1.
For the reversibility assertion, it is clear from the deﬁnit ion of Lt that
µi
|X|Lt(i,j ) = µj
|X|Lt(j,i )
for all i,j . □
One uses the chain Lt to construct an exchangeable pair ( W,W ′) in the
usual way. First choose i from Plancherel measure, then choose j with
probabilityLt(i,j ), and ﬁnally let ( W,W ′) = (W (i),W (j)).
Lemma 6.6. E(W ′|W ) =
(
φ s(t)
vs
)
W .
Proof. By the deﬁnitions and Lemma 6.2, one has that
E(W ′|i) = 1√vs
n∑
j=0
Lt(i,j )φs(j)
= 1√vs
1
|X|
n∑
r=0
φr(i)φr(t)
(vr)2
n∑
j=0
µjφs(j)φr(j)
=
( φs(t)
vs
)
W (i).
The result follows since this depends on i only through W . □
Corollary 6.7 will not be used but is worth recording.
Corollary 6.7. The eigenvalues of Lt are φ s(t)
vs
for 0 ≤s ≤n. The functions
ψs(i) = φ s(i)√vs
are a basis of eigenvectors of Lt, orthonormal with respect to
the inner product
⟨f1,f 2⟩ =
n∑
i=0
f1(i)f2(i) µi
|X|.
Proof. The proof of Lemma 6.6 shows that ψs is an eigenvector of Lt with
eigenvalue φ s(t)
vs . The orthonormality assertion follows from Lemma 6.2, and
the basis assertion follows since there are n + 1 eigenvectors. □
Lemma 6.8. E(W ′ −W )2 = 2
(
1 − φ s(t)
vs
)
.
Proof. This is immediate from Lemmas 2.3 and 6.6. □
46
Lemma 6.9. E((W ′)2|i) = vs
∑ n
r=0
φ r(i)φ r (t)
(vr)2 p2(r).
Proof. It follows from the deﬁnitions that
E((W ′)2|i) = 1
vs
n∑
j=0
µj
|X|
n∑
r=0
φr(i)φr(t)φr(j)
(vr)2 φs(j)2
= 1
vs
n∑
r=0
φr(i)φr(t)
(vr)2
n∑
j=0
µj
|X|φs(j)2φr(j).
The result now follows from Lemma 6.3. □
Note that in the next lemma, the sum is over non-zero r.
Lemma 6.10.
Var (E[(W ′ −W )2|i]) = (vs)2
n∑
r=1
p2(r)2
vr
( φr(t)
vr
+ 1 − 2φs(t)
vs
) 2
.
Proof. By Lemmas 6.6, 6.8, and 6.9, Var (E[(W ′ −W )2|i]) is equal to
E(E((W ′ −W )2|i)2) − 4
(
1 −φs(t)
vs
) 2
= E
[
vs
n∑
r=0
φr(i)φr(t)
(vr)2 p2(r) +
(
1 − 2φs(t)
vs
)
W 2
] 2
−4
(
1 − φs(t)
vs
) 2
= T1 +T2 +T3 − 4
(
1 − φs(t)
vs
) 2
,
where
T1 = (vs)2E
( n∑
r=0
φr(i)φr(t)
(vr)2 p2(r)
) 2
T2 = 2
(
1 − 2φs(t)
vs
) n∑
r=0
φr(t)
(vr)2p2(r)E
(
φr(i)φs(i)2)
T3 =
(
1 − 2φs(t)
vs
) 2
E
( φs(i)4
(vs)2
)
.
Next we simplify these terms. By Lemma 6.2,
T1 = (vs)2
n∑
r=0
φr(t)2
(vr)3 p2(r)2.
Lemma 6.3 implies that
T2 = 2(vs)2
(
1 − 2φs(t)
vs
) n∑
r=0
φr(t)
(vr)2p2(r)2.
47
Lemma 6.3 and part 1 of Lemma 6.4 imply that
T3 = (vs)2
(
1 − 2φs(t)
vs
) 2
p4(0) = (vs)2
(
1 − 2φs(t)
vs
) 2 n∑
r=0
p2(r)2
vr
.
Thus
T1 +T2 +T3 = (vs)2
n∑
r=0
p2(r)2
vr
( φr(t)
vr
+ 1 − 2φs(t)
vs
) 2
.
Since p2(0) = 1
vs
, the r = 0 term of T1 +T2 +T3 is equal to 4
(
1 − φ s(t)
vs
) 2
,
proving the result. □
Lemma 6.11. Letk be a positive integer.
(1) E(W ′ −W )k = (vs)k/ 2∑ k
m=0(−1)k−m( k
m
) ∑ n
r=0
φ r(t)
vr
pm(r)pk−m(r)
vr .
(2) E(W ′ −W )4 =v2
s
[ ∑ n
r=0
(
8
(
1 − φ s(t)
vs
)
− 6
(
1 − φ r(t)
vr
))
p2(r)2
vr
]
.
Proof. For the ﬁrst assertion, note that
E((W ′ −W )k|i)
= 1
(vs)k/ 2
n∑
j=0
µj
|X|
n∑
r=0
φr(i)φr(t)φr(j)
(vr)2 (φs(j) −φs(i))k
= 1
(vs)k/ 2
k∑
m=0
(−1)k−m
( k
m
)
φs(i)k−m
n∑
r=0
φr(i)φr(t)
(vr)2
·
n∑
j=0
µj
|X|φs(j)mφr(j)
= 1
(vs)k/ 2
k∑
m=0
(−1)k−m
( k
m
)
φs(i)k−m(vs)m
n∑
r=0
φr(i)φr(t)pm(r)
(vr)2 ,
where the last equality is Lemma 6.3. Consequently,
E((W ′ −W )k) = E(E((W ′ −W )k|i))
= ( vs)k/ 2
k∑
m=0
(−1)k−m
( k
m
)
·
n∑
r=0
φr(t)
(vr)2pm(r)
n∑
i=0
µi
|X|
φs(i)k−mφr(i)
(vs)k−m .
The ﬁrst assertion now follows from Lemma 6.3.
For the second part, the ﬁrst assertion gives that
E(W ′ −W )4 = (vs)2
4∑
m=0
(−1)m
( 4
m
) n∑
r=0
φr(t)
vr
pm(r)p4−m(r)
vr
.
48
By page 654 of [MaSl], φr(0) = vr for all r. Thus specializing to t = 0 shows
that
0 = (vs)2
4∑
m=0
(−1)m
( 4
m
) n∑
r=0
pm(r)p4−m(r)
vr
.
So for general t, one has that
E(W ′ −W )4 = −(vs)2
4∑
m=0
(−1)m
( 4
m
) n∑
r=0
(
1 −φr(t)
vr
) pm(r)p4−m(r)
vr
.
The contribution from the m = 0, 4 terms is 0, since p0(r) = 0 if r ⁄= 0. The
contribution from the m = 2 term is
−6(vs)2
n∑
r=0
(
1 − φr(t)
vr
) p2(r)2
vr
.
Them = 1, 3 terms are equal and together contribute
8(vs)2
n∑
r=0
(
1 − φr(t)
vr
) p1(r)p3(r)
vr
= 8( vs)2
(
1 −φs(t)
vs
) p3(s)
vs
= 8( vs)2
(
1 −φs(t)
vs
) n∑
r=0
p2(r)2
vr
,
where the ﬁnal equality is part 2 of Lemma 6.4. Adding the term s completes
the proof of the second assertion. □
Arguing as in the proof of Theorem 3.13, and using the above le mmas,
one obtains the following result.
Theorem 6.12. Fix s ∈ { 0, · · ·,n }, and let W = φ s(i)
√vs
where i is chosen
from the Plancherel measure of the association scheme. Fix t ∈ {1, · · ·,n }.
Then for all real x0,
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
≤ vs
a
/radicaltp
/radicalvertex
/radicalvertex
√
n∑
r=1
p2(r)2
vr
( φr(t)
vr
+ 1 − 2φs(t)
vs
) 2
+
√vs
(π)1/ 4
[ n∑
r=0
(
8 − 6
a
(
1 − φr(t)
vr
)) p2(r)2
vr
] 1/ 4
,
wherea = 1 − φ s(t)
vs .
49
