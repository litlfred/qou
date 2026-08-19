---
doc_id: topologicalinvariance3dindex
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-004-2-definitions
section_title: "Definitions"
section_number: 2
pages: 6-16
source_pdf: topological.invariance.3Dindex.pdf
source_sha256: 22953b4eee66dca2
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
---
De
nition 2.1. Let M be a topologically 
nite 3-manifold which is the interior of a compact
3-manifold with torus boundary components. An ideal triangulation T of M consists of a
pairwise disjoint union of standard Euclidean 3simplices ~∆ =∪n
k=1~∆k with vertex set ~∆(0),
together with a collection Φ of Euclidean isometries between the 2simplices in ~∆, called
face pairings , such that the quotient space (~∆\~∆(0))/Φ is homeomorphic to M. The images
of the simplices in T may be singular in M .
De
nition 2.2. Let T be an ideal triangulation with at least 2 distinct tetrahedra. A 23
move can be performed on any pair of distinct tetrahedra of T that share a triangular face
t. We remove t and the two tetrahedra, and replace them with three tetrahedra arranged
around a new edge, which has endpoints the two vertices not on t. See Figure 1a. A 32
move is the reverse of a 23 move, and can be performed on any triangulation with a degree
3 edge, where the three tetrahedra incident to that edge are distinct.
De
nition 2.3. Let T be an ideal triangulation. A 02 move can be performed on any pair
of distinct triangular faces of T that share an edge e2 . Around the edge e, the tetrahedra of
T are arranged in a cyclic sequence, which we call a book of tetrahedra . (Note that tetrahedra
may appear more than once in the book.) The two triangles and e separate the book into two
halfbooks . We unglue the tetrahedra that are identi
ed across the two triangles, duplicating
the triangles and also duplicating e. We glue into the resulting hole a pair of tetrahedra
glued to each other in such a way that there is a degree 2 edge between them. See Figure 1b.
A 20 move is the reverse of a 02 move, and can be performed on any triangulation with a
degree 2 edge, where the two tetrahedra incident to that edge are distinct, there are no face
pairings between the four external faces of the two tetrahedra, and the two edges opposite
the degree 2 edge are not identi
ed.
Remark 2.4 . A 02 move is also called a lune move in the dual language of standard
spines [Mat87, Mat07, Pie88, BP97]. In [Mat87, Lem.2.1.11] and [Pie88] (see also [Pet95,
Prop.I.1.13]) it was shown that a 02 move follows from a combination of 23 moves as long
as the initial triangulation has at least 2 ideal tetrahedra.
De
nition 2.5. Let ∆3 be the standard 3simplex with a chosen orientation. Each pair of
opposite edges corresponds to a normal isotopy class of quadrilateral discs in ∆3, disjoint
from the pair of edges. We call such an isotopy class a normal quadrilateral type . Each vertex
of ∆3 corresponds to a normal isotopy class of triangular discs in ∆3, disjoint from the face
of ∆3 opposite the vertex. We call such an isotopy class a normal triangle type . Let T(k)
2 Unlike for the 23 move, it is possible to make sense of the 02 move when the two triangles are not
distinct. However, we will not make use of this variant in this paper.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 7
23
32
(a) The 23 and 32 moves.
02
20
(b) The 02 and 20 moves.
Figure 1. Moves on (topological) triangulations.
be the set of all ksimplices in T. If σ∈ T(3), then there is an orientation preserving map
∆3→σ taking the ksimplices in ∆3 to elements of T(k), and which is a bijection between
the sets of normal quadrilateral and triangle types in ∆3 and in σ. Let □ and ∆ denote the
sets of all normal quadrilateral and triangle types in T respectively.
De
nition 2.6. Given a 3-manifold M with an ideal triangulation T, the normal surface
solution space C(M; T) is a vector subspace of R7n, where n is the number of tetrahedra
in T, consisting of vectors satisfying the compatibility equations of normal surface theory.
The coordinates of x∈ R7n represent weights of the four normal triangle types and the
three normal quadrilateral types in each tetrahedron, and the compatibility equations state
that normal triangles and quadrilaterals have to meet the 2simplices of T with compatible
weights.
A vector in R7n is called admissible if at most one quadrilateral coordinate from each
tetrahedron is non-zero and all coordinates are non-negative. An integral admissible element
of C(M; T) corresponds to a unique embedded, closed normal surface in (M, T) and vice
versa.
De
nition 2.7. (See [JR03], [KR05]) An ideal triangulation T of an orientable 3-manifold is
0-e
cient if there are no embedded normal 2-spheres or one-sided projective planes. An ideal
triangulation T is 1-e
cient if it is 0-e
cient, the only embedded normal tori are vertex-
linking and there are no embedded one-sided normal Klein bottles. An ideal triangulation T
is strongly 1-e
cient if there are no immersed normal 2spheres, projective planes or Klein
bottles and the only immersed normal tori are coverings of the vertex-linking tori.
Note that in some contexts, atoroidal is taken to mean that there is no immersed torus
whose fundamental group injects into the fundamental group of the 3manifold. In our
context, we mean that there are no embedded incompressible tori or Klein bottles, other
than tori isotopic to boundary components. In Corollary 3.4 and Remark 3.5 we highlight
this distinction.
Note that if M is orientable, it is su
cient to consider only normal 2-spheres and tori,
except in the special case that M is a twisted I-bundle over a Klein bottle. For any embedded
normal projective plane or Klein bottle must be one-sided, so the boundary of a small regular
neighbourhood is a normal 2-sphere or torus. However in the non-orientable case, one must
8 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
consider two-sided projective planes and Klein bottles. In this paper we will consider only
the orientable case.
De
nition 2.8. If e∈ T(1) is any edge, then there is a sequence (qn1,...,q nk) of normal
quadrilateral types facing e, which consists of all normal quadrilateral types dual to e listed
in sequence as one travels around e. Then k equals the degree of e, and a normal quadri-
lateral type may appear at most twice in the sequence. This sequence is called the normal
quadrilateral type sequence for e and is well-de
ned up to cyclic permutations and reversing
the order.
De
nition 2.9. A function α: □→ R is called a generalised angle structure on (M, T) if it
satis
es the following two properties:
(1) If σ3∈ T(3) and q,q′,q′′ are the three normal quadrilateral types supported by it,
then
α(q) +α(q′) +α(q′′) =π.
(2) If e∈ T(1) is any edge and (qn1,...,q nk) is its normal quadrilateral type sequence, then
k∑
i=1
α(qni) = 2π.
Dually, one can regard α as assigning angles α(q) to the two edges opposite to q in the
tetrahedron containing q. The triangulations we consider are of oriented manifolds, so we
may assume that the triangulation is also oriented. We 
x an ordering q→q′→q′′→q on
these quad types, well de
ned up to cyclic permutation. See Figure 2.
q q′ q′′
Figure 2. The three quad types within an oriented tetrahedron, arranged in
our chosen cyclic order.
De
nition 2.10. If we restrict the angles of a generalised angle structure to be in
• [0,π ], then the generalised angle structure is a semi-angle structure .
• (0,π ), then the generalised angle structure is a strict angle structure .
•{ 0,π}, then the generalised angle structure is a taut angle structure .
The set of generalised angle structures is denoted by GA(T) and is an a
ne subspace of R3N ,
where N is the number of tetrahedra in T. The subset of semi-angle structures is denoted
by SA(T), and is a closed polytope in GA(T).
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 9
Remark 2.11 . It is easy to see that a taut angle structure can only happen if every tetrahedron
has a pair of opposite edges with angles π and the other four edges have angles 0.
De
nition 2.12. For an ideal triangulation T with N tetrahedra, a quad-choice is an element
Q = (Q1,...,Q N)∈ □N such that Qn is a choice of one of the three quad types in the nth
tetrahedron. An index structure α on T consists of 3N generalised angle structures, indexed
by the quad-choices Q, with the property that αQ(Qn) > 0 for n = 1,...,N , for each
quad-choice Q.
De
nition 2.13. The equations determining a generalised angle structure can be read o
as three N×N integer-valued matrices A = (¯aij), B = (¯bij) and C = (¯cij) whose rows
are indexed by the N edges of T and whose columns are indexed by the α(qj),α (q′
j),α (q′′
j )
variables respectively, where qj,q′
j,q′′
j are the quad types in the jth tetrahedron. These are
the so-called Neumann-Zagier matrices that encode the exponents of the gluing equations of
T, originally introduced by Thurston [NZ85, Thu77]. In terms of these matrices, a generalised
angle structure is a triple of vectors Z,Z′,Z′′∈ RN that satisfy the equations
(3) AZ + BZ′ + CZ′′ = 2π(1,..., 1)T, Z +Z′ +Z′′ =π(1,..., 1)T.
Note that the matrix entries ¯aij,¯bij, ¯cij give the coe
cients of Zj,Z′
j,Z′′
j in the ith edge
equation corresponding to the edges of tetrahedron j facing quad types qj,q′
j,q′′
j respectively.
We can combine these into a single matrix equation
(4)
(
A B C
IN IN IN
)

