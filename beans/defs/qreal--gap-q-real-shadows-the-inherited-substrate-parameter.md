---
# qreal
title: 'GAP: a redundant `q_real : ℝ` shadows the inherited substrate parameter `q : R`'
status: in-progress
type: task
priority: high
tags:
    - wall-side
    - reorg-2026-10-04
    - lean
    - soundness
created_at: 2026-08-08T13:30:00Z
updated_at: 2026-11-16T18:38:00Z
parent: qou-rtxm
---

Surfaced by the `qou-mtcx` base-ring refactor (PR #4756) as a side effect. It is
**not** a base-ring nit — it is a soundness defect in the statements, and it
should be triaged independently of that PR.

## ⚠ COUNT CORRECTED, and this bean is a DUPLICATE

**Scope was overstated.** An earlier note here said 97 candidate sites. That grep
included the **vendored Mathlib in the working tree** —
`Mathlib/Analysis/CStarAlgebra/…`, `Probability/Distributions`,
`MeasureTheory/…/LpSeminorm` all carry an unrelated `q_real`. Excluding
`.lake/packages`, the real figure is **32 hits across 8 files**:

```
mass-theory/conj-im-q-physical-role.lean
lean/QOU/Braiding/mobius_energy.lean
lean/QOU/Information/reeb_operations_per_planck.lean
lean/QOU/Information/toffoli_transfer_matrix.lean
lean/QOU/Observations/brane_tower_q_laplacian_decay.lean
lean/QOU/Observations/strangelet_crossing_energy.lean
lean/QOU/BraidsAndKnots/wedderburn_bratteli_recursion.lean
lean/QOU/Torsion/antiparticle_crossing_reversal.lean
```

Always exclude `.lake/packages` when counting corpus-wide; the vendored Mathlib
is in-tree and will inflate any bare `grep -r`.

Three of the eight are already handled in **PR #4756** (`mobius_energy`,
`wedderburn_bratteli_recursion`, `antiparticle_crossing_reversal` — the shadow
`q_real` is dropped). So the genuinely open set is ~5 files, not a sweep.

**DUPLICATE — prefer `qou-mt7r`.** PR #4756 filed the same finding independently
and states it better. Its formulation:

> `q_real` is called "the specialisation of the shared `q : R`" by its docstring
> while the *type* relates it to that `q` not at all. An instance can set
> `q_real := 37` over an unrelated Hecke `q` and every proposition still holds.

and its proposed fix is sharper than the three-option list below: the honest tie
is an **archimedean-evaluation (τ) field with `eval q = q_real` as its law** — a
design change to the shared parent, not a per-file edit. Positing the coherence
without the functor would be assumption dressed as structure.

**Close this bean into `qou-mt7r`.** It is kept only for the corrected count and
file list above.

## The defect

Several `MarkovTraceContext` descendants declare their own

```lean
  q_real : ℝ
```

alongside the `q : R` they already inherit from the parent — **with nothing
tying the two together**. No field, no hypothesis, no coercion.

Consequence: any block whose classical-limit hypothesis reads `q_real = 1` (or
`q_real → 1`) is constraining a **free real that has no connection to the
substrate parameter**. The intended claim — "in the classical limit of the
substrate" — is not what the Lean says. The hypothesis is discharged by picking
any real, and the theorem holds for reasons unrelated to `q`.

Known instances (from #4756's per-file pass): `Braiding/mobius_energy`,
`BraidsAndKnots/wedderburn_bratteli_recursion`,
`Torsion/antiparticle_crossing_reversal`. **The list is not known to be
complete** — #4756 only inspected the 15 `MarkovTraceContext` descendants. Sweep
wider before closing:

```
grep -rn "q_real" --include=*.lean content/
```

## Why the existing detectors miss it

There is no `sorry`, no `axiom`, no `True` conclusion, no `ctx.field`
projection, and the file compiles. The defect is a **semantic disconnection
between two fields**, which no syntactic checker in
`content/pipeline/lean-vacuity-axiom-audit.ts` is shaped to see. Closest
relative is the `LevelSufficiency` finding on `qou-z3k1` — *"`markovTrace` is
definitionally independent of its particle argument"* — the same shape: a
hypothesis that decorates rather than constrains.

## Dispositions, per block

1. **Drop `q_real` and state the hypothesis on the inherited `q`** — what #4756
   did for `mobius_energy` (`ctx.q = 1`). Correct when the block's content is
   genuinely about the substrate parameter.
2. **Keep `q_real` and TIE it** — add a field relating it to `q` (a coercion, or
   an archimedean-evaluation hypothesis) if the block legitimately needs the
   real image of `q` after the τ functor. §7c wall-side, and then it must say so.
3. **Demote** if neither is defensible.

Do NOT simply delete the hypothesis to make a checker pass — that changes what
the block claims.

## Care needed

Some `q_real` uses may be legitimate: the archimedean evaluation of `q` at the
substrate anchor is a real number, and a block on the observable side of the
§7c wall may want it. The defect is the **missing tie**, not the existence of a
real. Read each before acting.

## Resolution across all 8 files (2026-11-16, PR [`litlfred/qou#8151`](https://github.com/litlfred/qou/pull/8151), commit `11d9d9a0016ff7aacd751e96586ecbf5f1217753`)

1. `folio/quantum-observable-universe/lean/QOU/Braiding/mobius_energy.lean`: shadow `q_real` dropped; classical limit stated directly on inherited `q : R` (`q = 1`).
2. `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/wedderburn_bratteli_recursion.lean`: vacuous duplicate context removed; formalisation lives in `mass-theory/wedderburn-bratteli-recursion.lean`.
3. `folio/quantum-observable-universe/lean/QOU/Torsion/antiparticle_crossing_reversal.lean`: shadow `q_real` dropped; fields live over inherited `R`.
4. `folio/quantum-observable-universe/lean/QOU/Information/reeb_operations_per_planck.lean`: extends `QOU.Shared.ArchimedeanEval`, deriving `q_real := eval q` via `eval : R →+* ℝ`.
5. `folio/quantum-observable-universe/lean/QOU/Information/toffoli_transfer_matrix.lean`: extends `QOU.Shared.ArchimedeanEval`, deriving `q_real := eval q` via `eval : R →+* ℝ`.
6. `folio/quantum-observable-universe/lean/QOU/Observations/strangelet_crossing_energy.lean`: extends `QOU.Shared.ArchimedeanEval`, deriving `q_real := eval q` via `eval : R →+* ℝ`.
7. `folio/quantum-observable-universe/lean/QOU/Observations/brane_tower_q_laplacian_decay.lean`: migrated `BraneTowerQLaplacianDecayContext` in PR #8151 to extend `QOU.Shared.ArchimedeanEval` so `q_real := eval q` is derived from the inherited `q : R` rather than posited as an independent `ℝ` field.
8. `folio/quantum-observable-universe/mass-theory/conj-im-q-physical-role.lean`: updated `default_q_real (q : ℂ) : ℂ := ((q.re : ℝ) : ℂ)` in PR #8151 so it projects `q : ℂ` onto the real axis rather than taking an untied `q_real : ℝ` parameter.
