---
doc_id: arxiv-math-0508291v1
doc_title: "Stein’s Method and Random Character Ratios"
section_id: sec-008-43-example-the-hypercube
section_title: "Example: The Hypercube"
section_number: 4.3
pages: 23-25
source_pdf: 0508291v1.pdf
source_sha256: d2d541426aaec742
doc_brief: "Stein’s Method and Random Character Ratios — Stein’s method is used to prove limit theorems for random character ratios."
---
2 con-
sists of n-tuples of 0’s and 1’s. Random walk on it proceeds by picking a
random coordinate and changing it. The spectrum of this rand om walk is
well known; for each 0 ≤i ≤n there is an eigenvalue 1 − 2i
n occurring with
multiplicity
( n
i
)
(see for instance page 28 of [Di]). Thus by the usual central
limit theorem for the binomial distribution, the spectrum o f the hypercube
is asymptotically normal with an error term O(n−1/ 2). The purpose of this
subsection is to revisit this classical result from the view point of Gelfand
pairs, illustrating the construction of Subsection 4.2.
To begin, note from the remarks on page 58 of [Di], that the hyp ercube
can be viewed as G/K for a certain Gelfand pair ( G,K ). Namely G is
the semidirect product of Zn
2 with Sn, where the group multiplication is
(x,π )(y,τ ) = (x +π(y),πτ ), where τ (x) permutes the coordinates of x. K
is the subgroup {(0,π ) : π ∈ Sn}. The induced module 1 G
K decomposes as
⊕n
r=0Vr wheredr =
( n
r
)
. Thus the Plancherel measure chooses i ∈ {0, · · ·,n }
with probability (n
i)
2n . For 0 ≤ r ≤ n, the double coset Kr in G consists of
elements (x,π ) where x has r coordinates equal to 1. Thus |Kr| =
( n
r
)
n!,
and as usual let gr denote some element of Kr. The spherical function ωi
(0 ≤i ≤n) is given by
ωi(gr) = 1( n
i
)
i∑
m=0
(−1)m
( r
m
)( n −r
i −m
)
,
which is a Krawtchouk polynomial if one overlooks the
( n
i
)
in the denomi-
nator.
The following result emerges from Theorem 4.13. Since ωi(g1) = 1 − 2i
n (or
by Lemma 4.5), it can be seen as a central limit theorem for the spectrum
of random walk on the hypercube.
24
Theorem 4.14. Let W = √
nωi(g1) where i is chosen from Plancherel
measure. Then for all real x0,
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
⏐ ≤
( 8
πn
) 1/ 4
.
Proof. Apply Theorem 4.13 with u = 1 and t = 1. Then a = 2
n . One
computes that p2(K0) = 1
n , p2(K2) = 1 − 1
n , and that p2(Kr) = 0 for all
r ⁄= 0, 2. Since ω1(g2) = 1 − 4
n , one has that ω1(g2) + 2a − 1 = 0. Thus the
ﬁrst error term in Theorem 4.13 is 0. The second error term in T heorem
4.13 is computed to be
( 8
πn
) 1/ 4, implying the result. □
To getO(n−1/ 2) bounds by Stein’s method, it will be shown that |W ′−W |
is bounded, so that one can use the version of Stein’s method i n Theorem
2.2 instead of that in Theorem 2.1. The boundedness of |W ′ −W | will follow
from Lemma 4.15, which proves that L1 is in fact a birth-death chain.
Lemma 4.15. The chain L1 on the set {0, · · ·,n } is a birth-death chain
with transition probabilities
L1(i,j ) =
{ i
n if j =i − 1
1 − i
n if j =i + 1
Proof. From the three term recurrence for Krawtchouk polynomials o n page
152 of [MaSl], it follows that
(i + 1)
( n
i + 1
)
ωi+1(gr) = (n − 2r)
( n
i
)
ωi(gr) − (n −i + 1)
( n
i − 1
)
ωi−1(gr).
Since n − 2r =nω1(gr), one obtains that
n
( n
i
)
ω1(gr)ωi(gr) = (i + 1)
( n
i + 1
)
ωi+1(gr) + (n −i + 1)
( n
i − 1
)
ωi−1(gr).
Simplifying one obtains the relation
ω1(gr)ωi(gr) =
(
1 − i
n
)
ωi+1(gr) +
( i
n
)
ωi−1(gr).
The result now follows from Lemma 4.2 and the deﬁnition of L1. □
Now an O(n−1/ 2) error term is established.
Theorem 4.16. Let W = √nωi(g1) where i is chosen from Plancherel
measure. Then for all real x0,⏐
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
⏐ ≤ 5n−1/ 2.
Proof. Apply the variation of Theorem 4.13 which would arise from us ing
Theorem 2.2 instead of Theorem 2.1. Recall that a = 2
n . Also |W ′ −W | ≤ A
with A = 2√n since L1 is a birth-death chain. As explained in the proof of
Theorem 4.14, Var (E[(W ′ −W )2|W ]) = 0. The result follows. □
25
A a ﬁnal remark, Lemma 4.15 shows that L1 is closely related to the
birth-death chain used by Stein [Stn1] in proving a central l imit theorem
for X1 +... +Xn, where the X ′s are independent and each equal to 0 or 1
with probability 1/2. To form an exchangeable pair Stein cho se a random
l ∈ {1, · · ·,n } and then replaced Xl by a new random variable which is also
0 or 1 with probability 1/2 and independent of all of the X ′s. The chain L1
would arise by picking a random index l and switching the value of Xl.