Z
Z′
Z′′

 =
(
2π(1,..., 1)T
π(1,..., 1)T
)
,
where IN is the N×N identity matrix. We call this matrix equation the matrix form of the
generalised angle structure equations .
3. Index structures and 1efficiency
We 
rst give a sketch proof of Theorem 1.5, showing that a semiangle structure implies
1e
ciency. We follow [KR05] and indicate the required small modi
cation. Suppose that M
is oriented with cusps and has an ideal triangulation T with a semi-angle structure. Assume
that there is an embedded normal torus or Klein bottle or sphere or projective plane, where
the normal torus is not a peripheral torus. Firstly, exactly as in [Lac00b] the latter two cases
are excluded by a simple Euler characteristic argument. Similarly, if there is a cube with
knotted hole bounded by an embedded normal torus, then a barrier argument as in [JR03]
establishes that there is a normal 2-sphere bounding a ball containing this normal torus,
which is a contradiction. Embedded Klein bottles are excluded, so we are reduced to the
cases of an embedded essential non peripheral normal torus or a normal torus bounding a
solid torus.
In both cases, there is a sweepout between the normal torus and a peripheral normal
torus (for essential tori) or to a core circle of the solid torus. By a minimax argument (see
10 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
[Rub97], [Sto00]), there is an almost normal 3 torus associated with this sweepout. This is
either obtained by attaching a tube parallel to an edge to a normal 2-sphere or has a single
properly embedded octagonal disc in a tetrahedron and a collection of normal triangular and
quadrilateral discs. The 
rst case is excluded, since we have ruled out such normal 2-spheres.
The semi-angle structure now implies that a standard combinatorial Gauss-Bonnet argu-
ment can be applied. Each polygonal disc in our torus has curvature given by Σiαi−(n−2)π,
where n is the number of edges of the disc and αi are the interior angles at the vertices of
the disc. Gauss-Bonnet then says that the sum of the curvatures of all the discs is zero,
since the Euler characteristic of the torus is zero. Every normal triangular disc contributes
zero and each normal quadrilateral is non-positive in the curvature sum. On the other hand,
any embedding of an octagon into an ideal tetrahedron with a semi-angle structure gives a
strictly negative contribution. See Figure 3. Hence the Euler characteristic of such a surface
cannot be zero and there could not have been an embedded normal torus to begin with. This
completes the sketch proof. □
α α
α α
γ
γ
β
β
Figure 3. A normal octagon in a tetrahedron with a semi-angle structure
with angles α,β,γ ∈ [0,π ]. The curvature of this octagon is 4α + 2β + 2γ−
(8− 2)π = 2α + 2π− 6π = 2α− 4π <0.
Remark 3.1 . Lackenby gives a result similar to Theorem 1.5 in Theorem 2.1 of [Lac08].
A useful observation (see [KR05]) following from Theorem 1.5 is the following;
Corollary 3.2. Suppose that T is an ideal triangulation of an oriented 3-manifold M with
cusps. If M is an-annular and T admits a semi-angle structure then M is strongly 1-e
cient.
3 A closed properly embedded surface is almost normal if it is a union of normal discs together with
precisely one exceptional piece (lying inside one tetrahedron), which is an octagon or an annulus consisting
of two disjoint normal discs joined by a tube.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 11
Proof. The key observation is that the semi-angle structure on T lifts to a semi-angle structure
on the lifted triangulation ~T, for any covering space ~M of M . Assume that there is an
immersed normal torus T in M which is not a covering of the peripheral torus. If ~M is chosen
as the covering space whose fundamental group corresponds to the image of π1(T ), then T
lifts to a normal torus ~T so that the inclusion map induces an onto map π1(~T )→π1(~M).
We can now use ~T as a barrier (see [JR03]) to produce an embedded normal non-peripheral
torus T∗, which is either essential and isotopic into a boundary cusp, or bounds a solid torus
or cube with knotted hole. (Here the an-annular assumption is used to show that the covering
space ~M is atoroidal). The rest of the argument is exactly the same as in Theorem 1.5.
□
Proof of Theorem 1.2. We closely follow LuoTillmann [LT08]. We use the following version
of Farkas' lemma, which is given as Lemma 10 (3) in [LT08]:
Lemma 3.3. Let A be a real K×L matrix, b∈ RK, and · denote the usual Euclidean inner
product on RK. Then {x∈ RL|Ax =b,x> 0}⁄ =∅ if and only if for all y∈ RK such that
ATy⁄= 0 and ATy≤ 0, one has y·b< 0.
For our purposes, Ax =b is the matrix form (4) of the generalised angle structure equa-
tions, so b = (2π,..., 2π,π,...,π )T . Consider a particular quad-choice Q, as in De
nition
2.12. If there is to be an index structure, then we must be able to 
nd the appropriate
generalised angle structure x. That is, xl > 0 if l corresponds to one of the Qn, and xl can
have any real value if not. We refer to the former as restricted variables, and the latter as
unrestricted variables.
The problem with applying Farkas' lemma directly is that it applies to the set of solutions
{Ax = b| x >0}. That is, all variables are strictly positive. However, we use a standard
trick: for each unrestricted variable xl, introduce a new variable x′
l. The new variable acts
precisely like −xl, so the old xl can be written in the new coordinates as xl−x′
l. This allows
both new variables xl,x′
l > 0, making them restricted variables, so that Farkas' lemma can
be applied.
The eect that this has on the matrix A is as follows: We get a new column after each
unrestricted xl for x′
l, and the values in the new column are the negatives of the values in
the column for xl.
Now we apply Farkas' lemma. We get a solution to our system if and only if for all
y∈ RK such that ATy⁄= 0 and ATy≤ 0, we have y·b< 0. The transposed matrix AT has
dual variables (z1,...,z n,w 1,...,w t), where the wi correspond to the tetrahedra and the zj
correspond to the edges. The dual system AT (z,w )T≤ 0 is given by inequalities:
wi +zj +zk≤ 0
whenever the ith tetrahedron contains a quad that faces the edges j and k (which may not
be distinct). This holds for all the rows corresponding to the xl, and we get the following
for the x′
l:
−(wi +zj +zk)≤ 0
12 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
The two of these together imply that wi + zj + zk = 0 for the quads corresponding to
unrestricted angles, while wi +zj +zk≤ 0 for restricted angles. The rest of the argument is
the same as in [LT08], as follows.
Kang and Rubinstein [KR04] give a basis of the normal surface solution space C(M; T)
which consists of one element for each edge and one element for each tetrahedron of T.
For the edge e, the corresponding basis element has each of the quad types in the normal
quadrilateral type sequence for e with coe
cient −1 (or −2 if that quad appears twice), and
each of the triangle disc types that intersect e with coe
cient +1. For each tetrahedron σ,
the corresponding basis element has each of the quad types in σ with coe
cient −1, and
each of the triangle disc types in σ with coe
cient +1.
If we have a solution to the dual system, then we can form a normal surface solution class
Ww,z as a sum of tetrahedral and edge basis elements with coe
cients given by the wi and zj
corresponding to their tetrahedra and edges respectively. There is a linear functional χ∗ on
R7n called the generalised Euler characteristic , which agrees with the Euler characteristic in
the case of an embedded normal surface represented by an element of C(M; T). It is shown
in [LT08] that the generalised Euler characteristic χ∗(Ww,z) is equal to y·b, and that the
normal quad coordinates of Ww,z are given by −(wi+zj+zk). From the above inequalities, we

