---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-015-45-modular-maps-and-the-right-picture
section_title: "Modular maps and the right picture"
section_number: 4.5
pages: 31-34
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
Modular maps and the right picture
In this section we describe the remaining objects deﬁned in Section 2.3, as well as
the description of the right invariant picture for the quantum plane.
From now on, let us restrict all operators on the dense subspace W, and we will
extend any bounded operators on W to the whole space H.
Proposition 4.13. The conjugation map T (cf. (2.20)) is given by
T (f) = f(−s, −t)e2πist,
(4.35)
T ∗is given by
T ∗(f) = f(−s, −t)e2πiste2πsQ.
(4.36)
Hence the modular operator ∇= T ∗T is given by
∇(f) = f(s, t)e2πsQ,
(4.37)
and the modular conjugation J = T ∇−1
2 = ∇
1
2 T is given by
J(f) = f(−s, −t)e2πisteπsQ.
(4.38)
We have J2 = J∗J = Id.
Proof. It suﬃces to establish the map T ∗. Since T is anti-linear, from the deﬁnition
31
of the adjoint of anti-linear maps, we have:
⟨T f, g⟩
=
⟨f, T ∗g⟩
RHS
=
ZZ
T ∗g(s, t + iQ
2 )f(s, t + iQ
2 )dsdt
=
ZZ
T ∗g(s, t + iQ
2 )f(s, t + iQ
2 )dsdt
LHS
=
ZZ
g(s, t + iQ
2 )f(−s, −t −iQ
2 )e2πis(t+ iQ
2 )dsdt
=
ZZ
g(s, t −iQ
2 )f(−s, −t + iQ
2 )e2πis(t+ iQ
2 )dsdt
=
ZZ
g(−s, −t −iQ
2 )f(s, t + iQ
2 )e2πi(−s)(−t+ iQ
2 )dsdt.
Hence T ∗g = g(−s, −t)e2πiste2πsQ.
Corollary 4.14. The modular group σt(x) = ∇itx∇−it is given by
σt(A)
=
e2πbQtA,
(4.39)
σt(B)
=
B.
(4.40)
or in other words
σt′(f) = f(s, t)e2πQt′s
(4.41)
With this expression of the modular group, it is now easy to see the following:
Corollary 4.15. The Haar weight is a KMS weight, in the sense of [24]. That is
h ◦σt
=
h
for every t ∈R,
(4.42)
h(a∗a)
=
h(σ i
2 (a)σ i
2 (a)∗)
for every a ∈A.
(4.43)
Proof. The ﬁrst equation is obvious from (4.41). For the second equation, it follows
by combining (4.35), (4.41) and Proposition 4.11.
Proposition 4.16. The scaling constant ν is given by
ν = e−2πQ2 > 0,
(4.44)
the modular element δ is given by
δ = A−Q
b ,
(4.45)
and the right Haar weight is given by
ψ(f) = f(−iQ, iQ)e−πiQ2.
(4.46)
32
Proof.
h(τt′(f))
=
h(
ZZ
f(s, t)e−2πbQt′ib−1tAib−1sBib−1tdsdt
=
h(
ZZ
f(s, t)e−2πiQt′tAib−1sBib−1tdsdt
=
f(0, iQ)e−2πiQt′iQ
=
f(0, iQ)e2πQ2t′,
hence ν = e−2πQ2.
Obviously
σt(δ) = e2πbQt(−Q
b )δ = e−2πQ2tδ = νtδ.
(4.47)
Finally for the right Haar weight, recall that
R(A)
=
A−1,
R(B)
=
q−1BA−1,
hence
ψ(f)
=
h(R(f))
=
h(
ZZ
f(s, t)(q−1BA−1)ib−1tA−ib−1sdsdt)
=
h(
ZZ
f(s, t)q−ib−1tq−ib−1t(ib−1t−1)q−2b−2t(s+t)A−ib−1(s+t)Bib−1tdsdt)
=
h(
ZZ
f(s, t)e−πi(2st+t2)A−ib−1(s+t)Bib−1tdsdt
=
h(
ZZ
f(−s −t, t)eπi(2st+t2)Aib−1sBib−1tdsdt
=
f(−iQ, iQ)eπi(iQ)2
=
f(−iQ, iQ)e−πiQ2.
We have an isometry HR −→HL between the Hilbert space associated to the
right and left invariant Haar weights respectively, given in Proposition 2.15 by
ΛR(a) = ΛL(aδ
1
2 ) = ΛL(aA−Q
2b ).
(4.48)
Explicitly, we can rewrite all the maps in the right picture. We list here for conve-
nience.
33
Proposition 4.17. We have
ΛR
Z
R+i0
Z
R
f(s, t)Aib−1sBib−1tdsdt

= f(s −iQ
2 , t)e−πQt,
(4.49)
with inner product given by
⟨f, g⟩R =
Z
R
Z
R
g(s −iQ
2 , t + iQ
2 )f(s −iQ
2 , t + iQ
2 )e−2πQtdsdt.
(4.50)
TRf(s, t)
=
f(−s, −t)e2πiste−πQt,
(4.51)
T ∗
Rf(s, t)
=
f(−s, −t)e2πist+πQt+2πQs−πiQ2,
(4.52)
∇Rf(s, t)
=
f(s, t)e2πsQ+2πtQ−πiQ2,
(4.53)
JRf(s, t)
=
f(−s, −t)e2πisteπsQe−πiQ2
2
.
(4.54)
In particular, we recover the relation [25]
JR = νi/4J.
(4.55)
