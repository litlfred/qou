---
doc_id: topologicalinvariance3dindex
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-012-48-invariance-of-index-under-isotopy-of-peripher
section_title: "Invariance of index under isotopy of peripheral curve"
section_number: 4.8
pages: 26-34
source_pdf: topological.invariance.3Dindex.pdf
source_sha256: 22953b4eee66dca2
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
---
Theorem 4.7. Let ϖ be an oriented simple closed curve ϖ in ∂M which is a normal curve
relative to the triangulation T∂ of ∂M . Then the index IT(ϖ) is invariant under isotopy of
the curve ϖ in ∂M .
Proof. Suppose we have two isotopic oriented normal curves ϖ1,ϖ 2. Then we can convert
one into the other via a sequence of moves (and their inverses) of the form shown in Figure
11. That is, we choose a point p on the curve ϖ and an arc α, disjoint from ϖ other than at
p, and which joins p to either a vertex or a point in the interior of an edge of T∂. We then
push the curve along and in a regular neighbourhood of α over the vertex or edge.
We will show that IT(ϖ) is invariant under these moves. Note that the result of these
isotopies will not in general be normal curves, so we need to extend the de
nition of the
index to deal with these cases as well. The class of curves we work in consists of oriented
simple closed curves, transverse to T(1)
∂ and disjoint from T(0)
∂ . For our purposes we will deal
only with curves that are non trivial in H1(∂M ), and so none of our curves is disjoint from
T(1)
∂ . Given such a curve, it enters a triangle somewhere on one edge, and can exit out either
of the two other edges, or the same edge that it entered, either to the left or the right of its
entry point. Thus there are four ways in which a component of a curve intersects a given
triangle. These contribute to the index in the following way. See Figure 12.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 27
Figure 11. The two kinds of isotopy moves on a curve relative to the trian-
gulation of ∂M .
+ − ⊕ ⊖
Figure 12. The four ways in which a curve can travel through a triangle.
We call the last two possibilities a positive backtrack and negative backtrack
respectively.
If the curve turns either left or right around a corner of the triangle then it contributes
to the index in exactly the same way as for a normal curve: we add +1 to the entry in the
vector (¯aϖ|¯bϖ|¯cϖ) corresponding to the angle at the edge of the tetrahedron we are turning
around if we are going anticlockwise around the corner, and add −1 if we are going clockwise.
Compare with Figure 7.
Here we de
ne the eect of backtracks on the index calculation: (This is, of course, chosen
in such a way as to be consistent with the index calculated with curves without backtracks.)
We do not change the vector (¯aϖ|¯bϖ|¯cϖ). These backtracks only alter the power of (−q1/2),
either multiplying the expression by (−q1/2) for a positive backtrack (turning to the left),
or by (−q1/2)−1 for a negative backtrack (turning to the right). We indicate these using the
symbols ⊕ and ⊖.
Note that by (22), a positive backtrack has the same eect on the index as anticlockwise
turns around each of the three corners of a triangle. Note also that by (25), an anticlockwise
loop around a vertex of the triangulation produces a power of (−q1/2)2. This follows since
28 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
adding an anticlockwise loop around an end of the ith edge has the eect of shifting the sum
by one in the ki component. The terms are unchanged after shifting other than the term
q
P
iki, and the eect is to multiply the index by q.
Thus an anticlockwise loop around a vertex is cancelled by two negative backtracks, and
anticlockwise turns around each of the three corners of a triangle are cancelled by one negative
backtrack.
+
+
+
+
+
+
⊖ ⊖
+
+
+
+
+
⊖
− −
+
+
+
+
+
+
⊖
⊖
+
+
+
+
+
⊖− −
+
+ +
⊖
⊕
⊖
⊖
⊕
⊖
⊕
⊖
⊖
⊕ ⊕ ⊖
⊕
Figure 13. Four cases of isotopy across a vertex and six cases of isotopy
across an edge. All other cases are symmetries of these.
Now all we need to do is to show that each version of the moves from Figure 11 preserves
the index, using the above rules. There are dierent versions of the isotopy moves depending
on where the curve we are acting on enters or exits the triangle. We show the possibilities
in Figure 13. Here the +,−,⊕ and ⊖ signs show the dierence in the index calculation
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 29
under the isotopy as we change from one curve to the other in the direction following the
double head arrow. Note that reversing the arrow on the curve 
ips all of the signs, as does
re
ecting the picture. With combinations of these symmetries applied to the ten cases shown
we obtain all possible ways in which the isotopy can be made relative to the position of the
curve. Considering each case in turn, we can see that the signs cancel out and so the index
is unchanged by these moves.
For example, consider the second diagram in the top row of Figure 13. We start with a
curve that enters the right side of the triangle and exits the bottom. We isotope this curve
by pushing it over the top vertex of the triangle. This has the following eects:
• Remove an anticlockwise turn around the lower right corner of the triangle, this
changes the coe
cient at that angle by −1.
• Add a negative backtrack to the right edge of the triangle.
• Add an anticlockwise turn around each of the angles at the top vertex of the triangle
other than the top corner of the triangle itself.
• Add a clockwise turn around the lower left corner of the triangle.
We view the top corner of the triangle as having both a + and a −, so that the total change
in the index calculation consists of one anticlockwise turn around a vertex, one negative
backtrack and clockwise turns around each of the three corners of the triangle. By our above
rules, these cancel out and so the index is unchanged. □
Remark 4.8 . These calculations are exactly analogous to those for calculating the holonomy
of a peripheral curve given shapes of ideal hyperbolic tetrahedra satisfying Thurston's gluing
equations. Thus this argument can easily be adapted to reprove the well-known fact that
the holonomy is independent of the choice of simple closed curve representing an element of
H1(∂M ; Z).
5. Inv ariance of index under the 02 move
Let M be a cusped 3-manifold and consider the 02 move on a pair T and ~T of ideal
triangulations of M with N and N + 2 tetrahedra, as shown in Figure 14.
Theorem 5.1. Suppose that T and ~T are ideal triangulations related by a 02 move and both
admit an index structure. Then, for any [ϖ]∈H1(∂M ; Z), IT([ϖ]) =IeT([ϖ]).
Proof. Our assumptions imply that both IT and IeT exist. We now compare these indices
using the alternative de
nition (25) and quadratic identity (23).
We use the labelling of the two bigons and triangles on ~T shown in Figure 14. Let Ti for
i = 3,...,N +2 denote the tetrahedra in T, and let T1,T 2 be the additional tetrahedra added
in ~T. Note that the edge e in T splits into two edges e′,e′′ in ~T, and there is another new
edge ~e in ~T. We abuse notation by identifying the symbols for the corresponding remaining
edges in T and ~T. We denote these as e1,...,e N−1.
Let ~k∈ ZN+2 be a weight function on the edges of ~T and write ~k = (k′,k′′,~k,k 1,...,k N−1)
where k′,k′′,~k,ki are the values of ~k on e′,e′′,~e and ei respectively. Similarly, let k =
(k,k 1,...,k N−1)∈ ZN be a corresponding weight function on T. We choose label ¯aj on the
30 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
e e
e2 e4
e1 e3
e2 e4
e1 e3
e′
e′′
~e
¯a2 ¯a1
¯c2
¯b2
¯b1
¯c1
¯a1 ¯a2
¯c1
¯b1
¯b2
¯c2
¯a1¯c1 ¯b1
¯a2¯b2 ¯c2
¯a2¯c2 ¯b2
¯a1¯b1 ¯c1
Figure 14. The 02 move shown with truncated tetrahedra. The four trian-
gulated ends of the new pair of tetrahedra are shown. All of the zoomed in
pictures are as seen from viewpoints outside of the pair of tetrahedra. The
labels at the corners of the triangles in the zoomed in pictures are explained
in Section 4.4.
edge ~e on tetrahedron Tj for j = 1, 2; then the location of labels ¯bj, ¯cj are determined using
the orientation on M .
Let ϖ be an oriented multi-curve which is normal with respect to the triangulation
T∂ of ∂M induced by T, and let ~ϖ an oriented multi-curve which is normal with re-
spect to ~T∂ and represents the same homology class [ϖ]∈ H1(∂M ; Z). Let J(Tj,k,ϖ ) =
J∆(¯aj(k,ϖ ),¯bj(k,ϖ ), ¯cj(k,ϖ )) denote the contribution of tetrahedron Tj to the index with
weight function k on its edges and peripheral curve ϖ on its truncated ends, and similarly
let J(Tj,~k,~ϖ) be contribution with weight function ~k and peripheral curve ~ϖ.
To compute IT we use Theorem 4.3 to choose an excluded set X of r edges in a maximal
tree with 1- or 3-cycle in T to be omitted from the summation in (25).
Case 1: If e /∈ X we can order the edges of T so that X ={eN−r,...,e N−2,eN−1}. Then
we can compute IeT by omitting the same edge set ~X = X.
Case 2: If e∈ X we can order the edges so X ={e,eN−r+1,...,e N−2,eN−1}. Then we can
compute IeT by omitting the edge set ~X ={e′′,eN−r+1,...,e N−2,eN−1}.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 31
Then
(30) IeT(~ϖ) =
∑
ek∈ eS
qk′+k′′+ek+PN−1
i=1 kiJ(T1,~k,~ϖ)J(T2,~k,~ϖ)
N+2∏
j=3
J(Tj,~k,~ϖ),
where
~S =
{
~k = (k′,k′′,~k,k 1,...,k N−1)∈ ZN+2 :kN−i = 0 for i = 1,...,r
}
in case 1
and
~S =
{
~k = (k′,k′′,~k,k 1,...,k N−1)∈ ZN+2 :k′′ = 0,kN−i = 0 for i = 1,...,r − 1
}
in case 2 .
Note that in both cases, the new edge ˜e is included in the set of basic edges so ˜k varies over
Z in the sum.
Now we look at the contribution to IeT coming from the tetrahedra T1,T 2 and summed
over the weight ~k on ˜e, namely
(31)
∑
ek∈Z
q
ekJ(T1;~k,~ϖ)J(T2;~k,~ϖ)
where
J(T1;~k,~ϖ) =J∆(k′ +~k + ¯a eϖ,1,k 2 +k3 + ¯b eϖ,1,k 1 +k4 + ¯c eϖ,1)
and
J(T2;~k,~ϖ) =J∆(k′′ +~k + ¯a eϖ,2,k 1 +k4 + ¯b eϖ,2,k 2 +k3 + ¯c eϖ,2).
Recall that ϖ be an oriented multi-curve which is normal with respect to the triangulation
T∂ of ∂M induced by T. Since the index only depends on the homology class of a peripheral
curve, we can calculate IeT([ϖ]) by using for ~ϖ a corresponding curve on ∂M which is normal
with respect to ~T∂ and goes straight through each pair of added triangles on ∂M . See
Figure 15.
Then we have
¯a eϖ,1 = ¯a eϖ,2 = 0, ¯b eϖ,1 = ¯c eϖ,2 =x, ¯b eϖ,2 = ¯c eϖ,1 =y,
for some x,y∈ Z, and
¯a eϖ,j = ¯aϖ,j, ¯b eϖ,j = ¯bϖ,j, ¯c eϖ,j = ¯cϖ,j for j = 3,...,N + 2.
Using the invariance of J∆ under all permutations of its arguments and the quadratic
identity (23), the sum (31) becomes
∑
ek∈Z
q
ekJ∆(k′ +~k,k 2 +k3 +x,k 1 +k4 +y)J∆(k′′ +~k,k 1 +k4 +y,k 2 +k3 +x) =q−k′
δk′,k′′.
This means that in the sum (30) we can remove the summation over ~k and put k′ =k′′ =k.
Hence J(Tj,~k,~ϖ) =J(Tj,k,ϖ ) for j = 3,...,N + 2, and
IeT(~ϖ) =
∑
k∈S
qk+PN−1
i=1 ki
N+2∏
j=3
J(Tj,k,ϖ ) =IT(ϖ),
32 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
¯a2 ¯a1
¯c2
¯b2
¯b1
¯c1
¯a2¯c2 ¯b2
¯a1¯b1 ¯c1
Figure 15. Changes in peripheral curve from ϖ in T∂ to ~ϖ in ~T∂. Note that
the curve in the top diagram could go either way around the new vertex.
where
S =
{
k = (k,k 1,...,k N−1)∈ ZN :kN−i = 0 for i = 1,...,r
}
in case 1
and
S =
{
k = (k,k 1,...,k N−1)∈ ZN :k = 0,kN−i = 0 for i = 1,...,r − 1
}
in case 2 .
This completes the proof of invariance of the index under the 02 move. □
6. The XEP
M class of triangulations
6.1. Subdivisions of the EpsteinPenner decomposition. For a once-cusped hyper-
bolic 3manifold M , the EpsteinPenner decomposition (see [EP88]) divides M into a 
nite
number of ideal hyperbolic polyhedra. This subdivision is canonical, depending only on the
topology of the manifold, if M has a single cusp. If M has r≥ 1 cusps, then the Epstein-
Penner cell decomposition is canonical up to the choice of a scale vector (t1,...,t r) with
t1,t 2,...,t r > 0 giving the relative size of the cusps. The scale vector is well-de
ned up to
multiplication by a positive real number. For the purposes of de
ning our canonical set, we
can choose all ti to be the same.
Very often, the cells of the decomposition are all ideal tetrahedra, but other polyhedra
can occur. For many applications, including the use in this paper, we need a subdivision
of M into ideal tetrahedra only. It is well known that every cusped 3manifold has a
decomposition into ideal tetrahedra, but one often needs more than a purely topological
structure on the tetrahedra. The EpsteinPenner decomposition, coming as it does with
a geometric structure, provides all of the nice geometric properties one could want. So,
in the cases when the cells of the decomposition are not themselves tetrahedra, we would
like to further subdivide the polyhedra into tetrahedra. However, there is no canonical
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 33
way to subdivide, and it is not even clear if one can subdivide the various polyhedra in
a consistent way, so that the triangulations induced on the faces of the polyhedra match
when the polyhedra are glued to each other. In particular, it is still unknown whether every
cusped hyperbolic 3manifold admits a geometric triangulation (that is, a subdivision into
positive volume ideal hyperbolic tetrahedra), either constructed by further subdividing the
EpsteinPenner decomposition or otherwise.
However, one can use the EpsteinPenner decomposition to produce an ideal triangulation
by subdividing the ideal polyhedra, if we also allow 
at tetrahedra inserted between faces of
the polyhedra to bridge between incompatible triangulations of those faces. Such an ideal
triangulation has a natural semi-angle structure (see Remark 6.6), and so by Theorem 1.5
all of these triangulations are 1e
cient.
To describe our triangulations more precisely, we use the same notation as in [HRS12].
De
nition 6.1. In this paper, the term polyhedron will mean a combinatorial object ob-
tained by removing all of the vertices from a 3-cell with a given combinatorial cell decom-
position of its boundary. We further require that this can be realised as a positive volume
convex ideal polyhedron in hyperbolic 3-space H3.
De
nition 6.2. An (ideal) polygonal pillow or n-gonal pillow is a combinatorial object
obtained by removing all of the vertices from a 3-cell with a combinatorial cell decomposition
of its boundary that has precisely two faces. The two faces are copies of an n-gon identi
ed
along corresponding edges.
De
nition 6.3. Suppose that P is a cellulation of a 3-manifold consisting of polyhedra
and polygonal pillows with the property that polyhedra are glued to either polyhedra or
polygonal pillows, but polygonal pillows are only glued to polyhedra. Then we call P a
polyhedron and polygonal pillow cellulation , or for short, a PPP-cellulation .
De
nition 6.4. Let t be a triangulation of a polygon. A diagonal 
ip move changes t as
follows. First we remove an internal edge of t, producing a four sided polygon, one of whose
diagonals is the removed edge. Second, we add in the other diagonal, cutting the polygon
into two triangles and giving a new triangulation of the polygon.
De
nition 6.5. Let Q be a polygonal pillow, with triangulations t− and t+ given on its
two polygonal faces Q− and Q+. By a layered triangulation of Q, bridging between t− and
t+, we mean a triangulation produced as follows. We are given a sequence of diagonal 
ips
which convert t− into t+. This gives a sequence of triangulations t− =L1,L 2,...,L k =t+,
where consecutive triangulations are related by a diagonal 
ip. Starting from Q− with the
triangulation t− = L1, we glue a tetrahedron onto the triangulation L1 so that two of its
faces cover the faces of L1 involved in the 
rst diagonal 
ip. The other two faces together
with the rest of L1 produce the triangulation L2. We continue in this fashion, adding one
tetrahedron for each diagonal 
ip until we reach Lk =t+, which we identify with Q+.
Our class of triangulations XEP
M of M consists of triangulations that are subdivisions
of PPP-cellulations. Our PPP-cellulation will have polyhedra being the polyhedra of the
Epstein-Penner decomposition. It also has a polygonal pillow inserted between all pairs of
identi
ed faces that have at least 4 sides. We will form our triangulations by 
rst sub-
dividing the ideal hyperbolic polyhedra into positive volume ideal hyperbolic tetrahedra.
34 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
Secondly, for each polygonal pillow, we insert any layered triangulation that bridges between
the induced triangulations of the two boundary polygons of the polyhedra to each side.
Remark 6.6 . Any triangulation produced in the way described above has a natural semi
angle structure . This comes from the shapes of the tetrahedra as ideal hyperbolic tetrahedra.
The dihedral angles of the positive volume ideal hyperbolic tetrahedra, together with 0 and
π angles for the 
at tetrahedra in the layered triangulations in the polygonal pillows satisfy
all of the rules for a generalised angle structure, and all angles are in [0,π ].
The natural semiangle structure together with Theorem 1.5 show that each triangulation
in our class is 1-e
cient. However, we also need to show that our class is connected under
23, 32, 02 and 20 moves, and for this we will need some extra machinery. The main tool
