---
doc_id: arxiv-2007.13108v1
doc_title: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-007-31-estimating-the-variance-in-terms-of-the-trans
section_title: "Estimating the variance in terms of the transportation distance between tilts"
section_number: 3.1
pages: 9-11
source_pdf: 2007.13108v1.pdf
source_sha256: b298478f5f5b948d
doc_brief: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube — It is well-known that measures whose density is the form e−V where V is a uniformly convex potential on Rn attain"
---
tween tilts
Deﬁne Mt =
∫
ϕdν t. Observe that by part 2 of Proposition 9, Mt is a martingale. We ﬁrst claim
that
Varν[ϕ ] = E[M]t + EVarνt[ϕ ], (16)
where [M]t denotes the quadratic variation of Mt.
Indeed, by part 3 of Proposition 9, we have that M∞ := lim t→∞ Mt exists almost surely
and has the law ϕ ⋆ν. Consequently, Varν[ϕ |Ft] = Var[M∞|Ft] almost surely, for all t. By Itˆ o’s
isometry, we have
Varν[ϕ ] = E[M]t + EVar[M∞|Ft] = E[M]t + EVarνt[ϕ ].
We will carry on by bounding each of the terms on the right hand side separately, for a suitable
chosen value of t. We begin with the ﬁrst term, for which we calculate
dMt = d
∫
Cn
ϕ (x)νt(x) =
∫
Cn
ϕ (x)dFt(x)ν(x) =
∫
Cn
ϕ (x)⟨x − at, dB t⟩νt(x).
Therefore, we can estimate
d[M]t =
⏐⏐⏐⏐
∫
Cn
ϕ (x)(x − at)dνt
⏐⏐⏐⏐
2
dt
≤ sup
|θ|=1, ˜ϕ∈Lip(Cn)
⏐⏐⏐⏐
∫
Cn
˜ϕ (x)⟨x − at, θ ⟩dνt
⏐⏐⏐⏐
2
dt
= sup
|θ|=1, ˜ϕ∈Lip(Cn)
⏐⏐⏐⏐
∫
Cn
(
˜ϕ (x) −
∫
Cn
˜ϕdν t
)
⟨x − at, θ ⟩dνt
⏐⏐⏐⏐
2
dt
= sup
|θ|=1, ˜ϕ∈Lip(Cn)
⏐⏐⏐⏐
∫
Cn
(
˜ϕ (x) −
∫
Cn
˜ϕdν t
)
limsupε→0+
1
ε (exp (⟨x − at, εθ ⟩) − 1) dνt
⏐⏐⏐⏐
2
dt
= sup
|θ|=1, ˜ϕ∈Lip(Cn)
⏐⏐⏐⏐limsupε→0+
1
ε
∫
Cn
(
˜ϕ (x) −
∫
Cn
˜ϕdν t
)
exp (⟨x, εθ ⟩) dνt
⏐⏐⏐⏐
2
dt
= sup
|θ|=1, ˜ϕ∈Lip(Cn)
⏐⏐⏐⏐limsupε→0+
1
εZνt(εθ)
∫
Cn
(
˜ϕ (x) −
∫
Cn
˜ϕdν t
)
dτεθνt
⏐⏐⏐⏐
2
dt
= sup
|θ|=1, ˜ϕ∈Lip(Cn)
⏐⏐⏐⏐Zνt(0)limsupε→0+
1
ε
( ∫
Cn
˜ϕdτ εθνt −
∫
Cn
˜ϕdν t
) ⏐⏐⏐⏐
2
dt
= sup
|θ|=1
⏐⏐⏐⏐limsupε→0+
1
εW1(ν, τ εθν)
⏐⏐⏐⏐
2
dt, (17)
where for two measures ν, ˜ν, we deﬁne
W1(ν, ˜ν) = sup
˜ϕ∈Lip(Cn)
⏐⏐⏐Eν[ ˜ϕ ] − E˜ν[ ˜ϕ ]
⏐⏐⏐
known as the Wasserstein transportation distance between ν and ˜ν.
Towards bounding the second term of the right hand side of (16 ), deﬁne At = Cov(νt).
9
Fact 11. One has,
V arνt[ϕ ] ≤ nTr(At).
Proof. It is easily checked that ϕ is 1-Hamming-Lipschitz then its multi-linear extension sat-
isﬁes |∂iϕ (x)| ≤ 1 for all x ∈ [−1, 1]n and i ∈ [n]. Therefore, its multi-linear extension is√n-Lipschitz with respect to the Euclidean distance, hence
|ϕ (x) − ϕ (y)| ≤ √n|x − y|, ∀x, y ∈ [−1, 1]n.
So, if X ∼ νt then,
V arνt[ϕ ] ≤ E[
(
ϕ (X) − ϕ (E[X]))2]
≤ nE
[
|X − E[X]|2]
= nTr(At).
Lemma 12. F or allt, r ≥ 0, we have almost surely,
E[Tr(At+r)|Fr] ≤ ne−t/8. (18)
Proof. Fix i ∈ [n], and deﬁne
St := (At)i,i, Q t = ⟨at, e i⟩.
By part 3 of Proposition 9, we have that a∞|Ft has the law νt, meaning that Q∞ := lim t→∞ Qt
exists almost surely, and that
St = Var[Q∞|Ft].
Recall that at is a martingale and thus so is Qt and
St = Var[Q∞|Ft] = E[Q2
∞|Ft] − Q2
t = 1 − Q2
t .
Equation (12) can be written
d[Q]t ≥ S2
t dt. (19)
By Itˆ o’s formula,
dSt = −2QtdQt − d[Q]t,
and
d
√
St = −2QtdQt − d[Q]t
2√St
− 1
8
d[Q]t
S3/2
t
(19)
≤ −QtdQt√St
−
√St
8 dt.
Since the ﬁrst term on the right hand side is a martingale, we h ave almost surely, for all s, t ≥ 0,
d
dtE[
√
St+r|Fr] ≤ − 1
8 E[
√
St+r|Fr].
By integrating (using Growall’s inequality), we ﬁnally get
E[St+r|Fr] ≤ E[
√
St+r|Fr] ≤
√
Sre−t/8 ≤ e−t/8
(where we used the fact that St ≤ 1 almost surely for all t). The proof is completed by summing
over coordinates.
10
Finally, combining equations (16), (17), (18) and Fact 11, w e have for all T > 0,
Var[ϕ ] ≤ E
∫ T
0
sup
|θ|=1
⏐⏐⏐⏐limsupε→0+
1
εW1(νt, τ εθνt)
⏐⏐⏐⏐
2
dt + n2e−T /8
(14)
= E
∫ T
0
sup
|θ|=1
⏐⏐⏐⏐limsupε→0+
1
εW1(τwtν, τ wt+εθν)
⏐⏐⏐⏐
2
dt + n2e−T /8. (20)
In light of the above bound, the proof boils down to the follow ing estimate on the trans-
portation distance between two close tilts.
Proposition 13. Let ν be a β -semi-log-concave measure on Cn. Let v ∈ Rn and let θ ∈ Sn−1.
Then, for all 0 < ε < 0. 1, we have
W1(τvν, τ v+εθν) ≤ 4εβn 1−1/(32β).
Proof of Theorem 2. Use equation (20) with T = 16 log n. Invoke the above proposition and
attain
Var[ϕ ] ≤ 4T βn2−1/(16β) + n2e−2 log n ≤ Cβn 2−1/(17β),
for a universal constant C > 0.
