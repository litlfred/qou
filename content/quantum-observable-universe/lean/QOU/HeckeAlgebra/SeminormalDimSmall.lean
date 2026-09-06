/-
# `seminormalDim` at named partitions

`QOU/HeckeAlgebra/WedderburnTrace.lean` states its results with `2 ≤ seminormalDim
lam` as a **hypothesis**, and flags why: no declaration in this corpus computed
`f^λ` at a named partition, so the reader-facing `(2,1)` reading of those theorems
rested on a classical value the Lean side could not supply. That gap is closed
here (bean `qou-v7ms` follow-up).

## Why it needed a route rather than a `decide`

`seminormalDim lam` unfolds to `QOU.Mathlib.dimSYT lam`, i.e.
`numStandardYoungTableaux (partitionShape lam)` — a `Nat.card` over a structure of
tableaux. Nothing reduces. The computable route is the **Frame–Robinson–Thrall
hook-length formula**: `QOU.Mathlib.dimSYT_eq_dimHLF` proves, *pointwise*,

    dimSYT p = dimHLF (p.parts.sort (· ≥ ·))

and `dimHLF l = (sz l).factorial / prodHooks l` is an ordinary computation on a
list. Measured 2026-09-05, `dimSYT_eq_dimHLF` reports
`[propext, Classical.choice, Quot.sound]`.

One obstacle remains after that: `Multiset.sort` is a `Quot.liftOn`, so `decide`
gets stuck on `p.parts.sort (· ≥ ·)` even for a literal partition. `sort_eq_list`
below routes around it — a sorted list is determined by its multiset, so the sort
is pinned by uniqueness of sorted permutations rather than by evaluation.

## Values

| λ | ⊢ n | `f^λ` | why this one |
|---|---|---|---|
| `(2,1)` | 3 | 2 | the clause in `unified-iterative-correction-proof.md` |
| `(2,2)` | 4 | 2 | the Wigner shape — the `n = 4` isospin menu is this singleton |
| `(1,1)` | 2 | 1 | the charge shape; included because `f^λ = 1` is the case where the block *is* its trace, so the `WedderburnTrace` results say nothing there — worth being able to see that rather than assume it |
-/
import QOU.Mathlib.IdentityIHLFBridge
import QOU.HeckeAlgebra.WedderburnTrace

namespace QOU.HeckeAlgebra.SeminormalDimSmall

open QOU.Mathlib QOU.BraidKnot.IdentityI
open QOU.HeckeAlgebra QOU.HeckeAlgebra.Hoefsmit QOU.HeckeAlgebra.Wedderburn

/-- **Pin a partition's sorted part list without evaluating `Multiset.sort`.**
A sorted list is determined by its multiset, so it suffices to exhibit the list
and check it is sorted. -/
theorem sort_eq_list {n : ℕ} (p : Nat.Partition n) (l : List ℕ)
    (hm : (p.parts : Multiset ℕ) = (l : Multiset ℕ))
    (hs : l.Sorted (· ≥ ·)) :
    p.parts.sort (· ≥ ·) = l := by
  have hq : ((p.parts.sort (· ≥ ·) : List ℕ) : Multiset ℕ) = (l : Multiset ℕ) := by
    rw [Multiset.sort_eq]; exact hm
  exact List.eq_of_perm_of_sorted (Quotient.exact hq)
    (Multiset.sort_sorted _ _) hs

/-- `seminormalDim` from a pinned part list, via the hook-length formula. -/
theorem seminormalDim_eq_dimHLF {n : ℕ} (p : Nat.Partition n) (l : List ℕ)
    (hm : (p.parts : Multiset ℕ) = (l : Multiset ℕ))
    (hs : l.Sorted (· ≥ ·)) :
    seminormalDim p = dimHLF l := by
  show QOU.Mathlib.dimSYT p = dimHLF l
  rw [dimSYT_eq_dimHLF, sort_eq_list p l hm hs]

/-! ### λ = (2,1) ⊢ 3 -/

/-- The partition `(2,1) ⊢ 3`. -/
def p21 : Nat.Partition 3 where
  parts := {2, 1}
  parts_pos := by decide
  parts_sum := by decide

@[simp] theorem seminormalDim_p21 : seminormalDim p21 = 2 := by
  rw [seminormalDim_eq_dimHLF p21 [2, 1] rfl (by decide)]; decide

theorem two_le_seminormalDim_p21 : 2 ≤ seminormalDim p21 := by
  rw [seminormalDim_p21]

/-! ### λ = (2,2) ⊢ 4 — the Wigner shape -/

/-- The partition `(2,2) ⊢ 4`. -/
def p22 : Nat.Partition 4 where
  parts := {2, 2}
  parts_pos := by decide
  parts_sum := by decide

@[simp] theorem seminormalDim_p22 : seminormalDim p22 = 2 := by
  rw [seminormalDim_eq_dimHLF p22 [2, 2] rfl (by decide)]; decide

theorem two_le_seminormalDim_p22 : 2 ≤ seminormalDim p22 := by
  rw [seminormalDim_p22]

/-! ### λ = (1,1) ⊢ 2 — the charge shape, and the case the results do NOT cover -/

/-- The partition `(1,1) ⊢ 2`. -/
def p11 : Nat.Partition 2 where
  parts := {1, 1}
  parts_pos := by decide
  parts_sum := by decide

