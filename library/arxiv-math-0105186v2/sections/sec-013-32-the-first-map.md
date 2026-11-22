---
doc_id: arxiv-math-0105186v2
doc_title: "A long exact sequence for symplectic Floer cohomology"
section_id: sec-013-32-the-first-map
section_title: "The first map"
section_number: 3.2
pages: 55-60
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
toc_source: inferred
doc_brief: "A long exact sequence for symplectic Floer cohomology — 17 sections: Front matter; Introduction; Dehn twists, and all that"
---
The ﬁrst map
Let S be the surface in Figure 3, which has three boundary components ∂kS
and three strip-like ends (two positive and a negative one). Take the trivial
exact symplectic ﬁbration π : E = S × M →S, with Ω∈Ω2(E), Θ ∈Ω1(E)
pulled back from ω, θ.
Equip this with the Lagrangian boundary condition
Q = (∂1S × τL(L0)) ∪(∂2S × L) ∪(∂3S × L1); κQ is zero, and KQ(z, x) is equal
to KτL(L0)(x), KL(x) or KL1(x), for z in the respective component ∂kS. This
gives rise to a relative invariant
Φrel
0 (E, π, Q) : HF(L, L1) ⊗HF(τL(L0), L) →HF(τL(L0), L1).
The purpose of this section is to analyse this more closely, on the cochain level.
Fix a complex structure j on S, trivial over the ends, and let U ⊂S be the
open set shaded in Figure 3.
S
2
S
3
S
1
Figure 3:
Lemma 3.3. (E, π, Q) and U satisfy the conditions of Proposition 2.28(i).
Proof. The curvature of (E, π) is zero. A section u(z) = (z, σ(z)) is horizontal
iﬀσ(z) ≡x ∈M is constant, and it further satisﬁes u(∂S) ⊂Q iﬀx ∈τL(L0) ∩
L∩L1. If W ⊂S is a connected open subset which intersects all three boundary
components, the same description applies to partial horizontal sections w : W →
E|W with w(W ∩∂S) ⊂Q. As a consequence, any such section can be extended
to u ∈Mh. This is in particular true for W = U.
Fix some x ∈τL(L0)∩L∩L1 and the corresponding constant section u ∈Mh.
By deﬁnition A(u) = 0, and it remains to prove that ind Du,J = 0. From the
description of the points x in Lemma 3.2(iii), together with the corresponding
local statement in Lemma 1.9, it follows that there is a symplectic isomorphism
T Mx ∼= Cn which takes the tangent spaces to τL(L0), L, and L1 to Rn, e2πi/3Rn,
and eπi/3Rn respectively. Since the index is independent of the almost complex
structure, we may choose J = j × JM to be the product of j and some ω-
compatible JM on M. We may also assume that the isomorphism T Mx ∼= Cn
takes JM
x
to the standard complex structure. By deﬁnition, the domain of Du,J
are sections of the vector bundle u∗(T Ev, J|T Ev) ∼= S × T Mx, with boundary
55
conditions given by the tangent spaces to τL(L0), L, L1. Its range are (0, 1)-
forms with values in the same vector bundle. The preceding discussion allows
us to identify
W1
u = {X ∈W 1,p(S, Cn) : Xz ∈ei(1−k)π/3Rn for z ∈∂kS},
W0
u,J = Lp(Λ0,1S ⊗Cn).
(3.8)
In (2.5) take ∇= ∇S × ∇M to be the product of torsion-free connections on
S and on M. Then the second term (∇XJ) ◦Du ◦j in the formula vanishes,
because Du ◦j takes values in T Eh whereas ∇XJ is nontrivial only on T Ev;
and moreover, the pullback connection u∗∇on u∗T Ev is trivial. This shows
that Du,J is the standard ¯∂-operator for functions S →Cn, with boundary
conditions (3.8).
2
z
z
z
z1
3
z0
4
z5
Figure 4:
There is a general index formula for such operators, but we prefer to use an
ad hoc gluing trick instead. Consider the compact surface ¯S in Figure 4, which
is of genus one with one boundary component. Parametrize the boundary by
a closed path l : [0; 6] →∂¯S, such that l(t) = zt for t ∈{0, 1, 2, 3, 4, 5} are the
marked points in Figure 4. Take a smooth nondecreasing function λ : [0; 6] →R
such that
λ(t) =









