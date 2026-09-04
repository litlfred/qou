---
doc_id: arxiv-1712.04212v4
doc_title: "CONCENTRATION OF 1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY WITH DIRICHLET BOUNDARY CONDITION"
section_id: sec-003-4-dirichlet-eigenvalues
section_title: "Dirichlet eigenvalues"
section_number: 4
pages: 19-22
source_pdf: 1712.04212v4.pdf
source_sha256: 521911fc8724f3c2
doc_brief: "CONCENTRATION OF 1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY WITH DIRICHLET BOUNDARY CONDITION — In this paper, we consider a concentration of measure problem on Riemannian manifolds with"
---
In what follows, let (M,dM,mM,f ) denote ann-dimensional weighted
Riemannian manifold with boundary deﬁned as (1.4) such thatmM,f is
a Borel probability measure. We study the metric measure space with
boundary (M,f ) deﬁned as (1.7).
4.1. Boundary separation distances and Dirichlet eigenvalues.
Let us show the following relation between the boundary separation
distance and the Dirichlet eigenvalue:
Lemma 4.1. LetM be compact. Then for all η1,...,η k > 0 we have
BSep ((M,f );η1,...,η k)≤ 2√
νf,k(M) minα=1,...,kηα
,
whereνf,k(M) is the k-th Dirichlet eigenvalue of ∆f deﬁned as (1.6).
Proof. We set S := BSep((M,f );η1,...,η k). We may assume S > 0.
Let us ﬁx a suﬃciently smallϵ> 0. There exists a sequence{Ωα}k
α=1∈
S(M,f )(η1,...,η k) such thatS−ϵ< D(M,f )
(
{Ωα}k
α=1
)
. Put Sϵ :=S−ϵ.
For eachα, we deﬁne a Lipschitz function φα :M→ R by
φα(x) := max
{
1− 2
Sϵ
dM(x, Ωα), 0
}
.
Notice that the support of φα coincides with BSϵ/2(Ωα). Furthermore,
the following properties hold:
(1) φα≡ 0 on BSϵ/2(∂M );
(2) φα≡ 0 on BSϵ/2(Ωβ) for every β = 1,...,k with β⁄=α;
(3) φα≡ 1 on Ωα;
(4)‖∇φα‖≤ 2/Sϵ mM,f -almost everywhere on M.
20 YOHEI SAKURAI
By (1),φα belongs to the Sobolev spaceH1
0(M,mM,f ). By (2), the func-
tions φ1,...,φ k are orthogonal to each other in H1
0(M,mM,f ). Let L0
be the k-dimensional subspace of H1
0(M,mM,f ) spanned by φ1,...,φ k.
From (3) and (4), for every φ∈L0\{ 0} we deduce
∫
M
φ2dmM,f =
k∑
α=1
c2
α
∫
M
φ2
αdmM,f≥
k∑
α=1
c2
αηα≥ min
α
ηα
k∑
α=1
c2
α,
∫
M
‖∇φ‖2dmM,f =
k∑
α=1
c2
α
∫
M
‖∇φα‖2dmM,f≤
( 2
Sϵ
)2 k∑
α=1
c2
α,
where c1,...,c k are determined by φ =∑k
α=1 cαφα. Hence we have
Rf(φ) =
∫
M‖∇φ‖2dmM,f∫
M φ2dmM,f
≤ 1
minαηα
( 2
Sϵ
)2
,
where Rf(φ) is the Rayleigh quotient of φ deﬁned as (2.9). From the
min-max principle (2.10) we derive
νf,k(M)≤ sup
φ∈L0\{0}
Rf(φ)≤ 1
minαηα
( 2
Sϵ
)2
.
Letting ϵ→ 0, we conclude the inequality. 2
Remark 4.1. In the forthcoming paper [11], Funano and the author
prove the following reﬁned estimate for k = 1 (see Theorem 2.3 in
[11]): For every η >0 we have
BSep ((M,f );η)≤ 1√
νf,1(M)
loge
η.
Remark 4.2. Colbois and Savo [9] have shown a similar estimate for
the k-th closed eigenvalue of the Laplacian (see Lemma 5 in [9]).
Remark 4.3. Chung, Grigor’yan and Yau [8] have estimated the k-th
closed eigenvalue and Robin eigenvalue of the Laplacian in terms of
the separation distance (see Theorem 1.1 in [8]). By applying the same
argument in [8] to our setting, we see the following estimate forνf,k(M):
Suppose thatM is compact. Then for every integerk >2, and for every
sequence{Ωα}k
α=1 of Borel subsets with minα⁄=βdM(Ωα, Ωβ)≥D,
νf,k(M)−νf,1(M)≤ 1
D2 max
α⁄=β
(
log 4∫
Ωα
φ2
f,1dmM,f
∫
Ωβ
φ2
f,1dmM,f
)2
,
where φf,1 is an L2-normalized eigenfunction for νf,1(M).
1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY 21
4.2. Observable inscribed radii and Dirichlet eigenvalues.Now,
Lemma 4.1 together with Lemma 3.4 leads us to the following relation
between the observable inscribed radius and the Dirichlet eigenvalue:
Proposition 4.2. LetM be compact. Then for every η >0,
ObsInRad((M,f );−η)≤ 2√
νf,1(M)η
.
Remark 4.4. Under the curvature condition (2.1) and InRad M≤ D,
the author [43] has provided a lower bound of νf,1(M) depending only
on κ, λ, Nand D (see Theorem 1.6 in [43] and Remark 2.8, and also
pioneering works of Li-Yau [27] and Kasue [17]). Combining Proposi-
tion 4.2 with the lower estimate tells us that we have an upper bound
of ObsInRad((M,f );−η) depending only on κ, λ, N, Dand η.
Similarly, under the condition (2.3) forκ andλ satisfying the convex-
ball-condition, and under f≤ (n− 1)δ, the author [45] has obtained a
lower bound of νf,1(M) depending only on n, κ, λandδ (see Theorem
8.5 in [45]). In virtue of Proposition 4.2, we possess an upper bound of
ObsInRad((M,f );−η) depending only on n, κ, λ, δand η.
Proposition 4.2 enables us to prove Theorem 1.1.
Proof of Theorem 1.1. Let{(Mn,fn)} be a sequence of compact metric
measure spaces with boundary deﬁned as (1 .7). By Proposition 4.2, if
νfn,1(Mn)→∞ asn→∞ , then ObsInRad((Mn,fn);−η)→ 0. Hence,
{(Mn,fn)} is a boundary concentration family. 2
We also derive the following from Proposition 4.2 and Theorem 2.4:
Theorem 4.3. LetM be compact. If Ric∞
f,M≥ 0 and Hf,∂M≥ 0, then
there is a universal constant C >0 such that for all k≥ 1 and η >0,
ObsInRad((M,f );−η)≤ Ck√
νf,k(M)η
.
Let us give a proof of Theorem 1.2 by using Theorem 4.3.
Proof of Theorem 1.2. Let{(Mn,fn)} denote a sequence of compact
metric measure spaces with boundary deﬁned as (1 .7). Assume that
Ric∞
fn,Mn≥ 0 and Hfn,∂Mn≥ 0. Due to Theorem 4.3, if νfn,k(Mn)→∞
for k, then ObsInRad((Mn,fn);−η)→ 0. We complete the proof. 2
Remark 4.5. The author wonders whether the following statement of E.
Milman type holds (see [33], [34], and Theorem 9.46 in [46]): Under the
same setting as in Theorems 1.1, 1.2, if Ric∞
fn,Mn≥ 0 and Hfn,∂Mn≥ 0,
and if{(Mn,fn)} is a boundary concentration family, thenνfn,1(Mn)→
22 YOHEI SAKURAI
∞. If it is true, then in virtue of Theorems 1.1, 1.2, we can say that
under Ric∞
fn,Mn≥ 0 and Hfn,∂Mn≥ 0, the following are equivalent:
(1){(Mn,fn)} is a boundary concentration family;
(2) νfn,1(Mn)→∞ as n→∞ ;
(3) νfn,k(Mn)→∞ as n→∞ for some k≥ 1.
The author also wonders if one can extend the above equivalence to
a weaker setting Ric N
fn,Mn≥ 0 and Hfn,∂Mn≥ 0 for N∈ (−∞, 1] (see
Remark 2.1). Under Ric N
f,∂M⊥≥ 0 and Hf,∂M ≥ 0 for N∈ (−∞, 1],
the author [44] has proved a dimension free inequality
νf,1(M)≥π2(2 InRadM)−2,
of Li-Yau, Kasue type, and a rigidity result for the equality case (see
Corollary 6.5 in [44], and also [27], [17], and cf. Remarks 2.3 and 2.8).
