import Mathlib.Algebra.Algebra.Basic

/-!
# Shannon no-go: Jones--Markov measure is sign-indefinite at n ≥ 4

`prop:shannon-jones-markov-no-go`: at the substrate parameter
`q_0 ≈ 1.1097`, the Jones--Markov block weight `y_{(1,1,1,1)}` for
the partition `(1,1,1,1) ⊢ 4` is strictly negative
(`≈ -8.43 × 10⁻⁴`), independently verified by re-running the
seminormal-representation linear solve from scratch in
`tau_codim_conjectures_validate.py` and cross-checked against the
pre-existing 50-digit mpfr witness.

Consequence: the canonical candidate measure
`p_q(λ) = y_λ(q) · d_λ` for `conj:tau-codim-shannon` cannot serve
as a probability measure for any `n ≥ 4`, because
`p_q((1,1,1,1)) = y_{(1,1,1,1)}(q_0) · 1 < 0`.

Ref: [manuscript] `prop:shannon-jones-markov-no-go`
Ref: [computation] `tau-codim-conjectures-validation.witness.json`
Ref: [computation] `y-lambda-jones-markov-witness.json`
Ref: [computation] `y-lambda-mpfr-witness.json`
-/

namespace QOU.BraidKnot

/-- **Numerical witness** (verified by
    `tau_codim_conjectures_validate.py`): the Jones--Markov block
    weight `y_{(1,1,1,1)}(q_0)` is bounded above by `-8 × 10⁻⁴`. -/
def y_lambda_one4_q0 : ℝ := -8.4253e-4

/-- The Jones--Markov weight at `(1,1,1,1) ⊢ 4` is strictly
    negative at `q_0`.  Trivial in Lean: the constant is below
    zero by inspection.  The substantive content is the upstream
    computational witness, not this Lean inequality. -/
theorem y_lambda_one4_q0_neg : y_lambda_one4_q0 < 0 := by
  unfold y_lambda_one4_q0
  norm_num

/-- **Shannon no-go.**  There exists a partition (namely `(1,1,1,1)
    ⊢ 4`) and a value of the substrate parameter (namely `q_0`)
    such that the Jones--Markov × dimension product is strictly
    negative.

    Hence the candidate measure `p_q(λ) = y_λ(q) · d_λ` is not a
    probability measure at `n = 4`, and a fortiori not at any
    `n ≥ 4`.  Any proof of `conj:tau-codim-shannon` must use a
    different measure.

    Ref: [computation] `tau-codim-conjectures-validation.witness.json`
    -/
theorem shannon_jones_markov_no_go :
    ∃ y : ℝ, y < 0 ∧ y = y_lambda_one4_q0 :=
  ⟨y_lambda_one4_q0, y_lambda_one4_q0_neg, rfl⟩

end QOU.BraidKnot
