/-
# The three channels differ by growth class, and only the massless one is quadratic

Adding a bond MULTIPLIES the Markov trace by `b < 1`, so the framework's native
falloff is `b^{d(i,j)} = exp(-μ·d(i,j))` with `μ = -log b`: exponential in graph
distance, which is a Yukawa profile. That puts the three nuclear channels on one
axis — the mediator mass:

| channel | mediator | `μ` | pair sum over `n` sites |
|---|---|---|---|
| weak | W/Z, ~80 GeV | ~407 fm⁻¹ | `O(n)` |
| strong | π, ~140 MeV | ~0.707 fm⁻¹ | `O(n)` |
| EM | photon, **massless** | `0` | `Θ(n²)` |

`massless_pair_sum` and `no_linear_bound_on_pairs` are the dichotomy: at `μ = 0`
every pair contributes 1 and the sum is `n(n-1)/2`, which no constant multiple
of `n` bounds. So Coulomb is not "a longer-range bond" — it is the massless
boundary, a different growth class, and every `q`-derived rate is strictly
positive because `b < 1`. This is the analytic content behind
`QOU/Hecke/BoundedDegreeCoulomb.lean`, which proves the same separation from the
degree side.

## Two convergence criteria, and only one of them binds a nucleus

The per-site sum is `Σ_k |S_k|·exp(-μk)` over shells `S_k` at graph distance `k`.

* **Tree-like (worst case for bounded degree `d`):** `|S_k| ≤ d(d-1)^{k-1}`, so
  the sum converges iff `(d-1)exp(-μ) < 1`, i.e. **`μ > log(d-1)`**
  (`tree_threshold_iff`, `geometric_partial_sum_le`).
* **Geometric in ℝ³ (a nuclear packing):** `|S_k| ~ ck²`, polynomial, and then
  `Σ k² exp(-μk)` converges for **every** `μ > 0`.

**The tree threshold does not bind a nucleus** — worth stating because it is easy
to reach for. Measured against the corpus letters it would look alarming: only
`L_nn = 0.907` clears `log 2` at `d = 3`, and none of the three clears `log(d-1)`
at `d ≥ 4`. A packing is not a tree, so nothing follows from that. What DOES
follow is a magnitude, in the probe: on an fcc shell count `10k²+2` the framework's
own decay reaches an effective **173.2** sites for `b_pp` against 12 contacts —
**14.4×**. So truncating the bond graph at range 1 is not self-consistent with
the decay rate the same framework supplies.

## The three rates are not independent — exactly one free parameter

`b_pp·b_nn = 1/[2]_q²` is an identity (`QOU/Hecke/SymmetrySignAmGm.lean`), so
`rate_sum_pinned` gives

```
L_pp + L_nn = 2 log [2]_q          (0.489899 + 0.907262 = 1.397162)
```

and `L_pn` is fixed between them by the averaging convention. Three decay rates,
one constraint, one free parameter `q`. Any proposal that moves one rate moves
another, which is the care the channel picture needs.

Bean `qou-556v`; raised by the owner as "the three rates are not necessarily
independent".
-/

import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Algebra.Ring.GeomSum
import Mathlib.Tactic

namespace QOU.Hecke.ChannelRangeGrowthClass

open Finset

/-- A geometric shell sum is bounded independently of how many shells are taken,
exactly when the decay beats the growth ratio. This is what "extensive" means
here: a per-site bound that does not grow with the system. -/
theorem geometric_partial_sum_le {c x : ℝ} (hc : 0 ≤ c) (hx0 : 0 ≤ x) (hx1 : x < 1)
    (K : ℕ) :
    ∑ k ∈ Finset.range K, c * x ^ k ≤ c / (1 - x) := by
  have hpos : (0 : ℝ) < 1 - x := by linarith
  have hgeom : ∑ k ∈ Finset.range K, x ^ k ≤ 1 / (1 - x) := by
    rw [le_div_iff₀ hpos]
    nlinarith [pow_nonneg hx0 K, geom_sum_mul x K]
  calc ∑ k ∈ Finset.range K, c * x ^ k
      = c * ∑ k ∈ Finset.range K, x ^ k := by rw [Finset.mul_sum]
    _ ≤ c * (1 / (1 - x)) := by exact mul_le_mul_of_nonneg_left hgeom hc
    _ = c / (1 - x) := by ring

