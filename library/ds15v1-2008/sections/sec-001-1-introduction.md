---
doc_id: ds15v1-2008
doc_title: "Rogers-Ramanujan-Slater Type Identities"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: ds15v1-2008.pdf
source_sha256: aef155a324c6fdf4
toc_source: inferred
---
1.1
Theta Functions
Ramanujan’s theta function [9, p. 11, Eq. (1.1.5)] is deﬁned as
f(a, b) :=
∞
X
n=−∞
an(n+1)/2bn(n−1)/2,
(1.1.1)
the electronic journal of combinatorics 15 (2008), #DS15
1
for |ab| < 1. It is called a theta function, despite the lack of a theta in the notation,
because it is equivalent, via change of variable, to the theta function of Jacobi [46, p.
463]:
ϑ(z, w) :=
∞
X
n=−∞
(−1)nwn2e2niz,
(1.1.2)
where |w| < 1.
The following special cases of f(a, b) arise so often that they were given there own
special notation by Ramanujan [9, p. 11]:
ϕ(q) := f(q, q)
(1.1.3)
ψ(q) := f(q, q3)
(1.1.4)
f(−q) := f(−q, −q2).
(1.1.5)
Ramanujan further deﬁnes
χ(q) := f(−q2, −q2)
f(−q)
.
(1.1.6)
One of the most important results in the theory of theta functions is that they can be
expressed as inﬁnite products:
Jacobi’s triple product identity. For |ab| < 1,
f(a, b) = (−a, −b, ab; ab)∞,
(1.1.7)
where
(A; w)∞:=
∞
Y
n=0
(1 −Awn),
and
(A1, A2, . . . , Ar; w)∞:= (A1; w)∞(A2; w)∞· · · (Ar; w)∞.
An immediate corollary of (1.1.7) is thus
Corollary 1.
f(−q) = (q; q)∞
(Euler [20]))
(1.1.8)
ϕ(−q) = (q; q)∞
(−q; q)∞
(Gauß [23])
(1.1.9)
ψ(−q) = (q2; q2)∞
(−q; q2)∞
(Gauß [23])
(1.1.10)
χ(−q) = (q; q2)∞
(1.1.11)
Sometimes a linear combination of two theta series can be expressed as a single inﬁnite
product. The quintuple product identity has probably been (re)discovered more than any
other identity in the theory of q-series. The earliest published occurrence appears to be
due to Fricke [21, p. 207, Eq. (6)]. See Cooper’s survey paper for a history and many
proofs of the quintuple product identity [17].
the electronic journal of combinatorics 15 (2008), #DS15
2
Quintuple product identity.
Q(w, x) := f(−wx3, −w2x−3) + xf(−wx−3, −w2x3)
= f(wx−1, x)f(−wx−2, −wx2)
f(−w2, −w4)
= (−wx−1, −x, w; w)∞(wx−2, wx2; w2)∞.
(1.1.12)
Bailey [14, p. 220, Eq. (4.1)] showed how certain linear combinations of theta series
can be simpliﬁed to a single theta series:
f(qz2, q3z−2) + zf(q3z3, qz−2) = f(z, qz−1).
(1.1.13)
1.2
