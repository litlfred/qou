/-
# The balanced family's theta limit — the `E`-shifted recentring, and the exact
# sense in which the `A_w` machinery does (and does not) transfer

The KSel-2-ID chain closed the **SW core** leg: the Stieltjes–Wigert core's
Nevanlinna denominator is `D_SW(z) = c₀ z A_w(z)` with `w = q̃⁻¹`, and
`AwZeroLocalization` formalises the algebraic core of the theta-limit Rouché
argument that localises its zeros at `w^{1−2n}` (`docs/audits/2026-08-01-awzero-asymptotics.md`).

What was still owed is the **balanced** leg: the balanced moment problem
`m_k = q̃^{k(k−1)/2} (p;p)_k E^k` (`SWJacksonMomentFactorization`) has its own
Nevanlinna denominator `D_bal(z) = z Σ_n p_n(0) p_n(z)`, whose zeros are the
Krein extremal support.  The claim "balanced extremal class = φ₁ = frac(log_q̃ E)"
was *measured*, not derived.

This module formalises the **exact algebra** of the transfer, which is the
part that is genuinely proved (`docs/audits/2026-08-01-balanced-theta-limit.md`):

* writing the balanced Taylor coefficients in the normalised form
  `d_j = d₀ (−1)^j E^{−j} w^{j²} g_j`, the substitution `z = E w^{1−2n} u`
  — the **`E`-shifted recentring** — makes the factor `E` cancel *identically*,
  leaving precisely the SW recentred series with `1/(w;w)_{n+k}` replaced by
  `g_{n+k}` (`balanced_E_absorption`);
* the recentred summand's exponent is the **same** Gaussian `k(k+1)` as in the
  SW core, and it is a Jacobi-triple-product index at base `w²` — so the theta
  limit, hence the candidate zero lattice `u ∈ w^{2ℤ}`, is the **same** object
  (`theta_index_base_change`, `defect_index_base_change`);
* the balanced coefficient ratios (the tropical / Newton-polygon corners of
  `D_bal`) are `E w^{−(2j+1)} g_j / g_{j+1}` (`balanced_dcoef_ratio`,
  division-free, generic `CommRing`);
* the `E`-shifted lattice `E v^{2n−1}` has `log_v`-class exactly `frac(log_v E)`,
  i.e. φ₁ (`logClass_E_shift`, `fract_logClass_E_shift`) — the class arithmetic of the
  target statement, over `ℝ`;
* the SW normaliser `Ψ_SW(x) = (wx;w)_∞` **vanishes at every negative index**
  `x = (w^m)⁻¹`, `m ≥ 1` (`swPsi_zero_at_inv_pow`) — the structural fact that
  lets the SW defect expansion run over all `k ∈ ℤ`, and precisely the property
  whose balanced analogue is NOT known.

NOT proved here, and explicitly NOT claimed: that the balanced normaliser
`g_m` converges; that `g_m = g_∞ Ψ(w^m)` for an analytic `Ψ` (hypothesis (H) of
the audit — *measured*, at high precision and overdetermined, but not derived);
that `Ψ_bal` is entire or vanishes on the negative-index lattice; the Jacobi
triple product itself; Rouché / the argument principle; any value of `n₀`; and
anything about the target conjecture.  Nothing here is wired to production.

Base ring (§7c): everything algebraic is stated over a generic `[CommRing K]`
or `[Field K]` (the content is rational q-shift bookkeeping).  Only the class
arithmetic is archimedean and lives over `ℝ`.

-- Ref: [leitner2026] docs/audits/2026-08-01-balanced-theta-limit.md;
--      docs/audits/2026-08-01-awzero-asymptotics.md;
--      docs/audits/2026-08-01-ksel2id-tropical-transport.md §3;
--      docs/audits/2026-08-01-ksel2id-friedrichs-sw-identification.md §1;
--      bean qou-r4ya.
-/

import Mathlib.Algebra.BigOperators.Field
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Algebra.Order.Round
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace QOU.Archimedean.BalancedThetaLimit

open Finset

/-! ## 1.  The `E`-shifted recentring: `E` cancels identically

The balanced Taylor coefficients of `D_bal(z)/z` have the normalised shape

    d_j = d₀ · (−1)^j · E^{−j} · w^{j²} · g_j ,      w = q̃⁻¹,