nd that the obstruction classes are solutions to the normal surface matching equations with
zero quad coordinates for unrestricted angles, non-negative quad coordinates for restricted
angles (i.e. the quads speci
ed by the quad-choice Q), at least one quad coordinate strictly
positive, and generalised Euler characteristic χ∗(Ww,z)≥ 0.
If there are any negative triangle coordinates, we can add vertex linking copies of the
boundary tori to the solution until all normal disc coordinates are non-negative. Now, since
at most one quad coordinate in each tetrahedron is non-zero, we can in fact realise the
normal surface solution class as an embedded normal surface, and so the generalised Euler
characteristic is equal to the Euler characteristic. Therefore, an obstruction class to this
quad-choice having an associated generalised angle structure is an embedded normal sphere,
projective plane, Klein bottle or torus, with the only quads appearing being of the quad
types given by the quad-choice. Thus, if the triangulation is 1-e
cient, then there can be
no such obstruction.
The above argument shows that a 1-e
cient triangulation admits an index structure. For
the converse, note that if a triangulation is not 1-e
cient, then there is an embedded normal
sphere, projective plane, Klein bottle or non-vertex linking torus. This must then have at
least one non-zero quad coordinate, and since it is embedded, there can be only one non-zero
quad coordinate in each tetrahedron. Choosing these quad types in the tetrahedra containing
the surface, and arbitrarily choosing quad types in any other tetrahedra, we construct a quad-
choice that by the above argument cannot have a suitable generalised angle structure, and
so there is no index structure. This completes the proof of Theorem 1.2. □
Corollary 3.4. Suppose that M is a compact oriented irreducible 3-manifold with incom-
pressible tori boundary components and no immersed incompressible tori or Klein bottles,
except those which are homotopic into the boundary tori. Then M admits an ideal trian-
gulation T having an index structure. Moreover if M has no essential annuli (i.e M is
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 13
an-annular) then for any 
nite sheeted covering space ~M , the lifted triangulation also admits
an index structure.
Proof. To construct 1-e
cient triangulations, we can use a construction of Lackenby [Lac00a].
He proves that if M is a compact oriented irreducible 3-manifold with incompressible tori
boundary components and M has no immersed essential annuli, except those homotopic into
the boundary tori, then M admits a taut ideal triangulation T. Then by Corollary 3.2 such
triangulations are strongly 1-e
cient. Note that the lift of such a triangulation to any 
nite
sheeted covering space is also 1-e
cient.
There is a remaining case of small Seifert 
bred spaces. For these are precisely the oriented
3-manifolds with tori boundary components which admit essential annuli, but no embedded
incompressible tori which are not homotopic into the boundary components.
Such examples have base orbifold either a disc with two cone points or an annulus with
one cone point or Möbius band with no cone points. The cone points are the images of the
exceptional 
bres in the Seifert structure. These manifolds have immersed incompressible
tori, but do not have embedded incompressible tori or Klein bottles, except in the case
where the base orbifold has orbifold Euler characteristic zero: a disc with two cone points
corresponding to exceptional 
bres of multiplicity two or orbit surface a Möbius band with
no cone points. This represents two dierent Seifert 
brations of the same manifold. We
exclude this latter case.
Now to construct a suitable ideal triangulation, note that these Seifert 
bred spaces M are
bundles over a circle with a punctured surface of negative Euler characteristic as the 
bre.
To see this, note that M is Seifert 
bred over an orientable base orbifold B with χorb(B)< 0.
Then M admits a connected horizontal surface F which is orientable with χ(F ) < 0 since
F is an orbifold covering of B. (A surface is horizontal if it is everywhere transverse to the
Seifert 
bration.) Since M is orientable it follows that F non-separating, so M 
bres over
the circle with F as 
bre (see, for example, [Hat07, sections 1.2 and 2.1].)
After Lemma 6 in [Lac00a], it is shown that, starting with any ideal triangulation of the
punctured surface F , a bundle can be formed as a layered triangulation. This is done by
realising a sequence of diagonal 
ips on the surface triangulation needed to achieve any
given monodromy map. Such a triangulation then gives an ideal triangulation with a taut
structure. So by Theorem 1.5 these are 1-e
cient triangulations and hence admit index
structures. □
Remark 3.5 . The small Seifert 
bred spaces from the proof of Corollary 3.4 have 
nite
sheeted coverings with embedded incompressible tori so that the lifted triangulations do not
all admit index structures, in contrast with the hyperbolic case.
Example 3.6. The trefoil knot complement has an ideal layered triangulation with two
tetrahedra and two edges, one of degree 2 and one of degree 10. See Figure 4. The comple-
ment of the trefoil knot can be seen as a punctured torus bundle with monodromy given by
RL−1, where
L =
(
1 0
1 1
)
R =
(
1 1
0 1
)
.
14 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
L−1
R
(0, 0) (1 , 0)
(1, 1) (0, 1)
(0, 1)
(0, 0) (1 , 0)
(1, 1)
(0,−1)
(1, 1)
(0, 0) (1 , 0)
Figure 4. A layered triangulation of the complement of the trefoil knot, seen
as a punctured torus bundle. On the left, the monodromy is decomposed
into generators which act on the punctured torus. The diagrams are shown
sheared to highlight the fact that the monodromy has the eect of rotation
by −π/3. The arrows show where edges of a triangulation of the punctured
torus map to under the generators. In the middle, we realise each change in
the triangulation by layering on a 
at tetrahedron. The arrows are shown on
the bottom and top of the stack of two tetrahedra to show the gluing. On the
right, we see the edges after the identi
cations induced by gluing the top to
the bottom. There are two tetrahedra and two edges in the triangulation, one
of degree two (shown with a dashed line) and the other of degree ten.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 15
Following the caption of Figure 4, we obtain a triangulation of the complement of the trefoil
consisting of two tetrahedra. The matrix form of the generalised angle structure equations
for this triangulation is


