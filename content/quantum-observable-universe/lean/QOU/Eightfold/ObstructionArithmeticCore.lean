/-!
# QOU.Eightfold.ObstructionArithmeticCore — the arithmetic heart, machine-checked

`ObstructionClassForcesComplexType` argues that a self-dual boundary-unipotent `PGL(3,ℂ)`
representation has trivial obstruction class: duality negates the class in
`H²(M, ∂M; ℤ/3)`, so `σ = -σ`, so `2σ = 0`, and `2` is invertible mod `3`.

Everything in that file except the last step is bookkeeping.  **The last step is the
mathematics**, and it is checked here — deliberately with **no imports at all**, over `Fin 3`
rather than `ZMod 3`.

## Why a separate, import-free file

Mathlib cannot currently be imported in this container: the restored `lake-cache` tree carries
**3470 `.olean` and zero `.olean.private` / `.olean.server` / `.ir`**, and a Lean 4.24 module
needs all four to load, so `import Mathlib.…` segfaults rather than erroring.  Isolating the
one substantive step in Lean core means it is **verified** instead of asserted, and stays
verifiable in any container.

`decide` is legitimate here and is not the banned laundering pattern: these are genuinely
decidable finite computations over `Fin 3` and `Fin 2` — three cases and two — not a
structural claim hidden behind the kernel evaluator.

## What is NOT proved here

That duality negates the obstruction class, and that the class is an isomorphism invariant.
Those are the topological inputs, carried as explicit hypotheses in the companion file, and
they are GGZ results rather than anything established in this corpus.
-/

namespace QOU.Eightfold

/-- `x + x = 0` forces `x = 0` in `ℤ/3`: two is invertible mod three. -/
theorem two_torsion_free_mod_three : ∀ x : Fin 3, x + x = 0 → x = 0 := by decide

/-- The form the obstruction argument uses: a class fixed by negation is trivial. -/
theorem eq_zero_of_eq_neg_mod_three : ∀ x : Fin 3, x = -x → x = 0 := by decide

/-- Contrapositive — the statement a search actually applies: a **non-trivial** obstruction
class is not fixed by negation, hence its representations are not self-dual. -/
theorem ne_neg_of_ne_zero : ∀ x : Fin 3, x ≠ 0 → x ≠ -x := by decide

/-- The argument genuinely needs `gcd(2, 3) = 1`: mod **2** the same statement is **false**,
witnessed by `1 = -1`.  So this is not a general fact about torsion — it is specific to the
centre of `SL(3)` being `μ₃` of odd order. -/
theorem mod_two_counterexample : ∃ x : Fin 2, x ≠ 0 ∧ x = -x := by decide

end QOU.Eightfold
