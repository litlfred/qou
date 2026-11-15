---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-084-chain-complexes-and-homology-theory
section_title: "Chain complexes and homology theory"
section_number: null
pages: 480-486
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
Instead of working only with cycles of integration, we develop homology in a
more general setting. This approach better illustrates underlying structure, and
allows us to reuse results in diﬀerent contexts. We therefore introduce the fol-
462
B.1 Chain complexes and homology theory
463
lowing abstract deﬁnitions, which generalize some of the properties discussed
above.
(i) A chain complex is a collection C = {Cn : n = 0, 1, 2, . . .} of com-
plex vector spaces, not necessarily ﬁnite dimensional, together with a
boundary operator ∂, which for all n is a linear map ∂n from the space
of n-chains Cn to the space of (n −1)-chains Cn−1 that satisﬁes ∂2 = 0
(meaning ∂n ◦∂n+1 = 0 for all n, so that “a boundary has no boundary””).
By deﬁnition, ∂= 0 on C0.
(ii) The vector space of n-cycles Zn ⊆Cn of a chain complex C is the kernel
of ∂n, and the group Bn ⊂Cn of n-boundaries of C is the image of ∂n+1.
(iii) The nth homology group of C is the vector space quotient
Hn(C) := Zn/Bn .
The notation H∗(C) is used to refer collectively to Hn(C) for all n. Cycles in
the same equivalence class are called homologous.
Remark. Because we work with complex vector spaces, H∗(C) is sometimes
called homology with coeﬃcients in C to distinguish it from the analogous
construction with integer coeﬃcients. While the theory with integer coeﬃ-
cients is richer, taking coeﬃcients in a ﬁeld better suits the purposes of com-
puting integrals. With integer coeﬃcients, the spaces of chains, cycles, and
boundaries are Z-modules, and their quotients are abelian groups, hence “ho-
mology group” rather than “homology vector space.”
To discuss the homology of a manifold, we must deﬁne an appropriate chain
complex. One natural candidate is the chain complex deﬁned by smooth chains
together with the boundary map discussed in Section A.3 of Appendix A. For
many purposes, however, it is convenient to relax our smoothness condition.
If M is any Hausdorﬀtopological space then a singular n-simplex in M is a
continuous (not necessarily smooth) map σ : ∆n →M from the standard n-
simplex ∆n to M, and a singular n-chain in M is a complex linear combination
of singular n-simplices in M. Just as for smooth chains, we may use the natural
ordering of the faces of ∆n to deﬁne a canonical boundary map through (A.3.1),
taking a singular n-simplex to a singular (n−1)-simplex and extending linearly
to singular chains. It is a foundational result in homology theory that the ho-
mology of a manifold is unchanged whether one studies smooth or singular
chains.
Proposition B.1. Let M be a diﬀerentiable manifold, let C be the chain com-
plex whose chains are linear combinations of singular simplices on M, and
let C′ be the chain complex whose chains are linear combinations of smooth
464
Algebraic topology
simplices on M. Then for any n ∈N the homology groups Hn(C) and Hn(C′)
are isomorphic.
Proof
See [Eil47].
□
We write C(M) for the chain complex deﬁned by the singular n-chains in M.
The homology group Hn(C(M)) is written Hn(M) and called the nth singular
homology group of M. One can think of the rank of the homology group
Hn(M) – i.e., the minimum size of a generating set of the group – as indicating
how many unique cycles in M don’t bound anything.
Example B.2. The rank of H1(M) represents the number of nonequivalent
circles that can be drawn on M without bounding something in M. The rank
of H1(M) for a connected space M is thus zero if M is simply connected,
however the converse does not hold. Homology with coeﬃcients in C cannot
detect the presence of a cycle γ such that γ does not bound anything but k times
γ does (homology with integer coeﬃcients is more discerning but typically
more complicated to compute).
◁
Topological invariance of homology
The ﬁrst crucial property of homology is that it is a topological invariant. A
topological map (or simply map) between two topological spaces is a continu-
ous function between them, while a chain map between two chain complexes
is a function between them that commutes with their boundary operators. More
precisely, if (A, ∂A) and (B, ∂B) are two chain complexes then a chain map be-
tween them can be considered to be a collection of functions f = ( f0, f1, . . . )
with fn : An →Bn mapping from the n-chains of A to the n-chains of B, such
that ∂B
n ◦fn = fn−1 ◦∂A
n for all n.
A topological map from X to Y induces a chain map from the singular chain
complex of X to the singular chain complex of Y. A map f : A →B between
chain complexes in turn induces a homomorphism f∗on homology groups
by applying the map to representatives for the equivalence classes of cycles
modulo boundaries. Both of these induced maps are functorial.
Proposition B.3. If the topological spaces X and Y are homeomorphic then
the singular homology groups Hn(X) and Hn(Y) are isomorphic for all n.
Proof
A homeomorphism between topological spaces is a topological map
whose inverse is also a topological map. Hence, a homeomorphism between
two spaces induces an isomorphism between the homology groups of the spaces.
□
B.1 Chain complexes and homology theory
465
Homology groups are preserved under more than just homeomorphism. If
X and Y are topological spaces then two maps f, g : X →Y are said to be
homotopic maps if there is a continuous map H : X × [0, 1] →Y, called a
homotopy, such that H(x, 0) = f(x) and H(x, 1) = g(x) for all x. A topological
map f : X →Y is called a homotopy equivalence if there is a topological map
g : Y →X such that f ◦g is homotopic to the identity on Y and g ◦f is
homotopic to the identity on X. If f : X →Y is a homotopy equivalence then
we say that X and Y are homotopic spaces.
We claim that homotopic maps induce equal maps on homology, hence
homotopy equivalent spaces have naturally identical homology. To see this
one proves, on the chain level, that a homotopy equivalence between topo-
logical spaces induces a chain homotopy equivalence between the singular
chain complexes, which in turn induces an isomorphism between the homol-
ogy groups.
Proposition B.4. If a topological map f : X →Y is a homotopy equivalence
then the singular homology groups Hn(X) and Hn(Y) are isomorphic for all n,
with f∗inducing one such isomorphism.
Proof
See Theorem 2.10 and Corollary 2.11 of [Hat02].
□
Exercise B.1. Explain why a homeomorphism is always a homotopy equiva-
lence.
Suppose H : X × [0, 1] →X is a homotopy with H(x, 0) = x for all X, and
Y ⊆X is a subspace such that H(x, 1) ∈Y for all x. If H(y, t) ∈Y for all y and
t (so that X ends in Y and Y stays in Y) then we call H a weak deformation
retract and say Y is a weak deformation retract of X. If H(y, t) = y for all y and
t then we call H a strong deformation retract (or simply deformation retract)
and say that Y is a strong deformation retract of X.
Exercise B.2. Prove that if Y is a weak deformation retract of X then X and Y
are homotopy equivalent.
Remark. Imagine looking at a space X that starts deforming in a continuous
manner, with points allowed to collide and pass through each other, ultimately
ending up in a diﬀerent space Y. The space Y can be smaller, even a single
point, but Exercise B.2 implies that as long as every point that starts in Y stays
in Y then the homology of X is isomorphic to the homology of Y.
Various homologies and their equivalence
Working with the homology of smooth chains is nice because they are what we
integrate over, but this approach has some disadvantages. Most prominently,
466
Algebraic topology
the large amount of freedom involved means the collection of chains on a man-
ifold is huge (not having a countable basis) even though the homology groups
are ﬁnite dimensional. Because of this we introduce new types of spaces with
more structure.
• A cell complex or CW-complex X is a Hausdorﬀspace deﬁned using a spe-
ciﬁc inductive procedure. Let X0 be a discrete collection of points and for
any n ≥0 let Xn be the quotient space, with quotient topology, deﬁned by the
disjoint union Xn−1 ⊔α ∆n
α of Xn−1 with a collection of standard n-simplices
∆n
α, where we identify each x ∈∂∆n
α with some φα(x) ∈Xn−1 using gluing
maps φα : ∂∆n
α →Xn−1. The set Xn is the n-skeleton of X, and contains its
k-cells ∆k
α for k ≤n. We consider ﬁnite dimensional cell complexes, mean-
ing X = Xn for some natural number n and the smallest such n is called the
dimension of the cell complex X. Each simplex ∆n
α corresponds to a map
σn
α : ∆n
α →X deﬁned by embedding ∆n
α into Xn−1 ⊔α ∆n
α and then taking the
quotient by the gluing maps.
• A ∆-complex is a cell complex X where the gluing map φα for any simplex
∆n
α maps each (n−1)-dimensional face F of ∆n
α homeomorphically to one of
the (n −1)-simplices in X, preserving the ordering of vertices and agreeing
with the previously deﬁned gluing map φF on ∂F. A ∆-complex X may be
viewed as a collection of maps σα : ∆nα →X such that the restriction of
σα to the interior of ∆nα is injective, each point of X lies in exactly one such
restriction, and the restriction of σα to a face of ∆nα is another one of the
maps σβ : ∆nα−1 →X in the collection deﬁning X.
• A simplicial complex is a ∆-complex where each gluing map is injective
(so that distinct faces in the boundary of each simplex are glued to distinct
lower-dimensional simplices) and each n-simplex is uniquely determined by
its vertices. A simplicial complex X may be viewed as a set of simplices such
that every face of a simplex in X is also in X and the nonempty intersection
of any two simplices ∆1, ∆2 ∈X is a face of both ∆1 and ∆2.
We say that a space S is represented by a cell complex, ∆-complex, or
simplicial complex X if S and X are homeomorphic. The representation of a
space by a simplicial complex is called a triangulation of the space. Figure B.1
shows some examples representing a sphere and a circle.
The CW approximation theorem [Hat02, Proposition 4.13] states that any
Hausdorﬀspace X can be approximated by a cell complex ˜X meaning, among
other things, that X and ˜X have the same singular homology groups. We are
most interested in algebraic varieties, or their complements, which are exam-
ples of semi-algebraic sets and can therefore be triangulated [BPR03, Theo-
rem 5.43].
B.1 Chain complexes and homology theory
467
Figure B.1 Top left: The sphere S 2 can be represented as a cell complex with one
0-cell and one 2-cell whose boundary is mapped to the 0-cell, but this is not a
∆-complex. Top right: A representation of S 2 as a ∆-complex containing three 0-
cells, three 1-cells, and two 2-cells. Bottom left: The circle S 1 can be represented
as a ∆-complex with one 0-cell and one 1-cell whose boundary is identiﬁed with
the 0-cell, but this is not a triangulation. Bottom right: A triangulation of S 1 with
three 0-cells and three 1-cells.
The diﬃculties with singular homology for general topological spaces still
arise for ∆and simplicial complexes. However, the additional structure present
allows us to deﬁne a more rigid notion of homology. If X is a simplicial com-
plex then the simplicial homology of X is the homology deﬁned by the chain
complex C whose n-chains are complex linear combinations of the n-simplices
in X, with the boundary map again deﬁned by (A.3.1). Simplicial homology is
crucial for calculation, due to the following result.
Proposition B.5. If X is a simplicial complex then the nth singular homol-
ogy group of X is isomorphic to the nth simplicial homology group of X. The
simplicial homology groups of X are algorithmically computable.
Proof
See [Hat02, Theorem 2.27] for the statement on the equivalence of
the homologies, and [Mun84, Theorem 11.5] for an algorithm to determine
simplicial homology by representing the linear boundary maps of X as matrices
and computing their Smith normal forms.
□
Among other corollaries, Proposition B.5 implies that a space which can
be represented by a ∆-complex with a ﬁnite number of simplices has ﬁnitely
generated homology groups. Although simplicial complexes have more struc-
ture than ∆-complexes, it can often be more eﬃcient to represent a space as a
∆-complex compared to representing it as a simplicial complex.
Example B.6. We compute the homology of the circle S 1 by representing it
as the ∆-complex X with one point X0 = {p} and one line segment X1 = {ℓ}
with both endpoints of ℓglued at p. The 0-chains in this representation are
468
Algebraic topology
the complex multiples of p, while the 1-chains are the complex multiples of ℓ.
Any 0-chain is trivially a cycle, and the only boundary is ∂ℓ= p −p = 0, so
H0(S 1) = C. This computation also shows that every 1-chain is a cycle, and
there are no non-trivial boundaries because there are no 2-cycles, so H1(S 1) =
C while Hk(S 1) = 0 for k ≥2.
◁
Exercise B.3. Compute the homology of the circle by triangulating it, veri-
fying you get the same result as Example B.6. Compute the homology of the
sphere S 2 using similar techniques.
