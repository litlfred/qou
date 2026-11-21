---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-027-a-appendix-proof-of-proposition-320
section_title: "A Appendix: Proof of Proposition 3.20"
section_number: null
pages: 44-44
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
Appendix: Proof of Proposition 3.20
Proposition 3.20. Consider the matrix
A =
1
3
4
3
0
13
9
10

.
For this matrix ˙κA = 5850 = 2 × 32 × 52 × 13 holds, and there exists no ˜A ∈Z2×4 such that
ker( ˜A) = ker(A) and the inverse of every nonsingular 2 × 2 submatrix of ˜A is 1/5850-integral.
Proof. We know all other representations of the space like ˜A such that ker( ˜A) = ker(A) are of
the form ˜A = BA where B is a 2 × 2 invertible matrix. Since A11 = 1 then to get an integral ˜A
we need to have integer B11 and B21. Furthermore since the g.c.d. of the numbers in the second
column is equal to 1, then B12 and B22 should be integers as well.
It can be veriﬁed by computer that the only 2×1 matrices like v such that all entries of vT A
are divisors of 5850 are
±
 9
−4

, ±
10
−3

, ±
13
−3

, ±
0
1

Checking all diﬀerent 2 × 2 matrices we can get these matrices:
 9
−4
10
−3
 1
3
4
3
0
13
9
10

=
 9
-25
0
−13
10
-9
13
0

13
−3
10
−3
 1
3
4
3
0
13
9
10

=
13
0
25
9
10
−9
13
0

 9
−4
13
−3
 1
3
4
3
0
13
9
10

=
 9
−25
0
-13
13
0
25
9

0
1
9
−4
 1
3
4
3
0
13
9
10

=
0
13
9
10
9
-25
0
-13

 0
1
10
−3
 1
3
4
3
0
13
9
10

=
 0
13
9
10
10
-9
13
0

 0
1
13
−3
 1
3
4
3
0
13
9
10

=
 0
13
9
10
13
0
25
9

All of these matrices contain a 2 × 2 submatrix such that its inverse is not
1
5850-integral.
