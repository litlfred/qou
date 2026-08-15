---
doc_id: arxiv-2205.01282v2
doc_title: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES YUYA MURAKAMI"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 2205.01282v2.pdf
source_sha256: 00f656afa60db838
doc_brief: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES YUYA MURAKAMI — In this paper, we prove a conjecture by Gukov–Pei–Putrov–Vafa for a wide class of plumbed"
---
Acknowledgement 3
2. Basic notations for plumbing graphs 3
2.1. Notations for graphs 3
2.2. The inverse matrix of the linking matrix 4
2.3. Periodic maps determined by the linking matrix 5
2.4. Rational functions determined by the linking matrix 6
3. Calculations of WRT invariants 8
4. Expressions of homological blocks as false theta functions 9
5. An asymtotic formula 11
5.1. Asymtotic formulas obtained from Euler–Maclaurin summation formula 11
5.2. Asymtotic expansion of infinite series with weighted Gauss sums 13
6. A proof of the main theorem 15
6.1. The main result 15
6.2. A proof of the main result 16
References 17
1. Introduction
In this paper, we study Witten–Reshetikhin–Turaev (WRT) invariants. They are quantum invari-
ants of 3-manifolds constructed by Witten [Wit89] from a physical viewpoint and constructed by
Reshetikhin–Turaev [RT91, Theorem 3.3.2] from a mathematical viewpoint. The Witten’s asymptotic
expansion conjecture plays a central role in studying WRT invariants. It claims that the Chern-Simons
invariants and the Reidemeister torsions appear in the asymptotic expansion of WRT invariants. This
conjecture is proved by Lawrence–Zagier [LZ99] for the Poincar´ e homology sphere, Hikami [Hik05a]
for Brieskorn homology spheres, Hikami [Hik06a] and Matsusaka–Terashima [MT21] independently
for Seifert homology spheres. Many other authors have studied this conjecture [AH12, AM22, And13,
BW05, Cha16, Chu17, CM15, FIMT21, FG91, GMnP16, Hik05b, Hik06b, HT04, Jef92, Roz94, Roz96,
Wu21].
Recently, Gukov–Pei–Putrov–Vafa [GPPV20] introducedq-series invariants called homological blocks
or GPPV invariants for plumbed manifolds. They conjectured that homological blocks have good mod-
ular transformations and their radial limits yield WRT invariants. These conjectures show a roadmap
Date: April 5, 2024.
1
arXiv:2205.01282v2  [math.GT]  4 Apr 2024
2 Y. MURAKAMI
w1 w2
w3
w4
wN′
wN′+1
wN′+2
wN
···
....
Figure 1
to prove the Witten’s asymptotic expansion conjecture. The first conjecture, modular transforma-
tions of homological blocks, are related to quantum modular forms introduced by Zagier [Zag10]. This
conjecture is proved by Matsusaka–Terashima [MT21] for Seifert homology spheres and Bringmann–
Mahlburg–Milas [BMM20] for non-Seifert homology spheres whose surgery diagrams are the H-graphs.
Bringmann–Nazaroglu [BN19] and Bringmann–Kaszian–Milas–Nazaroglu [BKMN21] clarified and proved
the modular transformation formulas of false theta functions, which are main tools to study modular
transformations of homological blocks.
The second conjecture, which asks the relation between WRT invariants and radial limits of ho-
mological blocks, is proved by Fuji–Iwaki–Murakami–Terashima [FIMT21] with a result in Andersen–
Misteg˚ ard [AM22] for Seifert homology spheres and Mori–Murakami [MM22] for non-Seifert homology
spheres whose surgery diagrams are the H-graphs. In this paper, we prove this conjecture for a large
class of plumbed manifolds by developing some new techniques.
Let us explain our setting. Let Γ = ( V,E, (wv)v∈V ) be a plumbing graph, that is, a finite tree
with the vertex set V , the edge set E, and integral weights wv∈ Z for each vertex v∈V . Following
[GPPV20], we assume that the linking matrix W of Γ is negative definite. Then one can define the
homological block bZΓ(q) with q∈ C and|q|< 1. Let M(Γ) be the plumed 3-manifold obtained from
S3 through the surgery along the diagram defined by Γ. We also assume that M(Γ) is an integral
homology sphere. This condition is equivalent to det W =±1 since H1(M(Γ), Z)∼= ZV/W (ZV ) by
use of the Mayer–Vietoris sequence. For a positive integer k, let WRTk(M(Γ)) be the WRT invariant
of M(Γ) normalised as WRTk(S3) = 1. We also denote ζk :=e2π√−1/k.
In the above setting, we can state the conjecture of Gukov–Pei–Putrov–Vafa [GPPV20] by the
following.
Conjecture 1.1 ([GPPV20, Conjecture 2.1, Equation (A.28)]) .
WRTk(M(Γ)) = 1
2(ζ2k−ζ−1
2k ) lim
q→ζk
bZΓ (q).
In this paper, we prove this conjecture for a wide class of plumbing graphs.
Theorem 1.2. Conjecture 1.1 is true for plumbing graphs depicted in Figure 1.
Here we remark that a plumbing graph has the form depicted in Figure 1 if and only if |v| + 2−
deg(v)> 0 for any vertexv∈V , where deg(v) is the degree ofv andv :={i∈V |{i,v}∈ E, deg(i) =
1}.
In a proof of Theorem 1.2, the most difficult point is to prove the vanishing of weighted Gauss sums
that appear in coefficients of negative degree in asymptotic expansions of homological blocks. The
previous works [BMM20, MM22] deal with this difficulty by direct calculations ([BMM20, Theorem
4.1],[MM22, Proposition 4.2]). However, we prove it indirectly by using our asymptotic formula
(Proposition 5.4 and Corollary 5.7) and holomorphy of a rational function whose radial limits are
WRT invariants. In a sense, our technique is a generalisation of the method of Lawrence–Zagier [LZ99,
pp.98, Proposition] using L-funcitons for periodic maps.
This paper will be organised as follows. In Section 2, we prepare some notations for plumbing
graphs Γ which we use throughout this paper. In Section 3, we calculate WRT invariants for plumbed
homology spheresM(Γ). The point of our calculation is to represent WRT invariants as a sum for the
submatrix ofW−1 with vertices whose degrees are greater than 2. In Section 4, we express homological
blocks as false theta functions. Then we can study the asymptotic expansions of homological blocks
as q→ ζk. To calculate asymptotic expansions, we develop a formula in Section 5.1 by the Euler–
Maclaurin summation formula based on Zagier [Zag06, Equation (44)]. In Section 5.2, we develop the
important asymptotic formula, which plays a central role in proving our main theorem. This formula
WRT INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES 3
asserts that the same factors appear in the asymptotic expansions of homological blocks and rational
functions whose radial limits are WRT invariants. Finally, we prove our main theorem in Section 6.
