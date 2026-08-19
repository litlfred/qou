---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-022-8-the-invariant-ptolemy-varieties
section_title: "The invariant Ptolemy varieties"
section_number: 8
pages: 20-21
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety forSL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
subsets ofA(V (M)).
Proposition 8.2. The invariant Ptolemy varieties are indeed varieties. Changing the triangu-
lation changes the varieties by biregular isomorphisms.
Proof. We prove this forP (T ); the proof for the other variants are identical. We must prove
that P (T ) has an open aﬃne cover. For each transitive edge set(T,E ) consider the triangu-
lation T (E) deﬁned as follows: ifE is non-degenerate or edge-degenerate,T (E) = T ; if E is
moderately, or simplex-degenerate, deﬁneT (E) to be a triangulationT′ as in Deﬁnitions 7.14
or 7.18, respectively. By deﬁnition, the invariant Ptolemy varietyP (T ) is then given by
(8.2) P (T ) =
⋃
E∈T(T )\{0}
F∈T(T (E)),F|T =E
P (T (E),F ).
Note that all transitive edge sets(T (E),F ) in the above union are (at worst) edge-degenerate.
Let W∈ V (M) be the union of allV (T (E)), i.e.W is the set of virtual edgese such thate is
an edge of one of theT (E). By Proposition 7.10, we may regardP(T ) as a subset of the ﬁnite
dimensional aﬃne spaceA(W ). Recall that A(W ) is given by a coordinatece for each virtual
edge inW. For a transitive edge set(T′,E′) let
(8.3) U(T′,E′) =
{ ∏
e∈E′
⁄=0
ce⁄= 0
}
∈A(V (M)),
where E′
⁄=0 denotes the set of nonzero edges of(T′,E′). Clearly,U(T′,E′) is Zariski open, and
(8.4) (T′,E′)⊂ (T′,E′′) ⇐⇒ U(T′,E′)⊂U(T′,E′′).
Also, for any transitive edge sets(T′,E′) and (T′′,E′′) we clearly have
(8.5) E′
=0∩E′′
⁄=0⁄=∅ =⇒ P (T′,E′)∩U(T′′,E′′) =∅.
From this it follows that for anyE∈ T(T ) and anyF∈ T(T (E)), we have
(8.6) P (T )∩U(T (E),F ) =
( ⋃
(T,E′)≤(T,E)
P (T,E′)
)
∩U(T (E),F )⊂A(W ).
By Proposition 7.10 the right-hand side of (8.6) canonically embeds inA(V (T (E))). Let X
be the aﬃne variety inA(V (T (E))) cut out by the Ptolemy relations, identiﬁcation relations,
and edge orientation relations forT (E) together with the edge relations around zero-edges of
F. Since (T (E),F )) is (at worst) edge-degenerate, there are no points inX∩U(T (E),F ) that
violate transitivity, so all points inX∩U(T (E),F ) are in P (T,E′) for some E′ ∈ T(T ) with
(T,E′)< (T,E ). It thus follows from (8.6) thatX∩U(T (E),F ) equals P (T )∩U(T (E),F ). Since
TRIANGULATION INDEPENDENT PTOLEMY V ARIETIES 21
U(T (E),F ) is the non-vanishing set of a single polynomial,X∩U(T (E),F ) is aﬃne. This concludes
the proof of existence of an aﬃne cover ofP (T ).
Given another triangulationT′, P (T ) and P (T′) are clearly isomorphic as sets since both
parametrize non totally degenerate decorations. The fact that they are also equal as varieties
follows from the fact that the images ofP (T ) and P (T′) in A(V (M)) are equal (see the proof
of Proposition 7.10). □
9. The reduced Ptolemy v arieties
The diagonal action on decorations, Ptolemy assignments, and natural cocycles extends canon-
ically to the case where some of the Ptolemy coordinates are zero and some of the long edges
are diagonal instead of counterdiagonal. We deﬁne the reduced Ptolemy varietyP red(T ) to be
the quotient ofP (T ) by the diagonal action. In [8] we showed that the reduced Ptolemy variety
P (T )red can be computed by setting appropriately chosen Ptolemy coordinates equal to1:
Theorem 9.1 ([8, Prop. 1.16]). Let G be a connected graph in the one-skeleton ofˆM, which
has fundamental group Z and contains all vertices. The reduced Ptolemy variety P (T )red is
isomorphic to the subvariety ofP (T ) where the Ptolemy coordinates of all edges inG are 1. The
same result holds forPσ(T )red.
Remark 9.2. In [8] this is only proved whenG is a so-called “maximal tree with1- or 3-cycle”,
but the proof can be trivially extended to any graph with fundamental groupZ containing all
vertices.
Theorem 9.3. Let E ∈ T(T ) be edge-degenerate. Then, there exists a graphG of nonzero
edges which has fundamental group Z and contains all vertices. The reduced Ptolemy variety
P (T,E )red is isomorphic to the subvariety ofP (T,E ) where the Ptolemy coordinates of all edges
in G are 1. The same result holds forPσ(T,E )red andEP (T,E )red.
Proof. SinceE is edge-degenerate, the set of nonzero edges connects all vertices ofT and contains
cycles. Thus, we can choose a graphG with the above properties. Hence, the result follows from
Theorem 9.1. The proofs trivially extend to the case ofEP (T,E )red. □
