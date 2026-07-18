import QOU.BraidKnot.KeystonePerronFrobeniusGroundState
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# A genuine physical instance of `PerronFrobeniusGroundState` — the SU(2)₂ (Ising) fusion

The keystone value-step input (B),
[`KeystonePerronFrobeniusGroundState.lean`](KeystonePerronFrobeniusGroundState.lean),
axiomatises Perron–Frobenius / Ocneanu–Wenzl up-to-scale uniqueness as a §3b-cond
`Prop`-class and ships only a `Unit`-block (1×1) non-vacuity model.  This file
inhabits the class with a **non-trivial, physically meaningful** fusion category:
the truncated `SU(2)₂` (Ising) category, whose fundamental fusion (branching)
operator is the path-graph `A₃` adjacency matrix

  `N = !![0,1,0; 1,0,1; 0,1,0]`,

with Frobenius eigenvalue `ρ = √2 = [2]_q` (at `q = e^{iπ/4}`) and quantum-dimension
vector `d = (1, √2, 1)` (the genuine Ising anyon dimensions `1, √2, 1`).

Everything is proved **sorry-free from `Real.sqrt` facts + finite linear algebra**
— in particular `pf_proportional` (the field the parent axiomatises for the general
categorical case) is here a *proved theorem*: the `ρ = √2` eigenspace of `A₃` is
one-dimensional, spanned by `d`.  This demonstrates that `pf_proportional` is
genuine classical Perron–Frobenius content, not a vacuous marker; the parent's
remaining conditionality is only the *identification* of the QOU substrate fusion
operator with such a matrix (the owner-gated categorical step), not the linear
algebra around it.
-/

open Matrix

namespace QOU.BraidKnot.Keystone

/-- The `SU(2)₂` fundamental fusion operator: the path-graph `A₃` adjacency. -/
noncomputable def isingN : Matrix (Fin 3) (Fin 3) ℝ :=
  !![0, 1, 0; 1, 0, 1; 0, 1, 0]

/-- The Ising quantum dimensions `(1, √2, 1)`. -/
noncomputable def isingD : Fin 3 → ℝ := ![1, Real.sqrt 2, 1]

/-- The Frobenius eigenvalue `ρ = √2 = [2]_q`. -/
noncomputable def isingRho : ℝ := Real.sqrt 2

private lemma sqrt2_pos : (0 : ℝ) < Real.sqrt 2 := Real.sqrt_pos.mpr (by norm_num)

/-- The SU(2)₂ (Ising) instance of the keystone PF ground-state class. -/
noncomputable instance instIsingPFGroundState :
    PerronFrobeniusGroundState isingN isingRho isingD where
  N_nonneg i j := by
    fin_cases i <;> fin_cases j <;> simp [isingN]
  d_pos i := by
    fin_cases i <;> simp [isingD]
  d_eigen := by
    funext i
    fin_cases i <;>
      simp [isingN, isingD, isingRho, Matrix.mulVec, dotProduct,
        Fin.sum_univ_three, Pi.smul_apply, smul_eq_mul] <;>
      ring
  pf_proportional := by
    intro v _ heig
    -- Extract two of the three component equations of `N v = √2 v`.
    have h0 : v 1 = Real.sqrt 2 * v 0 := by
      have := congrFun heig 0
      simpa [isingN, isingRho, Matrix.mulVec, dotProduct, Fin.sum_univ_three]
        using this
    have h2 : v 1 = Real.sqrt 2 * v 2 := by
      have := congrFun heig 2
      simpa [isingN, isingRho, Matrix.mulVec, dotProduct, Fin.sum_univ_three]
        using this
    -- h0, h2 ⇒ √2 v0 = √2 v2 ⇒ v0 = v2.
    have hv02 : v 0 = v 2 :=
      mul_left_cancel₀ sqrt2_pos.ne' (h0.symm.trans h2)
    refine ⟨v 0, funext (fun i => ?_)⟩
    fin_cases i <;> simp [isingD, Pi.smul_apply, smul_eq_mul]
    · -- i = 1 : v 1 = v 0 * √2
      rw [h0]; ring
    · -- i = 2 : v 2 = v 0
      exact hv02.symm

end QOU.BraidKnot.Keystone
