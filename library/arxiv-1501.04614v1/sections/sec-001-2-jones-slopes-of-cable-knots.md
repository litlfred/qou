---
doc_id: arxiv-1501.04614v1
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL II"
section_id: sec-001-2-jones-slopes-of-cable-knots
section_title: "Jones slopes of cable knots"
section_number: 2
pages: 3-7
source_pdf: 1501.04614v1.pdf
source_sha256: ebebcae0c1823217
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL II — We continue our study of the degree of the colored Jones polyn omial under knot cabling started in [8]."
---
Let Kp,q be the ( p, q )-cable of a knot K, where q > 1. For n > 0, let Sn be the set of
all k such that
|k| ≤ (n − 1)/ 2 and k ∈
{
Z if n is odd ,
Z + 1
2 if n is even .
By [10], for n > 0 we have
(2.1) JKp,q(n) = vpq(n2−1)/ 4 ∑
k∈Sn
v−pk(qk+1)JK (2qk + 1),
where it is understood that JK(−m) = −JK(m).
Proposition 2.1. Let K be a knot such that for n ≫ 0 we have
d+[JK (n)] = an2 + b(n)n + d(n)
where a is a constant, b(n) and d(n) are periodic functions with b(n) ≤ 0. Let
M1 = max {|b(i) − b(j)| : i ≡ j (mod 2) },
M2 = max {2b(i) + |b(i) − b(j)| + |d(i) − d(j)| : i ≡ j (mod 2) }.
Suppose p − (4a − M1)q < 0 or p − (4a + M1)q > max{0, M 2}. Then for n ≫ 0 we have
d+[JKp,q(n)] = An2 + B(n)n + D(n)
where A is a constant with A ∈ { q2a, pq/ 4}, and B(n), D (n) are periodic functions with
B(n) ≤ 0.
Proof. Fix n ≫ 0. Recall the cabling formula (2.1) of the colored Jones poly nomial
JKp,q(n) = vpq(n2−1)/ 4 ∑
k∈Sn
v−pk(qk+1)JK (2qk + 1).
In the above formula, there is a sum. Under the assumption of t he proposition, we will
show that there is a unique term of the sum whose highest degre e is strictly greater than
4
those of the other terms. This implies that the highest degre e of the sum is exactly equal
to the highest degree of that unique term.
For k ∈ S n let
f (k) := d+[v−pk(qk+1)JK (2qk + 1)] = −pk(qk + 1) + d+[JK (|2qk + 1|)].
The goal is to show that f (k) attains its maximum on Sn at a unique k.
Since d+[JK (n)] is a quadratic quasi-polynomial, f (k) is a piece-wise quadratic poly-
nomial. The above goal will be achieved in 2 steps. In the ﬁrst step we show that f (k)
attains its maximum on each piece at a unique k. Then in the second step we show that
the maximums of f (k) on all the pieces are distinct.
Step 1. Let π be the period of d+[JK (n)]. For ε ∈ {± 1} and 0 ≤ i < π , let hε
i (x) be
the quadratic real polynomial deﬁned by
hε
i (x) := ( −pq + 4q2a)x2 + (−p + 4qa + 2qb(i)ε)x + a + b(i)ε + d(i).
For each k ∈ S n, we have f (k) = hεk
ik (k) for a unique pair ( εk, i k). Let
In := {(εk, i k) | k ∈ S n}.
Then f (k) is a piece-wise quadratic polynomial of exactly |In| pieces, each of which is
associated with a unique pair ( ε, i ) in In.
For each ( ε, i ) ∈ In, let
Sn,ε,i := {k ∈ S n | (εk, i k) = ( ε, i )}
which is the set of all k on the piece associated with ( ε, i ).
The quadratic polynomial hε
i (x) is concave up if p − 4qa < 0, and concave down if
p − 4qa > 0. Hence, for n ≫ 0, hε
i (k) is maximized on the set Sn,ε,i at a unique k = kn,ε,i ,
where
kn,ε,i :=
{
max Sn,ε,i if ( p − 4qa)ε < 0,
min Sn,ε,i if ( p − 4qa)ε > 0.
Note that, as in the proof of [8, Proposition 3.2], we use the a ssumption that b(i) ≤ 0
when ( p − 4qa)ε > 0. Moreover we have
{
|kn,ε,i | → ∞ as n → ∞, if p − 4qa < 0
|kn,ε,i | ≤ π, if p − 4qa > 0.
Step 2. Let
Maxn := max{f (k) | k ∈ S n}.
From step 1 we have Max n = max{hε
i (kn,ε,i ) | (ε, i ) ∈ In}. We claim that
hε1
i1 (kn,ε 1,i 1) ⁄= hε2
i2 (kn,ε 2,i 2)
for ( ε1, i 1) ⁄= (ε2, i 2).
Indeed, let k1 := kn,ε 1,i 1 and k2 := kn,ε 2,i 2. Note that k1 ⁄= k2. Moreover, k1 and k2
are both in Z or 1
2 + Z. As a result we have k1 ± k2 ∈ Z, and i1 − i2 ≡ 2q(k1 − k2) ≡ 0
(mod 2). Let
σ := hε1
i1 (k1) − hε2
i2 (k2).
5
Without loss of generality, we can assume that |k1| ≥ | k2|. Then we write σ = σ ′ +
d(i1) − d(i2) where
σ ′ :=



(k1 − k2)
(
(−p + 4qa)
(
q(k1 + k2) + 1
)
+ 2qb(i1)ε1
)
+
(
b(i1) − b(i2)
)
ε1(2qk2 + 1) if ε1 = ε2,(
(−p + 4qa)(k1 − k2) + 2b(i1)ε1
) (
q(k1 + k2) + 1
)
−
(
b(i1) − b(i2)
)
ε1(2qk2 + 1) if ε1 ⁄= ε2.
We consider the following 2 cases.
Case 1: p − (4a − M1)q < 0. In particular, we have p − 4qa < 0. There are 2 subcases.
Subcase 1.1: ε1 = ε2. Since k1 and k2 have the same sign, we have
|q(k1 + k2) + 1| − |2qk2 + 1| = 2q(|k1| − |k2|) ≥ 0.
Hence
|σ ′| ≥
⏐⏐(−p + 4qa)
(
q(k1 + k2) + 1
)
+ 2qb(i1)ε1
⏐⏐−
⏐⏐(
b(i1) − b(i2)
)(
q(k1 + k2) + 1
) ⏐⏐
≥
(
− p + 4qa − |b(i1) − b(i2)|
)
|q(k1 + k2) + 1| + 2qb(i1).
Since |q(k1 + k2) + 1| → ∞ as n → ∞, and
−p + 4qa − |b(i1) − b(i2)| ≥ − p + 4qa − M1 > 0
we get |σ ′| → ∞ as n → ∞.
Subcase 1.2: ε1 ⁄= ε2. Since k1 and k2 have opposite signs, we have
(q|k1 − k2| + 1) − |2qk2 + 1| ≥ 2q(|k1| − |k2|) ≥ 0.
Hence
|σ ′| ≥
⏐⏐(−p + 4qa)(k1 − k2) + 2b(i1)ε1
⏐⏐− |b(i1) − b(i2)| (q|k1 − k2| + 1)
≥
(
− p + 4qa − q|b(i1) − b(i2)|
)
|k1 − k2| − |b(i1) − b(i2)| + 2b(i1).
Since |k1 − k2| → ∞ as n → ∞, and
−p + 4qa − q|b(i1) − b(i2)| ≥ − p + 4qa − qM1 > 0,
we get |σ ′| → ∞ as n → ∞.
Case 2: p − (4a + M1)q > max{0, M 2}. There are 2 subcases.
Subcase 2.1: ε1 = ε2. Note that q(k1 + k2) + 1 and ε1 have the same sign. Moreover,
both −p + 4qa and 2 qb(i1) are non-positive. As in subcase 1.1 we have
|σ ′| ≥
⏐⏐(−p + 4qa)
(
q(k1 + k2) + 1
)
+ 2qb(i1)ε1
⏐⏐−
⏐⏐(
b(i1) − b(i2)
)(
q(k1 + k2) + 1
) ⏐⏐
=
(
p − 4qa − |b(i1) − b(i2)|
)
|q(k1 + k2) + 1| − 2qb(i1).
Since p − 4qa − |b(i1) − b(i2)| ≥ p − 4qa − M1 > max{0, M 2}, we get
|σ ′| > M 2 − 2qb(i1) ≥ |d(i1) − d(i2)|.
6
Subcase 2.2: ε1 ⁄= ε2. Note that k1 − k2 and ε1 have the same sign. Moreover, both
−p + 4qa and 2 qb(i1) are non-positive. As in subcase 1.2 we have
|σ ′| ≥
⏐⏐(−p + 4qa)(k1 − k2) + 2b(i1)ε1
⏐⏐− |b(i1) − b(i2)| (q|k1 − k2| + 1)
=
(
p − 4qa − q|b(i1) − b(i2)|
)
|k1 − k2| − |b(i1) − b(i2)| − 2b(i1).
Since p − 4qa − q|b(i1) − b(i2)| ≥ p − 4qa − qM1 > max{0, M 2}, we get
|σ ′| > M 2 − |b(i1) − b(i2)| − 2b(i1) ≥ |d(i1) − d(i2)|.
In all cases, for n ≫ 0 we have |σ ′| > |d(i1) − d(i2)|. Hence
σ = σ ′ + d(i1) − d(i2) ⁄= 0.
We have proved that f (k) attains its maximum on Sn at a unique k. More precisely, there
exists a unique ( εn, i n) ∈ In such that hε
in(kn,ε n,i n) = Max n.
Equation (1.4) then implies that
d+[JKp,q(n)] = pq(n2 − 1)/ 4 + hεn
i (kn,ε n,i n).
If p − 4qa < 0 then kn,ε n,i n = εn(n/ 2 + sn), where sn is a periodic sequence and
sn ≤ −1/ 2. We have
d+[JKp,q(n)] = q2an2 +
(
(−p + 4qa)(qsn + εn/ 2) + qb(in)
)
n − pq/ 4
+ (−p + 4qa)sn(qsn + εn) + 2qb(in)sn + a + b(in)εn + d(in).
In this case we have
B(n) = ( −p + 4qa)(qsn + εn/ 2) + qb(in) < 0,
since qsn + εn/ 2 ≤ −q/ 2 + 1/ 2 < 0 and b(in) ≤ 0.
If p − 4qa > 0 then kn,ε n,i n = sn, where sn is a periodic function. We have
d+[JKp,q(n)] = pq(n2 − 1)/ 4 + (−p + 4qa)sn(qsn + 1) + 2qb(in)εnsn
+ a + b(in)εn + d(in).
In this case we have B(n) = 0.
This completes the proof of Proposition 2.1. □
Remark 2.2. The proof of Proposition 2.1 can be slightly modiﬁed to give t he following.
Let K be a knot such that for n ≫ 0 we have
d+[JK (n)] = a(n)n2 + b(n)n + d(n)
where a(n), b(n) and d(n) are periodic functions with b(n) ≤ 0. Let
aM = max{a(n)}, a m = min{a(n)}
and
M1 = max {|b(i) − b(j)| : i ≡ j (mod 2) },
M2 = max {2b(i) + |b(i) − b(j)| + |d(i) − d(j)| : i ≡ j (mod 2) }.
(1) Suppose p − (4am − M1)q < 0. Then for n ≫ 0 we have
d+[JKp,q(n)] = A(n)n2 + B(n)n + D(n)
where A(n), B(n) and D(n) are periodic functions with {A(n)} ⊂ { q2a(n)} and B(n) < 0.
7
(2) Suppose {a(n)} has period at most 2 and p − (4aM + M1)q > max{0, M 2}. Then
for n ≫ 0 we have
d+[JKp,q(n)] = pqn2/ 4 + O(1).
We now recall the following result about the behavior of the b oundary slopes under
knot cabling in [8].
Theorem 2.3. [8] For every knot K ⊂ S3 and (p, q ) coprime integers we have
(
q2bsK ∪ {pq}
)
⊂ bsKp,q.
Proposition 2.1 and Theorem 2.3 imply Theorem 1.1 stated in t he introduction.
Example 2.4. Theorem 1.1 applies to the non-alternating knots 8 20, 943, 944 (of period
3) in Section 4 of [4].
For K = 8 20 we have
d+[JK (n)] =
{
2n2/ 3 − n/ 2 − 1/ 6 if n ⁄≡0 (mod 3)
2n2/ 3 − 5n/ 6 − 1/ 2 if n ≡ 0 (mod 3) .
Hence Kp,q satisﬁes Conjectures 1.2 and 1.3 if p − 7
3 q < 0 or p − 3q > 0.
For K = 9 43 we have
d+[JK (n)] =
{
8n2/ 3 − n/ 2 − 13/ 6 if n ⁄≡0 (mod 3)
8n2/ 3 − 5n/ 6 − 7/ 2 if n ≡ 0 (mod 3) .
Hence Kp,q satisﬁes Conjectures 1.2 and 1.3 if p − 31
3 q < 0 or p − 11q > 2
3 .
For K = 9 44 we have
d+[JK (n)] =
{
7n2/ 6 − n − 1/ 6 if n ⁄≡0 (mod 3)
7n2/ 6 − 4n/ 3 − 1/ 2 if n ≡ 0 (mod 3) .
Hence Kp,q satisﬁes Conjectures 1.2 and 1.3 if p − 13
3 q < 0 or p − 5q > 0.
