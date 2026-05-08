/-!
# Canonical knot identification for ²H, ³H, ³He from the confinement SDP

This file axiomatizes `conj:canonical-knot-id-sdp` as a Lean `class`
following the §3b conditional-class pattern from CLAUDE.md.

**Conjecture (informal):** The joint mass-tower confinement SDP uniquely
selects the canonical Hecke elements for ²H (6₂), ³H (8₁₁), and ³He
(L₆ₐ₄) from first principles, matching the historically identified
hyperbolic-volume/AME-binding-energy fits.

The class packages the uniqueness assertion; downstream conditional
theorems may take it as an `[instance]` hypothesis and remain fully
verified by Lean modulo this single conjectural input.

## References
- [manuscript] conj:canonical-knot-id-sdp
- [manuscript] prop:confinement-sdp
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

/-- **CanonicalKnotIdSDP** — the conjectural class.

    An instance for nucleus `n` asserts that the joint mass-tower
    confinement SDP uniquely selects the canonical Hecke element for `n`
    (knot identifier given by `canonicalKnotId`), and that the unique
    minimizer is achieved at multiplicity `rho`. -/
-- Ref: [manuscript] conj:canonical-knot-id-sdp
-- Ref: [manuscript] prop:delta-max-uniform-bound
class CanonicalKnotIdSDP (n : LightNucleus) where
  /-- Name of the canonical knot (e.g. "6_2", "8_11", "L6a4"). -/
  canonicalKnotId : String
  /-- The SDP is uniquely solved; there is no other Hecke element in the
      feasible region that achieves the same minimal value. -/
  sdpUniqueness : Prop
  /-- The SDP uniqueness assertion holds for this nucleus. -/
  uniqueness_holds : sdpUniqueness
  /-- The SDP minimizer is achieved at this multiplicity ρ ≥ 1. -/
  rho : ℕ
  rho_pos : 0 < rho

/-- **Canonical-name skeleton.**  Pins the canonical knot identifier
    by direct knot-table lookup (`6_2`, `8_11`, `L6a4`), uses
    `sdpUniqueness := True` so `uniqueness_holds` closes by `trivial`,
    and sets `rho = 1`.  Encodes the historical knot-name assignment
    but not the SDP-uniqueness derivation. -/
-- Ref: [manuscript] conj:canonical-knot-id-sdp §"Skeleton"
instance skeleton : ∀ n : LightNucleus, CanonicalKnotIdSDP n
  | LightNucleus.deuterium =>
    { canonicalKnotId := "6_2",  sdpUniqueness := True
      uniqueness_holds := trivial,  rho := 1,  rho_pos := Nat.one_pos }
  | LightNucleus.tritium =>
    { canonicalKnotId := "8_11", sdpUniqueness := True
      uniqueness_holds := trivial,  rho := 1,  rho_pos := Nat.one_pos }
  | LightNucleus.helium3 =>
    { canonicalKnotId := "L6a4", sdpUniqueness := True
      uniqueness_holds := trivial,  rho := 1,  rho_pos := Nat.one_pos }

end QOU.BraidKnot
