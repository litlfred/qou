---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties Joan Porti ∗"
section_id: sec-024-52-an-example
section_title: "An example"
section_number: 5.2
pages: 41-44
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties Joan Porti ∗ — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
---
Let me use Proposition 5.9 to compute TM,γ for the ﬁgure eight knot for
PSL2(C) and PSL 3(C). For PSL 2(C) this is done in [82], but I recall it here
for completeness.
41
Let Γ = π1M denote the fundamental group of the ﬁgure eight knot exterior.
The presentation
Γ = ⟨a, b, m /divid⟩s.alt0m a m−1 = a b, m b m−1 = b a b⟩
corresponds to the fact that it is ﬁbered over the circle, with ﬁbre a punctured
torus, whose fundamental group is the free group F2 = ⟨a, b /divid⟩s.alt0⟩. The element m
is also a meridian curve of the knot. The monodromy φ∶ F2 → F2 satisﬁes
φ(a) = a b and φ(b) = b a b.
Since F2 is the derived subgroup of Γ, every representation of Γ in PSL n+1(C)
restricts to a representation of F2 in SL n+1(C) that is ﬁxed by the monodromy
φ∗. The set of ﬁxed characters is denoted by
X(F2, SLn+1(C))φ∗
.
The following lemma is proved in [82, 39] (using that F2 is the commutator of
Γ):
Lemma 5.16. For n = 1, 2, the restriction map induces an isomorphism
Xirr(Γ , PSLn+1(C)) ≅Xirr(F2, SLn+1(C))φ∗
,
where the subindex irr stands for irreducible characters.
5.2.1 Computations for X(M 3, PSL2(C))
By Fricke-Klein theorem, the variety of characters X(F 2, SL2(C)) is isomorphic
to C3. More precisely, deﬁning
α1(ρ) = tr(ρ(a)) ,
α2(ρ) = tr(ρ(b)) ,
α3(ρ) = tr(ρ(a b)) .
Fricke-Klein theorem asserts that (α1, α2, α3) are global coordinates of X(F 2, SL2(C)).
Using the relations of traces, ∀A, B ∈SL2(C):
tr(A−1) = tr(A),
tr(AB) = tr(AB−1) − tr(A) tr(B),
we may deduce:
φ∗(α1) = α3 ,
φ∗(α2) = α2α3 − α1 ,
φ∗(α3) = α2
3α2 − α1α3 − α2 .
Thus φ∗(αi) = αi is equivalent to
α3 = α1, α 1 + α2 = α1α2 .
Then, the torsion polynomial is
det(dφ∗ − t Id) = (t − 1)(t2 + (1 − 2α1α2)t + 1). (46)
42
Removing the factor (t − 1) and evaluation at t = 1 yields
TM,l = 3 − 2α1α2 = 3 − 2α1 − 2α2 (47)
Using that the trace of the longitude l = [a, b] satisﬁes θl = α2
1+α2
2−α1−α2−2 [82],
we get T 2
M,l = 17 + 4θl. If θm denotes the trace of the meridian, the distinguished
component X0(Γ , SL2(C)) is the curve
α2
1 + α1 − 1 = θ2
m (α1 − 1). (48)
(Let me emphasize that θl and θm denote traces and not angles, I made this
choice because τ is already used for torsion.) To get the variety PSL 2(C) char-
acters instead of SL 2(C) just replace θ2
m by a new variable. From (48) and
x1 + x2 = x1x2 we deduce:
α1 + α2 = θ2
m − 1 and α1 − α2 = ±
/radical.alt1
(θ2m − 5)(θm − 1) . (49)
Thus
TM,l = T2
M,l = 5 − 2θ2
m. (50)
Proposition 5.14 can be worked out [82] to yield:
TM,m = T2
M,m = ± α1 − α2
2 = ± /par⟩nl⟩ft.alt4α1 + 1 − θ2
m
2 /par⟩nright.alt4 = ± 1
2
/radical.alt1
(θ2m − 5)(θ2m − 1). (51)
5.2.2 Computations for X(M 3, PSL3(C))
By a theorem of Lawton [56] and Will [101]: X(F2, SL3(C)) is a double branched
covering of C8 with coordinates
β1(ρ) = tr(ρ(a))
β2(ρ) = tr(ρ(a−1))
β3(ρ) = tr(ρ(b))
β4(ρ) = tr(ρ(b−1))
β5(ρ) = tr(ρ(a b))
β6(ρ) = tr(ρ(b−1a−1))
β7(ρ) = tr(ρ(a−1b))
β8(ρ) = tr(ρ(a b−1))
and the trace of l = [a, b] and its inverse, ϑl±1 , are a degree two extension of the
coordinates β1, . . . , β8, and ϑl and ϑl−1 are Galois conjugate.
As φ(l) = l, we may work in C8. Following [39], φ∗ can be computed as
φ∗(β1) = β5
φ∗(β2) = β6
φ∗(β3) = −β1β4 + β3β5 + β8
φ∗(β4) = −β2β3 + β4β6 + β7
φ∗(β5) = −β1β4β5 + β3β5
2 − β3β6 + β5β8 + β2
φ∗(β6) = −β2β3β6 + β4β6
2 − β4β5 + β6β7 + β1
φ∗(β7) = β3
φ∗(β8) = β4.
Now, setting βi = φ∗(βi), we get rid of four variables (we are left with β1, β2,
β3, and β4), and we deduce that X(F 2, SL3(C))φ∗
has three components:
43
(a) V0, with equations β1 = β2, β3 = β4.
(b) V1, with equations β1 = β2 = 1,
(c) V2, with equations β3 = β4 = 1.
The component V0 is the restriction of the distinguished component X0(M 3, PSL3(C)).
On this component, the torsion polynomial is
det(dφ∗ − t Id) = (t − 1)2 /par⟩nl⟩ft.alt1t2 + (2 − β1β3)t + 1/par⟩nright.alt1
× /par⟩nl⟩ft.alt1t4 + (−β1β3 − 2 β1 − 2 β3)t3 + (6 β1β3 + 2)t2 + (−β1β3 − 2 β1 − 2 β3)t + 1/par⟩nright.alt1 .
(52)
After getting rid of (t − 1)2 and evaluating at t = 1, we get
TM,l = (4 − β1β3)4(1 − β1)(1 − β3) . (53)
Next Corollary 5.7 is used to compute T4
M,l. The relation between traces in
SL2(C) and their image in SL 3(C) via Sym yields
β1 = β2 = α2
1 − 1 ,
β3 = β4 = α2
2 − 1 .
Using these identities in (53) we get
TM,l ○ Sym = (3 − 2α1α2)4(2 − α2
1)(2 − α2
2).
Thus by applying Corollary 5.7 and (47), one gets
T4
M,l = 4(2 − α2
1)(2 − α2
2) = 8(1 − α1α2) = 8(2 − θ2
m). (54)
