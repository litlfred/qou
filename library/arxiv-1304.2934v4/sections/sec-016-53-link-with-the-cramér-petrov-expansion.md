---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-016-53-link-with-the-cramér-petrov-expansion
section_title: "Link with the Cramér-Petrov expansion"
section_number: 5.3
pages: 43-45
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
pansion of the ﬂuctuations up to any order T = o((αn)1−ε), and indeed, it is a partic-
ular case of the results given by Rudzkis, Saulis and Statuleviˇ cius in [RSS78, SS91], see
in particular [SS91, Lemma 2.3]. Suppose that
|κ(r)(Sn)|≤ (Cr)r αn (βn)r ; κ(r)(Sn) = K(r) αn (βn)r (1 + O((αn)−1))
the second estimate holding for anyr≤ v; we denote σ2 = K(2). In this setting, one can
push the expansion up to ordero((αn)1−1/v). Indeed, deﬁne recursively for a sequence
of cumulants (κ(r))r≥2 the coefﬁcients of the Cramér-Petrov seriesλ(r) =−br−1/r, with
j
∑
r=1
κ(r+1)
r!

 ∑
j1+···+jr=j
ji≥1
bj1bj2··· bjr

 = 1 j=1.
For instance, λ(2) =− 1
2, λ(3) = κ(3)
6 , λ(4) = κ(4)−3(κ(3))2
24 , etc. The appearance of these
coefﬁcients can be guessed by trying to push the previous technique to higher or-
der; in particular, the simple form of λ(3) is related to the fact that the only term in
z3 in the expansion (28) is κ(3)
6 . If for the cumulants κ(r)’s one has estimates of order
44 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
(αn)1−r/2(1 + O((αn)−1)), then one has the same estimates for theλ(r)’s, so there exists
coefﬁcients L(r) such that
λ(r)
(
Sn
σ βn (αn)
1
2
)
= L(r) (αn)1−r/2 (1 + O((αn)−1)).
Take then T = xn (αn)
v−1
v with xn = O(1); Lemma 2.3 of [SS91] ensures that
P
[ Sn
σβ n
≥ T
]
= e− T2
2αn
√
2π T2
αn
exp
(
v
∑
r=3
λ(r)
( T
σ(αn)1/2
)r)
(
1 + o(1)
)
= e− T2
2αn
√
2π T2
αn
exp
(
v
∑
r=3
L(r) Tr
σr (αn)r−1
)
(
1 + o(1)
)
.
Thus, the method of cumulants of Rudzkis, Saulis and Statuleviˇ cius can be thought of
as a particular case (and reﬁnement in this setting) of the notion of mod-φ convergence.
However, their works do not yield a bound
|κ(r)(Sn)|≤ (Cr)r αn (βn)r
but for simple cases, such as sums of i.i.d. random variables. In Section 9, we show
that dependency graphs are an adequate framework to provide such bounds.
6. A PRECISE VERSION OF THE ELLIS -GÄRTNER THEOREM
In the classical theory of large deviations, asymptotic results are formulated not only
for the probabilities of tails P[Xn≥ tnx], but more generally for probabilities
P[Xn∈ tnB] with B arbitrary Borelian subset of R.
In particular, under some technical assumptions on the generating series (that look
like, but are somehow weaker than mod-convergence), Ellis-Gärtner theorem provides
some asymptotic upper and lower bounds for log(P[Xn∈ tnB]), these bounds relying
on a limiting condition on (tn)−1 log ϕn(·). When the topology of B is nice enough,
these bounds coincide (see e.g. [DZ98, Theorem 2.3.6]). This generalizes Cramér’s
large deviations for sums of i.i.d. random variables.
Our Theorems 3.4 and 4.3 give estimates for the probabilities P[Xn ≥ tnx] them-
selves, instead of their logarithm). Therefore, it is natural to establish in the framework
of mod-convergence a precise version of Ellis-Gärtner theorem. In this section, we shall
give some asymptotic upper and lower bounds for the probabilities P[Xn∈ tnB] itself
instead of their logarithms. Once again, the upper and lower bounds coincide for nice
borelian sets B.
Remark 6.1. In [FMN15b], we shall prove similar estimates ofP[Xn∈ tnB] in the setting
of sequences of random vectors that converge in the multi-dimensional mod-Gaussian
sense.
MOD-φ CONVERGENCE, I 45
