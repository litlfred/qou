---
doc_id: motivicperiodsandp1minus3pointsv3
doc_title: "Motivic periods and P^1 minus 3 points"
section_id: sec-047-24-ihara-action-let-a-denote-the-group-of-automo
section_title: "Ihara action. Let A denote the group of automorphisms of the groupoid"
section_number: 2.4
pages: 12-13
source_pdf: MotivicPeriodsandP1minus3pointsv3.pdf
source_sha256: 7870572b8cc316d0
doc_brief: "Motivic periods and P^1 minus 3 points — This is a review of the theory of the motivic fundamental grou p of the projective line minus three points, and its relation to mult iple zeta values."
---
xΠ y for x, y ∈ {0, 1} which respects the structures 1 , 2 described in §2.3.
Proposition 2.5. The scheme 0Π 1 is an A-torsor. In particular, the action of A
on 1 ∈ 0Π 1 deﬁnes an isomorphism of schemes
a ↦→a(1) : A − →0Π 1 . (2.11)
The action of A on 0Π 1 deﬁnes, via this isomorphism, a new group law
◦ : 0Π 1 × 0Π 1 → 0Π 1 .
It is given explicitly on formal power series by Ihara’s form ula
A(x0, x1) ◦ G(x0, x1) = G(x0, Ax1A−1)A (2.12)
Proof. For the basic geometric idea, see [27], §2.3. Let a ∈ A, and write axy(ξ) for
the action of a on ξ ∈ xΠ y. Write a = a01(1). Since 0Π 0 is a group, a acts trivially
on its identity element, and so a00(1) = 1. Via the map 0Π 1 × 1Π 0 → 0Π 0 we have
a01(1)a10(1) = a00(1) and hence a10(1) = a−1. The inertial conditions give
a00(exp(x0)) = exp( x0) and a11(exp(x1)) = exp( x1) (2.13)
Now the composition of paths 1Π 0 × 0Π 0 × 0Π 1 → 1Π 1 gives rise to an equation
1. exp(x1).1 = exp( x1). Applying a to this gives by the second equation in (2 .13)
a00(exp(x1)) = a exp(x1)a−1 = exp(ax1a−1) (2.14)
which completely determines the action of A on 0Π 0. Via the map 0Π 0×0Π 1 → 0Π 1
we have the equation g.1 = g, and hence
a01(g) = a00(g).a . (2.15)
Formula (2.12) follows from (2.13), (2.14), (2.15). One easily checks that a uniquely
determines a, and so (2 .11) is an isomorphism (see also [14], 5.9.)
The groupoid and inertia structures are preserved by U dR, giving a morphism
ρ : U dR − → A
(2. 11)
∼
= 0Π 1 (2.16)
such that the following diagram commutes
U dR × 0Π 1 − →0Π 1 (2.17)
ρ ×id ↓ ↓ id
0Π 1 × 0Π 1
◦
− →0Π 1
In principle this describes the action of the motivic Galois group on 0Π 1. Note,
however, that the map (2 .16) is mysterious and very little is known about it.
Motivic periods and P1\{ 0, 1, ∞} 13
