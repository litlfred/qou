/-
# `A_w` zero localization — the algebraic core of the theta-limit Rouché argument

The KSel-2-ID chain's remaining analytic debt (`TropicalClassTransport` §3,
the u1-promotion audit §4 gap 2) is the zero asymptotics of the Ramanujan
entire function (q-Airy function)

    A_w(z) = Σ_{m ≥ 0} w^{m²} (−z)^m / (w;w)_m,     0 < w < 1,

namely `ζ_n = w^{1−2n}(1 + O(w^n))`: the zeros are asymptotic to the successive
coefficient ratios — the tropical / Newton-polygon corners.

`docs/audits/2026-08-01-awzero-asymptotics.md` proves this by recentring
`A_w` at index `n`, identifying the limit of the recentred series as a Jacobi
theta function whose zero set is the lattice `w^{2ℤ}`, and running Rouché
against that theta limit.  This module formalises the **algebraic core** of
that argument — three exact identities plus two order facts (strict convexity
of the Newton polygon, and the antitone Ω-factor behind the grid-free
majorant) — sorry-free.  The analytic steps that need complex analysis (Jacobi
triple product, Rouché, the argument principle) are NOT formalised here and
are NOT claimed to be: see the audit for their status.

PROVED here (sorry-free):

* `recentring_exponent` / `recentring_zpow` — the exponent bookkeeping behind
  `A_w(w^{1−2n}u) = (−1)^n w^{n−n²} u^n Φ_n(u)`: substituting `z = w^{1−2n}u`
  recentres the Gaussian exponent `m²` at index `m = n`.  This is *why* index
  `n` is the one whose term dominates near `z = w^{1−2n}`, i.e. why the n-th
  zero sits there and not elsewhere.
* `wPoch_ratio` — the tropical (Newton-polygon) ratio in division-free form:
  the coefficient ratio of `A_w` at index `n` is `w^{−(2n+1)}(1 − w^{n+1})`.
* `tropRoot_lt_succ` (ℝ) — those ratios are STRICTLY increasing, so the Newton
  polygon is strictly convex and every corner is genuine (no two zeros share a
  tropical index).  Reduces to `w^{n+2} < 1 + w`.
* `one_sub_inv` and `prod_one_sub_inv` — the reflection identity
  `1 − x⁻¹ = −x⁻¹(1 − x)` and its product form.  This is the exact q-shift
  cancellation that makes the even-`j` defect ratio collapse to the closed form
  `w^{−s(s+1)}|u|^{−s}`; it is what keeps the theta cancellation in the bound
  and hence what lets the argument survive `w → 1`, where a single-term Rouché
  provably cannot (audit §5).
* `omega_factor_key` and `omegaFactor_antitone` (ℝ) — each factor of the
  Ω-quotient on the counting circle `|u| = w⁻¹` is antitone in `S = sin²(θ/2)`,
  the fact behind the closed-form (grid-free) majorant
  `Ω ≤ 2 (w²;w²)_∞²/(w;w²)_∞²`.  The algebraic heart is the exact factorisation
  `w(1−x)² − (1−wx)² = −(1−w)(1 − wx²)`.

NOT proved here, and not claimed: the Jacobi triple product identification of
the theta limit, the Rouché/argument-principle steps, the value of `n₀(w)`, or
the asymptotics themselves.  Nothing in this module is wired to production.

Base ring (§7c): the four algebraic items are generic `[Field K]` (the
q-shift/reflection content is rational).  Only the two order statements —
strict convexity of the Newton polygon and the antitone factor — are
archimedean and live over `ℝ`.

-- Ref: [leitner2026] docs/audits/2026-08-01-awzero-asymptotics.md;
--      docs/audits/2026-08-01-ksel2id-tropical-transport.md §3;
--      docs/audits/2026-08-01-ksel2id-u1-promotion.md §4 gap 2;
--      bean qou-k16h.
-/

import Mathlib.Algebra.BigOperators.Field
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.Field.Power
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity.Basic
import Mathlib.Tactic.Ring

namespace QOU.Archimedean.AwZeroLocalization

open Finset

