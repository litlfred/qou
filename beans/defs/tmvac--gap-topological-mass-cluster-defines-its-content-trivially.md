---
# tmvac
title: 'GAP: the topological-mass cluster defines its content trivially (0, 1, identity)'
status: todo
type: task
priority: medium
tags:
    - reorg-2026-10-04
    - lean
    - vacuity
created_at: 2026-08-08T12:00:00Z
updated_at: 2026-10-10T07:01:23Z
parent: qou-d8c7
---

Found while draining the `wall-side-correct` WEAK queue, where it is **not** the
issue being drained. Filed here so it reaches the vacuity queue rather than being
lost in a base-ring audit.

## The finding

Three modules in the topological-mass / lifting-descent cluster define every
input as `0`, `1`, or the identity, so the lemmas above them hold for reasons
that have nothing to do with the mathematics they are named for.

| module | definitions |
|---|---|
| `lean/QOU/TopologicalMass/cat_transient_localises_blowup.lean` | `alpha : ℝ := 0`, `tauHat : ℝ → ℝ := fun x => x`, `trFrob : ℝ →+ ℝ := 0`, `localComponent (i : ℕ) : ℝ := 0`, hence `traceLocal i = 0` |
| `lean/QOU/LiftingDescent/tm_transient_localisation.lean` | `transientMItotal : ℝ := 0` |
| `lean/QOU/LiftingDescent/tm_descended_is_holonomy.lean` | `descendedMIdisc (i : ℕ) : ℝ := 1` |

A lemma whose every input is `0` or the identity is a §1a matter regardless of
what its statement says: it type-checks, it always will, and it constrains
nothing about the mass endomorphism.

## Why the existing detectors miss it

There is no `sorry`, no `axiom`, no `True` conclusion, and no `ctx.field`
projection — so `proof-no-trivial-true`, `proof-no-self-assuming-projection` and
the vacuous-existential detector all structurally cannot match. The vacuity is in
the **definitions the statement quantifies over**, not in the proof term.

This is a distinct shape from the classes already tracked on `qou-z3k1`
(unused-hypothesis `rfl`, vacuous existential, ascribed-literal tautology). The
closest analogue is `LevelSufficiency` on that bean — *"`markovTrace` is
definitionally independent of its particle argument, so the definition is the
real defect, not the theorem"* — and the same reading applies here.

## Candidate detector

`proof-trivial-definition-cone`: for a provable declaration, walk the `def`s its
statement mentions; flag when **all** of them reduce to `0`, `1`, `fun x => x`,
or a constant. High-recall, agent-confirmed like the other vacuity classes —
some of these are legitimately-zero base cases and only a read can tell.

## Explicitly not done here

No declaration edited. The honest disposition per §1a (prove / state with `sorry`
+ `-- Ref:` / demote to `conjecture`) is a per-item judgement, and these three sit
in a cluster (`lem:topological-mass-cat-transient`,
`lem:topological-mass-transient-localisation`, `lem:topological-mass-holonomy`)
whose intended content should be settled together rather than file by file.

The **base-ring** question for these files was answered separately and is closed:
the cluster's `ℝ` is load-bearing by meaning (a `nrm : ℝ → ℝ` is a norm; the rest
are masses and a holonomy), and §7c acknowledgements were added to the referring
blocks. That verdict is independent of this one.


## 2026-10-10 — reparented to the mass-endomorphism epic

This bean is carrier M2 of epic `qou-d8c7` (issue litlfred/qou#7547). Parent moved from `qou-wp3h` to `qou-d8c7`; nothing in the body above was changed by the move.


## 2026-10-10 — residues added by the epic survey (carrier M2 of `qou-d8c7`)

Absorbs `qou-m5fy` (scrapped today with a pointer here), and links `qou-0w3s`, `qou-wuxx`, `qou-ki4u`, and the `qou-lf1m` / `qou-hjf4` items. Two residues no bean owned, checked on `main` 2026-10-10:

- `instance trivialVortex` at `topological-mass-conjecture.lean:180` is a live global instance, so any `[...]`-conditional statement over that class is discharged trivially wherever it is in scope.
- `tm_transient_localisation.lean` carries its inputs as class fields that a zero instance satisfies, so the localisation statement says nothing as written.


## 2026-10-10 closed (session_01ST9RpvTF7JHNdUNafrjf9J)
Verified at HEAD: all three files use opaque constants + §3b input classes (CatTransientInputs, TMTransientLocalisationContext, TmDescendedInputs), citing qou-t4cv. Only the optional detector idea 'proof-trivial-definition-cone' remained; it is noted in thread qou-9bxg.
