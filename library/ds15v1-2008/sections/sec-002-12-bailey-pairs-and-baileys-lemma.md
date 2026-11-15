---
doc_id: ds15v1-2008
doc_title: "Rogers-Ramanujan-Slater Type Identities"
section_id: sec-002-12-bailey-pairs-and-baileys-lemma
section_title: "Bailey Pairs and Bailey’s lemma"
section_number: 1.2
pages: 3-4
source_pdf: ds15v1-2008.pdf
source_sha256: aef155a324c6fdf4
toc_source: inferred
---
Of central importance are the two Rogers-Ramanujan identities, which each assert the
equality of a certain q-series with a ratio of theta functions:
G(q) :=
∞
X
n=0
qn2
(q; q)n
= f(−q2, −q3)
f(−q)
(1.2.1)
H(q) :=
∞
X
n=0
qn(n+1)
(q; q)n
= f(−q, −q4)
f(−q)
,
(1.2.2)
where
(a; q)n :=



(1 −a)(1 −aq) · · ·(1 −aqn−1)
if n ∈Z+
1
if n = 0
[(1 −aq−1)(1 −aq−2) · · · (1 −aqn)]−1
if n ∈Z−.
Note that it is customary to write (A)n for (A; q)n and (A)∞for (A; q)∞.
Using (1.1.7), and after some simpliﬁcation, the right hand sides of (1.2.1) and (1.2.2)
can be expressed as, respectively, the inﬁnite products
∞
Y
n=1
1
(1 −q5n−4)(1 −q5n−1)
and
∞
Y
n=1
1
(1 −q5n−3)(1 −q5n−2).
Normally, an “identity of Rogers-Ramanujan type” asserts the equality of a certain
q-series with a ratio of a theta series (or perhaps a linear combination of several theta
series) to one of f(−qm), ϕ(−qm), or ψ(±qm) for some positive integer m. Sometimes,
however, the term is applied to other types of q-series—product identities, or polynomial
generalizations thereof. In particular, we limit ourselves to considering q-series in which
the power of q is quadratic in the summation variable.
L. J. Rogers [36, 37] and S.
the electronic journal of combinatorics 15 (2008), #DS15
3
Ramanujan [9, 10] discovered a number of identities of this type. W. N. Bailey studied
Rogers’s work and as a result was able to simplify and extend it in [12, 13]. L. J. Slater
used and extended Bailey’s methods to obtain a large collection of identities of Rogers-
Ramanujan type in [40, 41].
