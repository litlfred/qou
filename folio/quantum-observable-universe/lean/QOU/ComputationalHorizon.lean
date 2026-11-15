import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# QOU.ComputationalHorizon

**Canonical declaration** for content block at
[`quantum-observable-universe/information-theory/computational-horizon.ts`](quantum-observable-universe/information-theory/computational-horizon.ts).

Formalises the manuscript **definition** of a computational horizon for the
braid closure `L = β̂` of a computation with `c = 3N` crossings (`N` Toffoli
gates): the Skein resolution tree has `3^c` leaves, and bandwidth saturation
forces the time bound `t ≥ (c·log 3 / 𝔅(q))·3^{c−c₀}` (§7c: archimedean over
`ℝ` — `log`, `rpow`).
-/

namespace QOU

/-- Data for a computational horizon of `L = β̂`.

    A `definition` carrier: `N` Toffoli gates give `c = 3N` crossings; the
    resolution tree has `numLeaves = 3^c` leaves; the information bandwidth
    `bandwidth = 𝔅(q) > 0` bounds the sampling rate; and `minTime` is pinned
    to the bandwidth-saturation lower bound. -/
structure ComputationalHorizon where
  /-- Number of Toffoli gates `N`. -/
  N : ℕ
  /-- Number of crossings `c`. -/
  c : ℕ
  /-- `c = 3N`. -/
  c_eq : c = 3 * N
  /-- Number of leaves of the Skein resolution tree. -/
  numLeaves : ℕ
  /-- The resolution tree has `3^c` leaves — one per discrete history. -/
  numLeaves_eq : numLeaves = 3 ^ c
  /-- Information bandwidth `𝔅(q)` per Planck time. -/
  bandwidth : ℝ
  /-- Bandwidth is strictly positive. -/
  bandwidth_pos : 0 < bandwidth
  /-- Reference crossing count `c₀` in the exponent. -/
  c0 : ℝ
  /-- Minimum Planck-step time to extract the degree-0 answer. -/
  minTime : ℝ
  /-- Bandwidth-saturation bound: `t ≥ (c·log 3 / 𝔅(q))·3^{c−c₀}`. -/
  minTime_eq :
    minTime = (c * Real.log 3 / bandwidth) * (3 : ℝ) ^ ((c : ℝ) - c0)

-- Ref: [leitner2026] quantum-observable-universe/information-theory/computational-horizon.ts

/-- The saturation time is non-negative (it is `0` only in the degenerate
    `c = 0` case). -/
theorem minTime_nonneg (H : ComputationalHorizon) :
    0 ≤ H.minTime := by
  rw [H.minTime_eq]
  have hlog : 0 ≤ Real.log 3 := Real.log_nonneg (by norm_num)
  have hpow : 0 < (3 : ℝ) ^ ((H.c : ℝ) - H.c0) := Real.rpow_pos_of_pos (by norm_num) _
  have hfrac : 0 ≤ (H.c : ℝ) * Real.log 3 / H.bandwidth :=
    div_nonneg (mul_nonneg (Nat.cast_nonneg _) hlog) H.bandwidth_pos.le
  exact mul_nonneg hfrac hpow.le

/-- The leaf count is a power of three, hence positive: the resolution tree is
    never empty. -/
theorem numLeaves_pos (H : ComputationalHorizon) :
    0 < H.numLeaves := by
  rw [H.numLeaves_eq]; positivity

end QOU
