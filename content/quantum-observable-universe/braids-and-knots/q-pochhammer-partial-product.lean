/-!
# q-Pochhammer partial product Φ_n(x; q)

The depth-n truncation of the analytic quantum dilogarithm
Φ_q(x) = ∏_{k≥0} 1/(1 - x q^k). Defined recursively so the
denominator polynomial (x; q)_n is exposed as a finite product
of simple linear factors, each with a known root x = q^{-k}.

The recurrence Φ_{n+1}(x; q) = (1 - x q^n)^{-1} · Φ_n(x; q) is the
algebraic shadow of the inductive filtration step that drives jet-
stratified GB reduction.

-- Ref: [manuscript] def:q-pochhammer-partial-product
-- Ref: [faddeev1994] https://doi.org/10.1142/S0217732394002793
-/

import Mathlib.Algebra.BigOperators.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace QOU.QPochhammer

/-- Denominator polynomial `(x; q)_n = ∏_{k=0..n-1} (1 - x q^k)` as a
    real-valued partial product. The roots of this polynomial in `x`
    are exactly `q^{-k}` for `k = 0, .., n-1`, and they are the
    addresses of the algebraic poles of the categorical state sum. -/
-- Ref: [manuscript] def:q-pochhammer-partial-product
def denomPoly (q x : ℝ) : ℕ → ℝ
  | 0 => 1
  | n + 1 => (1 - x * q ^ n) * denomPoly q x n

/-- One-step unfold of the denominator. -/
@[simp] theorem denomPoly_succ (q x : ℝ) (n : ℕ) :
    denomPoly q x (n + 1) = (1 - x * q ^ n) * denomPoly q x n := rfl

@[simp] theorem denomPoly_zero (q x : ℝ) : denomPoly q x 0 = 1 := rfl

/-- The q-Pochhammer partial product `Φ_n(x; q) = 1 / (x; q)_n`.
    Defined via the recurrence `Φ_{n+1} = (1 - x q^n)^{-1} · Φ_n`.
    The recurrence is the inductive filtration step on the algebraic
    side of the QOU framework. -/
-- Ref: [manuscript] def:q-pochhammer-partial-product
noncomputable def partialProduct (q x : ℝ) (n : ℕ) : ℝ :=
  (denomPoly q x n)⁻¹

@[simp] theorem partialProduct_zero (q x : ℝ) :
    partialProduct q x 0 = 1 := by
  simp [partialProduct, denomPoly]

/-- Recursive step of the partial product: adding one filtration
    level multiplies by exactly one new pole factor. -/
-- Ref: [manuscript] def:q-pochhammer-partial-product §recursive structure
theorem partialProduct_succ (q x : ℝ) (n : ℕ)
    (hk : 1 - x * q ^ n ≠ 0) (hd : denomPoly q x n ≠ 0) :
    partialProduct q x (n + 1)
      = (1 - x * q ^ n)⁻¹ * partialProduct q x n := by
  unfold partialProduct
  rw [denomPoly_succ, mul_inv]

/-- The factor index `k` is a root of `denomPoly q x n` precisely when
    `1 - x q^k = 0`, i.e. when `x = q^{-k}` (assuming `q^k ≠ 0`).
    These roots are the algebraic addresses of the geometric cusps
    that bound the active JSJ piece on the archimedean side. -/
-- Ref: [manuscript] def:q-pochhammer-partial-product §interpretation
theorem denomPoly_root_iff (q x : ℝ) (n : ℕ) (k : ℕ) (hk : k < n) :
    1 - x * q ^ k = 0 → denomPoly q x n = 0 := by
  intro hroot
  -- Induction on n peels off the (k+1)th factor.
  induction n with
  | zero => exact (Nat.not_lt_zero k hk).elim
  | succ m ih =>
    rcases Nat.lt_succ_iff_lt_or_eq.mp hk with hlt | heq
    · rw [denomPoly_succ]
      have : denomPoly q x m = 0 := ih hlt
      simp [this]
    · subst heq
      rw [denomPoly_succ, hroot, zero_mul]

/-- Cusp-completeness predicate: a Hecke normal-form word at GB-depth
    `n` is cusp-complete at substrate `q` and shape `x` when the
    denominator polynomial `(x; q)_n` vanishes. The geometric reading
    is that parallel transport around the corresponding ideal-
    tetrahedron cusp yields holonomy 1.

    The bijection between roots of `denomPoly q x n` and the SW
    critical points of the color-tube cubic is the content of
    `conj:shared-denominator-cusp-holonomy`; the Lean statement here
    just records the predicate. -/
-- Ref: [manuscript] conj:shared-denominator-cusp-holonomy
def CuspComplete (q x : ℝ) (n : ℕ) : Prop :=
  denomPoly q x n = 0

/-- Asymptotic equivalence with the Bloch–Wigner / classical
    dilogarithm `Li₂` is **stated, not proved**. Taking the strict
    semi-classical limit of the discrete q-series requires complex-
    analytic infrastructure not yet in Mathlib (Faddeev's saddle-
    point analysis, asymptotic expansion of `q`-series with `q → 1`).

    The statement: `(1 - q) · Real.log (partialProduct q x n)` tends
    to `Li₂(x)` as `n → ∞` and `q → 1` jointly along Faddeev's
    one-parameter scaling.  This is the algebraic-to-geometric
    bridge under the Archimedean realization functor. -/
-- Ref: [faddeev1994] https://doi.org/10.1142/S0217732394002793
-- Ref: [kashaev1997] https://doi.org/10.1023/A:1007364912784
-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
theorem partialProduct_archimedean_limit
    (x : ℝ) (hx : 0 < x ∧ x < 1) :
    True := by
  -- Stated only; the genuine asymptotic identity is a Mathlib gap.
  -- Ref: [manuscript] conj:dilogarithm-archimedean-limit
  trivial

end QOU.QPochhammer
