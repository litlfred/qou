# `BringFiberAction` de-vacuified — false axiom removed, A₅-irrep domain corrected

**Date:** 2026-06-18
**File:** [`content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean)
**Status:** Lean correctness fix (formalize-first); hardens `conj:s5-so3-fiber-action`. Does **not** close the conjecture — the geometric map remains the open, owner-gated step.
**Discipline:** corpus-grep + lean-vacuity. The fix was already specified in the corpus (the 2026-06-13 falsification); the Lean had not caught up.

## The defect

The conditional class `BringFiberAction` (per AGENTS.md §3b-cond) carried a **provably-false axiom**
discharged by a **vacuous placeholder + trivial instance** — the lean-vacuity pattern:

```lean
class BringFiberAction where
  partition_to_rotation : PartitionOf5 → IcosahedralRotation
  respects_conjugate : ∀ p, (partition_to_rotation p.conjugate).asSO3.angle
                            = -(partition_to_rotation p).asSO3.angle      -- FALSE
  hits_five_conjugacy_classes : True                                       -- VACUOUS

noncomputable instance : BringFiberAction where
  partition_to_rotation _ := { asSO3 := { …, angle := 0 } }               -- constant
  respects_conjugate _ := by simp
  hits_five_conjugacy_classes := trivial                                   -- vacuous discharge
```

Two problems, both already diagnosed in
[`2026-06-13-bring-fiber-action-falsification.md`](2026-06-13-bring-fiber-action-falsification.md):

1. **`respects_conjugate` + a *real* `hits_five_conjugacy_classes` are mutually unsatisfiable.** The 5
   A₅ ≅ I conjugacy classes are fixed by `|θ| ∈ {0, π, 2π/3, 2π/5, 4π/5}`; `respects_conjugate` sends a
   conjugate pair to `±θ` (same class), so the map is constant on each of the **4** conjugation orbits of
   the 7 partitions ⇒ hits **≤ 4** classes, never 5. The placeholder `: True` hid this by asserting nothing.
2. **Vacuous satisfiability.** The trivial constant instance discharges everything, so every downstream
   `[BringFiberAction]` result was conditional on a vacuously-true hypothesis — no real content.

## The fix

Corrects the map's **domain** to the five A₅ irreps (the falsification's §2–§3 resolution), removes the
false axiom, and makes the surjectivity **substantive**:

- **New `A5Irrep`** (5 irreps `A, T₁, T₂, G, H`, dims 1,3,3,4,5) + `PartitionOf5.toA5Irrep` (each partition
  ↦ its A₅ representative; conjugate partitions share one; self-conjugate (3,1,1) ↦ T₁ — the T₁⊕T₂ split is
  already in `s5_to_a5_electron_block_splits`).
- **`PartitionOf5.conjugate_same_a5_irrep` (theorem, `cases <;> rfl`)** replaces the false `respects_conjugate`:
  conjugate partitions restrict to the **same** A₅ irrep, hence share a fiber. The sign-twist is Wedderburn-side,
  not a geometric orientation reversal.
- **`BringFiberAction` rewritten**: field `irrepToRotation : A5Irrep → IcosahedralRotation` + substantive
  `five_distinct_classes : Function.Injective (angle ∘ irrepToRotation)`. A constant map fails injectivity, so
  the class is **not vacuously satisfiable**. The vacuous `: True` and the trivial instance are **removed** — no
  global instance is provided, so `[BringFiberAction]` is a genuine conjectural hypothesis (its inhabitation IS
  `conj:s5-so3-fiber-action`).
- **`s5_so3_fiber_action_scaffold`** now uses the hypothesis meaningfully: a third conjunct
  `bfa.irrepToRotation p.conjugate.toA5Irrep = bfa.irrepToRotation p.toA5Irrep` (the corrected conjugate-fiber
  identity), proved by `rw [conjugate_same_a5_irrep]`.

## What this does and does not do

- **Does:** remove a provably-false axiom; remove a vacuous `: True` placeholder; remove a vacuous trivial
  instance; correct the geometric map's domain to the A₅ irreps; make the conjecture an honest conditional
  hypothesis. The unconditional derived facts (A₅/S₃ branching, Δ_λ chirality, McKay–E₈ anchors) are untouched.
- **Does NOT:** construct the geometric map (which A₅ irrep ↦ which icosahedral rotation, from Bring's quintic
  automorphism group). That remains the open, owner-gated keystone step. This is a *formalization* correction,
  not a *closure*.

## Verification

- New declarations (`A5Irrep`, `toA5Irrep`, `conjugate_same_a5_irrep`, the de-vacuified class,
  `conjugate_partitions_same_fiber`) verified by `lean`-direct on an isolated probe (exit 0), including a sanity
  check that a constant map **fails** `five_distinct_classes`.
- Full-file build delegated to CI (`lean_ci.yml`): the sandbox `lake-cache` is missing one pre-existing Mathlib
  import (`Algebra.BigOperators.Group.List`), blocking a local full-file `lean`-direct; the change is otherwise
  isolated and the `ℝ`-typed parts are identical to the existing CI-green code.

## Cross-references

- [`2026-06-13-bring-fiber-action-falsification.md`](2026-06-13-bring-fiber-action-falsification.md) — the orbit-counting falsification + the A₅-irrep resolution this implements
- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — the keystone ledger
- [`2026-06-16-s5so3-markov-weighting-sasakian-scope.md`](2026-06-16-s5so3-markov-weighting-sasakian-scope.md) — the (separate) open geometric-weighting piece
