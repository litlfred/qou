---
doc_id: arxiv-1001.2933v4
doc_title: "Analytic Continuation Of Chern-Simons Theory"
section_id: sec-003-2-2-role-of-morse-theory
section_title: "Role Of Morse Theory"
section_number: "2.2"
pages: 10-11
source_pdf: 1001.2933v4.pdf.txt
source_sha256: b02636c86d593c02
toc_source: inferred
---
2.2 Role Of Morse Theory
Finding a suitable integration cycle in the infinite-dimensional path integral of Chern-Simons
gauge theory may seem hopeless at first sight. What saves the day is that suitable integration
contours can be found by Morse theory and steepest descent (or in a different language, via
Picard-Lefschetz theory). The facts we need for understanding oscillatory integrals have been
described in [35–40] (and the aspiration of applying this approach to Feynman integrals is
stated in [37], p. 321). Section 3 of the present paper is devoted to a hopefully self-contained
exposition of this approach, with an emphasis on the aspects that we need in Chern-Simons
theory. The basic idea of the theory is to associate potential integration cycles to components
of the critical point set of the extended action I(A, Ae).
What makes it practical to use this formalism in Chern-Simons theory is that the critical
points are accessible. As long as t and et are both non-zero, the critical point equation derived
from the analytically continued action (2.12) is
F = Fe = 0, (2.14)
where F = dA+A∧A and Fe = dAe+A∧e Ae are the curvatures of the two connections. Hence
a critical point is just a pair of flat connections, corresponding to a pair of homomorphisms
from the fundamental group of M to the complex Lie group G. (We postpone to section 4 an
important detail about the value of the Chern-Simons invariant at a critical point.) Hence
in Chern-Simons theory on a given three-manifold M, the critical points can be effectively
described; this is typically not true for oscillatory Feynman integrals.
For simplicity, we assume until section 3.3.2 that the critical points are isolated points.
Let Σ be the set of critical points and denote the critical points as pσ, σ ∈ Σ. Then to each
pσ, we attach an integration cycle Jσ that is obtained by downward or gradient flow from σ,
taking the real part of the action as a Morse function. (Details are explained in section 3.)
The Jσ, which are known as Lefschetz thimbles, are constructed so that the integral over
Jσ always converges, regardless of the choice of σ or of the parameters in the action. Any
suitable integration cycle C for the sort of integral that we are interested in is equivalent to
a linear combination of the Jσ with integer coefficients:
C =
X
σ
nσJσ, nσ ∈ Z. (2.15)
The coefficients nσ can themselves be computed via Morse theory. To do this, one attaches
to each critical point pσ another cycle Kσ by upwards gradient flow starting from pσ. The
expansion coefficients in eqn. (2.15) can be computed as the intersection pairing of the
integration cycle C with the Kσ:
nσ = hC, Kσi. (2.16)
10

One might naively think that all critical points would contribute to the integral with
nσ = 1 (or with nσ = ±1, since in general the Jσ do not have natural orientations), but
this cannot be so. For example, in Chern-Simons theory with real s, there are complex
critical points at which the action I has a negative imaginary part; their inclusion would
lead to a pathologically wrong exponential growth of the partition function for large real
s. In fact, for real s, with C taken to be the real cycle CR defined by Ae = A, real critical
points (whose contributions to the path integral are oscillatory) all have nσ = 1, but critical
points that would make exponentially large contributions to the path integral have nσ = 0.
These statements will be deduced from (2.16). However, there is no simple formula for nσ
for critical points whose contributions to the real s path integral are exponentially small.
