/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.JimboGL
import QOU.SchurWeyl.QuantumGLHWBranching

/-!
# Slices commute with the restricted Hecke action

G3.4c (bean `qou-gl343`), identification step A.

Restrict the Jimbo action of `H_{m+2}` to `H_{m+1}` along `heckeIncl`.  The restricted
operator is `X ⊗ 1` on the last tensor factor (`jimbo_heckeIncl`), so it acts on each last-letter
slice `v_y(a) = v(a y)` separately:

`(ρ_{m+2}(ι x) v)_y = ρ_{m+1}(x) v_y`  (`slice_jimbo_heckeIncl`).

This is the equivariance needed to read the peel filtration of `HW_μ` as a filtration of
`H_{m+1}`-modules.

## Base ring (§7c)

Any field; `q ≠ 0`.
-/

namespace QOU.SchurWeyl.QuantumGL

open QOU.SchurWeyl.JimboGL QOU.SchurWeyl.HeckeInclusion Matrix

variable {K : Type*} [Field K] {d : ℕ} [NeZero d]

/-- **`X ⊗ 1` acts slice by slice.** -/
theorem slice_extLast_mulVec {N : ℕ} (X : Matrix (Fin N → Fin d) (Fin N → Fin d) K)
    (v : (Fin (N + 1) → Fin d) → K) (y : Fin d) :
    slice (extLast N X *ᵥ v) y = X *ᵥ slice v y := by
  classical
  funext a
  show ∑ b, extLast N X (Fin.snoc (α := fun _ => Fin d) a y) b * v b
    = ∑ b, X a b * v (Fin.snoc (α := fun _ => Fin d) b y)
  rw [sum_snoc]
  refine Finset.sum_congr rfl fun b _ => ?_
  rw [Finset.sum_eq_single y]
  · rw [extLast_snoc, if_pos rfl, mul_one]
  · intro x _ hx
    rw [extLast_snoc, if_neg (Ne.symm hx), mul_zero, zero_mul]
  · intro h; exact absurd (Finset.mem_univ y) h

/-- **Slices are `H_{m+1}`-equivariant** for the restricted Jimbo action. -/
theorem slice_jimbo_heckeIncl (q : K) (hq : q ≠ 0) (m : ℕ) (x : Hecke K q q⁻¹ m)
    (v : (Fin (m + 1 + 1) → Fin d) → K) (y : Fin d) :
    slice (jimbo d q hq (m + 1) (heckeIncl K q q⁻¹ m x) *ᵥ v) y
      = jimbo d q hq m x *ᵥ slice v y := by
  rw [jimbo_heckeIncl, slice_extLast_mulVec]

end QOU.SchurWeyl.QuantumGL
