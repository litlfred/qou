---
# qou-eqt3
title: 'MEASURE: valueOnlyProjects false-positive class — own-module-only reading cannot see Mathlib work'
status: completed
type: task
priority: normal
created_at: 2026-08-30T10:51:20Z
updated_at: 2026-08-30T11:11:03Z
---

## Result: the proposed fix is REFUTED, in the opposite direction

`qou-0avp` closed naming this follow-up: *"False-positive class: it reads only
own-module constants, so a proof doing real work through Mathlib alone is
indistinguishable from a projection (measured: `langlands_dual_pos`, and the two
`q_ns` conjuncts). Fix is a non-local non-packaging constant count; needs its
own recall measurement."*

Built that counter (`substantiveExternal`: constants outside the module, minus
logical plumbing, minus compiler-generated) and measured it.

**Population.** 297 theorems across 18 modules, chosen as the densest carriers
of `proof-no-self-assuming-projection` verdicts. `value_only_projects` fires on
45. Of those, 29 already carry a ledger verdict.

**The hypothesis predicted `legit` (false alarm) HIGH, `genuine` (real defect)
LOW. Measured:**

    legit   (false alarm)  n=11  median  0.0  mean  3.5   [0×7, 3, 3, 13, 19]
    genuine (real defect)  n=18  median  9.5  mean 13.7   [0×5, 1, 1, 2, 9, 10, 10, 10, 30, 31, 35, 35, 35, 38]

Opposite direction, ranges overlapping end to end. **Best single threshold
scores 62 %, exactly the always-flag baseline — zero discriminating power.**

**Why, in hindsight.** A `legit` conditional theorem honestly discharging its
goal from a stated hypothesis is a SHORT proof (`exact ctx.foo h`) touching
almost nothing external. A `genuine` self-assuming projection is often DRESSED —
a `rw`, a `simp`, some arithmetic — and the dressing is what gets counted. The
quantity tracks how ornamented a proof is, not whether the class carries the
conclusion.

Which is exactly what `valueOnlyProjects`'s own docstring already said: *"what
separates the two is whether the class carries the conclusion or its inputs, and
that is a reading, not a computation."* This measurement is the evidence for that
sentence, not a route around it.

**Disposition: KEPT, not reverted.** The counter is emitted as
`substantive_external` with the refutation in its docstring, because reverting
would leave `qou-0avp`'s follow-up standing as an untried good idea and the next
agent would rebuild it. Marked DO NOT THRESHOLD.

## Two process notes, both mine

1. **A detector reading 0 was my reader, not the detector.** First pass showed
   `value_only_projects` firing 0/49 — the TRAP this kernel's own docstring
   warns about. Cause: I read `only_projects`/`onlyProjects`; the emitted key is
   `value_only_projects`, so `dict.get` returned `None` and every row looked
   negative. The fix is an assertion on the key, not a change to the predicate.
2. **The ledger stores SHORT decl names; the kernel emits fully-qualified ones.**
   A bare-name join silently returned "not adjudicated" for all 32 rows. Join on
   `(file, shortname)` — and note 2 short names occur in more than one file
   (`strong_duality`, `r_matrix_braiding_structure`), so a short-name-only join
   is ambiguous as well as lossy. Same arity-conflation class AGENTS.md warns
   about, hit twice now inside this very tooling.
