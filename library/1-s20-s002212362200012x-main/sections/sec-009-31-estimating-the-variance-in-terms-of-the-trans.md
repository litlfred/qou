---
doc_id: 1-s20-s002212362200012x-main
doc_title: "Journal of Functional Analysis Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-009-31-estimating-the-variance-in-terms-of-the-trans
section_title: "Estimating the variance in terms of the transportation distance between tilts"
section_number: 3.1
pages: 12-15
source_pdf: 1-s2.0-S002212362200012X-main.pdf
source_sha256: 6fc7d28c8d40bf42
toc_source: outline
doc_brief: "Journal of Functional Analysis Log concavity and concentration of Lipschitz functions on the Boolean hypercube — V Article history: Received 17 December 2020 Accepted 13 January 2022 Available online"
---
Fix a test function ϕ : Cn →R. Deﬁne Mt =

ϕdνt. Observe that by part 2 of 
Proposition 10, Mt is a martingale. We ﬁrst claim that
Varν[ϕ] = E[M]t + EVarνt[ϕ],
(16)
where [M]t denotes the quadratic variation of Mt.
Indeed, by part 3 of Proposition 10, we have that M∞:= limt→∞Mt exists almost 
surely and has the law ϕ⋆ν. Consequently, Varν[ϕ|Ft] = Var[M∞|Ft] almost surely, for 
all t. By Itô’s isometry, we have
Varν[ϕ] = E[M]t + EVar[M∞|Ft] = E[M]t + EVarνt[ϕ].
We will carry on by bounding each of the terms on the right hand side separately, for a 
suitable chosen value of t. We begin with the ﬁrst term, for which we calculate
dMt = d

Cn
ϕ(x)νt(x) =

Cn
ϕ(x)dFt(x)ν(x) =

Cn
ϕ(x)⟨x −at, dBt⟩νt(x).
Therefore, we can estimate
d[M]t =


Cn
ϕ(x)(x −at)dνt

2
dt
≤
sup
|θ|=1, ˜ϕ∈Lip(Cn)


Cn
˜ϕ(x)⟨x −at, θ⟩dνt

2
dt
=
sup
|θ|=1, ˜ϕ∈Lip(Cn)


Cn
⎛
⎝˜ϕ(x) −

Cn
˜ϕdνt
⎞
⎠⟨x −at, θ⟩dνt

2
dt
=
sup
|θ|=1, ˜ϕ∈Lip(Cn)


Cn
⎛
⎝˜ϕ(x) −

Cn
˜ϕdνt
⎞
⎠limsupε→0+
1
ε (exp (⟨x −at, εθ⟩) −1) dνt

2
dt
=
sup
|θ|=1, ˜ϕ∈Lip(Cn)

limsupε→0+
1
ε

Cn
⎛
⎝˜ϕ(x) −

Cn
˜ϕdνt
⎞
⎠exp (⟨x, εθ⟩) dνt

2
dt
=
sup
|θ|=1, ˜ϕ∈Lip(Cn)

limsupε→0+
1
εZνt(εθ)

Cn
⎛
⎝˜ϕ(x) −

Cn
˜ϕdνt
⎞
⎠dτεθνt

2
dt
R. Eldan, O. Shamir / Journal of Functional Analysis 282 (2022) 109392
13
=
sup
|θ|=1, ˜ϕ∈Lip(Cn)

Zνt(0)limsupε→0+
1
ε
⎛
⎝

Cn
˜ϕdτεθνt −

Cn
˜ϕdνt
⎞
⎠

2
dt
= sup
|θ|=1
limsupε→0+
1
εW1(ν, τεθν)

2
dt,
(17)
where for two measures ν, ˜ν, we deﬁne
W1(ν, ˜ν) =
sup
˜ϕ∈Lip(Cn)
Eν[ ˜ϕ] −E˜ν[ ˜ϕ]

known as the Wasserstein transportation distance between ν and ˜ν.
Towards bounding the second term of the right hand side of (16), deﬁne At = Cov(νt).
Fact 12. One has,
V arνt[ϕ] ≤nTr(At).
Proof. It is easily checked that ϕ is 1-Hamming-Lipschitz then its multi-linear extension 
satisﬁes |∂iϕ(x)| ≤1 for all x ∈[−1, 1]n and i ∈[n]. Therefore, its multi-linear extension 
is √n-Lipschitz with respect to the Euclidean distance, hence
|ϕ(x) −ϕ(y)| ≤√n|x −y|,
∀x, y ∈[−1, 1]n.
So, if X ∼νt then,
V arνt[ϕ] ≤E[

ϕ(X) −ϕ(E[X]))2
≤nE

|X −E[X]|2
= nTr(At).

Lemma 13. For all t, r ≥0, we have almost surely,
E[Tr(At+r)|Fr] ≤ne−t/8.
(18)
Proof. Fix i ∈[n], and deﬁne
St := (At)i,i,
Qt = ⟨at, ei⟩.
By part 3 of Proposition 10, we have that a∞|Ft has the law νt, meaning that Q∞:=
limt→∞Qt exists almost surely and that, since at is a martingale,
Qt = E[Q∞|Ft]
and
St = Var[Q∞|Ft].
So,
St = Var[Q∞|Ft] = E[Q2
∞|Ft] −Q2
t = 1 −Q2
t.
14
R. Eldan, O. Shamir / Journal of Functional Analysis 282 (2022) 109392
Equation (12) can be written
d[Q]t ≥S2
t dt.
(19)
By Itô’s formula,
dSt = −2QtdQt −d[Q]t,
and
d

St = −2QtdQt −d[Q]t
2√St
−1
8
d[Q]t
S3/2
t
(19)
≤−QtdQt
√St
−
√St
8 dt.
Since the ﬁrst term on the right hand side is a martingale, we have almost surely, for all 
s, t ≥0,
d
dtE[

St+r|Fr] ≤−1
8E[

St+r|Fr].
By integrating (using Growall’s inequality), we ﬁnally get
E[St+r|Fr] ≤E[

St+r|Fr] ≤

Sre−t/8 ≤e−t/8
(where we used the fact that St ≤1 almost surely for all t). The proof is completed by 
summing over coordinates.

Finally, combining equations (16), (17), (18) and Fact 12, we have for all T > 0,
Varν[ϕ] ≤E
T

0
sup
|θ|=1
limsupε→0+
1
εW1(νt, τεθνt)

2
dt + n2e−T/8
(14)
= E
T

0
sup
|θ|=1
limsupε→0+
1
εW1(τwtν, τwt+εθν)

2
dt + n2e−T/8.
(20)
Remark 14. Up to this point, the semi-log-concavity of the measure ν has not been used, 
meaning that the bound (20) holds true for general measures. Semi-log-concavity will 
play a role when bounding the integrand on the right hand side of the above equation.
In light of the above bound, the proof boils down to the following estimate on the 
transportation distance between two close tilts.
Proposition 15. Let ν be a β-semi-log-concave measure on Cn. Let v ∈Rn and let θ ∈
Sn−1. Then, for all 0 < ε < 0.1, we have
W1(τvν, τv+εθν) ≤4εβn1−1/(32β).
R. Eldan, O. Shamir / Journal of Functional Analysis 282 (2022) 109392
15
Proof of Theorem 2. Use equation (20) with T = 16 log n. Invoke the above proposition 
and attain
Var[ϕ] ≤16Tβ2n2−1/(16β) + n2e−2 log n ≤Cβ2n2−1/(17β),
for a universal constant C > 0.

