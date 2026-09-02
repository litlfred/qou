---
doc_id: arxiv-2007.13108v1
doc_title: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-005-22-stochastic-localization
section_title: "Stochastic localization"
section_number: 2.2
pages: 7-9
source_pdf: 2007.13108v1.pdf
source_sha256: b298478f5f5b948d
---
We construct a stochastic process driven by a Brownian motio n, which we refer to as stochastic
localization. A somewhat similar process was originally used in [6] to est ablish concentration
properties for log-concave measures on Rn. Here we use a discrete version, similar to the con-
struction which appears in [7, 8]. In this section we occasio nally allow ourselves to omit some
of the details of the proofs, and the reader is referred to [7] for more rigorous derivations.
Let Bt be a standard Brownian motion on Rn adapted to a ﬁltration Ft. Consider the system
of equations,
F0(x) = 0 , dF t(x) = Ft(x)⟨x − at, dB t⟩, ∀x ∈ C n, (10)
where at :=
∫
xdνt(x) :=
∫
xFt(x)dν(x).
We think of this process (νt)t as an evolution of measures on Cn, which starts with the mea-
sure ν0 = ν, and as seen below, ends up with a Dirac measure whose support is ν-distributed.
Let us ﬁrst summarize some useful properties of this process .
Proposition 9. The process deﬁned above satisﬁes the following properties .
1. Almost surely, for all t, νt is a probability measure.
2. F or all A ⊂ C n, the process νt(A) is a martingale.
3. The process at almost surely converges to a point in Cn, and a∞ := lim t→∞ at is dis-
tributed according to the law ν. Moreover , the measureνt almost-surely weakly converges
to a Dirac measure at a∞.
Proof. We have
dνt(Cn) = d
∫
Cn
Ft(x)ν(x) =
∫
Cn
(x − at)dνt(x)dBt = 0,
which proves the ﬁrst part. The second part is evident from th e deﬁnition. For the third part, a
calculation gives,
dat = d
∫
Cn
xνt(x)
=
( ∫
Cn
x ⊗ (x − at)νt(dx)
)
dBt
=
( ∫
Rd
(x − at)⊗2νt(dx)
)
dBt
= Cov(νt)dBt. (11)
Therefore, at is a martingale, and
d[⟨at, e i⟩]t =
∑
j∈[n]
Cov(νt)2
i,j ≥ Cov(νt)2
i,i = (1 − ⟨at, e i⟩2)2dt, (12)
implying that ⟨at, e i⟩ converges to {±1} almost surely and that νt converges weakly to to δa∞ ,
which also implies that
lim
t→∞
at ∈ A ⇔ lim
t→∞
νt(A) = 1 ,
7
for all A ⊂ C n. Since νt(A) is a martingale, we have that
P
(
lim
t→∞
at ∈ A
)
= lim
t→∞
Eνt(A) = ν(A),
implying the third part.
Next, we have by Itˆ o’s formula, for all x ∈ C n,
d log Ft(x) = dFt(x)
Ft(x) − d[F (x)]t
2Ft(x)2
= ⟨x − at, dB t⟩ − 1
2 |x − at|2dt
= ⟨x, dB t + atdt⟩ + dZt (13)
where Zt is an Itˆ o process that does not depend on x (here we used the fact that |x|2 is constant
on Cn). Therefore,
log Ft(x) = ⟨x, w t⟩ + ct
where ct is some Itˆ o process andwt = Bt +
∫ t
0 asds. The above display and the fact that νt is a
probability measure, implies that
νt = τwtν, (14)
and therefore also
at =
∫
Cn
xdνt(x) =
∫
Cn
xdτwtν(x) = aν(wt).
The process wt thus satisﬁes the equation
w0 = 0, dw t = dBt + aν(wt)dt. (15)
The above equation gives an alternative construction for th e process deﬁned in (10). Due to the
Markov property of the measure-valued process νt, the above discussion leads to the following
result.
Proposition 10. Given a measure ν and a vector v ∈ Rn, consider the process deﬁned by the
equation
u0 = v, du t = dBt + aν(ut)dt.
Then X = lim t→∞ aν(ut) exists and is a point in Cn almost surely, and has the law τvν.
Proof. Consider the measure ˜ν = τvν and let wt be the process constructed as above with ν
replaced by ˜ν in equation (10). Observe that by deﬁnition
a˜ν(x) = aν(x + v), ∀x ∈ Rn.
In light of (15) and by the uniqueness of the solution to the ab ove SDE, we have that wt +v = ut
almost surely, for all t. The result now follows from part 3 of Proposition 9 and the fa ct that
at = a˜ν(wt) = aν(ut).
8