variable {K : Type*} [Field K]

/-! ## 1.  Recentring: why index `n` owns the point `z = w^{1−2n}` -/

/-- The Gaussian exponent of `A_w` recentres at index `n` under the
substitution `z = w^{1−2n} u`:  `m² + (1−2n)m = (n − n²) + (m−n)(m−n+1)`.
The right-hand side is a constant plus a Gaussian in `m − n`, so the term of
index `m = n` is the extremal one at that argument. -/
theorem recentring_exponent (m n : ℤ) :
    m ^ 2 + (1 - 2 * n) * m = (n - n ^ 2) + (m - n) * (m - n + 1) := by
  ring

/-- The field-level form of `recentring_exponent`. -/
theorem recentring_zpow {w : K} (hw : w ≠ 0) (m n : ℤ) :
    w ^ (m ^ 2 + (1 - 2 * n) * m)
      = w ^ (n - n ^ 2) * w ^ ((m - n) * (m - n + 1)) := by
  rw [← zpow_add₀ hw, recentring_exponent]

/-! ## 2.  The tropical (Newton-polygon) ratio -/

/-- `(w;w)_n = ∏_{i=1}^{n} (1 - w^i)`. -/
def wPoch (w : K) : ℕ → K
  | 0 => 1
  | n + 1 => wPoch w n * (1 - w ^ (n + 1))

@[simp] theorem wPoch_zero (w : K) : wPoch w 0 = 1 := rfl

theorem wPoch_succ (w : K) (n : ℕ) :
    wPoch w (n + 1) = wPoch w n * (1 - w ^ (n + 1)) := rfl

/-- Division-free form of the coefficient ratio of `A_w`.  Writing
`a_n = (−1)^n w^{n²}/(w;w)_n`, this says `a_n / a_{n+1} = −w^{−(2n+1)}(1−w^{n+1})`,
i.e. the `n`-th tropical root is `w^{−(2n+1)}(1 − w^{n+1})`. -/
theorem wPoch_ratio (w : K) (n : ℕ) :
    w ^ (n ^ 2) * w ^ (2 * n + 1) * wPoch w (n + 1)
      = w ^ ((n + 1) ^ 2) * (1 - w ^ (n + 1)) * wPoch w n := by
  have hpow : w ^ (n ^ 2) * w ^ (2 * n + 1) = w ^ ((n + 1) ^ 2) := by
    rw [← pow_add]
    congr 1
    ring
  rw [wPoch_succ, hpow]
  ring

/-! ## 3.  Strict convexity of the Newton polygon (archimedean) -/

/-- The `n`-th tropical root `w^{−(2n+1)}(1 − w^{n+1})` of `A_w`. -/
noncomputable def tropRoot (w : ℝ) (n : ℕ) : ℝ := (1 - w ^ (n + 1)) / w ^ (2 * n + 1)

/-- The tropical roots are strictly increasing for `0 < w < 1`: the Newton
polygon of `A_w` is strictly convex, so every corner is a genuine corner and
distinct indices give distinct tropical roots.  The whole statement reduces to
`w^{n+2} < 1 + w`. -/
theorem tropRoot_lt_succ {w : ℝ} (hw0 : 0 < w) (hw1 : w < 1) (n : ℕ) :
    tropRoot w n < tropRoot w (n + 1) := by
  have hp1 : (0:ℝ) < w ^ (2 * n + 1) := pow_pos hw0 _
  have hp2 : (0:ℝ) < w ^ (2 * (n + 1) + 1) := pow_pos hw0 _
  have hle : w ^ (n + 2) ≤ 1 := pow_le_one₀ hw0.le hw1.le
  -- the core inequality: `(1 − w^{n+1}) w² < 1 − w^{n+2}`
  have hkey : (1 - w ^ (n + 1)) * w ^ 2 < 1 - w ^ (n + 2) := by
    have e1 : w ^ (n + 2) = w ^ (n + 1) * w := by ring
    have e2 : w ^ (n + 1) * w ^ 2 = w ^ (n + 2) * w := by
      rw [e1]; ring
    nlinarith [hw0, hw1, hle, sq_nonneg w]
  have e3 : w ^ (2 * (n + 1) + 1) = w ^ (2 * n + 1) * w ^ 2 := by ring
  rw [tropRoot, tropRoot, div_lt_div_iff₀ hp1 hp2, e3]
  nlinarith [hp1, hkey]

