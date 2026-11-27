# PREREGISTRATION — heat-kernel time as RG time: sign of the colour one-loop coefficient

Bean `qou-bwwr` (route R-α3 / R-β3 of `computations/probes/mn_own_identity/GAP-STUDY-qcd-scales.md`).
Owner chose this route 2026-11-22 ("Both"). Written and pushed **before** any probe code exists.

QCD reference, **comparison only, never input**: β₀ ∝ (11/3)C_A − (4/3)T_F n_f > 0
(antiscreening: the coupling grows toward the IR). Nothing below is tuned to it.

## Setting (fixed by the corpus, not chosen)

- Colour space: V = C³ with U_q(gl₃); n strands carry V^{⊗n} = ⊕_{λ⊢n, ℓ(λ)≤3} V_λ ⊗ S_λ
  (quantum Schur–Weyl; H_n(q) acts on the S_λ factor). Colour needs N = 3 (§48: the N = 2
  nucleon model cannot see C_F).
- Heat operator, corpus form: the Reeb-holonomy Laplacian Δ_ξ = h⁻²Σ_k (q H_k + q⁻¹H_k⁻¹ − [2]),
  h = q − q⁻¹, H_k the Jucys–Murphy elements, eigenvalue on S_λ (and so on the λ-isotypic part)
  μ_λ(q) = Σ_{□∈λ} [c(□)]_q [c(□)+1]_q (`q-heat-kernel-peter-weyl.md`,
  `lean/QOU/BraidKnot/HeckeReebHolonomyLaplacian.lean`).
- Heat-kernel time t ≥ 0 read as RG proper time: t ∝ 1/μ², so **t → ∞ is the IR**.
  "Antiscreening" := the effective coupling increases with t. "Screening" := it decreases.
- Colour channels inside V^{⊗3k}: singlet = (k,k,k); adjoint (octet) = (k+1,k,k−1).
  For k = 1 this is V ⊗ Λ²V ≅ V ⊗ V̄ = 1 ⊕ 8 (the qq̄ meson channel), so no V̄ needs adding.
- q symbolic (sympy, exact). Numeric only at the proton pin `qou_substrate.constants.Q_MP` (mpmath).

## Constructions (all are reported, whatever they give)

**C1 — channel ratio under the corpus Laplacian Δ_ξ (primary).**
g²_eff(t) := W_8(t)/W_1(t), W_λ(t) = dim_q V_λ · d_λ(q) · e^{−tμ_λ(q)} (the heat trace restricted to
the λ-isotypic component). One-loop coefficient b_C1 := d log g²_eff / dt = −(μ_8 − μ_1),
t-independent. Computed for k = 1..4.
*Why primary:* it is the only heat operator the corpus defines on the Hecke tower, and the ratio of
an exchange channel to the vacuum channel is the minimal reading of "coupling" with no extra input.

**C2 — channel ratio under the U_q(gl₃) ribbon Casimir.**
Same ratio, heat operator replaced by the quadratic Casimir exponent of the ribbon element,
θ_λ = q^{⟨λ,λ+2ρ⟩} (the §48 normalisation in which T·T on the qq̄ singlet is −C_F = −4/3). Then
b_C2 = −(C(8) − C(1)) = −C_A.
*Why listed:* §48 shows colour factors are read off this exponent, so it is the colour-native
alternative to Δ_ξ.

**C3 — proper-time log coefficient, split by representation.**
Γ(t₀) = −½∫_{t₀}^∞ (dt/t)(4πt)^{−d/2} Tr e^{−t(p² + H)}, d = 4 (spatial part of the corpus
Laplacian, q⁻²|k|², contributes the (4πt)^{−2} prefactor up to q-powers). The coefficient of
log t₀ is the t² term of Tr_colour e^{−tH}: ½ Tr_R H². Evaluated for R = adjoint field (gluon,
weight C_A, index T(adj) = C_A) and R = fundamental field (quark, index T_F), H ∈ {Δ_ξ, Casimir}.
*Why listed:* this is the textbook route (heat-kernel a₂ ↔ β₀), and the α_EM per-loop arc's
a₀ = 1/(4π) is the d = 2 version of the same prefactor (shared with that arc; reported, not changed).

**Not picked, and why.**
- d/dt log of the F-projection of e^{−tΔ} (F = i f^{abc}T^a⊗T^b⊗T^c, §49/§54): Δ_ξ is central in
  H_3(q), so e^{−tΔ} is a combination of the central idempotents; its F-projection is a fixed
  linear combination of exponentials and its log-derivative is not a coupling of any channel. It
  is computed as a side check only (C1′), not scored.
- Running in tower index n (R-α2): a different bean; n counts constituents, not energy.
- Running in κ ∼ log q: varies q₀, collides with the forever gate.

## Predictions (pre-registered)

- **C1:** b_C1 = 0 exactly at k = 1. (Disclosure: I noticed this while choosing the channels:
  the contents of (2,1) are {0,1,−1} and of (1³) are {0,−1,−2}, and [c][c+1] is invariant under
  c ↦ −1−c, which maps one multiset onto the other.) For k ≥ 2: **no prediction of sign**.
- **C2:** b_C2 = −C_A = −3 < 0 at every k (Casimir positivity), i.e. the screening direction by the
  definition above. Trivial, carries no qou content.
- **C3:** ½Tr_R H² ≥ 0 for both R (sum of squares of a real spectrum at real q), so adjoint and
  fundamental enter with the **same** sign under the same statistics. An opposite sign can come
  only from (−1)^F, i.e. from spin–statistics put in by hand, not derived. n_f enters only as a
  multiplicity input.
- **n_f:** cannot enter C1 or C2 (a fixed channel of a fixed n); enters C3 only as an input count.

## Decision rule

- **HIT:** a construction gives a nonzero sign in the antiscreening direction (g² increases with t)
  **and** the adjoint (C_A) and fundamental (T_F) parts come out with opposite signs from the
  construction itself (no (−1)^F or spin factor inserted).
- **PARTIAL:** a definite nonzero antiscreening sign without a derived gluon/quark separation.
- **MISS:** sign zero, sign in the screening direction, or a separation that exists only because a
  sign was inserted.

## Honesty clause

Several constructions are listed. A definite sign of the right type in one of them is **weak**
evidence: with three readings and two signs, one hit by chance is likely. All constructions are
reported with their exact expressions; none is dropped or promoted after the fact. No measured value
(PDG, lattice) enters any computation. A miss is reported as scope (a): "not found in the searched
class (C1–C3)", not as an exclusion of a heat-kernel RG reading. Nothing here identifies the gluon
(owner ruling: the gluon of step 4 of def:derived-atom stays open).
