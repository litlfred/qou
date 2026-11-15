import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecificLimits.Normed
import QOU.MathlibExt.QIntegerCanonical


/-!
# QOU.qExponentialTaylor — archimedean Taylor series of e_q

Over any field of characteristic zero where the Jackson factorials
[n]_q! are invertible, the categorical grouplike e_q is represented
by the convergent series

  e_q(x) = Σ_{n ≥ 0} x^n / [n]_q!.

Derivation: power-series ansatz, apply D_q(x^n) = [n]_q x^{n-1} to
the defining equation D_q e_q = e_q, get recursion a_{n+1} = a_n/[n+1]_q.

LaTeX label: `prop:q-exponential-taylor`

## References

- [leitner2026] §9-information-theory/q-exponential-taylor

**Char 0 only.**  The series has denominators [n]_q!, which can vanish
in characteristic p.  The categorical `QExponential` structure is
defined abstractly in any base ring; this proposition is the
archimedean realisation.
-/

namespace QOU

noncomputable section
open scoped Classical

/-- Jackson integer [n]_q = (1 - q^n) / (1 - q) over a characteristic-zero
    field where q ≠ 1. -/
-- Ref: [leitner2026] §9
def jacksonInt (q : ℝ) (n : ℕ) : ℝ :=
  if q = 1 then (n : ℝ)
  else (1 - q^n) / (1 - q)

/-- **Bridge to the canonical guarded geometric bracket.**

`jacksonInt` is kept rather than aliased: downstream proofs rewrite with the
closed form `(1−qⁿ)/(1−q)` syntactically, and swapping the body for
`qIntGeoCl`'s `Finset.sum` breaks them. The two orientations differ only by
negating numerator and denominator, so the definitions agree — proved here
rather than asserted. -/
theorem jacksonInt_eq_canonical (q : ℝ) (n : ℕ) :
    jacksonInt q n = QOU.QInteger.qIntGeoCl q n := by
  unfold jacksonInt
  by_cases h : q = 1
  · simp [h]
  · rw [if_neg h, QOU.QInteger.qIntGeoCl_eq_closed_form h,
      show (1 - q ^ n) = -(q ^ n - 1) by ring, show (1 - q) = -(q - 1) by ring,
      neg_div_neg_eq]

/-- Jackson factorial [n]_q! = ∏_{k=1}^n [k]_q. -/
-- Ref: [leitner2026] §9
def jacksonFactorial (q : ℝ) : ℕ → ℝ
  | 0 => 1
  | n + 1 => jacksonInt q (n + 1) * jacksonFactorial q n

/-- Formal Taylor series of the q-exponential. -/
-- Ref: [leitner2026] §9
noncomputable def qExpSeries (q : ℝ) (x : ℝ) : ℕ → ℝ :=
  fun n => x^n / jacksonFactorial q n

/-- **Taylor series of e_q (substrate regime `q > 1`):** for `q > 1` the
    q-exponential series `Σ xⁿ/[n]_q!` is summable for every `x ∈ ℝ`.
    The Jackson factorials grow super-geometrically
    (`[n+1]_q / [n]_q = (q^{n+1}−1)/(q^n−1) → q > 1`), so the ratio test
    gives radius of convergence `∞`.

    **Regime correction (2026-06-26).** The previous encoding asserted
    summability for *all* `q ≠ 1` via an `axiom qExponentialTaylor_axiom`.
    That statement is **false**: for `0 < q < 1` one has `[k]_q → 1/(1−q)`,
    so `[n]_q!` grows only geometrically and the series has *finite* radius
    `1/(1−q)` — not summable for `|x| > 1/(1−q)`. Asserting the general
    statement as an axiom was therefore unsound; the axiom is removed and
    the proposition is restated in the substrate regime `q > 1`
    (`q₀ ≈ 1.11`), where the "convergent for all `x`" claim of the
    manuscript genuinely holds. The convergence proof itself (ratio test
    via the Jackson-integer divergence `[n]_q → ∞`) awaits the
    `q`-analysis API.  Proved below directly: the Jackson-integer
    divergence `[n+1]_q = (q^{n+1}−1)/(q−1) → ∞` (from `q^n → ∞` for
    `q > 1`) drives the ratio test. -/
