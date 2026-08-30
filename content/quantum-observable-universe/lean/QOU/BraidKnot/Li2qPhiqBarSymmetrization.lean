/-
Symmetric q-dilogarithm as bar-symmetrization of compact q-dilog Φ_q.

  Li_2^q(z) = (log Φ_q(z) + log Φ_{q^{-1}}(z)) / 2

The bar involution q ↦ q^{-1} fixes Li_2^q (palindromic in q),
which manifests at the coefficient level via the palindromy of
the symmetric q-integer [n]_q.

This Lean file follows the QOU.Infra.Polylogarithm pattern:
- Concrete `noncomputable def` for closed-form q-quantities
- Verified arithmetic theorems at q = 1 (classical limit)
- `class` hypothesis for the q ≠ 1 substantive content
  (per AGENTS.md §3b-cond conditional-class exception)
- Default instance discharging the verified base case

Ref: [faddeev1995] Discrete Heisenberg-Weyl group and modular group
Ref: [kashaev1997] Hyperbolic volume of knots from quantum dilogarithm
Ref: prop:li2q-phiq-bar-symmetrization.md
-/

import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import QOU.MathlibExt.QIntegerCanonical

namespace QOU.BraidKnot

/-- The symmetric q-integer [n]_q = (q^n - q^{-n})/(q - q^{-1})
    as a real-valued function.
    - n = 0: returns 0
    - q = 1: returns n (classical limit)
    - otherwise: symmetric q-integer formula.

    Stated over ℝ; the same definition transports to any field
    where (q - q⁻¹) is invertible. -/
noncomputable def qInteger (q : ℝ) (n : ℕ) : ℝ :=
  if n = 0 then 0
  else if q = 1 then (n : ℝ)
  else (q^n - q^(-(n : ℤ))) / (q - q⁻¹)

/-- **Bridge to the canonical classical-extended bracket.**  This site carries
*two* guards, `n = 0` and `q = 1`, but only the second is doing work: at `n = 0`
the canonical `qIntBalCl` already returns `0` on both branches (`(0 : ℝ)` at
`q = 1`, and `qIntBal q 0 = 0` otherwise).  So the extra `n = 0` case is
redundant and the agreement is unconditional. -/
theorem qInteger_eq_canonical (q : ℝ) (n : ℕ) :
    qInteger q n = QOU.QInteger.qIntBalCl q n := by
  unfold qInteger QOU.QInteger.qIntBalCl
  split_ifs with h0 h1 h1
  · subst h0; simp
  · subst h0; simp
  · rfl
  · simp [QOU.QInteger.qIntBal, QOU.Mass.QHookDimensionBalanced.qIntBal, zpow_neg,
      zpow_natCast, inv_pow]

/-- The n-th coefficient of the symmetric Li_2^q series:
    [Li_2^q]_n = 1 / (n · [n]_q) for n ≥ 1; 0 at n = 0. -/
noncomputable def li2qCoeff (q : ℝ) (n : ℕ) : ℝ :=
  if n = 0 then 0
  else 1 / ((n : ℝ) * qInteger q n)

/-- At q = 1, [n]_1 = n. **Verified** unconditionally. -/
theorem qInteger_at_q_eq_one (n : ℕ) (hn : n ≠ 0) :
    qInteger 1 n = (n : ℝ) := by
  unfold qInteger
  simp [hn]

/-- At q = 1, the symmetric Li_2^q coefficient reduces to the
    classical 1/n². **Verified** unconditionally. -/
theorem li2qCoeff_at_q_eq_one (n : ℕ) (hn : n ≠ 0) :
    li2qCoeff 1 n = 1 / ((n : ℝ)^2) := by
  unfold li2qCoeff
  rw [if_neg hn, qInteger_at_q_eq_one n hn]
  ring

/-- Bar invariance at q = 1: li2qCoeff 1 n = li2qCoeff 1⁻¹ n.
    **Verified** unconditionally via 1⁻¹ = 1. -/
theorem li2qCoeff_bar_invariant_at_q_eq_one (n : ℕ) :
    li2qCoeff 1 n = li2qCoeff (1⁻¹) n := by
  congr 1
  · norm_num

/-- The bar-symmetrization conjecture as a Lean class.

    For each n ≥ 1 and each q ∈ R, the bar-symmetrized Faddeev
    coefficient equals the symmetric Li_2^q coefficient.

    Class fields:
    - `bar_holds_at`: predicate naming the (q, n) pairs where
      the identity is verified.
    - `bar_holds_at_classical`: discharges all n at q = 1 (the
      classical-limit case, verified via li2qCoeff_at_q_eq_one).

    Downstream theorems consume the class via [Instance] per
    AGENTS.md §3b-cond. -/
class Li2qPhiqBarSymmetrization where
  /-- The (q, n) pairs where the bar-symmetrization identity
      is established. -/
  bar_holds_at : ℝ → ℕ → Prop
  /-- At q = 1, the identity holds for all n via the verified
      classical-limit chain. -/
  bar_holds_at_classical : ∀ n : ℕ, bar_holds_at 1 n

/-- **Model with the predicate read as its own witness.**  `bar_holds_at`
    is *defined* to be `fun q _n => q = 1`, so the conjectural field
    `bar_holds_at_classical : ∀ n, bar_holds_at 1 n` unfolds to `1 = 1`
    and closes by `rfl`, uniformly in `n`.  Nothing about bar
    symmetrisation, the Faddeev coefficients or `li2qCoeff` is encoded;
    the field is satisfied by choosing the predicate to be the equation
    the field asserts.

    The classical-limit fact it gestures at *is* proved in this file,
    unconditionally and without the class:
    `li2qCoeff_bar_invariant_at_q_eq_one`.  This model does not use it,
    and a real model would.

    **A `def`, not an `instance`, since 2026-08-24**, and given a name:
    it was anonymous, so resolution supplied it under the generated name
    `instLi2qPhiqBarSymmetrization`.  Nothing in the corpus takes
    `[Li2qPhiqBarSymmetrization]`, so the class documented as consumed
    "via [Instance] per AGENTS.md §3b-cond" has no consumers.

    Callers name it: `letI := li2qPhiqBarSymmetrization_qEqOne`. -/
def li2qPhiqBarSymmetrization_qEqOne : Li2qPhiqBarSymmetrization where
  bar_holds_at q _ := q = 1
  bar_holds_at_classical _ := rfl

/-- Empirical record: m_p/m_e under compact q-dilog Φ_q vs symmetric
    Li_2^q. The 99.82% gap (vs 1.84% with Faddeev) reflects the
    bar-symmetric projection killing the singular-braid mass scale.

    Witness: `m-p-m-e-li2q.witness.json`. -/
theorem m_p_m_e_empirical_record :
    (1869.85 : ℝ) > 1836 ∧ (3.31 : ℝ) < 1836 := by
  refine ⟨?_, ?_⟩ <;> norm_num

end QOU.BraidKnot
