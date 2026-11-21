---
doc_id: topologicalinvariance3dindex
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-013-46-choice-of-edges-in-the-summation-for-index
section_title: "Choice of edges in the summation for index"
section_number: 4.6
pages: 20-24
source_pdf: topological.invariance.3Dindex.pdf
source_sha256: 22953b4eee66dca2
toc_source: outline
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
---
with r ≥1 torus cusps and let T be an ideal triangulation of M with N tetrahedra and,
hence, N edges which we denote e1, . . . , eN. Let G be the 1-skeleton T(1) of T together with
one (ideal) vertex for each cusp of M. Note that G has r vertices and N edges, and may
contain loops (i.e. edges with both ends at a single vertex) or multiple edges between the
same two vertices. The incidence matrix C = (chi) for G is an r×N matrix whose (h, i) entry
gives the number of ends of edge i on cusp h. Note that each chi ∈{0, 1, 2} and the sum of
entries is 2 in each column of C. Let E(ei) = Ei ⊂Z2N be the edge equation coe
cients
corresponding to edge ei in T, and let
(19)
Λ =
( X
k∈ZN
kiEi
)
⊂Z2N
be the lattice of all integer linear combinations of these. In other words, Ei is the ith row of
the Neumann-Zagier matrix (A | B), and Λ is the integer row space of this matrix.
From the work of Neumann and Zagier (see [NZ85] and [Neu92, Thm 4.1]), the lattice
Λ has rank N −r and the matrix C gives the linear relations between the edge equation
coe
cients Ei ∈Z2N. More precisely,
(20)
X
i
chiEi = 0 for all h = 1, . . . , r
and any other linear relation between the Ei arises from a real linear combination of the
rows of C.
De
nition 4.2. A subset of the edges of a graph Γ is a maximal tree with 1- or 3-cycle in Γ
if (together with the vertices) it consists of any maximal tree T together with one additional
edge that either (1) is a loop at one vertex, or (2) forms a 3-cycle together with two edges
in T.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD
21
Theorem 4.3. There exists an integer basis for Λ consisting of N −r of the edge equation
coe
cients E1, . . . , EN. In fact, we can choose such a basis by omitting r edge equations
corresponding to a maximal tree with 1- or 3-cycle in G.
Remark 4.4. In other words, we can choose any maximal tree with 1- or 3- cycle for our set
X of excluded edges, and hence choose the remaining edges as our set B of basic edges.
This result and its proof were inspired by Je Weeks' argument in [Wee85, pp. 3536].
Proof. First we show that we can 
nd a maximal tree with 1- or 3-cycle. If there exists a loop
in G we use this loop together with any maximal tree. If not, any face of the triangulation
has its ideal vertices on 3 distinct cusps. Pick two edges of this face and extend these to a
maximal tree T ⊂G. Adding the third edge of the face gives the desired subgraph.
Now let S be a maximal tree with 1- or 3-cycle. Next we show that the N −r equations
E(e) corresponding to the edges e /∈S give an integer basis for Λ. We show that for each
s ∈S, the equation E(s) can be written as an integer linear combination of the equations
E(e) with e /∈S. Given this, the N −r equations E(e) with e /∈S form an integer spanning
set for Λ. The work of Neumann and Zagier ([NZ85] and [Neu92, Thm 4.1]), implies that
these equations are also linearly independent, hence form an integer basis for Λ, and we are
done.
So, we have to show that every E(s) can be written as an integer linear combination of
the E(e) for e /∈S. To organise the construction, we use the following sequence of decorated
graphs. At each step we have a graph Gk whose edges are labelled by names of edges of G.
We decorate each end of each edge of Gk with a sign. Each vertex v of Gk is then incident
to a set of ends of edges with signs. We list the names of the edges, together with the sign
associated to this end: {(eiv(1), ϵv(1)), (eiv(2), ϵv(2)), . . . , (eiv(d), ϵv(d))}. Here d is the degree
of the vertex v. To this vertex we associate the equation
Rk(v) =
d
X
l=1
ϵv(l)E(eiv(l)) = 0.
For each Gk we have a subset Sk of the edges of Gk which is a maximal tree with 1-or
3-cycle in Gk. We set G0 = G and S0 = S, with all signs set to +. Note that the equations
associated to the vertices of G0 are then the same as those given by (20).
We obtain the graph and edge subset (Gk+1, Sk+1) from (Gk, Sk) as follows. We arbitrarily
choose a vertex v of Gk that has only one end of one edge s of Sk incident. If there are no
such vertices then the sequence ends at (Gk, Sk). Let w be the other end of s, which by
assumption is distinct from v. The graph Gk+1 is the result of collapsing the edge s of Gk;
the two ends of s, v and w, are identi
ed in Gk+1. We label the edges of Gk+1 with the same
names as in Gk and set Sk+1 = Sk \ {s}. All of the signs decorating Gk+1 are the same as
in Gk, except that the ends of edges that were incident to v have their signs 
ipped. See
Figure 8.
Note that at each step of the sequence, both ends of each element of Sk have a + sign,
since they do in G0 and we never collapse an edge from a vertex with more than one incident
edge end in S. Consider the equations associated to the vertices of Gk and Gk+1. We have
22 STAVROS GAROUFALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
v
w
s
+
+
−
+
−
+
+
+
+
+
+
+
+
+
+
−
+
−
Figure 8. Collapsing the edge s 
ips the signs on the ends of the edges
incident to v. Edges in S are drawn dashed.
Rk(v) = +E(s)+
X
l,eiv(l)̸=s
ϵv(l)E(eiv(l)) = 0,
Rk(w) = +E(s)+
X
m,eiw(m)̸=s
ϵw(m)E(eiw(m)) = 0.
If we use Rk(v) to solve for E(s) we get
E(s) =
X
l,eiv(l)̸=s
−ϵv(l)E(eiv(l)).
Substituting this into Rk(w) gives
X
l,eiv(l)̸=s
−ϵv(l)E(eiv(l)) +
X
m,eiw(m)̸=s
ϵw(m)E(eiw(m)) = 0.
This is the equation associated to the vertex of Gk+1 formed by the identi
cation of v with
w. Thus, the sequence of graphs gives an expression for E(s) for each edge s ∈S which is
removed.
This expression is an integer linear combination of the E(e) for e /∈S. The sequence ends,
at GK say. By construction GK has no vertices for which only one end of an edge of S is
incident. If we are in case (1) of De
nition 4.2 then GK has one vertex, SK has one edge
and GK looks like Figure 9 (left). If we are in case (2) then GK has three vertices, SK has
three edges, and GK looks like Figure 9 (right).
In the 
rst case, the equation from the last vertex is of the form
2E(s) +
X
l,ei(l)̸=s
ϵ(l)E(ei(l)) = 0.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD
23
s
+
+
+
+
−
+
−
−
(a)
The
last
graph
when
S
has a 1-cycle.
sz
sx
sy
y
x
z
X
Z
Y
+
+
+
+
+ +
−
+
+
−
−
−
+
−
−+
−
−
+
−
(b) The last graph when S has a
3-cycle.
Figure 9. The last graph in the sequence has one of these two forms.
Notice that since all edges are now loops, each E(ei) appears with total coe
cient either
−2, 0 or 2. So we can divide the entire equation by 2, and get E(s) as an integer linear
combination of the E(ei).
The second case is slightly more complicated. We have three vertices x, y, z, with three
edges sx, sy, sz ∈S connecting the vertices into a triangle. The three vertices give equations
of the form
E(sy) + E(sz) + X = 0,
E(sz) + E(sx) + Y = 0,
E(sx) + E(sy) + Z = 0,
where X, Y, Z are terms coming from the edges not in S. We can solve these equations for
E(sz) as
2E(sz) = −X −Y + Z,
and the other two expressions similarly. We just have to show that −X −Y + Z has even
coe
cients, and then we will be done.
As before, any loops contribute a coe
cient in
{−2, 0, 2} to one of X, Y or Z. For edges with the same endpoints as one of sx, sy or sz, their
coe
cients are 1 or −1 at two of X, Y and Z and 0 at the third. Thus their contribution to
−X −Y + Z is also in {−2, 0, 2}, and so −X −Y + Z has even coe
cients, as required.
□
Example 4.5. The following example shows that the edges omitted must be chosen carefully
in the multi-cusped case. Let M be the Whitehead link complement (with the triangulation
given by m129 in SnapPy notation). Then the matrix of edge equations is
(A | B) =




2
−1
1
1
1
−2
0
0
−1
0
0
0
−1
1
1
1
0
1
−1
−1
1
0
−2
−2
−1
0
0
0
−1
1
1
1




24 STAVROS GAROUFALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
The cusp incidence matrix is
C =

1
2
1
0
1
0
1
2

and the corresponding graph G is shown in Figure 10.
e1
e3
e0
e2
c0
c1
Figure 10. The graph of edges and cusps for the Whitehead link.
The rows E0, E1, E2, E3 of (A | B) satisfy the relations:
E0 + 2E1 + E2 = 0 (from cusp 0)
and
E0 + E2 + 2E3 = 0 (from cusp 1),
which imply that E1 = E3.
It follows that E0, E1 are linearly independent and form an integer basis for the Z-span of
{E0, E1, E2, E3}. (This basis corresponds to removing the edge e2 in a maximal tree and an
additional loop e3.)
On the other hand, E0, E2 are also linearly independent and 2E1 is in the Z-span of
{E0, E2} but E1 is not in Z-span of {E0, E2}. So Z-span{E0, E2} is an index 2 subgroup in
Z-span{E0, E1}. Thus, a summation using E0, E2 will most likely give a dierent result for
the index than using E0, E1.
