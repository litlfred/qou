---
doc_id: arxiv-1712.04212v4
doc_title: "CONCENTRATION OF 1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY WITH DIRICHLET BOUNDARY CONDITION"
section_id: sec-005-6-infinite-dimensional-comparisons
section_title: "Infinite dimensional comparisons"
section_number: 6
pages: 26-30
source_pdf: 1712.04212v4.pdf
source_sha256: 521911fc8724f3c2
doc_brief: "CONCENTRATION OF 1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY WITH DIRICHLET BOUNDARY CONDITION — In this paper, we consider a concentration of measure problem on Riemannian manifolds with"
---
6.1. Relative volume comparisons. In order to prove Theorem 1.4,
we develop comparison geometry of manifolds with boundary under the
curvature condition (2.2). We notice that in our comparison theorems
in this subsection, mM,f need not be a probability measure.
We ﬁrst show the following Laplacian comparison:
Lemma 6.1. Let z∈ ∂M . Let us assume that Ric∞
f (γ′
z(t))≥ K for
all t∈ (0,τ (z)), and Hf,z≥ Λ. Then for all t∈ (0,τ (z))
∆fρ∂M (γz(t))≥Kt + Λ.
Proof. Deﬁne hf,z := (∆fρ∂M )◦γz. By applying the Bochner formula
(2.4) to the distance function ρ∂M , we obtain
0 = Ric∞
f (γ′
z(t)) +‖ Hessρ∂M‖2
HS (γz(t))−g (∇∆fρ∂M,∇ρ∂M ) (γz(t))
≥K−h′
f,z(t).
It holds that hf,z(t)→Hf,z as t→ 0, and hence
hf,z(t)≥Kt +Hf,z≥Kt + Λ.
We arrive at the desired inequality. 2
Furthermore, we prove the following volume element comparison:
Lemma 6.2. Letz∈∂M . Let us assume that Ric∞
f (γ′
z(t))≥K for all
t∈ (0,τ (z)), and Hf,z≥ Λ. Then for all t1,t 2∈ [0,τ (z)) with t1≤t2
θf(t2,z )
θf(t1,z )≤ e−K
2 t2
2−Λt2
e−K
2 t2
1−Λt1
,
whereθf(t,z ) is deﬁned as (2.5).
Proof. By (2.6) and Lemma 6.1, for all t∈ (0,τ (z)) we see
d
dt log θf(t,z )
e−K
2 t2−Λt =−∆fρ∂M (γz(t)) + (Kt + Λ)≤ 0.
This implies the lemma. 2
We now conclude the following relative volume comparison:
Theorem 6.3. Let∂M be compact. Let us assume that Ric∞
f,∂M⊥≥K
and Hf,∂M≥ Λ. Then for all r,R> 0 with r≤R
mM,f (BR(∂M ))
mM,f (Br(∂M ))≤
∫R
0 e−K
2 t2−Λtdt
∫r
0 e−K
2 t2−Λtdt
.
1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY 27
Proof. Using Lemma 6.2, for all t1,t 2≥ 0 with t1≤t2 we have
¯θf(t2,z )e−K
2 t2
1−Λt1≤ ¯θf(t1,z )e−K
2 t2
2−Λt2,
where ¯θf is deﬁned as (2.8). Let us integrate the both sides over [0 ,r ]
with respect to t1, and over [r,R ] with respect to t2. It follows that
∫R
r
¯θf(t2,z )dt2∫r
0
¯θf(t1,z )dt1
≤
∫R
r e−K
2 t2
2−Λt2dt2
∫r
0 e−K
2 t2
1−Λt1dt1
.
The formula (2.7) yields
mM,f (BR(∂M ))
mM,f (Br(∂M ))≤ 1 +
∫R
r e−K
2 t2
2−Λt2dt2
∫r
0 e−K
2 t2
1−Λt1dt1
=
∫R
0 e−K
2 t2
2−Λt2dt2
∫r
0 e−K
2 t2
1−Λt1dt1
.
We complete the proof of Theorem 6.3. 2
Remark 6.1. The author [43] has shown Lemmas 6.1, 6.2 and Theorem
6.3 when K = 0 and Λ = 0 (see Lemmas 3.2, 3.4 and Theorem 5.5 in
[43], and cf. Remark 2.8).
Remark 6.2. Under the same setting as in Theorem 6.3, Morgan [37]
has obtained a similar absolute volume comparison theorem of Heintze-
Karcher type (see Theorem 2 in [37]).
6.2. Distribution laws. Before we show Theorem 1.4, we present dis-
tribution laws concerning our inﬁnite dimensional model spaces.
We observe that our inﬁnite dimensional model spaces appear as the
limits of a sequence of hemispheres {Bn
κ/n,0}, and that of Euclidean
balls{Bn
0,λ/n} for κ,λ> 0 by letting n→∞ .
Proposition 6.4. Let us assume thatκ andλ satisfy the ball-condition.
Then the following distribution laws hold:
(1) if κ> 0 and λ = 0, then
dmI,ρ∂Bn
κ/n,0
dt → e−κ
2 t2
∫
I e−κ
2 t2
dt
as n→∞ , where mI,ρ∂Bn
κ/n,0
denotes the Borel probability mea-
sure of the ρ∂Bn
κ/n,0
-screenIρ∂Bn
κ/n,0
deﬁned as (1.3); in particu-
lar,mI,ρ∂Bn
κ/n,0
weakly converges to the Borel probability measure
of the half-Gaussian-model-space Gκ,0 deﬁned as (1.11);
(2) if κ = 0 and λ> 0, then
dmI,ρ∂Bn
0,λ/n
dt →λe−λt;
28 YOHEI SAKURAI
as n→∞ ; in particular, mI,ρ∂Bn
0,λ/n
weakly converges to the
measure of the exponential-model-space Eλ deﬁned as (1.12).
Proof. We notice that if κ and λ satisfy the ball-condition, then
dmI,ρ∂Bn
κ,λ
dt = sn−1
κ,λ (t)
∫Cκ,λ
0 sn−1
κ,λ (t)dt
, sκ,λ(t) =−
√
κ +λ2sκ(t−Cκ,λ),(6.1)
Cκ,λ =



