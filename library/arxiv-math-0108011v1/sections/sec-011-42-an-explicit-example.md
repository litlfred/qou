---
doc_id: arxiv-math-0108011v1
doc_title: "The Homfly polynomial of the decorated Hopf link"
section_id: sec-011-42-an-explicit-example
section_title: "An explicit example"
section_number: 4.2
pages: 21-24
source_pdf: 0108011v1.pdf
source_sha256: e4af4b5d3c5ff6cd
toc_source: inferred
doc_brief: "The Homfly polynomial of the decorated Hopf link — The main goal is to ﬁnd the Homﬂy polynomial of a link formed by decorating each component of the Hopf link with the closure of a directly oriented"
---
An explicit example
We illustrate our results by calculating the framed Homﬂy polynomial ⟨
,
⟩.
Let µ be a partition whose conjugate µ∨has r parts. The Jacobi-Trudy
formula gives the Schur function sµ of the series P eiti as the determinant
of the r × r matrix whose (i, j) entry is ek, with k = µ∨
i + j −i, taking
ek = 0 for k < 0. The diagonal entries in the matrix are thus the coeﬃcients
corresponding to the columns of µ, and each row of the matrix is completed
by taking consecutive coeﬃcients from the series. Then
s
= det
 
e2
e3
e1
e2
!
= e2
2 −e1e3
and it is enough to expand the series E
(t) as far as the term in t3 in order
to calculate s
(E
(t)).
For the diagram λ =
we have d(λ) = 1 with a1 = 2, b1 = 1 so that
E
(vs−1t) = 1 + q2t
1 + q−2tE∅(vs−1t).
Using (12) with λ = ci we can write
E∅(vs−1t)
=
1 + 1 −v2
q −1 t + (1 −v2)(1 −qv2)
(q −1)(q2 −1) t2
+
(1 −v2)(1 −qv2)(1 −q2v2)
(q −1)(q2 −1)(q3 −1)
t3 + O(t4).
We have
1 + q2t
1 + q−2t = 1 + (q2 −q−2)t −(1 −q−4)t2 + (q−2 −q−6)t3 + O(t4)
and so
E
(vs−1t)
=
1 +
 1 −v2
q −1 + q2 −q−2
!
t
+
 (1 −v2)(1 −qv2)
(q −1)(q2 −1) + (q2 −q−2)1 −v2
q −1 −(1 −q−4)
!
t2
+
 (1 −v2)(1 −qv2)(1 −q2v2)
(q −1)(q2 −1)(q3 −1)
+ (q2 −q−2)(1 −v2)(1 −qv2)
(q −1)(q2 −1)
−
(1 −q−4)1 −v2
q −1 + (q−2 −q−6)
!
t3 + O(t4)
=
1 + e1t + e2t2 + e3t3 + O(t4).
21
Now
s
(E
(t))
=
(vs−1)−4s
(E
(vs−1t))
=
(vs−1)−4(e2
2 −e1e3),
where e1, e2 and e3 are the coeﬃcients in the series above.
Combined with the expression
⟨
⟩= (v−1 −v)(v−1s −vs−1)(v−1s2 −vs−2)(v−1s−1 −vs)
(s −s−1)2(s2 −s−2)(s4 −s−4)
from (12) we get
⟨
,
⟩
=
(vs−1)−4(e2
2 −e1e3) ⟨
⟩
=
v−8(v2 −1)2(v2 −q)(v2 −q2)(v2q −1)
(q −1)3(q2 −1)3(q3 −1)(q4 −1) C
(19)
with
C
=
−q14 + q13 + q12 −q11 −q10 −q9 + 2q8 + q7 −q6 −2q4 + 2q2 −1
+(q13 −q10 −q9 + 2q8 + q7 + q6 −2q4 + q2 + q)v2
+(−q10 −q9 + q8 −q4 −q3)v4 + q6v6.
Remark.
Since ⟨λ, µ⟩= sµ(Eλ(t)) ⟨λ⟩= sλ(Eµ(t)) ⟨µ⟩the calculation in
our example could have been done with the roles of λ and µ interchanged. In
this case we would have had a more complicated expression for Eµ(t) since
d(µ) = 2, and in addition the expression for sλ would involve terms up to
degree 4 from the Jacobi-Trudy formula
s
= det



