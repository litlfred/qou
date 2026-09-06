---
doc_id: arxiv-2108.09349v2
doc_title: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS BARBARA NIMERSHIEM"
section_id: sec-009-32-volumes-of-angle-structures
section_title: "Volumes of angle structures"
section_number: 3.2
pages: 13-15
source_pdf: 2108.09349v2.pdf
source_sha256: 4c732bfcbf3dfb16
doc_brief: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS BARBARA NIMERSHIEM — We construct topological triangulations for complements of ( −2, 3,n )-pretzel knots and links with n≥ 7."
---
bolic tetrahedron, T , with dihedral angles θ1, θ2, and θ3 is given by
V (T ) = L(θ1) + L(θ2) + L(θ3),
where the Lobachevsky function, L, is deﬁned as
L(x) =−
∫ x
0
log|2 sint|dt.
14 BARBARA NIMERSHIEM
Deﬁnition 3.3. For a point θ∈A (τ), which speciﬁes angles for the n tetrahedra Ti∈ τ and has
all θi∈ (0,π ), deﬁne the volume associated to θ,V(θ), by
V(θ) =
n∑
i=1
V (Ti) =
3n∑
i=1
L(θi)
and note thatV(θ)> 0 for θ∈A (τ).
As summarized in [5], L is well-deﬁned and continuous on R. Thus, the deﬁnition of V can be
extended to the closure of A(τ), which may include points with coordinates equal to 0 or π where
the integral itself is improper. If θ∈A(τ), thenV(θ)≥ 0.
Straightforward tetrahedra-by-tetrahedra calculations show that for a positive angle structure θ
and a tangent vector ⃗ v∈TθA(τ),
∂V
∂⃗ v=
3n∑
i=1
−vi log sinθi and ∂2V
∂⃗ v2 < 0. (1)
See, for example, [5, Lemma 5.3].
BecauseV is strictly concave down onA(τ), any critical point inA(τ) is unique and an absolute
maximum. In fact, the ﬁrst and second partials (1) are enough to prove the same for a maximal
point on the boundary.
Proposition 3.1. WheneverA(τ)⁄=∅, the point at which the volume functional V :A(τ)→ [0,∞)
attains its maximum is unique.
Proof. If there is a critical point α inA(τ), the strict concavity ofV guarantees thatα is unique and
thatV(α) is the maximum volume. If, on the other hand, there is no critical point on the interior,
the compactness ofA(τ) ensures that there is a point α∈A(τ)−A(τ) withV(α) maximal. To show
such an angle structure is unique, we ﬁrst examine its coordinates. Because α /∈A (τ), there is at
least one tetrahedron in τ with an assigned angle of 0 or π. The maximality of α further constrains
the angles of such a tetrahedron as noted in the following lemma.
Lemma 3.2. WhenV(α) is a maximum, any tetrahedron assigned an angle of 0 or π must have
angles of 0, 0, and π in some order.
Proof of Lemma 3.2. By Condition (2) of Deﬁnition 3.1, the angles in a tetrahedron must sum to π,
so this statement is obviously true if one angle in a tetrahedron is assigned π or if two angles are
assigned 0. We now argue, as also noted in [9, Proposition 7.1] and [10, Proposition 7], that assigning
exactly one 0 angle contradicts the maximality of α.
Consider, for example, a tetrahedron, T0∈ τ, with nonnegative angles 0, θ0, and π−θ0. For
any 0 < λ < 1, deﬁne a family of tetrahedra T (t)|t≥0 with angles θ1 = t, θ2 = θ0−λt, and
θ3 = π− (t +θ0−λt), so T (0) = T0 and, as t increases, the angles of the tetrahedron change —
θ1 is increased, while θ2 and θ3 are decreased. The ﬁrst partial in (1) restricted to this family of
tetrahedra yields
dV (T (t))
dt
⏐⏐⏐
t=0+
=
3∑
i=1
−dθi
dt log sinθi
⏐⏐⏐
t=0+
= +∞.
In other words, increasing the solitary 0 angle by a small amount would increase T0’s volume (and
thus the total volumeV) by a much larger amount, violating the maximality ofα. Thus, if a maximal
angle structure assigns any angles in {0,π} to a tetrahedron, two of its angles are assigned 0 and
one π, thus proving the lemma. We call a tetrahedron with angles in {0,π} ﬂat and observe that
its volume is 0. □
Returning to the proof of Proposition 3.1, we will use the constraints Lemma 3.2 imposes on the
coordinates of a maximal point α∈A(τ)−A (τ) to prove thatα is unique. Let β be inA(τ)−A (τ)
withV(β) =V(α) and let µ∈ [0,π ]3n be the point whose coordinates are determined by averaging
GEOMETRIC TRIANGULATIONS OF A F AMILY OF HYPERBOLIC 3-BRAIDS 15
those of α and β. Then µ∈A(τ), because the set A(τ) is convex. We will examine the volume of
each tetrahedron T under the angle structure assigned by µ and will denote this volume byV(µ|T ).
Case 1: If α and β assign the same angles to a tetrahedron T , then their average µ does as
well, soV(µ|T ) is equal to V(α|T ) (and alsoV(β|T )).
Case 2: If α and β assign diﬀerent angles to a tetrahedron T and both α|T and β|T are ﬂat,
then, because α and β are maximum points, the angles must be 0, 0, and π (in diﬀerent
orders), and the coordinates of µ|T are 0, π
2 , and π
2 in some order. In this case, V(µ|T )
equals 0 just as V(α|T ) andV(β|T ) do.
Case 3: Ifα andβ assign diﬀerent angles to a tetrahedron T and at least one of α|T orβ|T is
not ﬂat, we will argue thatV(µ|T ) is strictly greater than the average ofV(α|T ) andV(β|T ).
Without loss of generality suppose α|T is not ﬂat. Deﬁne γ(t) to be the line segment joining
α|T and β|T :
γ(t) =tα|T + (1−t)β|T for t∈ [0, 1].
Let V (t) be the volume of the tetrahedron whose angles are given by γ(t). As a restriction
ofV, the function V is continuous on [0, 1]. Also, because α|T is not ﬂat, γ is in (0,π )3 for
0<t ≤ 1, so V is diﬀerentiable on (0, 1] and by the second partial in (1), V′′ < 0. Applying
the Mean Value Theorem to V yields points c1∈
(
0, 1
2
)
and c2∈
( 1
2, 1
)
with
V′(c1) = 2
(
V
( 1
2
)
−V (0)
)
V′(c2) = 2
(
V (1)−V
( 1
2
))
and negative second derivatives, so V′(c1)>V ′(c2), which means
2V
( 1
2
)
>V (1) +V (0).1
Because V
( 1
2
)
= V(µ|T ), V (1) = V(α|T ), and V (0) = V(β|T ), this inequality implies
V(µ|T )> 1
2(V(α|T ) +V(β|T )).
In all cases, the volume of a tetrahedron T computed usingµ, the average of the angle structures,
is greater than or equal to the average of the volumes of T computed using the angle structures α
and β, so summing the individual volumes over all tetrahedra in τ yields
V(µ)≥ 1
2(V(α) +V(β)) =V(α)
with equality only when there are no tetrahedra in Case 3. But V(α) is the maximum volume, so
V(µ)≤V (α), meaning V(µ) =V(α) and there are no Case 3 tetrahedra. The only way α and β
can assign diﬀerent angles to a tetrahedron T is if α|T and β|T are both ﬂat (Case 2). In this case,
V(µ) =V(α), so µ is also maximal, but, as we have seen, the coordinates of µ|T are 0, π
2 , and π
2 ,
which is not allowed for maximal angle structures. Therefore, α andβ cannot assign diﬀerent angles
to any of the tetrahedra and β =α, which is the unique maximum point. □
Positive angle structures that maximize the total volume play an important role in the Casson-
Rivin program.
