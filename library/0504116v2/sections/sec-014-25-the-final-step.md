---
doc_id: 0504116v2
doc_title: "On deformations of hyperbolic 3–manifolds with geodesic boundary"
section_id: sec-014-25-the-final-step
section_title: "The final step"
section_number: 2.5
pages: 17-18
source_pdf: 0504116v2.pdf
source_sha256: 24a8c998e40aed5d
toc_source: outline
doc_brief: "On deformations of hyperbolic 3-manifolds with geodesic boundary (Frigerio, AGT 6 (2006) 435–457) — the solution variety of consistency equations for a geometric partially truncated triangulation…"
---
The ﬁnal step
For γ ∈π1(DN′) let trγ : (−ε, ε) →C be the map deﬁned as follows: trγ(t) =
trace(D ˆρt(γ)), where t 7→D ˆρt(γ) ∈SL(2, C) is a smooth lift of t 7→Dρt(γ) ∈
PSL(2, C) (so trγ is well-deﬁned only up to the sign). Also recall that Dt and ρt
are respectively a developing map and a holonomy representation for the hyperbolic
structure Mt on N′. The following result can be easily deduced from the proof of the
previous proposition.
Lemma 2.10 Let γ ∈π1(DN′) be such that Dρ0(γ) is non-trivial parabolic. Then
¨trγ(0) = 0.
As a consequence of Proposition 2.7 and Lemma 2.10 we obtain the following:
Proposition 2.11
Dt and ρt can be chosen in such a way that
d
dt

t=0ρt(γ) = 0
for all γ ∈π1(N′). Moreover, if γ is a non-trivial element of a peripheral parabolic
subgroup of π1(N′), then ¨trγ(0) = 0.
Algebraic & Geometric Topology 6 (2006)
452
Roberto Frigerio
Let γ ∈π1(N′) be such that ρ0(γ)̸ = 1 and suppose rγ : (−ε, ε) →∂H3 is a smooth
path such that rγ(t) is a ﬁxed point for ρt(γ) for any t ∈(−ε, ε). We want to study
how the derivative of r(t) is related to the derivative of ρt(γ). We identify ∂H3 with
C ∪{∞} and we set
ρt(γ) =
 a(t)
b(t)
c(t)
d(t)

.
Without loss of generality we can suppose that ρ0(γ) does not ﬁx ∞and that rγ(0) =
0 ∈C ⊂∂H3, so b(0) = 0, c(0)̸ = 0. An easy computation now shows that
rγ(t) =

a(t) −d(t) ±
p
(trγ(t) + 2)(trγ(t) −2)

/ (2c(t)) .
From this formula we can readily deduce the following lemmas.
Lemma 2.12 If ρ0(γ) is non-trivial loxodromic and ˙ρ(γ) = 0, then ˙rγ(0) = 0. On
the other hand, let ρ0(γ) be non-trivial parabolic. Also assume that ˙ρ(γ) = 0 and
¨trγ(0) = 0. Then ˙rγ(0) = 0.
We can now conclude the proof of Proposition 2.6. Choose Dt and ρt as in the statement
of Proposition 2.11. Let S be a boundary component of the universal covering of ¯N′
which belongs to Spar, denote by PS the stabilizer of S in π1(N′) and choose an element
γ ∈PS with ρ0(γ)̸ = 1. By construction the projection of bS(t) to ∂H3 is ﬁxed by
ρt(γ), so Lemma 2.12 applies ensuring ˙bS(0) = 0.
Suppose now that S belongs to Sgd, and let PS be the stabilizer of S in π1(N′).
For γ ∈PS with ρ0(γ)̸ = 1 let pγ(t), qγ(t) be the ﬁxed points of ρt(γ) on ∂H3.
Note that since ρ0(γ) is loxodromic we can choose pγ, qγ to vary smoothly with
respect to t, at least in a small neighbourhood of 0. This gives ˙pγ = ˙qγ = 0 by
Lemma 2.12. Now a standard result in Kleinian group theory ensures that the set
{pγ(0), qγ(0) : γ ∈PS, ρ0(γ)̸ = 1} is dense in the closure at inﬁnity of D0(S) ⊂H3,
and this easily implies ˙bS(0) = 0.
