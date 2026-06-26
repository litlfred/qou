import Mathlib.Analysis.SpecialFunctions.Exp


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

- [manuscript] §9-information-theory/q-exponential-taylor

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
-- Ref: [manuscript] §9
def jacksonInt (q : ℝ) (n : ℕ) : ℝ :=
  if q = 1 then (n : ℝ)
  else (1 - q^n) / (1 - q)

/-- Jackson factorial [n]_q! = ∏_{k=1}^n [k]_q. -/
-- Ref: [manuscript] §9
def jacksonFactorial (q : ℝ) : ℕ → ℝ
  | 0 => 1
  | n + 1 => jacksonInt q (n + 1) * jacksonFactorial q n

/-- Formal Taylor series of the q-exponential. -/
-- Ref: [manuscript] §9
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
    `q`-analysis API and is an honest `sorry`. -/
-- Ref: [manuscript] §9-information-theory/q-exponential-taylor
theorem qExponentialTaylor (q : ℝ) (x : ℝ) (hq : 1 < q) :
    Summable (qExpSeries q x) := by
  -- Ratio test: the term ratio `qExpSeries q x (n+1) / qExpSeries q x n`
  -- equals `x / [n+1]_q`, and `[n+1]_q = (q^{n+1}−1)/(q−1) → ∞` for q > 1,
  -- so the ratio → 0 < 1 and `summable_of_ratio_norm_eventually_le` applies.
  -- Needs: Jackson-integer divergence lemma `Tendsto (jacksonInt q) atTop atTop`
  -- for q > 1 (not yet in the q-analysis API).
  -- Ref: [manuscript] §9-information-theory/q-exponential-taylor
  sorry

/-- At q = 1, the q-exponential Taylor series recovers the ordinary
    exponential. -/
-- Ref: [manuscript] §9
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
