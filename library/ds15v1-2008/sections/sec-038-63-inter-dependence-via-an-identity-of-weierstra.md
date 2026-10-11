---
doc_id: ds15v1-2008
doc_title: "Rogers-Ramanujan-Slater Type Identities"
section_id: sec-038-63-inter-dependence-via-an-identity-of-weierstra
section_title: "Inter-dependence Via an Identity of Weierstrass"
section_number: 6.3
pages: 48-50
source_pdf: ds15v1-2008.pdf
source_sha256: aef155a324c6fdf4
toc_source: inferred
---
The identity in question is given in the lemma below. We ﬁrst deﬁne
[x; q]∞:= (x, q/x; q)∞,
[x1, . . . xn; q]∞= [x1; q]∞. . . [xn; q]∞,
and note that [x−1; q]∞= −x−1[x; q]∞.
Lemma 13. Let a1, a2, . . . , an; b1, b2, . . . , bn be non-zero complex numbers such that
i) ai̸ = qnaj, for all i̸ = j and all n ∈Z,
ii) a1a2 . . . an = b1b2 . . . bn. Then
n
X
i=1
Qn
j=1[aib−1
j ; q]∞
Qn
j=1,j̸=i[aia−1
j ; q]∞
= 0.
(6.3.1)
This lemma appears in [46] (page 45) and a proof can be found in [31]. If n = 3, then
(6.3.1) can be written as
[a1/b1, a1/b2, a1/b3; q]∞
[a1/a2, a1/a3; q]∞
+ [a2/b1, a2/b2, a2/b3; q]∞
[a2/a1, a2/a3; q]∞
+ [a3/b1, a3/b2, a3/b3; q]∞
[a3/a1, a3/a2; q]∞
= 0. (6.3.2)
the electronic journal of combinatorics 15 (2008), #DS15
48
The dependence of identities via (6.3.1) is more tenuous than dependence via series-
equivalence or the Jacobi triple product. We give the following example to illustrate the
concept. If we replace q by q10 in (6.3.2) and set
{a1, a2, a3; b1, b2, b3} = {1, −q5, q; q−1, −q−2, q9},
then after a little simpliﬁcation we get that
q[q, q, −q2, −q4; q10]∞+ [q, q3, −q4, −q4; q10]∞−[q2, q2, −q3, −q5; q10]∞= 0.
(6.3.3)
This identity can be rearranged to give
(−q, −q, q2; q2)∞=
(q10; q10)∞
(q, q9, −q2, −q8; q10)∞
+
q(q10; q10)∞
(q3, q7, −q4, −q6; q10)∞
(6.3.4)
Similarly, if we replace q by q10 in (6.3.2) and set
{a1, a2, a3; b1, b2, b3} = {1, −q5, q6; q−1, −q−2, q14},
we get that
−q[q, −q, −q2, q4; q10]∞+ [−q, q3, q4, −q4; q10]∞−[q2, −q2, q3, −q5; q10]∞= 0.
(6.3.5)
This identity can likewise be rearranged to give
(−q5, −q5, q10; q10)∞=
(q10; q10)∞
(q, q9, −q2, −q8; q10)∞
−
q(q10; q10)∞
(q3, q7, −q4, −q6; q10)∞
(6.3.6)
Finally, if we replace q by −q and subtract, we get that
(q5, q5, q10; q10)∞−(q, q, q2; q2)∞=
2q(q10; q10)∞
(−q3, −q7, −q4, −q6; q10)∞
(6.3.7)
See the paper by Cooper and Hirschhorn [18] for these and similar identities.
We now exhibit two identities of Rogers-Ramanujan type which are related via (6.3.1).
The ﬁrst appears in [16]:
∞
X
n=0
q(n2+3n)/2(−q; q)n
(q; q2)n+1(q; q)n+1
=
(q10; q10)∞
(q; q)∞(q; q2)∞(−q3, −q4, −q6, −q7; q10)∞
.
(6.3.8)
The second is an identity of Rogers (see [38]):
∞
X
n=0
qn(n+1)/2(−1; q)n
(q; q)n(q; q2)n
= (q5, q5, q10; q10)∞
(q; q)∞(q; q2)∞
.
(6.3.9)
One easily checks (by re-indexing the second sum) that
∞
X
n=0
qn(n+1)/2(−1; q)n
(q; q)n(q; q2)n
−2q
∞
X
n=0
q(n2+3n)/2(−q; q)n
(q; q2)n+1(q; q)n+1
= 1.
the electronic journal of combinatorics 15 (2008), #DS15
49
That
(q5, q5, q10; q10)∞
(q; q)∞(q; q2)∞
−2q
(q10; q10)∞
(q; q)∞(q; q2)∞(−q3, −q4, −q6, −q7; q10)∞
= 1
follows from (6.3.7). We say that pairs of identities which are dependent via (6.3.1) are
W-dependent.
We give one other example of a pair of identities are W-dependent. The ﬁrst is S.56:
∞
X
n=0
(−q; q)nqn(n+2)
(q; q2)n+1(q; q)n+1
= (−q, −q11, q12; q12)∞
(q; q)∞
.
(6.3.10)
The second is
∞
X
n=0
(−1; q)nqn2
(q; q2)n(q; q)n
= (q3, q3, q6; q6)∞(−q; q)∞
(q; q)∞
.
(6.3.11)
It is easy to check (by re-indexing, as above) that
∞
X
n=0
(−1; q)nqn2
(q; q2)n(q; q)n
−2q
∞
X
n=0
(−q; q)nqn(n+2)
(q; q2)n+1(q; q)n+1
= 1.
That
(q3, q3, q6; q6)∞(−q; q)∞
(q; q)∞
−2q(−q, −q11, q12; q12)∞
(q; q)∞
= 1
follows from the following identity (proved by Cooper and Hirschhorn in [18], again making
use of (6.3.2)):
(q3, q3, q6; q6)∞−(q, q, q2; q2)∞= 2q(−q, −q11, q12; q12)∞(q; q2)∞.
It is possible that new, as yet unknown identities of the Rogers-Ramanujan type may be
derivable from existing identities through W-dependence.
7