-- Ref: [leitner2026] §9-information-theory/q-exponential-taylor
theorem qExponentialTaylor (q : ℝ) (x : ℝ) (hq : 1 < q) :
    Summable (qExpSeries q x) := by
  -- Ratio test: `qExpSeries q x (n+1) = (x / [n+1]_q) · qExpSeries q x n`,
  -- and `[n+1]_q = (q^{n+1}−1)/(q−1) → ∞` for `q > 1`, so the term ratio
  -- `|x|/[n+1]_q ≤ 1/2` eventually and `summable_of_ratio_norm_eventually_le`
  -- applies.
  -- Ref: [leitner2026] §9-information-theory/q-exponential-taylor
  -- Jackson-integer divergence: `[n+1]_q → ∞`.
  have hji : Filter.Tendsto (fun n : ℕ => jacksonInt q (n + 1))
      Filter.atTop Filter.atTop := by
    have hform : ∀ n : ℕ, jacksonInt q (n + 1) = (q ^ (n + 1) - 1) / (q - 1) := by
      intro n
      rw [jacksonInt, if_neg hq.ne',
        show (1 : ℝ) - q ^ (n + 1) = -(q ^ (n + 1) - 1) by ring,
        show (1 : ℝ) - q = -(q - 1) by ring, neg_div_neg_eq]
    rw [Filter.tendsto_congr hform]
    have hpow : Filter.Tendsto (fun n : ℕ => q ^ (n + 1)) Filter.atTop Filter.atTop := by
      simpa using (tendsto_pow_atTop_atTop_of_one_lt hq).comp (Filter.tendsto_add_atTop_nat 1)
    have hsub : Filter.Tendsto (fun n : ℕ => q ^ (n + 1) - 1) Filter.atTop Filter.atTop := by
      simpa [sub_eq_add_neg] using
        Filter.tendsto_atTop_add_const_right Filter.atTop (-1 : ℝ) hpow
    exact hsub.atTop_div_const (by linarith : (0 : ℝ) < q - 1)
  refine summable_of_ratio_norm_eventually_le (r := 1 / 2) (by norm_num) ?_
  filter_upwards [hji.eventually_ge_atTop (2 * |x| + 1)] with n hn
  -- `hn : 2·|x| + 1 ≤ [n+1]_q`
  have hJpos : 0 < jacksonInt q (n + 1) := by
    linarith [abs_nonneg x]
  have hstep : qExpSeries q x (n + 1)
      = (x / jacksonInt q (n + 1)) * qExpSeries q x n := by
    simp only [qExpSeries, jacksonFactorial]
    ring
  rw [hstep, norm_mul]
  refine mul_le_mul_of_nonneg_right ?_ (norm_nonneg _)
  rw [norm_div, Real.norm_eq_abs, Real.norm_eq_abs, abs_of_pos hJpos, div_le_iff₀ hJpos]
  linarith [abs_nonneg x]

/-- At q = 1, the q-exponential Taylor series recovers the ordinary
    exponential. -/
-- Ref: [leitner2026] §9
theorem qExpSeries_classical_limit :
    jacksonFactorial 1 = fun n => (n.factorial : ℝ) := by
  funext n
  induction n with
  | zero => simp [jacksonFactorial]
  | succ n ih =>
    -- jacksonFactorial 1 (n+1) = jacksonInt 1 (n+1) * jacksonFactorial 1 n
    -- jacksonInt 1 (n+1) = (n+1 : ℝ) since the if-condition is true
    -- jacksonFactorial 1 n = (n.factorial : ℝ) by IH
    -- Combined: (n+1) * n! = (n+1)!
    show jacksonInt 1 (n + 1) * jacksonFactorial 1 n
        = (((n + 1).factorial : ℕ) : ℝ)
    rw [jacksonInt, if_pos rfl, ih, Nat.factorial_succ]
    push_cast
    ring

end

end QOU
