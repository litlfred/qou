---
doc_id: arxiv-math-9905032v2
doc_title: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS"
section_id: sec-026-22-a-borodin-a-okounkov-and-g-olshanski
section_title: "A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI"
section_number: 22
pages: 22-23
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
doc_brief: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
Assume, therefore, that d is ﬁnite. Observe that for any bounded
increment ∆ x we have
(3.6) F (x + ∆ x, z) = cos
(√z G(u) + G′(u) ∆ x + π
4
)
H(u)1/ 2
+ O
((∆ x)2
√z econst |z−n|/ √n
)
,
and, in particular, the last term is o
(
econst |z−n|/ √n)
. Using the trigono-
metric identity
cos (A) cos (B + C) − cos (A + C) cos (B) = sin ( C) sin (A − B) ,
and observing that
G′(u) = arccos( u/2) , sin(G′(u)) =
√
4 − u2
2 = H(u)
π ,
we compute
F (xn; z) F (yn + 1; z) − F (xn + 1; z) F (yn; z) =
1
π sin
(
arccos
( xn
2√z
)
(xn − yn)
)
+ o
(
econst |z−n|/ √n
)
.
Since, by hypothesis,
xn√z → a , (xn − yn) → d ,
and d ⁄= 0, the lemma follows.
Remark 3.6. Below we shall need this lemma for a variable sequence
X = {xn, yn}. Therefore, let us spell out explicitly under what con-
ditions on X the estimates in Lemma 3.5 remain uniform. We need
the sequences xn√n and yn√n to converge uniformly; then, in particular,
the ratios xn√n and yn√n are uniformly bounded away from ±2. Also, we
need ℑxn and ℑyn to be uniformly bounded. Finally, we need |d| to be
uniformly bounded from below.
Proof of Proposition. First, we check the condition (3.2). In the case
d ⁄= 0 this was done in the previous lemma. Suppose, therefore, t hat
{xn} is a regular sequence in Z≥0 and consider the asymptotics of
J(xn, xn; z).
Because the function J(x, y; z) is an entire function of x and y we
have
J(x, x; z) = 1
2π
∫ 2π
0
J
(
x, x + reit; z
)
dt ,(3.7)
ASYMPTOTICS OF PLANCHEREL MEASURES 23
where r is arbitrary; we shall take r to be some small but ﬁxed number.
From the previous lemma we know that
J
(
x, x + reit; z
)
= 1
πreit sin
(
ω
( x√z
)
reit
)
+ o
(
econst |z−n|/ √n
)
.
From the above remark it follows that this estimate is unifor m in t.
This implies the property (3.2) for J(xn, xn; z).
To prove the estimate (3.1) we use Schl¨ aﬂi’s integral repre sentation
(see Section 6.21 in [39])
(3.8) Jx(2√
z) = 1
π
∫ π
0
cos
(
xt − 2√z sin t
)
dt −
sin πx
π
∫ ∞
0
e−xt−2√z sinh t dt ,
which is valid for | arg z| < π and even for arg z = ±π provided ℜx > 0
or x ∈ Z.
If x ∈ Z then the second summand in (3.8) vanishes and and the
ﬁrst is O
(
econst |z|1/ 2
)
uniformly in x ∈ Z. This implies the estimate
(3.1) provided d ⁄= 0.
It remains, therefore, to check (3.1) for J(xn, xn; z) where {xn} ∈ Z is
a regular sequence. Again, we use (3.7). Observe, that since ℜ√z ≥ 0
the second summand in (3.8) is uniformly small provided ℑx is bounded
from above and ℜx is bounded from below. Therefore, (3.7) produces
the (3.1) estimate for xn ≥ 1. For xn ≤ 0 we use the relation (2.13)
and the reccurence (2.16) to obtain the estimate.
Proof of Theorem 3. Let X(n) be a regular sequence and let the num-
bers ai and dij be deﬁned by (1.10), (1.11). We shall assume that
|ai| < 2 for all i. The validity of the theorem in the case when |ai| ≥ 2
for some i will be obvious form the results of the next section.
We have
̺θ (X(n)) = e−θ
∞∑
k=0
̺(k, X(n)) θk
k!(3.9)
= det
[
J(xi(n), xj(n))
]
1≤i,j ≤s
.(3.10)
where the ﬁrst line is the deﬁnition of ̺θ and the second is Theorem
