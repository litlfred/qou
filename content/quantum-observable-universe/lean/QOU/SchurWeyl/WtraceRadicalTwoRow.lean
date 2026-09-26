/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.OcneanuTraceNotFaithful

/-!
# The radical of `wtrace` contains the whole three-row part

#7458 exhibited **one** element of `Hecke ℝ q q⁻¹ 2` that the Ocneanu trace form
cannot see.  This generalises it to a characterisation of one side: at every
level, **everything killed by every at-most-two-row block is in the radical**.

## The statement

`mem_rad_of_twoRow_blocks_vanish` — if `seminormalRep … d x = 0` for every shape
`d` with `d.rowLen 2 = 0`, then `wtrace (x * b) = 0` for every `b`.

Two facts do it, and both are already on `main`: `wtrace` is *defined* as the
Frobenius sum `Σ_ν y_ν · tr ρ_ν` (`wtrace_apply` is `rfl`), and
`ocneanuWeight_conventionD_eq_zero_of_three_rows` kills the weight of every shape
with a third row.  So each summand dies for one of two reasons — the block kills
`x`, or the weight kills the block — and the case split is on `d.rowLen 2`.

This is the **⊇ half** of "the radical is exactly the `ℓ(λ) ≥ 3` blocks", stated
about the `wtrace` carrier.  `QBeta/MarkovGramDegenerate` has the abstract
Wedderburn-diagonal picture (`wedderburnGram_det_ne_zero_iff_all_live`) and the
exact coranks; this is the carrier-level inclusion, unconditional.

## 🛑 RETRACTED, same day: the ⊆ half is NOT blocked on Wenzl's theorem

This section said the ⊆ direction needed the ≤2-row Ocneanu weights to be
nonzero, that the only corpus statement of that fact was
`conventionD_ocneanuWeight_eq_zero_iff_of_wenzl`, and that it is **conditional on
the class `IsOcneanuWeightSystem`, which has no instance** — hence a §3b-cond
premise nobody has established. The same claim went into bean `qou-s7z2` and
PR #7460's body.

**The first half is right and the second is wrong, because the reasoning went
through the wrong object.** `IsOcneanuWeightSystem` relates an **opaque** weight
family `y` to `schurPrincipal`; an instance of it really is Wenzl's theorem, and
its own docstring says so. But the ⊆ direction never needed the class. It needs
`ocneanuWeight q z_D mu ≠ 0` for `mu` with at most two rows — and `ocneanuWeight`
is a **closed form** (`SchurWeyl/OcneanuWeight.lean`), so that is provable
directly from the genericity `wtrace` already carries.

Proved, no `sorry` and no instance:
`OcneanuWeightTwoRowNonzero.ocneanuWeight_conventionD_ne_zero_of_two_rows`.
At `z_D` the substitution collapses each numerator factor to
`(q^{2j+4} − q^{2i})/(q²+1) = q^{2i}((q²)^{j+2−i} − 1)/(q²+1)`, nonzero when
`i ≤ j+1` — which `rowLen 2 = 0` supplies, since then every cell has row `≤ 1`.
It is the exact mirror of `ocneanuWeight_conventionD_eq_zero_of_three_rows`: a
third row gives a cell of content `−2`, so `q^{2(c+2)} = 1` and the factor dies.
Two rows is the boundary.

**The error class, for the next reader.** I conflated *"the corpus's general
statement about weight systems is unproved"* with *"this particular weight is not
known to be nonzero."* Only the first is true. A class carrying an abstract
family is not the only route to a fact about a concrete member of it — check
whether the object in hand is opaque or closed-form before inheriting a blocker
from the abstract statement.

What actually remains for ⊆, neither blocked:

1. **A pairing fact** — a nonzero matrix over `ℝ` is seen by some matrix under
   the trace form (`∃ N, (M * N).trace ≠ 0`, witnessed by a single-entry
   matrix). Standard and cheap; it was never the obstacle.
2. **Block isolation** — hit one Wedderburn summand and zero the rest via
   `heckeProduct_surjective`, as `OcneanuTraceNotFaithful` already does for the
   column shape.

The ⊆ half is still not in this file. It is unwritten, which is a different
thing from blocked, and this file continues to deliver only the ⊇ inclusion.

## Scope

Convention **D** (`z = q³/(q²+1)`), `ℝ`, and the genericity `wtrace` carries.
Under the excised convention C the three-row weight is nonzero and this statement
is empty rather than false.
-/

namespace QOU.SchurWeyl.WtraceRadicalTwoRow

open YoungDiagram QOU.Mathlib QOU.SchurWeyl QOU.SchurWeyl.SeminormalRep

/-- **⊇ : the three-row part is invisible to `wtrace`.**

Anything annihilated by every at-most-two-row block is in the radical of the
Ocneanu trace form — at every level, not just at `n = 2`. -/
theorem mem_rad_of_twoRow_blocks_vanish {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0) (n : ℕ)
    (x : Hecke ℝ q q⁻¹ n)
    (hx : ∀ (d : YoungDiagram) (hd : d.cells.card = n + 1), d.rowLen 2 = 0 →
      seminormalRep q hq0 hq2 n hd x = 0)
    (b : Hecke ℝ q q⁻¹ n) :
    wtrace q hq0 hq2 n (x * b) = 0 := by
  rw [wtrace_apply]
  refine Finset.sum_eq_zero ?_
  rintro ⟨d, hd⟩ -
  rcases Nat.eq_zero_or_pos (d.rowLen 2) with hrow | hrow
  · -- the block kills `x`, hence `x * b`
    have hxb : seminormalRep q hq0 hq2 n hd (x * b) = 0 := by
      rw [map_mul, hx d hd hrow, zero_mul]
    rw [hxb, Matrix.trace_zero, mul_zero]
  · -- the weight kills the block: a third row at convention D
    have hw : ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) d = 0 :=
      ocneanuWeight_conventionD_eq_zero_of_three_rows q hq21 d hrow
    rw [hw, zero_mul]

/-- The same statement in the form `OcneanuTraceNotFaithful` used at `n = 2`:
a **nonzero** such element refutes faithfulness of the form at level `n`. -/
theorem exists_nonzero_orthogonal_of_twoRow_blocks_vanish {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0) (n : ℕ)
    (x : Hecke ℝ q q⁻¹ n) (hx0 : x ≠ 0)
    (hx : ∀ (d : YoungDiagram) (hd : d.cells.card = n + 1), d.rowLen 2 = 0 →
      seminormalRep q hq0 hq2 n hd x = 0) :
    ∃ y : Hecke ℝ q q⁻¹ n, y ≠ 0 ∧ ∀ b, wtrace q hq0 hq2 n (y * b) = 0 :=
  ⟨x, hx0, mem_rad_of_twoRow_blocks_vanish hq0 hq2 hq21 n x hx⟩

end QOU.SchurWeyl.WtraceRadicalTwoRow
