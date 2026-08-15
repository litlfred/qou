---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES STAVROS GAROUFALIDIS With an appendix by Sander Zwegers"
section_id: sec-008-43-the-rank-of-v-part-b-of-theorem-32
section_title: "The rank of V+: part (b) of Theorem 3.2"
section_number: 4.3
pages: 11-12
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES STAVROS GAROUFALIDIS With an appendix by Sander Zwegers — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of"
---
discrete integer variables e,m which satisﬁes Equations (3.1a) and 3.1b. Section 4.1 implies
that f(0,e ) satisﬁes the 3-term recursion
(4.1) f(0,e )− (2−qe−1)f(0,e− 1) +f(0,e− 2) = 0
for all integers e. It follows that for every integer e, f(0,e ) is a Z[q±1]-linear combination
of A and B where f(0, 0) = A and f(0, 1) = B. An induction on e <0 using the recursion
relation (4.1) shows that for all e< 0 we have
f(0,e ) =q−e2
2−e
2 (p1(e)A +p2(e)B)
wherep1(e),p 2(e)∈ Z[q] are polynomials of maximumq-degreee2/2+e/2 and constant term
(−1)e−1 and (−1)e respectively. For example, we have:
f(0,−1) = A−B
qf (0,−2) = A(−1 +q) +B(1− 2q)
q3f(0,−3) = A
(
1−q− 2q2 +q3)
+B
(
−1 + 2q + 2q2− 3q3)
q6f(0,−4) = A
(
−1 +q + 2q2 +q3− 2q4− 3q5 +q6)
+B
(
1− 2q− 2q2 +q3 + 4q4 + 3q5− 4q6)
q10f(0,−5) = A
(
1−q− 2q2−q3 + 5q5 + 3q6 +q7− 3q8− 4q9 +q10)
+B
(
−1 + 2q + 2q2−q3− 2q4− 7q5 + 3q7 + 6q8 + 4q9− 5q10)
Let us write
A =
∞∑
n=0
anqn B =
∞∑
n=0
bnqn.
If we assume thatf(0,e )∈ Z[[q]], this imposes a system of linear equations on the coeﬃcients
an and bn of A and B. In fact, for ﬁxed e< 0, the system of equations coeﬀ( f(0,e ),qj) = 0
forj =−e2/2−e/2,..., −2,−1 is a triangular system of linear equations with unknowns bj
forj = 0, 1,...,e 2/2−e/2− 1 where all diagonal entries of the coeﬃcient matrix are 1. For
example, we have:


1 0 0 0 0 0
−2 1 0 0 0 0
−2 −2 1 0 0 0
1 −2 −2 1 0 0
4 1 −2 −2 1 0
3 4 1 −2 −2 1




b0
b1
b2
b3
b4
b5


=


−a0
a0−a1
2a0 +a1−a2
a0 + 2a1 +a2−a3
−2a0 +a1 + 2a2 +a3−a4
−3a0− 2a1 +a2 + 2a3 +a4−a5


It follows that bn is a Z-linear combination of ak fork≤n. This proves that the rank of the
Z[[q]]-module V+ is at most 1. Since I∆∈V+ (as follows from the proof of Theorem 3.7), it
follows that the rank of the Z[[q]]-module V+ is exactly 1. This proves part (b) of Theorem
3.2. □
12 STA VROS GAROUF ALIDIS
Corollary 4.1. The above proof implies that f∈ V+ is uniquely determined by its initial
condition f(0, 0)∈ Z[[q]]. It follows that if f,g ∈V+, then
(4.2) g(0, 0)f(m,e ) =f(0, 0)g(m,e )
for all integers m and e.
