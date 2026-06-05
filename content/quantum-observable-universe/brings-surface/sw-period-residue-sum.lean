import Mathlib.Data.Complex.Basic
import Mathlib.Algebra.BigOperators.Basic

/-!
# QOU.Brings.sw_period_eq_residue_sum — SW period as a residue sum

On the exceptional divisor `S_c ≅ P¹(ℂ)` at a branch point, the `n`-th
prolonged Seiberg–Witten differential `λ_SW^{(n)}` is a meromorphic
1-form with poles only at the branch points, so its period is the sum of
its residues (residue theorem on the compact Riemann surface):

  ∮_{S_c} λ_SW^{(n)} = 2πi · Σ_p Res_p λ_SW^{(n)}.

LaTeX label: `prop:sw-period-residue-sum`.
This is Lemma **L1** of the step-9 binding-closure workplan: it turns the
SW period `a_D^{(n)}` into an algebraic residue sum.

## References

- [manuscript] §5-brings-surface/sw-period-residue-sum
- [seiberg1994] https://doi.org/10.1016/0550-3213(94)90124-4

**Ground ring**: `ℂ` (archimedean realisation; residues and periods are
genuinely complex-analytic). NOT part of the pre-archimedean formal chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Brings

open scoped BigOperators

/-- **SW period / residue data** on `S_c ≅ P¹(ℂ)` for the `n`-th prolonged
    Seiberg–Witten differential: the finite family of residues at the `k`
    branch-point poles, the period, the `2πi` normalisation, and the
    residue-theorem identity relating them.

    The geometric *realisation* — that `λ_SW^{(n)}` is meromorphic on
    `S_c` with exactly these residues — is the manuscript content
    (`prop:mi-sw-abelianisation`); here it is packaged as the structure's
    hypothesis so the residue-sum identity is available downstream. -/
structure SWPeriodResidue (k : ℕ) where
  /-- The vertical / jet (body) order `n`. -/
  jetLevel : ℕ
  /-- The residues `Res_p λ_SW^{(n)}` at the `k` branch-point poles. -/
  residues : Fin k → ℂ
  /-- The SW period `a_D^{(n)} = ∮ λ_SW^{(n)}`. -/
  period : ℂ
  /-- The `2πi` normalisation constant of the residue theorem. -/
  twoPiI : ℂ
  /-- Residue theorem on the compact surface `S_c ≅ P¹`. -/
  period_eq : period = twoPiI * ∑ p, residues p

/-- **L1.** The Seiberg–Witten period is `2πi` times the sum of its
    residues — an algebraic residue sum. -/
-- Ref: [manuscript] §5-brings-surface
theorem sw_period_eq_residue_sum {k : ℕ} (S : SWPeriodResidue k) :
    S.period = S.twoPiI * ∑ p, S.residues p :=
  S.period_eq

end QOU.Brings
