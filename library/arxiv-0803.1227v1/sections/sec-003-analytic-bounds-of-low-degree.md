---
doc_id: arxiv-0803.1227v1
doc_title: "Linear programming bounds for unitary space time codes"
section_id: sec-003-analytic-bounds-of-low-degree
section_title: "Analytic bounds of low degree"
section_number: null
pages: 5-7
source_pdf: 0803.1227v1.pdf
source_sha256: cf72e0fcdc7f3ddf
doc_brief: "Linear programming bounds for unitary space time codes — The linear programming method is applied to the space Un(C) of uni- tary matrices in order to obtain bounds for codes relative to the"
---
From the explicit description of the zonal functions (4), we have de duced con-
venient polynomials of low degree which verify the positivity property . Using
formula (2) we derive the analytic bounds of Theorems 4.1 and 4.2.
Theorem 4.1 Let V be a unitary space time code with diversity sum Σ V, the
following upper bounds hold :
|V| ≤ 2(Σ V)2
2(Σ V)2 − 1 , if (Σ V)2 > 1
2 (5)
|V| ≤ 8n2(Σ V)2
4n2(Σ V)2 − (2n2 − 1) , if (Σ V)2 > 2n2 − 1
4n2 (6)
5
|V| ≤ 16n2(Σ V)2
2n(2n − 1)(Σ V)2 − (2n2 − n − 2) , (7)
if (Σ V)2 ≥ 2n2 − n − 2
2n(2n − 1)
Theorem 4.2 Let V be a unitary space time code with diversity product Π V,
the following upper bounds hold :
|V| ≤ 2(Π V)2
2(Π V)2 − 1 , if (Π V)2 > 1
2 (8)
|V| ≤ 8n(Π V)2
4n(Π V)2 − (2n − 1) , if (Π V)2 > 2n − 1
4n , n ≥ 3 (9)
|V| ≤ 8(Π V)6 + 4(Π V)4 + 8(Π V)2
8(Π V)6 − 1
4
, (10)
if (Π V)2 ≥ 1
2 , n = 2.
The proofs of these theorems are based on Theorem 2.1 and on the following
lemma :
Lemma 4.3 Let yj = cos θj and m[a1,...,a r](y) the elementary symmetric poly-
nomials in the yj = cos θj. The following polynomials are linear combination of
the zonal functions (4) with non negative coeﬃcients:
Q[0] = 1
Q[11] = m[11](y) + (n−1)
4
Q[1] = m[1](y)
Q[2] = m[2](y) + m[11](y) − (n+1)
4
Q[1, 1, 1] = m[1, 1, 1](y) + (n−2)
4 m[1](y)
Q[2, 1] = m[2, 1](y) + 2m[1, 1, 1](y) − 1
4 m[1](y)
Q[3] = m[3](y) + m[2, 1](y) + m[1, 1, 1](y) − (n+2)
4 m[1](y)
Proof : [Theorem 4.1, Sketch] Let s = 1
n
∑ n
j=1 cos θj so that s = 1 − 2d2
Σ . We
apply formula (2) with the polynomials : P = Q[1]−ns, P = (Q[1]−ns)(Q[1]+n),
P = (Q[1] − ns)R, where R is the symmetrization of ( y1 + 1)(y2 + 1).
6
Proof : [Theorem 4.2, Sketch] Let p = 2 d2
π . We apply formula (2) with the
polynomials : P = Q[1] − n(p − 1), P = Q[2] + (n+1)p
2 Q[1] + (n+1)(2n(p−1)+1)
4
(if n ≥ 3),
P = Q[2] + ( p2
2 + 2p − 1)Q[1] + (p3 − 1
4 ) (if n = 2).
