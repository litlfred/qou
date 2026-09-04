---
doc_id: arxiv-1712.04212v4
doc_title: "CONCENTRATION OF 1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY WITH DIRICHLET BOUNDARY CONDITION"
section_id: sec-006-7-boundary-concentration-phenomena
section_title: "Boundary concentration phenomena"
section_number: 7
pages: 30-35
source_pdf: 1712.04212v4.pdf
source_sha256: 521911fc8724f3c2
doc_brief: "CONCENTRATION OF 1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY WITH DIRICHLET BOUNDARY CONDITION — In this paper, we consider a concentration of measure problem on Riemannian manifolds with"
---
7.1. Critical scale orders. We ﬁrst state the following assertion con-
cerning the critical scale order of sequences of hemispheres (cf. Propo-
sition 6.4, Subsection 1.1 in [14], Corollary 2.22 in [46], Theorem 8.1.1
and Corollary 8.5.7 in [47]):
Theorem 7.1. Forκ> 0, and for every η∈ (0, 1] we have
(7.1) lim
n→∞
ObsInRad(Bn
κ/n,0;−η) = PartInRad(Gκ,0; 1−η),
whereGκ,0 is the half-Gaussian-model-space deﬁned as (1.11), and the
right hand side of (7.1) is the partial inscribed radius of Gκ,0 deﬁned
as (1.2). In particular, for a sequence {κn} of κn > 0, the sequence
{Bn
κn,0} is a boundary concentration family if and only if nκn→∞ .
Proof. Let us regard then-dimensional standard sphereMn
n/κ with con-
stant curvaturen/κ as an mm-space deﬁned as (1.8) (see Remark 3.1).
We observe that Mn
n/κ is the double of the hemisphere Bn
κ/n,0. Based
on Lemma 5.5 and this geometric observation, we obtain
ObsInRad(Bn
κ/n,0;−η) = BSep(Bn
κ/n,0;η) = 1
2 Sep(Mn
κ/n;η/2,η/ 2),
where Sep(Mn
κ/n;η/2,η/ 2) is the (η/2,η/ 2)-separation distance ofMn
κ/n
deﬁned as (3.4) (see Remark 3.2). It is well-known that the right hand
side tends to r >0 determined by
1−η
2 =
∫r
0 e−κ
2 t2
dt∫∞
−∞ e−κ
2 t2
dt
asn→∞ (see e.g., Theorem 2.1 and Lemma 2.3 in [46]). We see that
r is equal to PartInRad(Gκ,0; 1−η), and hence (7.1).
For a metric measure space with boundary X = (X,dX,µX),
(7.2) ObsInRad( cX;−η) =c ObsInRad(X;−η)
1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY 31
for every c> 0, where we set cX := (X,cdX,µX) (cf. Proposition 2.19
in [46]). Therefore, by (7.1) and Bn
κn,0 =
√
κ (nκn)−1Bn
κ/n,0, we arrive
at the desired conclusion. 2
We next investigate sequences of Euclidean balls.
Theorem 7.2. Forλ> 0, and for every η∈ (0, 1] we have
(7.3) lim
n→∞
ObsInRad(Bn
0,λ/n;−η) = PartInRad(Eλ; 1−η) = 1
λ log 1
η,
whereEλ is the exponential-model-space deﬁned as (1.12). In particu-
lar, for a sequence {λn} of λn > 0, the sequence{Bn
0,λn} is a boundary
concentration family if and only if nλn→∞ .
Proof. By s0,λ/n(t) = 1−λn−1t, we have vn,0,λ/n(r) = (1−λn−1r)n,
where vn,0,λ is deﬁned as (5.1). Lemma 5.5 implies that
ObsInRad(Bn
0,λ/n;−η) = n
λ (1−η
1
n )→ 1
λ log 1
η
as n→∞ . On the other hand, PartInRad( Eλ; 1−η) is equal to a
positive numberr >0 determined as 1−η =
∫r
0 λe−λt dt; in particular,
PartInRad(Eλ; 1−η) = λ−1 logη−1. This proves the equalities (7.3).
Due to Bn
0,λn =λ (nλn)−1Bn
0,λ/n and (7.2), we complete the proof. 2
We also provide the following result for warped-product-model-spaces:
Theorem 7.3. Forκ< 0 and λ =
√
|κ|, and for every η∈ (0, 1]
lim
n→∞
ObsInRad(Mn
κ/n2,λ/n;−η) = PartInRad(Eλ; 1−η) = 1
λ log 1
η.
Moreover, for a sequence {κn} of κn < 0, and for a sequence {λn} of
λn =
√
|κn|, the sequence{Mn
κn,λn} is a boundary concentration family
if and only if we have nλn→∞ as n→∞ .
Proof. Lemma 5.5 yields
ObsInRad(Mn
κ/n2,λ/n;−η) = n
(n− 1)λ log 1
η→ 1
λ log 1
η
as n→∞ . The second equality of (7.3) tells us the desired equalities.
The later assertion also immediately follows from Lemma 5.5 2
Let us give a proof of Corollary 1.5.
Proof of Corollary 1.5. Let κ and λ satisfy the convex-ball-condition.
We will prove that{Bn
κ,λ} is a boundary concentration family.
We ﬁrst consider the case ofκ> 0. In this case, we have λ≥ 0. Due
to Theorem 1.3, we have ObsInRad( Bn
κ,λ;−η)≤ ObsInRad(Bn
κ,0;−η).
32 YOHEI SAKURAI
Furthermore, Theorem 7.1 tells us that {Bn
κ,0} is a boundary concen-
tration family. Hence,{Bn
κ,λ} is also a boundary concentration family.
When κ = 0, the desired statement follows from Theorem 7.2.
In the case of κ <0, it holds that λ >
√
|κ|. In virtue of Theorem
1.3 and Lemma 5.5, we obtain
ObsInRad(Bn
κ,λ;−η)≤ ObsInRad
(
Mn
κ,
√
|κ|;−η
)
= 1
(n− 1)
√
|κ|
log 1
η;
in particular, ObsInRad(Bn
κ,λ;−η)→ 0 as n→∞ . Thus, we complete
the proof of Corollary 1.5. 2
7.2. Positive dimensional cases. In this subsection, we summarize
corollaries of Theorem 5.3. Hereafter, let {(Mn,fn)} be a sequence of
metric measure spaces with compact boundary deﬁned as (1 .7). We
denote by dim Mn the dimension of Mn. Theorem 5.3 together with
Theorems 7.1, 7.2, 7.3 and Corollary 1.5 leads us to the following:
Corollary 7.4. Let{Nn} be a sequence of integers with Nn≥ dimMn,
and let{κn} be a sequence of κn > 0. Assume RicNn
fn,∂M⊥n
≥ (Nn− 1)κn
and Hfn,∂Mn ≥ 0 for each n. If Nnκn → ∞, then {(Mn,fn)} is a
boundary concentration family.
Corollary 7.5. Let{Nn} be a sequence of integers with Nn≥ dimMn,
and let {λn} be a sequence of λn > 0. We assume RicNn
fn,∂M⊥n
≥ 0 and
Hfn,∂Mn≥ (Nn− 1)λn for each n. If Nnλn→∞ , then{(Mn,fn)} is a
boundary concentration family.
Corollary 7.6. Let{Nn} be a sequence of integers with Nn≥ dimMn,
and let{κn} be a sequence of κn < 0. For each n, we put λn :=
√
|κn|.
We assume RicNn
fn,∂M⊥n
≥ (Nn− 1)κn and Hfn,∂Mn ≥ (Nn− 1)λn. If
Nnλn→∞ , then{(Mn,fn)} is a boundary concentration family.
Corollary 7.7. Let{Nn} be a sequence of integers with Nn≥ dimMn.
Assume RicNn
fn,∂M⊥n
≥ (Nn− 1)κ and Hfn,∂Mn≥ (Nn− 1)λ for each n.
We also assume that one of the following holds:
(1) κ and λ satisfy the convex-ball-condition;
(2) κ< 0 and λ =
√
|κ|.
If Nn→∞ , then{(Mn,fn)} is a boundary concentration family.
Now, we will present a concrete example concerning these corollaries,
especially Corollary 7.6:
1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY 33
Example 7.1. Let{Nn} be a sequence of integers with Nn≥n, and
let{κn} be a sequence of κn < 0. For each n, put λn :=
√
|κn|. Deﬁne
a sequence{(~Mn,~fn)} of metric measure spaces with boundary as
~Mn := ([0,∞)× Sn−1,dt 2 +e−2λntds2
n−1),
~fn := (Nn−n)λnρ∂ ~Mn
− log
(
(Nn− 1)λn (volSn−1(Sn−1))−1)
.
Then the sequence {(~Mn,~fn)} is a boundary concentration family if
and only if we have Nnλn→∞ .
Computing the curvatures of ~Mn, we see the following (cf. calcula-
tions in the proof of Lemma 3.1 in [43]): For all z∈∂~Mn and t> 0,
RicNn
~fn
(γ′
z(t)) = (Nn− 1)κn, H ~fn,z = (Nn− 1)λn.
Moreover,θ ~fn(t,z ) =e− ~fn(z)sNn−1
κn,λn(t), whereθ ~fn(t,z ) is deﬁned as (2.5).
This yields m ~Mn, ~fn
(~Mn) = 1. Furthermore, BSep(( ~Mn,~fn);η) is equal
to rn > 0 determined by
volSn−1(Sn−1)
∫ ∞
rn
θ ~fn(t,z )dt =η;
in particular, from Proposition 3.7 we deduce
ObsInRad((~Mn,~fn);−η) = BSep((~Mn,~fn);η) = 1
(Nn− 1)λn
log 1
η.
We conclude the desired statement.
7.3. One dimensional cases. We next summarize corollaries of The-
orem 5.4. Throughout this subsection, we always assume dim Mn =n.
Similarly to the above subsection, one can verify the following asser-
tions by using Theorem 5.4:
Corollary 7.8. Let{κn} be a sequence of κn > 0, and let {δn} be a
sequence of δn∈ R. Let us assume Ric1
fn,∂M⊥n
≥ (n− 1)κne
−4fn
n−1 and
Hfn,∂Mn≥ 0 for each n. Suppose additionally that fn≤ (n− 1)δn. If
nκne−4δn→∞ , then{(Mn,fn)} is a boundary concentration family.
Corollary 7.9. Let{λn} be a sequence of λn > 0, and let {δn} be
a sequence of δn∈ R. Let us assume Ric1
fn,∂M⊥n
≥ 0 and Hfn,∂Mn≥
(n−1)λne
−2fn
n−1 for eachn. Suppose additionally that fn≤ (n−1)δn. If
nλne−2δn→∞ , then{(Mn,fn)} is a boundary concentration family.
Corollary 7.10. Let{κn} be a sequence of κn < 0, and let {δn} be a
sequence ofδn∈ R. For each n, put λn :=
√
|κn|. Assume Ric1
fn,∂M⊥n
≥
(n− 1)κne
−4fn
n−1 and Hfn,∂Mn≥ (n− 1)λne
−2fn
n−1 . Suppose additionally
34 YOHEI SAKURAI
that fn≤ (n− 1)δn. If nλne−2δn→∞ , then{(Mn,fn)} is a boundary
concentration family.
Corollary 7.11. We assume Ric1
fn,∂M⊥n
≥ (n−1)κe
−4fn
n−1 andHfn,∂Mn≥
(n− 1)λe
−2fn
n−1 for each n. Suppose additionally that fn≤ (n− 1)δ for
some δ∈ R. We also assume that one of the following holds:
(1) κ and λ satisfy the convex-ball-condition;
(2) κ< 0 and λ =
√
|κ|.
Then{(Mn,fn)} is a boundary concentration family.
Let us construct a concrete example for the above corollaries:
Example 7.2. Let{κn} be a sequence of κn < 0, and let {δn} be a
sequence of δn∈ R. For each n, we put λn :=
√
|κn|. Let us denote by
(Sn−1
κn,λn,δn,ds 2
n−1,κn,λn,δn) the (n− 1)-dimensional sphere with volume
e−Cn
(∫ ∞
1
exp
(
−(n− 1)λne−2δn
2 t2
)
dt
)−1
,
whereCn := 2−1 (n−1) (λne−2δn−2δn). We deﬁne a sequence{(~Mn,~fn)}
of metric measure spaces with boundary as
~Mn :=
(
[0,∞)× Sn−1
κn,λn,δn, dt2 +H2
κn,λn,δn(t)ds2
n−1,κn,λn,δn
)
,
~fn :=−n− 1
2 log
(
ρ∂ ~Mn
+ 1
)
+(n− 1)δn,
where
Hκn,λn,δn(t) := 1√t + 1 exp
(
−λne−2δn
2
(
(t + 1)2− 1
))
.
Ifnλne−2δn→∞ , then{(~Mn,~fn)} is a boundary concentration family.
We derive this statement from Corollary 7.10. We rewrite ~Mn as
~Mn =
(
[0,∞)× Sn−1
κn,λn,δn, dt2 +F 2
κn,λn,z(t)ds2
n−1,κn,λn,δn
)
,
where for each z∈∂~Mn,
s ~fn,z(t) :=
∫ t
0
e
−2 ~fn(γz (a))
n−1 da,
Fκn,λn,z(t) := exp
(~fn(γz(t))− ~fn(z)
n− 1
)
sκn,λn(s ~fn,z(t)).
From this expression, one can compute the curvatures of~Mn as follows
(cf. calculations in the proof of Lemmas 3.5, 5.2 and 7.1 in [45]): For
1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY 35
all z∈∂~Mn and t> 0 we have
Ric1
~fn
(γ′
z(t)) = (n− 1)κne
−4 ~fn(γz (t))
n−1 , H ~fn,z = (n− 1)λne
−2 ~fn(z)
n−1 .
Moreover,θ ~fn(t,z ) =e− ~fn(z)sn−1
κn,λn(s ~fn,z(t)), and hence
θ ~fn(t,z ) =eCn exp
(
−(n− 1)λne−2δn
2 (t + 1)2
)
;
in particular, we see m ~Mn, ~fn
(~Mn) = 1. Since ~fn≤ (n− 1)δn, Corollary
7.10 leads us to the desired conclusion.
