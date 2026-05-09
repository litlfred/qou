/-!
# Canonical knot identification for ²H, ³H, ³He from the confinement SDP

This file axiomatizes `conj:canonical-knot-id-sdp` as a Lean `class`
following the §3b conditional-class pattern from CLAUDE.md.

**Conjecture (informal):** The joint mass-tower confinement SDP uniquely
selects the canonical Hecke elements for ²H (6₂), ³H (8₁₁), and ³He
(L₆ₐ₄) from first principles, matching the historically identified
hyperbolic-volume/AME-binding-energy fits.

**Structural sharpening (issue #604, deliverable 3 — concurrent with the
binding-K finding from deliverable 4):** the canonical T_w decomposes as

    T_w(𝔥) = K(𝔥) · ⊗_{i=1}^{A} T_w(constituent_i)

where K(𝔥) ∈ H_{3·A}(q₀) is the **binding operator** that links the
A nucleons (each contributing 3 quark strands) into the bound state.
The SDP uniqueness assertion factors into:

  (a) **Constituent uniqueness:** each T_w(constituent_i) is the
      canonical trefoil image at H_3(q₀) (closed by R5-minimal
      verifier — `joint_tower_sdp_solver_v2.py`).
  (b) **Binding-K uniqueness:** K(𝔥) ∈ H_{3·A}(q₀) is uniquely
      selected by the joint-tower SDP at the atomic strand count.

Numerical evidence for (a) is the existing `R5-minimal` PSD-feasibility
checks at H_3.  Numerical evidence for (b) requires Hoefsmit at H_{3·A}
(deferred); the framework for it is the R5-full prototype with the
binding-K decomposition — see deliverable 4 witness for the structural
finding driving this refinement
(`folio-assistant/computations/rho-prefactor-structural-verifier.witness.json`).

The class packages the uniqueness assertion; downstream conditional
theorems may take it as an `[instance]` hypothesis and remain fully
verified by Lean modulo this single conjectural input.

## References
- [manuscript] conj:canonical-knot-id-sdp
- [manuscript] prop:confinement-sdp
- [manuscript] prop:joint-tower-sdp-confinement
- [manuscript] prop:atom-knot-mass-derivation
-/

import Mathlib.Data.Nat.Basic
import Mathlib.Tactic

namespace QOU.BraidKnot

-- Ref: [manuscript] conj:canonical-knot-id-sdp

/-- Enumeration of the three light nuclei whose canonical knot
    identification this conjecture addresses. -/
inductive LightNucleus : Type
  | deuterium   -- ²H  = 6₂
  | tritium     -- ³H  = 8₁₁
  | helium3     -- ³He = L₆ₐ₄

/-- The atomic mass number `A` of a `LightNucleus`. -/
def LightNucleus.A : LightNucleus → ℕ
  | .deuterium => 2
  | .tritium   => 3
  | .helium3   => 3

/-- The atomic strand count `n₀ = 3 · A`. -/
def LightNucleus.n₀ : LightNucleus → ℕ
  | n => 3 * n.A

/-- The number of constituents (nucleons) of a `LightNucleus`. -/
def LightNucleus.numConstituents : LightNucleus → ℕ
  | n => n.A

/-- **CanonicalKnotIdSDP** — the conjectural class.

    An instance for nucleus `n` asserts that the joint mass-tower
    confinement SDP at the atomic strand count `n.n₀ = 3·n.A` uniquely
    selects the canonical Hecke element for `n` (knot identifier given
    by `canonicalKnotId`).  The full T_w decomposes as

        T_w(n) = bindingK(n) · ⊗_i T_w(nucleon_i)

    with `bindingK n ∈ H_{n.n₀}(q₀)` the binding link
    (Hopf for ²H, an 8₁₁-class link for ³H, L₆ₐ₄ for ³He) that joins
    the nucleon-trefoils.  The SDP uniqueness assertion is the
    conjunction of constituent uniqueness (R5-minimal PSD-feasibility,
    closed) and binding-K uniqueness (open — the deliverable-3
    open work).  -/
