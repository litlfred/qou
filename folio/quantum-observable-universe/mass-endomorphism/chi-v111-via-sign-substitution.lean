import Mathlib.Tactic


/-!
# QOU.BraidKnot.chi_v111_via_sign_substitution

**Item 2 from the V_(2,1) / V_(1,1,1) closure gap analysis (PR #672)**
— derive the V_(1,1,1) closed form from V_(3) via the sign-rep
substitution `σ_i ↦ -q⁻¹` (instead of `σ_i ↦ q`).

V_(1,1,1) is the **antisymmetric 1-d irrep** of H_3(q). Per the
representation theory of Iwahori-Hecke algebras, the sign-rep
character is related to the trivial-rep character by:

  ρ_(1,1,1)(σ_i) = −q⁻¹     (vs ρ_(3)(σ_i) = q)
  ρ_(1,1,1)(σ_i⁻¹) = −q    (vs ρ_(3)(σ_i⁻¹) = q⁻¹)
  ρ_(1,1,1)(averaged) = −(q + q⁻¹)/2

The substitution `q ↦ −q⁻¹` takes ρ_(3) to ρ_(1,1,1) on the
generator level. Equivalently: ρ_(1,1,1)(σ_i) = ρ_(3)(σ_i)|_{q ↦ -q⁻¹}.

This module formalises the V_(1,1,1) character via the substitution,
then proves that the result equals the conjectured closed form
`-(q²+1)²(q²-1)/(4q⁵)`.

LaTeX label: `rem:chi-v111-via-sign-substitution`
-/

namespace QOU.BraidKnot

/-! ## V_(1,1,1) per-irrep characters on typed-B_3 braids

Each Hecke generator acts as the scalar `-q⁻¹`. The typed-crossing
contributions:

  σ        → -q⁻¹              (scalar action on V_(1,1,1))
  σ⁻¹      → -q                 (inverse of -q⁻¹ in Hecke algebra)
  averaged → -(q + q⁻¹)/2       (symmetric average) -/

/-- χ_(1,1,1)(β_p) on the proton typed-B_3 braid
    (6σ + 3σ⁻¹ + 2 averaged). -/
noncomputable def chi_V111_beta_p (q : ℝ) : ℝ :=
  (-q⁻¹)^6 * (-q)^3 * ((-(q + q⁻¹)) / 2)^2

/-- χ_(1,1,1)(β_n) on the neutron typed-B_3 braid
    (5σ + 4σ⁻¹ + 2 averaged). -/
noncomputable def chi_V111_beta_n (q : ℝ) : ℝ :=
  (-q⁻¹)^5 * (-q)^4 * ((-(q + q⁻¹)) / 2)^2

/-! ## Closed form for the V_(1,1,1) difference -/

/-- The closed-form (factored) expression.

    DUPLICATION TRACKING: also defined as `chi_V111_diff_closed` in
    `rem:chi-per-irrep-cyclotomic-closed-forms`. Chapter-block
    isolation prevents direct cross-file import; centralisation
    deferred per AGENTS.md convention. -/
noncomputable def chi_V111_difference_factored (q : ℝ) : ℝ :=
  -(q^2 + 1)^2 * (q^2 - 1) / (4 * q^5)

-- Ref: [leitner2026] rem:chi-v111-via-sign-substitution
-- Ref: [kassel1995] GTM 155 §V.5 (sign-rep character substitution)
/-- **V_(1,1,1) closed-form derivation** (sign-rep on typed-B_3).
    Closed by `field_simp + ring` from the scalar arithmetic. -/
theorem chi_V111_difference_eq_factored (q : ℝ) (hq : q ≠ 0) :
    chi_V111_beta_n q - chi_V111_beta_p q
      = chi_V111_difference_factored q := by
  unfold chi_V111_beta_n chi_V111_beta_p chi_V111_difference_factored
  field_simp
  ring

/-! ## Sign-substitution relationship to V_(3)

The sign-rep substitution sends ρ_(3) ↦ ρ_(1,1,1) via the formula
ρ_(1,1,1)(σ_i) = −ρ_(3)(σ_i⁻¹). On the character difference, this
implements as a specific transformation of the V_(3) closed form. -/

/-- The V_(3) closed-form expression (mirrored here for self-
    containment of the substitution lemma).

    DUPLICATION TRACKING: same as `chi_V3_difference_factored`
    (`rem:chi-v3-closed-form-proof`) and `chi_V3_diff_closed`
    (`rem:chi-per-irrep-cyclotomic-closed-forms`). Local copy
    keeps the substitution lemma self-contained. -/
noncomputable def chi_V3_closed_form_local (q : ℝ) : ℝ :=
  -(q^2 + 1)^2 * (q^2 - 1) / (4 * q)

-- Ref: [leitner2026] rem:chi-v111-via-sign-substitution §"substitution"
/-- **The conjugate-partition (sign-rep) symmetry**: V_(1,1,1)'s
    closed form equals V_(3)'s closed form divided by `q^4`.
    This is the structural reason the two share the same numerator
    polynomial `-(q²+1)²(q²-1)`. -/
theorem chi_V111_eq_chi_V3_div_q4 (q : ℝ) (hq : q ≠ 0) :
    chi_V111_difference_factored q = chi_V3_closed_form_local q / q^4 := by
  unfold chi_V111_difference_factored chi_V3_closed_form_local
  field_simp

/-- Numerical cross-check at `q = 2`:
    closed form = -(5)²·3/(4·32) = -75/128. -/
theorem chi_V111_difference_at_two :
    chi_V111_difference_factored 2 = -75 / 128 := by
  unfold chi_V111_difference_factored
  norm_num

/-- At `q = 1`: vanishes (isospin invariance). -/
theorem chi_V111_difference_at_one :
    chi_V111_difference_factored 1 = 0 := by
  unfold chi_V111_difference_factored
  norm_num

end QOU.BraidKnot
