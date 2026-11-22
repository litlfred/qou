---
doc_id: topologicalinvariance3dindex
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-029-77-the-index-of-the-72-knot-complement
section_title: "The index of the 72 knot complement"
section_number: 7.7
pages: 49-51
source_pdf: topological.invariance.3Dindex.pdf
source_sha256: 22953b4eee66dca2
toc_source: outline
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
---
growth. The default SnapPy triangulation T of the 72 knot complement has 4 ideal tetrahedra,
and the Epstein-Penner decomposition has 8 ideal tetrahedra. The two triangulations are
related by geometric 23 moves and have equal indices. The angle structure equations of T
are given by:
50 STAVROS GAROUFALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
A =




1
2
1
0
0
0
1
0
1
0
0
1
0
0
0
1




B =




1
0
0
0
1
0
0
0
0
2
1
0
0
0
1
2




C =




0
0
1
0
0
1
0
2
1
1
1
0
1
0
0
0



.
Eliminating B, and removing the fourth row (which corresponds to the fourth edge equation),
we obtain the angle structure equations
A′α + B′γ = πν′
where
A′ =


0
2
1
0
−1
0
1
0
1
−2
−1
1


B′ =


−1
0
1
0
−1
1
0
2
1
−1
0
0


ν′ =


1
1
−1

.
The index of T is given by
I72(0)(q) =
X
(k1,k2,k3)∈Z3
(−1)k1+k2−k3q
1
2 (k1+k2−k3)I∆(−k1, k1 + k2 −k3)I∆(−2k2, k3)
I∆(k1 + k2 −k3, −k2 + k3)I∆(−k2 + k3, 2k1 −2k3) ∈Z[[q]] .
FT in R3 has 14 rays, spanned by the columns of the matrix


−2
−1
−1
0
0
0
0
0
0
1
1
1
1
2
−1
−1
0
−1
−1
−1
0
1
1
0
0
0
1
1
−2
−1
0
−2
−1
0
1
−1
0
0
1
2
1
3

.
If δ(k1, k2, k3) denotes the degree of the summand and N ∈N, then δ(k1, k2, k3) ≤N implies
that (k1, k2, k3) satisfy the bounds
1 −
√
1 + 2N ≤k1 ≤1
2(−1 +
√
1 + 8N)
1
2(1 −
√
1 + 4N) ≤k2 ≤N
1 −
√
1 + 2N ≤k3 ≤1
2(−1 +
√
1 + 12N) .
Observe that the upper bound for k3 is linear in N. The 
rst 50 coe
cients of I72(0) are
given by:
1 −4q + q2 + 16q3 + 20q4 + q5 −72q6 −156q7 −206q8 −98q9 + 275q10 + 924q11 + 1740q12 + 2370q13 + 2227q14 + 495q15 −
3485q16 −10168q17 −19045q18 −28467q19 −34899q20 −33157q21 −16460q22 + 22305q23 + 89035q24 + 185478q25 + 306146q26 +
434575q27+539981q28+575717q29+479148q30+176483q31−408854q32−1340316q33−2648389q34−4301970q35−6179555q36−
8036073q37 −9477453q38 −9942897q39 −8710346q40 −4925980q41 + 2323715q42 + 13897628q43 + 30430263q44 + 52111135q45 +
78414600q46 + 107796294q47 + 137380650q48 + 162674912q49 + 177363801q50
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD
