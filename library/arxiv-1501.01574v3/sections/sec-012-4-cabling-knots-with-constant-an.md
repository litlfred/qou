---
doc_id: arxiv-1501.01574v3
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL"
section_id: sec-012-4-cabling-knots-with-constant-an
section_title: "Cabling knots with constant a(n)"
section_number: 4
pages: 18-22
source_pdf: 1501.01574v3.pdf
source_sha256: 8af5d6264a0ad5e0
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL — We study the behavior of the degree of the colored Jones polyn omial and the boundary slopes of knots under the operation of cabling."
---
In Section 3 we studied the behavior of d+[JK (n)] under knot cabling for knots of
period at most two. In this section we study knots with period greater than two under
the additional hypothesis that, for n ≫ 0 we have a(n) = a, where a is a constant. In this
case, by abusing the terminology, we will say that a(n) is constant. The main result in
this section is the following.
Theorem 4.1. Let K be a knot such that for n ≫ 0 we have
d+[JK (n)] = an2 + b(n)n + d(n)
where a is a constant, b(n) and d(n) are periodic functions with b(n) ≤ 0. Let
M1 = max {|b(i) − b(j)| : i ≡ j (mod 2) },
M2 = max {2b(i) + |b(i) − b(j)| + |d(i) − d(j)| : i ≡ j (mod 2) }.
Suppose p − (4a − M1)q < 0 or p − (4a + M1)q > max{0, M2}. Then for n ≫ 0 we have
d+[JKp,q(n)] = An2 + B(n)n + D(n)
where A is a constant, and B(n), D(n) are periodic functions with B(n) ≤ 0. Moreover,
if jsK ⊂ bsK then jsKp,q ⊂ bsKp,q.
As a corollary of Theorem 4.1 and Theorem 2.2 we obtain the fol lowing result which
implies, in particular, that for knots with constant a(n) the Slope Conjecture is closed
under cabling for inﬁnitely many pairs ( p, q).
Corollary 4.2. Let K be a knot such that for n ≫ 0 we have
d+[JK (n)] = an2 + b(n)n + d(n)
19
where a is a constant, b(n) and d(n) are periodic functions with b(n) ≤ 0. Let M1, M2 be
as in the statement of Theorem 4.1. If K satisﬁes the Slope Conjecture, then Kp,q satisﬁes
the conjecture provided that p − (4a − M1)q < 0 or p − (4a + M1)q > max{0, M2}.
Example 4.3. As an illustration we apply Theorem 4.1 and Corollary 4.2 to t he knots
820, 943, 944. By [10, Section 4], these are the only knots, with at most nin e crossings,
that have Jones period larger than 2. Indeed, the period of th ese knots is 3. Another
application of Theorem 4.1 will be illustrated in Example 6. 3.
For K = 8 20 we have
d+[JK (n)] =
{
2n2/3 − n/2 − 1/6 if n ⁄≡0 (mod 3)
2n2/3 − 5n/6 − 1/2 if n ≡ 0 (mod 3) .
Hence Kp,q satisﬁes the Slope Conjecture if p − 7
3 q < 0 or p − 3q > 0.
For K = 9 43 we have
d+[JK (n)] =
{
8n2/3 − n/2 − 13/6 if n ⁄≡0 (mod 3)
8n2/3 − 5n/6 − 7/2 if n ≡ 0 (mod 3) .
Hence Kp,q satisﬁes the Slope Conjecture if p − 31
3 q < 0 or p − 11q > 2
3 .
For K = 9 44 we have
d+[JK (n)] =
{
7n2/6 − n − 1/6 if n ⁄≡0 (mod 3)
7n2/6 − 4n/3 − 1/2 if n ≡ 0 (mod 3) .
Hence Kp,q satisﬁes the Slope Conjecture if p − 13
3 q < 0 or p − 5q > 0.
Theorem 4.1 follows from Theorem 1.2 and the following propo sition.
Proposition 4.4. Let K be a knot such that for n ≫ 0 we have
d+[JK (n)] = an2 + b(n)n + d(n)
where a is a constant, b(n) and d(n) are periodic functions with b(n) ≤ 0. Let
M1 = max {|b(i) − b(j)| : i ≡ j (mod 2) },
M2 = max {2b(i) + |b(i) − b(j)| + |d(i) − d(j)| : i ≡ j (mod 2) }.
Suppose p − (4a − M1)q < 0 or p − (4a + M1)q > max{0, M2}. Then for n ≫ 0 we have
d+[JKp,q(n)] = An2 + B(n)n + D(n)
where A is a constant with A ∈ { q2a, pq/4}, and B(n), D(n) are periodic functions with
B(n) ≤ 0.
Proof. Fix n ≫ 0. Recall the cabling formula (3) of the colored Jones polyno mial
JKp,q(n) = vpq(n2−1)/ 4 ∑
k∈Sn
v−pk(qk+1)JK (2qk + 1).
In the above formula, there is a sum. As in the proof of Proposi tion 3.2 we will show that,
under the assumption of the proposition, there is a unique te rm of the sum whose highest
20
degree is strictly greater than those of the other terms. Thi s implies that the highest
degree of the sum is exactly equal to the highest degree of tha t unique term.
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
ik (k) for a unique pair ( εk, ik). Let
In := {(εk, ik) | k ∈ S n}.
Then f (k) is a piece-wise quadratic polynomial of exactly |In| pieces, each of which is
associated with a unique pair ( ε, i) in In.
For each ( ε, i) ∈ In, let
Sn,ε,i := {k ∈ S n | (εk, ik) = ( ε, i)}
which is the set of all k on the piece associated with ( ε, i).
The quadratic polynomial hε
i (x) is concave up if p − 4qa < 0, and concave down if
p − 4qa > 0. Hence, for n ≫ 0, hε
i (k) is maximized on the set Sn,ε,i at a unique k = kn,ε,i ,
where
kn,ε,i :=
{
max Sn,ε,i if ( p − 4qa)ε < 0,
min Sn,ε,i if ( p − 4qa)ε > 0.
Note that, as in the proof of Proposition 3.2, we use the assum ption that b(i) ≤ 0 when
(p − 4qa)ε > 0. Moreover we have
{
|kn,ε,i | → ∞ as n → ∞, if p − 4qa < 0
|kn,ε,i | ≤ π, if p − 4qa > 0.
Step 2. Let
Maxn := max{f (k) | k ∈ S n}.
From step 1 we have Max n = max{hε
i (kn,ε,i ) | (ε, i) ∈ In}. We claim that
hε1
i1 (kn,ε 1,i 1) ⁄= hε2
i2 (kn,ε 2,i 2)
for ( ε1, i1) ⁄= (ε2, i2).
Indeed, let k1 := kn,ε 1,i 1 and k2 := kn,ε 2,i 2. Note that k1 ⁄= k2. Moreover, k1 and k2
are both in Z or 1
2 + Z. As a result we have k1 ± k2 ∈ Z, and i1 − i2 ≡ 2q(k1 − k2) ≡ 0
(mod 2). Let
σ := hε1
i1 (k1) − hε2
i2 (k2).
21
Without loss of generality, we can assume that |k1| ≥ | k2|. Then we write σ = σ′ +
d(i1) − d(i2) where
σ′ :=
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
Case 1: Suppose that p − (4a − M1)q < 0. In particular, we have p − 4qa < 0. There
are 2 subcases.
Subcase 1.1: We have ε1 = ε2. Since k1 and k2 have the same sign, we have
|q(k1 + k2) + 1| − |2qk2 + 1| = 2q(|k1| − |k2|) ≥ 0.
Hence
|σ′| ≥
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
we get |σ′| → ∞ as n → ∞.
Subcase 1.2: We have ε1 ⁄= ε2. Since k1 and k2 have opposite signs, we have
(q|k1 − k2| + 1) − |2qk2 + 1| ≥ 2q(|k1| − |k2|) ≥ 0.
Hence
|σ′| ≥
⏐⏐(−p + 4qa)(k1 − k2) + 2b(i1)ε1
⏐⏐− |b(i1) − b(i2)| (q|k1 − k2| + 1)
≥
(
− p + 4qa − q|b(i1) − b(i2)|
)
|k1 − k2| − |b(i1) − b(i2)| + 2b(i1).
Since |k1 − k2| → ∞ as n → ∞, and
−p + 4qa − q|b(i1) − b(i2)| ≥ − p + 4qa − qM1 > 0,
we get |σ′| → ∞ as n → ∞.
Case 2: Suppose that p − (4a + M1)q > max{0, M2}. There are 2 subcases.
Subcase 2.1: We have ε1 = ε2. Note that q(k1 + k2) + 1 and ε1 have the same sign.
Moreover, both −p + 4qa and 2 qb(i1) are non-positive. As in subcase 1.1 we have
|σ′| ≥
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
Since p − 4qa − |b(i1) − b(i2)| ≥ p − 4qa − M1 > max{0, M2}, we get
|σ′| > M 2 − 2qb(i1) ≥ |d(i1) − d(i2)|.
22
Subcase 2.2: We have ε1 ⁄= ε2. Note that k1 − k2 and ε1 have the same sign. Moreover,
both −p + 4qa and 2 qb(i1) are non-positive. As in subcase 1.2 we have
|σ′| ≥
⏐⏐(−p + 4qa)(k1 − k2) + 2b(i1)ε1
⏐⏐− |b(i1) − b(i2)| (q|k1 − k2| + 1)
=
(
p − 4qa − q|b(i1) − b(i2)|
)
|k1 − k2| − |b(i1) − b(i2)| − 2b(i1).
Since p − 4qa − q|b(i1) − b(i2)| ≥ p − 4qa − qM1 > max{0, M2}, we get
|σ′| > M 2 − |b(i1) − b(i2)| − 2b(i1) ≥ |d(i1) − d(i2)|.
In all cases, for n ≫ 0 we have |σ′| > |d(i1) − d(i2)|. Hence
σ = σ′ + d(i1) − d(i2) ⁄= 0.
We have proved that f (k) attains its maximum on Sn at a unique k. More precisely, there
exists a unique ( εn, in) ∈ In such that hε
in(kn,ε n,i n) = Max n.
Equation (3) then implies that
d+[JKp,q(n)] = pq(n2 − 1)/4 + hεn
i (kn,ε n,i n).
If p − 4qa < 0 then kn,ε n,i n = εn(n/2 + sn), where sn is a periodic sequence and
sn ≤ −1/2. We have
d+[JKp,q(n)] = q2an2 +
(
(−p + 4qa)(qsn + εn/2) + qb(in)
)
n − pq/4
+ (−p + 4qa)sn(qsn + εn) + 2qb(in)sn + a + b(in)εn + d(in).
In this case we have
B(n) = ( −p + 4qa)(qsn + εn/2) + qb(in) < 0,
since qsn + εn/2 ≤ −q/2 + 1/2 < 0 and b(in) ≤ 0.
If p − 4qa > 0 then kn,ε n,i n = sn, where sn is a periodic function. We have
d+[JKp,q(n)] = pq(n2 − 1)/4 + (−p + 4qa)sn(qsn + 1) + 2qb(in)εnsn
+ a + b(in)εn + d(in).
In this case we have B(n) = 0.
This completes the proof of Proposition 4.4. □
