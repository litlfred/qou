---
doc_id: arxiv-1712.04212v4
doc_title: "CONCENTRATION OF 1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY WITH DIRICHLET BOUNDARY CONDITION"
section_id: sec-001-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 8-14
source_pdf: 1712.04212v4.pdf
source_sha256: 521911fc8724f3c2
doc_brief: "CONCENTRATION OF 1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY WITH DIRICHLET BOUNDARY CONDITION — In this paper, we consider a concentration of measure problem on Riemannian manifolds with"
---
Throughout this section, let (M,dM,mM,f ) denote ann-dimensional
weighted Riemannian manifold with boundary deﬁned as (1.4).
2.1. Curvatures. We denote by Ricg the Ricci curvature onM deter-
mined by the Riemannian metric g, and by RicM the inﬁmum of Ricg
on the unit tangent bundle overM. For N∈ (−∞,∞], theN-weighted
Ricci curvature RicN
f is deﬁned as follows: If N∈ (−∞,∞)\{n}, then
RicN
f := Ricg + Hessf− df⊗df
N−n,
where df and Hessf are the diﬀerential and the Hessian of f, respec-
tively; otherwise, ifN =∞, then RicN
f := Ricg + Hessf; ifN =n, and
if f is constant, then RicN
f := Ricg; if N =n, and if f is not constant,
then RicN
f :=−∞ ([1], [24]). For a function F :M→ R, we mean by
RicN
f,M≥F for every x∈M, and for every unit tangent vector v at x
it holds that RicN
f (v)≥F (x).
Remark 2.1. Traditionally,N has been chosen from [ n,∞] (see e.g.,
[30], [42], [50]). On the other hand, recently, various properties have
begun to be studied in the complemental case of N ∈ (−∞,n ) (see
e.g., [19], [18], [36], [38], [39], [40], [41], [51], [52]). We notice the
monotonicity of Ric N
f with respect to N: If N1, N2 ∈ [n,∞] with
N1 ≤ N2, then Ric N1
f ≤ RicN2
f ; if N1 ∈ [n,∞] and N2 ∈ (−∞,n ),
then RicN1
f ≤ RicN2
f ; if N1, N2∈ (−∞,n ) with N1≤N2, then RicN1
f ≤
RicN2
f .
Forz∈∂M , letuz denote the unit inner normal vector for ∂M atz,
and let γz : [0,T )→M denote the geodesic with γ′
z(0) =uz. We put
τ(z) := sup{t> 0|ρ∂M (γz(t)) =t}.
Let Ric∂M⊥ be the inﬁmum of the Ricci curvature in the ∂M -radial
direction on M deﬁned as infz,t Ricg(γ′
z(t)), where the inﬁmum is take
over allz∈∂M, t∈ (0,τ (z)). ForF :M→ R, we mean by RicN
f,∂M⊥≥
F for all z∈∂M, t∈ (0,τ (z)) we have RicN
f (γ′
z(t))≥F (γz(t)).
For vector ﬁeldsv1, v2 on∂M , the second fundamental formS(v1,v 2)
is deﬁned as the normal component of∇g
v1v2 with respect to∂M , where
1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY 9
∇g denotes the Levi-Civita connection induced from g. For z∈ ∂M ,
let Tz∂M denote the tangent space at z on ∂M . The shape operator
Auz :Tz∂M→Tz∂M for uz is deﬁned as
g(Auzv1,v 2) :=g(S(v1,v 2),uz).
The mean curvatureHz atz is deﬁned as the trace ofAuz. Put H∂M :=
infz∈∂M Hz. The weighted mean curvature Hf,z at z is deﬁned by
Hf,z :=Hz +g((∇f)z,uz).
For a functionG : ∂M→ R, we mean by Hf,∂M ≥G we have Hf,z≥
G(z) for all z∈∂M .
We mainly study the following three curvature conditions: Forκ,λ∈
R and K, Λ∈ R,
N∈ [n,∞), RicN
f,∂M⊥≥ (N− 1)κ, Hf,∂M≥ (N− 1)λ; (2.1)
N =∞, Ric∞
f,∂M⊥≥K, Hf,∂M≥ Λ; (2.2)
N = 1, Ric1
f,∂M⊥≥ (n− 1)κe
−4f
n−1, Hf,∂M≥ (n− 1)λe
−2f
n−1.(2.3)
Remark 2.2. We give a historical comment for the curvature condition
(2.3). First, Wylie [51] has obtained a splitting theorem of Cheeger-
Gromoll type under RicN
f,M≥ 0 forN∈ (−∞, 1]. After that Wylie and
Yeroshkin [52] have introduced the condition Ric 1
f,M ≥ (n− 1)κe
−4f
n−1
from the view point of study of aﬃne connections, and established com-
parison geometry. Furthermore, the author [45] has studied comparison
geometry of manifolds with boundary under the curvature condition
RicN
f,M≥ (n− 1)κe
−4f
n−1 and Hf,∂M≥ (n− 1)λe
−2f
n−1 for N∈ (−∞, 1].
2.2. Laplacians and Dirichlet eigenvalues. For the weighted Lapla-
cian ∆f deﬁned as (1.5), the following formula of Bochner type is well-
known (see e.g., Chapter 14 in [48]): For every smooth ψ :M→ R,
(2.4) − 1
2 ∆f‖∇ψ‖2 = Ric∞
f (∇ψ) +‖ Hessψ‖2
HS−g (∇∆fψ,∇ψ),
where‖·‖ and‖·‖ HS are the canonical norm and the Hilbert-Schmidt
norm induced from g, respectively.
Forz∈∂M , the value ∆fρ∂M (γz(t)) converges toHf,z ast→ 0. For
t∈ (0,τ (z)), and for the volume element θ(t,z ) of the t-level surface
of ρ∂M at γz(t), we set
(2.5) θf(t,z ) :=e−f(γz(t))θ(t,z ).
For allt∈ (0,τ (z)) it holds that
(2.6) ∆ fρ∂M (γz(t)) =−θ′
f(t,z )
θf(t,z ).
10 YOHEI SAKURAI
We also have the following (see e.g., [43]): If ∂M is compact, then
(2.7) mM,f (Br(∂M )) =
∫
∂M
∫ r
0
¯θf(t,z )dtd volh
for all r > 0, where vol h is the Riemannian volume measure on ∂M
induced from h, and ¯θf : [0,∞)×∂M→ R is a function deﬁned as
(2.8) ¯θf(t,z ) :=
{
θf(t,z ) if t<τ (z),
0 if t≥τ(z).
LetM be compact. Forφ∈H1
0(M,mM,f )\{0}, its Rayleigh quotient
is deﬁned as
(2.9) Rf(φ) :=
∫
M‖∇φ‖2dmM,f∫
M φ2dmM,f
.
For thek-th Dirichlet eigenvalueνf,k(M) of the weighted Laplacian ∆f
deﬁned as (1.6), the min-max principle states
(2.10) νf,k(M) = inf
L
sup
φ∈L\{0}
Rf(φ),
where the inﬁmum is taken over all k-dimensional subspaces L of the
Sobolev space H1
0(M,mM,f ).
2.3. Dirichlet isoperimetric constants. For a Borel subset Ω⊂M,
m+
M,f (Ω) := lim inf
r→0
mM,f (Ur(Ω))−mM,f (Ω)
r ,
where Ur(Ω) is the open r-neighborhood of Ω. The Dirichlet isoperi-
metric constant is deﬁned as
If(M) := inf
Ω
m+
M,f (Ω)
mM,f (Ω),
where the inﬁmum is taken over all Borel subsets Ω⊂ IntM (cf. Deﬁni-
tion 9.1 in [24]). The following inequality of Cheeger type is well-known
(see [5], and cf. Corollary 9.7 in [24]): If M is compact, then
(2.11) If(M)≤ 2
√
νf,1(M).
In the graph setting, Kwak, Lau, Lee, Oveis Gharan and Trevisan
[20] have established an improved Cheeger inequality in terms of the
smallest and higher eigenvalues of the Laplacian and the conductance
(see Theorem 1.1 in [20]). In the manifold setting, to answer a question
of Funano [10], Liu [29] has pointed out that a similar improved Cheeger
inequality holds for closed eigenvalues of the Laplacian and the Cheeger
constant via the same argument as in [20] (see Theorem 1.6 in [29]).
1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY 11
Now, we further point out that the following improvement of (2.11)
holds in our setting via the same argument as in [20]:
Theorem 2.1 ([20], [29]). LetM be compact. Then for all k≥ 1,
(2.12) If(M)≤ 8
√
2k νf,1(M)√
νf,k(M)
.
One can verify (2.12) by applying the same argument as in the proof
of Lemmas 3.2 and 3.3 in [29] (replace the role of the k-th closed eigen-
value with that ofνf,k(M)) to a non-negative eigenfunction ofνf,1(M),
here we recall that any eigenfunctions ofνf,1(M) are either always pos-
itive or always negative on IntM. Note that for such an eigenfunction,
the 2k disjointly supported Lipschitz functions constructed in the proof
of Lemma 3.3 in [29] also satisfy the Dirichlet boundary condition.
2.4. Dirichlet eigenvalue estimates. Wang [49] has produced a gra-
dient estimate of Bakry-Ledoux type for the Dirichlet heat semigroup
associated with the weighted Laplacian under a lower (unweighted)
Ricci curvature bound, a lower (unweighted) mean curvature bound
for the boundary, and a density bound (see Theorem 1.1 in [49], and
also [2]). From the same argument as in the proof of Theorem 1.1 in
[49], we can derive the following (cf. (1.10) in [49] for unweighted case):
Theorem 2.2 ([49]). If Ric∞
f,M≥ 0 and Hf,∂M≥ 0, then we have
‖‖∇Ptψ‖‖L∞≤
√
1 + 21/3 (1 + 42/3)
2√π
‖ψ‖L∞
√
t
for all t> 0 and non-negative, bounded measurable functions ψ on M,
wherePt is the Dirichlet heat semigroup generated by −∆f.
Wang [49] has proved Theorem 2.2 when f = 0. One can see Theo-
rem 2.2 only by using Lemma 3.4 in [43] (or Lemma 6.1 below) instead
of Lemma 2.3 in [49], and using the inequality (2.3) in [6] instead of
(2.5) in [49] along the line of the proof of Theorem 1.1 in [49].
In virtue of the gradient estimate, Wang [49] has obtained an isoperi-
metric inequality of Buser and Ledoux type based on the idea of Ledoux
[21] (see Theorem 1.2 in [49], and also [4], [21]). Theorem 2.2 together
with the same argument as in the proof of Theorem 1.2 in [49] yields:
Theorem 2.3 ([49]). LetM be compact. If Ric∞
f,M≥ 0 andHf,∂M≥ 0,
then we have
(2.13) If(M)≥ 2√π√
1 + 21/3 (1 + 42/3)
sup
t>0
1−e−t
√
t
√
νf,1(M).
Combining (2.12), (2.13) implies the following universal inequality:
12 YOHEI SAKURAI
Theorem 2.4. LetM be compact. If Ric∞
f,M≥ 0 and Hf,∂M≥ 0, then
there is a universal constant C >0 such that for all k≥ 1 we have
(2.14) νf,k(M)≤Ck 2νf,1(M).
Funano and Shioya [12], Funano [10], Liu [29] have formulated simi-
lar inequalities for closed manifolds of non-negative ∞-weighted Ricci
curvature (see Theorem 1.1 in [12], Theorem 1.2 in [10] and Theorem
1.1 in [29]). The inequality (2.14) corresponds to that of Liu [29].
Remark 2.3. Under similar setting Ric∞
f,∂M⊥≥ 0 andHf,∂M≥ 0 to that
in Theorem 2.4, the author [43] has shown a dimension free inequality
(2.15) νf,1(M)≥π2(2 InRadM)−2
of Li-Yau, Kasue type, and a rigidity result for the equality case (see
Corollary 7.6 in [43], and also [27], [17], and cf. Remarks 2.8 and 4.5).
Remark 2.4. Let M be compact, and let νk(M) be the k-th Dirichlet
eigenvalue of the Laplacian ∆. Let us mention a dimension dependent
estimate of the ratio νk(M)/ν1(M) induced from a classical method by
Cheng [7], Li-Yau [27]. We possess the following estimate by modifying
the proof of Corollary 2.2 in [7] (take a unit speed minimal geodesic
γ : [0, InRadM]→M withγ((0, InRadM])⊂ IntM that is orthogonal
to ∂M at γ(0), set k disjoint open balls in Int M centered at γ((2α−
1)(2k)−1 InRadM) with radius (2 k)−1 InRadM for α = 1,...,k , and
apply the argument of proof of Theorem 2.1 in [7]): If Ric M≥ 0, then
(2.16) νk(M)≤ 2n(n + 4)k2(InRadM)−2
for all k≥ 1. By (2.15), (2.16), we obtain the following: If Ric M≥ 0
and H∂M≥ 0, then there is Cn > 0 depending only on n such that
(2.17) νk(M)≤Cnk2ν1(M)
for all k≥ 1. Theorem 2.4 is a reﬁnement of (2.17) in the sense that
the upper bound of νk(M)/ν1(M) does not depend on n.
2.5. Comparisons. The author [43], [45] has obtained inscribed ra-
dius comparison theorems, and rigidity results for the equality case.
We ﬁrst recall the following comparison (see Theorem 1.1 in [43]):
Theorem 2.5 ([43]). ForN∈ [n,∞), we assume RicN
f,∂M⊥≥ (N−1)κ
and Hf,∂M≥ (N− 1)λ. If κ and λ satisfy the ball-condition, then
InRadM≤Cκ,λ.
Remark 2.5. Kasue [16] has proved Theorem 2.5, and rigidity result
for the equality case in the unweighted case where f = 0 and N = n.
Li and Wei have done in [26] when κ = 0, and in [25] when κ< 0.
1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY 13
We also have the following comparison (see Theorem 6.3 in [45]):
Theorem 2.6 ([45]). Assume Ric1
f,∂M⊥≥ (n− 1)κe
−4f
n−1 and Hf,∂M≥
(n− 1)λe
−2f
n−1 . Suppose additionally that f≤ (n− 1)δ for some δ∈ R.
If κ and λ satisfy the ball-condition, then we have
InRadM≤Cκe−4δ,λe−2δ.
Forκ,λ∈ R, let sκ,λ(t) be a unique solution of the Jacobi equation
ψ′′(t) + κψ (t) = 0 with ψ(0) = 1 , ψ′(0) = −λ. Notice that κ and
λ satisfy the ball-condition if and only if the equation sκ,λ(t) = 0
has a positive solution; moreover, Cκ,λ = inf{t > 0| sκ,λ(t) = 0 }.
We deﬁne ¯Cκ,λ as follows: If κ and λ satisfy the ball-condition, then
¯Cκ,λ := Cκ,λ; otherwise, ¯Cκ,λ :=∞. For N∈ (1,∞), let us deﬁne a
function sN,κ,λ : (0,∞]→ (0,∞] by
(2.18) ¯sκ,λ(t) :=
{
sκ,λ(t) if t< ¯Cκ,λ,
0 if t≥ ¯Cκ,λ, sN,κ,λ(r) :=
∫ r
0
¯sN−1
κ,λ (t)dt.
Remark 2.6. Forκ,λ∈ R, the value sn,κ,λ( ¯Cκ,λ) is ﬁnite if and only if
either (1)κ andλ satisfy the ball-condition; or (2)κ< 0 andλ =
√
|κ|
(cf. formulation of ﬁnite dimensional model spaces in Subsection 1.4).
Forr >0 and Ω⊂M, letBr(Ω) stand for the closedr-neighborhood
of Ω. We next recall the following relative volume comparison theorem
for metric neighborhoods of boundaries (see Theorem 5.4 in [43]):
Theorem 2.7 ([43]). Let∂M be compact. For N∈ [n,∞), we assume
RicN
f,∂M⊥≥ (N− 1)κ and Hf,∂M ≥ (N− 1)λ. Then for all r,R > 0
with r≤R we have
mM,f (BR(∂M ))
mM,f (Br(∂M ))≤ sN,κ,λ(R)
sN,κ,λ(r).
Remark 2.7. Under the same setting as in Theorem 2.7, Bayle [3] has
stated a similar absolute volume comparison of Heintze-Karcher type
(see Theorem E.2.2 in [3], and see also [15], [35], [36], [37]).
We further recall the following comparison (see Theorem 7.6 in [45]):
Theorem 2.8 ([45]). Let∂M be compact. Let us assume Ric1
f,∂M⊥≥
(n− 1)κe
−4f
n−1 and Hf,∂M ≥ (n− 1)λe
−2f
n−1 . Suppose additionally that
f≤ (n− 1)δ for some δ∈ R. Assume that one of the following holds:
(1) κ and λ satisfy the convex-ball-condition;
(2) κ≤ 0 and λ =
√
|κ|.
14 YOHEI SAKURAI
Then for all r,R> 0 with r≤R we have
mM,f (BR(∂M ))
mM,f (Br(∂M ))≤ sn,κe−4δ,λe−2δ(R)
sn,κe−4δ,λe−2δ(r).
Remark 2.8. In [43], the author has stated that the comparison in-
equalities in Theorems 2.5 and 2.7 hold under the curvature condition
RicN
f,M≥ (N− 1)κ and Hf,∂M ≥ (N− 1)λ. Actually, the author [43]
has proved such comparison inequalities under the curvature condition
RicN
f,∂M⊥≥ (N− 1)κ and Hf,∂M≥ (N− 1)λ relying on the Laplacian
comparison for the distance function ρ∂M . We can say the same thing
for the inequalities in Theorems 2.6 and 2.8 (see [45]).
