---
doc_id: zhao-standard-2010
doc_title: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity"
section_id: sec-001-11-multiple-polylog-values-at-roots-of-unity
section_title: "Multiple polylog values at roots of unity"
section_number: 1.1
pages: 3-4
source_pdf: Zhao_standard_2010.pdf
source_sha256: 94a70847c2937ba7
toc_source: inferred
doc_brief: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity — Let N be a positive integer."
---
Multiple polylog values at roots of unity
In this paper, the primary objects of study are the multiple polylog values at
roots of unity (MPVs). These special values, MZVs and the alternating Euler
sums in particular, have attracted a lot attention in recent years after they were
found to be connected to many branches of mathematics and physics (see, for
e.g., [7, 8, 10, 11, 15, 19, 28]). Results up to around year 2000 can be found in
the comprehensive survey paper [6].
Starting from early 1990s Hoﬀman [21, 22] has constructed some quasi-shuﬄe
(called stuﬄe in [6]) algebras reﬂecting the essential combinatorial properties of
MZVs. Later he [23] extends this to incorporate MPVs although his deﬁnition
of ∗-product is diﬀerent from ours. This approach was then improved in [24] and
[26] to study MZVs and MPVs in general, respectively, where the regularized
double shuﬄe relations play prominent roles. One derives these relations by
comparing (1) with another expression of the multiple polylogs given by the
following iterated integral:
Lis1,...,sℓ(x1, . . . , xℓ) =
(−1)ℓ
Z 1
0
dt
t
◦(s1−1)
◦
dt
t −a1
◦· · · ◦
dt
t
◦(sℓ−1)
◦
dt
t −aℓ
,
(2)
where ai = 1/(x1 . . . xi) for 1 ≤i ≤ℓ. Here, one deﬁnes the iterated integrals
recursively by
R b
a f(t) ◦w(t) =
R b
a (
R x
a w(t))f(x) for any 1-form w(t) and con-
catenation of 1-forms f(t). One may think the path lies in C; however, it is
more revealing to use iterated integrals in Cℓto ﬁnd the analytic continuation
of this function (see [29]).
The main feature of this paper is a quantitative comparison between the results
obtained by Racinet [26] who considers MPVs from the motivic viewpoint of
Drinfeld associators, and those by Deligne and Goncharov [17] who study the
motivic fundamental groups of P1−({0, ∞}∪µN) by using the theory of mixed
Tate motives over S-integers of number ﬁelds, where µN is the group of Nth
roots of unity.
Fix an Nth root of unity µ = µN := exp(2π√−1/N). An MPV of level N is a
number of the form
LN(s1, . . . , sℓ|i1, . . . , iℓ) := Lis1,...,sℓ(µi1, . . . , µiℓ).
(3)
We will always identify (i1, . . . , iℓ) with (i1, . . . , iℓ) (mod N). It is easy to see
from (1) that an MPV converges if and only if (s1, µi1)̸ = (1, 1). Clearly, all
Documenta Mathematica 15 (2010) 1–34
4
Jianqiang Zhao
MPVs of level N are automatically of level Nk for every positive integer k.
For example when i1 = · · · = iℓ= 0 or N = 1 one gets the MZV ζ(s1, . . . , sℓ).
When N = 2 one recovers the alternating Euler sums studied in [8, 31]. To
save space, if a string S repeats n times then {S}n will be used. For example,
LN({2}2|{0}2) = ζ(2, 2) = π4/120.
Standard conjectures in arithmetic geometry imply that Q-linear relations
among MVPs can only exist between those of the same weight.
Let
MPV(w, N) be the Q-span of all the MPVs of weight w and level N.
Let d(w, N) denoted its dimension.
In general, it is very diﬃcult to de-
termine d(w, N) because any nontrivial lower bound would provide some
nontrivial irrational/transcendental result which is related to a variant of
Grothendieck’s period conjecture (see [16] or [17, 5.27(c)]). For example, one
can show easily that MPV(2, 4) = ⟨log2 2, π2, π log 2√−1, (K −1)√−1⟩, where
K = P
n≥0(−1)n/(2n + 1)2 is the Catalan’s constant.
From a variant of
Grothendieck’s period conjecture we know d(2, 4) = 4 (see [16]) but we don’t
have an unconditional proof yet. Namely, we cannot prove that the four num-
ber log2 2, π2, π log 2√−1, (K −1)√−1 are linearly independent over Q. Thus,
nontrivial lower bound of d(w, N) is hard to come by.
On the other hand, one may obtain upper bound of d(w, N) by ﬁnding as
many linear relations in MPV(w, N) as possible. As in the cases of MZVs and
the alternating Euler sums the double shuﬄe relations play important roles in
revealing the relations among MPVs. In such a relation if all the MPVs involved
are convergent it is called a ﬁnite double shuﬄe relation (FDS). In general one
needs to use regularization to obtain regularized double shuﬄe relations (RDS)
involving divergent MPVs. We shall recall this theory in §2 building on the
results of [24, 26].
From the point of view of Lyndon words and quasi-symmetric functions Bigotte
et al. [3, 4] have studied MPVs (they call them colored MZVs) primarily by
using double shuﬄe relations and monodromy argument (cf. [4, Thm. 5.1]).
However, when the level N ≥2, these double shuﬄe relations often are not
complete, as we shall see in this paper (for level two, see also [5]).
