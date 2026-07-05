import QOU.BraidKnot.KeystonePerronFrobeniusGroundState

/-!
# A concrete non-`Unit` Perron–Frobenius witness (2-block model)

Strengthens the `Unit`-block non-vacuity witness of `KeystonePerronFrobeniusGroundState.lean` to a
genuine **2-block** model with a *non-constant* quantum-dimension vector and Frobenius eigenvalue
`≠ 1`: `N = [[1,1],[2,2]]`, `rho = 3`, `d = (1,2)`.  `N` is non-negative; `d` is a positive eigenvector
at `3`; and the eigen equation alone forces any eigenvector at `3` to have `v 1 = 2 · v 0`, hence to be
`v 0 • d` — so `pf_proportional` holds.  This shows the §3b-cond class admits non-trivial instances
(not only the constant `Unit` block).

**Still a toy.**  A non-negative-matrix witness, *not* the physical Hecke fusion category; the instance
whose `N` is the actual fusion operator and `d` the Hecke `d_q` remains the owner-gated open content
(narrow Subgoal-2 reversal, #2503/#2524).
-/

namespace QOU.BraidKnot.Keystone

open Matrix

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **2-block PF witness:** `N = [[1,1],[2,2]]`, `rho = 3`, `d = (1,2)` over any ordered field.
(Built with `Matrix.of ![![…]]` / `![…]` vector notation — the `!![…]` matrix notation module is not
needed.) -/
instance pfGroundState_twoBlock :
    PerronFrobeniusGroundState (Matrix.of ![![(1 : R), 1], ![2, 2]]) 3 ![1, 2] where
  N_nonneg := by
    intro i j; fin_cases i <;> fin_cases j <;>
      norm_num [Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one]
  d_pos := by
    intro i; fin_cases i <;> norm_num [Matrix.cons_val_zero, Matrix.cons_val_one]
  d_eigen := by
    funext i; fin_cases i <;>
      norm_num [Matrix.mulVec, dotProduct, Fin.sum_univ_two, Matrix.of_apply,
        Matrix.cons_val_zero, Matrix.cons_val_one, Pi.smul_apply, smul_eq_mul]
  pf_proportional := fun v _ heig => by
    refine ⟨v 0, ?_⟩
    have h1 := congrFun heig 1
    simp only [Matrix.mulVec, dotProduct, Fin.sum_univ_two, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val_one, Pi.smul_apply, smul_eq_mul] at h1
    funext i
    fin_cases i
    · simp [Pi.smul_apply, smul_eq_mul]
    · simp [Pi.smul_apply, smul_eq_mul]
      linarith

end QOU.BraidKnot.Keystone
