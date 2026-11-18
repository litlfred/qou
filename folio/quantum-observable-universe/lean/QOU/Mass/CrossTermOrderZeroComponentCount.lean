import QOU.MassTheory.BorromeanThreeBodyCluster
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic

/-!
# Component count decides the order-zero part of a Markov-trace cross term

`qou-5vhf` step 2 (bean `qou-0fxk`). Two measured facts on `main`:

* at `q = 1` the Markov trace on `ℚSₙ` is the component-count trace `tr₁(w) = 2^{c(w)−n}`
  (T1 probe, route-C probe; verified on all of `S₃`, `S₄` in the spin-½ representation), so the
  order-zero part of any cross term `tr(w) − tr(w')` is `2^{c(w)−n} − 2^{c(w')−n}`;
* the corpus's irreducible 3-body operator, the Brunnian band word `w₃ = [A₀₁, A₁₂]` against the
  3-unlink, has deficit `1 − τ_Borr(h) = h⁴(3+h²)/(h²+4)` (`one_sub_tauBorromean`), i.e. q-adic
  order **four** — its closure has the unlink's three components, so its order-zero part vanishes.

This file carries the two elementary statements that join them:

1. `componentTrace_eq_iff` — the order-zero cross term vanishes **iff** the component counts agree
   (`2^k` is injective). Component-changing word pairs (the `n = 4` trefoil-vs-chain, components
   `1` vs `3`) have an `O(1)` classical cross term; component-preserving pairs have a cross term of
   positive q-adic order — a pure q-deformation effect.
2. `one_sub_tauBorromean_eq_h4_mul` / `one_sub_tauBorromean_le` — the Brunnian deficit is `h⁴`
   times a bounded factor (`≤ 1` for `h² ≤ 1`, and `< 1` always, since `(3+h²)/(h²+4) < 1`), so
   at the substrate pin, where `h = q₀ − q₀⁻¹ ≈ 0.209`, it is bounded by `h⁴ ≈ 1.9 × 10⁻³`. The
   framework's classical cross terms are `O(1)`; the missing 3-body magnitude the Δ_λ audit names
   (quoted there as `μ₃ ≈ 0.47 MeV` against `E₀ ≈ 4.19 MeV`, i.e. `≈ 0.11` in trace units) sits
   between the two classes. Nothing here evaluates a target; the inequalities are exact bounds.

Base ring §7c: the component lemma is over `ℚ` (exact, no ordering); the deficit bounds are over
`ℝ`, inherited from `tauBorromean : ℝ → ℝ`, because they are ordering facts.

-- Ref: [leitner2026] computations/probes/component_count_decides_q_adic_order_probe.py
-- Ref: [leitner2026] QOU/MassTheory/BorromeanThreeBodyCluster.lean (`one_sub_tauBorromean`)
-/

namespace QOU.Mass.CrossTermOrderZeroComponentCount

open QOU.MassTheory

/-- The component-count trace at `q = 1`: a closure with `c` components on `n` strands has
Markov trace `2^c / 2^n` (the Ocneanu trace with `z = 1/2` on the group algebra). -/
def componentTrace (n c : ℕ) : ℚ := (2 : ℚ) ^ c / (2 : ℚ) ^ n

/-- **The order-zero cross term vanishes iff the component counts agree.** -/
theorem componentTrace_eq_iff (n c c' : ℕ) :
    componentTrace n c = componentTrace n c' ↔ c = c' := by
  unfold componentTrace
  have h2 : (2 : ℚ) ^ n ≠ 0 := pow_ne_zero n (by norm_num)
  constructor
  · intro h
    have h' : (2 : ℚ) ^ c = (2 : ℚ) ^ c' := by
      have := congrArg (· * (2 : ℚ) ^ n) h
      simpa [div_mul_cancel₀ _ h2] using this
    exact Nat.pow_right_injective (le_refl 2) (by exact_mod_cast h')
  · rintro rfl; rfl

/-- The `n = 4` instance behind T1: a knot (`c = 1`) and a three-component closure (`c = 3`)
have order-zero traces `1/8` and `1/2`, cross term `−3/8`. -/
theorem n4_instance : componentTrace 4 1 - componentTrace 4 3 = -3 / 8 := by
  unfold componentTrace; norm_num

/-- A component-preserving pair has **no** order-zero cross term. -/
theorem componentTrace_sub_eq_zero_of_eq {n c c' : ℕ} (h : c = c') :
    componentTrace n c - componentTrace n c' = 0 := by
  subst h; simp

/-! ### The Brunnian deficit is `h⁴` times a factor below one -/

/-- `1 − τ_Borr(h) = h⁴ · r(h)` with `r(h) = (3+h²)/(h²+4)`. -/
theorem one_sub_tauBorromean_eq_h4_mul (h : ℝ) :
    1 - tauBorromean h = h ^ 4 * ((3 + h ^ 2) / (h ^ 2 + 4)) := by
  rw [one_sub_tauBorromean]; ring

/-- The factor `(3+h²)/(h²+4)` is strictly below `1` for every real `h`. -/
theorem brunnian_factor_lt_one (h : ℝ) : (3 + h ^ 2) / (h ^ 2 + 4) < 1 := by
  have hd : (0 : ℝ) < h ^ 2 + 4 := by positivity
  rw [div_lt_one hd]; linarith

/-- **The Brunnian deficit is bounded by `h⁴`**: `0 ≤ 1 − τ_Borr(h) ≤ h⁴`, with the upper bound
strict for `h ≠ 0`. At the substrate pin `h ≈ 0.209` this is `≈ 1.9 × 10⁻³` — a pure
q-deformation quantity two orders below the `O(1)` classical cross terms. -/
theorem one_sub_tauBorromean_le (h : ℝ) : 1 - tauBorromean h ≤ h ^ 4 := by
  rw [one_sub_tauBorromean_eq_h4_mul]
  have h4 : (0 : ℝ) ≤ h ^ 4 := by positivity
  calc h ^ 4 * ((3 + h ^ 2) / (h ^ 2 + 4)) ≤ h ^ 4 * 1 :=
        mul_le_mul_of_nonneg_left (le_of_lt (brunnian_factor_lt_one h)) h4
    _ = h ^ 4 := mul_one _

theorem one_sub_tauBorromean_lt {h : ℝ} (hh : h ≠ 0) : 1 - tauBorromean h < h ^ 4 := by
  rw [one_sub_tauBorromean_eq_h4_mul]
  have h4 : (0 : ℝ) < h ^ 4 := by positivity
  calc h ^ 4 * ((3 + h ^ 2) / (h ^ 2 + 4)) < h ^ 4 * 1 :=
        mul_lt_mul_of_pos_left (brunnian_factor_lt_one h) h4
    _ = h ^ 4 := mul_one _


/-- **Self-difference of the component-count trace (`qou-qb9e`).**
For any strand count `n` and component count `c`, `componentTrace n c - componentTrace n c = 0`. -/
theorem componentTrace_self_sub_eq_zero (n c : ℕ) :
    componentTrace n c - componentTrace n c = 0 :=
  componentTrace_sub_eq_zero_of_eq rfl

end QOU.Mass.CrossTermOrderZeroComponentCount
