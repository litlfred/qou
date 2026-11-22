---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-035-521-computations-for-xm3psl2c
section_title: "Computations for X(M3,PSL2(C))"
section_number: 5.2.1
pages: 42-43
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
Computations for X(M 3,PSL2(C))
By Fricke-Klein theorem, the variety of characters X(F 2,SL2(C)) is isomorphic
to C3. More precisely, deﬁning
α1(ρ) = tr(ρ(a)),
α2(ρ) = tr(ρ(b)),
α3(ρ) = tr(ρ(ab)).
Fricke-Klein theorem asserts that (α1,α2,α3) are global coordinates of X(F 2,SL2(C)).
Using the relations of traces, ∀A,B ∈SL2(C):
tr(A−1)
= tr(A),
tr(AB)
= tr(AB−1) −tr(A)tr(B),
we may deduce:
φ∗(α1)
= α3 ,
φ∗(α2)
= α2α3 −α1 ,
φ∗(α3)
= α2
3α2 −α1α3 −α2 .
Thus φ∗(αi) = αi is equivalent to
α3 = α1,
α1 + α2 = α1α2 .
Then, the torsion polynomial is
det(dφ∗−tId) = (t −1)(t2 + (1 −2α1α2)t + 1).
(46)
42
Removing the factor (t −1) and evaluation at t = 1 yields
TM,l = 3 −2α1α2 = 3 −2α1 −2α2
(47)
Using that the trace of the longitude l = [a,b] satisﬁes θl = α2
1+α2
2−α1−α2−2 [82],
we get T 2
M,l = 17+4θl. If θm denotes the trace of the meridian, the distinguished
component X0(Γ,SL2(C)) is the curve
α2
1 + α1 −1 = θ2
m (α1 −1).
(48)
(Let me emphasize that θl and θm denote traces and not angles, I made this
choice because τ is already used for torsion.) To get the variety PSL2(C) char-
acters instead of SL2(C) just replace θ2
m by a new variable. From (48) and
x1 + x2 = x1x2 we deduce:
α1 + α2 = θ2
m −1
and
α1 −α2 = ±
√
(θ2m −5)(θm −1).
(49)
Thus
TM,l = T2
M,l = 5 −2θ2
m.
(50)
Proposition 5.14 can be worked out [82] to yield:
TM,m = T2
M,m = ±α1 −α2
2
= ±(α1 + 1 −θ2
m
2
) = ±1
2
√
(θ2m −5)(θ2m −1).
(51)