/-- **The tree criterion.** For a bounded-degree graph the shell at distance `k`
holds at most `d(d-1)^{k-1}` sites, so a Yukawa weight `exp(-μk)` gives a
bounded per-site sum exactly when `μ > log(d-1)`.

This is the WORST case (a tree). A nuclear packing has polynomial shell growth
and needs no such threshold — see the module docstring. -/
theorem tree_threshold_iff {d μ : ℝ} (hd : 1 < d) :
    (d - 1) * Real.exp (-μ) < 1 ↔ Real.log (d - 1) < μ := by
  have hd1 : (0 : ℝ) < d - 1 := by linarith
  have hpos : (0 : ℝ) < (d - 1) * Real.exp (-μ) := by positivity
  have hlog : Real.log ((d - 1) * Real.exp (-μ)) = Real.log (d - 1) - μ := by
    rw [Real.log_mul (ne_of_gt hd1) (Real.exp_ne_zero _), Real.log_exp]; ring
  constructor
  · intro h
    have := (Real.log_neg_iff hpos).mpr h
    rw [hlog] at this
    linarith
  · intro h
    have : Real.log ((d - 1) * Real.exp (-μ)) < 0 := by rw [hlog]; linarith
    exact (Real.log_neg_iff hpos).mp this

/-- **At zero decay every pair contributes fully.** A massless mediator weights
all `n(n-1)/2` pairs by `exp(0) = 1`. -/
theorem massless_pair_sum (n : ℕ) :
    (n * (n - 1) : ℝ) / 2 * Real.exp (-0 : ℝ) = (n * (n - 1) : ℝ) / 2 := by
  simp

/-- **And that is a different growth class from any extensive law.** No constant
multiple of `n` bounds the pair count, so a massless channel cannot be
represented by a bounded per-site sum however the bond letters are chosen. -/
theorem no_linear_bound_on_pairs (C : ℝ) :
    ∃ n : ℝ, 2 < n ∧ C * n < n * (n - 1) / 2 := by
  refine ⟨max 3 (2 * C + 2), ?_, ?_⟩
  · have : (3 : ℝ) ≤ max 3 (2 * C + 2) := le_max_left _ _
    linarith
  · have h3 : (3 : ℝ) ≤ max 3 (2 * C + 2) := le_max_left _ _
    have hC : 2 * C + 2 ≤ max 3 (2 * C + 2) := le_max_right _ _
    nlinarith

/-- **The p-p and n-n decay rates sum to a constant.** Given the pinned product
`b_pp·b_nn = 1/t²` (here `t = [2]_q`), the two rates `L = -log b` satisfy
`L_pp + L_nn = 2 log t`. Three rates, one constraint, one free parameter. -/
theorem rate_sum_pinned {bpp bnn t : ℝ} (hpp : 0 < bpp) (hnn : 0 < bnn)
    (ht : 0 < t) (h : bpp * bnn = 1 / t ^ 2) :
    -Real.log bpp + -Real.log bnn = 2 * Real.log t := by
  have hmul : Real.log bpp + Real.log bnn = Real.log (1 / t ^ 2) := by
    rw [← Real.log_mul (ne_of_gt hpp) (ne_of_gt hnn), h]
  rw [Real.log_div one_ne_zero (by positivity), Real.log_one, Real.log_pow] at hmul
  push_cast at hmul
  linarith

end QOU.Hecke.ChannelRangeGrowthClass
