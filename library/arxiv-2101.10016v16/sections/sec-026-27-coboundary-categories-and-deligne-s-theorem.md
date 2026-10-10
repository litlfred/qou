---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-026-27-coboundary-categories-and-deligne-s-theorem
section_title: "Coboundary categories and Deligne’s theorem"
section_number: 27
pages: 166-173
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
doc_brief: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem — We construct, for every complex simple Lie algebra g and every positive integer level k, a unitary modular"
---
27. Coboundary categories and Deligne’s theorem
By an interesting result of Deligne, the study of dimension in a braided tensor category
can be addressed in two equivalent ways: via right duality with extra (pivotal/spherical)
structure or else via extra structure on the braided symmetry (balancing/ribbon structure).
In this section we introduce a notion of symmetry that is more general than that of
braided symmetry, and we call generalised coboundary. It is a generalisation of both the
notion of braided symmetry and that of a coboundary due to Drinfeld that allows to study
these symmetries in a unified way.
The generalisation is motivated by the fact that some of the structures that we study in
this paper do not need the full notion of a braided symmetry, but only the more general
class of symmetries, which have the advantage of stability under certain twist deformation.
A important source of coboundaries indeed arises from deformation of braided symmetries with ribbon structure and plays a central role in the unitary structure of the weak
quasi-Hopf algebras arising from quantum groups at roots of unity studied in Sects. 28, 32.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 167
We study pivotal or spherical structures in tensor categories with a generalised coboundary, and we extend Deligne result to this case. We start reviewing the notion of pivotal
and spherical category.
If ρ
∨
is a two-sided dual of ρ and if (bρ, dρ) and (b
′
ρ
, d′
ρ
) respectively solve the right
and the left duality equations for this pair, then we can associate two functionals on the
morphism space (ρ, ρ), called left and right quantum traces, via
TrL
ρ
(T) = dρ ◦ 1ρ∨ ⊗ T ◦ b
′
ρ
(27.1)
TrR
ρ
(T) = d
′
ρ
◦ T ⊗ 1ρ∨ ◦ bρ. (27.2)
If these solutions correspond to pivotal (or spherical) structures a well behaved theory of
dimension can be developed. We briefly recall the main aspects, dropping, for simplicity,
the associativity morphisms in most of our formulae in this section.
Let (ρ
∨
, bρ, dρ) be a right duality, see Sect. 5, and D : C → C the associated functor as
in (5.6). Note that D2: C → C is a covariant tensor functor. We assume from now on that
our category has two-sided duals, so there is a natural isomorphism u from the identity
functor 1, to D2, which, however, need not be monoidal. An example of this occurrence
arises in the framework of representations of semisimple weak quasi-Hopf algebras. The
category has two-sided duals if the square of the antipode S is an inner automorphism. The
natural isomorphism is monoidal if the implementing element can be chosen group-like,
but this is not always the case. On the other hand, any natural isomorphism u ∈ (1, D2)
in a category with two-sided duals defines a left duality structure coinciding with the right
one on the objects via
b
′
ρ = 1ρ∨ ⊗ u
−1
ρ
◦ bρ∨ , d′
ρ = dρ∨ ◦ uρ ⊗ 1ρ∨ . (27.3)
Furthermore any pair of right and left dualities (ρ
∨
, bρ, dρ) and (∨ρ, b′
ρ
, d′
ρ
) with ρ
∨ = ∨ρ is
of this form with u uniquely determined. Indeed, the morphism
uρ := d
′
ρ ⊗ 1ρ∨∨ ◦ 1ρ ⊗ bρ∨ (27.4)
is a natural isomorphism in (1, D2) with u
−1
ρ = dρ∨ ⊗1ρ ◦1ρ∨∨ ⊗b
′
ρ
and the two constructions
are inverse of one another. Given u ∈ (1, D2), any other ω ∈ (1, D2) can be written in the
form ω = uv−1, with v ∈ (1, 1) uniquely determined. (The use of the inverse of v matches
our notation in the framework of quantum groups, and originates with the convention in
[174]). Correspondingly, any other left duality is of the form
˜bρ = 1ρ∨ ⊗ vρ ◦ b
′
ρ
,
˜dρ = d
′
ρ
◦ v
−1
ρ ⊗ 1ρ∨ . (27.5)
A pivotal structure on C is the datum of a right duality functor D together with a monoidal
isomorphism ω ∈ (1, D2
) [62]. In a tensor category with right duality (bρ, dρ) the left duality
defined by a pivotal structure ω in place of u in (27.3) will be denoted as (b
ℓ
ρ
, dℓ
ρ
). A pair
of dualities (bρ, dρ) and (b
ℓ
ρ
, dℓ
ρ
) so related induces C-valued left and right quantum traces
(27.1), (27.2) which are multiplicative on tensor product morphisms. A spherical structure
on C is a pivotal structure such that the associated left and right traces coincide. In this
case we shall simply write Trρ. A spherical category is a tensor category endowed with a

