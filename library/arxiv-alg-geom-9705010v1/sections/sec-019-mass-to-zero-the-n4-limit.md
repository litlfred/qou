---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-019-mass-to-zero-the-n4-limit
section_title: "Mass to zero: the N=4 limit"
section_number: null
pages: 27-29
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
toc_source: inferred
doc_brief: "Seiberg-Witten Integrable Systems — 32 sections: Front matter; Contents; Introduction"
---
The limit m →0 of N = 2 SYM with gauge group G and adjoint matter is
known to acquire a higher form of supersymmetry: it is the N = 4 SYM theory,
with the same gauge group. (A physicist might rather say that two of the four
28
RON Y. DONAGI
supersymmetries of N = 4 SYM are broken when the theory is perturbed by the
addition of a mass term to the Lagrangian).
The extra symmetry of the N =
4 theory means that “everything” (i.e.
the ingredients of the special geometry
package encountered in §2: the quantum moduli space, the Kahler metric, the
prepotential...) can be computed explicitly. The outcome matches perfectly to the
corresponding quantities for Hitchin’s system [Hi], i.e. the system of holomorphic
(no poles) Higgs bundles on E. (This computation is in §2.3 of [DW]). So the
physics predicts that our system should specialize, as m →0, to Hitchin’s for
SU(n), which it of course does.
(This is not really an honest “test”, since we
started out searching for deformations of Hitchin’s system, so this limit was built
in from the beginning).
τ to ∞: the ﬂow to pure N=2
One of the most interesting limits occurs as both m and τ go to inﬁnity simul-
taneously, with τ proportional to log(m). Equivalently, after an obvious rescaling,
we can keep m = 1 and let the elliptic curve degenerate (τ →∞) while adjusting
the coeﬃcients uℓin the spectral curves Cu.
The physics of this limit is easy to work out. Essentially, the mass going to
inﬁnity means that in this limit the particle is so heavy that it cannot be aﬀected
by the rest of the system; we get the pure N=2 theory, with no mass. This theory
was solved in [AF] and [KLTY]. The solution does not involve τ, as we saw in the
section on adding matter: instead of τ having a limit (which was there called τcl),
it now goes to ∞. The spectral curves found in [AF] and [KLTY] have the explicit
equation:
C′
b : w2 = (zn + b2zn−2 + · · · + bn)2 + 1
in the (z, w)-plane, where the coeﬃcients bk play a role analogous to our uℓ.
In [DW], we show that these curves are indeed recovered as the appropriate
limits of the spectral curves for the theory with adjoint mass. This is done by
substituting the τ →∞limit into the explicit equations obtained above for the Cu,
and performing the relevant rescalings. Instead of repeating the derivation here,
we will describe the geometry of this degeneration.
The pure N=2 curve C′
b is the ﬁbre product over P1 (with coordinate v) of the
rational two-sheeted cover w2 = v2 + 1 and the (again rational, with coordinate z)
n-sheeted cover v = zn + b2zn−2 + · · · + bn. In the adjoint theory, the analogue
of the double cover is just the elliptic curve E →P1 (which becomes rational in
the limit τ →∞), and Cu is again an n-sheeted branched cover of E, but it is no
longer the ﬁber product of E with any n-sheeted cover of P1. The degree 2 map
ψ : C →P1
z and the degree n map P1
z →P1
v arise only in the limit: C becomes
hyperelliptic.
The type of corank-1 degeneration involved in going from Cu to C′
b can be seen
more generally. Consider a degree n branched cover π : C →E where E is elliptic
and C has genus n. Up to isogeny, the Jacobian decomposes J(C) ≈P × E, where
P is the Prym. There are the Abel-Jacobi and Abel-Prym maps:
AJ : C →J(C)
AP : C →P
and their derivatives
φ : C →Pn−1
SEIBERG-WITTEN INTEGRABLE SYSTEMS
29
ψ : C →Pn−2.
Here φ is the canonical map and ψ is the composition of φ with linear projection
from the point 0 ∈Pn−1 determined by the isogeny.
In the degeneration, we want each of E, C to acquire a node: the singular curves
are E0, C0, with normalizations E′, C′, and singular points p0 ∈E0, q0 ∈C0 with
branches pi, qi, i = 1, 2 in the normalizations. The Jacobians J(C), J(E) become
non-compact: J(E0) is a C∗, while J(C0) is a C∗-extension of J(C′); but the Prym
P remains compact. This type of degeneration occurs when π′ : C′ →E′ is totally
ramiﬁed above each of the pi: π′−1(pi) = nqi. In this case we still have the Abel-
Jacobi and Abel-Prym maps, going to the compactiﬁed Jacobians. The derivative
φ is still the canonical map of the singular C0; its image has a node at 0 = φ(q0).
On the other hand, ψ is no longer a morphism on C0; its restriction ψ′ : C′ →Pn−2
is now the canonical map of C′.
Within the 2n −2-dimensional family of all covers π : C →E we restrict
attention to the n-dimensional family of our spectral curves. Here there exist points
p ∈E, q ∈C such that AJ(C) at q is tangent to π∗(E) at p. This is equivalent to
saying that AP : C →P(C/E) is ramiﬁed at q, or that the linear system giving ψ
has a base point at q, or that φ(q) = 0.
Combining these two eﬀects, we ﬁnd that when the corank-1 degeneration
described above occurs within the family of spectral curves, the two branches
φ(q1), φ(q2) are tangent at 0. Equivalently, the canonical map ψ′ satisﬁes ψ(q1) =
ψ(q2); so C′ is hyperelliptic, ψ is two-to-one, and O(p1 + p2) is the hyperelliptic
bundle. It follows immediately that the two maps, of degrees 2 and n respectively,
from C′ to P1 ﬁt in a cartesian diagram. The corank-1 degeneration of the spectral
curves (for the adjoint theory) therefore reproduces exactly the spectral curves of
the pure N = 2 theory.
