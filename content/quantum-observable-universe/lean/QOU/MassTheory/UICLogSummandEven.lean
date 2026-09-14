import Mathlib.Tactic
import QOU.MassTheory.UICFunctionalSelection

/-!
# The UIC block's displayed summand is even, so its total is sign-blind over `ℝ`

The archimedean half of the resolution of the `prop:unified-iterative-correction`
block-vs-producer mismatch (owner ruling 2026-09-12: *"resolve functionals ...
what lean provable"*).  The generic half — where every theorem lives — is
`QOU.MassTheory.UICFunctionalSelection`; this file only instantiates it at the
summand the content block actually displays,

    f_d(τ) = ln|τ| − ln d ,

and records that `f_d` is even.  `Real.log` is the only archimedean construct
here, which is why it is a separate file (AGENTS.md §7c).

**What this buys.** Composed with `uicAll_sign_blind` it says: the total the
content block writes down is unchanged when any subset of the block traces flips
sign.  Composed with `gate_not_a_function_of_displayed_data` it says the
producer's Pass-2 gate — which keeps exactly the blocks with `tr ≤ 0` — reads a
datum this summand has destroyed.  Hence the block's formula cannot denote the
producer's functional, independently of which one the physics should keep.
-/

namespace QOU.MassTheory.UICLogSummandEven

open QOU.MassTheory.UICFunctionalSelection

/-- The summand displayed in `prop:unified-iterative-correction`:
`ln|tr M_λ| − ln d_λ`, as a function of the **signed** trace. -/
noncomputable def logRatio (d : ℝ) (τ : ℝ) : ℝ := Real.log |τ| - Real.log d

/-- **The displayed summand is even in the trace.**  `|·|` discards the sign
before `Real.log` ever sees it, so `f_d(−τ) = f_d(τ)` unconditionally — no
positivity hypothesis on `τ`, and none on `d`. -/
theorem logRatio_even (d τ : ℝ) : logRatio d (-τ) = logRatio d τ := by
  unfold logRatio
  rw [abs_neg]

/-- **The block's total is blind to the sign of every block trace.**

The instantiation of `uicAll_sign_blind` at the displayed summand: flipping the
sign of any subset of the final Markov traces leaves the content block's stated
total exactly unchanged.  A functional with this invariance cannot implement a
selection rule that reads those signs — which is what
`gate_not_a_function_of_displayed_data` makes precise. -/
theorem uicAll_logRatio_sign_blind {ι : Type*} [Fintype ι]
    (c : ι → ℝ) (d : ℝ) (τ ε : ι → ℝ) (hε : ∀ i, ε i = 1 ∨ ε i = -1) :
    uicAll c (logRatio d) (fun i => ε i * τ i) = uicAll c (logRatio d) τ :=
  uicAll_sign_blind c (logRatio d) (logRatio_even d) τ ε hε

/-! ## Axiom audit -/

#print axioms logRatio_even
#print axioms uicAll_logRatio_sign_blind

end QOU.MassTheory.UICLogSummandEven
