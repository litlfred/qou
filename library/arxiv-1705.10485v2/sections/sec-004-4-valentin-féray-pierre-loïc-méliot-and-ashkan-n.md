---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-004-4-valentin-féray-pierre-loïc-méliot-and-ashkan-n
section_title: "Valentin Féray, Pierre-Loïc Méliot, and Ashkan Nikeghbali"
section_number: 4
pages: 4-5
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
to one of their result. Our contribution here therefore consists in giving a large variety of non-trivial
examples where such bounds on cumulants hold:
• The ﬁrst family of examples relies on a previous result by the authors [FMN16, Chapter 9] (see Theo-
rem 34 here), where bounds on cumulants for sums of variables with an underlyingdependency graph
are given. Let us comment a bit. Though introduced originally in the framework of the probabilistic
method [AS08, Chapter 5], dependency graphs have been used to prove central limit theorems on var-
ious objects: random graphs [Jan88], random permutations [Bón10], probabilistic geometry [PY05],
random character values of the symmetric group [FMN16, Chapter 11]. In the context of Stein’s
method, we can also obtain bounds for the Kolmogorov distance in these central limit theorems
[BR89, Rin94].
The results of this paper give another approach to obtain bounds for this Kolmogorov distance for
sums of bounded variables (see Section 4.2). The bounds obtained are, up to a constant, the same as
in [Rin94, Theorem 2.2]. Note that our approach is fundamentally diﬀerent, since it relies on classical
Fourier analysis, while Stein’s method is based on a functional equation for the Gaussian distribution.
We make these bounds explicit in the case of subgraph counts in Erdös–Rényi random graphs and
discuss an extension to sum of unbounded variables.
• The next example is the ﬁnite volume magnetization in the Ising model onZd. The Ising model is one
of the most classical models of statistical mechanics, we refer to [FV16] and references therein for an
introduction to this vast topic. The magnetizationM∆ (that is the sum of the spins in∆) is known
to have asymptotically normal ﬂuctuations [New80]. Based on a result of Duneau, Iagolnitzer and
Souillard [DIS74], we prove that, if the magnetic ﬁeld is non-zero or if the temperature is suﬃciently
large, M∆ has uniform bounds on cumulants. This implies a bound on the Kolmogorov distance
(Proposition 49):
dKol
(
M∆− E[M∆]√
Var(M∆)
,NR(0, 1)
)
≤ K√
|∆|
.
It seems that this result improves on what is known so far. In [Bul96], Bulinskii gave a general
bound on the Kolmogorov distance for sums ofassociated random variables, which applied toM∆,
yields a bound with an additional(log|∆|)d factor comparing to ours. In a slightly diﬀerent direction,
Goldstein and Wiroonsri [GW16] have recently given a bound of orderO(|∆|1/(2d+2)) for the L1-
distance (theL1-distance is another distance on distribution functions, which is a priori incomparable
with the Kolmogorov distance; note also that their bound is only proved in the special case where
∆ ={−m,−m + 1,...,m }d).
• The last example considers statistics of the formSn = ∑n
t=0ft(Xt), where (Xt)t≥0 is an ergodic
discrete time Markov chain on a ﬁnite space state. Again we can prove uniform bounds on cumulants
and deduce from it bounds for the Kolmogorov distance (Theorem 55). The speed of convergence
in the central limit theorem for Markov chains has already been studied by Bolthausen [Bol80] (see
also later contributions of Lezaud [Lez96] and Mann [Man96]). These authors study more generally
Markov chains on inﬁnite space state, but focus on the case of a statisticsft independent of the time.
Except for these diﬀerences, the bounds obtained are of the same order; however our approach and
proofs are again quite diﬀerent.
It is interesting to note that the proofs of the bounds on cumulants in the last two examples are highly
non trivial and share some common structure. Each of these statistics decomposes naturally as a sum.
In each case, we give an upper bound for joint cumulants of the summands, which writes as a weighted
enumeration of spanning trees. Summing terms to get a bound on the cumulant of the sum is then easy.
To formalize this idea, we introduce in Section 5 the notion of uniform weighted dependency graphs.
Both proofs for the bounds on cumulants (for magnetization of the Ising model and functional of Markov
chains) are presented in this framework. We hope that this will ﬁnd further applications in the future.
Mod-φ convergence, II: Estimates on the speed of convergence 5
