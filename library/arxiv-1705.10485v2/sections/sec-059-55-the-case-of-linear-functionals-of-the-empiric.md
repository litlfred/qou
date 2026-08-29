---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-059-55-the-case-of-linear-functionals-of-the-empiric
section_title: "The case of linear functionals of the empirical measure"
section_number: 5.5
pages: 49-50
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
As a particular case of Theorem 55, one recovers the central limit theorem for linear functionals of
empirical measures of Markov chains, that are random variables
Yn = Sn− E[Sn]√n = 1√n
n∑
t=1
(f(Xt)−π(f))
withf : X→ Rﬁxed function (independent of the timet). Thus, assuming for instancelimn→∞ Var(Yn) =
Σ2(f)> 0, we have
dKol
(
Sn− E[Sn]√
Var(Sn)
,NR(0, 1)
)
≤ 77
(
‖f‖∞
√
M
Σ(f)
)3(1 +θP
1−θP
)2 1√n (13)
50 Valentin Féray, Pierre-Loïc Méliot, and Ashkan Nikeghbali
for n large enough. We refer to [Cog72, KV86, Jon04, Häg05] and the references therein for the general
background of this Markovian CLT, and to [Bol80, Lez96, Man96] for estimates of the Kolmogorov
distance. It seems that we recover some results of [Man96] (see [SC97, §2.1.3]), but we were not able to
ﬁnd and read this paper. In this last paragraph, we discuss the problem of the varianceVar(Yn), giving
suﬃcient conditions, which are simple to check on examples and ensureΣ2(f)> 0. We also remark that,
provided thatΣ2(f)> 0, we can also prove complex mod-Gaussian convergence, which implies a zone of
normality result and moderate deviation estimates by [FMN16].
Denoteg =f−π(f), which has expectation0 under the stationary measureπ. By eventually replacing
f with g, we can assume thatf is centered. The variance ofYn tends to
Σ2(f) = E[(f(X0))2] + 2
∞∑
t=1
E[f(X0)f(Xt)]< +∞,
see [Cog72, Lemma 3.3]. If Σ2(f) > 0, then Var(Sn)
n2/3 = n1/3 Var(Yn)→ +∞ and Theorem 55 applies.
Unfortunately, one can easily construct non-trivial examples withΣ2(f) = 0. Thus, consider the Markov
chain with 3 states and transition matrix
P =


0 1 0
1/2 0 1/2
1 0 0

 ;
it admits for invariant measureπ(1) = π(2) = 2
5 and π(3) = 1
