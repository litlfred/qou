---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-019-71-edge-degenerate-edge-sets
section_title: "Edge-degenerate edge sets"
section_number: 7.1
pages: 16-18
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety forSL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
at most one zero-edge.
Proposition 7.1. Letc be a Ptolemy assignment on a simplex∆. If each face has at most one
Ptolemy coordinate which is zero, thenc is the Ptolemy assignment of a unique decoration.
Proof. By reordering the vertices if necessary, we may assume thatc01,c12 andc23 are nonzero.
Let
(7.1) g0 =I, g 1 =q(c01), g 2 =g1x( c02
c01c12
)q(c12), g 3 =g2x( c13
c12c23
)q(c23).
The Ptolemy coordinates of the decoration(g0P,g 1P,g 2P,g 3P ) then agree withc as is shown by
explicitly computingdet
(
gi ( 1
0 ),gj ( 1
0 )
)
. Uniqueness follows from Corollary 4.7 since the natural
cocycle is determined up to coboundaries by the Ptolemy coordinates (Proposition 4.9). □
Let C(E) be a union of disjoint cylindrical neighborhoods of the zero-edges ofE. The space
M\C(E) decomposes as a union of truncated simplices with the zero-edges being “chopped”
(see Figure 11).
Corollary 7.2. A Ptolemy assignmentc of typeE canonically determines aG-cocycle on the
space M\C(E).
Proof. ByProposition7.1andCorollary4.7, cdeterminesuptocoboundariesaBruhatcocycleon
each truncated simplex. By Proposition 4.9, all the long edges are canonically determined by the
Ptolemy coordinates, but a short edge near a zero-edge is only determined up to the coboundary
action. However, as shown in Figure 11, each chopped truncated simplex inherits canonical
edge labelings. The fact that the chopped cocycles match up follows from the identiﬁcation
relations. □
The link of each zero-edge is a complexK as in Section 5 (embedded inˆ~M) and sinceE is
only edge-degenerate, the top and bottom edges ofK are all nonzero. Hence, for a Ptolemy
assignment of typeE the edge relations (Deﬁnition 5.2) around each zero-edge are well deﬁned.
TRIANGULATION INDEPENDENT PTOLEMY V ARIETIES 17
I
I
β123β123
α12
α12
α01
α01
0
1
3
2
β201
β213
β123,0
β123,1
β123,2
β123,1β123,0
β123,N−1
β123,2
Figure 11. Natural cocycle af-
ter removing a neigborhood of a
zero-edge.
Figure 12. The cocycle ex-
tends if and only if the edge
relation holds.
Deﬁnition 7.3.LetE be edge-degenerate. The Ptolemy varietyP (T,E )is the quasi-aﬃne alge-
braic set deﬁned by the usual relations (as in Deﬁnition 2.3) together with the edge relations (5.1)
around zero-edges and the relationsce = 0 if e is a zero-edge andce⁄= 0 otherwise.
Note that each element inP (T,E ) is a Ptolemy assignment of typeE.
Theorem 7.4. LetE∈ T(T ) be edge-degenerate. There is a one-to-one correspondence
(7.2)
{
Decorated, boundary-unipotent
representations of typeE
}
1:1←→P (T,E ) 1:1←→
{
Bruhat cocycles of typeE
up to coboundaries
}
Proof. By Theorem 4.8 all we need to prove is that a Ptolemy assignment of typeE determines a
Bruhat cocycle. By Corollary 7.2, we have a canonical cocycle onM\C(E). By the van Kampen
theorem this extends to a Bruhat cocycle onM if and only if the product of the labelings around
each cylinder isI, which is a consequence of the edge relations. The freedom in the choice of
extension is exactly the coboundary action (see e.g. Remark 4.10). □
Deﬁnition 7.5.For σ ∈ H 2(ˆM; Z/2Z) deﬁnePσ(T,E ) as in Deﬁnition 7.3, but using the
identiﬁcation relations (3.1).
Theorem 7.6. LetE∈ T(T ) be edge-degenerate. There is a one-to-one correspondence
(7.3)



