---
doc_id: 0306345v1
doc_title: "Published: 16 June 2003 Skein-theoretical derivation of some formulas of Habiro Gregor Masbaum"
section_id: sec-004-4-another-formula-for-the-coeﬃcients-of-ω-p
section_title: "Another formula for the coeﬃcients of ω p"
section_number: 4
pages: 12-17
source_pdf: 0306345v1.pdf
source_sha256: 936aa08026b2683b
doc_brief: "Skein-theoretical derivation of some formulas of Habiro — We use skein theory to compute the coecients of certain power series considered by Habiro in his theory ofsl2 invariants of integral homol"
duplicate_of: "agt-v3-n1-p17-p"
---
Following Habiro, we introduce the polynomials R′
n = ({n}!)−1Rn and write
ω p =
∞∑
n=0
c′
n,p R′
n , (34)
where
c′
n,p = {n}! cn,p .
The aim of this section is to show that c′
n,p is a Laurent polynomial, i.e. that
c′
n,p ∈ Z[A±]. This fact was shown by Habiro [H3] using the quantum group
Uqsl2 . Observe that by (9) and (7), we already know this fact for p = ±1:
c′
n, 1 = (−1)nan(n+3)/ 2 , c ′
n, −1 = a−n(n+3)/ 2 .
(But Formula (33) tells us only that
c′
n,p = 1
(a − a−1)n
n∑
k=0
(−1)kµ p
2k[2k + 1] [n]!
[n + k + 1]! [n − k]! , (35)
from which it is not clear that c′
n,p ∈ Z[A±].)
To do so, we will replace Formula (32) in the previous section by Formula (42)
below. For this, we need the following two Lemmas.
Algebraic & Geometric Topology, Volume 3 (2003)
Skein-theoretical derivation of some formulas of Habiro 549
Lemma 4.1 We have
n
n =
n∑
k=0
Cn,k
k k
n − k
n − k
,
where
Cn,k = an(n−k)
[n
k
] n∏
j=n−k+1
(1 − a−2j) . (36)
Here, as usual, [n
k
]
= [n][n − 1] · · · [n − k + 1]
[k]! .
Proof For 0 ≤ p ≤ n, let us write, more generally,
n
p =
n∑
k=0
Cn,p,k
k k
n − k
p − k
.
First, we consider the case p = 1. By induction on n, it is easy to prove that
n
= an
n
+ an−1(1 − a−2n)
n − 1
(recall a = A2 ). Using this, we now ﬁx n and do induction on p to obtain the
recursion formula
Cn,p +1,k = an−2kCn,p,k + an−2k+1(1 − a−2(n−k+1))Cn,p,k −1 . (37)
Here we have used the following two facts which follow from th e deﬁning prop-
erties of the Jones-Wenzl idempotents. 2
p + q p
q =
p + q p
q (38)
p + q p
q = A−pq
p + q p
q (39)
2Equation (39) is a special case of the half-twist coeﬃcient.
Algebraic & Geometric Topology, Volume 3 (2003)
550 Gregor Masbaum
Note that the coeﬃcients Cn,p,k behave like the binomial coeﬃcients
( p
k
)
in that
Cn, 0, 0 = 1, and Cn,p,k = 0 for k < 0 or k > p . It follows that the recursion
formula (37) determines the Cn,p,k uniquely. One ﬁnds
Cn,p,k = ap(n−k)
[p
k
] n∏
j=n−k+1
(1 − a−2j) .
Specializing to the case p = n, this proves the Lemma.
Remark 4.2 The coeﬃcient Cn,n was computed by a diﬀerent method in
[A, Prop. 4.4]. Knowing this coeﬃcient would be enough to obt ain Habiro’s
formula (7) for ω (see Remark 4.4 below). Unfortunately, the method of [A]
does not give the coeﬃcients Cn,k for k ⁄= n, which we will need to obtain a
formula for ω p .
Lemma 4.3 We have
n
n k k
n − k
n − k
= µ 2
n−k
µ 2
n
k k
n − k
n − k
(40)
Proof The left hand side of (40) is equal to
k k
n − k
n − k
By an isotopy, this becomes
µ −2
k k k
n − k
n − k
Applying the coeﬃcients δ(n; n − k, k )−2 and δ(n; k, n − k)−2 , which are both
equal to µ kµ n−kµ −1
n (see also (39)), we see that this is equal to the right hand
side of (40).
Algebraic & Geometric Topology, Volume 3 (2003)
Skein-theoretical derivation of some formulas of Habiro 551
Let C (p)
n,k be the coeﬃcient deﬁned by the expansion
n
n · · · =
n∑
k=0
C (p)
n,k
k k
n − k
n − k
, (41)
(where the diagram on the left hand side of (41) has 2 p crossings). Putting the
two preceding Lemmas together, we may obtain a formula for th is coeﬃcient.
In particular, it follows by induction on p that C (p)
n,k is a Laurent polynomial
divisible by ∏ n
j=n−k+1(1 − a2j).
We are interested in the coeﬃcient C (p)
n,n , since we have
2n
2n
n
n
· · · = C (p)
n,n
2n
2n
nn
= C (p)
n,n
2n
(42)
(where there are 2 p crossings in the diagram on the left). Using (30) and (31)
from Section 3, it follows that
µ −2p
n cn,p (−1)n({n}!)2 = C (p)
n,n
and therefore
c′
n,p = {n}! cn,p = (−1)nµ 2p
n ({n}!)−1C (p)
n,n . (43)
As already observed, C (p)
n,n is divisible by
n∏
j=1
(1 − a2j) = a−n(n+1)/ 2{n}!
and hence c′
n,p is indeed a Laurent polynomial.
Remark 4.4 In the case p = 1, we have
C (1)
n,n = Cn,n = a−n(n+1)/ 2{n}! . (44)
Plugging this into (43), we get
c′
n, 1 = (−1)nan2+2na−n(n+1)/ 2 = (−1)nan(n+3)/ 2 ,
giving another proof of Habiro’s formula (7) for cn, 1 .
Algebraic & Geometric Topology, Volume 3 (2003)
552 Gregor Masbaum
Here is an explicit formula for C (p)
n,n which follows from (36) and (40). The sum is
over all multi-indices k = (k1, . . . , k p) such that ki ≥ 0 for all i, and ∑ ki = n.
For convenience, put si = k1 + . . . + ki and ri = n − si = ki+1 + . . . + kp , and
deﬁne
ϕ (k) =
p−1∑
i=1
ri(ri−1 + ri + 2) . (45)
C (p)
n,n =
∑
k
Cn,k 1
µ 2
n−k1
µ 2
n
Cn−k1,k 2
µ 2
n−k1−k2
µ 2
n
· · ·Cn−sp− 2,k p− 1
µ 2
n−sp− 1
µ 2
n
Cn−sp− 1,k p
= µ 2−2p
n
∑
k
( p−1∏
i=1
µ 2
ri
) p∏
i=1
Cri− 1,k i
= µ 2−2p
n