0
0 ≤t ≤1,
1/3
2 ≤t ≤3,
2/3
4 ≤t ≤5.
1
t = 6.
56
Let ¯D be the ¯∂-operator on the trivial bundle ¯S × Cn →¯S, with boundary
condition given by the family of Lagrangian subspaces Λl(t) = eπiλ(t)Rn ⊂Cn.
As a loop in the Lagrangian Grassmannian, this represents n times the standard
generator of the fundamental group. Riemann-Roch for compact surfaces with
boundary therefore tells us that ind ¯D = nχ( ¯S)+n = 0. On the other hand, one
can divide ¯S into ﬁve pieces (two shaded and three unshaded ones) as indicated
in Figure 4, and add strip-like ends to each piece; the standard gluing theory
for elliptic operators says that ind ¯D is the sum of the indices of the obvious
corresponding operators on those pieces. For each shaded piece, this yields a
copy of Du,J (in one of the two cases, the vector space Cn has been rotated
by eπi/3). The unshaded pieces give rise to operators of index zero. This can
be derived from the index theorem of [20], or else by directly deforming the
operator to an invertible one. Consider for instance the two intervals of ∂¯S
which are contained in the leftmost unshaded piece. The Lagrangian subspaces
Λz parametrized by the points z in one of these intervals are all equal to eπi/3Rn;
for the other interval, they are of the form eπisRn for 2/3 ≤s ≤1.
Since
eπi/3Rn ∩eπisRn = 0 for all such s, the Maslov index for paths [20] is zero. The
same holds for the other unshaded pieces, and one concludes that 0 = ind ¯D =
2 ind Du,J.
At this point, ﬁx
J(1) ∈Jreg(M, τL(L0), L),
J(2) ∈Jreg(M, L, L1),
J(3) ∈Jreg(M, τL(L0), L1).
Proposition 2.28(i) tells us that there is a J ∈J(E, π, j, J(1), J(2), J(3)) which
is both horizontal and regular. By part (ii) of the same result, the coeﬃcients
νJ(˜x0, x1, x) for ˜x0 ∈τL(L0)∩L, x1 ∈L∩L1, x ∈τL(L0)∩L1, are zero whenever
χ(˜x0, x1, x) = aτL(L0),L1(x) −aτL(L0),L(˜x0) −aL,L1(x1)
(3.9)
is < 0. Lemma 3.2(ii) shows that χ(˜x0, x1, x), if ≥0, must be either in [0; ǫ) or
[3ǫ; ∞), and that the ﬁrst case only happens for x = p(˜x0, x1). Hence, if one
writes the relative invariant as
CΦrel
0 (E, π, Q, J) = φ + (CΦrel
0 (E, π, Q, J) −φ),
φ(⟨˜x0⟩⊗⟨x1⟩) = νJ(˜x0, x1, p(˜x0, x1))⟨p(˜x0, x1)⟩
(3.10)
then φ is of order [0; ǫ), while the second term is of order [3ǫ; ∞). The rest of
this section contains the proof of the following result, which determines the low
order part:
Proposition 3.4. νJ(˜x0, x1, p(˜x0, x1)) = 1 for all (˜x0, x1).
There is one particular case of this which follows from the previous con-
siderations.
Namely, suppose that there is a pair (˜x0, x1) with ˜x0 = x1 =
57
x ∈τL(L0) ∩L ∩L1. In that case p(x, x) = x and χ(x, x, x) = 0 by Lemma
3.2(iii), and therefore νJ(x, x, x) = #Mh(x, x, x) by Proposition 2.28(ii). Now
#Mh(x, x, x) = 1 because, as we saw already when proving Lemma 3.3, the
unique element of that space is the constant section u(z) = (z, x). Our strategy
will be to reduce the computation of all the νJ(˜x0, x1, p(˜x0, x1)) to this case, by
using suitable deformations.
What “deformation” means here is keeping the submanifolds L, L0, L1 and
the constant ǫ ﬁxed, while changing the remaining data. More precisely, for
0 ≤µ ≤1 we consider the following: a smooth family f µ of diﬀeomorphisms
Sn →L; smoothly varying positive numbers λµ, and symplectic embeddings
ιµ : T (λµ) →M with ιµ|T (0) = f µ; the Dehn twists τ µ
L deﬁned using ιµ and
functions Rµ supported in (−∞; λµ); and constants δµ.
These should agree
with the given data f, λ, ι, R, τL, δ for µ = 0. We also require that the analogues
of (III)–(V) continue to hold for any µ; where in (V) we take the original ǫ
throughout.
Choose ˜x0 ∈τL(L0) ∩L, x1 ∈L ∩L1. Given a “deformation” in the sense
which we have just explained, one can set ˜xµ
0 = τ µ
L(τL)−1(˜x0) ∈τ µ
L(L0) ∩L and
xµ
1 = x1 ∈L ∩L1, which “continues” the points smoothly into the deformed
situation.
We claim that x = p(˜x0, x1) ﬁts similarly into a smooth family
xµ ∈τ µ
L(L0) ∩L1. The point is that since (I)–(V) continue to hold, Lemma 3.2
can be applied to the situation for any µ. This ensures that the intersections
τ µ
L(L0) ∩L1 remain transverse, which implies that a unique family xµ exists. In
fact, it even provides a smooth family of injective maps pµ : (τ µ
L(L0)∩L)×(L ∩
L1) →τ µ
L(L0) ∩L1, such that xµ = pµ(˜xµ
0 , xµ
1).
Lemma 3.5. For any (˜x0, x1) there is a “deformation” such that ˜x1
0 = x1
1.
Proof. From (III) we know that y0 = f −1(τ −1
L (˜x0)), y1 = f −1(x1) are points
on Sn whose distance is ≥2πδ. Let gµ ∈Diﬀ(Sn) be an isotopy, g0 = id, such
that g1(y0), g1(y1) are antipodes. There are Cµ ≥1, smoothly depending on µ
and with C0 = 1, with the property that
Cµ ≥||D(gµ)y||, ||D(gµ)−1
y ||
for all y ∈Sn.
Consider the “deformation” f µ = f ◦(gµ)−1, λµ = λ/Cµ, ιµ = ι ◦Gµ|T (λµ),
δµ = δ/Cµ; here Gµ ∈Sympe(T ) is induced by gµ, in the sense that Gµ|T (0) =
(gµ)−1. The bound on D(gµ) implies that Gµ maps T (λµ) to T (λ), so that
ιµ is well-deﬁned. On the other hand, because of the bound on D(gµ)−1, the
distance between any point of (f µ)−1(L∩L0) = gµf −1(L∩L0) and any point of
(f µ)−1(L∩L1) = gµf −1(L∩L1) is ≥2πδµ, which shows that (III) holds during
the deformation. For (IV) it is suﬃcient to note that Gµ takes the canonical
one-form θT to itself and maps ﬁbres to ﬁbres. And it is no problem to ﬁnd
functions Rµ which satisfy (V) with the δµ deﬁned above and the given ǫ. By
deﬁnition
τL|L = f ◦A ◦f −1,
τµ
L|L = f µ ◦A ◦(f µ)−1 = f ◦(gµ)−1 ◦A ◦gµ ◦f −1.
58
Since g1(y1) = A(g1(y0)) by construction, one sees that
˜x1
0 = τ1
L(τL)−1(˜x0) = f ◦(g1)−1 ◦A ◦g1(y0) = f(y1) = x1 = x1
1.
Given a “deformation”, one can repeat the construction at the beginning of
this section in a parametrized sense, which means equipping the trivial exact
symplectic symplectic ﬁbration (E, π) with a smooth family Qµ of Lagrangian
boundary conditions, modelled over the ends on the pairs of exact Lagrangian
submanifolds (τ µ
L(L0), L), (L, L1), and (τ µ
L(L0), L1). Since their intersections
are transverse for all µ, it makes sense to consider parametrized moduli spaces
of pseudo-holomorphic sections. To do that, take smooth families of almost com-
plex structures J(1),µ, J(2),µ, J(3),µ ∈J(M) which reduce to the previously cho-
sen ones for µ = 0, and similarly a family Jµ ∈Jh(E, π, j, J(1),µ, J(2),µ, J(3),µ).
The parametrized moduli space we are interested in is
Mpara =
[
µ
{µ} × MJµ(˜xµ
0 , xµ
1, xµ)
for points ˜xµ
0, xµ
1, xµ as introduced above.
Lemma 3.6. Mpara is compact.
Proof. Consider CF(L, L1), CF(τ µ
L(L0), L), CF(τ µ
L(L0), L1). We already know
that the ﬁrst of these R-graded vector spaces has gap (0; 3ǫ); for the second one,
the same is true because it agrees with CF(L0, L) up to a constant shift in the
grading; and by repeating the considerations after Lemma 3.2, one can show
that CF(τ µ
L(L0), L1) has gap (0; 2ǫ). As another consequence of Lemma 3.2(ii)
in the deformed situation, any (µ, u) ∈Mpara satisﬁes
A(u) = aτ µ
L(L0),L1(xµ) −aτ r
L(L0),L(˜xµ
0 ) −aL,L1(xµ
1) ∈[0; ǫ).
One can now argue exactly as in Lemma 2.24; there are no points at inﬁnity in
the parametrized Gromov-Floer compactiﬁcation, since the principal component
of any such point would have negative action, which would contradict the fact
that (E, π) has nonnegative curvature.
Suppose now that the J(k),µ and Jµ for µ = 1 have been chosen regular; for
J1 this can be achieved without leaving the class of horizontal almost complex
structure, because Lemma 3.3 equally applies to the deformed situation for
µ = 1. By using a parametrized version of the same lemma and of Proposition
2.28(i), one sees that in addition, the family (Jµ) can be chosen to be regular in
the parametrized sense. Then the one-dimensional part of Mpara is a compact
one-manifold, and its boundary points are precisely those with µ = 0 or 1. One
concludes that
νJ(˜x0, x1, x) = νJ1(˜x0
0, x1
1, x1).
59
If the “deformation” is as in Lemma 3.5, the situation for r = 1 is exactly the
special case which we have already discussed, so that νJ1(˜x0
0, x1
1, x1) = 1. Since
such deformations exist for all (˜x0, x1), Proposition 3.4 is proved.
From now on, we ﬁx some J = J(4) ∈Jreg,h(E, π, Q, j, J(1), J(2), J(3)) and
write b = CΦrel
0 (E, π, Q, J(4)) : C′ →C for the relative invariant on the cochain
level. Let β be the map deﬁned at the end of Section 3.1. What (3.10) and
Proposition 3.4 say is that b = β + (b −β), with b −β of order [3ǫ; ∞), which is
even slightly more than required by Lemma 2.32.
L1
L
L
τ
0
L0
(L  )
Figure 5:
Remark 3.7. Our relative invariant is the well-known pair-of-pants product,
or Donaldson product; in fact, if u(z) = (z, σ(z)) lies in MJ(˜x0, x1, x), then σ :
S →M is a “pseudo-holomorphic triangle” whose sides lie on τL(L0), L, L1 and
whose vertices are ˜x0, x1, x. Proposition 3.4 asserts that there is an odd number
of low-area triangles with certain speciﬁed vertices. In the lowest dimension,
n = 1, one can see directly that there is precisely one such triangle (Figure 5).
In higher dimensions it is still easy to construct explicitly the analogue of this
particular triangle, but proving that there are no others seems more diﬃcult. For
that reason, we have preferred to take the indirect approach via “deformations”,
which eﬀectively meant moving τL(L0) in such a way that the area of the triangle
shrinks to zero.
