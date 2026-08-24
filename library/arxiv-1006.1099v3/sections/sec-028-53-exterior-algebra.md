---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS IV AN SMITH"
section_id: sec-028-53-exterior-algebra
section_title: "Exterior Algebra"
section_number: 5.3
pages: 56-59
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry bet ween a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
pentagram spheres of Figure 1. We orient the spheres equivariant ly for the cyclic symmetry
group which permutes them. Any two pentagram spheres are eithe r disjoint, meet transversely
in a point, or meet cleanly in a copy of S2g. The two generators of the Floer complex in the last
case have degrees of the same parity, so there is no diﬀerential. Th erefore as Z2-graded groups,
HF (Li,L j) can be computed equivalently in Z⁄=∞ or in Z (in either case one just recovers the
cohomology of the clean intersection). It follows that H(A) = ⊕i,jHF (Li,L j) is isomorphic,
as a Z2-graded complex vector space, to the space Λ( V ) ⋊ Z2g+1 obtained in Lemma 5.11, and
hence to the graded vector space describing F(Σ g) from Section 3.7. Our strategy now has three
components:
(1) Prove the exterior algebra structure on H(A) survives compactiﬁcation from Z⁄=∞ toZ;
(2) Prove that the “ﬁrst order term” (cubic term) of the A∞-structure is non-trivial;
(3) Infer that the A∞-structure on the exterior algebra is determined up to quasi-isomo rphism
by knowledge of this ﬁrst order term and of the Hochschild cohomolo gy.
Whilst the ﬁnal step is pure algebra, and bypasses having to make ex plicit computations with
holomorphic curves, the ﬁrst two require some control on holomor phic polygons. Recall from
Lemma 5.3 that for each of the individual pentagram spheres L, the Floer cohomology ring
HF (L,L )∼=H ∗(S2g+1) is undeformed in Z.
Lemma 5.14. For a pair of pentagram spheres L,L ′, the Floer products
HF (L′,L ′)⊗HF (L,L ′)−→HF (L,L ′)
HF (L′,L )⊗HF (L,L ′)−→HF (L,L ) (5.2)
are the same in Z as in Z⁄=∞.
Proof. In the ﬁrst case, the input element of HF (L′,L ′) is either the identity, in which case the
product is obviously determined, or has odd mod 2 degree. However ,HF (L,L ′) is concentrated
in a single mod 2 degree. Therefore, only µ2(1L′,·) can be non-trivial. The second case is
analogous. By Poincar´ e duality in Floer cohomology, the groups HF (L,L ′) and HF (L′,L ) are
concentrated in distinct mod 2 degrees. Therefore, the product can only be non-trivial into the
odd degree component of HF (L,L ), which is spanned by the fundamental class. This component
FLOER COHOMOLOGY AND PENCILS OF QUADRICS 57
is determined by the non-degeneracy of Poincar´ e duality, via its tr ace, hence will be independent
of the compactiﬁcation to Z. □
To compute the algebra structure on H(A) (taken inside Z) completely, we must therefore
understand Floer products amongst 3 diﬀerent Lagrangians. Sinc e 3 distinct pentagram spheres
are pairwise transverse or cleanly intersecting, holomorphic pearls reduce to Morse-Bott Floer
trajectories, in which we count holomorphic triangles which may have non-trivial cycle constraints
(or attached ﬂowlines) at a corner mapping to a clean intersection. Lemma 5.12 implies that such
a Floer disk projects to a holomorphic triangle in P1 with boundary on the pentagram (but in
principle holomorphic triangles in Z might project onto P1). There are only two distinct possible
boundary patterns for the boundary of the triangle in P1, modulo the rotation action by Z2g+1
(in either picture any of the three vertices might be the output of t he Floer product). These are
depicted in Figure 6 in the case g = 2.
Figure 6. Possible holomorphic triangles
In Z⁄=∞, the generators of the exterior algebra are given by ( Z2g+1 orbits of) the idempotent
summands of the Floer cohomology of the clean intersection sphere s (lying over interval vertices)
and the isolated external vertices. Lemma 5.11 implies that we can ch oose Z2-gradings which
reproduce those of F(Σ g). From [93] and [29], or by direct computation, these are as follows:
(1) HF ∗(Lγ,L e−2iπ/(2g+1)γ)∼=H ∗(S2g)[1] is concentrated in odd degree;
(2) HF ∗(Lγ,L e−4iπ/(2g+1γ)∼= C is concentrated in even degree.
To clarify, for the small holomorphic triangle on the left of Figure 6 wit h the anticlockwise
boundary orientation that it inherits as a holomorphic disk in C, the clean intersections at the
internal vertices will be concentrated in odd degree when viewed as inputs, and will have output
the even degree external vertex. (Thus, the output is even deg ree read anticlockwise, meaning
viewed as a morphism going from the upper edge to the lower.) In Z⁄=∞ (and in the aﬃne
hyperelliptic curve) there are rigid holomorphic triangles projecting to these small triangles, and
their cyclically rotated versions, which deﬁne the exterior algebra s tructure. The existence of
these triangles determines the mod 2 degrees of the Floer generat ors of the algebra H(A).
Lemma 5.15. No rigid holomorphic triangle in Z has boundary which projects to the second
triangle of Figure 6.
Proof. The mod 2 gradings of the vertices preclude existence of any rigid tr iangle, recalling that
µ2 has degree zero. For instance, on the right of Figure 6, if the exte rnal vertices are the inputs,
they each have odd degree, but the internal vertex as an output also has odd degree. □
Return to the small triangle of Figure 6. Label the Lagrangians on t hat triangle: L′′ is the
vertical side, L the lower side and L′ the upper side. Let p∈HF odd(L,L ′) be the Floer generator
at the external vertex, viewed as an input.
58 IV AN SMITH
Lemma 5.16. The product µ2
F(Z)(p,·) : HF odd(L′′,L )→HF ev(L′′,L ′) is an isomorphism.
Proof. Consider the Lagrange surgery L#L′ of L and L′ at p, as depicted by the curved path
in Figure 7. This surgery is equivalently given by taking the Dehn twist o f L′ about L. The
surgery is Hamiltonian isotopic, via matching spheres, to a sphere L#L′ which is disjoint from
L′′, namely that deﬁned by the basic path between the leftmost two ve rtices of Figure 6.
Figure 7. Lagrange surgery at a vertex
The exact triangle for monotone Dehn twists implies there is an exact triangle in F(Z)
L /d47/d47L′
/d124/d124/d121/d121/d121/d121/d121/d121/d121/d121
L#L′
[1]
/d98/d98/d68/d68/d68/d68/d68/d68/d68/d68
(5.3)
This gives a long exact sequence of Floer cohomology groups in Z
···→ HF (L′′,L )→HF (L′′,L ′)→HF (L′′,L #L′)→···
Since the terms HF (L′′,L #L′) = 0, we deduce µ2(p,·) : HF (L′′,L )
∼
−→ HF (L′′,L ′) is an
isomorphism. □
Non-vanishing of µ2(p,·) a posteriori implies that the algebraic number of triangles in Z with
the boundary conditions on the left of Figure 6 is non-zero. The sam e argument proves that right
multiplication by p also deﬁnes an isomorphism
HF odd(L′,L ′′)
µ2
F(Z)(·,p)
−−−−−−→HF ev(L,L ′′). (5.4)
Poincar´ e duality in Floer cohomology is graded commutative [92, Sec tion 12e]. Together with
associativity of Floer cup-product, Lemma 5.14 and Lemma 5.16 toge ther imply that H(A) is
still given by an exterior algebra after compactiﬁcation from Z⁄=∞ toZ, compare to [93, Section
10]. Explicitly, in the notation of that paper, the generators of Λ 1 arise from p = ξ3 and the
two idempotents ξ1,ξ 2 of HF odd(L′′,L ), or rather their Z2g+1-orbits. The generators of Λ 2 are
the Poincar´ e dual cycles ¯ξ3, ¯ξ1, ¯ξ2, and the unit respectively fundamental class of the pentagram
spheres give the generators 1 ∈ Λ 0 and q∈ Λ 3. Lemma 5.16 and its cousin (5.4) implies that
ξ2·ξ3 = ¯ξ1 andξ3·ξ1 = ¯ξ2, for suitably chosen signs of the generators, whilst Lemma 5.14 implie s
that ξi· ¯ξi =q =− ¯ξi·ξi. These relations deﬁne an exterior algebra.
Corollary 5.17. If g≥ 2, the Floer cohomology algebra generated by the pentagram sp heres in
Z is Λ( C3) ⋊ Z2g+1 (graded mod 2).
FLOER COHOMOLOGY AND PENCILS OF QUADRICS 59
Both the curve C and the relative quadric Z deﬁne A∞-structures on the exterior algebra
which can be viewed as deformations of the particular quasi-isomorp hism type of Lemma 5.11,
with the deformation parameter counting intersections of holomor phic curves with the ﬁbre over
∞∈ P1. Since the relevant deformation space is large, we appeal to more a lgebraic methods to
pin down the A∞-structure.
Remark 5.18. By comparing to [93] and [29], one sees that two of the generators o f the exterior
algebra arise from the two idempotent summands of HF (V,V )∼= H ∗(S0), where V ⊂ Q is the
Lagrangian vanishing cycle in a quadric ﬁbre of Z. These play an essentially symmetric role.
Indeed, returning to Remark 4.11, there is a holomorphic involution τ of Z which reverses the
sign of the ﬁrst projective homogeneous co-ordinate x0, and acts ﬁbrewise over P1, in particular
ﬁxes the nodes in the singular ﬁbres. τ is one lift of the hyperelliptic involution on Σ to a
symplectomorphism of Z. The monotone K¨ ahler form, which is pulled back from P2g+1× P1,
is τ -invariant, which means that the associated parallel transport ma ps along matching paths
are τ -invariant, so τ preserves the Lagrangian pentagram spheres. In particular, τ preserves
the vanishing cycle V = L′′∩L in the ﬁbre Q deﬁned by the corresponding matching paths.
Being a lift of the hyperelliptic involution, τ reverses orientation on V (and so on L,L ′′), by
compatibility of the symplectic group representations on the Rieman n surface and the associated
(2, 2)-intersection and hence relative quadric, cf. [84].
Working with equivariant almost complex structures as in Lemma 5.12, and appealing to
Remark 5.13, we can assume that the A∞-structure on Z is equivariant with respect to τ . Note
that if e and f denote generators for HF (Q,Q ) ∼= HF (L′′,L ) above, then the idempotent
summands are (e±f )/2, and the fundamental class of Q is the diﬀerence between the idempotents.
Since the involutionτ acts by an orientation-reversing automorphism of the Lagrangian vanishing
cycle it sends f↦→−f and exchanges the two idempotents. Therefore τ -equivariance amounts
to saying that A(Z) is equivariant under changing f↦→−f .
