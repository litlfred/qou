---
doc_id: arxiv-1804.10084v1
doc_title: "Concentration of Lipschitz Functions of Negatively Dependent Variables"
section_id: sec-004-31-adaptive-martingale-analysis
section_title: "Adaptive martingale analysis"
section_number: 3.1
pages: 4-8
source_pdf: 1804.10084v1.pdf
source_sha256: 716da9708f06d930
doc_brief: "Concentration of Lipschitz Functions of Negatively Dependent Variables — We explore the question whether Lipschitz functions of random var iables under various forms of negative correlation satisfy"
---
As we show in Appendix A, it is not possible to replicate the martingale an alysis of McDiarmid’s
inequality under negative regression, if we work with a ﬁxed ordering of variables X1, . . . , X n. The
problem is that a particular variable X1 might have a large inﬂuence on the distribution of the
remaining variables, and hence aﬀect signiﬁcantly the conditional ex pectation of f once the value
of X1 is revealed.
Our way around this issue is that we can choose variables adaptively, in order to construct a
martingale with bounded diﬀerences. Our goal is to choose a variable that does not aﬀect the
remaining variables too heavily. Due to negative regression, we know that conditioning on Xi = 1
can only aﬀect the remaining variables negatively. Hence the only thin g we have to worry about is
that this negative eﬀect is too large. However, the following lemma sh ows that there always exists
a variable whose negative inﬂuence on the remaining variables is not to o large.
Lemma 1. Let X1, . . . , X n be {0, 1} random variables. Fix K ⊂ [n] and aK ∈ { 0, 1}K such that
P r[XK = aK] > 0. Then there exists i ∈ [n] \ K such that either Xi conditioned on XK = aK is
deterministic, or
∑
ℓ∈[n]\(K∪{i})
(E[Xℓ | XK = aK, X i = 0] − E[Xℓ | XK = aK, X i = 1]) ≤ 1.
Proof. Let us denote L = [n] \ K. We consider the following quantity:
Var
[ ∑
i∈L
Xi | XK = aK
]
=
∑
i∈L

Var[Xi | XK = aK] +
∑
j∈L\{i}
Cov[Xi, X j | XK = aK]

 .