1 1 0 0 0 0
1 1 2 2 2 2
1 0 1 0 1 0
0 1 0 1 0 1




Z1
Z2
Z′
1
Z′
2
Z′′
1
Z′′
2


=


2π
2π
π
π

.
There is a taut structure given by choosing angles (π,π, 0, 0, 0, 0)T . This assigns the angle
π to the quad types facing the degree 2 edge and 0 to all other angles. This taut structure is
compatible with the layering construction. By Theorem 1.5, this triangulation is 1e
cient.
It is easy to see that there are no other semi-angle structures for this particular triangu-
lation, because of the degree 2 edge. However, consistent with Theorem 1.2, it admits an
index structure. To see this, we have to produce a generalised angle structure for each of
the 32 = 9 possible quad-choices. However, by symmetry of the matrix we can reduce this
number to three, represented by the following three pairs of conditions that must be satis
ed
by three generalised angle structures.
(Z1 > 0,Z 2 > 0), (Z1 > 0,Z′
2 > 0), (Z′
1 > 0,Z′
2 > 0)
These three representatives are all satis
ed by, for example, (π,π,x,x, −x,−x)T for any
x> 0.
Note that there is a well-known 6-fold cyclic covering by the bundle which is a product
of a once punctured torus and a circle. This covering is toroidal so we see that there is an
index structure on the trefoil knot space but not on this covering space.
e1
e2
a
b
q
Figure 5. Part of a triangulation that does not admit an index structure,
and part of the corresponding surface. The edge e1 is degree 1, so the two
faces incident to it are identi
ed (indicated by the arrows).
16 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
Example 3.7. We give an example of a subset of a triangulation consisting of two tetrahedra
identi
ed in a particular way. Namely, we have a tetrahedron σ1 with opposite edges e1 of
degree 1 and e2 of degree 2, and another tetrahedron σ2 which is the second tetrahedron
incident to e2. See Figure 5. If these tetrahedra are part of any ideal triangulation with
torus boundary components then that triangulation will not have an index structure, and
will have a normal torus that is not vertex-linking, so it is not 1e
cient.
First we show that there is no index structure. Since e1 is degree 1, for any generalised
angle structure the angle of σ1 at the quad type facing e1 must be 2π. This quad type also
faces e2. The angle of the quad type in σ2 facing e2 must add to 2π to give 2π, and so it
must be zero. Therefore this angle can never be strictly positive, and so there is no index
structure.
Next, we 
nd the corresponding embedded normal torus. It has a single quadrilateral in
σ2, labelled q in Figure 5. Two of its triangles are in σ1, also shown. When the two identi
ed
faces of σ1 are glued to each other, the boundary of the shown surface consists of the two arcs
labelled a and b, on two of the boundary faces of σ2. Now consider the vertexlinking normal
torus T , given by the link of the vertex at which the endpoints of e2 meet. We complete our
surface into an embedded normal torus by deleting from T the normal triangles in σ1 and
σ2 at the endpoints of e2, and gluing the resulting boundary arcs to a and b. The resulting
surface is boundary parallel and so is a torus, but is obviously not vertexlinking since it
contains a quadrilateral.