n∏
j=1
(1 − a−2j)

∑
k
( p−1∏
i=1
ari2+2ri
) p−1∏
i=1
(
ari− 1ri
[ri−1
ki
])
= µ 2−2p
n a−n(n+1)/ 2{n}!
∑
k
aϕ (k)
[ n
k
]
where we have put, as usual,
[ n
k
]
= [n]!
[k1]! · · · [kp]! .
In view of (43), and using µ 2
n = an2+2n , we obtain the following ﬁnal result:
Theorem 4.5 (Habiro [H3]) For p ≥ 1, the coeﬃcients c′
n,p of ω p in (34) are
given by
c′
n,p = (−1)nan(n+3)/ 2 ∑
k
=(k1,...,kp)
ki≥ 0, ∑ ki=n
aϕ (k)
[ n
k
]
. (46)
where ϕ (k) is deﬁned in (45).
Remark 4.6 Since c′
n, −p = (−1)n
c′
n,p , this also determines the coeﬃcients of
negative powers of ω .
Remark 4.7 In [H3], Habiro has obtained a similar formula using the quan tum
group Uqsl2 .
Algebraic & Geometric Topology, Volume 3 (2003)
Skein-theoretical derivation of some formulas of Habiro 553
Example: Assume p = 2. We may write k = (k, n − k). Then
c′
n, 2 = (−1)nan(n+3)/ 2
n∑
k=0
a(n−k)(n+n−k+2)
[n
k
]
= (−1)na(5n2+7n)/ 2
n∑
k=0
ak2−2k−3nk
[n
k
]
