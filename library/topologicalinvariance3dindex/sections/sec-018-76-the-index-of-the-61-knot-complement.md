---
doc_id: topologicalinvariance3dindex
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-018-76-the-index-of-the-61-knot-complement
section_title: "The index of the 61 knot complement"
section_number: 7.6
pages: 48-49
source_pdf: topological.invariance.3Dindex.pdf
source_sha256: 22953b4eee66dca2
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
---
as an example of the phenomenon of linear growth. The default SnapPy triangulation T of
the 61 knot complement has 4 ideal tetrahedra, and the Epstein-Penner decomposition uses
6 ideal tetrahedra. The two triangulations are related by geometric 23 moves and so have
equal indices. The angle structure equations of T are given by:
A =


1 1 0 0
0 0 0 1
0 1 1 0
1 0 1 1

 B =


0 2 0 1
1 0 1 0
1 0 0 0
0 0 1 1

 C =


1 0 1 1
1 2 1 0
0 0 0 1
0 0 0 0

 .
Eliminating B, and removing the fourth row (which corresponds to the fourth edge equa-
tion), we obtain the angle structure equations
A′α + B′γ =πν′
where
A′ =


1 −1 0 −1
−1 0 −1 1
−1 1 1 0

 B′ =


1 −2 1 0
0 2 0 0
−1 0 0 1

 ν′ =


−1
0
1

 .
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 49
The index of T is given by
I61(0)(q) =
∑
(k1,k2,k3)∈Z3
q
1
2 (−k1+k3)I∆(−k1,−k2 +k3)I∆(2k1− 2k2,−k1 +k3)
I∆(−k3,−k1 +k2)I∆(−k1 +k3,k 1−k2−k3)∈ Z[[q]].
FT in R3 has 18 rays, corresponding to the columns of the matrix


−1 −1 −1 −1 −1 −1 0 0 0 0 0 0 1 1 1 1 2 3
−2 −2 −1 0 0 1 −1 −1 −1 0 1 1 0 0 1 1 1 2
−3 −1 0 −1 0 0 −2 −1 0 1 −1 0 −1 1 0 1 1 1

 .
If δ(k1,k 2,k 3) denotes the degree of the summand and N∈ N, then δ(k1,k 2,k 3)≤N implies
that (k1,k 2,k 3) satisfy the bounds
1
2(1−
√
1 + 4N)≤k1≤ 1
2(−1 +
√
1 + 12N)
2
3(1−
√
1 + 3N)≤k2≤ 1
2(−1 +
√
1 + 8N)
3
7(1−
√
1 + 7N)≤k3≤N.
Observe that the upper bound for k3 is linear in N . For instance, when N = 3, the following
17 terms (each a product of 4 truncated tetrahedron indices, as in Equation (32) for N = 3)
contribute to I61(0) +O(q)4 = 1− 4q +q2 + 18q3 +O(q)4:
I∆(−2, 0)2I∆(0,−2)I∆(0, 0)−q− 1
2I∆(−1,−1)I∆(−1, 0)I∆(0,−1)I∆(0, 0) +I∆(−1, 0)2I∆(0,−1)I∆(0, 0) +I∆(0, 0)4
+I∆(−2, 0)I∆(0,−1)2I∆(0, 1)−q
1
2I∆(−2, 0)I∆(−1, 1)I∆(0, 1)I∆(1,−2)−q
1
2I∆(−1, 0)I∆(0, 1)2I∆(1,−1)
−q− 1
2I∆(−1, 1)I∆(0,−1)2I∆(1, 0)−q
1
2I∆(−2, 1)I∆(0, 1)I∆(1,−1)I∆(1, 0) +I∆(0, 0)I∆(0, 1)I∆(1, 0)2
+I∆(−2, 0)I∆(0, 0)I∆(1,−1)I∆(1, 1)−q
1
2I∆(0, 0)I∆(0, 1)I∆(1, 0)I∆(1, 1) +qI∆(−2, 0)I∆(0, 2)2I∆(2,−2)
−q− 1
2I∆(−2, 0)I∆(−1,−1)I∆(−1, 0)I∆(2,−1)−q− 1
2I∆(−1, 0)I∆(−1, 1)I∆(0,−1)I∆(2,−1)
−q− 1
2I∆(−1, 2)I∆(0, 0)I∆(1,−1)I∆(2,−1))−q
3
2I∆(−3, 0)I∆(0, 3)2I∆(3,−3)
The 
rst 50 coe
cients of I61(0) are given by:
1− 4q +q2 + 18q3 + 22q4 +q5− 78q6− 178q7− 254q8− 188q9 + 167q10 + 855q11 + 1864q12 + 2892q13 + 3426q14 + 2583q15−
488q16− 6698q17− 16273q18− 28550q19− 41189q20− 49943q21− 48554q22− 28899q23 + 17621q24 + 98726q25 + 217819q26 +
371551q27 + 544496q28 + 707360q29 + 811832q30 + 792301q31 + 565550q32 + 40436q33− 872995q34− 2241496q35− 4087180q36−
6354321q37−8877834q38−11348143q39−13283739q40−14014789q41−12685231q42−8288627q43 +266720q44 +14032731q45 +
33862808q46 + 60173861q47 + 92687285q48 + 130092845q49 + 169735693q50
