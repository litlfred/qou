---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION"
section_id: sec-015-6-berry-esseen-theorem-on-bkn
section_title: "Berry-Esseen theorem on Bk,n"
section_number: 6
pages: 46-50
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION — We study a class of commuting Markov kernels whose simplest element describes the movement ofk particles on a discrete"
---
We state and prove in this section the ﬁrst main result of the manuscript, which consists in a
Berry-Esseen type theorem for the measureξn(∗m). The complete result is a bit more general than
the simpliﬁed version written in Theorem 2.4, in order to give a more precise constant.
Recall that the shift action of R on Tk is given for ⃗ u∈ [0, 2π[k and t∈ R by
Rt(⃗ u) =Sort(u1−t,..., uk−t),
where Sort(⃗ v) is the sequence obtained from ⃗ v∈ [0, 2π[k by sorting it in increasing order, and
Rt(µ) for the image of the measure µ∈M 1(Tk) by the map⃗ u↦→Rt(⃗ u). We then have, for J∈Bk,
Φ[Rt(µ)](J) =
∫
Tk
SJ(⃗ u)|V (⃗ u)|2dRtµ(⃗ u) =
∫
Tk
SJ(⃗ u+t1k)|V (⃗ u+t1k)|2dµ(⃗ u)
= exp(i⟨λJ⟩t)
∫
Tk
SJ(⃗ u)|V (⃗ u)|2dµ(⃗ u)
= exp(i⟨λJ⟩t)Φ[µ](J).(49)
Comparing Proposition 5.3 with (23) suggests a convergence of the distribution of ξn(∗m), viewed
as a probability distribution onTk, to the marginal distribution of a unitary Brownian motionBα,γ
at time m/n2 with adequate parameters α,γ . We will quantify this convergence in terms of the
1-Wassertein metric on the space of probability measures on Tk. Due to the circular nature of Tk,
deﬁne the metric
dTk(z,z′) =
vuu√ inf
σ∈Sk
k∑
i=1
dR(zi−z′
σ(i), 2πZ)2
on Tk. This is indeed a metric, since dTk(z,z′) = W2(δz,δz′), where the Wasserstein distance W2
is taken on the metric space R/Z with the natural distance and δz =∑k
i=1δzi. Remark that when
z,z′∈]0, 1/2[k, one has dTk(z,z′) =‖z−z′‖2.
We then deﬁne the 1-Wasserstein distance WTk
1 on Tk with respect to the metric dTk as
WTk
1 (µ,ν ) = sup
(⏐⏐⏐⏐
∫
Tk
fdµ−
∫
Tk
fdν
⏐⏐⏐⏐, f: (Tk,dTk)→ (R,d R) 1−Lipschitz
)
,
for µ,ν ∈M 1(Tk).
Theorem 6.1 (Berry-Esseen Theorem). LetM >0 and suppose that m = (µr)1≤r≤m is a sequence
ofh-probability measures onBk,n such that Var 3(m)≤MVar⟨m⟩3/2 and⟨ ˆm⟩3≤MK (m)3/2, and
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 47
set t0 = (2π)2m
n2 . Then, there are numeric constants c1,c 2 > 0 such that for all I∈ Bk,n, setting
µ =Rm⟨m⟩
kn
(ξn [(∗m)∗δI]) and ν =Bα,γ
ξn(I) (t0) (viewed as a distribution on Tk),
WTk
1 (µ,ν )≤ M
n
(
c1(k8γ +kα) logn + c2k9/2
√t0
KSU (k)
γt0/2 (ξn(I),ξn(I))1/2
)
,
for some numeric constants c1,c 2> 0, with
α = 1
2Var (m), γ= k
2(k2− 1)K(m).
Theorem 2.4 given in Section 2 is then a simpliﬁed version of the latter result, using Lemma 5.4
to bound⟨ ˆm⟩3 by 2
√
2k3‖ ˜m‖3. The main ingredients in the proof of Theorem 6.1 is Proposition
5.3 together the adaption of an approach of [9] relating the Wassertein distance to the Fourier
transform.
6.1. Wasserstein distance onTk. In [9], the authors related the Wassertein distance between two
probability measures on R/2πZ to a weighted norm of the diﬀerence of their Fourier transform. We
will use the same method on Tk, taking advantage of the Fourier transform which has been deﬁned
in Section 4.3 (the reader should refer to this section for the notation used in this paragraph). For
J∈Bk, set κ(J) :=‖J− k−1
2 1k‖2−‖ ˜I0‖2. Then, according to (23), κ(J) =κk,k(J) for J∈Bk,n.
We ﬁrst have the following result relating the Wassertein distance between two probability measures
on U(k) to the diﬀerence between their Fourier transform, in a similar way as in [9].
Lemma 6.2. Forµ,ν ∈M 1(U(k)) which are conjugation invariant and all t> 0,
W1,U(k)(µ,ν )≤ 2
√
2tk +
vuuu√
∑
J∈Bk
J⁄=I0
exp(−2κ(J)t)
κ(J) |Φ[µ](J)− Φ[ν](J)|2,
where the Wassertein distance is taken with respect to the metric on U(k) induced by⟨·,·⟩k,k on uk.
Proof. Note ﬁrst that for any function f : U(k) → R central and 1-Lipschitz, ∇f is almost-
everywhere deﬁned and essentially bounded by 1 so that
−
∫
U(k)
f∆(f)dµH =
∫
Uk
‖∇f‖2dµH≤ 1.
Sincef is central, we have the expansion f =∑
λ∈Bk Φ[f](J)χJ where (χJ)J∈Bk is an orthonormal
family ofL2(U(k),µH) satisfying ∆χJ =−κ(J)χJ (see [21, Prop. 12.1.2]) and such thatχJ =SJ◦p,
see Section 4.3. Hence,
∑
J∈Bk
κ(J)|Φ[f](J)|2 =−
∫
U(k)
f∆(f)dµ≤ 1.
48 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
By using Parseval and Cauchy-Schwartz equalities, we deduce that for any central probability
densities g1,g 2 on U(k) such that g1,g 2∈L2(U(k),µH),
⏐⏐⏐⏐⏐
∫
U(k)
fg 1dµH−
∫
U(k)
fg 2dµH
⏐⏐⏐⏐⏐ =
⏐⏐⏐⏐⏐
∫
U(k)
f(g1−g2)dµH
⏐⏐⏐⏐⏐
=
⏐⏐⏐⏐⏐⏐⏐⏐
∑
J∈Bk
J⁄=I0
Φ[f](J)Φ[g1−g2](J)
⏐⏐⏐⏐⏐⏐⏐⏐
≤
vuu√
∑
J∈Bk
J⁄=I0
κ(J)|Φ[f](J)|2·
vuuu√
∑
J∈Bk
J⁄=I0
1
κ(J)|Φ[g1](J)− Φ[g2](J)|2
≤
vuuu√
∑
J∈Bk
J⁄=I0
1
κ(J)|Φ[g1](J)− Φ[g2](J)|2,(50)
where we used on the second equality that Φ[ g1−g2](I0) = 0 because
∫
U(k)g1dµH =
∫
U(k)g2dµH.
For arbitrary conjugation invariant probability measures µ,ν on U(k) we use as in [9] the heat
kernel on U(k) for regularization purpose. Such heat kernel corresponds to the special case α =
γ = k of the family of heat kernels deﬁned in Section 4.4. Denote by µt (resp. νt) a solution at
time t≥ 0 of the heat equation with initial measure µ (resp ν). On the one hand, by the diﬀusion
equation of the heat equation, see (23) with α =γ =k,
(51) Φ[ µt](J) =e−κ(J)tΦ[µ](J).
On the other hand, denoting by Kt(x,y ) the heat kernel on U(k) and d(x,y ) the distance on U(k),
⏐⏐⏐⏐⏐
∫
U(k)
fdµt−
∫
U(k)
fdµ
⏐⏐⏐⏐⏐ =
⏐⏐⏐⏐⏐
∫
U(k)
(∫
U(k)
Kt(x,y )f(y)dµH(y)
)
dµ(x)−
∫
U(k)
fdµ
⏐⏐⏐⏐⏐
≤
∫
Uk
(∫
U(k)
Kt(x,y )|f(y)−f(x)|dµH(y)
)
dµ(x)
≤
∫
Uk
(∫
U(k)
Kt(x,y )d(x,y )dµH(y)
)
dµ(x)
≤
∫
Uk
(∫
U(k)
Kt(e,y )d(e,y )dµH(y)
)
dµ(x)
≤
∫
U(k)
Kt(e,y )d(e,y )dµH≤
√∫
U(k)
Kt(e,y )d(e,y )2dµH,
where we used the fact that f is 1-Lipschitz on the second inequality and the bi-invariant property
of the heat-kernel on Uk on the third inequality. By [10, Lemma 6] (which is a consequence of
the Laplacian comparison theorem) applied to the Riemannian manifold U(k) of dimension k2 and
positive scalar curvature, ∫
U(k)
Kt(e,y )d(e,y )2dµH≤ 2k2t.
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 49
Hence,
(52)
⏐⏐⏐⏐⏐
∫
U(k)
fdµt−
∫
U(k)
fdµ
⏐⏐⏐⏐⏐≤k
√
2t.
Using (50), (51) and (52) yields then for t> 0
⏐⏐⏐⏐⏐
∫
U(k)
fdµ−
∫
U(k)
fdν
⏐⏐⏐⏐⏐≤
⏐⏐⏐⏐⏐
∫
U(k)
fdµ−
∫
U(k)
fdµt
⏐⏐⏐⏐⏐ +
⏐⏐⏐⏐⏐
∫
U(k)
fdµt−
∫
U(k)
fdνt
⏐⏐⏐⏐⏐
+
⏐⏐⏐⏐⏐
∫
U(k)
fdν−
∫
U(k)
fdνt
⏐⏐⏐⏐⏐
≤2
√
2tk +
vuuu√
∑
J∈Bk
J⁄=I0
exp(−2κ(J)t)
κ(J) |Φ[µ](J)− Φ[ν](J)|2.
Taking the supremum on all f :U(k)→ R which are 1-Lipschitz yields then
W1,U(k)(µ,ν )≤ 2
√
2tk +
vuuu√
∑
J∈Bk
J⁄=I0
exp(−2κ(J)t)
κ(J) |Φ[µ](J)− Φ[ν](J)|2
for µ,ν central probability distributions on U(k). To conclude, for µ,ν ∈M 1(Tk) we have by
Lemma 6.3 which is proven below
W1,Tk(µ,ν )≤W1,U(k)(p⋆(µ),p⋆(ν))≤ 2
√
2tk +
vuuu√
∑
J∈Bk
J⁄=I0
exp(−2κ(J)t)
κ(J) |Φ[µ](J)− Φ[ν](J)|2.
□
The latter lemma involves measures on Uk, whereas we are rather interested in measures on Tk.
Recall from Section 4.3 that any probability measureµ onTk yields a probability measurep⋆(µ) on
Uk by considering the unique conjugation invariant measure whose image by p is µ. Next lemma
shows that the mapp⋆ is coercive from the metric space (Tk,W 1,Tk) to the metric space (Uk,W 1,Uk).
Lemma 6.3. For any µ,ν ∈M 1(Tk),
W1,U(k)(p⋆(µ),p⋆(ν))≥W1,Tk(µ,ν ).
Proof. For any function f : Tk → R, set ˆf = f◦p, where p : Uk → Tk is the projection on
the ordered set of eigenvalues. Let U,U′∈ U(k). Remark ﬁrst that ‖U−U′‖HS ≤ dUk(U,U′),
where the former norm is the Hilbert-Schmidt norm on Mk(C), see [42, Lemma 1.3] (this can be
deduced from the fact that ‖·‖ HS is the Euclidean distance on Mn(C) and U(k) is a Riemannian
submanifold of Mn(C)). Let ( λi)1≤i≤k (resp. (µi)1≤i≤k) be the eigenvalues of U (resp U′). Then,
by Hoﬀman-Wielandt inequality,
min
σ∈Sk
k∑
i=1
|λi−µσi|2≤‖U−U′‖HS,
50 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
and, since we have d(u1−u2, 2πZ)≤| exp(iu1)− exp(iu2)| for u1,u 2∈ R,
dTk(p(U),p (U′))≤ min
σ∈Sk
k∑
i=1
|λi−µσi|2≤‖U−U′‖HS≤dUk(U,U′).
Hence, if f is Lipschitz with Lipschitz constant equal to 1, we have
| ˆf(U)− ˆf(U′)| =|f(p(U))−f(p(U′)|≤ dTk(p(U),p (U′))≤dUk(U,U′),
and ˆf is again Lipschitz with Lipschitz constant equal to 1. Since∫
Uk
f◦pdp⋆(µ) =
∫
Tk
fdp⋆p⋆(µ) =
∫
Tk
fdµ,
we deduce that
W1,U(k)(p⋆(µ),p⋆(ν)) = sup
(⏐⏐⏐⏐
∫
Uk
fdp⋆(µ)−
∫
Uk
fdp⋆(ν)
⏐⏐⏐⏐, f: (Uk,dUk)→ (R,d R) 1−Lipschitz
)
,
≥ sup
(⏐⏐⏐⏐
∫
Uk
ˆfdp⋆(µ)−
∫
Uk
ˆfdp⋆(ν)
⏐⏐⏐⏐, f: (Tk,dTk)→ (R,d R) 1−Lipschitz
)
≥ sup
(⏐⏐⏐⏐
∫
Tk
fdµ−
∫
Tk
fdν
⏐⏐⏐⏐, f: (Tk,dTk)→ (R,d R) 1−Lipschitz
)
≥W1,Tk(µ,ν ).
□
Combining the two previous lemmas yields then the following proposition.
Proposition 6.4. Forµ,ν ∈M 1(Tk) which are conjugation invariant and all t> 0,
W1,U(k)(µ,ν )≤ 2
√
2tk +
vuuu√
∑
J∈Bk
J⁄=I0
exp(−2κ(J)t)
κ(J) |Φ[µ](J)− Φ[ν](J)|2.
