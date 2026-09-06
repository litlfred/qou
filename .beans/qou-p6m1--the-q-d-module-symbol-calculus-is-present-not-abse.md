---
# qou-p6m1
title: The q-D-module symbol calculus is PRESENT, not absent — split the conflated wall claim at every site
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T13:46:21Z
updated_at: 2026-09-06T13:47:00Z
---

## The claim, and why half of it is false

Eight sites in the corpus assert, in these words or close paraphrase:

> the named multi-month research walls **W1-W3** (q-jet-bundle / q-D-module
> symbol calculus, absent from Mathlib and the corpus)

The parenthetical bundles TWO objects and asserts absence of both. One of them
is present, in two independent sorry-free builds.

### PRESENT: the q-D-module symbol calculus

| carrier | content | sorries | built |
|---|---|---|---|
| `QOU.Machinery.QuantumTorusSymbol` | QDM-1/QDM-2: principal symbol on the q-Weyl quantum torus — `symbol`, `leadDeg`, `leadCoeff`, `topDeg_mul`, `symbol_mul`. 19 decls | 0 | on `main` by 2026-07-24 |
| `QOU.Mathlib.RamifiedShiftCalculus` | header reads literally "the q-D-module symbol calculus at a simple ramification point `z = z_c + t^2`". `shiftOp_comp`, `shiftOp_iterate`, `shiftOp_residue_slot` | 0 | `15bb70f4cd`, 2026-09-03 |

**The self-contained proof, needing no external evidence:**
`RamifiedShiftCalculus.lean` line 2 is `import QOU.Brings.RamificationParityMonodromy`
— it IMPORTS the file whose line 54 says the thing it builds is absent from the
corpus. The builder depends on the denial.

**And it was arguably stale when written.** `RamificationParityMonodromy.lean`'s
claim dates to `2c68d7f34a` (2026-08-10). `docs/coordination/deltalambda-covariance-week-review-2026-07-24.md:14`
already recorded "**q-D-module symbol calculus (QDM-1..2) sorry-free**" on
2026-07-24 — seventeen days EARLIER. So this is not only drift-since-09-03.

### ABSENT: the q-jet bundle over Sigma

Genuinely absent, and W1 ("construct `D_q` from `Sigma`") remains open. The
2026-09-03 audit says so in its own Honest scope section: "`D_q` is **not
constructed**; W1 stays a wall." `QuantumTorusSymbol`'s header likewise scopes
QDM-3/QDM-4 (characteristic variety / holonomicity) out.

So the fix is a SCOPING SPLIT, not a deletion, and not a downgrade of W1.

## Sites (8 measured, not 9)

A sibling report put this at 9; measured on `main` it is 8. Two further hits
are NOT defects and must be left alone: `2026-09-03-ramified-shift-calculus-w1-prune.md`
QUOTES the claim and immediately scopes it, and `qou-4g01` records the build.

1. `content/quantum-observable-universe/lean/QOU/Brings/RamificationParityMonodromy.lean:54` — the origin
2. `docs/audits/2026-09-03-enclosed-pole-set-E-is-not-identifiable.md:124`
3. `docs/audits/2026-09-06-resurgence-arc-convention-d-reanalysis.md:223` — MINE, merged 2026-09-06
4. `docs/audits/2026-07-20-zgeometric-prolongation-symbol-scoping.md:97` — the original scoping doc; TRUE when written, so it gets a dated update note, not a rewrite
5. `docs/coordination/dilog-part-b-cusp-attack.md:54`
6. `.beans/qou-p443:25` — MINE
7. `.beans/qou-l155:25` — MINE
8. `.beans/qou-3cgi:22`

Three of the eight are mine, propagated 2026-09-06 in the resurgence-arc PR.
I repeated an absence claim I had not measured, which is the exact defect
AGENTS.md names: "I found no rationale" and "there is no rationale" are
different claims and only one of them was measured.

## Two measurement traps hit while establishing this

- **`grep -c sorry` counts prose.** I reported `QuantumTorusSymbol` as carrying
  1 sorry. Its only match is the docstring heading `## What is proved here
  (sorry-free)`. The file is sorry-free. Count declarations, or check axioms.
- **A sibling agent's count is not a measurement.** The "9 sites" figure did not
  survive a direct grep; the real set is 8, and it excludes two sites that are
  correct records rather than defects.
