---
# qou-xzd5
title: 'confinement_categorical: MarkovTraceContext has NO instance anywhere — may be vacuously true, not unclosable'
status: todo
type: task
created_at: 2026-08-09T11:07:51Z
updated_at: 2026-08-09T11:07:51Z
---


The last unresolved item from the qou-octr sweep (18 of 18 others refuted).
`confinement_categorical` could **not** be attempted, and the reason turns out
to be more interesting than the result would have been.

## Why it is blocked

`ConfinementCategoricalContext extends QOU.Shared.MarkovTraceContext`, whose
fields are not data but *structure*:

    R : Type u,  ringR : CommRing R,  invR : Inv R,  q : R,  n : ℕ,
    A : Type u,  ringA : Ring A,  algebraA : Algebra R A,
    heckeInst  : QOU.Hecke.HeckeAlgebra R n q A …,
    markovInst : QOU.Hecke.MarkovTrace  R n q A …

Refuting the theorem needs an instance, and an instance needs a Hecke algebra
carrying a Markov trace.

**Grepped the whole tree: there is no concrete instance of `MarkovTraceContext`,
and none of `QOU.Hecke.MarkovTrace` either.** Both appear only as hypotheses
(`[markovInst : QOU.Hecke.MarkovTrace n q A]`), never constructed.

## Why that matters more than the refutation would have

If `MarkovTraceContext` is **uninhabited**, then every
`theorem foo [ctx : MarkovTraceContext] : P ctx` is **vacuously true** — and
that is criterion **#3 `proof-no-false-premise`**, not #10. A different defect
with a different fix, and one that would apply to the *whole* family of
theorems quantified over this class, not just this one.

So the status of `confinement_categorical` is genuinely open in a way none of
the other 18 were: it is either

- **#10 unclosable** — if the class is inhabitable and the free fields
  (`E_infinity_00`, `e_block`, `integral`, `pi_centre`, `observable`) can
  disagree, which they plainly can once an instance exists; or
- **#3 vacuous** — if no instance can exist, in which case the `sorry` is
  closeable *and worthless*, and so is everything else over this class.

Deciding it decides the family.

## How to settle it

1. Try to build any instance of `QOU.Hecke.HeckeAlgebra R n q A` — the
   degenerate `n = 0`, `A = R` case is the obvious candidate. If it goes
   through, the class is inhabited and the #10 refutation follows immediately
   by the qou-octr method.
2. If it does not, find out whether the axioms are jointly satisfiable at all.
   An unsatisfiable `HeckeAlgebra` class would be a much larger finding: every
   `[HeckeAlgebra …]`-quantified result in the corpus would be vacuous.

Step 1 is an hour's work and settles the common case.

## Count

With this one outstanding, the sweep stands at **18 attempted, 18 refutable, 0
survivors**, plus this one blocked. The only statement to survive any check
remains `covariance_kernel_conjecture` (proved on `k ≤ 8`).
