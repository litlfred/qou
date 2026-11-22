---
doc_id: arxiv-math-0611504v1
doc_title: "QUANTUM HYPERBOLIC GEOMETRY"
section_id: sec-005-24-towards-geometric-specializations
section_title: "Towards geometric specializations"
section_number: 2.4
pages: 10-12
source_pdf: 0611504v1.pdf
source_sha256: a33d2771c873a97e
toc_source: outline
doc_brief: "Quantum hyperbolic geometry — 25 sections: Front matter; Introduction; Universal QHG"
duplicate_of: "agt-v7-n2-p13-s"
---
built ad hoc on the functional properties of the matrix dilogarithms.
In order to eventually get
specializations with a geometric content, such as QHFT, it is necessary to reﬁne more and more our
rough ﬂat/charged I-triangulations. In fact we have to impose some global constraints that would
be preserved by (possibly reﬁned) QHG isomorphisms. It is useful to recall at once some of these
reﬁnements, and related matter. We adopt the notations introduced above.
Deﬁnition 2.6. A triple T = (T, b, w) is an I-triangulation if at each edge e not contained in ∂T
we have the edge compatibility relation WT (e) = 1.
We say that T = (T, b, w, f) is a ﬂattened
I-triangulation (and f a global ﬂattening) if moreover LT (e) = 0.
It is easily seen that the collection of cross-ratio moduli of an I-triangulation T of a pseudomanifold
Z deﬁnes a PL pseudo developing map d : ˜Z →H
3, unique up to post composition with the action
of PSL(2, C), and a holonomy representation h : π1(Z) →PSL(2, C) such that d(γ(y)) = h(γ)(d(y))
for every γ ∈π1(Z), y ∈˜Z.
Our main tool for producing I-triangulations is the following idealization procedure:
Deﬁnition 2.7. Let T = (T, b, z) be a branched triangulation of a pseudomanifold Z equipped with
a PSL(2, C)-valued 1-cocycle z, where the cocycle relation is z(e0)z(e1)z(e2)−1 = 1 on a branched
triangle with edges e0, e1 and e2. A 3-simplex ∆of (T, b, z) with vertices x0, x1, x2, x3 is idealizable if
(12)
u0 = 0, u1 = z(x0x1)(0), u2 = z(x0x2)(0), u3 = z(x0x3)(0)
are four distinct points in C ⊂CP1 = ∂H
3.
The convex hull is a hyperbolic ideal tetrahedron
with ordered vertices, denoted (u0, u1, u2, u3). Let us give each edge e of ∆the cross-ratio modulus
w(e) ∈C\{0, 1} of the corresponding edge in (u0, u1, u2, u3), and put w = (w0, w1, w2) ∈(C\{0, 1})3.
We call (∆, b, w) the idealization of (∆, b, z). If all 3-simplices of (T, b, z) are idealizable we say that
TI = (T, b, w) is the idealization of T .
Note that the idealization includes the choice of a base point (ie. 0 in Deﬁnition 2.7; we make this
choice once for ever). The idealization of each single 3-simplex strongly depends on this choice, but
taking a diﬀerent base point is equivalent to conjugating the cocycle z. Not all branched triangulations
support idealizable cocycles (for example an ideal triangulation of a knot in S3 only supports the trivial
constant cocycle). However, when it exists we have:
Lemma 2.8. ([4], section 2.4) The idealization TI is an I-triangulation of Z.
The following fact will be important below (a version of it was implicitely used in [4]; see (3), Lemma
2.12 and §3.2 in that paper):
Lemma 2.9. The idealization TI is canonically ﬂattened by taking for each 3-simplex the log-branches
(with the notations of Deﬁnition 2.7):
l0 := log(u2 −u1) + log(u3) −log(u2) −log(u3 −u1)
l1 := log(u2) + log(u3 −u1) −log(u0) −log(u3 −u2) +
√
−1π
l2 := log(u3 −u2) + log(u0) −log(u3) −log(u2 −u1) −
√
−1π.
Moreover, replacing at each edge of TI the standard log with any other log determination still makes
it ﬂattened.
Proof. These expressions are just (corrected) signed sums of the standard logs of the edge vectors
in the cross-ratio moduli w0 = (u2 −u1)u3/u2(u3 −u1), w1 = u2(u3 −u1)/u0(u3 −u2) and w2 =
−(u3 −u2)u0/(u2 −u1)u3.
They clearly deﬁne triples of log-branches. The idealizations for two
distinct branchings with the same b-orientation are related by an element in PSL(2, C), that is, a
conformal transformation of CP 1. We deduce that triples (l0, l1, l2) are invariant under a change of
QUANTUM HYPERBOLIC GEOMETRY
11
branching, because the angle formed by any pair of vectors is preserved (for instance u2 −u1 and u2,
or u3 and u3 −u1). Then, the edge compatibility relations LT (e) = 0 follow easily by developing the
tetrahedra around e with branchings such that e = e0, similarly as for Lemma 2.8. For the last claim
we note that any log correction appears for each 3-simplex in two distinct lj, with opposite signs. ✷
Distinguished ﬂat/charged I-triangulations. Given an arbitrary non empty and properly embed-
ded tangle L in Z, we say that (T, H) and T = (T, H, b, w, f, c) are distinguished if H is a subcomplex
of the 1-skeleton of T isotopic to L and passing through all the vertices that are manifold points, and
containing no singular vertices (we say that H is Hamiltonian).
Deﬁnition 2.10. A distinguished I-triangulation T = (T, H, b, w, f, c) is ﬂat/charged if f is a global
ﬂattening, and
(13)
CT (e) =

