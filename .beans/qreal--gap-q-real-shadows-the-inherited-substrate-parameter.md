---
# qreal
title: 'GAP: a redundant `q_real : ℝ` shadows the inherited substrate parameter `q : R`'
status: todo
type: task
priority: high
tags: [lean, soundness, wall-side]
created_at: 2026-08-08T13:30:00Z
updated_at: 2026-08-08T13:30:00Z
---

Surfaced by the `qou-mtcx` base-ring refactor (PR #4756) as a side effect. It is
**not** a base-ring nit — it is a soundness defect in the statements, and it
should be triaged independently of that PR.

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
