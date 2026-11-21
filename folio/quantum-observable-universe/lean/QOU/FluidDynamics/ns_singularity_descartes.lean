import Mathlib.Tactic.IntervalCases
import Mathlib.Tactic.NormNum.DivMod
import Mathlib.Algebra.Ring.Divisibility.Basic
import Mathlib.Data.Int.Basic

/-!
# QOU.FluidDynamics.ns_singularity_descartes — Kummer root levels of the Descartes universe

Lean companion of [`thm:ns-singularity-descartes`](../../../quantum-observable-universe/fluid-dynamics/ns-singularity-descartes.md),
restated 2026-10-12 by owner decision (option B).

**This file no longer asserts NS-singularity.** It used to provide a context
class `NsSingularityDescartesContext` whose field `obstruction_from_chi`
assumed `χ(A) = -6 → NS(A) ≠ 0`, and a theorem that projected it. That
self-assuming carrier is removed: the claim is not supported, since the
collision locus `Σ` is one-dimensional and `H²(Σ, ·) = 0`. See
`docs/audits/2026-10-12-ns-chain-after-item3-retraction.md`.

What remains is the **arithmetic** half of item 2 of the restated theorem. The
Reeb bundle has an `n`-th root iff `n` divides `χ = -6`, and the positive
`n` for which that holds are exactly `1, 2, 3, 6`. The topological half (that
the obstruction to an `n`-th root is `χ mod n` in `H²(S, μₙ)`) needs first
Chern classes, which Mathlib does not have; it is proved in prose in
`prf:qu-to-qou`, item 3, and is **not** formalised here.
-/

namespace QOU.FluidDynamics

/-- **Kummer root levels of the Descartes universe.** For `n ≥ 1`, `n` divides
`χ = -6` exactly when `n ∈ {1, 2, 3, 6}`. This is the arithmetic content of
item 2 of `thm:ns-singularity-descartes`. -/
-- Ref: [leitner2026] quantum-observable-universe/fluid-dynamics/ns-singularity-descartes.ts
theorem descartes_kummer_root_levels (n : ℕ) (hn : 0 < n) :
    (n : ℤ) ∣ -6 ↔ n = 1 ∨ n = 2 ∨ n = 3 ∨ n = 6 := by
  constructor
  · intro h
    have h6 : n ∣ 6 := by
      have : (n : ℤ) ∣ 6 := dvd_neg.mp h
      exact_mod_cast this
    have hle : n ≤ 6 := Nat.le_of_dvd (by norm_num) h6
    interval_cases n <;> simp_all
  · rintro (rfl | rfl | rfl | rfl) <;> norm_num

end QOU.FluidDynamics