e2
e3
e4
1
e1
e2
0
1
e1


.
In general ⟨λ, µ⟩contains some form of least common multiple of ⟨λ⟩and
⟨µ⟩, and a ‘core’ part, such as the expression C in the example above.
To ﬁnd ⟨λ, µ⟩N we can make the substitution v = s−N. When either
⟨λ⟩N = 0 or ⟨µ⟩N = 0 this will vanish.
This happens when one of the
partitions has more than N parts. In our example this is the case when
N = 1, as we can see from the factor v2q −1 in (19).
We can equally calculate ⟨λ, µ⟩N from Vandermonde minors, using theo-
rem 4.2, and we compare the two results for our example in the case N = 3.
22
The substitution with N = 3 in equation (19) gives
⟨
,
⟩3 = (q2 +q +1)(q8 +q4 +q3 −q2 +1)(q2 +1)(q4 +q3 +q2 +q +1)/q3.
On the other hand taking I
= {0, 2, 5} and I
= {0, 3, 4}, gives the
minor
P 3
(
,
)
=
det



1
1
1
1
q6
q15
1
q8
q20


= q26 −q23 −q20 + q15 + q8 −q6
=
q6(q + 1)(q2 + 1)(q2 + q + 1)
(q4 + q3 + q2 + q + 1)(q8 + q4 + q3 −q2 + 1)(q −1)3,
and so
⟨
,
⟩3
=
q−8P 3
(
,
)/P 3
(∅,∅), by theorem 4.2,
=
q−8q26 −q23 −q20 + q15 + q8 −q6
(q −1)(q2 −1)(q2 −q)
=
(q2 + 1)(q2 + q + 1)
(q4 + q3 + q2 + q + 1)(q8 + q4 + q3 −q2 + 1)/q3,
as before.
4.3
The sl(N)q invariants of the Hopf link
Irreducible sl(N)q modules{Vλ} are indexed by Young diagrams with at
most N rows. The framed sl(N)q invariant (JH; Vλ, Vµ) for the Hopf link
H coloured by the irreducible modules Vλ and Vµ is given, up to a frac-
tional power of s, from our Homﬂy invariant ⟨λ, µ⟩by applying the sl(N)
specialisation v = s−N. The exact formula, noted in [6], is
(JH; Vλ, Vµ) = x2|λ||µ|⟨λ, µ⟩N, with x = s−1
N .
The correction factor arises from the isomorphism between the Hecke algebras
used here and the version based on the R-matrix in sl(N)q.
The sl(N)q invariants of the Hopf link are then essentially the Laurent
polynomials in q determined by N × N minors of the Vandermonde matrix
(qij).
In the simplest case N = 2 the most general minor is
det
 
qij
qi(j+b)
q(i+a)j
q(i+a)(j+b)
!
= q2ij+ib+aj(qab −1),
23
arising from partitions λ with parts (b+j−1, j) and µ with parts (a+i−1, i).
Then ⟨λ, µ⟩2 = qab −1
q −1 , up to a power of q. Calculation of this power and
the correction factor gives the formula
(JH; Vλ, Vµ) = [ab]
(20)
for the sl(2)q invariants of the Hopf link, where [k] is the quantum integer
[k] = sk −s−k
s −s−1 .
The sl(2)q modules Vλ and Vµ in this case do not depend on i or j, and
have dimension a and b respectively.
They correspond to the single row
diagrams da−1 and db−1. The formula (20) for the sl(2)q Hopf link invariants
was given in [11] and [4]. It allows a simple development of the properties
for the related 3-manifold invariants where q is replaced by a root of unity,
[12, 4].
For N ≥3 the sl(N)q invariants of the Hopf link do not have such an
immediately memorable form. Their expression by Vandermonde minors was
given by Kohno and Takata, [5], only in the case where q is a root of unity.
Our determination of them here for generic q in theorem 4.2 and the eventual
2-variable formulation for ⟨λ, µ⟩given in theorem 4.5 was initially inspired
by our reading of [5].
Version 1.6, July 2001.
