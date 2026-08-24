---
doc_id: arxiv-math-0105186v2
doc_title: "Along exact sequence for symplectic Floer cohomology Paul Seidel"
section_id: sec-036-0-eπqj-φ-cφ-rel
section_title: "(E,π,Q,J ) = φ + (CΦ rel"
section_number: 0
pages: 57-60
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
doc_brief: "A long exact sequence for symplectic Floer cohomology — 45 sections: Introduction; Dehn twists, and all that; Exact symplectic geometry and ﬁbra"
---
0 (E,π,Q,J )−φ),
φ(⟨˜x0⟩⊗⟨x1⟩) = νJ (˜x0,x 1,p (˜x0,x 1))⟨p(˜x0,x 1)⟩ (3.10)
then φ is of order [0; ǫ), while the second term is of order [3 ǫ;∞). The rest of
this section contains the proof of the following result, whi ch determines the low
order part:
Proposition 3.4. νJ (˜x0,x 1,p (˜x0,x 1)) = 1 for all (˜x0,x 1).
There is one particular case of this which follows from the pr evious con-
siderations. Namely, suppose that there is a pair (˜ x0,x 1) with ˜x0 = x1 =
57
x∈ τL(L0)∩L∩L1. In that case p(x,x ) = x and χ(x,x,x ) = 0 by Lemma
3.2(iii), and therefore νJ (x,x,x ) = # Mh(x,x,x ) by Proposition 2.28(ii). Now
#Mh(x,x,x ) = 1 because, as we saw already when proving Lemma 3.3, the
unique element of that space is the constant section u(z) = (z,x ). Our strategy
will be to reduce the computation of all the νJ (˜x0,x 1,p (˜x0,x 1)) to this case, by
using suitable deformations.
What “deformation” means here is keeping the submanifolds L,L 0,L 1 and
the constant ǫ ﬁxed, while changing the remaining data. More precisely, fo r
0≤ µ≤ 1 we consider the following: a smooth family fµ of diﬀeomorphisms
Sn→ L; smoothly varying positive numbers λµ, and symplectic embeddings
ιµ : T (λµ)→ M with ιµ|T (0) = fµ; the Dehn twists τµ
L deﬁned using ιµ and
functions Rµ supported in ( −∞;λµ); and constants δµ. These should agree
with the given data f,λ,ι,R,τ L,δ forµ = 0. We also require that the analogues
of (III)–(V) continue to hold for any µ; where in (V) we take the original ǫ
throughout.
Choose ˜x0∈ τL(L0)∩L, x1∈ L∩L1. Given a “deformation” in the sense
which we have just explained, one can set ˜ xµ
0 =τµ
L (τL)−1(˜x0)∈τµ
L (L0)∩L and
xµ
1 = x1∈ L∩L1, which “continues” the points smoothly into the deformed
situation. We claim that x = p(˜x0,x 1) ﬁts similarly into a smooth family
xµ∈τµ
L (L0)∩L1. The point is that since (I)–(V) continue to hold, Lemma 3.2
can be applied to the situation for any µ. This ensures that the intersections
τµ
L (L0)∩L1 remain transverse, which implies that a unique family xµ exists. In
fact, it even provides a smooth family of injective maps pµ : (τµ
L (L0)∩L)× (L∩
L1)→τµ
L (L0)∩L1, such that xµ =pµ(˜xµ
0,xµ
1 ).
Lemma 3.5. For any (˜x0,x 1) there is a “deformation” such that ˜x1
0 =x1
1.
Proof. From (III) we know that y0 = f −1(τ −1
L (˜x0)), y1 = f −1(x1) are points
on Sn whose distance is ≥ 2πδ. Let gµ∈ Diﬀ( Sn) be an isotopy, g0 = id, such
thatg1(y0), g1(y1) are antipodes. There are Cµ≥ 1, smoothly depending on µ
and with C0 = 1, with the property that
Cµ≥||D(gµ)y||,||D(gµ)−1
y || for all y∈Sn.
Consider the “deformation” fµ = f◦ (gµ)−1, λµ = λ/Cµ, ιµ = ι◦Gµ|T (λµ),
δµ =δ/Cµ; here Gµ∈ Sympe(T ) is induced by gµ, in the sense that Gµ|T (0) =
(gµ)−1. The bound on D(gµ) implies that Gµ maps T (λµ) to T (λ), so that
ιµ is well-deﬁned. On the other hand, because of the bound on D(gµ)−1, the
distance between any point of ( fµ)−1(L∩L0) = gµf −1(L∩L0) and any point of
(fµ)−1(L∩L1) = gµf −1(L∩L1) is≥ 2πδµ, which shows that (III) holds during
the deformation. For (IV) it is suﬃcient to note that Gµ takes the canonical
one-form θT to itself and maps ﬁbres to ﬁbres. And it is no problem to ﬁnd
functions Rµ which satisfy (V) with the δµ deﬁned above and the given ǫ. By
deﬁnition
τL|L =f◦A◦f −1, τ µ
L|L =fµ◦A◦ (fµ)−1 =f◦ (gµ)−1◦A◦gµ◦f −1.
58
Since g1(y1) = A(g1(y0)) by construction, one sees that
˜x1
0 =τ 1
L(τL)−1(˜x0) = f◦ (g1)−1◦A◦g1(y0) = f (y1) = x1 =x1
1.
Given a “deformation”, one can repeat the construction at th e beginning of
this section in a parametrized sense, which means equipping the trivial exact
symplectic symplectic ﬁbration ( E,π ) with a smooth family Qµ of Lagrangian
boundary conditions, modelled over the ends on the pairs of e xact Lagrangian
submanifolds (τµ
L (L0),L ), (L,L 1), and ( τµ
L (L0),L 1). Since their intersections
are transverse for all µ, it makes sense to consider parametrized moduli spaces
of pseudo-holomorphic sections. To do that, take smooth fam ilies of almost com-
plex structures J (1),µ,J (2),µ,J (3),µ∈ J(M ) which reduce to the previously cho-
sen ones for µ = 0, and similarly a family Jµ∈ Jh(E,π,j,J (1),µ,J (2),µ,J (3),µ).
The parametrized moduli space we are interested in is
Mpara =
⋃
µ
{µ}× MJ µ (˜xµ
0,xµ
1,xµ)
for points ˜xµ
0,xµ
1,xµ as introduced above.
Lemma 3.6. Mpara is compact.
Proof. ConsiderCF (L,L 1),CF (τµ
L (L0),L ),CF (τµ
L (L0),L 1). We already know
that the ﬁrst of these R-graded vector spaces has gap (0; 3 ǫ); for the second one,
the same is true because it agrees with CF (L0,L ) up to a constant shift in the
grading; and by repeating the considerations after Lemma 3. 2, one can show
thatCF (τµ
L (L0),L 1) has gap (0; 2 ǫ). As another consequence of Lemma 3.2(ii)
in the deformed situation, any ( µ,u )∈ Mpara satisﬁes
A(u) = aτ µ
L(L0),L1(xµ)−aτ r
L(L0),L(˜xµ
0 )−aL,L1(xµ
1 )∈ [0;ǫ).
One can now argue exactly as in Lemma 2.24; there are no points at inﬁnity in
the parametrized Gromov-Floer compactiﬁcation, since the principal component
of any such point would have negative action, which would con tradict the fact
that (E,π ) has nonnegative curvature.
Suppose now that the J (k),µ and Jµ for µ = 1 have been chosen regular; for
J 1 this can be achieved without leaving the class of horizontal almost complex
structure, because Lemma 3.3 equally applies to the deforme d situation for
µ = 1. By using a parametrized version of the same lemma and of Pr oposition
2.28(i), one sees that in addition, the family ( Jµ) can be chosen to be regular in
the parametrized sense. Then the one-dimensional part of Mpara is a compact
one-manifold, and its boundary points are precisely those w ithµ = 0 or 1. One
concludes that
νJ (˜x0,x 1,x ) = νJ 1 (˜x0
0,x 1
1,x 1).
59
If the “deformation” is as in Lemma 3.5, the situation for r = 1 is exactly the
special case which we have already discussed, so that νJ 1(˜x0
0,x 1
1,x 1) = 1. Since
such deformations exist for all (˜x0,x 1), Proposition 3.4 is proved.
From now on, we ﬁx some J = J (4)∈ Jreg,h(E,π,Q,j,J (1),J (2),J (3)) and
writeb =CΦ rel
