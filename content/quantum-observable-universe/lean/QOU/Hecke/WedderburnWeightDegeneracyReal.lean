/-
# QOU.Hecke.WedderburnWeightDegeneracyReal

The archimedean half of `QOU.Hecke.WedderburnWeightDegeneracy` — the statements
about signs and reachability, where the ordering on `ℝ` is genuinely used and
`§7c` therefore calls for `ℝ` rather than a generic `Field K`.

Bean `qou-vvv4`.  Companion probe:
`computations/hecke/h3_gram_degeneracy_is_wedderburn_weight_vanishing.py` (19/19).
-/
import QOU.Hecke.WedderburnWeightDegeneracy

namespace QOU.Hecke.WedderburnWeightDegeneracy

/-- **`z_D = −1/q` has no real solution at all**, since it forces
`q⁴ + q² + 1 = 0`.  Convention D never reaches the second root either. -/
theorem zD_ne_neg_inv (q : ℝ) (hq : q ≠ 0) : zD q ≠ -1 / q := by
  unfold zD
  intro h
  have h1 : (q ^ 2 + 1) ≠ 0 := by positivity
  rw [div_eq_div_iff h1 hq] at h
  have hpos : (0 : ℝ) < q ^ 4 + q ^ 2 + 1 := by positivity
  have hzero : q ^ 4 + q ^ 2 + 1 = 0 := by linear_combination h
  linarith

/-- **THE RESULT.  The `(2,1)` Wedderburn weight is strictly positive at the
canonical loop value, for every nonzero real `q`.**

`y_(2,1)(z_D) = q²/(q²+1)²` is a manifestly positive rational function, so the
block never degenerates: there is no convention-D analogue of the convention-C
hadronic melt at any real `q`.  A scope-(b) exclusion of the Wedderburn /
Gram-degeneracy route with the invariant exhibited — it says nothing about a
transition produced by some other mechanism. -/
theorem y21_at_zD_pos (q : ℝ) (hq : q ≠ 0) : 0 < y21 q (zD q) := by
  have h1 : (q ^ 2 + 1) ≠ 0 := by positivity
  have h2pos : (0 : ℝ) < q ^ 2 - q + 1 := by nlinarith [sq_nonneg (2 * q - 1)]
  have h3pos : (0 : ℝ) < q ^ 2 + q + 1 := by nlinarith [sq_nonneg (2 * q + 1)]
  rw [y21_at_zD q h1 h2pos.ne' h3pos.ne']
  have hq2 : (0 : ℝ) < q ^ 2 := by positivity
  positivity

/-- **The convention-C loop value never reaches 1**, for any `u > 0`: `z_C ≤ 1/2`.

The corpus (`qbeta-counit-closed-form.md`) says the trivial loop value "is never
attained on the substrate", which is a statement about `q_0`.  This is the
stronger fact: under convention C the Frobenius counit `ε = tr_M|_{z=1}` is
unreachable as a Markov trace at EVERY `q`, not merely at the anchor. -/
theorem zC_le_half (u : ℝ) (hu : 0 < u) : zC u ≤ 1 / 2 := by
  unfold zC
  rw [div_le_iff₀ (by positivity : (0 : ℝ) < u ^ 2 + 1)]
  nlinarith [sq_nonneg (u - 1)]

/-- Immediate corollary: `z_C = 1` has no positive solution. -/
theorem zC_ne_one (u : ℝ) (hu : 0 < u) : zC u ≠ 1 := by
  intro h
  have hle := zC_le_half u hu
  rw [h] at hle
  norm_num at hle

end QOU.Hecke.WedderburnWeightDegeneracy
