---
doc_id: arxiv-1712.04212v4
doc_title: "CONCENTRATION OF 1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY WITH DIRICHLET BOUNDARY CONDITION"
section_id: sec-004-5-finite-dimensional-comparisons
section_title: "Finite dimensional comparisons"
section_number: 5
pages: 22-26
source_pdf: 1712.04212v4.pdf
source_sha256: 521911fc8724f3c2
doc_brief: "CONCENTRATION OF 1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY WITH DIRICHLET BOUNDARY CONDITION — In this paper, we consider a concentration of measure problem on Riemannian manifolds with"
---
5.1. Estimates. To prove Theorem 1.3, we begin with the following:
Lemma 5.1. Let ∂M be compact. For N ∈ [n,∞), let us assume
RicN
f,∂M⊥≥ (N−1)κ andHf,∂M≥ (N−1)λ. Suppose additionally that
InRadM≤ D for some D >0. For η∈ (0, 1), let Ω⊂ M be a Borel
subset with mM,f (Ω)≥η and dM(Ω,∂M )> 0. Then we have
sN,κ,λ(dM(Ω,∂M ))≤sN,κ,λ(D)(1−η),
wheresN,κ,λ is the function deﬁned as (2.18).
Proof. We putr :=dM(Ω,∂M ). Since the open r-neighborhood of ∂M
and Ω are mutually disjoint, we see
η≤mM,f (Ω)≤ 1−mM,f (Br(∂M )).
From InRadM≤ D we derive M = BD(∂M ); in particular, we have
mM,f (BD(∂M )) = 1. Therefore, Theorem 2.7 leads to
η≤ 1− mM,f (Br(∂M ))
mM,f (BD(∂M ))≤ 1− sN,κ,λ(r)
sN,κ,λ(D).
This yields the lemma. 2
One can also show the following lemma by using Theorem 2.8 instead
of Theorem 2.7 in the proof of Lemma 5.1. We omit the proof.
Lemma 5.2. Let ∂M be compact. Assume Ric1
f,∂M⊥≥ (n− 1)κe
−4f
n−1
and Hf,∂M ≥ (n− 1)λe
−2f
n−1 . Suppose additionally that InRadM≤ D
and f≤ (n− 1)δ for some D >0 and δ∈ R. We further assume that
one of the following holds:
1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY 23
(1) κ and λ satisfy the convex-ball-condition;
(2) κ≤ 0 and λ =
√
|κ|.
For η∈ (0, 1), let Ω⊂ M be a Borel subset with mM,f (Ω)≥ η and
dM(Ω,∂M )> 0. Then we have
sn,κe−4δ,λe−2δ(dM(Ω,∂M ))≤sn,κe−4δ,λe−2δ(D)(1−η).
Recall that sκ,λ(t) is the solution of the equation ψ′′(t) +κψ (t) = 0
with ψ(0) = 1, ψ′(0) =−λ. For N∈ (1,∞), and κ and λ satisfying
the ball-condition, we deﬁne a function vN,κ,λ : [0,Cκ,λ]→ [0, 1] by
(5.1) vN,κ,λ(r) :=
∫Cκ,λ
r sN−1
κ,λ (t)dt
∫Cκ,λ
0 sN−1
κ,λ (t)dt
.
Under the curvature condition (2.1), we produce the following:
Theorem 5.3. Let ∂M be compact. For N ∈ [n,∞), let us assume
RicN
f,∂M⊥≥ (N− 1)κ and Hf,∂M≥ (N− 1)λ. Then for every η∈ (0, 1]
the following hold:
(1) if κ and λ satisfy the ball-condition, then
ObsInRad((M,f );−η)≤v−1
N,κ,λ(η);
(2) if κ< 0 and λ =
√
|κ|, then
ObsInRad((M,f );−η)≤ 1
(N− 1)λ log 1
η.
Proof. We may assume that η <1. By Lemma 3.4, it suﬃces to prove
that BSep((M,f );η) is at most the right hand side of the desired in-
equality in each case. We may assume that BSep((M,f );η) is positive.
We ﬁx a Borel subset Ω⊂M with mM,f (Ω)≥η and dM(Ω,∂M )> 0.
Let us consider the case where κ andλ satisfy the ball-condition. In
this case, Theorem 2.5 implies InRad M≤Cκ,λ. By using Lemma 5.1,
η≤ 1− sN,κ,λ(dM(Ω,∂M ))
sN,κ,λ(Cκ,λ) =vN,κ,λ(dM(Ω,∂M )).
Hence,dM(Ω,∂M )≤v−1
N,κ,λ(η). This proves BSep((M,f );η)≤v−1
N,κ,λ(η).
We arrive at the desired inequality.
We next consider the case where κ <0 and λ =
√
|κ|. Notice that
sκ,λ(t) =e−λt. In view of Lemma 5.1, we see
η≤ 1− sN,κ,λ(r)
sN,κ,λ(InRadM)≤ 1− sN,κ,λ(r)∫∞
0 sN−1
κ,λ (t)dt =e−(N−1)λr,
24 YOHEI SAKURAI
where we put r := dM(Ω,∂M ). In particular, dM(Ω,∂M ) is smaller
than or equal to the right hand side of the desired one. We obtain
BSep((M,f );η)≤ 1
(N− 1)λ log 1
η.
Thus, we complete the proof. 2
We also have the following estimate under the condition (2.3):
Theorem 5.4. Let∂M be compact. Assume Ric1
f,∂M⊥≥ (n−1)κe
−4f
n−1
andHf,∂M≥ (n− 1)λe
−2f
n−1 . Suppose additionally that f≤ (n− 1)δ for
some δ∈ R. Then for every η∈ (0, 1] the following hold:
(1) if κ and λ satisfy the convex-ball-condition, then
ObsInRad((M,f );−η)≤v−1
n,κe−4δ,λe−2δ(η);
(2) if κ< 0 and λ =
√
|κ|, then
ObsInRad((M,f );−η)≤ 1
(n− 1)λe−2δ log 1
η.
Proof. The proof is similar to that of Theorem 5.3. For a ﬁxed Ω ⊂M
with mM,f (Ω)≥η, dM(Ω,∂M )> 0, it suﬃces to estimate dM(Ω,∂M )
from above by the right hand side of the desired inequality in each case.
In the case where κ and λ satisfy the convex-ball-condition, from
Theorem 2.6 and Lemma 5.2 we derive
η≤ 1− sn,κe−4δ,λe−2δ(dM(Ω,∂M ))
sn,κe−4δ,λe−2δ(Cκe−4δ,λe−2δ) =vn,κe−4δ,λe−2δ(dM(Ω,∂M )).
In particular, dM(Ω,∂M )≤v−1
n,κe−4δ,λe−2δ(η). This is the desired one.
If κ< 0 and λ =
√
|κ|, then in view of Lemma 5.2 we see
η≤ 1− sn,κe−4δ,λe−2δ(r)∫∞
0 sn−1
κe−4δ,λe−2δ(t)dt =e−(n−1)λe−2δr,
where r :=dM(Ω,∂M ). From the above inequality, we deduce
dM(Ω,∂M )≤ 1
(n− 1)λe−2δ log 1
η.
This completes the proof of Theorem 5.4. 2
1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY 25
5.2. Proof of Theorem 1.3. In order to conclude Theorem 1.3, we
calculate the invariants of the ﬁnite dimensional model spaces.
Lemma 5.5. For every η∈ (0, 1] the following hold:
(1) for the ball-model-space Bn
κ,λ deﬁned as (1.9),
ObsInRad(Bn
κ,λ;−η) = BSep(Bn
κ,λ;η) =v−1
n,κ,λ(η);
(2) for the warped-product-model-spaceMn
κ,λ deﬁned as (1.10),
ObsInRad(Mn
κ,λ;−η) = BSep(Mn
κ,λ;η) = 1
(n− 1)λ log 1
η.
Proof. Let us present the equality for Bn
κ,λ. We show
(5.2) BSep( Bn
κ,λ;η) =v−1
n,κ,λ(η).
LetBη⊂Bn
κ,λ denote the closed geodesic ball with same center as Bn
κ,λ
and mBn
κ,λ(Bη) =η. For the radius rη of Bη, we see
BSep
(
Bn
κ,λ;η
)
=dBn
κ,λ
(
Bη,∂B n
κ,λ
)
=Cκ,λ−rη.
It holds that
η =mBn
κ,λ(Bη) =
∫Cκ,λ
Cκ,λ−rη
sn−1
κ,λ (t)dt
∫Cκ,λ
0 sn−1
κ,λ (t)dt
=vn,κ,λ (Cκ,λ−rη) ;
in particular, Cκ,λ−rη =v−1
n,κ,λ(η). This yields (5.2). Since supp mBn
κ,λ
coincides with Bn
κ,λ, Proposition 3.7 and (5.2) imply the desired one.
For the warped-product-model-space Mn
κ,λ, the same argument as in
the proof of Bn
κ,λ leads to the desired equality. 2
We are now in a position to prove Theorem 1.3.
Proof of Theorem 1.3. Let ∂M be compact. Assume Ric ∂M⊥≥ (n−
1)κ and H∂M ≥ (n− 1)λ. Letting f = log volM(M) and N = n in
Theorem 5.3, for η∈ (0, 1] we have the following (cf. Remark 1.2):
(1) if κ and λ satisfy the ball-condition, then
ObsInRad(M;−η)≤v−1
n,κ,λ(η);
(2) if κ< 0 and λ =
√
|κ|, then
ObsInRad(M;−η)≤ 1
(n− 1)λ log 1
η.
By Lemma 5.5, we complete the proof of Theorem 1.3. 2
26 YOHEI SAKURAI
