---
doc_id: arxiv-2305.14884v2
doc_title: "PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS"
section_id: sec-009-6-invariance-under-pachner-moves
section_title: "Invariance under Pachner moves"
section_number: 6
pages: 23-25
source_pdf: 2305.14884v2.pdf
source_sha256: ebc8e64d901c9e4f
doc_brief: "PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS — We prove that a formal power series associated to an ideally triangu lated cusped hyperbolic 3-manifold (together with some further"
---
In this section, we will prove that Φ Ξ is invariant under 2–3 Pachner moves. There are
several versions of the 2–3 move (and of the corresponding pent agon identity in Teichm¨ uller
TQFT [
27]) and the one we choose in the next theorem is slightly diﬀerent from t he one
in [ 11, Sec.3.6] and can be related by composing with quad moves.
The 2–3 move involves two triangulations T and ~T with N + 2 and N + 3 tetrahedra,
respectively, shown in Figure 2.
z1 z′
1
z′′
1
z2
z′
2z′′
2
~z0
~z′
0
~z′′
0
~z1
~z′
1
~z′′
1~z2
~z′′
2
~z′
2
Figure 2. The 2–3 Pachner move.
Usingz0 =z1 +z2 −z1z2 from Equation ( 46) used in Theorem 3.6, it follows that the shapes
z of T and~z of ~T are related by
z = ( z1,z 2,z ∗) ↦→~z =
(
~z0, ~z1, ~z2, ~z∗)
=
(
z0, z1z−1
0 , z2z−1
0 , z∗)
. (93)
24 STA VROS GAROUF ALIDIS, MATTHIAS STORZER, AND CAMPBELL WH EELER
Similarly to [ 11, Eq. (3.20) and (3.21)], these shapes satisfy the relations
~z′
0 = z′
1z′
2, ~z′′
1 = z′′
1z2, ~z′′
2 = z1z′′
2,
z1 = ~z0~z1, z ′
1 = ~z′
1~z2, z ′′
1 = ~z′′
0~z′
2,
z2 = ~z0~z2, z ′
2 = ~z1~z′
2, z ′′
2 = ~z′′
0~z′
1.
(94)
If we write the Neumann–Zagier matrices of T in the form
A = ( a1 |a2 |a∗), B = ( b1 |b2 |b∗), (95)
where a1, a2 are the ﬁrst two columns of A and a∗ is the block ( N + 2) ×N matrix of the
remainingN columns of A, and likewise for B, then using Equations ( 94) the corresponding
Neumann–Zagier matrices of ~T are given by
~A =
(
−1 0 0 0
−b1 −b2 +a1 +a2 a1 −b2 a2 −b1 a∗
)
, ~B =
(
−1 1 1 0
0 b1 b2 b∗
)
(96)
and the corresponding vector ~ν = (1,ν ). Analogously to the shapes, we will ﬁx ﬂattenings
(~f0,~f1,~f2,~f ∗) and ( ~f ′′
0,~f ′′
1,~f ′′
2,~f ′′∗) for ( ~A |~B) and ( f1,f 2,f ∗) = ( ~f0 + ~f1,~f0 + ~f2,f ∗) and
(f ′′
1,f ′′
2,f ′′∗) = (~f ′′
0 +~f ′
2,~f ′′
0 +~f ′
1,f ′′∗) for (A |B). The data of the ﬂattenings then satisfy the
additive versions of Equations ( 94).
Theorem 6.1. The series Φ Ξ (ℏ) is invariant under 2–3 Pachner moves.
The proof involves an application of the pentagon identity for ψℏ of Theorem 3.6.
For two triangulations T and ~T withN + 2 andN + 3 tetrahedra and NZ matrices ( A | B),
respectively, related by a Pachner 2–3 move. To deﬁne the corres ponding series Φ Ξ (ℏ) and
Φ ~Ξ (ℏ), we need to possibly change quads on T and ~T so that both B and ~B are invertible.
By a quad move q, we can replace ( A | B) by ( A | B) where det( B) ⁄= 0. Recalling that quad
moves act on tetrahedra and actions on diﬀerent tetrahedra com mute, we can write the move
q =q2 ×qN as a product of quad moves q2 on the ﬁrst 2 tetrahedra times moves qN on the
remaining N tetrahedra of T . Let ( A |B) denote the result of applying the move 1 ×qN on
the N + 2 tetrahedra of T .
Since the (N + 2) × (N + 2) matrix B has full rank and B and B have the same last N
columns, it follows that B has nullity 0, 1 or 2.
Now on ~T , we can apply the identity move on the ﬁrst three tetrahedra and t heqN moves
on the remaining N tetrahedra, which transforms the NZ matrices ( ~A |~B) to ( ~A |~B), and
further apply the q2 moves on the second and third tetrahedra to obtain the NZ matrice s
(~A |~B). By looking at how the matrix B transforms under a 2–3 move (see Equation ( 96)),
it follows that ~B has the same rank as B, and hence det( ~B) ⁄= 0.
The above discussion can be summarized in the following commutative d iagram.
PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS 25
(A | B ) ( ~A | ~B)
(A |B) ( ~A | ~B)
(A | B) ( ~A |~B)
2→3
1×qN
q2×qN
1×1×qN
1×q2×qN2→3
q2×1
1×q2×1
(97)
where det( B) ⁄= 0 and det( ~B) ⁄= 0. Now Φ Ξ (ℏ) and Φ ~Ξ (ℏ) can be deﬁned using the non-
degenerate NZ data with matrices ( A | B) and ( ~A |~B), respectively. We will show that the
two ℏ-series are equal using a diagram
Φ Ξ (ℏ) • • • Φ ~Ξ (ℏ)
⊗iFourier Pentagon ⊗iFourier−1 2i−Fubini
(98)
where i = 0, 1, 2 denotes the nullity of B. We will treat each case in a separate section.
With this discussion the Theorem 6.1 follows from Propositions 6.2, 6.4, and 6.6. Before
proceeding with the proof, we will set some notation. Similarly to the p roof of the quad
invariance, denote Q = B−1A
Q =



Q11 Q12 Q∗
1
Q12 Q22 Q∗
2
Q∗
1
t Q∗
2
t Q∗


, (99)
where Qij are matrices of size 1 × 1, Q∗
j are matrices of size 1 ×N and Q∗ is a matrix of
size N ×N.