1√κ
(π
2− tan−1 λ√κ
)
if κ> 0,
λ−1 if κ = 0,
1
2
√
|κ|
logλ +
√
|κ|
λ−
√
|κ|
if κ< 0,
wheresκ(t) is a unique solution of the Jacobi equationψ′′(t)+κψ (t) = 0
with ψ(0) = 0, ψ′(0) = 1; in particular, if κ> 0, then
(6.2) sκ,λ(t) =
√
1 +λ2
κ cos√κ
(
t + 1√κ tan−1 λ√κ
)
,
and if κ = 0, then s0,λ(t) = 1−λt . Therefore, in the case where κ> 0
and λ = 0, the desired convergence follows from (6.1), (6.2) and
cosn−1 t√n→e−t2
2.
In the case where κ = 0 and λ> 0, the formula (6.1) yields
dmI,ρ∂Bn
0,λ/n
dt =λ
(
1− λ
nt
)n−1
→λe−λt
as n→∞ . We complete the observation. 2
We further mention that the exponential-model-space also appears
as the limit of a sequence of warped-product-model-spaces{Mn
κ/n2,λ/n,}
for κ< 0 and λ =
√
|κ| when n→∞ , here λ/n =
√
|κ/n2|.
Proposition 6.5. Letκ< 0 and λ =
√
|κ|. Then
dmI,ρ∂Mn
κ/n2,λ/n
dt →λe−λt;
as n→∞ ; in particular, mI,ρ∂Mn
κ/n2,λ/n
weakly converges to the Borel
probability measure of the exponential-model-space Eλ.
1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY 29
Proof. Let us note that if κ< 0 and λ =
√
|κ|, then sκ,λ(t) =e−λt and
dmI,ρ∂Mn
κ,λ
dt = sn−1
κ,λ (t)∫
I sn−1
κ,λ (t)dt = (n− 1)λe−(n−1)λt.
This proves the assertion. 2
6.3. Proof of Theorem 1.4. One can prove the following result only
by replacing the role of Theorem 2.7 with that of Theorem 6.3 in the
proof of Lemma 5.1. The proof is left to the reader.
Lemma 6.6. Let ∂M be compact. Let us assume Ric∞
f,∂M⊥≥ K and
Hf,∂M≥ Λ. Suppose additionally that InRadM≤D for some D >0.
For η∈ (0, 1), let Ω⊂ M be a Borel subset with mM,f (Ω)≥ η and
dM(Ω,∂M )> 0. Then we have
∫ dM(Ω,∂M )
0
e−K
2 t2−Λtdt≤ (1−η)
∫ D
0
e−K
2 t2−Λtdt.
We are now in a position to prove Theorem 1.4.
Proof of Theorem 1.4. Let∂M be compact. Let us assume Ric∞
f,∂M⊥≥
K andHf,∂M≥ Λ. Suppose either (1) K >0 and Λ∈ R; or (2) K = 0
and Λ > 0. We note again that in this case,
∫∞
0 e−K
2 t2−Λtdt is ﬁnite.
We can assumeη <1. We prove the desired statement by estimating
BSep((M,f );η) from above. We may assume BSep((M,f );η)> 0. Let
Ω⊂M denote a Borel subset with mM,f (Ω)≥η and dM(Ω,∂M )> 0.
Lemma 6.6 leads us to
η≤ 1−
∫dM(Ω,∂M )
0 e−K
2 t2−Λtdt
∫ InRadM
0 e−K
2 t2−Λtdt
≤S K,Λ(dM(Ω,∂M )),
whereSK,Λ : [0,∞]→ [0, 1] is a function deﬁned as
SK,Λ(r) :=
∫∞
r e−K
2 t2−Λtdt
∫∞
0 e−K
2 t2−Λtdt
.
It follows that dM(Ω,∂M )≤S −1
K,Λ(η); in particular, BSep((M,f );η)≤
S−1
K,Λ(η). Here, we can check that
S−1
K,Λ(η) =
{
BSep(GK,Λ;η) if K >0 and Λ∈ R,
BSep(EΛ;η) if K = 0 and Λ > 0,(6.3)
=
{
ObsInRad(GK,Λ;−η) if K >0 and Λ∈ R,
ObsInRad(EΛ;−η) if K = 0 and Λ > 0,
30 YOHEI SAKURAI
where we used Proposition 3.7 in the second equality. By combining
Lemma 3.4, BSep((M,f );η)≤S −1
K,Λ(η) and (6.3), we obtain
ObsInRad((M,f );−η)≤ BSep((M,f );η)
≤
{
ObsInRad(GK,Λ;−η) if K >0 and Λ∈ R,
ObsInRad(EΛ;−η) if K = 0 and Λ > 0.
Thus, we conclude Theorem 1.4. 2
