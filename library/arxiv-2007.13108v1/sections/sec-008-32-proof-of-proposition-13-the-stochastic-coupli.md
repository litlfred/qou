---
doc_id: arxiv-2007.13108v1
doc_title: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-008-32-proof-of-proposition-13-the-stochastic-coupli
section_title: "Proof of Proposition 13: The stochastic coupling"
section_number: 3.2
pages: 11-14
source_pdf: 2007.13108v1.pdf
source_sha256: b298478f5f5b948d
doc_brief: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube — It is well-known that measures whose density is the form e−V where V is a uniformly convex potential on Rn attain"
---
Proposition 13 will be proven via a coupling argument laid ou t below. Let v ∈ Rn and consider
the process
w0 = v, dw t = dBt + aν(wt)dt. (21)
According to Proposition 10, we have that limt→∞ aν(wt) ∼ τvν. This gives rise to the follow-
ing coupling. Let Ut be process adapted to Ft such that for all t, Ut is an orthogonal matrix. Let
ε > 0 and θ ∈ Sn−1, and consider the additional process deﬁned by the equation
u0 = v + εθ, du t = UtdBt + aν(ut)dt. (22)
Similarly to the above, we have limt→∞ aν(wt) ∼ τv+εθν, and therefore
W1(τvν, τ v+εθν) = sup
˜ϕ∈Lip(Cn)
⏐⏐⏐E
[
˜ϕ
(
lim
t→∞
aν(wt)
)]
− E
[
˜ϕ
(
lim
t→∞
aν(ut)
)] ⏐⏐⏐
≤ E
[ ‖‖‖ lim
t→∞
aν(wt) − lim
t→∞
aν(ut)
‖‖‖
1
]
≤ √nE
[ ⏐⏐⏐lim
t→∞
aν(wt) − lim
t→∞
aν(ut)
⏐⏐⏐
2
]
.
Consider the stopping time
τ := inf {t; ut = wt}
and the event E := {τ ≤ 1}. By setting U = In for all t ≥ τ, we get that aν(wt) = aν(ut) for
all t ≥ τ almost surely, and therefore
E holds ⇒ lim
t→∞
|aν(wt) − aν(ut)| = 0.
11
Moreover, since aν(wt) is a martingale (as follows from part 2 of Proposition 9), we h ave
E
[ ⏐⏐⏐aν(wt) − lim
s→∞
aν(ws)
⏐⏐⏐
⏐⏐⏐Ft
]
≤
√
E
[ ⏐⏐⏐aν(wt) − lim
s→∞
aν(ws)
⏐⏐⏐
2
⏐⏐⏐⏐Ft
]
=
√
Tr
(
Cov(τwtν)
)
=
√
Tr(Aν(wt)),
where the ﬁrst equality uses the fact that lims→∞ aν(ws)|Ft has the law τwtν, which follows
from Proposition 10. Combining the above displays and using the triangle inequality, we con-
clude that for all t ≥ 1,
W1(τvν, τ v+εθν) ≤ √nE
[
1EC
⏐⏐⏐lim
t→∞
aν(wt) − lim
t→∞
aν(ut)
⏐⏐⏐
2
]
≤ √nE
[
|aν(wt) − aν(ut))|
]
+ E
[
1EC
( √
nTr(Aν(wt)) +
√
nTr(Aν(ut))
)]
.
(23)
We estimate every term on the right hand side separately, beg inning with the ﬁrst one. Accord-
ing to equation (9), we have almost surely,
|aν(ut) − aν(wt)| ≤ β |ut − wt|. (24)
Using equation (21) and (22), and by Itˆ o’s formula, we have
d|ut − wt|2 = 2⟨ut − wt, du t − dwt⟩ + Tr
(
(Ut − In)2)
dt
= 2⟨ut − wt, (Ut − In)dBt⟩ + 2⟨ut − wt, a ν(ut) − aν(wt)⟩dt + Tr
(
(Ut − In)2)
dt.
(25)
Set
Wt =
∫ t
0
⟨ ut − wt
|ut − wt| , dB t
⟩
, ∀t ≤ τ.
Observe that Wt is a standard Wiener process up to the time τ. Finally, for all t < τ , choose
Ut = In − 2
( wt − ut
|wt − ut|
) ⊗2
,
The reﬂection about the axis spanned by wt − ut. We have, by deﬁnition,
⟨wt − ut, (In − Ut)dBt⟩ = 2|ut − wt|dWt.
Consequently, equation (25) can be written
d|ut − wt|2 = 4|ut − wt|dWt + 4dt + Stdt
where
St = 2⟨ut − wt, a ν(ut) − aν(wt)⟩
(24)
≤ 2β |ut − wt|2.
Now deﬁne Yt = |ut − wt|. Invoking Itˆ o’s formula again, we have that up to time τ, one has
dYt = d (|ut − wt|2)
2|ut − wt| − d [|ut − wt|2]t
8|ut − wt|3
= 2dWt + St + 4
2|ut − wt| dt − 16|ut − wt|2
8|ut − wt|3 dt
= 2dWt + St
2|ut − wt| dt.
12
Combining the two last displays, we learn that there exists a n adapted process Zt such that
dYt = 2dWt + Ztdt, ∀t < τ (26)
such that Zt ≤ βY t almost surely for all t ≤ τ. A ﬁnal application of Itˆ o’s formula gives,
d(e−βtYt) = e−βtdYt − βe −βtYtdt = 2e−βtdWt + e−βt(Zt − βY t)dt. (27)
Therefore, e−βtYt is a supermartingale, and by the optional stopping theorem, we have
E [Yt∧τ ] ≤ eβtE
[
e−β(t∧τ )Yt∧τ
]
= eβtY0 = eβtε.
It follows that
E
[
|aν(wt) − aν(ut))|
] (24)
≤ β E
[
|wt − ut|
]
≤ βe βtε. (28)
It remains to bound the second summand in the right hand side o f (23). To this end, recall that
E is F1-measurable, so we have for all t ≥ 1,
E
[
1EC
√
nTr(Aν(wt))
]
≤ P
(
EC)
sup
v∈Rn
E
[ √
nTr(Aν(wt))
⏐⏐⏐w1 = v
]
. (29)
To give an upper bound for the right hand side, we will ﬁrst nee d the following lemma.
Lemma 14. Let ε > 0. Let Wt be a standard Brownian motion and let Yt, Z t be adapted to Wt,
which satisfy
Xt = ε + Wt +
∫ t
0
Zsds
and such that Zt ≤ 0, almost surely for all t. Let τ = inf {t; Xt = 0}. One has
P(τ ≥ s) ≤ ε√s , ∀s > 0.
Proof. By the reﬂection principle (see [11, Theorem 2.19]), we have
P
(
min
t∈[0,s]
Xt ≤ −ε
)
≥ P
(
min
t∈[0,s]
|Wt + ε| = 0
)
= 2P(Ws ≤ −ε)
= 1 − 2(P(Ws ∈ [0, ε ])
≥ 1 − 2ε√
2πs .
Let t → T (t) be the unique increasing function satisfying
4
∫ T (t)
0
e−2βsds = t, ∀0 ≤ t ≤ 4
∫ ∞
0
e−2βsds.
According to (27),
[e−βtYt]T (s) = 4
∫ T (s)
0
e−2βtdt = s
13
Since, as seen above, the process e−βtYt is a super-martingale, by applying a change of time we
have that the process t → e−βT (t)YT (t) is also a super-martingale (with respect to the ﬁltration
FT (t)). We may invoke the above lemma on this process and use the fac t that 4
∫ 1
0 e−2βsds ≥ 1
β ,
to attain
P
(
EC)
= P(τ ≥ 1) ≤ ε
√
β.
Finally, that by Equation (18) we have for all v ∈ Rn that
E
[ √
nTr(Aν(wt))
⏐⏐⏐w1 = v
]
≤ ne−(t−1)/16.
Combining the last two displays with equation (29), we have
E
[
1EC
√
nTr(Aν(wt))
]
≤ ε
√
βne −(t−1)/16.
By a similar argument, the same bound holds with wt replaced by ut. Together with equations
(23) and (28) this gives
W1(τvν, τ v+εθν) ≤ ε
(
β √neβt + 2
√
βne −(t−1)/16
)
, ∀t ≥ 1.
Choosing t = log(2n)
2β+ 1
8
ﬁnally gives
W1(τvν, τ v+εθν) ≤ 4εβn 1−1/(32β),
completing the proof of Proposition 13.
