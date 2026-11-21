---
doc_id: oberwolfachreports1223-v20120708-9-40
doc_title: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by"
section_id: sec-021-on-a-cohomology-theory-for-colored-tangles
section_title: "On a cohomology theory for colored tangles"
section_number: null
pages: 43-46
source_pdf: OberwolfachReports1223_v20120708_9_40.pdf
source_sha256: 94f82cfc185955ba
toc_source: inferred
doc_brief: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by — This meeting concentrated on topological invariants in low di"
---
On a cohomology theory for colored tangles
Carmen Caprau
1. Introduction
In [6] Khovanov constructed a cochain complex associated to an oriented framed
link whose components are labelled by irreducible representations of Uq(sl(2)).
The graded Euler characteristic of the homology of this complex is the colored
Jones polynomial. Speciﬁcally, [6] provides a categoriﬁcation of the colored Jones
polynomial by interpreting the deﬁning formula for the polynomial
Jn(K) =
⌊n
2 ⌋
!
i=0
(−1)i
0
n −i
i
1
J(Kn−2i),
where Kj is the j-parallel cable of the knot K, as the Euler characteristic of a
complex whose objects require the original Khovanov homology [5] of the cablings
Kn−2i, for i = 0, . . . , ⌊n
2 ⌋.
This construction works over Z2, due to the sign
ambiguity in the functoriality property of the original Khovanov homology.
A similar approach to constructing homology theories for colored links was pro-
posed by Mackaay and Turner [7], and independently by Beliakova and Wehrli [2],
by exploring ideas of Bar-Natan [1]. In both constructions one needs to juggle with
the sign ambiguity in the functoriality property of the employed Khovanov-type
homology theories.
The goal of this talk is two-folded. First we improve the existing categoriﬁca-
tions of the colored Jones polynomial by giving a clean deﬁnition of the colored
invariant of a knot.
For that, we employ the universal sl(2) foam cohomology
theory using foams (seamed 2-cobordisms) constructed by the author in [4] (see
also [3]).
Moreover, we construct a local colored cohomology theory, in that it
is built with colored tangles in mind, and which “composes” well under tangle
composition, leading to eﬃcient computations of the colored invariants of a knot.
The construction in [4] is deﬁned over the ring R = Z[i, a, h], and it involves
webs and dotted foams modulo local relations. The resulting Khovanov-type coho-
mology theory is properly functorial with respect to tangle or link cobordisms with
no sign indeterminacy. Denote by Kof /h the homotopy category of complexes over
dotted foams modulo certain local relations. Given a diagram D of an oriented
tangle T , the author constructed a formal complex [D] whose isomorphism class
in Kof /h is an invariant of T . If C ⊂R3 × [0, 1] is a tangle cobordism between
tangles T1 and T2, then there is an induced map [T1] →[T2], well-deﬁned under
ambient isotopy of C (rel. boundary). The category Kof /h has a natural struc-
ture of an oriented planar algebra, and [ · ] is a planar algebra morphism from the
planar algebra of oriented tangles modulo the three Reidemeister moves to Kof /h.
44 Oberwolfach Report 28/2012

2. COLORED TANGLE-COHOMOLOGY

We restrict our attention to oriented framed tangles T without closed compo-
nents, whose strands are colored by the same natural number n, or equivalently,
by the (n + 1)-dimensional irreducible representation of quantum sl(2). Let D be
a diagram of T whose blackboard framing agrees with the given framing of T. The

k
neighbors from n dots placed on a line, such that each dot appears in at most one
pair. A dot-row s is a set of n dots on a line in which some adjacent dots are
paired. Denote by p(s) the number of pairs in s.

