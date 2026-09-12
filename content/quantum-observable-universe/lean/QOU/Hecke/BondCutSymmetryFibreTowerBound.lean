/-
# What a bounded fibre tower can move, and it is not enough

Archimedean specialisation (§7c) of `QOU/Hecke/BondCutSymmetryFibreTower.lean`.
The generic file proves that a fibre-level bond count renders to a bond count
(`bondSum_map`), that every order of the tower is separately a bond count
(`bondSum_tower`, `energySlope_tower`), and that the convexity of the interface
is a ring identity insensitive to the Markov parameter and to the deformation
(`interface_affine`). Those are statements about *form*. This file is the
quantitative half: given the form, how far can the tower move the one number the
form leaves free?

## The bridge

`interface_affine` in the `w = 1 - u` letters is exactly
`BondCutSymmetryLogBound.interface` (`interface_eq_letterTrace`), so the cap
`energySlope_convex_le_two_log` applies to the corpus's interface with the
flavour split as its only input (`flavour_interface_le_two_log`): for every
rendered `δ_f ∈ [-2, 2]`,

```
δ  ≤  2 ln q          (= 0.2087 at the proton q₀)
```

whatever the tower does to `z` and to `h`. The measured `δ_f` is `≈ 1.4e-3`, so
the hypothesis holds with three orders of magnitude of slack, and
`FibreTower.flavour_factor_to_leave_hull` prices the alternative.

## The tail bound

Suppose instead the tower is allowed to move `δ` directly: `δ = δ^{(0)} +
Σ_{k≥1} h^k δ^{(k)}` in an expansion parameter `h`, which at the substrate is
`ℏ_q = (q-1)/q ≈ 0.0991`. If the coefficients are bounded by `C` then

```
|Σ_{k≥1} h^k δ^{(k)}|  ≤  C·h/(1-h)          (`tower_partial_abs_le`)
```

at **every** truncation order, which is the honest form: a truncation is what
any computation has, and the bound does not depend on which one.

Read backwards (`tower_coefficient_lower_bound`) that is a lower bound on the
coefficients a tower would need. The SEMF symmetry energy wants
`δ* = 4·a_A/(E₀·k) ≈ 1.869` on a degree-`12` well-mixed graph; the corpus sits
at `δ ≈ -0.0218`; so the tower would need

```
C  ≥  (δ* - δ)·(1-h)/h  ≈  1.890 · 0.9009 / 0.0991  ≈  17.2
```

against an order-zero slope of `0.0218` and an order-zero *cap* of `0.2087`.
The required coefficient is **82 times the cap on the leading term**. A series
whose coefficients exceed its leading term by two orders of magnitude is not a
correction to that term; it is a different leading term, and `h`-convergence is
the least of what it gives up. `bounded_tower_lt_target` states the conclusion
in the direction that decides it: for every truncation, a bounded tower stays
strictly below the target.

## What is proved and what is hypothesis

Everything below is proved over `ℝ`, because `Real.log` is an archimedean
construct. No nuclear datum and no substrate constant appears in any statement:
`a_A`, `E₀`, `q₀`, `ℏ_q` and `δ_f` enter the file only through this docstring
and through the producer, and every theorem is universally quantified over the
quantities they name. The numbers above are measured in
`computations/qbeta/qbeta_class_d_fibre_tower_probe.py` and are targets checked
against, never search directions (AGENTS.md §NO FITTING).

Bean `qou-brng`.
-/

import QOU.Hecke.BondCutSymmetryLogBound
import QOU.Hecke.BondCutSymmetryFibreTower

namespace QOU.Hecke.BondCutSymmetryFibreTowerBound

open QOU.Hecke.BondCutSymmetry
open QOU.Hecke.BondCutSymmetryLogBound
open QOU.Hecke.BondCutSymmetryFibreTower

section Bridge

/-- **The affine-offset identity IS the `interface` of the log-bound file.**
With `b_pp = tr(σ) = z` and `b_nn = tr(σ - h) = z - h`, the interface letter
`σ - h(1 - w)` traces to `interface b_pp b_nn w`. So the `δ ≤ 2 ln q` cap's
convexity hypothesis is supplied by a ring identity rather than by a numerical
check at `q₀`, and is therefore untouched by any order of any fibre-level
expansion of `z` or of `h`. -/
theorem interface_eq_letterTrace (z h w : ℝ) :
    interface (letterTrace z 0) (letterTrace z (-h)) w
      = letterTrace z (-(h * (1 - w))) := by
  unfold interface letterTrace
  ring

/-- **The cap, with the flavour split as its only input.** For the corpus's
letters the log-bound's convex weight is `w = 1 - u = 1/2 + δ_f/4`, so the whole
`δ ≤ 2 ln q` bound reduces to `-2 ≤ δ_f ≤ 2`: one two-sided bound on one
rendered scalar, with every other ingredient of the tower already absorbed by
`FibreTower.interface_affine`. -/
theorem flavour_interface_le_two_log {q df : ℝ} (hq : 1 ≤ q)
    (h0 : -2 ≤ df) (h2 : df ≤ 2) :
    energySlope (-Real.log (q ^ 2 / (q + 1 / q)))
        (-Real.log (interface (q ^ 2 / (q + 1 / q)) ((q ^ 2)⁻¹ / (q + 1 / q))
          (1 - offsetRatio df)))
        (-Real.log ((q ^ 2)⁻¹ / (q + 1 / q)))
      ≤ 2 * Real.log q := by
  have hu := offsetRatio_mem_iff.mpr ⟨h0, h2⟩
  exact energySlope_convex_le_two_log hq (by linarith [hu.2]) (by linarith [hu.1])

end Bridge

section Tail

