---
# qou-k21h
title: 'Lean does not compile: 37 modules failing, CI red since 2026-04-25'
status: in-progress
type: bug
priority: high
created_at: 2026-08-07T20:43:08Z
updated_at: 2026-08-07T21:03:41Z
---

A complete `lake build` of the QOU package — the first in months — failed on
**37 modules**. `lean_ci.yml` last ran **2026-04-25** and failed on `main`;
nothing has run a full Lean build since, so this accumulated unseen.

Found while reseeding the Lean olean cache (folio-assistant side).

## Status: all 37 now build (37 -> 17 -> 5 -> 1 -> 0)

`lake build` over all 37: **exit 0, 3238 jobs, zero errors.**

- [x] Class 1 — declaration outside the namespace its dot-notation needs
- [x] Class 2 — parse errors
- [x] Class 4 — duplicate / clashing declarations
- [x] Class 3 — "nonexistent Mathlib constants" (see correction below)
- [x] Class 5 — residual tactic failures
- [ ] Full `lake build` of the whole package — NOT yet proven (see Caveat)
- [ ] Re-enable / verify `lean_ci.yml`

## What it actually was

Nearly all of it was **one bug repeated**: a `def`/`theorem` meant to be
`Type.member` declared at namespace top level, so it became
`Namespace.member` and every `x.member` call site failed. 57 declarations
in the first sweep, more after.

Lean's error hid it. When the carrier is a `def ... : Prop`, dot-notation
resolution unfolds the type, reaches a Pi type, and reports
**`Function.member`** — a name nobody wrote and which greps find nowhere.

**No call site was changed for these.** `TorusKnot.lean` and
`BetaDecay.lean` already wrote `TorusKnotLabel.seifertRank`;
`QCollatz.lean` already wrote `QCollatz.inDomain`. Only the declarations
sat in the wrong place, which is what makes the rename the fix rather
than a guess.

### Correction to this bean's original Class 3

`List.foldl_mul_eq_mul_prod`, `Real.rpow_half_eq_sqrt`,
`Matrix.frobeniusInner`, `Matrix.PosSemidef.entry_*`,
`List.commute_init_prod` were recorded here as "references to Mathlib
constants that do not exist". Wrong. They are **defined locally** in
`MathlibExt.lean`, `FrobeniusInnerProduct.lean` and
`PosSemidefDiagZero.lean`, merely declared outside the namespace they are
called in. Mathlib genuinely lacks them; the inference that the code was
inventing upstream lemmas did not follow.

`algebraMap_self_apply` likewise DOES exist, at
`Mathlib/Algebra/Algebra/Defs.lean:395` — the earlier "not declared
anywhere" came from a grep that excluded `.lake`. It needed the `Algebra`
prefix.

### The genuinely distinct ones

- **Parse errors (files that had never compiled).** Three wrote
  `@[deprecated (since := "...") "msg"]`; the message comes first, per
  Mathlib's own usage. One declared `theorem exists` — a reserved keyword.
- **Two notions sharing a name.** `IsSelfDual` was declared twice for a
  categorical and a concrete involution; each now sits under its own type.
- **A misnamed legacy definition.** `hoefsmit_sigma1_gen` was declared
  twice; the second is the legacy archimedean form — its own docstring
  says so, and its deprecation message points callers *at* the generic, so
  it cannot be the generic. Renamed `hoefsmit_sigma1_legacy`, matching
  `markovZax_legacy` / `markovZN_legacy` in sibling files. That also
  cleared 5 "failed to synthesize" errors: the elaborator was matching a
  single real argument against the generic's `(d1 d2 b : R)`.
- **Structure-field collisions.** `AppendixSurreals/Basic` declared
  `neg/add/mul/sub` inside `namespace SurrealField`, which extends `Field`
  — those are inherited fields, so the declarations were rejected. They
  are lemmas about `IsInfinitesimal` / `IsFinite` and now sit under the
  predicate in each signature.
- **Two redundant rewrites.** `List.get?_eq_getElem?` led two chains whose
  goals were already in `l[i]?` form, so it matched nothing.

### A regression I introduced and fixed

The first sweep was scripted, and when one file needed two different
owners for the same bare name it applied whichever error came first —
turning `def transpose (P : PartitionWithCells)` into `Cell.transpose`,
colliding with the real one. Same for `A5Irrep.dim` vs `PartitionOf5.dim`
and three `allList` definitions sharing a namespace. The owner is the
declaration's own argument type; fixed on that rule.

## Caveat — this does NOT mean the package builds

The 37 are the modules that *failed*. The build that found them was killed
by a container reclaim at **625 of 1592** QOU modules, so roughly 950 were
never reached and have never been compiled in this cycle. Expect more
failures there. A full `lake build` is the only thing that settles it.

## Also fixed here

The `beans` CLI was down for the whole repo: `qou-8p1f`'s front matter had
unescaped single quotes inside a single-quoted YAML title, so every
command failed to parse it. 16857 beans load now.
