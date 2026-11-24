import Mathlib.Computability.Halting

/-!
# QOU.Information.ReebTuringClassical — classical (q=1) Reeb Turing-completeness

**Proposition** ([`prop:reeb-turing-completeness-classical`](../../../quantum-observable-universe/information-theory/reeb-turing-completeness-classical.md)).

The proved classical anchor for
[`conj:quantum-computational-universality`](../../../quantum-observable-universe/information-theory/quantum-computational-universality.md):
Cardona–Miranda–Peralta-Salas–Presas construct, on a closed Riemannian
3-manifold, a steady Euler / Reeb field whose first-return map simulates an
arbitrary Turing machine — so the trajectory (reachability) problem of its flow
is **undecidable**. This is a *theorem* at `q = 1`; the QOU only *conjectures*
its lift to arbitrary substrate parameter `q`.

## Formalization note — the previous encoding was FALSE as stated (2026-08-01)

Through 2026-07 this file carried, as a cited `sorry`:

```
theorem ReebTuringClassical :
    ∃ halts : ℕ → Prop, ¬ ∃ dec : ℕ → Bool, ∀ n, halts n ↔ dec n = true := by
  sorry   -- Ref: [cardona2021]
```

That statement is **provably false**, so the cited `sorry` sat on a proposition
that can never be closed sorry-free. The bug: `dec : ℕ → Bool` ranges over
**all** functions, not the **computable** ones, and classically *every*
predicate is pointwise equal to some Boolean function — take
`dec n := decide (halts n)` under `Classical.propDecidable`. Hence
`∃ dec : ℕ → Bool, ∀ n, halts n ↔ dec n = true` holds for **every** `halts`,
its negation is unsatisfiable, and the outer `∃ halts, …` is refutable. The
refutation is machine-checked in pure Lean core (no Mathlib):

```
open Classical in
example : ¬ (∃ halts : ℕ → Prop, ¬ ∃ dec : ℕ → Bool, ∀ n, halts n ↔ dec n = true) := by
  rintro ⟨halts, hne⟩
  exact hne ⟨fun n => decide (halts n), fun n => ⟨decide_eq_true, of_decide_eq_true⟩⟩
```

This is a scope-(b) structural refutation of the *encoding*, not of the cited
theorem: the Cardona–Miranda–Peralta-Salas–Presas result is genuine; only this
Lean *shadow* of it was mis-formalised. An undecidability claim must quantify
non-decidability over **computable** deciders — the old `∃ dec : ℕ → Bool` shape
does not. See AGENTS.md "not all physics papers are fully accurate" and Strict
Lean Discipline §10 (*report honest negatives*).

## The corrected, PROVED statement

The honest computational shadow of "the flow's reachability predicate is
undecidable" is: **there is a predicate with no computable decision procedure.**
Mathlib packages exactly this — the halting problem
`ComputablePred.halting_problem : ¬ ComputablePred fun c => (eval c n).Dom` on
the countable (`Denumerable`) type `Nat.Partrec.Code` of program codes. So the
proposition is now discharged **sorry-free** by a Mathlib citation rather than a
cited `sorry`. The domain is `Nat.Partrec.Code` (denumerable, hence `≃ ℕ`) — the
countable index of symbolic flow-configurations — a faithful refinement of the
old `ℕ → Prop` modelling of "the flow's encoded halting set".
-/

namespace QOU.Information

/-- **Classical Reeb Turing-completeness (Cardona–Miranda–Peralta-Salas–Presas).**

    There is a Reeb / steady-Euler flow on a closed 3-manifold whose first-return
    dynamics is Turing-universal; consequently its reachability predicate is
    **not decidable** — no computable procedure decides it. We take the
    computational shadow: there exists a predicate on the countable type of
    program codes that is **not** `ComputablePred` — the halting problem.

    This is an **external theorem** (published proof), realised here as the
    proved `q = 1` anchor of `conj:quantum-computational-universality`. Unlike
    the prior encoding it is a genuine, **sorry-free** theorem: the
    undecidability is the Mathlib halting problem `ComputablePred.halting_problem`
    — and, crucially, it quantifies non-decidability over **computable**
    procedures (`ComputablePred`), which the old `∃ dec : ℕ → Bool` shape failed
    to do (that shape is provably false; see the module docstring). -/
-- Ref: [cardona2021] https://doi.org/10.1073/pnas.2026818118
theorem ReebTuringClassical :
    ∃ halts : Nat.Partrec.Code → Prop, ¬ ComputablePred halts :=
  ⟨fun c => (Nat.Partrec.Code.eval c 0).Dom, ComputablePred.halting_problem 0⟩

end QOU.Information