/-- The partial geometric sum, in the form that needs no division. -/
theorem geom_partial_eq (h : ℝ) (n : ℕ) :
    (1 - h) * ∑ k ∈ Finset.range n, h ^ k = 1 - h ^ n := by
  induction n with
  | zero => simp
  | succ n ih =>
      rw [Finset.sum_range_succ, mul_add, ih, pow_succ]
      ring

/-- Every partial geometric sum is below the full one. -/
theorem geom_partial_le {h : ℝ} (h0 : 0 ≤ h) (h1 : h < 1) (n : ℕ) :
    ∑ k ∈ Finset.range n, h ^ k ≤ (1 - h)⁻¹ := by
  have hpos : (0 : ℝ) < 1 - h := by linarith
  have hn : (0 : ℝ) ≤ h ^ n := pow_nonneg h0 n
  have heq := geom_partial_eq h n
  rw [inv_eq_one_div, le_div_iff₀ hpos, mul_comm]
  linarith

/-- **A tower with bounded coefficients moves its quantity by at most
`C·h/(1-h)`, at every truncation order.** The counting is one-sided in the
direction that decides the question — the claim under test is that higher orders
make `δ` *bigger* — and the bound is uniform in `n`, so no truncation choice
evades it and no convergence question arises. -/
theorem tower_partial_abs_le {h C : ℝ} (h0 : 0 ≤ h) (h1 : h < 1) {a : ℕ → ℝ}
    (ha : ∀ k, |a k| ≤ C) (n : ℕ) :
    |∑ k ∈ Finset.range n, h ^ (k + 1) * a k| ≤ C * h * (1 - h)⁻¹ := by
  have hC : 0 ≤ C := le_trans (abs_nonneg (a 0)) (ha 0)
  calc |∑ k ∈ Finset.range n, h ^ (k + 1) * a k|
      ≤ ∑ k ∈ Finset.range n, |h ^ (k + 1) * a k| :=
        Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ k ∈ Finset.range n, h ^ (k + 1) * C := by
        refine Finset.sum_le_sum ?_
        intro k _
        rw [abs_mul, abs_of_nonneg (pow_nonneg h0 (k + 1))]
        exact mul_le_mul_of_nonneg_left (ha k) (pow_nonneg h0 (k + 1))
    _ = C * h * ∑ k ∈ Finset.range n, h ^ k := by
        rw [Finset.mul_sum]
        refine Finset.sum_congr rfl ?_
        intro k _
        rw [pow_succ]
        ring
    _ ≤ C * h * (1 - h)⁻¹ :=
        mul_le_mul_of_nonneg_left (geom_partial_le h0 h1 n) (mul_nonneg hC h0)

/-- **Read backwards: the coefficient a tower would need.** If the whole tower
is to carry the quantity from `base` to `target`, its coefficient bound is at
least `(target - base)·(1-h)/h`. At the substrate `h = ℏ_q ≈ 0.0991`, closing
`δ: -0.0218 → 1.869` needs `C ≥ 17.2` — two orders of magnitude above the
order-zero slope, and 82 times the order-zero cap `2 ln q₀ = 0.2087`. -/
theorem tower_coefficient_lower_bound {h C base target : ℝ}
    (h0 : 0 < h) (h1 : h < 1)
    (hreach : target - base ≤ C * h * (1 - h)⁻¹) :
    (target - base) * (1 - h) / h ≤ C := by
  have hpos : (0 : ℝ) < 1 - h := by linarith
  have hfac : (0 : ℝ) ≤ (1 - h) / h := div_nonneg hpos.le h0.le
  have hid : C * h * (1 - h)⁻¹ * ((1 - h) / h) = C := by
    field_simp
  calc (target - base) * (1 - h) / h = (target - base) * ((1 - h) / h) := by ring
    _ ≤ C * h * (1 - h)⁻¹ * ((1 - h) / h) :=
        mul_le_mul_of_nonneg_right hreach hfac
    _ = C := hid

/-- **The exclusion, assembled: a bounded tower stays strictly below the
target, at every truncation order.** Given that the whole tail `C·h/(1-h)` falls
short of the gap `target - base`, no partial resummation reaches the target —
for every coefficient sequence within the bound, every sign pattern, and every
`n`. This is the class-D analogue of `MultiplicityNotExtensive`'s
`multiplicity_not_extensive`: the channel is capped by counting, not by an
estimate of what the corpus happens to produce. -/
theorem bounded_tower_lt_target {h C base target : ℝ}
    (h0 : 0 ≤ h) (h1 : h < 1) {a : ℕ → ℝ} (ha : ∀ k, |a k| ≤ C)
    (hshort : C * h * (1 - h)⁻¹ < target - base) (n : ℕ) :
    base + ∑ k ∈ Finset.range n, h ^ (k + 1) * a k < target := by
  have hle := le_of_abs_le (tower_partial_abs_le h0 h1 ha n)
  linarith

/-- **The exclusion has content.** At `h = 1/2`, `C = 1`, `base = 0`,
`target = 2` the hypotheses hold — the whole tail is `1`, the gap is `2` — and
the conclusion is a genuine strict inequality. Guards against the failure mode
of AGENTS.md §"No trivial trues". -/
example (n : ℕ) :
    (0 : ℝ) + ∑ k ∈ Finset.range n, (1 / 2 : ℝ) ^ (k + 1) * (1 : ℝ) < 2 := by
  refine bounded_tower_lt_target (h := 1 / 2) (C := 1) (base := 0) (target := 2)
    (by norm_num) (by norm_num) (fun _ => by norm_num) ?_ n
  norm_num

end Tail

end QOU.Hecke.BondCutSymmetryFibreTowerBound
