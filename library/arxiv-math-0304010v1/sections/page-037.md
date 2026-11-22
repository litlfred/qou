---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-037
section_title: "Page 37"
section_number: null
pages: 37-37
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Set
a0 = a1 = 0,
ak = qk
(k ≥2);
b0 = b1 = 0,
bk =
p#
k
(p#
1 )k/2
(k ≥2).
The relations (7.8) coincide with the ﬁrst system in (7.13), up to remainder terms
of negative degree. These terms can be neglected, because they aﬀect only similar
remainder terms in the inverse relations. These inverse relations are given then by
the second system in (7.13). This leads to (7.12).
□
Proof of Theorem 7.1. We rewrite (7.12) as follows. For any k ≥2,
[ k−2
2
]
X
j=0
(−1)j
k −1 −j
j
 qk−2j
k −2j = 1
k
p#
k
(p#
1 )k/2 + Rk ,
where Rk ∈Aext is a certain element such that deg1(Rk) < 0.
In the left–hand side, we may extend the summation up to [ k−1
2 ], because q1 = 0.
Comparing this with formula (7.3) for uk−1(x) and formula (7.7) for the moments
of ∆λ, we conclude that
u(n)
k−1 =
1
√
kη(n)
k
+ R(n)
k
k ≥2.
Or, equivalently,
u(n)
k
=
1
√k+1η(n)
k+1 + R(n)
k+1
k ≥1.
As n →∞, the asymptotics of the (mixed) moments of the random variables
u(n)
1
, u(n)
2
, . . . is the same as that for the random variables
1
√
k+1η(n)
k+1 , k = 1, 2, . . . .
Indeed, the remainder terms of negative degree do not aﬀect the asymptotics, see
Proposition 6.2. As for the moments of the random variables η(n)
k+1, their asymp-
totics has been evaluated in the proof of Theorem 6.1. This concludes the proof.
□
§8. The central limit theorem for
transition measures of Young diagrams
Let M denote the set of probability measures on R with compact support, and
let M0 ⊂M be the subset of measures with the ﬁrst moment equal to 0.
Proposition 8.1. There exists a bijective correspondence ω ↔µ between D and
M, which is also a bijection D0 ↔M0. It is characterized by the relation
exp
Z
R
σ′(x)dx
x −z
=
Z
R
µ(dx)
1 −x
z
,
(8.1)
where z ∈C \ I, where I ⊂R stands for a suﬃciently large interval, and, as usual,
σ(x) = 1
2(ω(x) −|x|).
Proof. See [Ke2], [Ke4].
□
We call µ the transition measure of the continual diagram ω.
In [Ke4], the
correspondence σ′ 7→µ deﬁned by (8.1) is deﬁned in a greater generality, so that its
37