TypeE decorated
boundary-unipotent
π1(M)→ PSL(2, C)


 mm
1:1
00Pσ(T,E )1:koo k:1 //



Bruhat PSL(2, C)-cocycles
typeE, obstruction classσ
up to coboundaries


,
Proof. As in the proof of Theorem 7.4 an element inPσ(T,E ) determines a Bruhat cocycle
up to coboundaries. The fact that this map isk : 1 follows from the elementary fact that two
Ptolemy assignments determine the same Bruhat cocycle if and only if they diﬀer by an element
in Z1(ˆM; Z/2Z). □
Deﬁnition 7.7.ForM as in Section 3.2 deﬁne the enhanced Ptolemy varietyEP (T,E ) as in
Deﬁnition 7.3 using the identiﬁcation relations from Deﬁnition 3.4 and the edge relations (5.4).
Theorem 7.8.LetE∈ T(T ) be edge-degenerate andM as in Section 3.2. There is a one-to-one
correspondence
(7.4)
{
Decorated representations
of typeE
}
1:1←→EP (T,E ) 1:1←→
{
Fattened Bruhat cocycles of typeE
up to coboundaries
}
18 MATTHIAS GOERNER AND CHRISTIAN K. ZICKERT
Proof. The proof is identical to that of Theorem 7.4 using the fattened decomposition and the
geometric interpretation of the edge relations (5.4) given in Figure 10. □
7.2. Embeddings in aﬃne space.
Deﬁnition 7.9.A virtual edgeof M is an element in the set
(7.5) V (M) =
(
I(~M)×I(~M)
)/
π1(M)
of pairs of ideal points in~M up to theπ1(M)-action.
Given an ideal triangulationT , each oriented edgee ofT determines a virtual edge, namely
the orbit of(e0,e 1). Hence,T determines a (ﬁnite) subsetV (T ) of V (M).
For each subsetV ofV (M) letA(V ) denote the aﬃne space with coordinate ring equal to the
polynomial ring generated byV. ForV ⊂W we have a canonical projectionπ : A(W )→A(V )
onto a direct summand. We wish to embed the Ptolemy varietyP (T,E ) inA(V (M)). The idea
is that a decoration assigns a Ptolemy coordinate to every virtual edge, not just the edges ofT .
Proposition 7.10. Let E∈ T(T ) be non- or edge-degenerate. There is a canonical embedding
of P (T,E ) in the (inﬁnite dimensional) aﬃne spaceA(V (M)). Furthermore, for each ﬁnite
subset W of V (M) containingV (T ) the map
(7.6) P (T,E )  //A(V (M)) π //A(W )
is an embedding ofP (T,E ) in the ﬁnite dimensional aﬃne spaceA(W ).
Proof. Bydeﬁnition,P (T,E )isaquasi-aﬃnesubsetof A(V (T )). ToembedP (T,E )inA(V (M)),
we must construct a surjective map from the coordinate ringOA(V (M )) of A(V (M)) to the co-
ordinate ringO of P (T,E ). By Corollary 7.2 we have a canonical Bruhat cocycle on the space
M\C(E) with edges labeled by matrices inSL(2,O). This cocycle canonically lifts to a cocycle
on ~M\C(E). Given a virtual edgee = (e0,e 1), one obtains a matrixBe in SL(2,O) by selecting
a path in ~M\C(E) joining e0 to e1. Up to left and right multiplication by elements inP the
matrixBe is independent of the choice of path, so the determinantce = det(( 0
1 ),Be ( 0
1 )) is well
deﬁned. Moreover, ife corresponds to an edge ofT , ce is simply the Ptolemy coordinate of
e. One thus obtains a surjectionOA(V (M ))→O by taking a virtual edgee to ce. The second
statement is obvious. □
Remark 7.11. The same result holds forPσ(T,E ). ForEP (T,E ) one must consider embed-
dings into an aﬃne space generated by pairs of triangular faces of~T instead of virtual edges.
