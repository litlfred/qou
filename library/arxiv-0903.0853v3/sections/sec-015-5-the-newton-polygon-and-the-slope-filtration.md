---
doc_id: arxiv-0903.0853v3
doc_title: "Jean-Pierre Ramis"
section_id: sec-015-5-the-newton-polygon-and-the-slope-filtration
section_title: "The Newton polygon and the slope filtration"
section_number: 5
pages: 23-24
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
---
17
To follow the next example, recall from paragraph 2.1.2.1 how we vectori-
alize a scalar q-diﬀerence equation P.f = 0, P ∈Dq, by a q-diﬀerence sys-
tem σqX = AX, and then associate to this system a q-diﬀerence module
(C({z})n, ΦA). Remember that the latter is isomorphic to some Dq/DqQ (by
the cyclic vector lemma and left euclideanity of Dq), but that Q is not equal
to P, it is dual to P.
Example 2.2.2. — Vectorializing an analytic equation of order two yields:
σ2
qf+a1σqf+a2f = 0 ⇐⇒σqX = AX, with X =
 f
σqf

and A =
 0
1
−a2
−a1

.
The associated module is (C({z})2, ΦA). Putting e :=
1
0

, one has ΦA(e) =
−a1/a2
1

and:
Φ2
A(e) = −1
a2
e+ −σqa1
σqa2
ΦA(e) =⇒M ≃Dq/Dq ˆL, where ˆL := σ2
q + σqa1
σqa2
σq+ 1
a2
,
ˆL thus being a dual of L := σ2
q + a1σq + a2 ∈Dq.
Note that if we started from vector e′ :=
0
1

, we would compute likewise:
Φ2
A(e′) = −1
σqa2
e′+ −a1
σqa2
ΦA(e′) =⇒M ≃Dq/Dq ˆL′, where ˆL′ := σ2
q+ a1
σqa2
σq+
1
σqa2
,
another dual of L.
However, they give the same Newton polygon, since
v0(a1/σqa2) = v0(σqa1/σqa2) and v0(1/σqa2) = v0(1/a2).
We now specialize to the equation satisﬁed by a q-analogue of the Euler series,
the so-called Tshakaloﬀ(3)series:
(2.1)
Q(z) :=
X
n≥0
qn(n−1)/2zn.
Then ˆφ := Q satisﬁes:
ˆφ = 1 + zσq ˆφ =⇒L.ˆφ = 0,
where:
qzL := (σq −1)(zσq −1) = qzσ2
q −(1 + z)σq + 1.
3. We use the cyrillic letter Q (“tsh”) to denote it.
18
CHAPTER 2. SOME GENERAL NONSENSE
By our previous deﬁnitions, S(L) = {0, 1} (both multiplicities equal 1). The
second computation of a dual above implies that:
M ≃Dq/Dq ˆL, where ˆL := σ2
q −q(1 + z)σq + q2z = (σq −qz)(σq −q),
whence S(M) = S(ˆL) = {−1, 0} (both multiplicities equal 1).
This computation relies on the obvious vectorialisation with matrix A =

0
1
−1/qz
(1 + z)/qz

. However, we also have:
L.f = 0 ⇐⇒σqY = BY, with Y =

f
zσqf −f

and B =
z−1
z−1
0
1

.
The fact that matrix A is analytically equivalent to an upper triangular matrix
comes from the analytic factorisation of ˆL; the exponents of z on the diagonal
are the slopes: this, as we shall see, is a general fact when the slopes are
integral.
