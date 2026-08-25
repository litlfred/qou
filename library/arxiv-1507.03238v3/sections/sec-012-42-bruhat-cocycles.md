---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-012-42-bruhat-cocycles
section_title: "Bruhat cocycles"
section_number: 4.2
pages: 11-13
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety forSL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
Deﬁnition 4.5.A Bruhat cocycleis a natural cocycle as in Deﬁnition 2.16, but where long edges
may be either diagonal or counter-diagonal. A zero-cochainη : V (T )→ P preserves a Bruhat
cocycle τ if ητ is again a Bruhat cocycle.
The motivation for our deﬁnition is the following corollary of the Bruhat decomposition the-
orem.
Lemma 4.6. Let gP and hP be cosets. If gB ⁄= hB there are unique coset representatives
gx0 and hx1 such that (gx0)−1hx1 is counterdiagonal. IfgB =hB there are (not unique) coset
representatives such that(gx0)−1hx1 is diagonal.
Proof. By Bruhat decomposition, everyg∈ G can be decomposed asb1wb2, wherew is either( 0−1
1 0
)
or ( 1 0
0 1 ) and bi∈B. The result is an elementary consequence. □
Corollary 4.7. For every decorationD = (g0P,g 1P,g 2P,g 3P ) of a simplex ∆ there exists a
Bruhat cocycleτ on the corresponding truncated simplex∆ compatible withD. Moreoverτ is
unique up to coboundaries preservingτ.
Proof. Lemma 4.6 provides the existence of a mapη : V (∆)→G such thatδη is a Bruhat cocycle
(see Figure 6). Uniqueness up to coboundaries and compatiblity withD is immediate from the
construction. □
The following is the global analogue of Corollary 4.7.
Theorem 4.8. There is a one-to-one correspondence
(4.2)
{
Decorated boundary-unipotent
SL(2, C)-representations
}
1:1←→
{
Bruhat cocyclesτ up to
coboundaries preservingτ
}
.
Proof. We must show that given a decorationD there exists a Bruhat cocycleτ compatible
with D and that τ is unique up to the action by coboundaries preservingτ. A decoration
D : I(~M)→ SL(2, C)/P of a representationρ determines a mapΓ: V (~T )→ SL(2, C)/P deﬁned
by taking a vertex near an ideal vertexv to the coset assigned tov. We shall construct aρ-
equivariant lift of Γ to a mapη : V (~T )→ SL(2, C) such that ˜τ = δη is a natural cocycle on
~T descending to a natural cocycleτ onT . Any cocycle compatible with D arises from this
construction (since~M is simply connected all lifts are coboundaries). Fix an orientation of each
long edgee ofT , and a lift˜e of e. Each vertex of~T is then in theπ1 orbit of exactly one of
the vertices ˜e0 and ˜e1. By ρ-equivariance it is thus enough to deﬁneη on the set of endpoints
˜e0 and ˜e1. Now deﬁneη(˜ei) =gixi, where Γ(˜ei) =giP and xi∈P is an element as provided by
Lemma 4.6. By construction,δη is a Bruhat cocycle descending to a Bruhat cocycle onT . The
freedom in the choice ofη is exactly the action by coboundaries preservingτ. This proves the
result. □
12 MATTHIAS GOERNER AND CHRISTIAN K. ZICKERT
4.2.1. Explicit formulas via Ptolemy coordinates.Note that the labelings of the long edges are
canonically determined, whereas a short edge is canonically determined if and only if it connects
two counter diagonal long edges. The result below, generalizing the correspondence in Figure 2,
gives explicit formulas for the canonically determined edges in terms of Ptolemy coordinates when
at most one Ptolemy coordinate per face is zero (the edge-degenerate case; see Deﬁnition 6.4).
Fora∈ C and b∈ C\{ 0} let
(4.3) x(a) =
(
1 a
0 1
)
, q (b) =
(
0 −b−1
b 0
)
, d (b) =
(
b 0
0 b−1
)
.
Proposition 4.9. Let αij and βk
ij be the labelings of long and short edges of a Bruhat cocycle
coming from a decoration(g0P,g 1P,g 2P,g 3P ). Ifcij are the Ptolemy coordinates, we have
(4.4)
αij =q(cij) if cij⁄= 0.
βk
ij =x( cij
cikckj
) if cikckj⁄= 0.
αij =−d(c−1
ik ckj) if cij = 0 and cikckj⁄= 0.
Proof. The ﬁrst formula only involves a single edge and is thus independent of whether or not
the remaining Ptolemy coordinates are zero. The second only involves the faceijk and holds by
the fundamental correspondence ifcij⁄= 0 and forcij = 0 as well by analytic continuation. The
third is a consequence of the ﬁrst two using the cocycle condition. □
Remark 4.10. IdentifyingP with C via ( 1 x
0 1 )↔x allows us to view the labelings of the short
edges near an ideal vertexv ofM as complex vectors. The action of a coboundary taking a vertex
v to x∈ C (keeping all other vertices ﬁxed) then corresponds to movingv byx (see Figure 5).
v
v+x
g0P
g1P
g2P
g3P
g0x01
g1x10
g0x02
αij=x−1ijg−1i gjxji
βkij=x−1kixkj
g2x23
g3x32
g3x31
g0x03
g1x13
g3x30
g2x20
g2x21
g1x12
Figure 5. The action by
coboundary corresponds to
moving the “center” point.
Figure 6. The natural cocy-
cle from a decoration.
4.3. PSL(2, C)-representations. The analogue of Theorem 4.8 forPSL(2, C)-representations
and PSL(2, C) Bruhat cocycles also holds. The proof is identical to that of Theorem 4.8 using
the obvious analogues of Lemma 4.6 and Corollary 4.7 forPSL(2, C).
TRIANGULATION INDEPENDENT PTOLEMY V ARIETIES 13