Variance is always nonnegative, so at least one term of the summatio n over i ∈ L must be non-
negative:
Var[Xi | XK = aK] +
∑
j∈L\{i}
Cov[Xi, X j | XK = aK] ≥ 0. (1)
4
Let us denote πi = Pr[Xi = 1 | XK = aK]. We can write
Var[Xi | XK = aK] = E[X 2
i | XK = aK] − (E[Xi | XK = ak])2 = πi(1 − πi)
and
Cov[Xi, X j | XK = aK] = E[XiXj | XK = aK] − E[Xi | XK = aK] E[Xj | XK = aK]
= πi(E[Xj | XK = aK, X i = 1] − E[Xj | XK = aK]).
Since E[Xj | XK = aK] = πiE[Xj | XK = aK, X i = 1] + (1 − πi)E[Xj | XK = aK, X i = 0], we can
rewrite this as
Cov[Xi, X j | XK = aK] = πi(1 − πi)(E[Xj | XK = aK, X i = 1] − E[Xj | XK = aK, X i = 0]).
If πi = 0 or πi = 1, then Xi conditioned on XK = aK is deterministic, and we are done. Otherwise,
substitute the expressions for Var[Xi | XK = aK] and Cov[Xi, X j | XK = aK] in (1), divide by
πi(1 − πi), and conclude that
∑
ℓ∈L\{i}
(E[Xℓ | XK = aK, X i = 0] − E[Xℓ | XK = aK, X i = 1]) ≤ 1.
Next, we show that conditioning on Xi indeed cannot aﬀect the conditional expectation of f
too much. To prove this, we need one more tool, which is Strassen’s m onotone coupling theorem
(easily proved from the max-ﬂow min-cut theorem).
Theorem 2 (Strassen’s Theorem). Consider two probability measures µ (0) and µ (1) on {0, 1}L.
Suppose that for every down-closed M ⊂ {0, 1}L, µ (1)(M ) ≥ µ (0)(M ). Then there exists a coupling
ν : {0, 1}L × {0, 1}L → [0, 1] such that:
µ (1)(x) =
∑
y
ν(x, y ),
µ (0)(y) =
∑
x
ν(x, y ),
and ν(x, y ) = 0 unless x ≤ y coordinate-wise.
I.e., if µ (1) dominates µ (0) on every down-closed event, then it is possible to transform µ (0) into
µ (1) in such a way that we only transfer probability mass downwards in {0, 1}L. From the condition
of negative regression and Strassen’s theorem, we get immediately the following.
Corollary 1. For random variables X1, . . . , X n satisfying negative regression, K ⊂ [n], aK ∈
{0, 1}K, and i ∈ [n] \ K such that Pr[XK = ak, X i = 0] > 0, Pr[XK = ak, X i = 1] > 0, there exists
a coupling ν : {0, 1}L × {0, 1}L → [0, 1] for L = [n] \ (K ∪ {i}) such that
µ (1)(aL) = Pr[ XL = aL | XK = aK, X i = 1] =
∑
y
ν(aL, y ),
µ (0)(bL) = Pr[ XL = bL | XK = aK, X i = 0] =
∑
x
ν(x, b L),
and ν(x, y ) = 0 unless x ≤ y.
Now we are ready to construct a martingale with bounded diﬀerence s. We formalize this as
follows.
5
Lemma 2. Given {0, 1} random variables X1, . . . , X n satisfying negative regression, and a 1-
Lipschitz function f : {0, 1}n → R, there exists an adaptive ordering (random permutation)
π (1), π (2), . . . , π (n) such that:
• π (1) is deterministic.
• For each 1 ≤ k < n , π (k + 1) is determined by π ([k]) = {π (1), . . . , π (k)} = K and XK = aK.
• If we denote Yk = E[f (X) | π ([k]), X π([k])], then Y0, Y 1, . . . , Y n is a martingale.
• Conditioned on π ([k]) = K, X K = aK, there are α < β, β − α ≤ 2, such that Yk+1 − Yk ∈ [α, β ]
with prob. 1.
• For monotone f , Yk+1 − Yk ∈ [α, β ] where β − α ≤ 1.
Proof. Let us ﬁx π ([k]) = K and XK = aK. Given this conditioning, there exists i ∈ [n] \ K as
provided by Lemma 1. Let us deﬁne π (k + 1) to be the minimum index i satisfying the conclusion
of Lemma 1.
Now let us consider Yk = E[f (X) | π ([k]) = K, X K = aK]. Under this conditioning, π (k + 1)
is deterministic and Xπ(k+1) could take two possible values (0 or 1) which determines the value of
Yk+1. By construction, Yk = EXπ (k+1) [Yk+1 | π ([k]) = K, X K = aK]. By averaging over all possible
choices of K and aK consistent with the same value of Yk, we also get Yk = E[Yk+1 | Yk]; i.e., the
sequence Y0, Y 1, . . . , Y n forms a martingale.
Our goal now is to analyze how much Yk+1 can deviate from Yk. In the following we ﬁx
π ([k]) = K and XK = aK. We have Yk = E[f (X) | π ([k]) = K, X K = aK]. Recall that this
conditioning also determines the choice of π (k + 1) (but of course not the value of Xπ(k+1)). If
Xπ(k+1) attains only one possible value under this conditioning, then Yk+1 = Yk and we are done
— hence, let us assume that both values of Xπ(k+1) occur with positive probability. For c = 0 , 1,
let us denote
Y (c)
k+1 = E[f (X) | π (1), . . . , π (k), π (k + 1), X π(1), . . . , X π(k); Xπ(k+1) = c].
We claim that |Y (1)
k+1 − Y (0)
k+1| ≤ 2, and in the case of monotone f , |Y (1)
k+1 − Y (0)
k+1| ≤ 1; showing this
will complete the proof.
Let L = [ n] \ π ([k + 1]) = [ n] \ (K ∪ {π (k + 1)}). Denote by µ (c) the probability distribution
of XL ∈ { 0, 1}L conditioned on π ([k]) = K, XK = aK, and Xπ(k+1) = c ∈ { 0, 1}. By Corollary 1,
there is a monotone coupling ν(x, y ) between µ (1) and µ (0). We can write
Y (1)
k+1 = E[f (X) | π ([k]) = K, X K = aK, X π(k+1) = 1]
=
∑
aL∈{0,1}L
µ (1)(aL) f (XK = aK, X π(k+1) = 1, X L = aL)
=
∑
aL,bL∈{0,1}L
ν(aL, b L) f (XK = aK, X π(k+1) = 1, X L = aL).
Similarly,
Y (0)
k+1 = E[f (X) | π ([k]) = K, X K = aK, X π(k+1) = 0]
=
∑
bL∈{0,1}L
µ (0)(bL) f (XK = aK, X π(k+1) = 0, X L = bL)
=
∑
aL,bL∈{0,1}L
ν(aL, b L) f (XK = aK, X π(k+1) = 0, X L = bL).
Now we can compare the values of f in the two expressions. First we modify the coordinate Xπ(k+1),
and then the remaining coordinates XL. Since f is 1-Lipschitz, we have
⏐⏐f (XK = aK, X π(k+1) = 1, X L = aL) − f (XK = aK, X π(k+1) = 0, X L = aL)
⏐⏐ ≤ 1.
6
Next, since aL ≤ bL in all the terms with ν(aL, b L) > 0, we have
⏐⏐f (XK = ak, X π(k+1) = 0, X K = aL) − f (XK = ak, X π(k+1) = 0, X K = bL)
⏐⏐ ≤ ‖bL‖1 − ‖aL‖1.
By the triangle inequality,
⏐⏐f (XK = ak, X π(k+1) = 1, X K = aL) − f (XK = ak, X π(k+1) = 0, X K = bL)
⏐⏐ ≤ 1 + ‖bL‖1 − ‖aL‖1.
Hence
⏐⏐⏐Y (1)
k+1 − Y (0)
k+1
⏐⏐⏐ ≤
∑
aL,bL∈{0,1}L
ν(aL, b L)(1 + ‖bL‖1 − ‖aL‖1)
= 1 +
∑
bL∈{0,1}L
µ (0)(bL) ‖bL‖1 −
∑
aL∈{0,1}L
µ (1)(aL) ‖aL‖1
= 1 +
∑
ℓ∈L
E[Xℓ | XK = aK, X π(k+1) = 0] −
∑
ℓ∈L
E[Xℓ | XK = aK, X π(k+1) = 1]
by the properties of µ (0), µ (1) and ν. Finally, we recall that π (k + 1) was chosen so as to satisfy the
conclusion of Lemma 1:
∑
ℓ∈L
E[Xℓ | XK = aK, X π(k+1) = 0] −
∑
ℓ∈L
E[Xℓ | XK = aK, X π(k+1) = 1] ≤ 1.
This concludes the proof that |Y (1)
k+1 − Y (0)
k+1| ≤ 2.
In the case of monotone f , we observe that we can improve some of the inequalities: we get
0 ≤ f (XK = aK, X π(k+1) = 1, X L = aL) − f (XK = aK, X π(k+1) = 0, X L = aL) ≤ 1
and
0 ≥ f (XK = ak, X π(k+1) = 0, X K = aL) − f (XK = ak, X π(k+1) = 0, X K = bL)| ≥ ‖ aL‖1 − ‖bL‖1
whenever aL ≤ bL. This implies that
1 ≥ f (XK = ak, X π(k+1) = 1XK = aL) − f (XK = ak, X π(k+1) = 0, X K = bL) ≥ ‖aL‖1 − ‖bL‖1
and by the same computations as above, we conclude that 1 ≥ Y (1)
k+1 − Y (0)
k+1 ≥ −1.
Theorem 1 now follows by standard exponential moment analysis; se e for example [9]. For
completeness, we summarize the rest of the analysis as follows.
Proof of Theorem 1. For a parameter λ ∈ R, we estimate the exponential moment E[eλf (X1,...,Xn)] =
E[eλYn ]. Inductively, we prove that E[eλ(Yk−Y0)] ≤ ekλ2/2 (for monotone f , the bound improves to
ekλ2/8). The inductive step is that
E[eλ(Yk+1−Yk) | π ([k]) = K, X K = aK] ≤ eλ2/2
which is true because under this conditioning, Yk+1 − Yk is a random variable of expectation 0,
conﬁned to an interval of length 2 (see Lemma 2). It is known that t he exponential moment of such
a variable is upper-bounded by eλ2/2. By averaging over all choices of K and aK that yield the
same value of Yk, we also obtain E[eλ(Yk+1−Yk) | Yk] ≤ eλ2/2. In the case of f monotone, Yk+1 − Yk
is conﬁned to an interval of length 1 and the exponential moment is u pper-bounded by eλ2/8.
From here, by induction, we obtain
E[eλ(Yk+1−Y0)] = EYk [EYk+1[eλ(Yk+1−Yk) | Yk] eλ(Yk−Y0)] ≤ eλ2/2 EYk [eλ(Yk−Y0)] ≤ e(k+1)λ2/2.
7
Therefore, E[eλ(Yn−Y0)] ≤ enλ2/2. (For f monotone, the bound improves to enλ2/8.)
Recall that Y0 = E[f (X1, . . . , X n)] = µ . By Markov’s inequality applied to the exponential
moment, we get
Pr[f (X1, . . . , X n) > µ + t] = Pr
[
eλ(Yn−Y0) ≥ eλt
]
≤ E[eλ(Yn−Y0)]
eλt = enλ2/2−λt.
The choice of λ = t/n gives the upper-tail bound in Theorem 1; the other bounds follow sim ilarly.
