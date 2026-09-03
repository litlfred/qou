---
doc_id: arxiv-2509.04267v3
doc_title: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY"
section_id: sec-010-20-masahico-saito-and-emanuele-zappala
section_title: "MASAHICO SAITO AND EMANUELE ZAPPALA"
section_number: 20
pages: 20-22
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
doc_brief: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
Theorem 6.1.The deformed YBO ˜R, pairing ˜∪and copairing ˜∩on ˜V=k[[ℏ]]/(ℏ 2)⊗Vsatisfy
the switchback, passcup, and passcap properties if and only if the following equations hold.
X
(i,j)∈Γ
(∪i⊗1)(1⊗∩ j) =1(10)
X
(i,j)∈Γ
(1⊗∪ i)(∩j⊗1) =1(11)
X
(i,j)∈Γ
(1⊗∪ i)(ϕj⊗1) =
X
(i,j)∈Γ
(∪i⊗1)(1⊗ ˆϕj) (12)
X
(i,j)∈Γ
(1⊗∪ i)(ˆϕj⊗1) =
X
(i,j)∈Γ
(∪i⊗1)(1⊗ϕ j) (13)
X
(i,j)∈Γ
(ϕi⊗1)(1⊗∩ j) =
X
(i,j)∈Γ
(1⊗ ˆϕi)(∩j⊗1) (14)
X
(i,j)∈Γ
(ˆϕi⊗1)(1⊗∩ j) =
X
(i,j)∈Γ
(1⊗ϕ i)(∩j⊗1) (15)
Moreover, if ˜ϕ, ˜∪and ˜∩satisfy the switchback, passcup and passcap identities, then they define
a knot invariant
ΦM
( ˜R,˜∪,˜∩)(K) = ΦM0
( ˜R,˜∪,˜∩)(K) + ΦM1
( ˜R,˜∪,˜∩)(K)
up to regular isotopy (equivalence without type I Reidemeister moves).
If in addition X
(i,j)∈Γ
∪jϕi =∪ 1,
X
(i,j)∈Γ
ϕj∩i =∩ 1
are satisfied, it provides a knot invariant up to isotopy.
Proof.The YBO ˆϕon ˜V⊗ ˜V, where ˜V=V⊗k[[ℏ]]//(ℏ 2), together with ˜∪and ˜∩satisfy the switch-
back, passcup, and passcap properties if they satisfy the corresponding conditions on infinitesimal
part (degree one part with respect topℏ), which are computed in Equations (10) through (15).
Then the composition corresponding to a given knot diagram with a height function defines a knot
invariant up to regular isotopy with these operators. For isotopy, the condition for type I move
translates to the stated condition on the degree one term ofℏ.□
Figure 10
For the rest of the section, we show that the cobounded cocycles give trivial infinitesimal part,
in parallel to Lemma 4.5 and Proposition 4.6.
Lemma 6.2.Letϕ=δ 1(f)be a cobounded YB 2-cocycle and ˜R=R+ ˆϕbe the deformed YBO on
˜V. Let ˜∪=∪+ℏ ¯∪and ˜∩=∩+ℏ ¯∩be a deformed pairing and copairing on ˜V, respectively, where
¯∪:=∪(f⊗1+1⊗f) and ¯∩:= (−f⊗1−1⊗f)∩
as represented by diagrams in Figure 10 left and right. Then( ˜R, ˜∪, ˜∩)satisfy the conditions in
Theorem 6.1.
QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY 21
Proof.The switchback property Equation (11) is checked directly as diagrammatically represented
in Figure 11. Equation (10) is similarly checked by their mirror diagrams.
A direct computation as in the proof of Lemma 4.5 shows that ˜R−1 =R −1 +ℏ ˆϕ, where ˆϕ=
δ1
R−1(f) is the image of the first YB coboundary of the inverse YBOR −1. A direct computation
for the terms of degree 1 inℏfor the passcap and passcup moves using ˜Rand ˜R−1 shows that the
equations hold. A part of a passcap move is depicted in Figure 12. In the figure, one of the terms
R(1⊗f) of the coboundary fromϕis depicted as a circle in the middle edge of the right-hand side,
and another term−(f⊗1)∩from ¯∩is depicted as another circle on the same edge, and seen to
cancel. The other terms involvingfare assigned on the end edges. The passcap equality ofRand
∩imply the corresponding equality for ˜Rand ˜∩.□
0
Figure 11
By Theorem 6.1, the deformed YBO and (co)pairings ( ˜R, ˜∪, ˜∩) of Lemma 6.2 defines a regular
isotopy invariant ΦM
( ˜R,˜∪,˜∩) = ΦM0
( ˜R,˜∪,˜∩) +ℏΦ M1
( ˜R,˜∪,˜∩).
Rφ (f    1)
R(1    f)
Figure 12
Proposition 6.3.The infinitesimal part of the invariantΦ M1
( ˜R,˜∪,˜∩) is trivial for a cobounded YB
2-cocycleϕ=δ 1(f). In other words, it holds thatΦ M
( ˜R,˜∪,˜∩) = ΦM0
( ˜R,˜∪,˜∩).
Proof.This is proved in a manner similar to Proposition 4.6. There are three types of arcs in a
given diagram in this case: (1) internal edge bounded by crossings, (2) edges with one end point
on a crossing, other on an extremum, and (3) both ends on extrema. For the internal edge (1),
cancelation happens as in Figure 7. Edges of case (2) happens where diagrams are as in passcup
or passcap moves, and cancelation happens as in Figure 12. Case (3) happens as in figures of
the switchback move, and cancelations happen as in Figure 11. Hence the same argument as in
Proposition 4.6 applies.□
7.Examples via maxima/minima
The Kauffman bracket polynomial [13] for knots up to regular isotopy is defined by the skein
relation in Figure 13. The bracket value for the unknot diagram with no crossing is set to be 1.
In this section we examine invariants defined from YB 2-cocycles and the bracket following the
definition in Section 6. In this section we assume thatkcontains √−1 and an invertible element
Athat serves as a variable in the Kauffman bracket.
Let∪and∩be pairing used in the bracket skein relation defined in [13] for basis elementse 1,
e2 ofV=k ⊗2 by∪(e i⊗ei) = 0 fori= 1,2 and
∪(e1⊗e 2) =
√
−1A,∪(e 2⊗e 1) =−
√
−1A−1.
