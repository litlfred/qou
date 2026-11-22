---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS"
section_id: sec-034-54-the-cubic-term
section_title: "The cubic term"
section_number: 5.4
pages: 59-62
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
toc_source: outline
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry between a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
only Z2-graded, as in Section 3.5 one can impose a Z-grading by considering the ﬁltrations on
Floer complexes coming from intersections of holomorphic polygons with the polar divisor ∆of
a meromorphic 1-form. We will choose the divisor ∆disjoint from the pentagram Lagrangians,
at which point one can achieve transversality with perturbations of the almost complex structure
and Floer equation supported away from ∆. The reason this is useful is that the term ∆·[im(u)]
in Equation 3.10 is necessarily positive, by positivity of intersections of holomorphic curves with
holomorphic divisors. If one knows something about the absolute indices ιη(xj) of intersection
points, this can be a non-trivial constraint on which polygons exist. As an illustration, we will
extract slightly more from the argument of Lemma 5.16, to give at least partial information on
the cubic term µ3
A(Z) of the A∞-structure.
Choose a ﬁbrewise hyperplane section of Z – the pullback of a general hyperplane H ⊂P2g+1,
which now plays the role of Href from Section 4.5 – whose complement is an aﬃne quadric
bundle at least over a large open set in C containing the ﬁnite set of pentagram matching paths.
(Globally, any choice of hyperplane H ⊂P2g+1 will fail to be transverse to a ﬁnite number of the
quadrics in the pencil, and its complement will not globally be a T ∗S2g-bundle over P1; but one
can put the singular ﬁbres near inﬁnity, and they will make no diﬀerence to the computations
undertaken below.) Up to symplectomorphism, one can identify an open set in this T ∗S2g-bundle
with an open set in a suitable family of Milnor ﬁbres
W =
(
(x0, . . . , x2g, y)

 h(x0) +
X
i>0
x2
i = y2
)
⊂C2g+2
60
IVAN SMITH
as studied by Khovanov and Seidel in [52], taking h(z) = z(z2g+1 −1) to obtain a family of aﬃne
quadrics with nodal singular ﬁbres at the origin and the (2g + 1)-st roots of unity. Since this
open subset of Z̸=∞is simply-connected, as are the Lagrangians, we know a priori that gradings,
which come from trivialisations of K⊗2 and associated phase functions, are unique.
Lemma 5.19. The Z-gradings on the pentagram algebra inside W are Z2g+1-equivariant.
Proof. For any M = g−1(0) ⊂Cn+1, there is a holomorphic n-form η on M given by
detC(dgx ∧. . .)|T M
(5.5)
for which the phase of an oriented Lagrangian n-plane with orthonormal basis ⟨e1, . . . , en⟩is given
by detC(dgx ∧e1 . . . ∧en)2. Starting from here, [52, Equation 6.5] shows that for a Lagrangian
Lγ ⊂W associated to a matching path γ(t), the phase function is
t 7→h(γ(t))2g−1γ′(t)2
(5.6)
where h(z) = z(z2g+1 −1) and the phase is O(2g + 1)-invariant so depends only on the base co-
ordinate. (5.6) extends continuously over the two points of the sphere Lγ ⊂W ⊂Z̸=∞lying over
the endpoints of γ, and is invariant under rotation by exp(2iπ/(2g + 1)), so the phase functions
for the diﬀerent pentagram spheres Lj are identical under natural parametrisations. Absolute
gradings in Floer theory are determined by local geometry near the intersection point and the
associated phase function; here, both are invariant under rotation.
□
Remark 5.20 (Notation). Recall in Figure 7 the three Lagrangians are L′′ (vertical), L (lower)
and L′ (upper). We will write e, f and p for three Floer generators (or their Z2g+1-orbits) arising
as follows: p is the external vertex of the pentagram, graded in odd degree as the generator
of HF(L, L′) (as in the proof of Lemma 5.16); and e, f are the generators of H∗(S2g)[1] =
HF(L′′, L) (which are also, by equivariance, the odd degree generators of HF(L′, L′′), cf. op.
cit.). We will write ¯e, ¯f for the Poincar´e dual generators, and ιη(·) = | · | for the absolute index
of any generator. We declare |f| = |e| + 2g, so e arises from the cohomological identity of the
S2g-clean intersection and f from the fundamental class.
We now take a holomorphic volume form ηZ on Z which has poles of order g along Href and
simple poles along the ﬁbre Z∞, recalling that c1(Z) = (2g + 2)H −E = 2gH + [Fibre]. Up to
homotopy, the induced volume form on the subset W ⊂Z̸=∞agrees with that from (5.5), so the
corresponding gradings are Z2g+1-invariant. Note that although the Z2-graded A∞-structure on
A(Z) can be taken to be invariant under the involution of Remark 5.18, the Z-gradings need not
be, since ∆is not invariant. Poincar´e duality in Floer cohomology implies that if x ∈CF(L, L′)
is a transverse intersection, then
ιη(x) = (2g + 1) −ιη(¯x)
where ¯x ∈CF(L′, L) is the morphism viewed in the opposite direction.
The proof of Lemma 5.16 relied only on the fact that the Lagrange surgery L#L′ was Hamil-
tonian isotopic to a Lagrangian sphere disjoint from L′′. This is true inside the aﬃne open subset
W, so the holomorphic triangles whose existence was implied by Lemma 5.16 actually exist in
W, in particular have trivial intersection number with the divisor ∆. This provides a constraint
on the absolute gradings of the Floer generators, via Equation 3.10:
|e| + |p| and |f| + |p| ∈{|¯e|, | ¯f|} = {2g + 1 −|e|, 1 −|e|}
where the two equations come from the fact that µ2(p, ·) was an isomorphism in Lemma 5.16, so
of rank 2. On the other hand, we also know
|f| = |e| + 2g
FLOER COHOMOLOGY AND PENCILS OF QUADRICS
61
The two previous equations imply 2|e| + |p| = 1. Now we consider cubic terms:
µ3(e, e, p);
µ3(e, f, p);
µ3(f, f, p).
(5.7)
We are interested in the coeﬃcient of the identity 1L in these cubic terms, which are pieces of
the product
µ3 : CF ∗(L′′, L) ⊗CF ∗(L′, L′′) ⊗CF ∗(L, L′) −→CF(L, L)[−1]
Consider ﬁrst working in Z̸=∞. One can import some information about the higher A∞-structure
on A(Z̸=∞), using Lemma 5.11 and our knowledge of A(C̸=∞) arising from the results of Seidel
and Eﬁmov described in Section 3.7. Recall from (3.12) that the cubic term of an A∞-structure
extending a given product deﬁnes a Hochschild cocycle; exponentiated inﬁnitesimal gauge trans-
formations
α 7→α −∂γ + [γ, α] + 1
2[γ, [γ, α] −∂γ] + · · ·
by elements γ ∈CC0 with vanishing linear term γ = (γi)i≥2, so preserving the product, preserve
the cohomology class Φ1(α3) ∈HH∗of α3, which is accordingly well-deﬁned, cf. [93, Eqn. (5.6)].
In this vein, we record one implication of Seidel and Eﬁmov’s work.
Lemma 5.21. In Z̸=∞, the product µ3(e + f, e −f, p) contains 1L with non-zero coeﬃcient,
whilst µ3(e + f, e + f, p) is trivial.
This follows from Equation 3.17; in that notation, the ﬁrst statement of the Lemma reﬂects
the non-trivial cubic term v1v2v3 whilst the second reﬂects the vanishing of the terms v2
i v3,
i = 1, 2. We now combine Lemma 5.21 with the Z-grading considerations discussed before (5.7).
Lemma 3.15 implies that intersections with Href respectively Z∞contribute 4g respectively 2
to the Maslov index of the corresponding holomorphic polygon.
Indeed, for a rigid (virtual
dimension zero) polygon contributing to µk, with inputs xj and output the identity element
1L ∈HF 0(L, L), Lemma 3.15 implies
X
j
|xj| + 2 −k = ∆· [im(u)] = 4g im(u) · Href + 2 im(u) · Z∞.
(5.8)
We now put together the following pieces of information:
• By Remark 5.18, the A∞structures on Z̸=∞and Z can be taken invariant under an
involution which preserves p and e but sends f 7→−f, so µ3(e, f, p) = 0 in both cases;
• Lemma 5.21 then implies µ3̸
=∞(e, e, p)̸ = µ3̸
=∞(f, f, p) when computed in Z̸=∞. By Equa-
tion 5.8, and the discussion before (5.7), the holomorphic polygons which contribute to
these expressions are necessarily disjoint from ∆, for µ3̸
=∞(e, e, p), respectively meet ∆
exactly once, for µ3̸
=∞(f, f, p).
Now consider the term µ3
A(Z)(e, e, p). Equation 5.8 and the relation 2|e| + |p| = 1 implies that
no holomorphic polygon contributing to this product can meet either Href or Z∞, in particular
its value does not change under compactiﬁcation from Z̸=∞to Z. There are in principle new
holomorphic polygons which contribute to µ3
A(Z)(f, f, p), given by adding a Chern number zero
sphere in homology class 2gR −L to a disk living in Z̸=∞. (Since our total space is mono-
tone, such a Chern number zero sphere cannot itself be represented by a holomorphic curve, so
these additional polygons do not arise from broken conﬁgurations by gluing on sphere bubble
components.) However, we can deduce:
Corollary 5.22. The coeﬃcient of 1L in exactly one of
µ3
A(Z)(e + f, e −f, p)
and
µ3
A(Z)(e + f, e + f, p)
is non-zero.
62
IVAN SMITH
Proof. This is immediate from the preceding discussion. Either the coeﬃcient of 1L in µ3(f, f, p)
does not change on compactiﬁcation, in which case we inherit the non-vanishing of Lemma 5.21,
or it does change, but since the analogous coeﬃcient didn’t change in µ3(e, e, p), that would
imply the second outcome.
□
Remark 5.23. It is possible to compute the absolute grading of A(Z) using the theory of “bigraded
curves” developed in [52], given a computer to plot phase functions along matching paths (and a
blackboard to extract the gradings from those plots). Knowledge of A(Z̸=∞) gives many further
a priori constraints on the bigrading; for instance, (3.17) implies µ2g+1̸
=∞(p, . . . , p)̸ = 0, which
together with Lemma 3.15 shows that |p| = 4gk −1 for some k ≥1, etc.