168 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
spherical structure. In a spherical category Trρ(ST) = Trσ(T S), for any pair of morphisms
T ∈ (ρ, σ), S ∈ (σ, ρ) the categorical (or quantum) dimension ρ → d(ρ) is defined by
d(ρ) = Trρ(1ρ).
It is additive, multiplicative and, for categories over C as those of this paper, it takes real
values on the objects, see [9] and Sect. 2 in [51] for more details. It is not known whether
a fusion category always admits a pivotal structure, but see [51, 138, 132] for results and
references.
Definition 27.1. A generalised coboundary is a natural isomorphism c(ρ, σ) ∈ (ρ⊗σ, σ⊗ρ)
satisfying (5.7) and such that the following diagram commutes.
(ρ ⊗ σ) ⊗ τ
α −−−→ ρ ⊗ (σ ⊗ τ )1⊗c −−−→ ρ ⊗ (τ ⊗ σ)
c⊗1


y


yc
(σ ⊗ ρ) ⊗ τ
c −−−→ τ ⊗ (σ ⊗ ρ)α ←−−− (τ ⊗ σ) ⊗ ρ
(27.6)
If c(ρ, σ) is a generalised coboundary then c
′
(ρ, σ) := c(σ, ρ)
−1
is too.
Example 27.2. A generalised coboundary for which c satisfies the symmetry condition
c
2 = 1 is a coboundary in the sense introduced by Drinfeld [47].
Remark 27.3. Every braided symmetry is a generalised coboundary. Indeed, if c is such a
symmetry, we may use the hexagonal equations (5.8), (5.9) and verification of commutativity of (27.6) reduces to the Yang-Baxter relation, which follows from the braided symmetry
axioms, see e.g. Prop. 8.1.10 in [50].
The following statement explains the notion of generalised coboundary in an important
class of tensor categories.
Proposition 27.4. Let A be a weak quasi bialgebra and Q ∈ A ⊗ A a twist such that
AQ = Aop. Then c(ρ, σ) := Σρ ⊗ σ(Q) is a generalised coboundary of Rep(A).
We refer to (10.2), (10.3), (10.6), (10.15), with Q in place of R, for an explicit form of
the equality AQ = Aop.
Remark 27.5. The construction of generalised cobounderies on Rep(A) of 27.4 extends
to the case where A is a discrete weak quasi bialgebra, and the twist between A and Aop
satisfies Q ∈ M(A ⊗ A). In this case, we also see that all generalised coboundaries of
Rep(A) are of this form, via Tannaka-Krein duality.
We introduce twist deformation of generalised coboundaries.
Proposition 27.6. Let c be a generalised coboundary and η ∈ (1, 1) a natural isomorphism
of the identity functor with ηι = 1ι. Then c
η
(ρ, σ) := c(ρ, σ)◦η
−1
ρ ⊗η
−1
σ ◦ηρ⊗σ is a generalised
coboundary as well.
If c is a braided symmetry, c
η may fail to be a braided symmetry, but it is a generalised
coboundary.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 169
Proposition 27.7. Let C be a tensor category with generalised coboundary c. Then duals
are two-sided. If the category has right duals and (ρ
∨
, bρ, dρ) denotes a right duality then
b
′
ρ = c(ρ
∨
, ρ)
−1
◦ bρ, d′
ρ = dρ ◦ c(ρ, ρ∨
) (27.7)
is a left duality with ρ
∨ = ∨ρ. Conversely, given a left duality, (∨ρ, b′
ρ
, d′
ρ
) the same formula
defines a right duality.
Proof. The left duality relations for b
′
ρ
and d
′
ρ
follow from a computation that uses, in
order, commutativity of the diagram (27.6), naturality of c and the right duality equations
for bρ and dρ. □
Remark 27.8. Note that we may apply the same construction to c
′ and get another left
duality with ∨ρ = ρ
∨
,
b
′′
ρ = c(ρ, ρ∨
) ◦ bρ, d′′
ρ = dρ ◦ c(ρ
∨
, ρ)
−1
. (27.8)
In the special case where c is a genuine coboundary, these two left dualities coincide, thus
every right duality (bρ, dρ) has a canonically associated left duality in this way. It is also
easy to see that the associated right and left traces coincide thanks to naturality of c.
We do not know whether this pair of dualities corresponds to a pivotal structure for all
coboundaries, but this is known to be the case when c is a permutation symmetry or for
all the examples of coboundaries that may be constructed from braided symmetries and
twist deformation.
Definition 27.9. Let C be a tensor category and let aρ,σ ∈ (ρ ⊗ σ, ρ ⊗ σ) be a tensor
structure for the identity functor.
a) A balancing structure for a is a natural isomorphism v ∈ (1, 1) making the identity
functor 1 with tensor structure a monoidally isomorphic to the trivial tensor structure of
1, so
aρ,σ = vρ ⊗ vσ ◦ v
−1
ρ⊗σ
. (27.9)
b) If C has a right duality (ρ
∨
, bρ, dρ), a ribbon structure for a is a balancing structure
compatible with duality, see Def. 5.3.
Remark 27.10. If v is a balancing structure for a, the relation vι = 1ι easily follows from
the fact that we are assuming that ι is a strict unit, but for general categories it needs to
be part of the axioms.
We next see that the question of whether a rigid tensor category with a generalised
coboundary admits a pivotal or spherical structure can be reduced to the analysis of
two tensorial structures of the identity functor, which are naturally associated to the
coboundary. In the case where c is a braided symmetry, these reduce to the same structure,
but they may be distinct in general. We first generate tensor structures of 1 from c.
Definition 27.11. Let c be a generalised coboundary and (bρ, dρ) a right duality. Consider
the left duality (b
′
ρ
, d′
ρ
) described in (27.7). The natural isomorphism u ∈ (1, D2) associated
to this pair as in (27.3), (27.4) is called Drinfeld isomorphism.

