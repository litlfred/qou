---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-006-16-feynman-diagrams
section_title: "Feynman diagrams"
section_number: 1.6
pages: 8-8
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
diagrams, using Wick’s theorem to express each term ST ,n as a ﬁnite sum of connected
diagrams with at most n loops, where the number of loops of a connected graph is its
ﬁrst betti number. This is well known and explained in detail, e.g. in [HKK+03, Ch.9],
[BIZ80, Pol05].
The Feynman rules for computing the ST ,n, described in Section 5, turn out to be the
following.1 One draws all connected graphs D with vertices of all valencies, such that
(1.15)
L(D) := (# 1-vertices + # 2-vertices + # loops) ≤n .
In each diagram, the edges represent an N × N propagator
(1.16)
propagator :
Π = ℏH−1 ,
while each k-vertex comes with an N-vector of factors Γ(k)
i ,
(1.17)
Γ(k)
i
= (−1)k
αk+n−L(D)
X
p = αk
ℏp−1Bp
p!
Li2−p−k(z−1
i ) +
(
−1
2(B−1ν)i
k = 1
0
k ≥2 ,
where αk = 1 (resp., 0) if k = 1, 2 (resp., k ≥3). The diagram D is then evaluated by
contracting the vertex factors Γ(k)
i
with propagators, multiplying by a standard symmetry
factor, and taking the ℏn−1 part of the answer. In the end, SM,n is the sum of evaluated
diagrams, plus an additional vacuum contribution
(1.18)
Γ(0) = Bn
n!
N
X
i=1
Li2−n(z−1
i ) +
(
1
8f · B−1Af
n = 2
0
n ≥3 .
To illustrate the above algorithm, we give the explicit formulas for S2 and S3 below.
