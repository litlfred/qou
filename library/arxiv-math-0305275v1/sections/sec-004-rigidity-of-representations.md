---
doc_id: arxiv-math-0305275v1
doc_title: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds"
section_id: sec-004-rigidity-of-representations
section_title: "Rigidity of representations"
section_number: null
pages: 21-34
source_pdf: 0305275v1.pdf
source_sha256: 9b356a9d716a0d3e
doc_brief: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds — Let W be a compact manifold and let ρ be a representation of its fundamental group into PSL(2 , C)."
---
This section is completely devoted to proving the following:
Theorem 6.1 Let M be a non-compact, complete, orientable hyperbolic 3-
manifold of ﬁnite volume. Let Γ ∼= π1(M) be the sub-group of PSL(2, C)
such that M = H3/Γ . Let ρ : Γ → PSL(2, C) be a representation. If
|vol(ρ)| = vol(M) then ρ is discrete and faithful. More precisely there ex-
ists ϕ ∈ PSL(2, C) such that for any γ ∈ Γ
ρ(γ) = ϕ ◦γ ◦ϕ−1.
Remark 6.2 It is well-known that, in the hypotheses of Theorem 6.1, the
manifoldM is the interior of a compact manifold
M whose boundary consists
of tori. Thus M is a cusped manifold and, by Remark 2.10, all the deﬁnitions
and results we gave for ideally triangulated manifold apply.
As product structure on the cusps we ﬁx the horospherical one, having
the arc-length as cone parameter. For this section Dρ will denote a ﬁxed
pseudo-developing map for ρ.
Remark 6.3 By Proposition 4.18 we can suppose vol( ρ) ≥ 0.
Remark 6.4 A subgroup of PSL(2 , C) is said to be elementary if it has an
invariant set of at most two points in ∂H3. If the image of ρ is elementary,
then one can construct a pseudo-developing map as in Lemma 2.7 in su ch a
way that all the tetrahedra of any ideal triangulation of M collapse in the
straightening. Thus, by Theorem 4.10, vol( ρ) = 0.
This remark implies that, in the present case, since vol( ρ) = vol(M) ⁄= 0, the
image of ρ is non-elementary.
The idea for proving Theorem 6.1 is to rewrite the Gromov-Thurston -
Goldman-Dunﬁeld proof of Mostow’s rigidity, valid in the compact case .
We will follow the lead-line of [D], with the diﬀerence that we will use
classical chains instead of measure-chains. The technique for con structing
21
classical chains representing smear-cycles is that used in [BP] for the proof
of Mostow’s rigidity for compact manifolds. As an eﬀect of non-comp actness
we will work with inﬁnite chains. Therefore, we have to prove that so me
usual homological arguments actually work for our chains.
The core of the proof is to deduce from the equality vol( ρ) = vol(M) that
Dρ “does not shrink the volume.” This allows us to construct a measurab le
extension of Dρ to the whole H
3
, whose restriction to ∂H3 is almost every-
where a M¨ obius transformation. Such a M¨ obius transformation w ill be the
ϕ of Theorem 6.1.
The key fact is the following proposition, whose proof can be found
in [D] (claim 3 of Theorem 6.1).
Proposition 6.5 Let f : ∂H3 → ∂H3 be a measurable map that maps the
vertices of almost all regular ideal tetrahedra to vertices of regular ideal tetra-
hedra. Then f coincides almost everywhere with the trace of an isometry
ϕ.
We want to apply Proposition 6.5 to Dρ, and we do it in two steps. Let
M0 be M minus the cusps and let π : H3 →M be the universal cover.
Proposition 6.6 The map Dρ extends to
H
3
. More precisely, there exists a
measurable map Dρ :∂H3 →∂H3 such that for almost all x ∈∂H3, for any
geodesicγx ending at x, for any sequence tn → ∞ such that π(γx(tn)) ∈M0,
we have
lim
n→∞
Dρ(γx(tn)) = Dρ(x).
Proposition 6.7 The map Dρ satisﬁes the hypothesis of Proposition 6.5.
Before proving Propositions 6.6, and 6.7 we show how they imply Theo-
rem 6.1
Proof of 6.1. By Proposition 6.7, Proposition 6.5 applies. By Proposition 6.6
the equivariance of Dρ implies the equivariance of
Dρ, getting for any γ ∈ Γ
ρ(γ) = ϕ ◦γ ◦ϕ−1.
✷
Remark 6.8 Both Propositions 6.6, and 6.7 will follow from Lemma 6.22
and 6.23 below. We notice that Lemma 6.22 is a restatement of Lemmas 6.2
of [D]. While Proposition 6.7 corresponds to Claim 2 of [D]. Proposition 6.6
follows from Lemmas 6.22 and 6.23 exactly as in [D]. We will give a complete
proof of Proposition 6.7 because the proof of Claim 2 in [D] seems to be
incomplete.
22
From now until Lemma 6.11 we will describe how to construct a simplicial
version of the smearing process of measure-homology (see [Th1] or [Ra]).
Then we will prove Lemma 6.23. Finally we will complete the proof of
Theorem 6.1 by proving Propositions 6.6 and 6.7.
Let µ be the Haar measure on Isom( H3) such that for each x ∈ H3 and
A ⊂ H3 we have
µ{g ∈ Isom(H3) : g(x) ∈A} = vol(A)
where vol(A) is the hyperbolic volume of A.
In the following by a tetrahedron of
H
3
we mean an ordered 4-tuple of
points (the vertices). The volume of a tetrahedron is the hyperbo lic volume
with sign of the convex hull of its vertices.
Let S be the set of all genuine (non-ideal, non-degenerate) tetrahedr a:
S = {(y0,...,y 3) ∈ (H3)4 : vol( y0,...,y 3) ⁄= 0}.
For any Y ∈S let S(R) be the set of all isometric copies of Y :
S(Y ) = {X ∈S : ∃g ∈ Isom(H3), X =g(Y )}.
Then a natural bijection fY : Isom( H3) →S(Y ) is well-deﬁned by
fY (g) = g(Y ).
Thusµ induces a measure, which we still call µ, on S(Y ) deﬁned by
µ(A) = µ(f −1
Y (A)).
We consider the sets S±(Y ) = f −1
Y (Isom±(H3)) of tetrahedra respectively
positively and negatively isometric to Y . Note that S+(Y ) and S(Y )− are
both measurable.
Set S = Γ 4/Γ where Γ acts on Γ 4 by left multiplication. Each element
σ = [(γ0,...,γ 3)] ∈ S has a unique representative with γ0 = Id. When we
writeσ ∈ S we tacitly assume that the representative of the form ( γ0,...,γ 3)
with γ0 = Id has been chosen. So γ0 is always the identity.
For the rest of the section we ﬁx a fundamental polyhedron F ⊂ H3 for
M. For all ε> 0 let F ε be a locally ﬁnite ε-net in F . For any ξ ∈ F ε let
Fξ = {x ∈F : d(x,ξ ) = d(x, F ε)}.
EachFξ is a geodesic polyhedron of diameter less than ε. From the cone-
property of Dρ it follows that the diameters of Dρ(Fξ) are bounded by a
23
constant δ that depends on ε. Moreover, by removing some boundary face
from some Fξ, we get that F is the disjoint union of the Fξ’s. We deﬁne now
a family of special simplices. Let
N = {(γ0,...,γ 3,ξ 0,...,ξ 3) : ( γ0,...,γ 3) ∈ S, ξi ∈ F ε for all i}.
For each η ∈ N deﬁne ∆ η as the straight geodesic singular 3-simplex
whose vertices are the points ξ0,γ 1(ξ1),γ 2(ξ2),γ 3(ξ3), more precisely
∆ η : ∆ 3 ∋t ↦→π
( 3∑
i=0
tiγi(ξi)
)
.
For each tetrahedron X = ( x0,...,x 3) ∈ S(Y ) there exists a unique
η = (γ0,...,γ 3,ξ 0,...,ξ 3) ∈ N such that xi ∈ γi(Fξi) for i = 0,..., 3. This
deﬁnes a function
sY :S(Y ) → N.
Roughly speaking, N is a locally ﬁnite ε-net in the space of 3-simplices of M
and sY is the “closest point”-projection.
For any η ∈ N deﬁne
a±
Y (η) = µ{s−1
Y (η) ∩S±(Y )} =µ{X ∈S±(Y ) : xi ∈γi(Fξi)}
and
aY (η) = a+
Y (η) −a−
Y (η).
In the language of measures, one can think of a±
Y as the push-forward
of the measure µ under the map sY : S±(Y ) → N. This is the key for the
passage from measure-chains to classical ones.
The smearing of the tetrahedron Y is the cycle:
ZY =
∑
η∈N 
aY (η)∆ η.
We notice that, as N depends on the family F ε, the cycleZY actually depends
on ε.
Remark 6.9 The smearing of a tetrahedron in general is not a ﬁnite sum.
Nevertheless, as the following lemma shows, it has bounded l1-norm.
Lemma 6.10 For any Y ∈S, we have
∑
η
|aY (η)|< vol(M).
24
Proof. If Y = (y0,...y 3) then
∑
η
|aY (η)| ≤
∑
η
(
a+
Y (η) +a−
Y (η)
)
=
∑
η
µ{s−1
Y (η)} =µ
{ ⋃
η
s−1
Y (η)
}
=µ{s−1
Y (N) } =µ{f −1
Y s−1
Y (N) } =µ{g : g(y0) ∈F } = vol(F ) = vol(M).
✷
Lemma 6.11 The inﬁnite chain ZY is a cycle, i.e. ∂ZY = 0.
Proof. First note that the l1-norm of ∂ZY is bounded by 4 times the l1-norm
of ZY . Thus all the sums we will consider make sense.
Letυ be a simplex of ∂ZY . By construction υ is obtained as the projection
of an (n−1)-simplex having vertices inFξ0,γ 1(Fξ1),γ 2(Fξ2) for someγ1,γ 2 ∈ Γ
and ξ0,ξ 1,ξ 2 ∈ F ε. Let Aυ be the set of the elements of N of the form
η = (γ0,γ 1,γ 2,γ,ξ 0,ξ 1,ξ 2,ξ ) with γ ∈ Γ and ξ ∈ F ε. The simplices ∆ η ofZY
havingυ as the last face contribute to the coeﬃcient of υ in ∂ZY by
∑
η∈Aυ
aY (η) =
∑
η∈Aυ
µ(s−1
Y (η) ∩S+(Y )) −
∑
η∈Aυ
µ(s−1
Y (η) ∩S−(Y ))
=µ(s−1
Y (Aυ ) ∩S+(Y )) −µ(s−1
Y (Aυ ) ∩S−(Y )) = 0.
The same calculation, made with the simplices having υ as the ith face,
shows that the coeﬃcient of υ in ∂ZY is zero.
✷
For any ideal, non-ﬂat, tetrahedron Y = (y0,...,y 3) let t ↦→yi(t) be the
geodesic ray from the center of mass of Y to yi, i = 0,..., 3. For any R> 0
let YR be the following element of S:
YR = (y0(R),...,y 3(R)).
Remark 6.12 From now on we ﬁx a positively oriented regular ideal tetra-
hedron Y , and we write S±(R), fR, sR, aR(η) and ZR for S±(YR), fYR, sYR,
aYR(η) and ZYR.
We say that a 3-simplex ∆ is ε-close to a tetrahedron X if the vertices of
∆ are ε-close to X. We deﬁne
ǫ(R,ε ) = sup {v3 − vol(∆) : ∆ is ε-close to an element of S(R)}
Lemma 6.13 For any ﬁxed ε, for large R the function ǫ(R,ε ) goes to zero
exponentially in R.
25
This is because v3 − vol(YR) goes to zero like e−R and the volume of any ∆
which is ε-close to YR is close to the volume of YR. See [BP], [D], [Th1] for
details.
Remark 6.14 What we actually need to prove our claims is a restatement
for ZR of the Step 2 of Theorem 5.1. From now until Proposition 6.20, we
prove facts that are standard for ﬁnite chains, but need a proof for ZR.
For η ∈ N, we set vη = vol(∆ η). Using the fact that all the Fξ’s have
diameter less than ε, one can prove the following lemma (see [BP] for details).
Recall that N depends on F ε and so it depends on ε.
Lemma 6.15 For anyε> 0, for large enough R we have that for any η ∈ N
• a+
R(η) ·a−
R(η) = 0 .
• aR(η) ⁄= 0 = ⇒ aR(η) ·vη ≥ 0.
Lemma 6.16 There exists a constant c such that |D∗
ρω|< c|ω|, where ω is
the volume-form of H3.
Proof. Let M0 be M minus the cusps. The function |D∗
ρω|/|ω| is continuous
and hence bounded on M0. In the cusps, by direct calculation and using the
cone property of Dρ, one can show that the same bound holds.
✷
Lemma 6.17 The integrals ⟨ω,Z R⟩ and ⟨D∗
ρω,Z R⟩ are well-deﬁned.
Proof. As ∑ |aR(η)| < +∞, since |⟨ω, ∆ η⟩| is bounded by v3, then ⟨ω,Z R⟩
is well-deﬁned. Consider now D∗
ρω. From Lemma 6.16 it follows that the
integral of |D∗
ρ| over straight geodesic simplices is bounded by cv3. Hence
also ⟨D∗
ρω,Z R⟩ is well-deﬁned.
✷
As above, let M0 denote M minus the cusps and, for k ∈ N∗ let
Mk =
⋃
T ⊂∂M 0
T × [k − 1,k ).
Let F ε
k = F ε ∩π−1(Mk) and Nk = {η ∈ N : ξ0 ∈ F ε
k}. We have
ZR =
∑
k∈N
∑
η∈N k
aR(η)∆ η.
26
Lemma 6.18 For any k the chain ∑
η∈N k
aR(η)∆ η is a ﬁnite sum.
Proof. If aR(η) ⁄= 0 and η ∈ Nk then ∆ η is ε-close to an element X ∈S(R)
having ﬁrst vertex in Fξ0 with ξ0 ∈ F ε
k . Since F ε is locally ﬁnite and M k
is compact, F ε
k is ﬁnite, so there is only a ﬁnite number of possibilities for
ξ0. Since F ξ0 is compact, any X ∈ S(R) with ﬁrst vertex in Fξ0 lies on a
compact ball B of H3. Since F is a fundamental domain, then there exists
only a ﬁnite number of elements γ ∈ Γ so that γ(F ) intersects B. Then for
anyξ0 there is only a ﬁnite number of possibilities for ξ1, ξ2 andξ3. It follows
that there exists only a ﬁnite number of η ∈ Nk such that aR(η) ⁄= 0.
✷
Lemma 6.19 For any R, if k is large enough, then for any η ∈ Nk with
aR(η) ⁄= 0, the simplex ∆ η is completely contained in a cusp of M.
Proof. If X = (x0,...,x 3) ∈ S(R) then X lies in the ball B(x0, 2R). Since
M has a ﬁnite number of cusps, for any R there exists m ∈ N such that for
k ≥m ifx0 ∈Mk then the whole ball B(x0, 2R +ε) is contained in the cusp
containing x0. If η ∈ Nk and aR(η) ⁄= 0, then there exists X ∈ S(R) with
x0 ∈ π−1(Mk) ∩F hence ∆ η is ε-close to X. Thus ∆ η ⊂ B(x0, 2R +ε) is
contained in the cusp that contains x0.
✷
Now for k ∈ N deﬁne
ZR,k =
∑
j<k
∑
η∈N j
aR(η)∆ η.
ZR,k is a ﬁnite chain by Lemma 6.18. Moreover, since ∂ZR = 0, then
each simplex υ of ∂ZR,k appears as a face of a simplex ∆ η with aR(η) ⁄= 0
and η ∈ Nj for some j ≥ k. Therefore, by Lemma 6.19, for k large enough
each simplex υ of ∂ZR,k is contained in a cusp of M. Thus to each υ there
corresponds an ideal point of ˆM . For each υ ∈ ∂ZR,k let λR,k (υ) be the
coeﬃcient of υ in ∂ZR,k and let Cυ be the cone from υ to the corresponding
ideal point.
Let ˆZR,k be the chain obtained by adding to ZR,k the cones Cυ :
ˆZR,k =ZR,k +
∑
υ ∈∂Z R,k
λR,k (υ)Cυ.
The chain ˆZR,k is a ﬁnite sum and it is easily checked that it is a cycle.
For any 3-simplex ∆ let Strvol(∆) denote the volume of the convex h ull
of the vertices of Dρ(∆). For any η ∈ N set wη = Strvol(∆ η).
27
Proposition 6.20 For any R> 0 We have:
∑
η
aR(η)vη = ⟨ω,Z R⟩ = ⟨D∗
ρω,Z R⟩ =
∑
η
aR(η)wη.
Proof. The ﬁrst equality is tautological. We use now the cycles ˆZR,k to
approximate ZR. Since vol( ρ) = vol( M), then [ ω] = [ D∗
ρω] as elements of
H 3( ˆM ). Thus for any k ∈ N we have ⟨ω, ˆZR,k ⟩ = ⟨D∗
ρω, ˆZR,k ⟩. As in Step 2
of Theorem 5.1, we can straighten the ﬁnite cycle ˆZR,k , getting:
⟨ω, ˆZR,k ⟩ = ⟨D∗
ρω, ˆZR,k ⟩ =
∑
j<k
∑
η∈N k
aR(η)wη +
∑
υ ∈∂Z R,k
λR,k (υ)Strvol(Cυ ).
For each simplex α of ˆZR,k we have |vol(α)| ≤ v3, |Strvol(α)| ≤ v3 and,
by Lemma 6.16, |⟨D∗
ρω,α ⟩| ≤ cv3. It follows that to get the remaining
inequalities it suﬃces to show that
lim
k→∞
∑
υ ∈∂Z R,k
|λR,k (υ)| = 0.
Since ∂ZR = 0, if υ ∈ ∂ZR,k then υ ∈ ∂∆ η with aR(η) ⁄= 0 and η ∈ Nj
for some j ≥k. So we have
∑
υ ∈∂Z R,k
|λR,k (υ)| ≤ 4
∑
j≥k
∑
η∈N j
a+
R(η) +a−
R(η) = 4
∑
j≥k
∑
η∈N j
µ{s−1
R (η)}
= 4
∑
j≥k
µ{s−1
R (Nj)} = 4
∑
j≥k
µ{Y ∈S(R) : ∃ξ ∈ F ε
j, y0 ∈Fξ}
= 4
∑
j≥k
∑
ξ∈F ε
j
vol(Fξ) ≤ 4vol(
⋃
j≥k−ε
Mj)
The last term goes to zero as k → ∞ because M has ﬁnite volume and the
desired equality follows.
✷
Now that we have Proposition 6.20, forget about the cycles ˆZR,k .
From triangular inequality, Proposition 6.20 and Lemma 6.15 we have
∑
η
|aR(η)| · |wη| ≥
⏐
⏐
⏐
∑
η
aR(η)wη
⏐
⏐
⏐ =
⏐
⏐
⏐
∑
η
aR(η)vη
⏐
⏐
⏐
=
∑
η
|aR(η)| · |vη| ≥
∑
η
|aR(η)|(v3 −ǫ(R,ε ))
from which and Lemma 6.10 we get:
28
Proposition 6.21 ForR large enough we have
∑
η∈N 
|aR(η)|(v3 − |wη|) ≤
∑
η∈N 
|aR(η)|ǫ(R,ε ) ≤ vol(M)ǫ(R,ε ).
For anyR> 0 let AR ⊂ N be the set of tetrahedra with “small” straight
volume:
AR = {η ∈ N : v3 − |wη|>R 2 · vol(M) ·ǫ(R,ε )}.
Lemma 6.22 ForR large enough we have
∑
η∈AR
|aR(η)| ≤ 1
R2.
Proof. From Proposition 6.21 we get
R2vol(M)ǫ(R,ε ) ·
∑
η∈AR
|aR(η)| ≤
∑
η∈AR
|aR(η)|(v3 − |wη|)
≤
∑
η∈N 
|aR(η)|(v3 − |wη|) ≤ vol(M)ǫ(R,ε )
The claimed inequality follows.
✷
Lemma 6.23 For almost all isometries g we have
lim
n→∞
Strvol(g(Yn)) = v3.
Proof. Since a+
R ·a−
R = 0, then ∑
η∈AR
|aR(η)| = µ(s−1
R (AR)). Thus for any
ﬁxed R> 0 we have
µ
( ⋃
N∋n>R
s−1
R (An)
)
≤
∑
n>R
1
n2 < 1
R.
Recalling that for any set A ⊂ N we have µ(s−1
R (A)) = µ(f −1
R s−1
R (A)), we
get
µ{g ∈ Isom(H3) : ∃n>R, w sn(g(Yn)) <v 3 −n2 · vol(M) ·ǫ(n,ε )}< 1
R.
From Lemma 6.13 it follows that lim n→∞n2ǫ(n,ε ) = 0. As R → ∞, this
implies that for any ε> 0, for almost any isometry g we have
lim
n→∞
wsn(g(Yn)) =v3.
29
Letg be one of such maps. Since the diameters of the Dρ(Fξ) are bounded
byδ, then Dρ(∆ sR(g(YR))) is δ-close to Dρ(g(YR)). Recalling that wsR(g(YR)) =
Strvol(∆ sR(g(YR))), we have that
lim
n→∞
Strvol(∆ sn(g(Yn))) = v3
and, since Dρ(g(YR)) is δ-close to Dρ(∆ sR(g(YR))), then also
lim
n→∞
Strvol(g(Yn)) = v3.
✷
We sketch here the proof of Proposition 6.6, referring to [D] for de tails.
Proof of Proposition 6.6. In the disc model let γ be a geodesic from 0 to
a point in ∂H3. Let XR be a family of regular tetrahedra of edge R with
ﬁrst vertex in 0 and second in γ(R). All the claims from Lemma 6.10 to
Lemma 6.23 hold for {XR}. It follows that for almost all isometries g we
have
lim
n→∞
Strvol(g(Xn)) = v3.
Then Dρ(g(γ(n))) must reach the boundary of H3. Using again the above
property of the limit, one can estimate the angle α(n) between the geodesic
fromDρ(g(0)) toDρ(g(γ(n))) and the geodesic from Dρ(g(0)) andDρ(g(γ(n+
1))). Such estimate shows that ∑ α(n)< ∞, which implies that Dρ(g(γ(n)))
converges. The claim follows because Dρ is locally Lipschitz outside the
cusps. Measurability follows because the extension can be viewed as a point-
wise limit of measurable functions.
✷
Remark 6.24 In general Dρ is not uniformly continuous in the cusps. So it
cannot be locally Lipschitz on the whole H3.
We come now to the proof of Proposition 6.7.
Lemma 6.25 Let X = (x0,x 1,x 2,x 3) be an ideal tetrahedron in H
3
. Sup-
pose that no three vertices of X coincide. Then for any ε > 0 there exist
neighborhoodsUi of xi in H
3
such that for any tetrahedron Y = (y0,...,y 3)
with yi ∈Ui we have |vol(Y ) − vol(X)|<ε .
This follows from the formula of the volume for ideal tetrahedra, se e [BP]
for details.
30
Remark 6.26 Lemma 6.25 does not hold if three vertices of X coincide.
To see this, let Y be a regular ideal tetrahedron and let γ be a parabolic
or hyperbolic isometry. Then γn(Y ) is a family of tetrahedra with maximal
volume, but at least three of the vertices of γn(Y ) converge to the same point.
Lemma 6.27 For almost all regular ideal tetrahedra Y , the ideal tetrahe-
dron Dρ(Y ) is deﬁned. Moreover, for almost all Y either Dρ(Y ) is regular
(whence vol(Dρ(Y )) = v3) or at least three of its vertices coincide (whence
vol(Dρ(Y )) = 0 ).
Proof. Without loss of generality, we can restrict the ﬁrst claim to the spac e
of positive regular ideal tetrahedra. We parametrize such a space with
{(a,b,c ) ∈S2
∞ ×S2
∞ ×S2
∞ : a ⁄=b ⁄=c}
where S2
∞ = ∂H3, by mapping ( a,b,c ) to the unique positive regular ideal
tetrahedron with ( a,b,c ) as the ﬁrst three vertices. We denote by Q(a,b,c )
the fourth vertex of such tetrahedron. Since Dρ is deﬁned almost everywhere,
the ﬁrst claim follows from Fubini’s theorem. The second claim follows fr om
Lemmas 6.23 and 6.25.
✷
With the above notation, by Lemma 6.27 we can restate Proposition 6 .7
as follows.
Proposition 6.28 The set {Y ∈ S2
∞ ×S2
∞ ×S2
∞ : vol(
Dρ(Y )) = 0 } has
zero measure.
The proof of this result will follow from the next:
Lemma 6.29 If the set
{Y ∈S2
∞ ×S2
∞ ×S2
∞ : vol(
Dρ(Y )) = 0 }
has positive measure, then the map Dρ is constant almost everywhere.
Before proving Lemma 6.29 we show how it implies Proposition 6.28.
Proof of 6.28. By contradiction, we apply Lemma 6.29 deducing that Dρ is
a.e. a constant p. From the equivariance of Dρ it follows that for any γ ∈ Γ
and x ∈∂H3 we have
p =Dργ(x) = ρ(γ)(Dρ(x)) = ρ(γ)(p).
31
Thus p is a ﬁxed point of any element of Γ. This implies that the image of
ρ is elementary, but this cannot happen because of Remark 6.4.
✷
We now prove Lemma 6.29.
Lemma 6.30 In the hypothesis of Lemma 6.29 there exists a positive-mea-
sure set A ⊂S2
∞ such that Dρ is constant on A.
Proof. By Lemma 6.27 it is not restrictive to suppose that the set
{(a,b,c ) ∈S2
∞ ×S2
∞ ×S2
∞ : Dρ(a) = Dρ(b) = Dρ(c)}
has positive measure. Then by Fubini’s theorem there exists a positiv e-
measure set A0 ⊂S2
∞ such that for all a0 ∈A0 the set
{(b,c ) ∈S2
∞ ×S2
∞ : Dρ(a0) = Dρ(b) = Dρ(c)}
has positive measure in S2
∞ ×S2
∞. Again by Fubini’s theorem for all a0 ∈A0
there exists a positive-measure set A1 ∈ S2
∞ such that for any a1 ∈ A1 the
set
{c ∈S2
∞ :Dρ(a0) = Dρ(a1) = Dρ(c)}
has positive measure. In particular Dρ is constant on A1.
✷
We set p =Dρ(A1) and A =D
−1
ρ (p).
Remark 6.31 In the sequel we use the symbol ~
∀ to mean “for almost all.”
By Lemma 6.27 the set A has the following property
~
∀(a0,a 1,x ) ∈A ×A ×Ac, Q (a0,a 2,x ) ∈A.
We work now in the half space model C × R+ of H3. So S2
∞ = C ∪ {∞}.
In that model
Q(∞,a,z ) = α(z −a) +a
where α = (1 + i
√
3)/2. Again by Fubini’s theorem ~
∀a0 ∈ A, ~
∀(a1,x ) ∈
A ×Ac, we have Q(a0,a 1,x ) ∈ A and we can suppose that this holds for
a0 = ∞.
In other words, for almost all ( a,x ) ∈ A ×Ac the third vertex of the
equilateral triangle with the ﬁrst two vertices in a and x is in A. For any
32
a,x ∈ C we call Ex(a) the set of the vertices of the regular hexagon centered
at x and with a vertex in a. Then we have
~
∀(a,x ) ∈A ×Ac, Ex(a) ⊂A (1)
and in particular ~
∀(a,x ) ∈A×Ac, 2x−a ∈A. Note thatx is the middle-point
of the segment between a and 2x −a.
Lemma 6.32 For any open set B ⊂ C we have µ(A ∩B)> 0.
Proof. Suppose the contrary. Then there exists an open set B such that
µ(A ∩B) = 0. That is, almost all the points of B are in Ac. Moreover,
from (1) and Fubini’s theorem it follows that ~
∀x ∈ Ac, ~
∀a ∈ A,E x(a) ∈ A.
Therefore there exists a point x0 ∈B such that a small ball B0 =B(x0,r 0)
is contained in B and
~
∀a ∈A, Ex0(a) ∈A. (2)
Since µ(A) > 0 then there exists a small ball B1 = B(x1,r 1) such that
µ(A ∩B1) > 0. Let x2 = (x1 +x0)/2. If there exists r > 0 such that
µ(A ∩B(x2,r )) = 0, then applying the same argument we can ﬁnd a point
y arbitrarily close to x2 such that (2) holds for y. In particular we get that
almost all the points of the set C = {2y −a : a ∈B1 ∩A} are in A. But if
y is close enough to x2 thenC ∩B0 has positive measure, contradicting that
µ(A ∩B) = 0.
It follows that for all r2 > 0 we have µ(A ∩B(x2,r 2))> 0, in particular
we choose r2 < r0/2. By iterating this construction, we ﬁnd a sequence of
points xn →x0 and radii r0/2>r n > 0 such that µ(A ∩B(xn,r n))> 0. For
n large enough this contradicts the fact that µ(A ∩B) = 0.
✷
Lemma 6.33 For all z ∈ C we have
∀r >0 µ(B(z,r ) ∩A) ≥ 1
2µ(B(z,r )). (3)
Proof. From Fubini’s theorem, and condition (1), it follows that for almost
all a ∈A we have
~
∀x ∈Ac, Ex(a) ⊂A. (4)
Note that if (4) holds for a, then (3) holds for a.
Let z ∈ C. From Lemma 6.32 it follows that there exists a sequence
xn → z such that (4) (and hence (3)) holds for xn. As the function x ↦→
µ(A ∩B(x,r )) is continuous, then the claim holds for z.
✷
33
Lemma 6.34 Let X ⊂ R2 be a measurable set. If there exists α >0 such
that for any ball B
µ(B ∩X) ≥αµ(B)
then µ(R2 \X) = 0 .
This is a standard fact of integration theory and it follows from Lebe sgue’s
diﬀerentiation theorem (see for example [Ru]).
From this lemma and Lemma 6.33 it follows that the set A has full
measure. Since A = D
−1
ρ (p) then Dρ is constant almost everywhere and
Lemma 6.29 is proved.
✷
This completes the proof of Theorem 6.1.