0
2
if e ⊂H
if e ⊂T \ (H ∪∂T )
In such a case c is said a global charge.
The existence of global ﬂattenings of an arbitrary I-triangulation with empty boundary, and of global
charges (such that CT (e) = 2 at all edges e) on any topological ideal triangulation of an oriented 3-
manifold whose boundary consists of tori, was proved by Neumann in [25], section 9, and [24], section
6, respectively. This last result is easily adapted to the existence of global charges on distinguished
triangulations (T, H) (see [4], Theorem 4.7).
We have to reﬁne the QHG isomorphisms in order to deal with distinguished ﬂat/charged
I-
triangulations.
First we have to incorporate the Hamiltonian tangles into the bare moves.
Any
positive 2 →3 move T →T ′ naturally specializes to a move (T, H) →(T ′, H′); in fact H′ = H is
still Hamiltonian. For positive bubble moves, we assume that an edge e of H lies in the boundary
of the involved 2-simplex f; then e lies in the boundary of a unique 2-simplex f ′ of T ′ containing
the new vertex of T ′. We deﬁne the Hamiltonian subcomplex H′ of T ′ just by replacing e with the
other two edges of f ′. The inverse moves are deﬁned in the same way; in particular, for negative
3 →2 moves we require that the edge disappearing in T belongs to T ′ \ H′. The 2 ↔3 QHG transit
specializes verbatim. For the bubble transit we just impose that the marked edge e (see section 2.2)
coincides with the above edge of H. Thanks to (9) and (10) we see that distinguished ﬂat/charged
I-triangulations are closed under such reﬁned QHG transits.
Remark 2.11. The residue mod(2
√
−1πN) of the classical log-branches of a ﬂattened I-triangulation
are equivalently given by Nth roots w′(h) of the cross-ratio moduli w(h) such that w′(e1)w′(e2)w′(e3) =
1 at each 3-simplex and Q
h∈ǫ−1
T (e) w′(h)∗b = 1 at each edge, with the notations of (7). For level N
quantum log-branches of distinguished ﬂat/charged I-triangulations this is replaced with
w′(e1)w′(e2)w′(e3) = exp(−∗b
√
−1π/N)
and
Y
h∈ǫ−1
T (e)
w′(h)∗b =
 1
