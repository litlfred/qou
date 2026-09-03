---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-039-94-analysis-of-the-second-term-in-the-pointwise
section_title: "Analysis of the second term in the pointwise estimate I. We proceed to estimate the"
section_number: 9.4
pages: 35-35
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
second term on the right-hand side of (9.2.3). We write
(9.4.1)
v0(z) := K⟨k⟩
2,m(w, z)χ0(z) −P2,m[K⟨k⟩
2,m(·, w)χ0](z),
and realize that v = v0 is the norm minimal solution in L2(Ω, e−2mQ) of the partial diﬀerential
equation
¯∂2
zv(z) = ¯∂2
z[χ0(z)K⟨k⟩
2,m(z, w)].
For the ¯∂-equation, there are the classical Hörmander L2-estimates [18], [19], which are based
on integration by parts and a clever duality argument.
Here, luckily we can just iterate
the Hörmander L2-estimates to control the solution to the ¯∂2-equation.
We recall that the
Hörmander L2-estimate asserts that there exists a (norm-minimal) solution u0 to ¯∂u0 = f with
Z
Ω
|u0|2e−2φdA ≤1
2
Z
Ω
| f|2 e−2φ
∆φ dA,
provided f ∈L2
loc(Ω) and the right-hand side integral converges.
Proposition 9.1. Let Ωbe a domain in C and suppose φ : Ω→R is a C4-smooth function with both
∆φ > 0 and ∆φ + 1
2∆log ∆φ > 0 on Ω. Assume that f ∈L2
loc(Ω). Then there exists a (norm-minimal)
solution v0 to the problem ¯∂2v0 = f with
Z
Ω
|v0|2e−2φ ≤1
4
Z
Ω
| f|2
e−2φ
[∆φ][∆φ + 1
2∆log ∆φ]
dA,
provided that the right-hand side is ﬁnite.
Proof. We apply Hörmander’s L2-estimates for the ¯∂-operator with respect to the two weights
φ and φ + 1
2 log ∆φ. The details are quite straightforward and left to the reader.
□
