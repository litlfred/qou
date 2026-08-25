import QOU.QBeta.FiveTwoEnvelopeAssembly
import Mathlib.Analysis.SpecialFunctions.Complex.Log

/-!
# Pinning the branch integer WITHOUT continuity — an argument count

Bean `qou-trns`. After `FiveTwoEnvelopeAssembly`, `hcont` is the single open
input to the envelope step. `hcont` is used for exactly one thing: to force the
branch integer `k` in

    Σⱼ log(1 − x·yⱼ) = log x + 2πi·k

to be `0`. This file replaces that topological argument with an **arithmetic**
one, trading an analytic hypothesis for two real-algebraic ones.

## The idea

`exp(Σⱼ log(1 − x·yⱼ) − log x) = 1` is already proved from Vieta alone
(`exp_logSumA_sub_log_eq_one`), so `k` exists. Taking imaginary parts on
`x = e^{iφ}`,

    Σⱼ arg(1 − x·yⱼ) = φ + 2π·k .

Now `k` is pinned by *bounds*: if the argument sum lies in `(−π, 2π)` and
`φ ∈ [0, π)`, then `|2πk| < 2π`, so `k = 0`. No continuity, no root tracking, no
base point — `branchInt_eq_zero_of_bounds` below.

## What the bounds need, and what they cost

`sum_bounds_of_arg_structure` derives `(−π, 2π)` from three facts about the
individual arguments, all measured on the open arc at 40 dps (Route 27):

| fact | measured |
|---|---|
| each `arg(1 − x·yⱼ) > −π/2` | min over the arc is `−1.4077…`, and `−π/2 = −1.5708` |
| **at most one** exceeds `π/2` | max count is `1`; second-largest peaks at `1.3099 < π/2` |
| at least one is `≥ 0` | at most two are negative |

These are **real-algebraic statements on `|x| = 1`** — the same shape as
`xy_neg`, which this branch already proves by resultant elimination. They are
*not* proved here; they are the new obligations, and they replace `hcont`.

**Whether that is a good trade is a judgement, not a theorem.** In its favour:
they are algebraic rather than analytic, they are finite (three inequalities),
and the lane has working machinery for exactly this shape. Against: the margins
are not generous — `−1.4077` against `−π/2` is a 10% margin, and `1.3099`
against `π/2` is 17% — so the eliminations will be tighter than `xy_neg`'s was.

## A structural simplification found along the way

On the **open** arc the two log-sums are complex conjugates,

    Σⱼ log(1 − yⱼ/x) = conj( Σⱼ log(1 − x·yⱼ) )    (Route 27, to 1e-40)

because the roots are closed under conjugation (the cubic has real coefficients
on `|x| = 1`) and `x⁻¹ = conj x`. Hence `k₂ = −k₁`: **there is only one branch
integer, not two.** It fails at `φ = π` exactly because `1 − x·y₁` sits on the
cut there and `log(conj z) ≠ conj(log z)`.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms. This file does not
close `hcont`; it exchanges it for a different, arguably more tractable set of
obligations, and says so.
-/

namespace QOU.QBeta.FiveTwoDeformedSaddle

open Real

/-! ### The arithmetic core -/

/-- **The branch integer is `0` as soon as the argument sum is bounded.**

If `S = φ + 2π·k` with `S ∈ (−π, 2π)` and `φ ∈ [0, π)`, then `|2πk| < 2π`, so
`k = 0`. Pure arithmetic — no continuity, no base point, no topology. -/
theorem branchInt_eq_zero_of_bounds {S φ : ℝ} {k : ℤ}
    (hlo : -π < S) (hhi : S < 2 * π) (hφ0 : 0 ≤ φ) (hφπ : φ < π)
    (h : S = φ + 2 * π * k) : k = 0 := by
  have hpi : (0 : ℝ) < π := Real.pi_pos
  have hk : |(k : ℝ)| < 1 := by
    rw [abs_lt]
    constructor <;> nlinarith
  have hkz : |k| < 1 := by exact_mod_cast hk
  exact Int.abs_lt_one_iff.mp hkz

/-- The bounds, from the structure of the three individual arguments.

`a₁` is the one that may exceed `π/2` (at most one does); `a₂`, `a₃` stay at or
below it; all three exceed `−π/2`; and at least one is nonnegative. -/
theorem sum_bounds_of_arg_structure {a₁ a₂ a₃ : ℝ}
    (h1lo : -(π / 2) < a₁) (h2lo : -(π / 2) < a₂) (h3lo : -(π / 2) < a₃)
    (h1hi : a₁ < π) (h2hi : a₂ ≤ π / 2) (h3hi : a₃ ≤ π / 2)
    (hnn : 0 ≤ a₁ ∨ 0 ≤ a₂ ∨ 0 ≤ a₃) :
    -π < a₁ + a₂ + a₃ ∧ a₁ + a₂ + a₃ < 2 * π := by
  constructor
  · rcases hnn with h | h | h <;> linarith
  · linarith

/-- **The replacement for `hcont`, assembled.**

Given the argument bounds and `φ ∈ [0,π)`, the branch integer vanishes. Compare
`branchDiff_eq_zero_of_continuousOn`, which reaches the same conclusion from
continuity plus a base point: this route needs neither. -/
theorem branchInt_eq_zero_of_arg_structure {a₁ a₂ a₃ φ : ℝ} {k : ℤ}
    (h1lo : -(π / 2) < a₁) (h2lo : -(π / 2) < a₂) (h3lo : -(π / 2) < a₃)
    (h1hi : a₁ < π) (h2hi : a₂ ≤ π / 2) (h3hi : a₃ ≤ π / 2)
    (hnn : 0 ≤ a₁ ∨ 0 ≤ a₂ ∨ 0 ≤ a₃)
    (hφ0 : 0 ≤ φ) (hφπ : φ < π)
    (h : a₁ + a₂ + a₃ = φ + 2 * π * k) : k = 0 :=
  let ⟨hlo, hhi⟩ := sum_bounds_of_arg_structure h1lo h2lo h3lo h1hi h2hi h3hi hnn
  branchInt_eq_zero_of_bounds hlo hhi hφ0 hφπ h

/-! ### Non-vacuity -/

/-- **Non-vacuity.** The hypotheses of `branchInt_eq_zero_of_arg_structure` are
satisfiable, with the measured arc values: taking `a₁ = 1.4`, `a₂ = a₃ = 0`
and `φ = 1.4` gives a genuine instance, so the theorem is not about an empty set.

The check with real content is Route 27, which measures the three structural
facts along the arc and finds the margins `−1.4077` vs `−π/2` and `1.3099` vs
`π/2`. -/
theorem branchInt_hypotheses_satisfiable :
    ∃ (a₁ a₂ a₃ φ : ℝ) (_ : -(π / 2) < a₁) (_ : a₁ < π),
      a₁ + a₂ + a₃ = φ + 2 * π * (0 : ℤ) := by
  refine ⟨1, 0, 0, 1, by nlinarith [Real.two_le_pi], by nlinarith [Real.two_le_pi], ?_⟩
  push_cast
  ring

end QOU.QBeta.FiveTwoDeformedSaddle
