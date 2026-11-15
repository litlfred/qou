import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# QOU.QBeta.StokesSymmetryConstant — `A_ω = 3` is a structure constant

The W3 probe (`qbeta_3bp8_w3_stokes_symmetry_constant.py`) certifies that
the GGM Stokes matrix of 4₁ satisfies, as an **exact integer q-series
identity** (all coefficients through q⁴⁰⁰, GGM 2012.00062 symmetry eq 65):

    S⁺₁₂(q) + S⁺₂₁(q) = 3 · S⁺₁₁(q),      det S⁺(q) = 1.

Three candidate readings of "the integer 3" of the T4/T5 chain coincide at
`q → 0` (where `S⁺(0) = [[1,3],[0,1]]`) and separate at the substrate:

  R1  raw entry           `S⁺₁₂`                → 1.5852 at q̃_sub
  R2  value-ratio         `S⁺₁₂ / S⁺₁₁`         → 3.7067 at q̃_sub
  R3  symmetry constant   `(S⁺₁₂ + S⁺₂₁)/S⁺₁₁`  → **exactly 3, at every q**

This file proves the two structural facts that make R3 the distinguished
reading, over an arbitrary field and an arbitrary index type (so nothing
depends on the specific series):

* `symmetryConstant_const` — if a family satisfies the symmetry with
  constant `c`, then its symmetry constant is `c` at **every** index. So
  q-independence of R3 is a *consequence of the symmetry*, not a numerical
  accident. (Empirically this shows up as truncation-invariance: R3 = 3
  already at a pre-asymptotic q-order 400 where R1 and R2 are meaningless.)
* `readings_coincide_at_base` — at a base point with `S₁₁ = 1`, `S₂₁ = 0`
  all three readings equal `S₁₂`. This is why the `q → 0` data of GGM
  eq (60) cannot distinguish them, and why the substrate evaluation was
  needed to separate them.
* `rawEntry_eq_symmetryConstant_iff` / `symmetryConstant_sub_valueRatio` —
  separation criteria: R1 equals R3 exactly when `S₁₂ + S₂₁ = S₁₂·S₁₁`, and
  R3 − R2 = `S₂₁/S₁₁`, so R2 and R3 agree iff the off-diagonal vanishes.
  Away from the base point the three are genuinely different objects.

**Scope.** Nothing here derives the number 3 from the categorical drivers —
that remains open (`qou-qnnq` lineage). What is established is that *if*
`A_ω` is the Stokes symmetry constant, then it is exact and q-independent,
so the corpus's constant `A_ω = 3` needs no substrate correction; and the
raw-entry reading is separately excluded by
`QOU.QBeta.ThetaRealityBound.thetaSq_nonneg_iff` (`A ≥ 2.054`).

-- Ref: [garoufalidis-gu-marino2021] GGM 2012.00062 (symmetry eq 65, eq 60)
-- Ref: [leitner2026] docs/audits/2026-08-01-3bp8-entirety-and-channel-correctness.md
-/

namespace QOU.QBeta.StokesSymmetryConstant

variable {R : Type*} [Field R] {ι : Type*}

/-- Reading R1: the raw `(1,2)` entry. -/
def rawEntry (S₁₂ : ι → R) (i : ι) : R := S₁₂ i

/-- Reading R2: the value-ratio `S₁₂ / S₁₁`. -/
def valueRatio (S₁₁ S₁₂ : ι → R) (i : ι) : R := S₁₂ i / S₁₁ i

/-- Reading R3: the symmetry constant `(S₁₂ + S₂₁) / S₁₁`. -/
def symmetryConstant (S₁₁ S₁₂ S₂₁ : ι → R) (i : ι) : R :=
  (S₁₂ i + S₂₁ i) / S₁₁ i

/-- **The symmetry constant is constant.** If a family satisfies
`S₁₂ + S₂₁ = c · S₁₁` pointwise with `S₁₁` nonvanishing, then its symmetry
constant equals `c` at every index — q-independence is forced by the
symmetry itself, not observed numerically. -/
theorem symmetryConstant_const {c : R} {S₁₁ S₁₂ S₂₁ : ι → R}
    (hsym : ∀ i, S₁₂ i + S₂₁ i = c * S₁₁ i) (hne : ∀ i, S₁₁ i ≠ 0) :
    ∀ i, symmetryConstant S₁₁ S₁₂ S₂₁ i = c := by
  intro i
  unfold symmetryConstant
  rw [hsym i, mul_div_assoc, div_self (hne i), mul_one]

/-- Two indices always agree on the symmetry constant — the invariance
statement in the form used by the audit ("nothing about it deforms"). -/
theorem symmetryConstant_eq_of_symmetry {c : R} {S₁₁ S₁₂ S₂₁ : ι → R}
    (hsym : ∀ i, S₁₂ i + S₂₁ i = c * S₁₁ i) (hne : ∀ i, S₁₁ i ≠ 0) (i j : ι) :
    symmetryConstant S₁₁ S₁₂ S₂₁ i = symmetryConstant S₁₁ S₁₂ S₂₁ j := by
  rw [symmetryConstant_const hsym hne i, symmetryConstant_const hsym hne j]

/-- **The `q → 0` degeneracy.** At a base point where `S₁₁ = 1` and
`S₂₁ = 0` — exactly GGM eq (60)'s `S⁺(0) = [[1,3],[0,1]]` — all three
readings collapse to `S₁₂`. Hence the `q → 0` data cannot distinguish
them, and the substrate evaluation is what separates the readings. -/
theorem readings_coincide_at_base {S₁₁ S₁₂ S₂₁ : ι → R} {i : ι}
    (h11 : S₁₁ i = 1) (h21 : S₂₁ i = 0) :
    rawEntry S₁₂ i = valueRatio S₁₁ S₁₂ i ∧
      valueRatio S₁₁ S₁₂ i = symmetryConstant S₁₁ S₁₂ S₂₁ i := by
  unfold rawEntry valueRatio symmetryConstant
  rw [h11, h21]
  simp

/-- **Separation criterion.** Away from the base point the raw entry and the
symmetry constant are the *same* number precisely when
`S₁₂ + S₂₁ = S₁₂ · S₁₁`; otherwise they are genuinely different objects.
(For the 4₁ substrate data the right side fails, and the two readings are
1.5852 vs 3.) -/
theorem rawEntry_eq_symmetryConstant_iff {S₁₁ S₁₂ S₂₁ : ι → R} {i : ι}
    (hne : S₁₁ i ≠ 0) :
    rawEntry S₁₂ i = symmetryConstant S₁₁ S₁₂ S₂₁ i ↔
      S₁₂ i + S₂₁ i = S₁₂ i * S₁₁ i := by
  unfold rawEntry symmetryConstant
  rw [eq_div_iff hne]
  exact ⟨fun h => h.symm, fun h => h.symm⟩

/-- The value-ratio and the symmetry constant differ by exactly
`S₂₁ / S₁₁` — so they agree iff the off-diagonal `S₂₁` vanishes. At the
4₁ substrate `S₂₁ = −0.3022 ≠ 0`, which is the whole gap between R2's
3.7067 and R3's exact 3. -/
theorem symmetryConstant_sub_valueRatio {S₁₁ S₁₂ S₂₁ : ι → R} {i : ι}
    (hne : S₁₁ i ≠ 0) :
    symmetryConstant S₁₁ S₁₂ S₂₁ i - valueRatio S₁₁ S₁₂ i = S₂₁ i / S₁₁ i := by
  unfold symmetryConstant valueRatio
  rw [div_sub_div_same]
  congr 1
  ring

end QOU.QBeta.StokesSymmetryConstant
