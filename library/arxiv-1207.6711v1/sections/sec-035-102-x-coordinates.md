---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-035-102-x-coordinates
section_title: "X-coordinates"
section_number: 10.2
pages: 33-36
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
ments. These are deﬁned for face points and agree with the X-coordinates of Fock and
Goncharov [8, p. 133].
The natural A4 action on vertices of ∆has two orbits. Let εv0v1v2
⟲
be a sign, which is
positive if and only if v0v1v2 is in the orbit of 012.
34
STAVROS GAROUFALIDIS, MATTHIAS GOERNER, AND CHRISTIAN K. ZICKERT
Deﬁnition 10.8. Let c be a Ptolemy assignment and let t ∈∆3
n(Z) be a face point. The
X-coordinate at t is given by
(10.10)
Xt =
Y
t∈face(v0v1v2)
c
εv0v1v2
⟲
t+v0−v1
where the product is taken over the six ordered triples of vertices v0, v1, v2 spanning the face
containing t.
As an example, the X-coodinate of t = (t0, t1, t2, 0) is given by
(10.11)
X(t0,t1,t2,0) = ct+e0−e1ct+e1−e2ct+e2−e0
ct+e0−e2ct+e1−e0ct+e2−e1
.
Deﬁnition 10.9. Let z be a shape assignment on ∆3
n and let t be a face point spanned by
v0, v1 and v2. The X-coordinate at t is given by
(10.12)
Xt = −
Y
s+e=t
ze
s.
Remark 10.10. Note that the product (10.12) consists of half of the terms involved in a
face equation. More precisely, if v0v1v2 ∈∆0 is glued to w0w1w2 ∈∆1, the face equations
are given by
(10.13)
X
εv0v1v2
⟲
t0v0+t1v1+t2v2 = X
εw0w1w2
⟲
t0w0+t1w1+t2w2.
Note that εv0v1v2
⟲
and εw0w1w2
⟲
are equal if and only if the face pairing preserves orientation.
For oriented triangulations the signs are always opposite.
Lemma 10.11. The X-coordinates transform as the shapes under reordering, i.e. we have
(10.14)
X(σ∗(c))t = X(c)sgn(σ)
σ(t)
,
X(σ∗(z))t = X(z)sgn(σ)
σ(t)
.
Proof. Unwinding the deﬁnitions, we have
(10.15)
X(σ∗c)t =
Y
t∈face(v0v1v2)
(σ∗c)
εv0v1v2
⟲
t+v0−v1 =
Y
t∈face(v0v1v2)
det(Iσ,σ(t+v0−v1))c
εv0v1v2
⟲
σ(t)+σ(v0)−σ(v1) =


Y
t∈face(v0v1v2)
det(Iσ,σ(t+v0−v1))

X(c)sgn(σ)
σ(t)
= X(c)sgn(σ)
σ(t)
.
The fact that the product of determinants equals 1 follows from Remark 5.7, which implies
that det(Iσ,σ(t+v0−v1)) = det(Iσ,σ(t+v1−v0)). Since both are ±1, their product is 1. The second
equation is obvious.
□
Lemma 10.12. The X-coordinates of a Ptolemy assignment c agree with the X-coordinates
of the corresponding shape assignment µ(c).
Proof. We must prove that
(10.16)
−
Y
s+e=t
µ(c)e
s =
Y
t∈face(v0v1v2)
c
εv0v1v2
⟲
t+v0−v1.
GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS
35
By compatibility under reordering, it is enough to prove this for t = (t0, t1, t2, 0) = t0e0 +
t1e1 + t2e2. Let t = α + (1110). By (6.8),
(10.17)
−
Y
s+e=t
µ(c)e
s = z1100
α+0010z0110
α+1000z1010
α+0010
= cα+2010,0cα+1200,0cα+0120,0
cα+2100,0cα+0210,0cα+1020,0
= ct+e0−e1ct+e1−e2ct+e2−e0
ct+e0−e2ct+e1−e0ct+e2−e1
=
Y
t∈face(v0v1v2)
c
εv0v1v2
⟲
t+v0−v1,
where the last equality follows from (10.11).
□
Lemma 10.13. One can express the X-coordinates in terms of diamond coordinates:
(10.18)
Xt =
dv0v1v2
t−v0−v1
dv0v1v2
t−v0−v2
εv0v1v2
⟲
Here t is a face point spanned by v0, v1 and v2.
Proof. It is enough to prove this for t = (t0, t1, t2, 0). Since
(10.19)
d012
t−e0−e1 = −ct+e0−e1ct+e2−e0
ctct+e2−e1
,
d012
t−e0−e2 = −ct+e0−e2ct+e1−e0
ct+e1−e2ct
,
the result follows from (10.11).
□
0
1
2
+
+
+
_
_
_
t
0
1
2
+_
+
+
+
_
_
_
Figure
23.
Exponents of the
Ptolemy coordinates involved in the
X-coordinate at t.
Figure 24.
An X-coordinate as
a quotient of two diamond coordi-
nates.
36
STAVROS GAROUFALIDIS, MATTHIAS GOERNER, AND CHRISTIAN K. ZICKERT