Let [, be the oriented graph whose vertices are all possible dot-rows s corre-
sponding to n. Two vertices s and s’ of [, are connected by an edge e: s > 8’
if and only if all pairs in s are pairs in s’, and p(s’) = p(s) +1. The height of a
vertex s is equal to p(s), and the edges are oriented towards increasing heights.
In Figure 1 we show such a graph for n = 5. To a dot-row s attach the cable dia-
gram D, := D"~?P(), formed by taking the (n — 2p(s))-parallel cable of D. When
forming an m-parallel cable of D we enumerate the strands in a cross-section of
D™ from left to right by 1 to m, and orient the parallel cable-strands such that
adjacent strands receive opposite orientations, where we give strand 1 the original
orientation of D. To an edge e: s > s’ we attach the cobordism S, : D, > Dy
given by contracting the neighboring strands in D, corresponding to the pair in
s’ but not in s. That is, S, is the cobordism with two inputs and no output for
these two strands, and the identity otherwise (see Figure 1).

binomial coefficient ( n ) equals the number of ways of selecting k pairs of

wee ee eeeee eoecve eeeee

ae ee

FicurE 1. Graph I's and cobordism S,

We sprinkle the edges of the resulting graph of tangle diagrams and tangle
cobordisms with some minus signs. Let o(s, s’) represent the number of pairs in s
to the right of the only pair in s’\s, and multiply each cobordism S, by (—1) ),

To the latter graph we apply now the morphism [-] constructed in the sl(2)
foam cohomology, and form the complex C;,,(D) for the colored tangle theory. The
cochain objects are given by

(s,s

Ci,(D) = @IP.I,

where the sum is over all dot-rows s such that p(s) = i. The i-th differential
d' : Ci + Ct+1 is a formal sum of all morphisms [S,] corresponding to edges e at
height i, where [Se]: [Ds] + [Ds].
Invariants in Low-Dimensional Topology and Knot Theory
45
Theorem 1. The isomorphism class of the cochain complex Cn(D) is an invariant
of the colored framed link T .
To obtain a cohomology theory we apply a functor to switch from the geometric
picture to an algebraic one. Speciﬁcally, we employ the Bar-Natan type functor F
constructed in the sl(2) foam cohomology theory, switching from the category of
foams (rel. local relations) to the category of R-modules. This yields an ordinary
complex FCn(D), and we can take its cohomology. The isomorphism class of
the cohomology group Hn(D) := H(FCn(D)) is a triply-graded invariant of the
colored framed tangle T . Moreover, if the tangle T is a knot, the total graded
Euler characteristic of FCn(D) is the colored Jones polynomial of the knot.
We consider now two colored tangle diagrams D1 and D2, whose components are
colored by n. Moreover, we suppose that the vertical tangle composition D1 ◦D2
is deﬁned, and that D1, D2 and D1 ◦D2 have no circle components. Then there
exists a binary operation ∗deﬁned on the homotopy category of complexes over
Kof /h, such that Cn(D1) ∗Cn(D2) = Cn(D1 ◦D2).
Denote by (Ci, φi) := Cn(D1) ∗Cn(D2). Then Ci =
2
s,p(s)=i
([D1,s] ⊗R [D2,s])
and
φi(v1 ⊗v2) :=
!
e
[S1,e](v1) ⊗[S2,e](v2), for all v1 ⊗v2 ∈[D1,s] ⊗R [D2,s]
where the latter sum is over all edges e with tail s. The formal tensor product
here is the “gluing” operation of formal complexes coming from the sl(2) foam
cohomology.
Theorem 2. (Ci, φi) is a cochain complex, and (Ci, φi) = Cn(D1 ◦D2), up to
homotopy.
References
[1] D. Bar-Natan, Khovanov’s homology for tangles and cobordisms, Geom. Topol. 9 (2005),
1443–1499.
[2] A. Beliakova, S. Wehrli, Categoriﬁcation of the colored Jones polynomial and Rassmussen
invariant of links, Canad. J. Math. 60 (2008), 1240–1266.
[3] C. Caprau, sl(2) tangle homology with a parameter and singular cobordisms, Algebr. Geom.
Topol. 8 (2008), 729–756.
[4] C. Caprau, The universal sl(2) cohomology via webs and foam, Topol. and Applications
156 (2009), 1684–1702.
[5] M. Khovanov, A categoriﬁcation of the Jones polynomial, Duke Math. J. 101 (2000), no. 3,
359–426.
[6] M. Khovanov, Categoriﬁcations of the colored Jones polynomial, J. Knot Theory Ramiﬁca-
tions 14 (2005), no. 1, 111–130.
[7] M. Mackaay, P. Turner, Bar-Natan’s Khovanov homology for coloured links, Paciﬁc J. Math.
229 (2007), no. 2, 429–446.
46
Oberwolfach Report 28/2012
