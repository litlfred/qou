/-
# How far the fibre tower can move the slope, and what it actually sums to

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

## The tail bound, and 🛑 the BOUNDED form does not decide this tower

Suppose the tower moves `δ` directly: `δ = δ^{(0)} + Σ_{k≥1} h^k δ^{(k)}` in an
expansion parameter `h`, which at the substrate is `ℏ_q = (q-1)/q ≈ 0.0991`. If
the coefficients are bounded by `C` then

```
|Σ_{k≥1} h^k δ^{(k)}|  ≤  C·h/(1-h)          (`tower_partial_abs_le`)
```

at **every** truncation order, which is the honest form: a truncation is what
any computation has, and the bound does not depend on which one. Read backwards
(`tower_coefficient_lower_bound`) it is a lower bound on the coefficients a
tower would need: `δ* = 4·a_A/(E₀·k) ≈ 1.8687` at degree `12` against the
corpus's `δ ≈ -0.02176` needs `C ≥ 17.19`.

**And the corpus's tower does not satisfy the hypothesis.** Measured with exact
rational coefficients (producer R4), `max_k |δ^{(k)}|` over `k = 1…24` is
**26.14**, at `k = 24` — the coefficients *grow*. So `17.19 < 26.14` and the
bounded-coefficient route **fails to decide the close-packed degree**. It does
decide the chain (`k = 2` needs `C ≥ 102.1`), and that asymmetry is recorded as
its own assertion in the producer (R5c / R5d) rather than omitted.

The first draft of this file asserted the 17.19 as though it bit, on an
unmeasured assumption that the tower's coefficients were `O(1)`. They are not;
the claim is withdrawn. `tower_partial_abs_le` and `tower_coefficient_lower_bound`
are correct mathematics about a *bounded* tower and are kept as such.

**The bound that does apply is the geometric one.** The coefficients grow like
`ρ^{-k}` for a radius of convergence `ρ ≈ 0.8729` (measured
`|δ^{(24)}|^{1/24} = 1.1456`), and `tower_geometric_abs_le` is
`tower_partial_abs_le` with `h := h/ρ` — giving `|tail| ≤ M·(h/ρ)/(1 - h/ρ) =
0.1951` at `M = 1.524`, which contains the measured `|δ| = 0.02176` and sits
below the convex cap `2 ln q₀ = 0.2087`.

## What actually decides it: the closed form is already the all-orders sum

The sharper reading, and the one the producer's R4 establishes: **the corpus's
`δ` is not an order-zero truncation of anything.** Exactly,

* `δ^{(0)} = δ^{(1)} = 0` — the series starts at order `2` in `ℏ_q`, so the
  *whole* p–n slope is a tower effect and there is no leading term for higher
  orders to correct;
* resumming `k = 0…24` reproduces the directly-evaluated closed form at `q₀` to
  `< 1e-20`.

So "use the full tower in `q`" has already been done — by writing the closed
form and evaluating it. What remains is what that sum *is*: `-0.02176`, giving
`a_A = E₀·k·δ/4 = -0.2760` MeV at `k = 12` — **short of the `23.7` MeV target by
85.9×, and of the wrong sign** — while the cap on *any* convex interface is
`2.6466` MeV, short by `8.955×`. Those two numbers, not the tail bound, are
what closes the row.

`bounded_tower_lt_target` is retained as the assembled conditional: for every
truncation, a tower *within its coefficient bound* stays strictly below the
target.

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

/-- **The bound that applies to a GEOMETRIC tower**, which is what the corpus's
actually is. If the coefficients grow no faster than `r^{-k}` — i.e.
`|a k|·r^{k+1} ≤ C`, a radius-of-convergence statement — then the tail is
bounded by the same geometric expression in `h/r`. This is
`tower_partial_abs_le` applied to `a k · r^{k+1}` at expansion parameter `h/r`,
and it is the form to reach for whenever `max |a k|` is not finite or not small:
the corpus's measured `r ≈ 0.8729`, `h/r ≈ 0.1135`, `C ≈ 1.524` give a tail
bound of `0.1951`, which contains the measured `|δ| = 0.02176`. -/
theorem tower_geometric_abs_le {h r C : ℝ} (h0 : 0 ≤ h) (hr : 0 < r)
    (hlt : h < r) {a : ℕ → ℝ} (ha : ∀ k, |a k * r ^ (k + 1)| ≤ C) (n : ℕ) :
    |∑ k ∈ Finset.range n, h ^ (k + 1) * a k|
      ≤ C * (h / r) * (1 - h / r)⁻¹ := by
  have hrne : r ≠ 0 := ne_of_gt hr
  have hrw : ∀ k : ℕ, h ^ (k + 1) * a k
      = (h / r) ^ (k + 1) * (a k * r ^ (k + 1)) := by
    intro k
    rw [div_pow]
    field_simp
  have hsum : ∑ k ∈ Finset.range n, h ^ (k + 1) * a k
      = ∑ k ∈ Finset.range n, (h / r) ^ (k + 1) * (a k * r ^ (k + 1)) :=
    Finset.sum_congr rfl fun k _ => hrw k
  rw [hsum]
  exact tower_partial_abs_le (div_nonneg h0 hr.le)
    ((div_lt_one hr).mpr hlt) ha n

/-- **Read backwards: the coefficient a tower would need.** If the whole tower
is to carry the quantity from `base` to `target`, its coefficient bound is at
least `(target - base)·(1-h)/h`. At the substrate `h = ℏ_q ≈ 0.0991`, closing
`δ: -0.02176 → 1.8687` needs `C ≥ 17.19` at the close-packed degree and
`C ≥ 102.1` at the chain degree.

🛑 **Measured, the corpus's tower has `max_k |δ^{(k)}| = 26.14`**, so this
decides the chain and NOT the close-packed degree. See the header; the numbers
here are the *requirement*, not a demonstration that it is unmet. -/
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
