---
doc_id: cuspshapes
doc_title: "CUSP SHAPE AND TUNNEL NUMBER"
section_id: sec-003-3-spaces-of-hyperbolic-structures
section_title: "Spaces of hyperbolic structures"
section_number: 3
pages: 6-8
source_pdf: CuspShapes.pdf
source_sha256: 01db19e63193e6ae
doc_brief: "CUSP SHAPE AND TUNNEL NUMBER — We show that the set of cusp shapes of hyperbolic tunnel number one manifolds is dense in the Teichm¨ uller space of the torus."
---
Deﬁne the representation space of C with parabolic locusT to be the space
R(C,T ) ={representationsρ: π1(C)→ PSL(2, C)|g∈π1(T )⇒ρ(g) is parabolic}.
The space AH(C,T ) of hyperbolic structures on C is the set
AH(C,T ) ={ρ∈R (C,T )|ρ is discrete and faithful}/∼
where the equivalence∼ is given by ρ∼ρ′ if they are conjugate representations.
The topology on AH(C,T ) is given by algebraic convergence, as follows.
Deﬁnition 3.1. A sequence of representations {ρn} in AH(C,T ) converges alge-
braically to a representation ρ if the sequence{ρn(g)} converges to ρ(g) for every
g∈ π1(C). Here we regard ρn(g) as a point in the manifold PSL(2, C), and so
{ρn(g)} converges to ρ(g) in the sense of convergence of points in PSL(2 , C).
Suppose{ρn} converges to ρ algebraically. Algebraic convergence does not re-
veal much geometric information. For example the sequence of quotient mani-
folds H3/ρn(π1(C)) does not necessarily converge to the limiting quotient manifold
H3/ρ(π1(C)); see [35, 7, 22]. A stronger notion is geometric convergence.
Deﬁnition 3.2. A sequence of subgroups Γn of PSL(2, C) converges geometrically
to a subgroup Γ if:
(1) For each ζ∈ Γ, there exists ζn∈ Γn such that{ζn} converges to ζ.
(2) If ζnj∈ Γnj, and{ζnj} converges to ζ, then ζ∈ Γ.
Geometric convergence of discrete groups implies convergence of their quotient
spaces; see e.g. [ 9, Theorem 3.2.9]. Work of Jorgensen and Marden [ 18] implies
that if a sequence {Γn} converges to a discrete group Γ algebraically, then there
is a subsequence converging geometrically to a group Γ ′, with Γ ≤ Γ′. Thus the
quotient manifoldM = H3/Γ of the algebraic limit is a cover of the quotient manifold
M′ = H3/Γ′ of the geometric limit.
Deﬁnition 3.3. A hyperbolic structure is geometrically ﬁnite if H3/Γ admits a
ﬁnite-sided, convex fundamental domain.
For example, the hyperbolic structures of Lemmas 2.5 and 2.6 are geometrically
ﬁnite. The fundamental domain consists of the isometric spheres described in the
lemmas as well as a vertical fundamental domain. These are ﬁnite sided.
Deﬁnition 3.4. A hyperbolic structure on C is minimally parabolic if Γ has no
non-peripheral parabolic subgroups. Equivalently, in the case of C(1;n + 1), a
hyerbolic structure is minimally parabolic if it has no rank-1 parabolic subgroup
aside from subgroups of ⟨ρ(α),ρ (β)⟩.
CUSP SHAPE AND TUNNEL NUMBER 7
The hyperbolic structures of Lemmas 2.5 and 2.6 are not minimally parabolic.
Each of the representatives ρ(γi) has been chosen to be parabolic, but γi is not
an element of the free abelian rank-2 subgroup π1(T ) of π1(C). Thus ρ givesC a
structure which is geometrically ﬁnite but not minimally parabolic.
Denote the space of minimally parabolic, geometrically ﬁnite structures on C
by MP(C,T ). The boundary of the space MP(C,T ) consists of equivalence classes
of representations which give C structures that are geometrically ﬁnite but not
minimally parabolic, or structures that are geometrically inﬁnite (not geometrically
ﬁnite). The Density theorem ([ 30], [32]) implies that every structure on the boundary
of MP(C,T ) is the algebraic limit of a convergent sequence in MP(C,T ), and that
the closure of MP(C,T ) is AH(C,T ). We call structures that are geometrically ﬁnite
but not minimally parabolic pinched structures.
Note that Lemma 2.5 and Lemma 2.6 give examples of pinched structures.
Deﬁnition 3.5. A maximally pinched structure is a pinched structure ρ for which
the boundary of the convex core of H3/ρ(π1(C)) consists of 3-punctured spheres.
Remark 3.6. The structures of Deﬁnition 3.5 are typically called maximal cusps in
the literature on Kleinian groups, because the boundary of each 3-punctured sphere
is a rank-1 cusp (e.g. [ 27, 10]). Unfortunately, in the case of manifolds with torus
boundary components, a maximal cusp refers to something else entirely: a maximally
embedded horoball neighborhood of all rank-2 cusps of the manifold. Because our
maximally pinched manifolds will also have a maximal horoball neighborhood of
the torus boundary component, we rename the type of structures. We decided on
pinched because such a structure pinches a maximal collection of curves on the higher
genus boundary component into parabolics, with length 0.
Maximally pinched structures are useful because of the following result due to
Canary, Culler, Hersonsky, and Shalen [10], extending work of McMullen [27].
Theorem 3.7. Maximally pinched structures are dense on the boundary ∂ MP(C,T )
of the space MP(C,T ). □
Lemma 3.8. Let [T ] be any point in the Teichm¨ uller space of the torus. For any
n≥ 1, there exists a pinched structure ρ on C(1;n + 1) such that ρ gives C(1;n + 1)
cusp shape [T ].
Proof. The representation ρ: π1(C)→ PSL(2, C) is deﬁned as in Lemma 2.5 and in
Lemma 2.6, choosing complex numbers a and b to give the desired shape, as follows:
(i) Complex numbers a and b are chosen to be linearly independent over R with
|a| > 5 and|b| > 5, and|a| and|b| large enough that the set of isometric
spheres{I(ρ(γ±1
j ))} is disjoint from its translates under ρ(α) and ρ(β).
(ii) Also, [∂H/⟨ρ(α),ρ (β)⟩] = [T ] for H a horoball about inﬁnity.
Condition (i) ensures that a and b satisfy the hypothesis of Lemma 2.6. Hence, ρ
gives a pinched structure. Condition (ii) ensures that the shape on the rank-2 cusp
of C equipped with this structure is [ T ]. □
Recall that the Teichm¨ uller space of the torus is the space of similarity classes
of (marked) ﬂat metrics on the torus. It is isometric to the upper half plane
H2 ={z∈ C| Im(z)> 0}, equipped with the hyperbolic metric; see for example [ 25].
8 VINH DANG AND JESSICA S. PURCELL
γ1 γ−1
1
βγ1
αγ1
Figure 3. Left: A fundamental region for a maximally pinched
structure on C(1; 2). Right: A fundamental region for its convex core.
Lemma 3.9. Let [T ] be any point in the Teichm¨ uller space of the torus. For any
ϵ> 0, there exists a maximally pinched structure ρ′ on C(1;n + 1) such that the cusp
shape of ρ′ is ϵ/2-close to [T ].
Proof. Let ρ be a pinched structure on C with cusp shape [T ] as in Lemma 3.8. By
Theorem 3.7, maximally pinched structures are dense on the boundary ∂ MP(C,T ) of
the space MP(C,T ). Therefore, the fact that ρ∈∂MP (C) implies that there exists
a sequence{ρn} of maximally pinched structures on C which converges algebraically
to ρ. Thus, there exists a maximally pinched structure ρ′ that is ϵ/2-close to ρ. In
particular, ρ′(α) and ρ′(β) are ϵ/2-close to ρ(α) and ρ(β) because the convergence is
algebraic. As a result, ρ′ givesC a cusp shape that is ϵ/2-close to [T ]. □
Lemma 3.9 is only an existence result, and unfortunately gives no explicit structure
or examples to work with. Finding examples of maximally pinched structures is
non-trivial. To ﬁnd such a structure on C(1; 2), a choice of three appropriate curves
on ∂+C(1; 2) must be pinched, which amounts to ﬁnding values of ρ(α), ρ(β) and
ρ(γ1) for which certain products of generators have trace ±2, namely those products
that represent the boundary curves. For example, one maximally pinched structure
with cusp shape [T ] = [−1/4 +i
√
3/4] is given by the representation
ρ(α) =
(
1 4
0 1
)
, ρ (β) =
(
1 −1 +i
√
3
0 1
)
, ρ (γ1) =
(
2 −1
1 0
)
.
This maximally pinched structure has a fundamental region in H3 lying over the
parallelogram and hemispheres on C shown on the left of Figure 3; the group elements
labeling the circles in that ﬁgure are short for isometric spheres I(ρ(γ1)), I(ρ(γ−1
1 )),
etc. To obtain a fundamental region for the convex core, cut out four additional
hemispheres that are “dual,” enclosing each curvilinear triangle in the original
fundamental region as shown on the right of Figure 3. Note that face identiﬁcations
glue boundaries of those curvilinear triangles in such a way that the convex core has
boundary consisting of two totally geodesic 3-punctured spheres. Note also that this
example has particularly simple geometry. There are (countably inﬁnitely many)
more complicated structures, with varied cusp shapes. More discussion can be found
in [13, Section 4.3]; see also [21].
