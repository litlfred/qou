/-
# Bar symmetry does not pin the averaging weight

The p-n interface is built as a convex combination of the two like-species
crossings, `f_pn = w·b_pp + (1-w)·b_nn`, and the corpus takes `w = 1/2 + δ/4`
(`bring_color_weighted`). The stated justification for the `1/2` is bar
invariance: `σ_avg = (σ + σ⁻¹)/2` is the bar-symmetric projection
(`prop:averaging-resonance-rule`). `QOU/Hecke/SymmetrySignAmGm.lean` then shows
that choice is what makes the symmetry energy come out with the wrong sign.

**This file shows bar invariance does not force `1/2`.** Under `q ↦ 1/q` the
bracket `[2]_q` is fixed while `b_pp = q²/[2]_q` and `b_nn = q⁻²/[2]_q` swap, so
invariance of `f_pn` requires

```
(1 - w̄ - w)·(b_pp - b_nn) = 0        i.e.        w̄ = 1 - w
```

for `q ≠ 1`. That is **one equation, not a determination**, and the family

```
w_k = q^{-k} / [2]_{q^k}          [2]_x := x + 1/x
```

satisfies it for every `k` (`bar_weight_bar_eq_one_sub`). The corpus's `1/2` is
the `k = 0` member and nothing selects it except the unstated extra assumption
that `w` carries no `q` — an undeformed bracket inside a deformed algebra.

## Where the sign lives on that family

`weight_strictAnti` gives `w_k` strictly decreasing in `k` for `q > 1`, and
`weight_one` identifies `w_1 = 1/(q²+1)`, which
`SymmetrySignAmGm.crossing_weight` shows lands exactly on the geometric mean.
Chaining those two with `SymmetrySignAmGm.delta_nonpos_iff` places every `k > 1`
strictly below the geometric mean — the SEMF side:

| `k` | `w_k` at `q₀` | `δ` | |
|---|---:|---:|---|
| **0** | **0.5** | **−0.0216177** | wrong — the corpus |
| 1 | 0.448018 | `0` | neutral: the geometric mean |
| 2 | 0.397148 | +0.0216177 | the SEMF sign |

`δ(w_k)` vanishes at exactly `k = 1` and is odd about it, measured in
`computations/qbeta/qbeta_bar_weight_family_probe.py`.

## What is derived here, and what is NOT

Derived: the invariance condition `w̄ = 1 - w`; that the family satisfies it for
all `k`; the monotonicity; and hence the **bound** `δ > 0 ⟺ k > 1`.

**Not derived: `k`.** `k = 2` gives the SEMF sign and is deliberately NOT adopted
on that basis — it is a target to check a future derivation against, never a
criterion to search on. The one member with an independent argument is `k = 1`,
which uses the framework's own bracket `[2]_q` and returns the loop value
`1/[2]_q` — and it gives **zero** symmetry term, not the SEMF one. Reported
rather than skipped past.

Bean `qou-79wa`; the open half of `qou-i01a`.
-/

import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

namespace QOU.Hecke.BarWeightFamily

/-- The bar-symmetric weight family, `w_k = q^{-k}/(q^k + q^{-k})`. At `k = 0`
this is `1/2`, the corpus's averaging rule. -/
noncomputable def w (q k : ℝ) : ℝ := q ^ (-k) / (q ^ k + q ^ (-k))

/-- Its image under the bar involution `q ↦ 1/q`, written out. -/
noncomputable def wbar (q k : ℝ) : ℝ := q ^ k / (q ^ k + q ^ (-k))

/-- **Every member of the family is bar-invariant.** Bar invariance of the
interface `w·b_pp + (1-w)·b_nn` requires exactly `w̄ = 1 - w`, and that holds for
the whole family — so the condition constrains one degree of freedom and leaves
`k` free. -/
theorem bar_weight_bar_eq_one_sub {q : ℝ} (hq : 0 < q) (k : ℝ) :
    wbar q k = 1 - w q k := by
  have h1 : (0 : ℝ) < q ^ k := Real.rpow_pos_of_pos hq k
  have h2 : (0 : ℝ) < q ^ (-k) := Real.rpow_pos_of_pos hq (-k)
  have hs : q ^ k + q ^ (-k) ≠ 0 := by positivity
  simp only [w, wbar]
  field_simp
  ring

/-- `w_0 = 1/2`: the corpus's averaging rule is the undeformed member. -/
theorem weight_zero : ∀ q : ℝ, 0 < q → w q 0 = 1 / 2 := by
  intro q hq
  have : q ^ (0 : ℝ) = 1 := Real.rpow_zero q
  simp [w, this]
  norm_num

/-- `w_1 = 1/(q²+1)`, which `SymmetrySignAmGm.crossing_weight` shows is exactly
the weight landing on the geometric mean `1/[2]_q`. -/
theorem weight_one {q : ℝ} (hq : 0 < q) : w q 1 = 1 / (q ^ 2 + 1) := by
  have h1 : q ^ (1 : ℝ) = q := Real.rpow_one q
  have h2 : q ^ (-1 : ℝ) = q⁻¹ := by
    rw [Real.rpow_neg_one]
  have hq0 : q ≠ 0 := ne_of_gt hq
  have : q + q⁻¹ ≠ 0 := by positivity
  rw [w, h1, h2]
  field_simp

/-- **`w_k` is strictly decreasing in `k`** for `q > 1`, so the family sweeps
monotonically from `1/2` downward. With `weight_one` this places every `k > 1`
strictly below the crossing — the region `SymmetrySignAmGm.delta_nonpos_iff`
identifies as the SEMF sign. -/
theorem weight_strictAnti {q : ℝ} (hq : 1 < q) {k l : ℝ} (hkl : k < l) :
    w q l < w q k := by
  have hq0 : (0 : ℝ) < q := by linarith
  have key : ∀ m : ℝ, w q m = 1 / (q ^ (2 * m) + 1) := by
    intro m
    have hm : (0 : ℝ) < q ^ m := Real.rpow_pos_of_pos hq0 m
    have hnm : (0 : ℝ) < q ^ (-m) := Real.rpow_pos_of_pos hq0 (-m)
    have hprod : q ^ (2 * m) = q ^ m * q ^ m := by
      rw [← Real.rpow_add hq0]; ring_nf
    have hinv : q ^ (-m) = (q ^ m)⁻¹ := by
      rw [Real.rpow_neg hq0.le]
    have hs : q ^ m + q ^ (-m) ≠ 0 := by positivity
    rw [w, hinv, hprod]
    field_simp
  rw [key k, key l]
  have hmono : q ^ (2 * k) < q ^ (2 * l) :=
    Real.rpow_lt_rpow_left_iff hq |>.mpr (by linarith)
  have h1 : (0 : ℝ) < q ^ (2 * k) + 1 := by positivity
  have h2 : (0 : ℝ) < q ^ (2 * l) + 1 := by positivity
  exact div_lt_div_of_pos_left one_pos h1 (by linarith)

end QOU.Hecke.BarWeightFamily
