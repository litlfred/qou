---
# qou-k520
title: 'VALIDATE WARNINGS (10): 5x missing chap:particle-interactions, 3x no Lean decl, 1 dangling remark, 1 missing rem ref'
status: todo
type: task
created_at: 2026-08-07T10:42:40Z
updated_at: 2026-08-07T10:42:40Z
---


## Status: PRE-EXISTING on `main` — verified 2026-08-07

Same 10 warnings on a clean `origin/main` checkout as on feature branches. Non-blocking
(`run-validate` fails on the 2 errors in `qou-idd2`, not on these), but they are real and
they are the kind of rot that accumulates silently.

## Grouped by root cause — 4 groups, not 10 problems

### G1 — `chap:particle-interactions` does not exist (5 warnings, ONE cause)

```
⚠ [chapter-overview]                  Undefined cross-reference: chap:particle-interactions
⚠ [approach-to-exceptional-divisor]   Undefined cross-reference: chap:particle-interactions
⚠ [thurston-relaxation]               Undefined cross-reference: chap:particle-interactions
⚠ [observations-intro]                Undefined cross-reference: chap:particle-interactions
⚠ [ns-blowup-physical-evidence]       Undefined cross-reference: chap:particle-interactions
```

Five blocks reference a chapter label that is not defined. Either the chapter was renamed /
never landed, or the label is wrong in all five. **Resolve once, fix five.** Check first
whether a particle-interactions chapter exists under a different label before adding one.

### G2 — proposition with no Lean declaration yet (3 warnings)

```
⚠ [meson-octet-decomposition]    prop:meson-octet-decomposition: no Lean declaration yet
⚠ [borromean-decuplet-derivation] prop:borromean-decuplet:       no Lean declaration yet
⚠ [tm-gs-normal-form]            prop:tm-gs-normal-form:         no Lean declaration yet
```

Expected-but-missing per the kind→Lean table (`proposition` warns if absent). These are
**honest** warnings — the blocks are not lying about their status. Each is a formalization
task; size them individually rather than as a batch.

### G3 — dangling remark (1 warning)

```
⚠ [einstein-ether-substrate]  rem:einstein-ether-substrate: remark has no `interprets` field
```

Per AGENTS.md §3a the fix is one of three: promote the claim to a `proposition`/`lemma`,
add `interprets:` pointing at the provable it interprets, or demote to `prose` if it makes no
logical claim. **Read the block before choosing** — the right disposition depends on whether
it asserts anything.

### G4 — undefined remark reference (1 warning)

```
⚠ [meson-em-sinh-closed-form]  Undefined cross-reference: rem:fine-structure-data
```

Same shape as G1 but a single target. Check whether `rem:fine-structure-data` was renamed or
removed.

## Reproduce

```bash
bash scripts/setup-folio-assistant.sh
bun run scripts/run-validate.ts content/quantum-observable-universe
```

## Suggested order

G1 first (5-for-1 payoff), then G4 (same shape), then G3 (needs a judgement call), then G2
(three separate formalization tasks — do not bundle).

## Definition of done

`run-validate` warning count 10 → 0, or each survivor explicitly justified in this bean as
intentional.
