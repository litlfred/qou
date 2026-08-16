---
doc_id: sigma12-065
doc_title: ""
section_id: sec-007-5-vector-of-riemann-constants
section_title: "Vector of Riemann constants"
section_number: 5
pages: 15-16
source_pdf: sigma12-065.pdf
source_sha256: a6e0e0da5cc5ff9b
doc_brief: "Bring’s Curve: its Period Matrix and the Vector of Riemann Constants ⋆ — Bring’s curve is the genus 4 Riemann surface with automorphism group of maximal size, S5."
---
5 Vector of Riemann constants
We shall now calculate the vector of Riemann constants for Bring’s curve determining various
other quantities on the way. This vector together with Riemann’s theta function and the Abel
map provide a bridge between the analytic and algebraic structures of a Riemann surface C,
and as such are critical elements in the implementation of the modern approach to integrable
systems.
5.1 The vector of Riemann constants
Riemann established the fundamental result,
θ(e|τ) = 0 ⇐⇒ e≡A Q
(g−1∑
i=1
Pi
)
−KQ∈ JacC,
where θ is Riemann’s theta function, AQ is the Abel map with base point Q∈C , τ is the
period matrix, g is the genus of C, Pi∈C and the equivalence holds in the Jacobian Jac C =
Cg/(Zg +τ Zg). (We are assuming that g≥ 1 in what follows.) Both the period matrix τ and
the Abel map depend on a choice of homology basis, the latter through the basis of normalized
holomorphic differentials ω whereAQ(P ) =
∫P
Q ω. The vector KQ is known as the vector of
Riemann constants7 (with base point Q) and it also depends on the choice of homology basis.
Let{γi}2g
i=1 = {ai, bi}g
i=1 be our choice of homology basis of H1(C, Z), where ai and bi are
canonically paired. One has that
KQj =−1
2 (τjj + 1) +
∑
k⁄=j
∮
ak
ωk(P )
∫ P
Q
ωj.
Because of the integrations involved, both τ and KQ are rather transcendental objects. One
may also express
KQ≡A∗ (∆− (g− 1)Q) =
∫ ∆
∗
ω− (g− 1)
∫ Q
∗
ω =AQ (∆), (5.1)
which holds for any base point∗ of the Abel map and where the degree (g− 1) divisor ∆ is that
of the Sz¨ ego-kernel [12]. The critical relation for us is the linear equivalence
2∆∼KC,
and so
2KQ≡A Q(KC). (5.2)
HereKC is the canonical divisor ofC, the unique divisor class of degree 2g−2 of any meromorphic
differential on the curve, and (hereafter) ∼ denotes linear equivalence. Thus ∆ gives a square
root of the canonical bundle or spin-structure on C; the set Σ of divisor classes D such that
2D∼K C is called the set of theta characteristics ofC. The vector of Riemann constants gives
us the shift in the Jacobian necessary to identify spin structures with the 2-torsion points of the
Jacobian. (Recall, an N-torsion point x is such that Nx lies in the period lattice.)
7The choice of sign of this vector depends on author. We will use that of Fay [12] whose convention is the
negative of Farkas and Kra [11].
16 H.W. Braden and T.P. Northover
