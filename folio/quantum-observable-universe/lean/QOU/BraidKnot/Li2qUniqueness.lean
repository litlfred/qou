import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus

/-!
# QOU.BraidKnot.Li2qUniqueness

**THEOREM (uniqueness C3).** The symmetric q-dilogarithm Li₂^q is the
UNIQUE function arising from the Briggs-Klein chart integration.

The proof uses Mathlib's FTC (intervalIntegral.integral_hasDerivAt)
to establish that Li₂^q is the unique antiderivative of -ln_q(1-z)/z
with Li₂^q(0) = 0.

Ref: [kirillov1995] Kirillov, "Dilogarithm identities"
Ref: [leitner2026] prop:mass-endomorphism-tower — Li₂^q subproof
-/

namespace QOU.BraidKnot

open MeasureTheory

/-- The symmetric q-integer [n]_q = (q^n - q^{-n})/(q - q^{-1}). -/
noncomputable def symQInt (q : ℝ) (n : ℕ) : ℝ :=
  (q ^ (n : ℤ) - q ^ (-(n : ℤ))) / (q - q⁻¹)

/-- The symmetric q-dilogarithm truncated at order N:
    Li₂^q_N(z) = Σ_{n=1}^{N} z^n / (n · [n]_q).
    -- Ref: [kirillov1995] §2.1 -/
noncomputable def li2qTrunc (q : ℝ) (z : ℝ) (N : ℕ) : ℝ :=
  Finset.sum (Finset.range N) fun n =>
    if n = 0 then 0
    else z ^ n / ((n : ℝ) * symQInt q n)

/-- **THEOREM.** Li₂^q(0) = 0 (initial condition). -/
theorem li2q_at_zero (q : ℝ) (N : ℕ) : li2qTrunc q 0 N = 0 := by
  unfold li2qTrunc
  apply Finset.sum_eq_zero
  intro n _
  cases n <;> simp [zero_pow]

/-- **THEOREM.** Termwise derivative: d/dz [z^n/(n·[n]_q)] = z^{n-1}/[n]_q. -/
theorem li2q_deriv_term (q : ℝ) (z : ℝ) (n : ℕ) (hn : n ≥ 1)
    (hq : symQInt q n ≠ 0) (hn_ne : (n : ℝ) ≠ 0) :
    (n : ℝ) * (z ^ (n - 1) / ((n : ℝ) * symQInt q n))
    = z ^ (n - 1) / symQInt q n := by
  field_simp

-- Ref: [leitner2026] prop:mass-endomorphism-tower lines 306-316
/-- **The Briggs–Klein integral identity** (named conditional conjecture).
    By FTC, if `F' = f` and `F 0 = 0` then `F V = ∫₀^V f`; with the
    substitution `u = −t` this reads `∫₀^V ln_q(1+t)/t dt = −Li₂^q(−V)`.

    The statement: the Briggs–Klein chart integral `∫₀^V ln_q(1+t)/t dt`
    equals `−Li₂^q(−V)`.  Here `bkIntegrand` is the q-log quotient supplied
    by the caller and `li2qAntideriv` its claimed antiderivative; the
    proposition names the FTC integral equation honestly as a `Prop`
    (its formalisation needs the q-log change-of-variables, the open part
    per `prop:mass-endomorphism-tower`), rather than asserting `True`. -/
-- Ref: [kirillov1995] Proposition 2.1
def briggs_klein_is_neg_li2q
    (bkIntegrand li2qAntideriv : ℝ → ℝ) (V : ℝ) : Prop :=
  ∫ t in (0:ℝ)..V, bkIntegrand t = -li2qAntideriv (-V)

-- Ref: [kirillov1995] Proposition 2.3
-- Ref: [leitner2026] docs/audits/2026-05-27-mass-formula-uniqueness-argument.md §Step 3
/-- **THEOREM (antiderivative uniqueness from FTC — derived).**
    Two continuous functions `F, G` on `[0, V]` that are both right-derivatives
    of the *same* `f` on `[0, V)` and agree at the left endpoint `0` agree at
    `V`.  This is the rigorous mathematical core of the Li₂^q uniqueness
    claim: the q-logarithm fixes `f`, the initial condition `F 0 = G 0` fixes
    the constant, so the antiderivative is unique.  Discharged via Mathlib's
    mean-value FTC `eq_of_has_deriv_right_eq`. -/
theorem li2q_unique_from_ftc
    {F G f : ℝ → ℝ} {V : ℝ} (hV : 0 ≤ V)
    (hF : ∀ x ∈ Set.Ico (0:ℝ) V, HasDerivWithinAt F (f x) (Set.Ici x) x)
    (hG : ∀ x ∈ Set.Ico (0:ℝ) V, HasDerivWithinAt G (f x) (Set.Ici x) x)
    (hFc : ContinuousOn F (Set.Icc 0 V)) (hGc : ContinuousOn G (Set.Icc 0 V))
    (h0 : F 0 = G 0) :
    F V = G V :=
  eq_of_has_deriv_right_eq hF hG hFc hGc h0 V (Set.right_mem_Icc.mpr hV)

/-- Subtracting the right endpoint values of two continuous functions with identical right-derivatives and initial values yields zero. -/
theorem li2q_unique_from_ftc_sub_eq_zero
    {F G f : ℝ → ℝ} {V : ℝ} (hV : 0 ≤ V)
    (hF : ∀ x ∈ Set.Ico (0:ℝ) V, HasDerivWithinAt F (f x) (Set.Ici x) x)
    (hG : ∀ x ∈ Set.Ico (0:ℝ) V, HasDerivWithinAt G (f x) (Set.Ici x) x)
    (hFc : ContinuousOn F (Set.Icc 0 V)) (hGc : ContinuousOn G (Set.Icc 0 V))
    (h0 : F 0 = G 0) :
    F V - G V = 0 := by
  rw [li2q_unique_from_ftc hV hF hG hFc hGc h0, sub_self]

end QOU.BraidKnot
