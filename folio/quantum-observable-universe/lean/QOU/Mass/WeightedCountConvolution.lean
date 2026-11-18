import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Tactic

/-!
# The K-weighted count is multiplicative over disjoint blocks

Bean `qou-8uxw`, candidate S1 of
`docs/audits/2026-09-07-route-c-step3-and-kz-level-plans.md` §A.

§7h of the binding-gap survey writes the framework's convention-D trace of a braid word `w`
on `n` strands as a weighted count over the colour-1 strand number `k`,

    C(w) = Σ_{k=0}^{n} q^{n − 2k} · N_k(w),

with `N_k(w)` the per-weight-space fixed-point count. For a *disjoint juxtaposition*
`w₁ ⊔ w₂` (the tensor product of two words on `n₁` and `n₂` strands) the counts convolve —
`N_k(w₁ ⊔ w₂) = Σ_{i+j=k} N_i(w₁) N_j(w₂)` — because a colouring of the union is a pair of
colourings. The worry S1 answers is whether the *disjoint union over `k`* in `C` could be
where a many-body term hides. It cannot: `C` is a polynomial evaluation, `C(w) = q^n · P_w(q⁻²)`
with `P_w(y) = Σ_k N_k(w) y^k`, and convolution of coefficients is multiplication of
polynomials, so `C(w₁ ⊔ w₂) = C(w₁) · C(w₂)` — hence `log C` is additive over blocks by
construction. Non-factorisation over *bonds* is therefore decided by the word's topology
alone (the ordering hypothesis of `FormalityBridgeF1`), never by the `k`-structure.

The statement is proved at the level it has: for polynomials `P, Q` over a field and
`x ≠ 0`, `weighted (P * Q) (n₁ + n₂) x = weighted P n₁ x * weighted Q n₂ x`. Identifying
`P_w` with the count polynomial of a specific word is the probe's job
(`route_c_step2_pivotal_vs_count_probe.py`, checks 18–26), not this file's.

Base ring: a generic `Field K`; no `ℝ`.
-/

namespace QOU.Mass.WeightedCountConvolution

open Polynomial

variable {K : Type*} [Field K]

/-- `Σ_k a_k x^{n−2k}`, written as `x^n · P(x⁻²)` for `P = Σ a_k Y^k`. -/
noncomputable def weighted (P : K[X]) (n : ℕ) (x : K) : K := x ^ n * P.eval (x⁻¹ ^ 2)

/-- Disjoint juxtaposition multiplies the weighted counts: convolution of the `N_k` is
polynomial multiplication, and the weight `x^{n}` is additive in `n`. -/
theorem weighted_mul (P Q : K[X]) (n₁ n₂ : ℕ) (x : K) :
    weighted (P * Q) (n₁ + n₂) x = weighted P n₁ x * weighted Q n₂ x := by
  unfold weighted
  rw [eval_mul, pow_add]
  ring

/-- Consequently the weighted count of a juxtaposition of `m` copies is the `m`-th power. -/
theorem weighted_pow (P : K[X]) (n : ℕ) (x : K) (m : ℕ) :
    weighted (P ^ m) (m * n) x = (weighted P n x) ^ m := by
  induction m with
  | zero => simp [weighted]
  | succ m ih =>
    rw [pow_succ, Nat.succ_mul, weighted_mul, ih, pow_succ]

/-- Subtracting the product of weighted evaluations from the weighted evaluation of the product polynomial cancels to zero (`qou-drag`). -/
theorem weighted_mul_sub_eq_zero (P Q : K[X]) (n₁ n₂ : ℕ) (x : K) :
    weighted (P * Q) (n₁ + n₂) x - weighted P n₁ x * weighted Q n₂ x = 0 := by
  rw [weighted_mul P n₁ Q n₂ x, sub_self]

end QOU.Mass.WeightedCountConvolution
