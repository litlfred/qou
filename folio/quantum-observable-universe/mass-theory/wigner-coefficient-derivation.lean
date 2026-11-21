/-
  Wigner coefficient = [5]_q! · m_e from Frobenius reciprocity.

  Note: `Σ_λ dim_q(λ)² = [n]_q!` is FALSE for n ≥ 3
  (`QOU.MathlibExt.sum_qDim_sq_ne_qFactorial_n3_at_two`); the true identity
  carries a factor `q^{-κ_λ}` and `f^λ` (`molienSum_eq_qFactorial`). This
  header said the false form until 2026-11-21.

  Ref: [leitner2026] §5.7, prop:wigner-coefficient-derivation
-/

import QOU.Torsion.HeckeMassElement
import QOU.MathlibExt.QIntegerCanonical

namespace QOU.BraidKnot

/-- Quantum n-integer `[n]_q = (q^n − q^{-n}) / (q − q^{-1})`. -/
-- Consolidated onto the canonical q-integer (bean `qou-qint`): this was a
-- verbatim duplicate of `QOU.QInteger.qIntBal`.  Kept as a local `abbrev` so
-- every call site and proof below is unchanged, while the DEFINITION now has a
-- single home.  See QOU/MathlibExt/QIntegerCanonical.lean.
noncomputable abbrev qInt (n : ℕ) (q : ℝ) : ℝ := QOU.QInteger.qIntBal q n

/-- The quantum factorial [n]_q! = Π_{k=1}^n [k]_q. -/
noncomputable def qFactorial (n : ℕ) (q : ℝ) : ℝ :=
  Finset.prod (Finset.range n) (fun k => qInt (k + 1) q)

/-- The Wigner coefficient at level k is [k]_q! · m_e. -/
noncomputable def wignerCoefficient (k : ℕ) (q m_e : ℝ) : ℝ :=
  qFactorial k q * m_e

/-- **`[5]_q! · m_e` written out** (prop:wigner-coefficient-derivation).

    What this proves: the level-5 Wigner coefficient is the explicit product
    `[1]_q [2]_q [3]_q [4]_q [5]_q · m_e` displayed in the block. That is all.

    What it does not prove: that the Wigner term of the Bethe–Weizsäcker mass
    formula equals this coefficient. That identification is the content of
    `conj:q-integer-mass-formula` and is not formalised.

    Until 2026-11-21 this theorem asserted
    `|wignerCoefficient 5 q₀ m_e − 68.896| / 68.896 < 0.03` at
    `q₀ = 1.109978595554181` (the retired CODATA-2018 muon pin), discharged by
    an `axiom` carrying that bound. 68.896 MeV is a fitted liquid-drop
    coefficient, so the axiom put an empirical comparison inside a formal
    result (round-trip audit pass 2, C12; bean `qou-wg3c`). Axiom and bound
    are deleted. -/
-- Ref: [leitner2026] Ch. mass-theory, prop:wigner-coefficient-derivation
theorem wigner_coefficient (q m_e : ℝ) :
    wignerCoefficient 5 q m_e =
      qInt 1 q * qInt 2 q * qInt 3 q * qInt 4 q * qInt 5 q * m_e := by
  unfold wignerCoefficient qFactorial
  rw [Finset.prod_range_succ, Finset.prod_range_succ, Finset.prod_range_succ,
    Finset.prod_range_succ, Finset.prod_range_succ, Finset.prod_range_zero, one_mul]

end QOU.BraidKnot


/-! ## §3b-cond conditional-class hypothesis -/

namespace QOU.BraidKnot.WignerCoefficient.ConditionalAudit

/-- **§3b-cond hypothesis class** for `conj:q-integer-mass-formula`.

    The empirical Bethe–Weizsäcker liquid-drop coefficients
    (`λ_V, λ_S, λ_C, a_asym, …`) are each a product of quantum integers
    `[n]_q = (q^n − q^{-n})/(q − q^{-1})` evaluated at the substrate
    parameter `q₀`, times the electron mass `m_e` — i.e. each empirical
    coefficient equals a substrate-derived algebraic `q`-rational
    multiple of `m_e`, not a free fit parameter.

    Concrete content (shape of the claim): for every empirical
    coefficient `c` (indexed by `ℕ`) there is a non-negative
    `q`-rational ratio `r` with `c = r · m_e`. -/
-- Ref: [leitner2026] conj:q-integer-mass-formula
class QIntegerMassFormula : Prop where
  /-- Each liquid-drop coefficient is `m_e` scaled by a non-negative
      substrate-derived `q`-rational ratio (existence of the ratio
      family is the conjectural input). -/
  coeffs_are_q_rational :
    ∀ (m_e : ℝ), 0 ≤ m_e → ∀ _c : ℕ, ∃ r : ℝ, 0 ≤ r ∧ ∃ value : ℝ, value = r * m_e

/-- **Conditional on `conj:q-integer-mass-formula`.** For a
    non-negative electron-mass scale, every liquid-drop coefficient is
    a non-negative multiple of `m_e` (so all are non-negative). Derived
    from the class field, not assumed. -/
theorem wigner_coefficient_conditional [inst : QIntegerMassFormula]
    (m_e : ℝ) (hme : 0 ≤ m_e) :
    ∀ c : ℕ, ∃ value : ℝ, 0 ≤ value := by
  intro c
  obtain ⟨r, hr, value, hval⟩ := inst.coeffs_are_q_rational m_e hme c
  exact ⟨value, by rw [hval]; exact mul_nonneg hr hme⟩

end QOU.BraidKnot.WignerCoefficient.ConditionalAudit
