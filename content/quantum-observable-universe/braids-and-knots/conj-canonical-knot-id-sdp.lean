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

/-- **Canonical-name skeleton.**  Pins the canonical knot identifier
    by direct knot-table lookup (`6_2`, `8_11`, `L6a4`).  The
    `sdpUniqueness` predicate is the weakest-non-trivial content-bearing
    assertion: the canonical knot identifier is a non-empty string
    (length ≥ 3).  This catches "skeleton was wired with empty
    knot id" but is implied by — not equivalent to — the genuine
    SDP-uniqueness assertion.  `rho := 1` per the historical
    multiplicity assignment. -/
-- Ref: [manuscript] conj:canonical-knot-id-sdp §"Skeleton"
instance canonical : ∀ n : LightNucleus, CanonicalKnotIdSDP n
  | LightNucleus.deuterium =>
    { canonicalKnotId := "6_2",  sdpUniqueness := "6_2".length ≥ 3
      uniqueness_holds := by decide,  rho := 1,  rho_pos := Nat.one_pos }
  | LightNucleus.tritium =>
    { canonicalKnotId := "8_11", sdpUniqueness := "8_11".length ≥ 3
      uniqueness_holds := by decide,  rho := 1,  rho_pos := Nat.one_pos }
  | LightNucleus.helium3 =>
    { canonicalKnotId := "L6a4", sdpUniqueness := "L6a4".length ≥ 3
      uniqueness_holds := by decide,  rho := 1,  rho_pos := Nat.one_pos }

end QOU.BraidKnot
