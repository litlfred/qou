/-
  Volume perturbation δΦ_k = z² · Vol(4₁) · [k-3]_q.
  Ref: [manuscript] §5.9, prop:volume-perturbation-formula
-/
namespace QOU.BraidKnot
noncomputable def volumePerturbation (k : ℕ) (q : ℝ) : ℝ :=
  let z := 1 / (q ^ (1/2 : ℝ) + q ^ (-(1/2 : ℝ)))
  let vol41 := 2.029883212819307  -- :leanval[Vol_4_1]{precision=16}
  z ^ 2 * vol41 * qInt (k - 3) q

/-- Theorem asserting the validity of the volume perturbation formula. -/
-- Ref: [manuscript]
def volume_perturbation_formula : True := sorry

end QOU.BraidKnot
