---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUT A TIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-016-b1-rotation-and-excess-numbers
section_title: "B.1. Rotation and Excess numbers"
section_number: null
pages: 19-20
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent p olynomials that encodes the Jones polynomial of a knot and its parallels."
---
edges of GK so that for each admissible state s and its corresponding (see Lemma B.2) admissible subgraph
c of GK, rot( s) =∑
e∈c rot(e).
Deﬁnition B.6. There is a Gauss map d :K →S1 which together with the orientation of K and the
counterclockwise orientation of S1 induces a map
H1(PK, Z)−→ H1(S1, Z)∼
= Z.
The above composition is deﬁned to be the rotation number rot. We c an think of the rotation number as an
element of H 1(PK, Z) represented by a 1-cocyle, that is a map
rot : Edges( PK)−→ Z.
Consider now the arc-graph GK ofK. There is a canonical map
Edges(GK)−→ 2Edges(PK)
deﬁned as follows: if ( i, j) is an edge of GK, consider the ith crossing of PK, and start walking on the part
of the arc aj in a direction of the orientation of K, until the end of the arc aj. This deﬁnes a collection
of part-arcs that we associate to the edge ( i, j) of GK. Taking the sum of the rotation numbers of these
part-arcs, deﬁnes a map
rot : Edges( GK)−→ Z.
Next we show that exc ′ of next deﬁnition agrees with exc of Deﬁnition 4.1.
Deﬁnition B.7. Let c be an admissible subgraph of GK. We let exc ′(c) equal to exc( s), where s is the
corresponding admissible state (see Deﬁnition B.4 and Lemma B.2 for t he correspondence).
Lemma B.8. For every admissible subgraph c of GK, we have:
exc′(c) = exc( c).
Proof. exc′(c) is the sum of sign( v) where all 4 edges incident to a crossing v of K belong to c:
a v+1
a w
a v
We will translate this in the language of the arc-graph GK, using Figure 1. A crossing v as above determines
a unique vertex of GK (corresponding to the arc av ending at v) and a unique pair of edges ( e, e′) of GK : e
is the blue edge that starts at v, and e′ is the unique edge of c that ends in w and signiﬁes the transition on
the arc aw. The result follows. □
19
Proof. (of Theorem 5)
Assume (after possibly changing the orientation of the knot, which does not change the Jones polynomial)
that we mark by ⋆ the last partarc of an arc of K. Lemma B.2, (8), and subsection B.1 conclude the proof
of Theorem 5. □