where `g_j` is the balanced normaliser (`g_j = 1/(w;w)_j` recovers the SW core).
The recentring substitution is `z = E w^{1−2n} u`: the `E` in the substitution
is exactly the `E^{−j}` in the coefficient, so the two cancel for *every* `j`,
and what is left is the SW recentring `j² + (1−2n)j = (n−n²) + k(k+1)`,
`k = j − n`.  This is the precise sense in which the `E`-shift is absorbed by
the recentring rather than deforming it. -/

/-- The exponent bookkeeping: `j² + (1−2n)j = (n − n²) + (j−n)(j−n+1)`.
Identical to the SW core's `recentring_exponent`; recorded here because it is
the exponent that survives the `E`-cancellation. -/
theorem recentring_exponent (j n : ℤ) :
    j ^ 2 + (1 - 2 * n) * j = (n - n ^ 2) + (j - n) * (j - n + 1) := by
  ring

/-- **The `E`-absorption.**  With `Ei` the inverse scale (`Ei = E⁻¹`), the
`j`-th normalised monomial of `D_bal` evaluated at the `E`-shifted recentring
point `z = E w^{1−2n} u` is exactly the SW recentred monomial:

    Ei^j · w^{j²} · (Ei⁻¹ · w^{1−2n})^j = w^{n−n²} · w^{(j−n)(j−n+1)} .

The `E`-dependence cancels identically — for every `j`, not asymptotically. -/
theorem balanced_E_absorption {K : Type*} [Field K] {Ei w : K} (hE : Ei ≠ 0)
    (hw : w ≠ 0) (j n : ℤ) :
    Ei ^ j * w ^ (j ^ 2) * (Ei⁻¹ * w ^ (1 - 2 * n)) ^ j
      = w ^ (n - n ^ 2) * w ^ ((j - n) * (j - n + 1)) := by
  have hEj : (Ei : K) ^ j ≠ 0 := zpow_ne_zero _ hE
  have h1 : Ei ^ j * w ^ (j ^ 2) * (Ei⁻¹ * w ^ (1 - 2 * n)) ^ j
      = (Ei ^ j * (Ei ^ j)⁻¹) * w ^ (j ^ 2 + (1 - 2 * n) * j) := by
    rw [mul_zpow, inv_zpow, ← zpow_mul, zpow_add₀ hw]
    ring
  rw [h1, mul_inv_cancel₀ hEj, one_mul, ← zpow_add₀ hw]
  congr 1
  ring

/-! ## 2.  The theta limit is the *same* theta: Jacobi-triple-product indices -/

/-- The recentred summand carries the exponent `k(k+1)`, which is a
Jacobi-triple-product index **at base `w²`**: `k(k+1) = k(k−1) + 2k`.  So the
limit `Σ_{k∈ℤ} (−1)^k w^{k(k+1)} u^k` is the theta function at base `p = w²`
with argument `w² u`, whose zero set is `u ∈ w^{2ℤ}` — the balanced tropical
lattice.  This is *the same theta function* as in the SW core; only the
prefactor (`g_∞` in place of `1/(w;w)_∞`) differs. -/
theorem theta_index_base_change (k : ℤ) : k * (k + 1) = k * (k - 1) + 2 * k := by
  ring

/-- The `j`-th defect term of the SW argument carries the exponent
`k(k+1) + jk`, again a triple-product index at base `w²`, now with argument
`w^{j+2} u`: `k(k+1) + j·k = k(k−1) + (j+2)·k`.  Under hypothesis (H) of the
audit the balanced defect has *literally this* expansion, with the SW
coefficients `(−1)^{j+1} w^{j(j+1)/2}/(w;w)_j` replaced by the Taylor
coefficients of the balanced normaliser. -/
theorem defect_index_base_change (j k : ℤ) :
    k * (k + 1) + j * k = k * (k - 1) + (j + 2) * k := by
  ring

/-! ## 3.  The balanced tropical (Newton-polygon) corners -/

/-- The normalised balanced Taylor coefficient
`d_j = d₀ (−1)^j Ei^j w^{j²} g_j` (with `Ei = E⁻¹`). -/
def dcoef {K : Type*} [CommRing K] (d₀ Ei w : K) (g : ℕ → K) (j : ℕ) : K :=
  d₀ * (-1) ^ j * Ei ^ j * w ^ (j ^ 2) * g j

