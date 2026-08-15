---
doc_id: arxiv-2411.03801v2
doc_title: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS"
section_id: sec-009-41-flattening-of-the-collapsed-triangulation
section_title: "Flattening of the collapsed triangulation"
section_number: 4.1
pages: 14-17
source_pdf: 2411.03801v2.pdf
source_sha256: a7f1f6fa74cb0949
doc_brief: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS — Motivated by the conjectured asymptotics of the Kashaev invariant, Dimofte and the first author introduced a power series associated to a suitable ideal"
---
flatteningf = (f,f′,f′′) ofT˚D. Recall from Section 2.1 thatf consists of integer triplesfj =
(fj,f′
j,f′′
j )∈ Z 3, one for each tetrahedron ∆j ofT˚D and is required to satisfyfj +f′
j +f′′
j = 1
for each ∆j and
ei :
X
j
Gijfj +G′
ijf′
j +G′′
ijf′′
j = 2 (9)
for each edge ei. We denote by⟨f,ei⟩ the left-hand side of Equation (9).
We fix a quad type of each ∆ j so that fj is assigned to the vertical and horizontal edges
of ∆j (the edges 0∞ and xy in Figure 4). Denoting ∆ j with a corner of ˚D, we choose an
integer triplefj as follows.
fj =



(1, 0, 0) for the N and S-corners of a crossing
(0, 1, 0) for the E and W-corners of a positive crossing
(0, 0, 1) for the E and W-corners of a negative crossing .
(10)
Here N, E, S or W indicates the position of a corner with respect to the nearby crossing.
Note that each tetrahedron has two edges assigned with 1 and four edges assigned with 0.
When we compute⟨f,e⟩, the ones with 0 have no influence, and thus it suffices to consider
the ones with 1, which are marked by red in Figure 12.
Recall from Section 3 thatT˚D has four edge-types: C, R, O and U-edges. We first compute
⟨f,e⟩ for C and R-edges. As these edges recieve contributions only from fj’s (not from f′
j’s
and f′′
j ’s), only N and S-corners are involved in the computation. For simplicity we call a
segment with κ∈{ 0, 1,∞} assigned a κ-segment.
Lemma 4.2. We have⟨f,e⟩ = 2 for all C-edges e.
1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS 15
Figure 12. A choice of f.
Proof. Recall that a C-edge corresponds to a crossing with no adjacent 0 and ∞-segments.
Thus a corner around it is essential, unless adjacent segments are both 1-segments. Given
that ˚D is given as in Figure 11, both the N and S-corners are essential and contribute 1 to
⟨f,e⟩. This proves that ⟨f,e⟩ = 2. □
Lemma 4.3. We have⟨f,e⟩ = 2 for all R-edges e.
Proof. Let us consider a region of ˚D that corresponds to an R-edge e. The S-corner of the
topmost crossing contributes 1 to⟨f,e⟩. Similarly, the N-corner of the bottommost crossing
contributes 1 to ⟨f,e⟩. The other crossings that are neither top nor bottom ones have no
contribution; see Figure 12. This proves that ⟨f,e⟩ = 2. □
We now compute ⟨f,e⟩ for O and U-edges. Recall that O and U-edges correspond to
over and under-arcs of ˚D, respectively. In what follows, for simplicity we confuse an over
or under-arc of ˚D with the corresponding O or U-edge of T˚D. In addition, we assume that
starting from the top endpoint of ˚D, we underpass the first crossing (thus from the bottom
endpoint, we overpass the first crossing). The opposite case can be proved similarly by
exchanging the roles of∞ and 0.
The diagram ˚D has one cap, and we choose one crossing c∞ and one segment s∞ around
it shown as in Figure 13. Similarly, we choose one crossing c0 and one segment s0 around
the cup of ˚D as in Figure 13. We denote by oκ anduκ forκ = 0,∞ the over and under-arcs
containing the segment sκ, respectively.
c∞
c0 c0
s0 s0
s∞
or
Figure 13. Cap and cup of ˚D.
16 STA VROS GAROUF ALIDIS AND SEOKBEOM YOON
Lemma 4.4. For an O or U-edge e, we have
⟨f,e⟩ =



3 if e =u∞ or o0,
1 if e =o∞ or u0,
2 otherwise .
Proof. Following the diagram from the top endpoint, we encounter all over and under-arcs.
Thus for each O and U-edge we can think of a crossing where it starts or ends. Except
for the four edges u0,u∞,o 0 and o∞, every O and U-edge e,⟨f,e⟩ receives one from the
crossing where it starts and another one from where it ends; see Figure 12. This proves that
⟨f,e⟩ = 2. Note that this includes the case when an O-edge and a U-edge are identified.
Such identification happens when they meet at the W or E-corner lying in the unbounded
region, and the fact that we do not have a tetarhedron at that corner preserves the fact
⟨f,e⟩ = 2.
Fore =u∞, it receives one from the crossing where it starts and another one from where
it ends, as before. However, as the face-gluing around c∞ is different from other crossings,
i.e., as the vertical edge at c∞ is identified with u∞, it receives one additional contribution
from c∞.
It follows that⟨f,e⟩ = 3. We deduce the same for e =u0 similarly.
Fore = o∞,∞-segments make corners around the crossing where it starts not essential.
This results in a tetrahedron being missing at the E or W-corner of its start crossing, and
thus⟨f,e⟩ = 1. We deduce the same for e =u0 similarly. □
Lemma 4.5. Let ei and ej be two edges of T˚D that correspond to consecutive under or
over-arcs. Then there is a triple g = (g,g′,g′′) of vectors such that gj +g′
j +g′′
j = 0 and
⟨f +g,e⟩−⟨ f,e⟩ =



−1 if e =ei
1 if e =ej
0 otherwise .
In addition, such g can be chosen independently of f .
Proof. Leta1 anda2 be the over or under-arcs corresponding to the edges ei andej, respec-
tively. As they are adjacent, there is a common crossing. If a1 and a2 are under-arcs, then
we defineg by assigning integer triples to the corners at the common crossing as in Figure 14
(left); if a1 anda2 are over-arcs, then as in Figure 14 (right). Then one can easily check that
g satisfies the desired condition.
a2
(0, 1,−1)(0, 1,−1)
(0,−1, 1)(0,−1, 1)
a1 a2a1
Figure 14. A choice of g.
□
1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS 17
Remark 4.6. In the proof of Lemma 4.5, we used two tetrahedra that are below the arcs a1
and a2, but one may use two tetrahedra that are above the arcs. This implies that a choice
ofg is not unique. However, regardless of a choice of g, the product
ζg :=
Y
j
ζ
gj
j ζ′
j
g′
jζ′′
j
g′′
j
is invariant: if there are two choices g1 andg2, then for any flattening f ofT˚D,f +g1−g2
is also a flattening, and thus
ζf+g1−g2 =ζf ⇒ ζg1 =ζg2.
Explicitly,ζg agrees with z1z2 for Figure 19 (left) and with 1 /(z1z2) for Figure 19 (right)
where z1 and z2 are shape parameters placed at the corners shown as in Figure 19.
Roughly speaking, Lemma 4.5 allows us to take one contribution from an arc, either over
or under, and give it to the next arc, and thus to any arc by applying the lemma multiple
times. We take one contribution from o0 (resp., u∞) and give it to o∞ (resp., u0). This
results in a triple g such that (see Lemma 4.4)
⟨f +g,e⟩ = 2
for all edges e. Namely, f +g is a flattening ofT˚D.