170 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Hence Drinfeld isomorphism is the composite
uρ : ρ
1⊗bρ∨
−−−→ ρ ⊗ ρ
∨ ⊗ ρ∨∨ c⊗1
−−→ ρ
∨ ⊗ ρ ⊗ ρ∨∨ dρ⊗1
−−−→ ρ
∨∨
. (27.10)
Proposition 27.12. Let c be generalised coboundary. The isomorphisms
c
2
(ρ, σ) := c(σ, ρ) ◦ c(ρ, σ) ∈ (ρ ⊗ σ, ρ ⊗ σ)
define a tensor structure on the identity functor.
Proof. Naturality of c
2
in the two variables is obvious. The tensor structure axiom
c
2
(ρ, στ ) ◦ 1ρ ⊗ c
2
(σ, τ ) = c
2
(ρσ, τ ) ◦ c
2
(ρ, σ) ⊗ 1τ
is indeed a simple consequence of the generalised coboundary axioms for c. □
We start with a condition leading to the construction of two coinciding quantum traces.
Theorem 27.13. Let c be a generalised coboundary, (bρ, dρ) a right duality and v ∈ (1, 1)
a ribbon structure for c
2
. Then the left and right quantum traces corresponding to a given
right duality (bρ, dρ) and to the associated left duality via ω := uv−1 ∈ (1, D2), coincide.
Proof. The left duality defined by ω = uv−1is given by
˜bρ = 1ρ∨ ⊗ vρ ◦ c(ρ
∨
, ρ)
−1
◦ bρ,
˜dρ = dρ ◦ c(ρ, ρ∨
) ◦ v
−1
ρ ⊗ 1ρ∨ . (27.11)
The corresponding right trace is given by
TrR
ρ
(T) = dρ ◦ 1ρ∨ ⊗ T ◦ c(ρ, ρ∨) ◦ v
−1
ρ ⊗ 1ρ∨ ◦ bρ.
To compare it with the left trace we compute
TrL
ρ
(T) = dρ ◦ 1ρ∨ ⊗ T ◦ 1ρ∨ ⊗ vρ ◦ c(ρ
∨
, ρ)
−1
◦ bρ =
dρ ◦ 1ρ∨ ⊗ T ◦ c(ρ
∨
, ρ)
−1
◦ vρ ⊗ 1ρ∨ ◦ bρ =
dρ ◦ 1ρ∨ ⊗ T ◦ c(ρ
∨
, ρ)
−1
◦ 1ρ ⊗ vρ∨ ◦ bρ,
the last equality follows from vρ ⊗ 1ρ∨ ◦ bρ = 1ρ ⊗ vρ∨ ◦ bρ in turn due to compatibility of v
with duality. On the other hand, c(ρ
∨
, ρ)
−1 ◦ 1ρ ⊗ vρ∨ = c(ρ, ρ∨
) ◦ v
−1
ρ ⊗ 1ρ∨ ◦ vρ⊗ρ∨ thanks
to the balancing condition c
2
(ρ, σ) = vρ ⊗ vσ ◦ v
−1
ρ⊗σ
. The conclusion now follows from this
and naturality of v.
□
We have yet another tensor structure of the identity functor induced by c as follows.
Let d2(ρ, σ) : ρ
∨∨ ⊗ σ∨∨ → (ρ ⊗ σ)∨∨ denote the natural tensor structure of D2
. In the
framework of weak quasi-Hopf algebras, we have explicitly computed the element of A⊗A
inducing d2, see the discussion following Prop. 7.4 and Def. 7.5. We can equip 1 with
the new tensor structure, denoted c2, obtained pulling back the tensorial structure of D2

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 171
via Drinfeld isomorphism. In other words, we let c2(ρ, σ) ∈ (ρ ⊗ σ, ρ ⊗ σ) denote the
isomorphisms making the following diagram commute,
ρ ⊗ σ
uρ⊗uσ −−−−→ ρ
∨∨ ⊗ σ∨∨
c2


