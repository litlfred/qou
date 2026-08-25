---
doc_id: arxiv-math-0305275v1
doc_title: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds"
section_id: sec-001-the-straightening
section_title: "The straightening"
section_number: null
pages: 6-9
source_pdf: 0305275v1.pdf
source_sha256: 9b356a9d716a0d3e
doc_brief: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds — Let W be a compact manifold and let ρ be a representation of its fundamental group into PSL(2 , C)."
---
A straightening of a pseudo-developing map D is a map that agrees with
D on the ideal points and that maps each tetrahedron to a straight o ne.
The straightening is useful to calculate the hyperbolic volume assoc iated to
a pseudo-developing map (see Section 4). A particular case is when t he
6
manifold M is complete hyperbolic, because in this case the straightening
descends to a map from M to itself. Here we prove that such a map is onto.
Let ∆ ⊂ H3 be an oriented geodesic ideal tetrahedron. Since ∆ is the
convex hull of its vertices, then the Isom +(H3)-class of ∆ is completely de-
termined by the Isom +(H3)-class of the oriented set of its vertices (the ori-
entation of the vertices is deﬁned up to the action of A4). Such a class is
completely determined by a non-real complex number called modulus, up to
a three-to-one ambiguity. Such an ambiguity can be avoided by choo sing a
preferred pair of opposite edges of ∆ (see [BP], [F], [PP], [PW] [Th1]). W e
extend the notion of modulus to the set of ﬂat tetrahedra, that is to those
whose vertices are distinct and lie on a hyperbolic plane of H3, by accepting
real moduli diﬀerent from 0 and 1. We want to extend this deﬁnition a lso
to the degenerate tetrahedra, i.e. to those having two ore more coincident
vertices. Unfortunately, for such a tetrahedron it is not possible to encode
its isometry class in a complex number. Let us agree that when we use a
modulus in {0, 1, ∞} for ∆, we mean that ∆ is a degenerate tetrahedron and
that the modulus encodes the complete information on the isometry class of
∆, i.e. who are the coincident vertices of ∆.
Deﬁnition 3.1 Let ∆ k be the standard k-simplex. Let ϕ : ∆ k → H
n
be
a continuous map that maps the 0-skeleton of ∆ k to ∂Hn. Let Q be the
Euclidean convex hull of the ϕ-image of the vertices of ∆ k, made in a disc
model of Hn. Let ψ : ∆ k →Q be the only simplicial map that agrees with ϕ
on the 0-skeleton.
We say that the map ϕ is standard if there exist two homeomorphisms
η : Im(ϕ) →Q and β : ∆ k → ∆ k such that
η ◦ϕ ◦β =ψ.
We say that a foliation F of ∆ k is standard if there exists a standard map
ϕ : ∆ k → H
n
such that F = {ϕ−1(x)}.
Remark 3.2 For any standard map ϕ the dimension of F = {ϕ−1(x)} de-
pends only on the ϕ-image of the 0-skeleton.
Remark 3.3 It is not hard to show that for a map ϕ to be standard does
not depend on the disc model we use. In other words ϕ is standard if and
only if γϕ is standard for any isometry γ.
Let M be an ideally triangulated manifold, ρ : π1(M) →Isom+(H3) be
a representation, and Dρ be a pseudo-developing map for ρ. Let ∆ be a
tetrahedron of τ and ~∆ be one of its lifts. The vertices of ~∆ are ideal points,
7
so their images under Dρ lie in ∂H3. The map Dρ determines a modulus
for ~∆ simply by considering the convex hull of the image of its vertices (th e
orientation is the one induced by M). Note that since Dρ is equivariant, then
it deﬁnes a modulus for ∆. For each face σ of ∆ we call Str Dρ (~σ), or simply
Str(~σ), the straight simplex obtained as the convex hull of the Dρ-image of
the vertices of ~σ.
Deﬁnition 3.4 (Straightening) A straightening of Dρ is a continuous,
piecewise smooth, ρ-equivariant map Str(Dρ) : ˆ~M → H
3
such that:
1. For each simplex σ of the triangulation, Str( Dρ) maps ~σ to Str( ~σ).
2. The restriction of Str( Dρ) to any simplex σ is standard.
3. For each cusp N~p = P~p × [0, ∞] there exists c ∈ R such that Str( Dρ)
restricted to P~p × [c, ∞] is a cone-map.
Lemma 3.5 Let M be an ideally triangulated manifold. Let ρ be a represen-
tation ρ :π1(M) →Isom+(H3) and Dρ be a pseudo-developing map. Then a
straightening Str(Dρ) ofDρ exists. Moreover Str(Dρ) is always equivariantly
homotopic to Dρ via a homotopy that ﬁxes the ideal points.
Proof. A straightening of Dρ can be constructed with the same techniques of
Lemma 2.7. Regarding the homotopy, since Dρ maps non-ideal points to the
interior of H3, then one can use a geodesic ﬂow with the time-parameter in
[0, ∞] (for example the convex combination of Deﬁnition 4.11) to constru ct
a homotopy with the required properties.
✷
Remark 3.6 A straightening in general is not a pseudo-developing map in
our setting, because it can map some point of ~M to ∂H3. However, if there
are no degenerate tetrahedra, then a straightening is also a pseu do-developing
map, and the homotopy between Dρ and Str(Dρ) can be made coherently
with the cone structure of the cusps, i.e. in such a way that the intermediate
maps along the homotopy between Dρ and Str(Dρ) have the cone property
on the cusps.
When M has a complete hyperbolic structure of ﬁnite volume, there is
a natural notion of straightening of the ideal triangulation. Namely , choose
the arc-length as the cone parameter on the cusps of M and consider H3 as
the universal cover of M. Then choose ρ as the holonomy of the hyperbolic
structure of M; the identity map of H3 clearly is a pseudo-developing map
for ρ. A natural straightening map is a straightening of the identity.
8
Proposition 3.7 Let M be an ideally triangulated manifold equipped with a
complete, ﬁnite-volume hyperbolic structure. Then any nat ural straightening
map projects to a map Str : ˆM → ˆM which is onto. Moreover Str(M) ⊃M.
Proof. It is easy to see that ˆ~M = ˆH3 naturally embeds into H
3
and that the
ideal points lie on ∂H3. Since the straightening is equivariant, then it projects
to a map Str : ˆM → ˆM . Moreover, Str ﬁxes the ideal points. We prove that
Str is onto. One can easily prove that H3( ˆM ; Z) ∼= H3(M,∂ M ; Z) ∼= Z. So
we can deﬁne the degree of a map f : ˆM → ˆM by
f∗([ ˆM ]) = deg(f ) · [ ˆM ]
where [ ˆM ] is the generator of H3( ˆM ; Z) induced by the orientation of M.
Now note that by Lemma 3.5 the natural straightening is homotopic t o the
identity via an equivariant homotopy. Because of equivariance, the homotopy
projects to a homotopy between Str and the identity. It follows th at Str ∗ and
id∗ coincide on H∗( ˆM ; Z), so deg(Str) = deg(id) = 1. Now suppose that Str
is not onto and let x be a point in ˆM outside its image. If we consider Str as
a map from ˆM to ˆM \ {x}, we get Str ∗([ ˆM]) = 0 ∈ H3( ˆM \ {x}; Z) simply
because H3( ˆM \ {x}; Z) = 0. Then Str ∗([ ˆM ]) is a boundary in ˆM \ {x},
consequently it is a boundary also in ˆM. It follows that Str ∗([ ˆM ]) = 0. This
implies deg(Str) = 0, that is a contradiction.
The last assertion follows because Str is onto and ﬁxes the ideal poin ts.
✷
