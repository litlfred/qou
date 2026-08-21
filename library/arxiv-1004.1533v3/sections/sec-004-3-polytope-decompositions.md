---
doc_id: arxiv-1004.1533v3
doc_title: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT"
section_id: sec-004-3-polytope-decompositions
section_title: "Polytope decompositions"
section_number: 3
pages: 10-15
source_pdf: 1004.1533v3.pdf
source_sha256: 95c1544431e6bf37
doc_brief: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT — In this paper we show how one can extend Turaev-Viro invarian ts, deﬁned for an arbitrary spherical fusion category C, to 3-manifolds with cor- ners."
---
It will be convenient to rewrite the deﬁnition of Turaev–Viro (TV) inv ariants
using not just triangulations, but more general cellular decomposit ions. In this
section we give precise deﬁnitions of these decompositions.
In what follows, the word “manifold” denotes a compact, oriented, piecewise-
linear (PL) manifold; unless otherwise speciﬁed, we assume that it ha s no boundary.
Note that in dimensions 2 and 3, the category of PL manifolds is equiva lent to the
category of topological manifolds. For an oriented manifold M , we will denote by
M the same manifold with opposite orientation, and by ∂M , the boundary of M
with induced orientation.
Instead of triangulated manifolds as in [BW1996], we prefer to consid er more
general cellular decompositions, allowing individual cells to be arbitrar y polytopes
(rather than just simplices); moreover, we will allow the attaching m aps to iden-
tify some of the boundary points, for example gluing polytopes so th at some of
the vertices coincide. On the other hand, we do not want to conside r arbitrary
cell decompositions (as is done, say, in [Oec2005]), since it would make describing
the elementary moves between two such decompositions more comp licated. The
following deﬁnition is the compromise; for lack of a better word, we will call such
decompositions polytope decompositions.
Recall that a cellular decomposition of a manifold M is a collection of inclu-
sion maps Bd →M , where Bd is the (open) d-dimensional ball, satisfying certain
conditions. Equivalently, we can replace d-dimensional balls with d-dimensional
cubes I d = (0, 1)d. For a PL manifold, we will call such a cellular decomposition
a PL decomposition if each inclusion map (0 , 1)d → M is a PL map. In particu-
lar, every triangulation of a PL manifold gives such a cellular decompos ition (each
d-dimensional simplex is PL homeomorphic to a d-dimensional cube).
We will call a cell regular if the corresponding map (0 , 1)d → M extends to a
map of the closed cube [0 , 1]d →M which is a homeomorphism onto its image.
TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT 11
Deﬁnition 3.1. A polytope decomposition of a 2- or 3-dimensional PL manifold
M (possibly with boundary) is a cellular decomposition which can be obtain ed from
a triangulation by a sequence of moves M1—M3 below (for dim M = 2, only moves
M1, M2).
M1: removing a vertex: Letv be a vertex which has a neighborhood whose
intersection with the 2-skeleton is homeomorphic to the “open book ” shown
below with k ≥ 1 leaves; moreover, assume that all leaves in the ﬁgure are
distinct 2-cells and the two 1-cells are also distinct (i.e., not two ends o f
the same edge). Then move M1 removes vertex v and replaces two 1-cells
adjacent to it with a single 1-cell.
remove vertex v
− − − − − − − − − − →
Figure 8. Move M1
M2: removing an edge: Let e be a 1-cell which is regular and which is
adjacent to exactly two distinct 2-cells c1,c 2 as shown in the ﬁgure below.
Then the move M2 removes the edge e and replaces the cells c1,c 2 with a
single cell c.
remove edge e
− − − − − − − − − →
Figure 9. Move M2
M3: removing a 2-cell: Let c be a 2-cell which is regular and which is ad-
jacent to exactly two distinct 3-cells F1,F 2 as shown in the ﬁgure below.
Then the move M2 removes the 2-cell c and replaces the cells F1,F 2 with
a single cell F .
A 2 or 3-dimensional PL manifold M with boundary together with a choice of
polytope decomposition will be called a combinatorial manifold; for dim M = 2, we
will also use the term “combinatorial surface”. We will use script lett ers to denote
combinatorial manifolds and Roman letters for underlying PL manifold s.
Note that the extension of the inclusion maps (0 , 1)d →M to the boundary does
not have to be injective.
12 BENJAMIN BALSAM AND ALEXANDER KIRILLOV, JR.
remove face c
− − − − − − − − →
Figure 10. Move M3
If F is an oriented d-dimensional cell of a combinatorial manifold M (i.e., a
pair consisting of a cell and its orientation), we can deﬁne its bounda ry ∂F in the
obvious way, as a formal union of oriented ( d − 1)-dimensional cells. Note that ∂F
can contain the same (unoriented) cell C more than once: for example, one could
have∂F = · · · ∪C ∪C... .
Lemma 3.2. If M is a combinatorial manifold of dimension d with boundary, then
⋃
F
∂F =
( ⋃
C∈∂M
C
)
∪
(⋃
cin
c′
in ∪c′′
in
)
whereF runs over the set of d-cells of M (each taken with induced orientation ), C
runs over the set of (d − 1)-cells of ∂M (each taken with induced orientation ), and
cin runs over the set of (unoriented) (d − 1)-cells in the interior of M , with c′,c ′′
denoting two possible orientations of c (so that
c′ =c′′).
The main result of this section is the following theorem.
Theorem 3.3. LetM be a PL 2- or 3-manifold without boundary. Then any two
polytope decompositions of M can be obtained from each other by a ﬁnite sequence
of moves M1–M3 and their inverses (if dimM = 2, only moves M1, M2 and their
inverses).
Proof. It is immediate from the deﬁnition that it suﬃces to prove that any tw o
triangulations can be obtained one from another by a sequence of m oves M1–M3
and their inverses. On the other hand, since it is known that any two triangulations
are related by a sequence of Pachner bistellar moves [Pac1987], it su ﬃces to show
that each Pachner bistellar move can be presented as a sequence o f moves M1–M3
and their inverses. For dim M = 2, this is left as an easy exercise to the reader; for
dimM = 3, this is shown in Figure 11, Figure 12.
□
This can be generalized to manifolds with boundary.
Theorem 3.4. Let M be a PL 2- or 3-manifold with boundary and let N be a
polytope decomposition of ∂M . Then
(1) N can be extended to a polytope decomposition M of M .
(2) Any two polytope decompositions M1, M2 of M which coincide with N on
∂M can be obtained from each other by a ﬁnite sequence of moves M1 –M3
and their inverses which do not change the polytope decompos ition of ∂M .
Proof. The theorem immediately follows from the following two lemmas.
Lemma 3.5. If N is a triangulation, then the statement of the theorem holds.
TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT 13
remove face ADE
− − − − − − − − − − − →
remove edge DE
− − − − − − − − − − →
remove face CDBE
− − − − − − − − − − − − →
add face ABC
− − − − − − − − − →
Figure 11. Pachner 3-2 move as composition of elementary moves
Lemma 3.6. If N is obtained from another polytope decomposition N ′ of ∂M by
a move M1, M2 (only M1 if dimM = 2) , and the statement of the theorem holds
for N ′, then the statement of the theorem holds for N .
Proof of Lemma 3.5. Follows from the relative version of Pachner moves [Cas1995].
□
Proof of Lemma 3.6. We will do the proof in the case when dim M = 3 and N is
obtained from N ′ by erasing an edge e separating two cells c1,c 2. The proof in
other cases is similar and left to the reader.
Let M′ be a polytope decomposition of the M which agrees with N ′ on∂M ; by
assumption such a decomposition exists. Denote c =c1 ∪e ∪c2. Let us glue to M′
another copy of 2-cell c along the boundary of c1 ∪e ∪c2 and a 3-cell F ﬁlling the
space between c1 ∪e ∪c2 and c as shown in Figure 13
This gives a new manifold ˜M which is obviously homeomorphic to M , together
with a polytope decomposition ˜M such that its restriction to the boundary is N .
This proves existence of extension. Moreover, it is immediate from t he assumption
on N ′ that any two polytope decompositions ˜M1, ˜M2 obtained in this way from
polytope decomposition M′
1, M′
2 extending N ′ can be obtained from each other by
a sequence of moves M1, M2 and their inverses which do not change d ecomposition
of ∂M .
To prove the second part, let M1, M2 be two polytope decompositions which
coincide with N on∂M . Let us add 2-cells c1,c 2 and an edge e to to each of these
decomposition as shown in Figure 14; this gives new decompositions ˜M1, ˜M2 which
are of of the form discussed above and thus can be obtained from e ach other by a
14 BENJAMIN BALSAM AND ALEXANDER KIRILLOV, JR.
remove faces AOB,DOC
− − − − − − − − − − − − − − − − →
remove edges AO,OB
− − − − − − − − − − − − − − →
remove vertex O
− − − − − − − − − − →
remove edge DC
− − − − − − − − − − →
remove face ADBC
− − − − − − − − − − − − →
Figure 12. Pachner 4-1 move as composition of elementary moves
− →
Figure 13. Proof of Lemma 3.6
sequence of moves M1, M2 and their inverses which do not change de composition
of ∂M .
− →
Figure 14. Proof of Lemma 3.6
□
□
Finally, we will need a slight generalization of this result.
TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT 15
Theorem 3.7. LetM be a 3-manifold with boundary and let X ⊂∂M be a subset
homeomorphic to a 2-manifold with boundary. Let N be a polytope decomposition
of a X. Then
(1) N can be extended to a polytope decomposition M of M
(2) Any two polytope decompositions M1, M2 of M which coincide with N on
X can be obtained from each other by a ﬁnite sequence of moves M1 –M3
and their inverses which do not change the polytope decompos ition of X.
A proof is similar to the proof of the previous theorem; details are lef t to the
reader.