/-! ## 4.  The reflection identity — the exact q-shift cancellation -/

/-- `1 − x⁻¹ = −x⁻¹ (1 − x)`.  Applied with `x = w^{2i} u` this is the exact
cancellation that collapses the even-`j` defect ratio to `w^{−s(s+1)}|u|^{−s}`,
keeping the theta cancellation in the Rouché comparison. -/
theorem one_sub_inv {x : K} (hx : x ≠ 0) : 1 - x⁻¹ = -x⁻¹ * (1 - x) := by
  field_simp
  ring

/-- Product form of the reflection identity: the finite telescoping used to
evaluate the even-`j` ratio in closed form. -/
theorem prod_one_sub_inv (x : ℕ → K) (hx : ∀ i, x i ≠ 0) (s : ℕ) :
    (∏ i ∈ range s, (1 - (x i)⁻¹))
      = (-1) ^ s * (∏ i ∈ range s, x i)⁻¹ * ∏ i ∈ range s, (1 - x i) := by
  induction s with
  | zero => simp
  | succ s ih =>
      have hne : (∏ i ∈ range s, x i) ≠ 0 := prod_ne_zero_iff.2 fun i _ => hx i
      rw [prod_range_succ, ih, prod_range_succ (f := x), prod_range_succ (f := fun i => 1 - x i),
        one_sub_inv (hx s)]
      field_simp
      ring

/-! ## 5.  The antitone Ω-factor (archimedean) — the grid-free majorant -/

/-- The algebraic heart of the counting-circle majorant:
`w(1−x)² − (1−wx)² = −(1−w)(1 − wx²)`. -/
theorem omega_factor_key (w x : ℝ) :
    w * (1 - x) ^ 2 - (1 - w * x) ^ 2 = -((1 - w) * (1 - w * x ^ 2)) := by
  ring

/-- Each factor of the Ω-quotient on the counting circle `|u| = w⁻¹` is
antitone in `S = sin²(θ/2)`.  With `x = w^{2i+1}` the factor is
`((1 − wx)² + 4wx·S) / ((1 − x)² + 4x·S)`; monotonicity follows from
`omega_factor_key`, whose right-hand side is negative for `0 < w < 1`,
`0 < x < 1`.  Evaluating at `S = 0` therefore majorises the whole circle,
which is what turns the Rouché threshold `n₀(w)` into a closed-form,
grid-free quantity. -/
theorem omegaFactor_antitone {w x S T : ℝ} (hw0 : 0 < w) (hw1 : w < 1)
    (hx0 : 0 < x) (hx1 : x < 1) (hS : 0 ≤ S) (hST : S ≤ T) :
    ((1 - w * x) ^ 2 + 4 * (w * x) * T) / ((1 - x) ^ 2 + 4 * x * T)
      ≤ ((1 - w * x) ^ 2 + 4 * (w * x) * S) / ((1 - x) ^ 2 + 4 * x * S) := by
  have hT : (0:ℝ) ≤ T := hS.trans hST
  have hx1' : (1 - x) ≠ 0 := by linarith
  have hdS : (0:ℝ) < (1 - x) ^ 2 + 4 * x * S := by positivity
  have hdT : (0:ℝ) < (1 - x) ^ 2 + 4 * x * T := by positivity
  have hwx2 : w * x ^ 2 < 1 := by nlinarith
  have hkey : w * (1 - x) ^ 2 - (1 - w * x) ^ 2 < 0 := by
    rw [omega_factor_key]; nlinarith
  rw [div_le_div_iff₀ hdT hdS]
  nlinarith [mul_nonneg (mul_nonneg (by norm_num : (0:ℝ) ≤ 4) hx0.le) (sub_nonneg.2 hST),
    hkey, hx0, hST]

end QOU.Archimedean.AwZeroLocalization