y


y
d2
ρ ⊗ σ
uρ⊗σ −−−→ (ρ ⊗ σ)
∨∨
(27.12)
We next analyse dependence of Drinfeld isomorphism and c2 on the right duality.
Lemma 27.14. Let (ρ
∨
, bρ, dρ) and (˜ρ, ˜bρ,
˜dρ) be two right dualities with associated functors
D and D˜ respectively, and let ξ ∈ (D, D ˜ ) the corresponding monoidal isomorphism. Let u
and u˜ be corresponding Drinfeld isomorphisms defined by the same generalised coboundary.
Then
u˜ρ = ζρ ◦ uρ
where ζρ := ξ
−1
ρ˜
◦ ξ
∨
ρ
: D2 → D˜ 2is the composite monoidal isomorphism.
Proof. The proof follows from a computation starting from ˜uρ taking into account bρ˜ =
ξ
−1
ρ ⊗ ξ
∨
ρ
◦ bρ∨ ,
˜bρ˜ = 1ρ˜ ⊗ ξ
−1
ρ˜
◦ bρ˜,
˜dρ = dρ ◦ ξρ ⊗ 1ρ and naturality of c. □
Proposition 27.15. Let C be a tensor category with generalised coboundary c and right
duality (ρ
∨
, bρ, dρ). Then the isomorphism
c2(ρ, σ) ∈ (ρ ⊗ σ, ρ ⊗ σ)
is a tensor structure of the identity functor which does not depend on the choice of the
right duality.
Remark 27.16. a) It is known that c2 = c
2
if c(ρ, σ) is a braided symmetry, for a proof
in a strict tensor category see [50], Prop. 8.9.3. b) In Prop. 10.9 we have explicitly shown
that c2 = c
2
for the braided symmetry associated to the quasitriangular structure of any
weak Hopf algebra.
We give an example showing that c2 and c
2 may be different tensor structures.
Example 27.17. Consider the tensor category C = VecG of finite dimensional G-graded
vector spaces over a finite abelian group G, with tensor product defined in the standard
way, for V = (Vg) and W = (Wh), (V ⊗ W)k = ⊕gh=kVg ⊗ Vh, and natural associator, see
[50]. Then every group element g defines a 1-dimensional space δg of grade g and these are
all the irreducible objects up to equivalence. We have that δ
−1
g
is both a right and left dual
of δg and duality equations are solved by the identity maps. A generalised coboundary c
is determined by the action on δg ⊗ δh, and this gives a complex-valued nonzero function
c(g, h) on two variables. The coboundary relation corresponds to requiring that c(g, h)
be a two-cocycle: c(g, h)c(gh, k) = c(h, k)c(g, hk) with c(1, g) = c(g, 1) = 1. Drinfeld
isomorphism ug acts as c(g, g−1) on δg, while d2 acts trivially. It follows that c2(g, h) =
c(g, g−1)c(h, h−1)c(gh,(gh)
−1
)
−1 while c2
(g, h) = c(g, h)c(h, g). A computation shows that
c2 = c
2
if and only if c(h, h−1) = c(h, g)c(h,(gh)
−1
), and it is easy to see that this is not
always the case for a normalised cohomologically trivial c(g, h) = µ(gh)µ(g)
−1µ(h)−1
for
G = Z3.