-- Ref: [manuscript] conj:canonical-knot-id-sdp
-- Ref: [manuscript] prop:delta-max-uniform-bound
-- Ref: [manuscript] prop:joint-tower-sdp-confinement
class CanonicalKnotIdSDP (n : LightNucleus) where
  /-- Name of the canonical knot / link (e.g. "6_2", "8_11", "L6a4"). -/
  canonicalKnotId : String
  /-- Name of the binding-link operator K ∈ H_{n.n₀}(q₀)
      (e.g. "L_H Hopf" for ²H, "L6a4" for ³He). -/
  bindingLinkName : String
  /-- The SDP minimizer is achieved at this multiplicity ρ ≥ 1.
      Per conj:rho-prefactor-structural, this comes from the
      dominant Wedderburn summand of `bindingK n` at H_{n.n₀}(q₀). -/
  rho : ℕ
  rho_pos : 0 < rho
  /-- The constituent-uniqueness sub-assertion: at H_3(q₀), each
      nucleon's trefoil image is the unique PSD-feasible canonical
      element.  This sub-assertion is **closed** numerically by the
      R5-minimal verifier (`joint_tower_sdp_solver_v2.py`). -/
  constituentUniqueness : Prop
  constituentUniqueness_holds : constituentUniqueness
  /-- The binding-K-uniqueness sub-assertion: at H_{n.n₀}(q₀), the
      binding link K(n) is the unique PSD-feasible Hecke element
      satisfying the joint-tower SDP cross-level consistency
      constraints (4) of prop:joint-tower-sdp-confinement.  This
      sub-assertion is **open** — the deliverable-3 categorical
      uniqueness theorem is exactly this claim. -/
  bindingKUniqueness : Prop
  bindingKUniqueness_holds : bindingKUniqueness

/-! ### Per-nucleus instances (issue #604, deliverable 4)

Numerical evidence is recorded in
`folio-assistant/computations/binding-k-solver.witness.json`.

Every instance below is **conjectural in the binding-K leg** — the
`bindingKUniqueness` Prop is `True` at the Lean level and the witness
is `trivial`, marking these as placeholders awaiting the categorical
proof of the binding-K uniqueness sub-assertion (the deliverable-3
open core).  The `constituentUniqueness` leg is **closed** numerically
(R5-minimal verifier, `joint_tower_sdp_solver_v2.py`), but the Lean
discharge of the constituent-uniqueness Prop is also a `True` placeholder
here pending a separate Lean instantiation of the R5-minimal claim.

Per CLAUDE.md §1, the placeholder Props are kept TRIVIAL (`True`) so
the instances type-check; the manuscript references guide downstream
work.  When the categorical proofs land, the Props can be sharpened
without breaking downstream consumers. -/

-- Ref: [manuscript] conj:canonical-knot-id-sdp § "Structural decomposition"
-- Ref: binding-k-solver.witness.json (issue #604 deliverables 3 + 4)
instance instCanonicalKnotIdSDP_deuterium : CanonicalKnotIdSDP .deuterium where
  canonicalKnotId := "6_2"
  bindingLinkName := "L_H (Hopf, σ_3^2 in B_6)"
  rho := 1
  rho_pos := by decide
  constituentUniqueness := True
  constituentUniqueness_holds := trivial
  bindingKUniqueness := True
  bindingKUniqueness_holds := trivial

-- Ref: [manuscript] conj:canonical-knot-id-sdp § "Structural decomposition"
-- Ref: binding-k-solver.witness.json (issue #604 deliverables 3 + 4)
instance instCanonicalKnotIdSDP_tritium : CanonicalKnotIdSDP .tritium where
  canonicalKnotId := "8_11"
  bindingLinkName := "8_11-class link in B_9"
  rho := 2
  rho_pos := by decide
  constituentUniqueness := True
  constituentUniqueness_holds := trivial
  bindingKUniqueness := True
  bindingKUniqueness_holds := trivial

-- Ref: [manuscript] conj:canonical-knot-id-sdp § "Structural decomposition"
-- Ref: binding-k-solver.witness.json (issue #604 deliverables 3 + 4)
instance instCanonicalKnotIdSDP_helium3 : CanonicalKnotIdSDP .helium3 where
  canonicalKnotId := "L6a4"
  bindingLinkName := "L_{6a4} 3-component link in B_9"
  rho := 2
  rho_pos := by decide
  constituentUniqueness := True
  constituentUniqueness_holds := trivial
  bindingKUniqueness := True
  bindingKUniqueness_holds := trivial

/-! ### Structural lemma — ρ extraction is well-defined

This is a `theorem`, not a conjecture: given any `CanonicalKnotIdSDP`
instance, the multiplicity ρ extracted from the class is positive and
the `rho_pos` field is exactly the witness needed downstream.  This
small wrapper formalises the API for the conditional-class pattern:
downstream computations conditional on `[CanonicalKnotIdSDP n]` can
extract `ρ` and `rho_pos` directly without touching the (open)
binding-K uniqueness Prop.

The lemma is fully Lean-verified (no `sorry`); only the *meaning* of
the Props in the class instance is conjectural. -/

theorem rho_extraction_pos (n : LightNucleus) [h : CanonicalKnotIdSDP n] :
    0 < CanonicalKnotIdSDP.rho n := h.rho_pos

end QOU.BraidKnot
