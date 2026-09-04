---
doc_id: arxiv-1712.04212v4
doc_title: "CONCENTRATION OF 1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY WITH DIRICHLET BOUNDARY CONDITION"
section_id: sec-002-3-invariants
section_title: "Invariants"
section_number: 3
pages: 14-19
source_pdf: 1712.04212v4.pdf
source_sha256: 521911fc8724f3c2
doc_brief: "CONCENTRATION OF 1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY WITH DIRICHLET BOUNDARY CONDITION — In this paper, we consider a concentration of measure problem on Riemannian manifolds with"
---
3.1. Isomophisms. We ﬁrst introduce the following notion:
Deﬁnition 3.1. Fori = 1, 2, letXi = (Xi,dXi,µXi) be metric measure
spaces with boundary. We say that X1 dominates X2 if there exists a
1-Lipschitz map Φ : X1→X2 such that
(3.1) Φ #µX1 =µX2, Φ(∂X1)⊂∂X2,
where Φ#µX1 denotes the push-forward of µX1 by Φ. We also say that
X1 and X2 are isomorphic to each other if they dominate each other.
Remark 3.1. A tripleX = (X,rX,σX ) is said to be an mm-space when
(X,rX ) is a complete separable metric space, and σX is a Borel proba-
bility measure onX . For i = 1, 2, letXi = (Xi,rXi,σXi) be mm-spaces.
They are said to be mm-isomorphic to each other if there exists an
isometry Φ : supp σX1 → suppσX2 such that Φ #σX1 = σX2, where
suppσXi are the support of σXi. It is said that X1 dominates X2 if
there exists a 1-Lipschitz map Ψ : X1→X 2 such that Ψ #σX1 = σX2.
It is well-known that ifX1 andX2 dominate each other, then they are
mm-isomorphic to each other (see e.g., Proposition 2.11 in [46]).
For i = 1, 2, let Xi = (Xi,dXi,µXi) be two metric measure spaces
with boundary. If X1 and X2 are isomorphic to each other in the
sense of Deﬁnition 3.1, then they dominate each other as mm-spaces;
in particular, they are mm-isomorphic to each other.
Let us show the following monotonicity of the partial inscribed radius
deﬁned as (1.2) (cf. Proposition 2.18 in [46]):
Lemma 3.1. For i = 1, 2, let Xi = (Xi,dXi,µXi) be metric measure
spaces with boundary. If X1 dominates X2, then for every η >0
PartInRad(X2; 1−η)≤ PartInRad(X1; 1−η).
1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY 15
Proof. By the assumption for the dominance, there exists a 1-Lipschitz
map Φ : X1→X2 such that (3.1). We ﬁx a Borel subset Ω ⊂X1 with
µX1(Ω)≥ 1−η. From Φ #µX1 =µX2 it follows that
(3.2) µX2
(
Φ(Ω)
)
=µX1
(
Φ−1(Φ(Ω))
)
≥µX1(Ω)≥ 1−η,
where Φ(Ω) denotes the closure of Φ(Ω).
We now show
(3.3) InRad Φ(Ω)≤ InRad Ω,
where InRad Φ(Ω) and InRad Ω are the inscribed radii of Φ(Ω) and Ω
deﬁned as (1.1), respectively. We ﬁx x2∈ Φ(Ω), and take a sequence
{x2,j} in Φ(Ω) with x2,j→x2. For each j we have x1,j∈ Ω satisfying
x2,j = Φ(x1,j). By using the properness of X1, we can choose z1,j∈
∂X1 with dX1(x1,j,z 1,j) = ρ∂X1(x1,j). We set z2,j := Φ(x2,j). From
Φ(∂X1)⊂∂X2 we deduce z2∈∂X2. Since Φ is 1-Lipschitz, we see
ρ∂X2(x2,j)≤dX2(x2,j,z 2,j)≤dX1(x1,j,z 1,j) =ρ∂X1(x1,j)≤ InRad Ω.
Letting j→∞ , we derive ρ∂X2(x2)≤ InRad Ω. This yields (3.3). In
virtue of (3.2) and (3.3), we obtain
PartInRad(X2; 1−η)≤ InRad Φ(Ω)≤ InRad Ω.
The arbitrariness of Ω completes the proof. 2
We also have the following monotonicity of the observable inscribed
radius introduced in Deﬁnition 1.1 (cf. Proposition 2.18 in [46]). The
proof is straightforward, and we omit it.
Lemma 3.2. For i = 1, 2, let Xi = (Xi,dXi,µXi) be metric measure
spaces with boundary. If X1 dominates X2, then for every η >0
ObsInRad(X2;−η)≤ ObsInRad(X1;−η).
According to Lemmas 3.1 and 3.2, they are invariants under the
isomorphism introduced in Deﬁnition 3.1.
3.2. Boundary separation distances. Let X = (X,dX,µX) be a
metric measure space with boundary, and let k≥ 1 be an integer. For
positive numbersη1,...,η k > 0, we denote bySX(η1,...,η k) the set of
all sequences {Ωα}k
α=1 of Borel subsets Ω α with µX(Ωα)≥ ηα. For a
sequence{Ωα}k
α=1∈S X(η1,...,η k), we set
DX
(
{Ωα}k
α=1
)
:= min
{
min
α⁄=β
dX(Ωα, Ωβ), min
α
dX(Ωα,∂X )
}
.
We now deﬁne the following quantity:
16 YOHEI SAKURAI
Deﬁnition 3.2. LetX = (X,dX,µX) be a metric measure space with
boundary. For η1,...,η k > 0, we deﬁne the (η1,...,η k)-boundary sep-
aration distance BSep(X;η1,...,η k) of X as follows: If SX(η1,...,η k)
is non-empty, then
BSep(X;η1,...,η k) := supDX
(
{Ωα}k
α=1
)
,
where the supremum is taken over all {Ωα}k
α=1∈S X(η1,...,η k); oth-
erwise, BSep(X;η1,...,η k) := 0.
The boundary separation distance BSep( X;η1,...,η k) is monotone
non-increasing in ηα for each α = 1,...,k .
Remark 3.2. The boundary separation distance is an analogue of the
separation distance on mm-spaces introduced by Gromov [13]. For later
convenience, we recall its precise deﬁnition: LetX = (X,rX,σX ) be an
mm-space (see Remark 3.1). For positive numbers η0,η 1,...,η k > 0,
the (η0,η 1,...,η k)-separation distance is deﬁned as
(3.4) Sep( X ;η0,η 1,...,η k) := sup min
α⁄=β
rX (Ωα, Ωβ),
where the supremum is taken over all sequences{Ωα}k
α=0 of Borel sub-
sets Ωα⊂X with σX (Ωα)≥ηα. If there exists no such sequence, then
we set Sep(X ;η0,η 1,...,η k) := 0.
We verify the following monotonicity (cf. Lemma 2.25 in [46]):
Lemma 3.3. For i = 1, 2, let Xi = (Xi,dXi,µXi) be metric measure
spaces with boundary. If X1 dominates X2, then for all η1,...,η k > 0
BSep(X2;η1,...,η k)≤ BSep(X1;η1,...,η k).
Proof. We may assumeSX2(η1,...,η k)⁄=∅. Fix a sequence{Ωα}k
α=1∈
SX2(η1,...,η k). There exists a 1-Lipschitz map Φ : X1→X2 such that
(3.1). Since Φ is 1-Lipschitz, for all α,β = 1,...,k , we see
(3.5) dX2(Ωα, Ωβ)≤dX1(Φ−1(Ωα), Φ−1(Ωβ)).
Furthermore, by Φ#µX1 =µX2, for every α = 1,...,k ,
(3.6) µX1(Φ−1(Ωα)) =µX2(Ωα)≥ηα.
We show that for every α = 1,...,k ,
(3.7) dX2(Ωα,∂X 2)≤dX1(Φ−1(Ωα),∂X 1).
Takex1∈ Φ−1(Ωα), and put x2 := Φ(x1)∈ Ωα. From the properness
ofX1, there exists z1∈∂X1 such thatdX1(x1,z 1) =dX1(x1,∂X 1). Put
z2 := Φ(z1)∈∂X2. It follows that
dX2(Ωα,∂X 2)≤dX2(x2,z 2)≤dX1(x1,z 1) =dX1(x1,∂X 1),
1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY 17
and we obtain (3.7). By combining (3.5), (3.6) and (3.7),
DX2
(
{Ωα}k
α=1
)
≤D X1
(
{Φ−1(Ωα)}k
α=1
)
≤ BSep(X1;η1,...,η k).
This completes the proof. 2
Lemma 3.3 tells us that the boundary separation distance is an in-
variant under the isomorphism introduced in Deﬁnition 3.1.
3.3. Relations between invariants. We present the following rela-
tion between our invariants (cf. Proposition 2.26 in [46]):
Lemma 3.4. Let X = (X,dX,µX) be a metric measure space with
boundary. Then for every η >0 we have
ObsInRad(X;−η)≤ BSep(X;η).
In particular, ObsInRad(X;−η)≤ InRadX.
Proof. We may assumeη <1. We ﬁx a 1-Lipschitz function ϕ :X→I
with ϕ|∂X = 0. Let mI,ϕ be the Borel probability measure on the ϕ-
screen Iϕ deﬁned as (1.3). By mI,ϕ = ϕ#µX and ϕ(∂X)⊂ ∂I, the
space X dominates Iϕ; in particular, Lemma 3.3 yields
(3.8) BSep( Iϕ;η)≤ BSep(X;η).
We put
t0 := inf{t∈I|mI,ϕ((t,∞))≤η}.
Note thatmI,ϕ((t0,∞))≤η andmI,ϕ([t0,∞))≥η. Since mI,ϕ([0,t 0])≥
1−η, we have
(3.9) PartInRad( Iϕ; 1−η)≤ InRad[0,t 0] =t0.
On the other hand, mI,ϕ([t0,∞))≥η leads to
(3.10) t0 =dI(∂I, [t0,∞))≤ BSep(Iϕ;η).
Now, (3.8) together with (3.9), (3.10) implies the desired one. 2
Remark 3.3. A sequence{Xn} of metric measure spaces with boundary
is said to be inscribed radius collapsing if InRadXn→ 0 as n→∞ .
Yamaguchi and Zhang [53] have studied inscribed radius collapsing
sequences of manifolds with boundary from the view point of the col-
lapsing theory. From Lemma 3.4, it follows that if a sequence of metric
measure spaces with boundary is inscribed radius collapsing, then it is
a boundary concentration family introduced in Deﬁnition 1.2.
We also possess the following relation (cf. Proposition 2.26 in [46]):
Lemma 3.5. Let X = (X,dX,µX) be a metric measure space with
boundary. Then for all η,η′ > 0 with η >η′ we have
BSep(X;η)≤ ObsInRad(X;−η′).
18 YOHEI SAKURAI
Proof. We may assume BSep(X;η) > 0. Fix a Borel subset Ω ⊂ X
with µX(Ω)≥η, and also ﬁx J⊂I with mI,ρ∂X (J)≥ 1−η′. Then
mI,ρ∂X (ρ∂X(Ω)) +mI,ρ∂X (J)≥µX(Ω) +mI,ρ∂X (J)≥η + (1−η′)> 1,
and henceρ∂X(Ω)∩J⁄=∅, whereρ∂X(Ω) denotes the closure ofρ∂X(Ω).
For everyt0∈ρ∂X(Ω)∩J we see
InRadJ≥dI(t0,∂I )≥dI(ρ∂X(Ω),∂I )
=dI(ρ∂X(Ω),∂I ) = inf
x∈Ω
ρ∂X(x) =dX(Ω,∂X ).
This yields
ObsInRad(X;−η′)≥ PartInRad(Iρ∂X ; 1−η′)≥ BSep(X;η).
We arrive at the desired assertion. 2
By combining Lemmas 3.4 and 3.5, and by straightforward argument,
one can conclude the following equivalence:
Proposition 3.6. Let{Xn} be a sequence of metric measure spaces
with boundaryXn = (Xn,dXn,µXn). Then the following are equivalent:
(1){Xn} is a boundary concentration family;
(2) for every sequence {Ωn} of Borel subsets Ωn⊂ Xn satisfying
lim infn→∞µXn(Ωn)> 0, we have limn→∞ dXn(Ωn,∂Xn) = 0;
(3) for every r >0 we have limn→∞ µXn(Br(∂Xn)) = 1.
Finally, we observe the following fact for the equality case of Lemma
3.5. The statement and its proof are informed by Daisuke Kazukawa.
Proposition 3.7. LetX = (X,dX,µX) be a metric measure space with
boundary. If suppµX =X, then for every η >0 we have
ObsInRad(X;−η) = BSep(X;η).
Proof. Lemma 3.4 tells us that the left hand side is at most the right
hand side. We verify the opposite. We may assume BSep( X;η) > 0.
Fix a suﬃciently small ϵ> 0. Then there exists a Borel subset Ω ⊂X
with µX(Ω)≥η such that dX(Ω,∂X )> BSep(X;η)−ϵ. Let us deﬁne
a 1-Lipschitz function ϕ :X→I by
ϕ(x) := max{dX(Ω,∂X )−dX(x, Ω), 0}.
Notice that ϕ|∂X = 0, ϕ|Ω =dX(Ω,∂X ) and
mI,ϕ({dX(Ω,∂X )})≥µX(Ω)≥η.
Furthermore, suppµX =X implies suppmI,ϕ = [0,dX(Ω,∂X )].
We now show
(3.11) PartInRad( Iϕ; 1−η)≥dX(Ω,X ).
1-LIPSCHITZ FUNCTIONS ON MANIFOLDS WITH BOUNDARY 19
The proof is by contradiction. Suppose that there exists a Borel subset
J⊂I with mI,ϕ(J)≥ 1−η such that InRadJ <dX(Ω,∂X ). We put
ˆJ := (InRadJ,dX(Ω,∂X )). Then we have
1 =mI,ϕ([0, InRadJ]) +mI,ϕ( ˆJ) +mI,ϕ({dX(Ω,∂X )})
≥mI,ϕ(J) +mI,ϕ( ˆJ) +η≥ 1 +mI,ϕ( ˆJ),
and hence mI,ϕ( ˆJ) = 0. This contradicts supp mI,ϕ = [0,dX(Ω,∂X )].
From (3.11) it follows that
BSep(X;η)−ϵ<d X(Ω,∂X )≤ ObsInRad(X;−η).
By letting ϵ→ 0, we complete the proof. 2
