---
# qou-lkrd
title: '`lake build` (default target) scope gap — targeted builds are not library builds (the 22 errors are FIXED on main)'
status: todo
type: bug
priority: high
tags:
    - lean
    - infra
    - ci
created_at: 2026-08-08T11:45:00Z
updated_at: 2026-08-08T16:30:00Z
---

## UPDATE 2026-08-08 (later the same day): the two named modules are GREEN

Re-measured against `origin/main` at `d4c9a36022`, **194 commits after the
measurement below**:

```sh
lake build QOU.MathlibExt QOU.Archimedean.TorusKnot   # exit 0, no errors
```

Both modules now compile. The 22 errors were real when recorded, but they were
measured against a base that was already ~194 commits stale, and main has since
repaired them. **The claim in this bean's title is no longer true and should not
be quoted.**

What survives is the *scope* lesson in "Why it matters", which was the actual
point: "lake green" in this repo has usually meant targeted module builds, not
the default target, and those are different claims. Keep this bean open only
until the default target is confirmed green end-to-end and wired into a gate.

The measurement lesson is the durable content, and it is self-inflicted:
**this bean asserted a main-side defect that main had already fixed, because it
was recorded against a stale base.** Measuring "on main" means fetching main
first.

## What (as originally measured — SUPERSEDED by the update above)

Plain `lake build` in `content/quantum-observable-universe/lean` fails, on
`origin/main`, with **22 errors across two modules that `QOU.lean` imports**:

| module | errors | cause |
|---|---|---|
| `QOU/MathlibExt.lean` (imported **directly** by `QOU.lean:80`) | 11 | `List.foldl_mul_eq_mul_prod` and `Real.rpow_half_eq_sqrt` do not exist in the pinned Mathlib (`f897ebcf72`) |
| `QOU/Archimedean/TorusKnot.lean` (via `QOU/Archimedean.lean`) | 11 | `TorusKnotLabel.seifertRank` and `.embeddableOn` are referenced but the structure has only `r, s, r_ge_two, r_lt_s, coprime` |

Both files were last touched by `22728b8801` ("chore(lean): LWC-2 drop redundant
namespace prefix on the decl", Carl Leitner, 2026-08-03), which is an ancestor of
`origin/main`. Neither is touched by any `claude/*` branch in the 5₂ lane.

## Why it matters — this is the orphan gate's blind spot, inverted

`qou-orph` established that **`lake build` compiles only `QOU.lean`'s import
closure, so 756 of 1600 modules are never built by anything.** True. But it
carries the unstated implication that the closure *does* build. It does not.

So "lake green" in this repo has only ever meant **targeted** module builds
(`lake build QOU.QBeta.Foo`), never the default target. That is the same failure
this lane has now hit seven times: **a check that tests something adjacent to
what it claims.** A reviewer reading "lake green" reasonably hears "the library
builds"; what was verified is "these seven modules build".

Targeted builds do work — `lake build QOU.QBeta.FiveTwoArgSector` is green over
2060 jobs — so this does not invalidate any per-module claim. It invalidates the
*scope* those claims are stated in.

## Not fixed here, deliberately

Both modules are outside the 5₂/dilogarithm lane and are main-side; repairing
them from a feature branch would collide with siblings. Claim before working
this.

## Repro

```sh
cd content/quantum-observable-universe/lean
lake build                                   # 22 errors, exit 1
lake build QOU.MathlibExt                    # 11 errors
lake build QOU.Archimedean.TorusKnot         # 11 errors
lake build QOU.QBeta.FiveTwoArgSector        # green, 2060 jobs
```

## Suggested repair

1. `QOU/MathlibExt.lean`: both missing lemmas are Mathlib renames. Find the
   current spellings under the pinned rev, or inline the two-line proofs.
2. `QOU/Archimedean/TorusKnot.lean`: `seifertRank` / `embeddableOn` need to be
   defined (or the dot-notation call sites repointed at whatever replaced them).
3. Then wire `lake build` — the *default* target — into whatever gate is
   supposed to be checking Lean, so the scope of "green" matches the claim.