@[simp] theorem seminormalDim_p11 : seminormalDim p11 = 1 := by
  rw [seminormalDim_eq_dimHLF p11 [1, 1] rfl (by decide)]; decide

/-- `f^{(1,1)} = 1`, so its block is `M₁(ℝ)` and the trace loses nothing there.
`trace_does_not_separate` needs `2 ≤ f^λ` and genuinely does not apply — recorded
so the boundary of those results is visible rather than assumed. -/
theorem not_two_le_seminormalDim_p11 : ¬ (2 ≤ seminormalDim p11) := by
  rw [seminormalDim_p11]; omega

/-! ### The `(2,1)` instances, no longer conditional

These are the statements `WedderburnTrace.lean` could only make with the bound as
a hypothesis. The shape objection to the `(2,1)` clause now has its dimension
fact in Lean, not only in prose.
-/

/-- At `(2,1)` the block traces do not separate decompositions. -/
theorem trace_does_not_separate_p21 :
    ∃ x y : WedderburnDecomposition 3, x ≠ y ∧
      ∀ mu : Nat.Partition 3, (x mu).trace = (y mu).trace :=
  WedderburnTrace.trace_does_not_separate p21 two_le_seminormalDim_p21

/-- And every trace-factoring functional at `(2,1)` — the Markov trace included —
is blind to that difference. -/
theorem indistinguishable_p21 :
    ∃ x y : WedderburnDecomposition 3, x ≠ y ∧
      (∀ c : Nat.Partition 3 → ℝ,
        WedderburnTrace.traceFunctional c x = WedderburnTrace.traceFunctional c y) ∧
      MarkovTrace.markovTraceOnWedderburn x = MarkovTrace.markovTraceOnWedderburn y :=
  WedderburnTrace.exists_indistinguishable_by_every_traceFunctional p21
    two_le_seminormalDim_p21

/-! ### The complement: three *block-reading* functionals at (2,1) ARE independent

`WedderburnTrace.three_supported_traceFunctionals_dependent` says any three
**trace-factoring** functionals at one partition are linearly dependent — one
coefficient against one number. This is the other half, and it is what makes the
pair sharp rather than merely discouraging: read the block instead of its trace
and three independent functionals exist at `(2,1)`, exhibited explicitly and
witnessed by matrix units.

Together the two say precisely where a derivation of the `(2,1)` clause has to
live: **not** in the Markov trace, which is one-dimensional there, but in the
`f^{(2,1)} = 2`-dimensional block, of which the trace reads one dimension.

**What this does not say, and the distinction is the whole point.** It does *not*
identify these three functionals with volume, surface and Coulomb. It says three
independent functionals exist at `(2,1)` once you read the block — an existence
statement about the linear algebra, nothing more. Matching them to physical
quantities is exactly the open obligation `qou-qb7p` recorded, and three
independent functionals existing is a *necessary* condition for such a match, not
evidence of one. A count agreeing with a count is a target to check a future
derivation against, never a criterion to search on.
-/

/-- Read entry `(i,j)` of the block at `lam`. Unlike `traceFunctional`, this sees
the block itself rather than only its trace. -/
noncomputable def blockEntry (lam : Nat.Partition 3)
    (i j : Fin (seminormalDim lam)) (x : WedderburnDecomposition 3) : ℝ :=
  x lam i j

/-- **Three block-reading functionals at (2,1) are linearly independent** — the
exact complement of `three_supported_traceFunctionals_dependent`, which says any
three *trace-factoring* ones there are dependent. Witnessed by matrix units:
each functional is 1 on its own and 0 on the others. -/
theorem three_blockEntry_independent_p21
    (a b c : ℝ)
    (h : ∀ x : WedderburnDecomposition 3,
        a * blockEntry p21 ⟨0, by rw [seminormalDim_p21]; omega⟩
              ⟨0, by rw [seminormalDim_p21]; omega⟩ x
          + b * blockEntry p21 ⟨0, by rw [seminormalDim_p21]; omega⟩
              ⟨1, by rw [seminormalDim_p21]; omega⟩ x
          + c * blockEntry p21 ⟨1, by rw [seminormalDim_p21]; omega⟩
              ⟨0, by rw [seminormalDim_p21]; omega⟩ x = 0) :
    a = 0 ∧ b = 0 ∧ c = 0 := by
  classical
  set i0 : Fin (seminormalDim p21) := ⟨0, by rw [seminormalDim_p21]; omega⟩
  set i1 : Fin (seminormalDim p21) := ⟨1, by rw [seminormalDim_p21]; omega⟩
  have hne : i0 ≠ i1 := by simp [i0, i1, Fin.ext_iff]
  have key : ∀ p q : Fin (seminormalDim p21),
      a * (Matrix.single p q (1:ℝ)) i0 i0
        + b * (Matrix.single p q (1:ℝ)) i0 i1
        + c * (Matrix.single p q (1:ℝ)) i1 i0 = 0 := by
    intro p q
    have := h (WedderburnTrace.blockAt p21 (Matrix.single p q 1))
    simpa [blockEntry, WedderburnTrace.blockAt_self, i0, i1] using this
  refine ⟨?_, ?_, ?_⟩
  · have := key i0 i0; simpa [Matrix.single, hne, hne.symm] using this
  · have := key i0 i1; simpa [Matrix.single, hne, hne.symm] using this
  · have := key i1 i0; simpa [Matrix.single, hne, hne.symm] using this

end QOU.HeckeAlgebra.SeminormalDimSmall
