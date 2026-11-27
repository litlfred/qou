import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp

/-!
# QOU.BringsSurface.OhtsukiKappaFormal — the 4₁ Ohtsuki tail coefficients as ring symbols

Bean `qou-gfsr` (item 5 of epic `qou-dk7p`). Owner ruling 2026-11-27: a
transcendental quantity appears outside `QOU/Transcendental/` only as a symbol
in a ring, together with its cut. Here `π` is a symbol `p` and `√3` is a symbol
`s` constrained by `s² = 3`. The 4₁ Ohtsuki tail coefficients are

    κ₁(s, p) = 11·s·p / 108,      κ₂(p) = 2·p² / 27,

and their rational dependence `288 κ₁² = 121 κ₂` uses nothing about `π` or `√3`
beyond `s² = 3`. Positivity needs only `0 < s` and `0 < p` in an ordered field.
The instantiation `s = √3`, `p = π` in `ℝ` is
`QOU.Transcendental.BringsSurface.OhtsukiKappaDependence`.

No empirical value enters this file.
-/

namespace QOU.AlgebraicSubstrate

/-- **The relation is formal.** For any `s` with `s² = 3` and any `p`, the pair
`(11sp/108, 2p²/27)` satisfies a rational relation, stated denominator-cleared
so it holds over any commutative ring. -/
theorem kappa_relation_formal {R : Type*} [CommRing R] (s p : R) (hs : s ^ 2 = 3) :
    288 * (11 * s * p) ^ 2 * 27 = 121 * (2 * p ^ 2) * 108 ^ 2 := by
  linear_combination (940896 * p ^ 2) * hs

variable {K : Type*} [Field K]

/-- `κ₁` of `4₁` as a ring symbol: `11·s·p/108`. -/
def kappa1Sym (s p : K) : K := 11 * s * p / 108

/-- `κ₂` of `4₁` as a ring symbol: `2·p²/27`. -/
def kappa2Sym (p : K) : K := 2 * p ^ 2 / 27

/-- **`288·κ₁² = 121·κ₂`** in any field of characteristic zero where `s² = 3`. -/
theorem kappaSym_relation [CharZero K] (s p : K) (hs : s ^ 2 = 3) :
    288 * kappa1Sym s p ^ 2 = 121 * kappa2Sym p := by
  unfold kappa1Sym kappa2Sym
  field_simp
  linear_combination (940896 * p ^ 2) * hs

/-- Both symbols are positive when `s, p > 0` in an ordered field. -/
theorem kappa1Sym_pos [LinearOrder K] [IsStrictOrderedRing K] {s p : K}
    (hs : 0 < s) (hp : 0 < p) : 0 < kappa1Sym s p := by
  unfold kappa1Sym; positivity

theorem kappa2Sym_pos [LinearOrder K] [IsStrictOrderedRing K] {p : K}
    (hp : 0 < p) : 0 < kappa2Sym p := by
  unfold kappa2Sym; positivity

end QOU.AlgebraicSubstrate