exp(−2
√
−1π/N)
if e ⊂H
otherwise.
Cohomological weights and structural facts. Given an I-triangulation T = (T, b, w) without
boundary, let T0 be the complement of an open cone neighborhood of each 0-simplex. This is a disjoint
union of triangulated closed oriented surfaces, the links of the vertices in T . To each ﬂattening f of
T a class γ(f) ∈H1(∂T0; C) is associated as follows. Represent any non zero integral 1-homology
class a of ∂T0 by “normal paths”, that is, a disjoint union of oriented essential simple closed curves
transverse to the triangulation and such that no component enters and exits from the same face of
a 2-simplex. Such a curve selects a vertex for each 2-simplex. The value γ(f)(a) is deﬁned as the
signed sum of the log-branches of the edges ending at the vertices selected by a. For each vertex v the
sign is ∗b if the path goes in the direction given by the orientation of ∂T0 as viewed from v, and −∗b
otherwise. Using the edge compatibility relations of Deﬁnition 2.6 it is easily checked that γ(f) does
not depend on the choice of normal path representative. If the holonomy of T is trivial or parabolic
about each (non manifold) point this class takes values in 2Z ([25], Proposition 5.2). Similarly we can
12
ST´EPHANE BASEILHAC1 AND RICCARDO BENEDETTI2
deﬁne γ2(f) ∈H1(T0; Z/2Z) by using normal paths in T0 and taking modulo 2 sum of the ﬂattenings
we meet along the paths. We call (γ(f), γ2(f)) the (cohomological) weight of f. These deﬁnitions
extend immediately to global charge, replacing log-branches with charges; then branchings are not
needed to compute the signed sums (ie. put ∗b = 1).
In [24], section 4 (see also [25], section 9), Neumann deﬁnes an integral chain complex J such that
global charges are deﬁned from cycles at level 3. The maps γ and γ2 above are well-deﬁned on the
third homology group H3(J ) and satisfy:
Theorem 2.12. ([24], Theorem 5.1) The sequence
0 →H3(J )
(γ2,γ)
−→H1(T0; Z/2Z) ⊕H1(∂T0; Z)
i∗−r
−→H1(∂T0; Z/2Z) →0
is exact, where r : H1(∂T0; Z) →H1(∂T0; Z/2Z) is the coeﬃcient map and i∗: H1(T0; Z/2Z) →
H1(∂T0; Z/2Z) is induced by the inclusion ∂T0 →T0.
In particular, any pair (h, k) ∈H1(T0; Z/2Z) × H1(∂T0; Z) with r(k) = i∗(h) is a weight for some
global charges. This fact extends to log-branches as follows. Assume that the holonomy of T restricted
to each component of ∂T0 takes values in a Borel subgroup of PSL(2, C), so that it ﬁxes some point in
∂H
3. Let γ′ be deﬁned as above, except that for each 3-simplex log-branches are taken with ﬂattenings
f0 = f1 = 0. It can be checked that γ′(a) is the logarithm of the derivative of the holonomy of a (a
similarity), up to multiples of 2
√
−1π. Then, any pair (h, k) ∈H1(T0; Z/2Z) × H1(∂T0; C) such that
(14)

(k −γ′)/
√
−1π ∈H1(∂T0; Z)
r((k −γ′)/
√
−1π) = i∗(h)
is a weight for some ﬂattening. For instance, when γ′(a) ∈2
√
−1πZ for all a the ﬁrst condition means
that k is integral.
Finally, the structure of the spaces of ﬂattenings and integral charges is given by Theorem 2.4 in
[24]. For each ﬁxed weight (h, k) they form an aﬃne space over an integral lattice. Generators have
the following combinatorial realization: for each 3-simplex in the star of an edge e, add +1 to the
ﬂat/charges of one of the two other pairs of opposite edges, and −1 for the other pair, so that the
total log-branches or charges stay equal everywhere. In particular, for ﬂattenings of an idealization TI
any generator is obtained by adding +1 to the log determination at some edge. Hence any ﬂattening
of TI inducing the weight of the canonical ﬂattening of Lemma 2.9 diﬀers from it as described in the
statement.
We note that the above reﬁned QHG isomorphisms preserve the weights (see eg. Lemma 4.12 in
[4]).
The diﬀerence in considering global ﬂattenings or charges with diﬀerent mod(2) weights in
H1(T0; Z/2Z) seems to carry not so essential information (see Theorem 5.4 and Remark 5.5). This
contrasts with boundary weights in H1(∂T0; Z), which play a key role in surgery formulae (see [25],
theorems 14.5 and 14.7, and section 6.2 below). We note that a process involving 2-handle surgery
allows to deﬁne explicit isomorphisms between lattices of ﬂat/charges with diﬀerent boundary weights
(see [25], section 11, p. 457).
