---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-036-522-computations-for-xm3psl3c
section_title: "Computations for X(M3,PSL3(C))"
section_number: 5.2.2
pages: 43-44
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
Computations for X(M 3,PSL3(C))
By a theorem of Lawton [56] and Will [101]: X(F2,SL3(C)) is a double branched
covering of C8 with coordinates
β1(ρ) = tr(ρ(a))
β2(ρ) = tr(ρ(a−1))
β3(ρ) = tr(ρ(b))
β4(ρ) = tr(ρ(b−1))
β5(ρ) = tr(ρ(ab))
β6(ρ) = tr(ρ(b−1a−1))
β7(ρ) = tr(ρ(a−1b))
β8(ρ) = tr(ρ(ab−1))
and the trace of l = [a,b] and its inverse, ϑl±1, are a degree two extension of the
coordinates β1,... ,β8, and ϑl and ϑl−1 are Galois conjugate.
As φ(l) = l, we may work in C8. Following [39], φ∗can be computed as
φ∗(β1) = β5
φ∗(β2) = β6
φ∗(β3) = −β1β4 + β3β5 + β8
φ∗(β4) = −β2β3 + β4β6 + β7
φ∗(β5) = −β1β4β5 + β3β5
2 −β3β6 + β5β8 + β2
φ∗(β6) = −β2β3β6 + β4β6
2 −β4β5 + β6β7 + β1
φ∗(β7) = β3
φ∗(β8) = β4.
Now, setting βi = φ∗(βi), we get rid of four variables (we are left with β1, β2,
β3, and β4), and we deduce that X(F 2,SL3(C))φ∗has three components:
43
(a) V0, with equations β1 = β2, β3 = β4.
(b) V1, with equations β1 = β2 = 1,
(c) V2, with equations β3 = β4 = 1.
The component V0 is the restriction of the distinguished component X0(M 3,PSL3(C)).
On this component, the torsion polynomial is
det(dφ∗−tId) = (t −1)2 (t2 + (2 −β1β3)t + 1)
× (t4 + (−β1β3 −2 β1 −2 β3)t3 + (6 β1β3 + 2)t2 + (−β1β3 −2 β1 −2 β3)t + 1) .
(52)
After getting rid of (t −1)2 and evaluating at t = 1, we get
TM,l = (4 −β1β3)4(1 −β1)(1 −β3).
(53)
Next Corollary 5.7 is used to compute T4
M,l. The relation between traces in
SL2(C) and their image in SL3(C) via Sym yields
β1 = β2 = α2
1 −1 ,
β3 = β4 = α2
2 −1 .
Using these identities in (53) we get
TM,l ○Sym = (3 −2α1α2)4(2 −α2
1)(2 −α2
2).
Thus by applying Corollary 5.7 and (47), one gets
T4
M,l = 4(2 −α2
1)(2 −α2
2) = 8(1 −α1α2) = 8(2 −θ2
m).
(54)
