import QOU.QBeta.StokesQZeroDTCount
import QOU.QBeta.StokesSymmetryConstant

/-!
# QOU.QBeta.StokesSymmetryConstantQZero — the symmetry constant reads exactly `3` at q→0

This brick **connects** the two existing sorry-free G3-keystone bricks that were
previously unlinked:

* `QOU.QBeta.StokesQZeroDTCount` — the *concrete* q→0 Stokes matrix
  `S⁺(0) = [[1,3],[0,1]]`, obtained as `−½·(A·W₋₁(0)·B·W₋₁(0)ᵀ·C)` by decidable
  integer arithmetic (GGM eq 60; certified from `W₋₁(0)`).
* `QOU.QBeta.StokesSymmetryConstant` — the *abstract* conditional lemma
  `symmetryConstant_const`: **if** a Stokes family satisfies the GGM symmetry
  `S₁₂ + S₂₁ = c·S₁₁` (eq 65), **then** its symmetry-constant reading
  `(S₁₂+S₂₁)/S₁₁` equals `c` at every index — q-independence *forced* by the
  symmetry, not observed.

The point of the connection — and the **sharpening of the internal-derivation
target** it records — is this. The corpus's `A_ω` is the *symmetry-constant*
reading R3 (`3bp8` §4: reality-excluded R1, truncation-invariant R3), and by
`symmetryConstant_const` that reading is **q-independent**. A q-independent
quantity equals its own q→0 limit. So the certified concrete matrix `S⁺(0)`
already carries the *entire* value of the symmetry constant, and this file
machine-checks that it reads exactly **3**:

* `eq65_holds_qzero` — the GGM symmetry (eq 65) `S⁺₁₂(0) + S⁺₂₁(0) = 3·S⁺₁₁(0)`
  holds at q→0 with constant exactly `3` (`3 + 0 = 3·1`), decidable over ℤ from
  `StokesQZeroDTCount.Splus0`.
* `det_qzero` — `det S⁺(0) = 1` (the second GGM identity, eq 65), decidable.
* `symmetry_reading_qzero` — discharging the abstract `symmetryConstant_const`
  hypothesis at the base point with the *concrete* `Splus0` entries (over ℚ),
  the symmetry-constant reading of `S⁺(0)` equals `3`.

## Scope (STRICT — honest, anti-laundering)

**This is NOT an internal derivation of the integer `3`.** It links two already
sorry-free objects and records that, *because* the symmetry constant is
q-independent (`StokesSymmetryConstant.symmetryConstant_const`), the physics
target collapses onto the **decidable q→0** matrix — i.e. deriving `A_ω = 3`
internally does **not** require the resurgent tail; it requires deriving the
single q→0 datum `S⁺(0)₁₂ = 3` (equivalently `W₋₁(0)`) from the QOU categorical
drivers. That derivation is **open** (`qou-qnnq`); the `3` here still originates
in the GGM/DGG q→0 evaluation (`StokesQZeroDTCount`), not in a Hecke / Wedderburn
/ Bring construction. Nothing is fitted, axiomatized, or wired.

The full DT/Stokes *spectrum* of `T[4₁]` is the pair `{3,4}` (GGM eq 98); the
symmetry constant `3` is a **narrower** object than that spectrum (the eq-65
structure constant, not a spectrum entry). The `3`-from-`disc(ℚ(√−3))=−3`
shortcut was refuted precisely because it targeted the spectrum and a `4`
co-occurs (`2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md`);
whether the *symmetry-constant* target admits a genuine internal formula
surviving the cross-knot test is the open question this file sharpens — it is
**not** resolved here and must not be asserted (`5₂`'s block is `3×3`, different
symmetry structure).

-- Ref: [garoufalidis-gu-marino2021] GGM 2012.00062 (symmetry eq 65, eq 60)
-- Ref: [leitner2026] docs/audits/2026-08-02-aomega-internal-derivation-symmetry-constant-target.md
-/

namespace QOU.QBeta.StokesSymmetryConstantQZero

open QOU.QBeta.StokesQZeroDTCount

/-- **GGM symmetry (eq 65) at q→0.** For the certified `S⁺(0) = [[1,3],[0,1]]`,
`S⁺₁₂ + S⁺₂₁ = 3·S⁺₁₁` holds with structure constant exactly `3` (`3 + 0 = 3·1`).
Decidable integer arithmetic on `StokesQZeroDTCount.Splus0`. -/
theorem eq65_holds_qzero : Splus0 0 1 + Splus0 1 0 = 3 * Splus0 0 0 := by decide

/-- **The second GGM identity (eq 65) at q→0.** `det S⁺(0) = 1`. Decidable. -/
theorem det_qzero : det Splus0 = 1 := by decide

/-- **The symmetry-constant reading of `S⁺(0)` is `3`.** Discharging the abstract
`StokesSymmetryConstant.symmetryConstant_const` hypothesis at the base point with
the concrete (cast-to-ℚ) `Splus0` entries: the reading `(S⁺₁₂+S⁺₂₁)/S⁺₁₁` equals
`3`. Because that reading is q-independent (the abstract lemma), this base value
is its value at *every* q — the entire symmetry constant is carried by the
decidable q→0 matrix. Not an internal derivation of `3`; see the file scope. -/
theorem symmetry_reading_qzero :
    StokesSymmetryConstant.symmetryConstant
      (fun _ : Unit => (Splus0 0 0 : ℚ))
      (fun _ : Unit => (Splus0 0 1 : ℚ))
      (fun _ : Unit => (Splus0 1 0 : ℚ)) () = 3 := by
  have hsym : ∀ _ : Unit,
      (Splus0 0 1 : ℚ) + (Splus0 1 0 : ℚ) = 3 * (Splus0 0 0 : ℚ) := by
    intro _
    have h : Splus0 0 1 + Splus0 1 0 = 3 * Splus0 0 0 := eq65_holds_qzero
    exact_mod_cast h
  have hne : ∀ _ : Unit, (Splus0 0 0 : ℚ) ≠ 0 := by
    intro _
    have h : Splus0 0 0 = 1 := by decide
    rw [h]; norm_num
  exact StokesSymmetryConstant.symmetryConstant_const hsym hne ()

/-- **Trace of the concrete `q → 0` matrix `Splus0` is `2` (`1 + 1 = 2`).** -/
theorem trace_qzero : Splus0 0 0 + Splus0 1 1 = 2 := by decide

/-- **Upper-triangular unipotent structure of `Splus0`**: the lower-left entry
vanishes and `(S₀₀ − 1)(S₁₁ − 1) − S₀₁ S₁₀ = 0`. -/
theorem unipotent_characteristic_qzero :
    Splus0 1 0 = 0 ∧
      (Splus0 0 0 - 1) * (Splus0 1 1 - 1) - Splus0 0 1 * Splus0 1 0 = 0 := by
  decide

/-- **Off-diagonal square vs determinant relation at `q → 0`**:
`(S₀₁ + S₁₀)² = 9 · det Splus0`. -/
theorem off_diag_sum_sq_eq_nine_det_qzero :
    (Splus0 0 1 + Splus0 1 0) ^ 2 = 9 * det Splus0 := by
  decide

end QOU.QBeta.StokesSymmetryConstantQZero
