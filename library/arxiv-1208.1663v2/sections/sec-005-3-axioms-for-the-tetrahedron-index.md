---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES STAVROS GAROUFALIDIS With an appendix by Sander Zwegers"
section_id: sec-005-3-axioms-for-the-tetrahedron-index
section_title: "Axioms for the tetrahedron index"
section_number: 3
pages: 8-10
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES STAVROS GAROUFALIDIS With an appendix by Sander Zwegers — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of"
---
In this section we discuss an axiomatic approach to the tetrahedron index. Let Z((q1/2))
(resp., Z[[q1/2]]) denote the ring of series of the form
f(q) =
∑
n∈ 1
2 Z
anqn
where there exists n0 = n0(f) such that an = 0 for all n < n0 (resp., n < 0). For
f(q)∈ Z((q1/2)), its degreeδ(f(q)) is the largest half-integer (or inﬁnity) such that f(q)∈
qd(f)Z[[q1/2]]. We will say that f(q)∈ Z((q1/2)) is q-positive if δ(f(q))≥ 0.
Deﬁnition 3.1. A tetrahedron index is a function f : Z2−→ Z((q1/2)) that satisﬁes the
equations
(3.1a) q
e
2f(m + 1,e ) +q−m
2f(m,e + 1)−f(m,e ) = 0
(3.1b) q
e
2f(m− 1,e ) +q−m
2f(m,e− 1)−f(m,e ) = 0
for all integers m,e , together with the parity condition f(m,e )∈ q
em
2 Z((q)) for all m and
e. Let V denote the set of all tetrahedron indices, and V+ denote the set of all q-positive
tetrahedron indices.
Theorem 3.2. (a) V is a free q-holonomic Z((q))-module of rank 2.
(b) V+ is a free q-holonomic Z[[q]]-module of rank 1.
(c) If f∈V , then it satisﬁes the equation
(3.2) f(m,e )(q) = (−q
1
2 )−ef(e,−e−m)(q) = (−q
1
2 )mf(−e−m,m )(q)
THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES 9
for all integers m and e.
(d) If f∈V , then it satisﬁes the equations
(3.3a) f(m,e + 1) + (qe+m
2−q−m
2−q
m
2 )f(m,e ) +f(m,e− 1) = 0
(3.3b) f(m + 1,e ) + (q−e
2−m−q−e
2−q
e
2 )f(m,e ) +f(m− 1,e ) = 0
for all integers m,e .
Question 3.3. What is a basis for V ?
Remark 3.4. The proof of part (a) of Theorem 3.2 implies that if f(m,e ) is a tetra-
hedron index, then f(m,e ) is a a unique Z[q±1/2] linear combination of A and B where
(f(0, 0),f (0, 1)) = (A,B ). For example, if C = (f(m,e ))−2≤m,e≤2, then C = MAA +MBB
where
MA =


1− 1
q3 + 1
q2 + 1
q−q2 1
q−q −1 − 1
q − 1
q2 + 1
q
1− 1
q2 + 1
q
1√q 0 − 1√q − 1
q
1− 1
q 1 1 0 −1
−1 0 1 1√q
1
q−q
−q −1 1 − 1
q 1− 1
q2 + 1
q 1− 1
q3 + 1
q2 + 1
q−q2


MB =


1
q3− 2
q2− 1
q +q + 2q2−q3 1− 1
q + 2q−q2 2−q −1 + 1
q
1
q2− 2
q
−1 + 1
q2− 2
q +q − 1√q +√q 1 1√q −1 + 1
q
−2 + 1
q −1 0 1 2 −q
1−q −√q −1 − 1√q +√q 1− 1
q + 2q−q2
2q−q2 1−q −2 + 1
q −1 + 1
q2− 2
q +q 1
q3− 2
q2− 1
q +q + 2q2−q3


Remark 3.5. The proof of part (b) of Theorem 3.2 implies that if f(m,e ) is a tetrahedron
index, thenf(m,e ) is uniquely determined byf(0, 0) =∑∞
n=0anqn. In particular, if f(0, 1) =∑∞
n=0bnqn, then bn are Z-linear combinations of ak for k≤n. For example, we have:
b0 = a0
b1 = a0 +a1
b2 = 2 a0 +a1 +a2
b3 = 4 a0 + 2a1 +a2 +a3
b4 = 9 a0 + 4a1 + 2a2 +a3 +a4
b5 = 20 a0 + 9a1 + 4a2 + 2a3 +a4 +a5
b6 = 46 a0 + 20a1 + 9a2 + 4a3 + 2a4 +a5 +a6
b7 = 105 a0 + 46a1 + 20a2 + 9a3 + 4a4 + 2a5 +a6 +a7
b8 = 242 a0 + 105a1 + 46a2 + 20a3 + 9a4 + 4a5 + 2a6 +a7 +a8
b9 = 557 a0 + 242a1 + 105a2 + 46a3 + 20a4 + 9a5 + 4a6 + 2a7 +a8 +a9
b10 = 1285 a0 + 557a1 + 242a2 + 105a3 + 46a4 + 20a5 + 9a6 + 4a7 + 2a8 +a9 +a10
b11 = 2964 a0 + 1285a1 + 557a2 + 242a3 + 105a4 + 46a5 + 20a6 + 9a7 + 4a8 + 2a9 +a10 +a11
b12 = 6842 a0 + 2964a1 + 1285a2 + 557a3 + 242a4 + 105a5 + 46a6 + 20a7 + 9a8 + 4a9 + 2a10
+a11 +a12
In fact, it appears that bn is a N-linear combination of ak for k≤ n, although we do not
know how to show this, nor do we know of a geometric signiﬁcance of this experimental fact.
10 STA VROS GAROUF ALIDIS
The next lemma computes the degree of the tetrahedron index.
Lemma 3.6. The degree δ(m,e ) of I∆(m,e )(q) is given by:
(3.4) δ(m,e ) = 1
2 (m+(m +e)+ + (−m)+e+ + (−e)+(−e−m)+ + max{0,m,−e})
It follows that δ(m,e ) is a piece-wise quadratic polynomial given by Figure 4.
Figure 4. The degree of the tetrahedron index.
The next theorem gives an axiomatic characterization of the tetrahedron index I∆.
Theorem 3.7. I∆ is uniquely characterized by the following equations:
(a) I∆∈V+, I∆(0, 0)(0)⁄= 0
(b) I∆ satisﬁes the pentagon identity
(3.5) I∆(m1−e2,e 1)I∆(m2−e1,e 2) =
∑
e3∈Z
qe3I∆(m1,e 1 +e3)I∆(m2,e 2 +e3)I∆(m1 +m2,e 3),
for all integers m1,m 2,e 1,e 2.
Remark 3.8. The uniqueness part of Theorem 3.7 uses only the facts that I∆ ∈ V ,
δ(I∆(0,e ))≥ 0 for all e and I∆ satisﬁes the special pentagon
I∆(0, 0)2 =
∑
e∈Z
I∆(0,e )3qe.
