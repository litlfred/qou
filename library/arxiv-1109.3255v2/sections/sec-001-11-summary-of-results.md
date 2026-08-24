---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE"
section_id: sec-001-11-summary-of-results
section_title: "Summary of results"
section_number: 1.1
pages: 1-5
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
1.2. Context and related work 5
1.3. Acknowledgments 10
2. The ﬁber of W and its tropicalization 11
2.1. Torus ﬁbrations on CP2 \D and its mirror 11
2.2. The topology of the map W 16
2.3. Tropicalization in a singular aﬃne structure 17
3. Symplectic constructions 19
3.1. Symplectic monodromy associated to a Hessian metric 20
3.2. Focus-focus singularities and Lefschetz singularities 22
3.3. Lagrangians ﬁbered over paths 25
4. A degeneration of holomorphic triangles 32
4.1. Triangles as sections 32
4.2. Extending the ﬁber 37
4.3. Degenerating the ﬁbration 38
4.4. Horizontal sections over a disk with one critical value 40
4.5. Polygons with ﬁxed conformal structure 44
4.6. Signs 52
5. A tropical count of triangles 54
5.1. Tropical polygons 54
Date: Revised 2013–12–19.
1
2 JAMES PASCALEFF
5.2. Tropical triangles for ( CP2,D ) 58
6. Parallel monodromy–invariant directions 60
6.1. Symplectic forms 60
6.2. Lagrangian submanifolds 61
6.3. Holomorphic and tropical triangles 62
7. Mirrors to divisor complements 63
7.1. Algebraic motivation 64
7.2. Wrapping 64
7.3. Continuation maps and products 68
References 70
1. Introduction
This article is concerned with a case of mirror symmetry relating the a lgebraic
geometry of a Fano manifold to the symplectic geometry of a Landau –Ginzburg model.
The Fano manifold is the projective plane CP2 with homogeneous coordinates x,y,z ,
and additionally we choose as anticanonical divisor D =C ∪L, the union of a conic
C = {xz −y2} and a line L = {y = 0} (a binodal cubic curve). According to Auroux
[7], the mirror of this pair ( CP2,D ) is the Landau–Ginzburg model ( X ∨,W )
X ∨ = {(u,v ) ∈ C2 |uv ⁄= 1}, W =u + e−Λv2
uv − 1
(1)
The function W is known as the superpotential. This example is interesting in the
context of the Strominger-Yau-Zaslow picture of mirror symmetr y [42] in terms of
dual torus ﬁbrations, since the spaces CP2 \D and X ∨ admit special Lagrangian
torus ﬁbrations with a singularity. The presence of singularities in th e torus ﬁbration
is known to make the mirror duality vastly more complicated, but in this article we
develop techniques to deal with it in the above case (and other case s with similar
properties, see §6).
1.1. Summary of results. The piece of symplectic geometry in the Landau–Ginzburg
model (X ∨,W ) we study is the Floer cohomology of Lagrangian submanifolds, while
on the mirror side CP2 we consider the cohomology of the coherent sheaves OCP2(d).
We construct a symplectic manifold X(B), that serves as our symplectic model for
X ∨, and a collection of Lagrangian submanifolds {L(d)}d∈Z in X(B) that is mirror
to the collection {OCP2(d)}d∈Z. The constructions of X(B) and L(d) are based on the
SYZ picture of mirror symmetry in terms of torus ﬁbrations and aﬃn e manifolds, and
also use the theory of Lefschetz ﬁbrations. The manifold X(B) carries two ﬁbrations:
one is a ﬁbration over a singular aﬃne manifold B whose ﬁbers are Lagrangian tori,
while the other is a Lefschetz ﬁbration whose ﬁbers are symplectic s ubmanifolds. See
section 3 for the deﬁnitions.
To state the main result, let An =H 0(CP2, OCP2(n)), and choose a basis x,y,z of
A1. Thus A =⨁ ∞
n=0An ∼= C[x,y,z ] is the homogeneous coordinate ring of CP2. The
Floer cohomology of two Lagrangian submanifolds L,L ′ is a Z-graded C-vector space
denoted HF ∗(L,L ′).
MIRROR OF THE PROJECTIVE PLANE 3
Theorem 1.1. For each d ∈ Z and n ≥ 0, there is an isomorphism
(2) ψd,n :HF 0(L(d),L (d +n)) →An
carrying the basis of intersection points L(d) ∩L(d +n) to the basis of An consisting
of the polynomials of the form
(3) {xa(xz −y2)iyn−a−2i} ∪ {za(xz −y2)iyn−a−2i}
(where we require a ≥ 0,i ≥ 0,n −a − 2i ≥ 0). The system of isomorphisms ψd,n
intertwines the Floer triangle product
(4)
µ2 :HF 0(L(d +n),L (d +n +m)) ⊗HF 0(L(d),L (d +n)) →HF 0(L(d),L (d +n +m))
and the product of polynomials Am ⊗An →An+m.
Let us remark on the formulation of the theorem. From the constr uction of the
LagrangiansL(d) it is easy to count the number of intersection points and show that
the map ψd,n exists as an isomorphism of vector spaces. Such a map exists for an y
choice of basis of An. The last statement equating Floer triangle products and the
products of polynomials is the nontrivial bit that ties the choices tog ether and shows
that we have chosen the right basis for An.
This basis we obtain is related to the choice of divisor D = C ∪L, as it consists
of monomials in the deﬁning section p = xz −y2 of C, the deﬁning section y of L,
and the homogeneous variables x orz (but not both x andz in the same monomial).
Another point of view has to do with the fact that the ring of functio ns on CP2 \D
is a cluster algebra [12]. There are two triples of homogeneous forms on CP2, (x,p,y )
and (z,p,y ), which are related by the so-called exchange relation xz = y2 +p, and
our basis consists of sections that are monomials in either triple.
For the proof of this theorem, the majority of our technical eﬀor ts are aimed at
computing the Floer triangle product. This occupies section 4. At th is point in the
argument, the picture of X(B) as a Lefschetz ﬁbration is the focus. The holomorphic
triangles we need to ﬁnd can be represented as sections of this Lef schetz ﬁbration.
The problem of counting sections of Lefschetz ﬁbrations has a TQF T-type structure,
developed by Seidel. This structure, where one breaks a given prob lem into simpler
ones by degenerating the base of the Lefschetz ﬁbration, provid es the basis of our
technique.
There are several variations on Theorem 1.1 that are accessible us ing the same
holomorphic curve analysis. We consider the complement of (some co mponents of)
the anticanonical divisor in CP2, and on the Landau–Ginzburg side, we must change
the superpotential W and consider a certain form of wrapped Floer cohomology. Our
techniques allow us to treat three cases:
(1) the mirror of ( CP2 \L,C \ (C ∩L)),
(2) the mirror of ( CP2 \C,L \ (L ∩C)), and
(3) the mirror of ( CP2 \ (C ∪L), ∅).
In each case the mirror space is the same manifold X ∨, and the Lagrangians mirror
to line bundles are the same L(d), but in each case there is a diﬀerent prescrip-
tion for wrapping the Lagrangian submanifolds. The ﬁrst two cases require “par-
tially wrapped” Floer cohomology, while the third uses the more stand ard “fully
wrapped” Floer cohomology. In each case we denote wrapped Floer cohomology by
4 JAMES PASCALEFF
HW ∗(L1,L 2). Let U = CP2 \ L, CP2 \C, or CP2 \ (C ∪L), and let An(U) =
H 0(U, OU (n)). The space An(U) consists of rational functions in the variables x,y,z
that are regular on U and have degree n. The wrapped version of Theorem 1.1 is as
follows (see §7)
Theorem 1.2. Ford ∈ Z and n ≥ 0, there is an isomorphism
(5) ψd,n :HW 0(L(d),L (d +n)) →An(U)
carrying a certain distinguished basis of HW 0(L(d),L (d +n)) to the basis of An(U)
consisting of rational functions of the form
(6) {xa(xz −y2)iyn−a−2i} ∪ {za(xz −y2)iyn−a−2i}
where the exponents a andi are restricted to those values which actually give elements
ofAn(U). The system of isomorphisms ψd,n intertwines the Floer triangle product on
wrapped Floer cohomology and the product of rational functi ons Am(U) ⊗An(U) →
An+m(U).
While our holomorphic triangle counts use the structure of a Lefsch etz ﬁbration on
X(B), we can also study the geometry of the X(B) as a Lagrangian torus ﬁbration
over the base aﬃne manifold B. One of the expectations of SYZ philosophy is that
much of the geometry of the space X(B) can be seen tropically, in terms of the
geometry of the aﬃne base B.
In fact, this is how we arrive at the construction of the manifold X(B). In section
2, we construct a tropicalization of the ﬁber of the superpotentia lW −1(c) over a large
positive real value, with respect to a torus ﬁbration on the manifold X ∨ with a single
singularity. This gives a tropical curve in the base of our torus ﬁbra tion. It bounds a
compact region B in the base, which agrees with the aﬃne base of the torus ﬁbration
on CP2 \D. The purpose of this section is to motivate the use of the singular aﬃ ne
manifold B as the basis for our main symplectic constructions in section 3.
We also are able to verify a conjectural tropical description of Floe r cohomology in
the cases we study. This description comes from a recent proposa l of Abouzaid, Gross
and Siebert for a tropical Fukaya category associated to a singula r aﬃne manifold.
The Lagrangian submanifolds are taken to be sections of the torus ﬁbration, but all
we see of them tropically are their intersection points, which map to f ractional integral
points of the aﬃne manifold B. The Floer triangle product corresponds to a “tropical
triangle product” counting certain tropical curves in B joining the fractional integral
points. Since we do not say anything about degenerating holomorph ic polygons to
tropical ones, we merely verify the equivalence by matching bases a nd computing on
both sides. See section 5 for the precise deﬁnitions of the terms.
Theorem 1.3. There is a bijection between the basis of intersection point s L(d) ∩
L(d +n) forHF 0(L(d),L (d +n)) and the set of ( 1
n )-integral points of the aﬃne man-
ifoldB. Under this bijection, the counts of pseudo-holomorphic tr iangles contributing
to the Floer triangle product are equal to counts of tropical curves in B joining ( 1
n)-
integral points.
The techniques developed in this article apply to a larger but still rest ricted class
of 2–dimensional singular aﬃne manifolds, where the main restriction is that all sin-
gularities have parallel monodromy-invariant directions . The generalization to these
types of manifolds is discussed in 6.
MIRROR OF THE PROJECTIVE PLANE 5
