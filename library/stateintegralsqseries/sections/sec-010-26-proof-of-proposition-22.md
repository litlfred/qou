---
doc_id: stateintegralsqseries
doc_title: "FROM STATE INTEGRALS TO q-SERIES"
section_id: sec-010-26-proof-of-proposition-22
section_title: "Proof of Proposition 2.2"
section_number: 2.6
pages: 12-13
source_pdf: state.integrals.qseries.pdf
source_sha256: a5e86443f35e21c0
toc_source: outline
doc_brief: "FROM STATE INTEGRALS TO q-SERIES — It is well-known to the experts that multi-dimensional state integra ls of prod- ucts of Faddeev’s quantum dilogarithm which arise in Quantum Topolog y can be"
duplicate_of: "arxiv-1304.2705v1"
---
Lemma 2.6. For part (b), we will use the series
E[m]
l
(q) =
∞
X
s=1
sk−1qs(m+1)
1 −qs
Using
log(eφn(x)) = log
 (˜q; ˜q)∞
(˜qex; ˜q)∞

+ log
 (˜q−1; ˜q−1)n
(˜q−1ex; ˜q−1)n

and the proof of part (a) of Proposition 2.2, it follows that
log(eφn(x)) = log
 (˜q; ˜q)∞
(˜qex; ˜q)∞

+ log
 (˜q−1; ˜q−1)n
(˜q−1ex; ˜q−1)n

=
∞
X
l=1
1
l!
l−1
X
r=0
Al−1,rE(0)
l,r+1(˜q)xl +
∞
X
l=1
1
l!
l−1
X
r=0
Al−1,rE[n]
l,r+1(˜q−1)xl
=
∞
X
l=1
1
l!
l−1
X
r=0
Al−1,r

E(0)
l,r+1(˜q) + E[n]
l,r+1(˜q−1)

xl
where
(42)
E[n]
l,r (q) =
n
X
k=1
qkr
(1 −qk)l .
Let
(43)
eE(n)
l,r (˜q) =





−n + E(n)
1,1 (˜q)
if l = r = 1
E(n)
l,r (˜q)
if l > 1 is odd
2E(0)
l,r (˜q) −E(n)
l,r (˜q)
if l > 1 is even
We claim that
(44)
E(0)
l,r (˜q) + E[n]
l,l−r(˜q−1) = eE(n)
l,r (˜q)
for l > r ≥1 and
(45)
E(0)
1,1(˜q) + E[n]
1,1(˜q−1) = eE(n)
1,1 (˜q)
Assuming Equations (44) and (45), it follows that
log(eφn(x)) =
∞
X
l=1
1
l!
l−1
X
r=0
Al−1,r eE(n)
l,r+1(˜q)xl
=
∞
X
l=1
1
l!
eE(n)
l
(˜q)xl
where the last step follows from part (b) of Lemma 2.5.
FROM STATE INTEGRALS TO q-SERIES
13
It remains to prove Equations (44) and (45). Equation (44) follows from the deﬁnition of
eE(n)
1,1 (˜q) and
E(0)
l,r (˜q) + E[n]
l,l−r(˜q−1) =
∞
X
k=1
˜qkr
(1 −˜qk)l +
n
X
k=1
˜q−k(l−r)
(1 −˜q−k)l
=
∞
X
k=1
˜qkr
(1 −˜qk)l + (−1)l
n
X
k=1
˜qkr
(1 −˜qk)l
= (1 + (−1)l)
n
X
k=1
˜qkr
(1 −˜qk)l +
∞
X
k=n+1
˜qkr
(1 −˜qk)l
Equation (45) follows from
E(0)
1,1(˜q) + E[n]
1,1(˜q−1) =
∞
X
k=1
˜qk
1 −˜qk +
n
X
k=1
˜q−k
1 −˜q−k
=
∞
X
k=1
1 −1 + ˜qk
1 −˜qk
−
n
X
k=1
1
1 −˜qk = −n +
∞
X
k=n+1
˜qk
1 −˜qk
This completes the proof of Proposition 2.2.
□
