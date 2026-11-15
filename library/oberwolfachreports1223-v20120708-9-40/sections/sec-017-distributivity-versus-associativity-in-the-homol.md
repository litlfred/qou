---
doc_id: oberwolfachreports1223-v20120708-9-40
doc_title: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by"
section_id: sec-017-distributivity-versus-associativity-in-the-homol
section_title: "Distributivity versus associativity in the homology theory of algebraic structures"
section_number: null
pages: 33-36
source_pdf: OberwolfachReports1223_v20120708_9_40.pdf
source_sha256: 94f82cfc185955ba
toc_source: inferred
doc_brief: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by — This meeting concentrated on topological invariants in low di"
---
structures
J´ozef H. Przytycki
1. Introduction
While homology theory of associative structures, such as groups and rings,
has been extensively studied in the past beginning with the work of Hurewicz,
Hopf, Eilenberg, and Hochschild, the non-associative structures, such as racks or
quandles, were neglected until recently.
The distributive structures have been
studied for a long time and even C.S. Peirce in 1880 emphasized the importance
of (right) self-distributivity in algebraic structures. However, homology for such
universal algebras was introduced only between 1990 and 1995 by Fenn, Rourke,
and Sanderson. We develops theory in the historical context and propose a general
framework to study homology of distributive structures. We outline potential rela-
tions to Khovanov homology and categoriﬁcation, via Yang-Baxter operators. We
use here the fact that Yang-Baxter equation can be thought of as a generalization
of self-distributivity.
34
Oberwolfach Report 28/2012
1.1. Invariants of arc colorings. Consider a link diagram D, say
, and a ﬁ-
nite set X. We may deﬁne a diagram invariant as the number of colorings of arcs of
D by elements of X, colX(D). Even such a naive deﬁnition leads to a link invariant
colX(L) = minD∈LcolX(D), where D ∈L means that D is a diagram of L.1. More
sensible approach would start with magma (X; ∗) with the coloring convention
*
a  b
a
b
b
. Again, let for a ﬁnite X, colX(D) denote the number of colorings of arcs
of D by elements of X, according to the above convention at every crossing. We
can deﬁne an oriented link invariant by considering colX(L) = minD∈LcolX(D).
Alternatively, we can minimize colX(D) over minimal crossing diagrams of L only.
Such an invariant would be very diﬃcult to compute so it is better to look for
properties of (X; ∗) so that colX(D) is invariant under Reidemeister moves: R1
(
) gives idempotency relation a ∗a = a. R2 (
) forces ∗to be an invertible
operation and the third move is illustrated in detail below:
*
(a   c)
*
(a   c)
R 3
a
b
c
c
*
*
(b   c)
b   c
*
a
c
c
a    b
(a    b)
b   c
*   c
*
*
*
b
The magma (X; ∗) satisfying all three conditions is called a quandle, the last
two – a rack, and only the last condition – a shelf or RDS. Thus, if (X; ∗) is a
quandle then colX(D) is a link invariant. We can do more (after Carter-Kamada-
Saito). We can sum over all crossings pairs ±(a, b) according to the convention
a
b
*
a     b
−(a,b) 
a
b
*
a     b
(a,b) 
; the investigation of invariance of . ±(a, b) under Reidemeis-
ter moves was a hint toward construction of (co)homology of quandles.
Let us now compare homology for associative structures (semigroups) with that
for distributive structures (shelves).
1.2. Group homology of a semigroup. Let (X, ∗) be a semigroup. We deﬁne
a chain complex {Cn, ∂n} as follows: Cn(X) = ZXn and ∂n = .n
i=0(−1)idi
(alternating sum of face maps). Where d0(x1, ..., xn) = (x2, ..., xn),
di(x1, ..., xn) = (x1, ..., xi−1, xi ∗xi+1, xi+2, ..., xn), for 0 < i < n and
dn(x1, ..., xn) = (x1, ..., xn−1).
We check that didj = dj−1di for i < j. The sequence of groups Cn (n ≥0) with
maps di : Ci →Ci−1, which satisﬁes equalities didj = dj−1di for 0 ≤i < j ≤n is
called a presimplicial group (or presimplicial Z-module).
1.3. Hochschild homology of a semigroup. Let (X; ∗) be a semigroup. We
deﬁne a Hochschild chain complex {Cn, ∂n} as follows Cn(X) = ZXn+1 and the
1One can say that it is a nonsense but an invariant nontrivial: colX(L) = |X|2cr(L)+t(L),
where cr(L) is the crossing number of L and t(L) the number of trivial components in L.
Invariants in Low-Dimensional Topology and Knot Theory
35
Hochschild boundary ∂n = .n
i=0(−1)idi, where di(x0, ..., xn) = (x0, ..., xi−1, xi ∗
xi+1, xi+2, ..., xn), for 0 ≤i < n and
dn(x0, ..., xn) = (xn ∗x0, ..., xn−1).
Again, (Cn, di) is a presimplicial module. If (X, ∗) is a monoid, one can deﬁne
n+1 homomorphisms si : Cn →Cn+1, called degeneracy maps, by si(x0, ..., xn) =
(x0, ..., xi, 1, xi+1, ..., xn) (similarly, in the case of group homology of a monoid, we
put, si(x1, ..., xn) = (x1, ..., xi, 1, xi+1, ..., xn)). We check that in both cases the
following conditions hold:
(1)
didj = dj−1di for i < j,
(2)
sisj = sj+1si,
0 ≤i ≤j ≤n,
(3)
disj =
/
sj−1di
if i < j,
sjdi−1
if i > j + 1,
(4)
disi = di+1si = IdCn.
(Cn, di, si) satisfying conditions (1)-(4) above is called a simplicial module (Z-
module in our case). If we replace (4) by a weaker condition disi = di+1si we deal
with a weak simplicial module, the concept useful in the theory of homology of
distributive structures (spindles or quandles).
1.4. Homology of distributive structures. Recall that a shelf (X; ∗) is a set
X with a right self-distributive binary operation ∗: X × X →X (i.e. (a ∗b) ∗c =
(a ∗c) ∗(b ∗c)). We deﬁne a (one-term) distributive chain complex Cn, ∂n) as
follows: Cn = ZXn+1 and the boundary operation ∂(∗)
n
= .n
i=0(−1)idi, where
di(x0, ..., xn) = (x0 ∗xi, ..., xi−1 ∗xi, xi+1, ..., xn).
(Cn, di) is a presimplicial module. If we deﬁne si : Cn →Cn+1 by si(x0, ..., xn) =
(x0, ..., xi−1, xi, xi, xi+1, ..., xn), then (Cn, di, si) satisﬁes conditions (1)-(3) of sim-
plicial module, and if (X; ∗) is a spindle (a ∗a = a), then (Cn, di, si) is a weak
simplicial module and degenerate homology (not necessarily trivial) can be deﬁned.
If (X; ∗) is a rack then the complex (C(∗)
n , ∂(∗)) is acyclic, but in the general case
of a shelf or spindle homology can be nontrivial with nontrivial free and torsion
part (joint work with A. Crans, K. Putyra and A. Sikora [1, 5, 6]).
1.5. Multi-term distributive homology. One generalize one term distributive
homology as follows. Let X be a set and Bin(X) the set of all binary operations
on X (in fact a monoid with composition a ∗1 ∗2b = (a ∗1 b) ∗2 b and a ∗0 b =
a).
We say that S ⊂Bin(X) is a distributive set if for any pair ∗1, ∗2 ∈S
we have (a ∗1 b) ∗2 c = (a ∗2 c) ∗1 (b ∗2 c). If (∗1, ..., ∗k) is a distributive set, we
deﬁne a multiterm chain complex by taking any linear combination of ∂(∗i), that is
(Cn, ∂(a1,...,ak)) is deﬁned by Cn = ZXn+1 and ∂(a1,...,ak) = a1∂(∗1) + ...+ ak∂(∗k),
where ai ∈Z.
We computed with K. Putyra [5] various multiterm homology,
including that for ﬁnite distributive lattices (including Boolean algebras). Also
multiterm homology based on the distributive embedding of G to Bin(G), given
by Greg Mezera, where g →∗g with a ∗g b = ab−1gb is of great interest.
36
Oberwolfach Report 28/2012
1.6. From distributivity homology to Yang-Baxter homology. For a given
Yang-Baxter operator we attempt to ﬁnd presimplicial module using graphical
presentation of the (co)presimplicial category ∆op
pre, from which homology will
be derived.
The ﬁgure below illustrate various graphical interpretation of the
generating morphism di of a presimplicial category ∆op
pre. They are loosely related
to homology of set-theoretical Yang-Baxter equation of Carter-Kamada-Saito and
Fenn, and to homology of Yang-Baxter equation of Eisermann [2, 3]. We should
also acknowledge stimulating observations by Ivan Dynnikov.
i
Figure 1; Various interpretation of the graphical face map di
References
[1] A. Crans, J. H. Przytycki, K. Putyra, Torsion in one term distributive homology and clas-
sifying space, in preparation.
[2] M. Eisermann, Yang-Baxter deformations of quandles and racks, Algebr. Geom. Topol. 5
(2005), 537–562. e-print: http://front.math.ucdavis.edu/0409.5202 .
[3] M. Eisermann, Yang-Baxter deformations and rack cohomology, submitted TAMS, e-print:
http://front.math.ucdavis.edu/0808.0108.
[4] J. H. Przytycki, Distributivity versus associativity in the homology theory of algebraic struc-
tures, Demonstratio Math. 44 (2011), no. 4, 821-867.
e-print: http://front.math.ucdavis.edu/1109.4850.
[5] J. H. Przytycki, K. Putyra, Homology of distributive lattices,
e-print: http://arxiv.org/abs/1111.4772.
[6] J. H. Przytycki, A. S. Sikora, Distributive products and their homology, preprint, May, 2011,
e-print: http://front.math.ucdavis.edu/1105.3700.
