---
doc_id: arxiv-1712.04212v4
doc_title: "CONCENTRATION OF 1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY WITH DIRICHLET BOUNDARY CONDITION"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-8
source_pdf: 1712.04212v4.pdf
source_sha256: 521911fc8724f3c2
doc_brief: "CONCENTRATION OF 1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY WITH DIRICHLET BOUNDARY CONDITION — In this paper, we consider a concentration of measure problem on Riemannian manifolds with"
---
In the present paper, we consider a concentration of measure problem
on manifolds with boundary. We study concentration phenomena of
non-negative 1-Lipschitz functions with Dirichlet boundary condition.
1.1. Motivations. Let us recall the following well-known fact: The
normalized volume measure on the n-dimensional unit sphere concen-
trates around the equator when n is large. One can rephrase this fact
as follows: The normalized volume measure on the n-dimensional unit
hemisphere concentrates around the boundary when n is large.
We call a triple X = (X,dX,µX) a (smooth) metric measure space
with boundary when X is a connected complete Riemannian manifold
Date: August 16, 2018.
2010 Mathematics Subject Classiﬁcation. Primary 53C23; Secondary 58C40.
Key words and phrases. Concentration of measure; Manifold with boundary;
Comparison theorem; Ricci curvature; Mean curvature; Dirichlet eigenvalue.
1
arXiv:1712.04212v4  [math.MG]  16 Aug 2018
2 YOHEI SAKURAI
with boundary,dX is the Riemannian distance, andµX is a Borel prob-
ability measure on X. Let ∂X denote its boundary. In this paper, we
consider the following problem: For a given sequence {Xn} of metric
measure spaces with boundary Xn = (Xn,dXn,µXn), does the measure
µXn concentrate around ∂Xn when n is large ? We will observe that
µXn concentrates around ∂Xn if and only if every 1-Lipschitz function
ϕn :Xn→ [0,∞) withϕn|∂Xn = 0 is closed to zero (more precisely, see
Remark 1.1 and Proposition 3.6). From this point of view, we inves-
tigate concentration phenomena of non-negative 1-Lipschitz functions
with Dirichlet boundary condition around zero. We call such phenom-
ena boundary concentration phenomena.
1.2. Observable inscribed radii. Gromov [13] has established the-
ory of geometry of metric measure spaces based on the idea of concen-
tration of measure phenomena discovered by L´ evy [23], and developed
by V. D. Milman [31], [32]. He has introduced some important invari-
ants on metric measure spaces. One of them is the so-called observable
diameter that measures the diﬀerence between 1-Lipschitz functions
and constants. The observable diameter has been widely studied from
the view point of the study of concentration phenomena of 1-Lipschitz
functions (see e.g., [13], [22], [46] and the references therein).
We now introduce a new invariant on metric measure spaces with
boundary called the observable inscribed radius that measures the dif-
ference between non-negative 1-Lipschitz functions with Dirichlet bound-
ary condition and zero. We will refer to the formulation of the observ-
able diameter on metric measure spaces.
LetX = (X,dX,µX) be a metric measure space with boundary. Let
ρ∂X : X→ [0,∞) stand for the distance function from the boundary
∂X deﬁned as ρ∂X(x) := dX(x,∂X ). The function ρ∂X is 1-Lipschitz
with ρ∂X|∂X = 0. The inscribed radius InRadX of X is deﬁned to be
the supremum of the distance function ρ∂X over X. We extend the
notion of the inscribed radius to all subsets of X. For Ω ⊂ X, we
deﬁne the inscribed radius InRad Ω of Ω as follows: If Ω ⁄=∅, then
(1.1) InRad Ω := sup
x∈Ω
ρ∂X(x);
if Ω =∅, then InRad Ω := 0. Forξ∈ (−∞, 1], let us deﬁne theξ-partial
inscribed radius PartInRad(X;ξ) of X by
(1.2) PartInRad( X;ξ) := inf
Ω⊂X
InRad Ω,
where the inﬁmum is taken over all Borel subsets Ω with µX(Ω)≥ξ.
1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY 3
We set a screen I := [0,∞). For a 1-Lipschitz function ϕ : X→ I
with ϕ|∂X = 0, we call the metric measure space with boundary
(1.3) Iϕ := (I,d I,mI,ϕ)
the ϕ-screen, where mI,ϕ denotes the push-forward ϕ#µX of µX byϕ.
We now deﬁne the following quantity:
Deﬁnition 1.1. Forη >0, we deﬁne the η-observable inscribed radius
ObsInRad(X;−η) of X by
ObsInRad(X;−η) := sup
ϕ
PartInRad(Iϕ; 1−η),
where the supremum is taken over all 1-Lipschitz functions ϕ :X→I
with ϕ|∂X = 0.
We remark that ObsInRad(X;−η) = 0 for all η≥ 1. Furthermore,
ObsInRad(X;−η) is monotone non-increasing in η.
We also introduce the following notion:
Deﬁnition 1.2. We say that a sequence{Xn} of metric measure spaces
with boundary is a boundary concentration family if for every η >0
lim
n→∞
ObsInRad (Xn;−η) = 0.
Remark 1.1. Let{Xn} denote a sequence of metric measure spaces with
boundary Xn = (Xn,dXn,µXn). By the deﬁnition of the observable
inscribed radius,{Xn} is a boundary concentration family if and only
if for every sequence {ϕn} of 1-Lipschitz functions ϕn : Xn→ I with
ϕn|∂Xn = 0, we have dKF (ϕn, 0)→ 0 as n→∞ , where dKF (ϕn, 0) is
the Ky Fan metric betweenϕn and 0 deﬁned as
dKF (ϕn, 0) := inf{ϵ≥ 0|µXn ({x∈Xn|ϕn(x)>ϵ})≤ϵ}.
We further see that the following are equivalent (see Proposition 3.6):
(1){Xn} is a boundary concentration family;
(2) for every sequence {Ωn} of Borel subsets Ω n⊂ Xn satisfying
lim infn→∞µXn(Ωn)> 0, we have limn→∞ dXn(Ωn,∂Xn) = 0;
(3) limn→∞ µXn(Br(∂Xn)) = 1 for every r >0, where Br(∂Xn) is
the closed r-neighborhood of ∂Xn.
1.3. Dirichlet eigenvalues and concentration phenomena. We
study relation between boundary concentration phenomena and large
spectral gap phenomena for Dirichlet eigenvalues of Laplacian. For
n≥ 2, let (M,dM,mM,f ) be an n-dimensional weighted Riemannian
manifold with boundary, namely, M = (M,g ) be an n-dimensional,
4 YOHEI SAKURAI
connected complete Riemannian manifold with boundary, dM is the
Riemannian distance on M, and
(1.4) mM,f :=e−f volM
for some smooth function f : M→ R, where volM is the Riemannian
volume measure on M. The weighted Laplacian ∆f is deﬁned by
(1.5) ∆ f := ∆ +g(∇f,∇·),
where∇ is the gradient, and ∆ is the Laplacian deﬁned as the minus
of the trace of Hessian. In the case where M is compact, we consider
the following Dirichlet eigenvalue problem with respect to ∆ f:
{
∆fφ =νφ in IntM;
φ = 0 on ∂M,
where IntM denotes the interior of M. We denote by
(1.6) 0 <ν f,1(M)<ν f,2(M)≤···≤ νf,k(M)≤···↗ +∞
the all Dirichlet eigenvalues of ∆f, counting multiplicity.
For a smooth function f :M→ R such that mM,f is a Borel proba-
bility measure, we study the metric measure space with boundary
(1.7) ( M,f ) := (M,dM,mM,f ).
Our ﬁrst main result is the following:
Theorem 1.1. Let{(Mn,fn)} be a sequence of compact metric mea-
sure spaces with boundary deﬁned as (1.7). If we have νfn,1(Mn)→∞
as n→∞ , then{(Mn,fn)} is a boundary concentration family.
This is an analogue of the Gromov-V. D. Milman theorem for closed
manifolds (compact manifolds without boundary) (see Theorem 4.1 and
its corollary in [14]). We show Theorem 1.1 by using relation between
the observable inscribed radii and νf,1(M) (see Proposition 4.2).
For higher eigenvalues, we will establish the following assertion under
Ric∞
f,M≥ 0 and Hf,∂M ≥ 0, where Ric∞
f,M and Hf,∂M are the inﬁmum
of the ∞-weighted Ricci curvature and the weighted mean curvature
on M and on ∂M , respectively (more precisely, see Subsection 2.1):
Theorem 1.2. Let{(Mn,fn)} be a sequence of compact metric mea-
sure spaces with boundary deﬁned as (1.7). Assume that Ric∞
fn,Mn≥ 0
and Hfn,∂Mn≥ 0. If there exists k≥ 1 such that νfn,k(Mn)→∞ as
n→∞ , then{(Mn,fn)} is a boundary concentration family.
Theorem 1.2 is an analogue of the Funano-Shioya theorem for closed
manifolds of non-negative ∞-weighted Ricci curvature (see Corollary
1.4 in [12]). One of key ingredients of the proof is to obtain an upper
1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY 5
bound of the ratio νf,k(M)/νf,1(M) in terms ofCk 2 for some universal
constant C > 0 under Ric∞
f,M≥ 0 and Hf,∂M ≥ 0 (see Theorem 2.4).
We obtain such universal estimate by combining an improved Cheeger
inequality of Kwak, Lau, Lee, Oveis Gharan and Trevisan [20], and an
isoperimetric inequality of Wang [49] (see Subsections 2.3, 2.4).
1.4. Comparisons and concentration phenomena. To understand
boundary concentration phenomena, we establish comparison theorems
of the observable inscribed radii under a lower curvature Ricci curva-
ture bound, and a lower mean curvature bound for the boundary.
We ﬁrst present ﬁnite dimensional comparisons. Let M be an n-
dimensional, connected complete Riemannian manifold with boundary
with volM(M)<∞. We study metric measure space with boundary
(1.8) M := (M,dM,mM), m M := 1
volM(M) volM.
Let Ric∂M⊥ stand for the inﬁmum of the Ricci curvature in the ∂M -
radial direction on M, andH∂M the inﬁmum of the mean curvature on
∂M (more precisely, see Subsection 2.1).
Forκ∈ R, let Mn
κ be the n-dimensional space form with constant
curvatureκ. For λ∈ R, we say that κ and λ satisfy the ball-condition
if there exists a closed ball Bn
κ,λ in Mn
κ whose boundary has constant
mean curvature (n− 1)λ. Let Cκ,λ denote its radius. Note that κ and
λ satisfy the ball-condition if and only if either (1) κ >0; (2) κ = 0
and λ >0; or (3) κ <0 and λ >
√
|κ|. We say that κ and λ satisfy
the convex-ball-condition if they satisfy the ball-condition and λ≥ 0.
Let us prepare the following ﬁnite dimensional model spaces: (1) For
κ andλ satisfying the ball-condition, we call the metric measure space
with boundary
(1.9) Bn
κ,λ =
(
Bn
κ,λ,dBn
κ,λ,mBn
κ,λ
)
the ball-model-space; (2) For κ < 0 and λ :=
√
|κ|, we consider the
warped product space Mn
κ,λ := ([0,∞)× Sn−1,dt 2 +e−2λtds2
n−1), where
(Sn−1,ds 2
n−1) is the (n− 1)-dimensional standard unit sphere. We call
the metric measure space with boundary
(1.10) Mn
κ,λ =
(
Mn
κ,λ,dMn
κ,λ,mMn
κ,λ
)
the warped-product-model-space(cf. Remark 2.6).
We have the following ﬁnite dimensional comparison theorem:
Theorem 1.3. Let ∂M be compact. We assume Ric∂M⊥≥ (n− 1)κ
and H∂M≥ (n− 1)λ. Then for every η∈ (0, 1] the following hold:
6 YOHEI SAKURAI
(1) if κ and λ satisfy the ball-condition, then
ObsInRad(M;−η)≤ ObsInRad(Bn
κ,λ;−η);
(2) if κ< 0 and λ =
√
|κ|, then
ObsInRad(M;−η)≤ ObsInRad(Mn
κ,λ;−η).
Remark 1.2. For (1) of Theorem 1.3, we always have vol M(M) <∞.
Indeed, the Heintze-Karcher theorem (Theorem 2.1 in [15]) leads to
volM(M)
vol∂M (∂M )≤
volBn
κ,λ(Bn
κ,λ)
vol∂Bn
κ,λ(∂Bn
κ,λ).
Similarly, for (2), the Heintze-Karcher theorem guarantees that the
Riemannian volume volM(M) of M is ﬁnite.
The proof of Theorem 1.3 is based on comparison geometry of man-
ifolds with boundary established by Heintze and Karcher [15], Kasue
[16], [17], the author [43], [45], and so on (see Subsection 2.5). We
ﬁrst estimate observable inscribed radii under lower weighted curva-
ture bounds by using relative volume comparison theorems for metric
neighborhoods of boundaries (see Theorems 5.3 and 5.4). We conclude
Theorem 1.3 by computing the observable inscribed radii of ﬁnite di-
mensional model spaces (see Lemma 5.5).
We next produce inﬁnite dimensional comparisons for metric mea-
sure spaces with boundary (M,f ) deﬁned as (1.7) under Ric∞
f,∂M⊥≥K
andHf,∂M≥ Λ forK, Λ∈ R, where Ric∞
f,∂M⊥ is the inﬁmum of the∞-
weighted Ricci curvature in the∂M -radial direction onM (see Subsec-
tion 2.1). We prepare the following inﬁnite dimensional model spaces:
(1) ForK >0, Λ∈ R, we call the metric measure space with boundary
(1.11) GK,Λ :=
(
I,d I, e−K
2 t2−Λt
∫
I e−K
2 t2−Λtdt
volI
)
the half-Gaussian-model-space; (2) For Λ > 0, we call
(1.12) EΛ :=
(
I,d I, Λe−Λt volI
)
the exponential-model-space. We remark that for K, Λ∈ R, the value∫
I e−K
2 t2−Λtdt is ﬁnite if and only if either (1) K > 0; or (2) K = 0
and Λ > 0. Moreover, if K = 0 and Λ > 0, then we see
e−K
2 t2−Λt
∫
I e−K
2 t2−Λtdt
= Λe−Λt.
We observe that our inﬁnite dimensional model spaces appear as limits
of sequences of ﬁnite dimensional model spaces (see Subsection 6.2).
1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY 7
We have the following inﬁnite dimensional comparison:
Theorem 1.4. Let∂M be compact. Let us assume Ric∞
f,∂M⊥≥K and
Hf,∂M≥ Λ. Then for every η∈ (0, 1] the following hold:
(1) if K >0 and Λ∈ R, then
ObsInRad((M,f );−η)≤ ObsInRad(GK,Λ;−η);
(2) if K = 0 and Λ> 0, then
ObsInRad((M,f );−η)≤ ObsInRad(EΛ;−η).
To prove Theorem 1.4, we develop comparison geometry of manifolds
with boundary under Ric∞
f,∂M⊥≥K and Hf,∂M≥ Λ for K, Λ∈ R (see
Subsection 6.1). We will show a relative comparison theorem for metric
neighborhoods of boundaries (see Theorem 6.3).
Having Theorems 1.3 and 1.4 at hand, we will study various bound-
ary concentration phenomena of sequences of metric measure spaces
with boundary (see Section 7). For instance, for a sequence of ball-
model-spaces, we conclude the following:
Corollary 1.5. If κ and λ satisfy the convex-ball-condition, then the
sequence{Bn
κ,λ} is a boundary concentration family.
Remark 1.3. In the case whereκ> 0 andλ< 0, the sequence{Bn
κ,λ} is
not a boundary concentration family. Indeed, for r∈ (0,Cκ,λ−Cκ,0), if
we deﬁne Ωn⊂Bn
κ,λ as ther/2-neighborhood of the metric sphere with
same center asBn
κ,λ and radiusCκ,0, then lim infn→∞mBn
κ,λ(Ωn)> 0 and
limn→∞dBn
κ,λ(Ωn,∂B n
κ,λ)> 0 (see Remark 1.1 and Proposition 3.6).
1.5. Organization. In Section 2, we review basics of weighted Rie-
mannian manifolds with boundary, and examine their geometric and
analytic properties. In Section 3, we introduce some invariants on met-
ric measure spaces with boundary, and investigate their fundamental
properties. In Section 4, we prove Theorems 1.1 and 1.2. In Section 5,
we prove Theorem 1.3. In Section 6, we prove Theorem 1.4.
Section 7 is devoted to the collection of boundary concentration phe-
nomena of sequences of metric measure spaces with boundary. We
will determine the critical scale orders of some sequences of ﬁnite di-
mensional model spaces (see Theorems 7.1, 7.2, 7.3). We also prove
Corollary 1.5. Furthermore, we construct several non-trivial examples
of boundary concentration families (see Examples 7.1 and 7.2).
Acknowledgements. The author expresses his gratitude to Ryunosuke
Ozawa and Kohei Suzuki for fruitful discussions and encouragement.
The author would like to thank Shin-ichi Ohta for his useful comments.
8 YOHEI SAKURAI
One of his comment leads to the study of Section 6. The author would
also like to thank Daisuke Kazukawa for informing him of Proposition
3.7 with its proof. The author is deeply grateful to Kei Funano for his
interests in this paper, valuable comments, and informing him of [8].