172 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
The following extends Deligne’s result to generalised coboundaries.
Theorem 27.18. Let C be a tensor category with generalised coboundary c and right duality
(ρ
∨
, bρ, dρ). There is a bijective correspondence between pivotal structures ω ∈ (1, D2) and
balancing structures z ∈ (1, 1) for c2 given by
ω = uz−1,
where u ∈ (1, D2) is Drinfeld isomorphism associated to c.
Proof. The map z → ω = uz−1is a bijective correspondence between isomorphisms ω ∈
(1, D2) and z ∈ (1, 1), furthermore ω is monoidal precisely when z is a balancing for c, by
commutativity of (27.12). □
We derive a sufficient condition for existence of spherical structures.
Corollary 27.19. Let C be a tensor category with right duality (bρ, dρ), generalised coboundary c satisfying
c2(ρ, σ) = c
2
(ρ, σ). (27.13)
and ribbon structure v. Then the pivotal structure ω = uv−1is spherical. The corresponding
left duality is given by
b
ℓ
ρ = 1ρ∨ ⊗ vρ ◦ c(ρ
∨
, ρ)
−1
◦ bρ, dℓ
ρ = dρ ◦ c(ρ, ρ∨
) ◦ v
−1
ρ ⊗ 1ρ∨ (27.14)
Proof. This is a consequence of Theorem. 27.13 and Prop. 27.18. The left duality equations
follow from (27.5), (27.7). □
In particular, the quantum dimension is given by
d(ρ) = dρ ◦ 1ρ∨ ⊗ vρ ◦ c(ρ
∨
, ρ)
−1
◦ bρ = dρ ◦ c(ρ, ρ∨) ◦ v
−1
ρ ⊗ 1ρ∨ ◦ bρ. (27.15)
Theorem. 27.13 recovers corresponding results known for ribbon categories [174]. Note
that Cor. 27.19 is of little use in the case where (27.13) does not hold. Indeed in the
Example 27.17 as we may choose for c the unique permutation symmetry, so c2 = c
2 = 1,
gives that the associated Drinfeld isomorphism uρ = 1 is a spherical structure.
We next discuss properties of twisted generalised coboundaries. Let (bρ, dρ) be a fixed
right duality, c a generalised coboundary, u the associated Drinfeld isomorphism and
c2 ∈ (ρ ⊗ σ, ρ ⊗ σ) natural isomorphism as in (27.12). Let η ∈ (1, 1) be a natural isomorphism, and c
η
the twisted coboundary. The corresponding isomorphisms will be denoted
respectively by u
η and c
η
2
.
Proposition 27.20. Let η ∈ (1, 1) be a compatible with duality. We have
a) u
η = u ◦ η−2
,
b) c
η
2
(ρ, σ) = η
2
ρ⊗σ ◦ c2(ρ, σ) ◦ η
−2
ρ ⊗ η
−2
σ
, ((c
η
)
2
(ρ, σ) = η
2
ρ⊗σ ◦ c
2
(ρ, σ) ◦ η
−2
ρ ⊗ η
−2
σ
,)
c) if v is a balancing (ribbon) structure for c2 (c
2
) then v
η
:= v ◦ η
−2
is a balancing
(ribbon) structure for c
η
2
((c
η
)
2
)
d) v and v
η
correspond to the same pivotal structure under the map described in Prop.
27.18, and therefore to the same left duality and quantum traces,
e) if c satisfies (27.13) then so does c
η
.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 173
Proof. a) The proof follows from a computation starting from (27.10), with c replaced by
c
η
, where we use naturality and compatibility with duality of η and the fact that the right
duality functor (5.6) can equivalently be defined by dσ ◦ 1σ∨ ⊗ T = dρ ◦ T
∨ ⊗ 1ρ. The
remaining statements follow from one another. □
We describe a twisting making a generalised coboundary with a balancing structure into
a genuine coboundary and Drinfeld isomorphism into a monoidal isomorphism from the
identity tensor functor. This twisting first appeared in the work of Drinfeld [47] in the
framework of quantised universal Hopf algebras. As it turns out, the associated spherical
structure is the same as that arising in the framework of ribbon categories.
Theorem 27.21. In a tensor category with right duality, let c be a generalised coboundary
satisfying (27.13) (e.g. a braided symmetry) with balancing structure v, and let w ∈ (1, 1)
be a natural isomorphism compatible with duality such that w
2 = v. Then cw is a coboundary, c
w
2 = 1 ⊗ 1, v
w = 1, and uw is a spherical structure coinciding with that defined by c
and v as in Prop. 27.18.
The construction of c
w is the analogue of Drinfeld construction of unitarized R-matrix
in a ribbon Hopf algebra. In Sect. 28 we shall study the relation with Ω-involution.