/-- **The balanced coefficient ratio, division-free.**  Equivalent to
`−d_j / d_{j+1} = E · w^{−(2j+1)} · g_j / g_{j+1}`: the `j`-th tropical corner
of `D_bal` is `E w^{−(2j+1)}` times the normaliser ratio.  With `w = q̃⁻¹` the
corner is `E q̃^{2j+1} (g_j/g_{j+1})`, so — once `g_j/g_{j+1} → 1` — the corners
lie on the `E`-shifted `q`-lattice whose `log_q̃`-class is `frac(log_q̃ E) = φ₁`
(§4).  Stated over a generic `CommRing`; no inverses appear. -/
theorem balanced_dcoef_ratio {K : Type*} [CommRing K] (d₀ Ei w : K)
    (g : ℕ → K) (j : ℕ) :
    dcoef d₀ Ei w g j * (w ^ (2 * j + 1) * g (j + 1) * Ei)
      + dcoef d₀ Ei w g (j + 1) * g j = 0 := by
  have hpow : w ^ ((j + 1) ^ 2) = w ^ (j ^ 2) * w ^ (2 * j + 1) := by
    rw [← pow_add]
    congr 1
    ring
  simp only [dcoef]
  rw [hpow, pow_succ (-1 : K) j, pow_succ Ei j]
  ring

/-! ## 4.  The class arithmetic of the `E`-shifted lattice (archimedean, `ℝ`) -/

/-- The `log_v`-class coordinate, written with `Real.log` (this is `Real.logb v x`;
spelled out so the module does not need the `Logb` import). -/
noncomputable def logClass (v x : ℝ) : ℝ := Real.log x / Real.log v

/-- `log_v (E · v^m) = m + log_v E` for `v > 1`, `E > 0`, `m : ℤ`. -/
theorem logClass_E_shift {v E : ℝ} (hv : 1 < v) (hE : 0 < E) (m : ℤ) :
    logClass v (E * v ^ m) = m + logClass v E := by
  have hv0 : (0:ℝ) < v := lt_trans zero_lt_one hv
  have hlv : Real.log v ≠ 0 := ne_of_gt (Real.log_pos hv)
  rw [logClass, logClass, Real.log_mul (ne_of_gt hE) (zpow_ne_zero _ (ne_of_gt hv0)),
    Real.log_zpow]
  field_simp
  ring

/-- **The class statement.**  The fractional part of `log_v` of any point of the
`E`-shifted lattice `E v^m` is exactly `frac(log_v E)` — the class φ₁.  This is
the arithmetic content of "the balanced tropical class is φ₁": the integer part
of the lattice index drops out, for every `m : ℤ`.  Combined with
`balanced_dcoef_ratio`, it says the balanced `D`-function's tropical corners
carry class φ₁ exactly once the normaliser ratio tends to 1. -/
theorem fract_logClass_E_shift {v E : ℝ} (hv : 1 < v) (hE : 0 < E) (m : ℤ) :
    Int.fract (logClass v (E * v ^ m)) = Int.fract (logClass v E) := by
  rw [logClass_E_shift hv hE m]
  exact Int.fract_intCast_add _ _

/-! ## 5.  What the SW normaliser has and the balanced one is not known to have

The SW defect expansion runs over **all** `k ∈ ℤ`, not merely `k ≥ −n`, because
the SW normaliser `g_m = 1/(w;w)_m` is `g_∞ · Ψ_SW(w^m)` with
`Ψ_SW(x) = (w x; w)_∞` an ENTIRE function that **vanishes at every negative
index** `x = (w^m)⁻¹`, `m ≥ 1`.  That is exactly the convention `g_m = 0` for
`m < 0`, realised analytically — and it is what lets the SW argument treat the
truncated series as a full bilateral theta series.

The balanced normaliser's analytic continuation `Ψ_bal` is measured to exist
(hypothesis (H) of the audit) but is *not* known to be entire, and the
numerically-extracted Taylor coefficients decay slower than the SW ones.  This
is the precise residual: the finite-order statement below is the SW half of a
contrast, not a balanced result. -/

/-- `Ψ_SW(x) = ∏_{i<N} (1 − w^{i+1} x)` vanishes at `x = (w^m)⁻¹` whenever
`1 ≤ m ≤ N`: the SW normaliser's continuation kills every negative index. -/
theorem swPsi_zero_at_inv_pow {K : Type*} [Field K] {w : K} (hw : w ≠ 0) {m N : ℕ}
    (hm : 1 ≤ m) (hmN : m ≤ N) :
    ∏ i ∈ range N, (1 - w ^ (i + 1) * (w ^ m)⁻¹) = 0 := by
  refine Finset.prod_eq_zero (i := m - 1) (mem_range.2 ?_) ?_
  · omega
  · have hmm : m - 1 + 1 = m := by omega
    rw [hmm, mul_inv_cancel₀ (pow_ne_zero _ hw), sub_self]

end QOU.Archimedean.BalancedThetaLimit
