---
doc_id: ds15v1-2008
doc_title: "Rogers-Ramanujan-Slater Type Identities"
section_id: sec-036-61-series-equivalent-identities
section_title: "Series-Equivalent Identities"
section_number: 6.1
pages: 40-44
source_pdf: ds15v1-2008.pdf
source_sha256: aef155a324c6fdf4
toc_source: inferred
---
Suppose we have an identity of the form
Inﬁnite Series1 = Inﬁnite Product × Inﬁnite Series2,
(6.1.1)
where each side contains one or more free parameters. It is immediately clear that if,
for particular values of the parameters, either series has a representation as an inﬁnite
product, then so does the other. We say two identities of Rogers-Ramanujan type are
series-equivalent, if one can be derived from the other by specializing the free parameters
in an identity of the type at (6.1.1).
We next list some general series transformations. Most can be derived as limiting
cases of transformations between basic hypergeometric series. Let a, b, c, d, γ and q ∈C,
|q| < 1. Then
∞
X
n=0
(a, b; q)nqn(n−1)/2 (−cγ/ab)n
(c, γ, q; q)n
= (cγ/ab; q)∞
(γ; q)∞
∞
X
n=0
(c/a, c/b; q)nqn(n−1)/2(−γ)n
(c, cγ/ab, q; q)n
.
(6.1.2)
∞
X
n=0
(a; q)nqn(n−1)/2γn
(b; q)n(q; q)n
= (−γ; q)∞
(b; q)∞
∞
X
n=0
(−aγ/b; q)nqn(n−1)/2(−b)n
(−γ; q)n(q; q)n
.
(6.1.3)
∞
X
n=0
(a; q)nqn(n−1)/2γn
(q; q)n
= (−γ; q)∞
∞
X
n=0
(−aγ)nqn(n−1)
(−γ; q)n(q; q)n
.
(6.1.4)
∞
X
n=0
(a; q)nqn(n−1)/2γn
(−aγ; q)n(q; q)n
= (−γ; q)∞
(−aγ; q)∞
.
(6.1.5)
∞
X
n=0
q3n(n−1)/2γn
(γ; q2)n(q; q)n
=
1
(γ; q2)∞
∞
X
n=0
q2n2−nγn
(q2; q2)n
.
(6.1.6)
the electronic journal of combinatorics 15 (2008), #DS15
40
∞
X
n=0
qn2−n(−γ)n
(γq; q2)n(q2; q2)n
=
1
(γq; q2)∞
∞
X
n=0
qn2−n(−γ)n
(q; q)n
.
(6.1.7)
∞
X
n=0
qn2−n(−γ)n
(γ/q; q2)n(q2; q2)n
=
1
(γ/q; q2)∞
∞
X
n=0
qn2−2n(−γ)n
(q; q)n
.
(6.1.8)
∞
X
n=0
qn(n−1)/2γn
(γ; q)n(q; q)n
=
1
(γ; q)∞
∞
X
n=0
q2n2−nγ2n
(q2; q2)n
.
(6.1.9)
∞
X
n=0
(b; q2)nqn(n−1)/2(−γ)n
(b; q)n(q; q)n
= (γ; q)∞
∞
X
n=0
q4n2−2n(bγ2)n
(q2; q2)n(bq; q2)n(γ; q)2n
.
(6.1.10)
∞
X
n=0
qn(n−1)/2(−γ)n
(b; q)n(q; q)n
= (γ; q)∞
∞
X
n=0
q(3n2−3n)/2(−bγ)n
(q; q)n(b; q)n(γ; q)n
.
(6.1.11)
∞
X
n=0
qn2γn
(q/b; q)n(q; q)n
= (−γq2; q2)∞
∞
X
n=0
qn2γn(−q/b; q)2n
(q2; q2)n(q2/b2; q2)n(−γq2; q2)n
.
(6.1.12)
∞
X
n=0
(a; q)nqn2+n(bγ/a)n
(−bq; q)n(−γq; q)n(q; q)n
=
1
(−γq; q)∞
∞
X
n=0
(−bq/a; q)nqn(n+1)/2γn
(−bq; q)n(q; q)n
.
(6.1.13)
If n is a positive integer, then
(−bqn; qn)∞
∞
X
m=0
q(m2+m)/2am
(−bqn; qn)m(q; q)m
= (−aq; q)∞
∞
X
m=0
qn(m2+m)/2bm
(−aq; q)nm(qn; qn)m
.
(6.1.14)
∞
X
n=0
qn2+nan
(q2; q2)n(1 + aq2n+1) = (−aq2; q2)∞
∞
X
n=0
q(n2+n)/2(−a)n
(−aq; q)n
.
(6.1.15)
∞
X
n=0
(b/a; q)nq(n2+n)/2an
(q; q)n(aq; q)n
= (bq; q2)∞
(aq; q)∞
∞
X
n=0
(a2q/b; q2)nqn2+n(−b)n
(q2; q2)n(bq; q2)n
.
(6.1.16)
∞
X
n=0
(d; q)2nqn2−n(−c2/d2)n
(q2; q2)n(c; q)2n
= (c2/d2; q2)∞
(c; q)∞
∞
X
n=0
qn2−n(−c)n
(q; q)n(−c/d; q)n
.
(6.1.17)
∞
X
n=0
q3n2−2n(−a2)n
(q2; q2)n(a; q)2n
=
1
(a; q)∞
∞
X
n=0
qn2−n(−a)n
(q; q)n
.
(6.1.18)
∞
X
n=0
(a; q)nqn2−n(−b)n
(q; q)n(ab; q2)n
= (b; q2)∞
(ab; q2)∞
∞
X
n=0
(a; q2)nqn2−n(−bq)n
(q2; q2)n(b; q2)n
.
(6.1.19)
∞
X
n=0
(a2, b; q)nqn2+n(−a2/b)n
(q; q)n(a2q/b; q)n
= (a2q; q)∞
(−aq; q)∞
∞
X
n=0
(aq/b, −a; q)nq(n2−n)/2(aq)n
(a2q/b, aq, q; q)n
.
(6.1.20)
the electronic journal of combinatorics 15 (2008), #DS15
41
∞
X
n=0
(a2; q)nq(3n2+n)/2a2n
(q; q)n
= (a2q; q)∞
(−aq; q)∞
∞
X
n=0
(−a; q)nq(n2−n)/2(aq)n
(aq, q; q)n
.
(6.1.21)
Some of the identities above are derived from other identities above, as limiting cases.
However, we list them explicitly to have the available for what follows below. Several
follow from identities in Andrews’ two papers [1], [2] and some also follow from identities
in Ramanujan’s notebooks.
The transformation at (6.1.2) is a limiting case of a q-analogue of the Kummer-
Thomae-Whipple formula (see [22], page 72, equation 3.2.7), which in turn is a limiting
case of Sear’s 4φ3 transformation formula, [40].
The identity at (6.1.3) is found in Ramanujan’s lost notebook [35] and a proof can be
found in the recent book by Andrews and Berndt [9]. Equation 6.1.4 follows from 6.1.3
upon letting b →0. The identity at (6.1.5), which follows upon setting b = −aγ in (6.1.3),
is also found in Ramanujan’s notebooks (see [15], Chapter 27, Entry 1, page 262). This
identity is also equivalent to a result found in Andrews [3], where Andrews attributes it
to Cauchy.
Proofs of (6.1.6), (6.1.7), (6.1.8) and (6.1.9) can be found in [24], and alternative proofs
can be found in [16]. Identities (6.1.7), (6.1.8) and (6.1.9) were also stated by Ramanujan
in the lost notebook (see Entries 1.5.1 and 1.5.2 in [10]). Proofs of (6.1.10), (6.1.11) and
(6.1.12) also are to be found in [24]. Transformation 6.1.11 was also stated by Ramanujan
(see Entry 2.24 of [10]).
The transformation at (6.1.13) is a limiting case of Jackson’s transformation, [27] (see
also [22], page 14).
A limiting case of a transformation due to Andrews [1] leads to the identity at (6.1.14),
which was also given by Ramanujan in the lost notebook (see [10], Entry 1.4.12).
Identity 6.1.15 can be found in Ramanujan’s lost notebook, and a proof is given in
[10], Entry 1.6.5. Likewise, (6.1.16) is also from Ramanujan’s lost notebook (see [10],
Entry 1.7.3).
The transformation at (6.1.17) follows from a series transformation relating two 8φ7’s
in [22] ( (3.5.4) on pages 77–78, after replacing c with aq/c, then letting a →0 and ﬁnally
letting b →∞). The identity at (6.1.18) follows from that at (6.1.17), upon letting d →∞
and then replacing c with a.
The identity at (6.1.19) follows from a result of Andrews in [2] (see also Corollary 1.2.3
of [10], where it follows after replacing t by t/b, then letting b →∞and ﬁnally replacing
t by b).
A special case of Watson’s transformation [45] of a terminating very-well-poised 8φ7
yields (6.1.20) (see also [22], page 43, where the transformation follows upon letting
n →∞, replacing a by a2, setting c = a, d = −a and ﬁnally letting e →∞). The
transformation at (6.1.21) follows from that at (6.1.20), after letting b →∞.
Several identities on Slater’s list follow directly from some of the transformations
above, in that particular values of the parameters make one of the series identically equal
to 1, so that what remains is a “series = product” identity. We list such identities, along
with the transformations from which they derive in Table 2. Series-equivalent identities
are listed in Table 3.
the electronic journal of combinatorics 15 (2008), #DS15
42
Note that the case a = q in (6.1.5) implies that, for |q| < 1 and γ ∈C,
∞
X
n=0
qn(n−1)/2γn
(−γ, q)n+1
= 1.
The tables are to be understood as follows: let the parameters have the speciﬁed values
in the speciﬁed transformations (listed in the ﬁrst column), and then, if applicable, make
the indicated base changes in either both sides of the transformation or else recognize
that one of the series equals the series in the corresponding identity, after the indicated
base change.
For example, from row one of Table 3, if the indicated substitutions are made in
Transformation 6.1.13, we get that
∞
X
n=0
(−1; q)nqn2+n(1/q)n
(−q1/2; q)n(q1/2; q)n(q; q)n
=
1
(q1/2; q)∞
∞
X
n=0
(q1/2; q)nqn(n+1)/2(−q−1/2)n
(−q1/2; q)n(q; q)n
.
From S.6 on Slater’s list, the left side equals (−q, −q2, q3; q)∞/(q; q)∞. Replace q by q2
and we have that
(−q2, −q4; q6; q6)∞(q; q2)∞
(q2; q2)∞
=
∞
X
n=0
(q; q2)nqn2(−1)n
(−q; q2)n(q2; q2)n
.
Finally, replace q by −q and we have Identity S.29 from Slater’s list.
As a second example, from row 5 of the table, if the indicated value γ = q3/2 is
substituted in Transformation 6.1.9, we get
∞
X
n=0
qn(n+2)/2
(q3/2; q)n(q; q)n
=
1
(q3/2; q)∞
∞
X
n=0
q2n2+2n
(q2; q2)n
.
The series on the right is the series in Identity S.14 (with q replaced by q2). Thus it
follows that
∞
X
n=0
qn(n+2)/2
(q3/2; q)n(q; q)n
=
1
(q3/2; q)∞(q4, q6; q10)∞
.
Replacing q by q2 and dividing both sides by 1 −q leads to Identity S.96.
The transformations also imply some identities which we believe to be new.
For
example, if we set c = −q2, d = q1/2 and then replace q by q2 in (6.1.17), the series on
the right side becomes that in S38 (up to a multiple of 1 −q) and leads to the following
identity:
∞
X
n=0
(q; q2)2nq2n2+4n(−1)n
(q8; q8)n(−q2; q4)n+1
= (−q9, −q7, q8; q8)∞
(q2; q4)∞
(q4; q4)∞
.
(6.1.22)
A similar pairing of S39 and (6.1.17) leads to the following:
∞
X
n=0
(q; q2)2nq2n2(−1)n
(q8; q8)n(−q2; q4)n
= (−q3, −q5, q8; q8)∞
(q2; q4)∞
(q4; q4)∞
.
(6.1.23)
the electronic journal of combinatorics 15 (2008), #DS15
43
These identities are somewhat reminiscent of the following identities of Gessel and Stanton
[24]:
∞
X
n=0
(−q; q2)2nq2n2
(q8; q8)n(q2; q4)n
= (−q3, −q5, q8; q8)∞
(−q2; q4)∞
(q4; q4)∞
.
(6.1.24)
∞
X
n=0
(q; q2)2n+1q2n2+2n
(q2; q2)2n+1(−q2; q4)n+1
= (−q, −q7, q8; q8)∞(−q4; q4)∞
(q4; q4)∞
.
(6.1.25)
Transform.
Identity
a
b
γ
base change
6.1.4
S.2
0
q
6.1.4
S.3
1
q
6.1.3
S.4
−q1/2
−q
−q1/2
q →q2
6.1.4
S.9
1
−q3
q →q2
6.1.3
S.10
-1
q
q
q →q2
6.1.3
S.11
−q
q3
q2
q →q2
6.1.4
S.52
1
−q1/2
q →q2
6.1.4
S.47
-1
q1/2
q →q2
Table 2: Identities deriving directly from general transformations.
6.2
