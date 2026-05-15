/-!
# QOU.BraidKnot.DominantPolePartitionHook — hook formula for λ_⋆(Z, N)

Class-conditional proposition: for canonical atomic braid β(Z, N)
in H_{3A}(q), the u-pole maximizer of tr_M is the hook partition

    λ_⋆(Z, N) = (Z + 2N + 1, 1^{2Z + N − 1})

with width w = Z + 2N + 1, depth d = 2Z + N.  The uniqueness clause
of `HasHookMaximizer` ensures the maximizer is a singleton.

This file's substantive content is the `width_minus_depth_substrate`
theorem: a Z↔N asymmetry identity derived directly from the class
hypothesis.  No new `sorry` is introduced in this file — all proofs
discharge to the class fields.

LaTeX: `\\label{prop:dominant-pole-partition-hook}`
-/

import QOU.BraidKnot.HasHookMaximizer

namespace QOU.BraidKnot.DominantPolePartitionHook

open QOU.BraidKnot

/-- The hook-width formula `w(Z, N) = Z + 2N + 1` follows from the
    `HasHookMaximizer` class hypothesis. -/
theorem hook_width_formula (Z N : ℕ) [hyp : HasHookMaximizer Z N] :
    hyp.hookWidth = Z + 2 * N + 1 :=
  hyp.hookWidth_eq

/-- The hook-depth formula `d(Z, N) = 2 Z + N` follows from the
    `HasHookMaximizer` class hypothesis. -/
theorem hook_depth_formula (Z N : ℕ) [hyp : HasHookMaximizer Z N] :
    hyp.hookDepth = 2 * Z + N :=
  hyp.hookDepth_eq

/-- The hook is a partition of `3A`: `w + d - 1 = 3A` where
    `A = Z + N`.  Equivalently `w + d = 3A + 1`. -/
theorem hook_cell_count (Z N : ℕ) [hyp : HasHookMaximizer Z N] :
    hyp.hookWidth + hyp.hookDepth = 3 * (Z + N) + 1 :=
  hyp.hookCells_eq_3A

/-- **Z↔N asymmetry of the hook shape.** The substrate Z↔N
    asymmetry is encoded in the hook (w, d) pair:

        w − d = N − Z + 1.

    Proven directly from the class fields. -/
theorem width_minus_depth_substrate (Z N : ℕ)
    [hyp : HasHookMaximizer Z N] :
    (hyp.hookWidth : ℤ) - hyp.hookDepth = (N : ℤ) - Z + 1 := by
  have hw := hyp.hookWidth_eq
  have hd := hyp.hookDepth_eq
  omega

/-- **Per-nucleon contribution to (w, d).** Each proton adds 1 to
    width and 2 to depth; each neutron adds 2 to width and 1 to
    depth.  Equivalently, swapping one proton for one neutron
    moves 2 units of `w − d`. -/
theorem swap_one_proton_for_neutron (Z N : ℕ)
    [hZN : HasHookMaximizer Z N]
    [hSwap : HasHookMaximizer Z.pred N.succ] (hZ : Z ≥ 1) :
    ((hSwap.hookWidth : ℤ) - hSwap.hookDepth)
      - ((hZN.hookWidth : ℤ) - hZN.hookDepth) = 2 := by
  -- (N.succ − Z.pred + 1) − (N − Z + 1) = 2
  have h1 : (hZN.hookWidth : ℤ) - hZN.hookDepth = (N : ℤ) - Z + 1 :=
    width_minus_depth_substrate Z N
  have h2 : (hSwap.hookWidth : ℤ) - hSwap.hookDepth =
      (N.succ : ℤ) - Z.pred + 1 :=
    width_minus_depth_substrate Z.pred N.succ
  rw [h1, h2]
  have hZpred : (Z.pred : ℤ) = Z - 1 := by
    cases Z with
    | zero => omega
    | succ n => simp [Nat.pred_succ]
  rw [hZpred]
  push_cast
  ring

end QOU.BraidKnot.DominantPolePartitionHook
