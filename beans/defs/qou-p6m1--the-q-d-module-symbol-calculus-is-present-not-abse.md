---
# qou-p6m1
title: The q-D-module symbol calculus is PRESENT, not absent — split the conflated wall claim at every site
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-09-06T13:46:21Z
updated_at: 2026-10-04T15:14:13Z
parent: qou-n4nr
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

1. `folio/quantum-observable-universe/lean/QOU/Brings/RamificationParityMonodromy.lean:54` — the origin
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



## Landed

- `ac49a3b5a5` — the origin site, `RamificationParityMonodromy.lean:54`. lean-direct exit 0 on it and on `RamifiedShiftCalculus`, its importer.
- `7e8404686b` — the six further sites.

PR #6968. **Final count: 7 files**, not the 9 a sibling reported nor the 8 my own phrase-grep gave. The population naming these objects is 35 lines / 22 files; most merely name them. Two sites are correct records and were deliberately left (`2026-09-03-ramified-shift-calculus-w1-prune.md`, `qou-4g01`), and `dilog-part-b-cusp-attack.md:54` is a false positive both earlier counts carried (Dedekind-eta limit, and "previously").

**W1 is untouched and still open** (`qou-d8de`): no `J^n_q E`, no connection lift.



## Stand-down on the convention-C adjudication (2026-09-06)

I had queued the 26 blocking value-audit sites as the next item and began
measuring them. **Stood down**: a sibling owns it — bean `qou-htsi` (created
today 09:38Z, carrying a verbatim owner directive of the same date) and PR
#6969, which had already adjudicated all 26 four minutes before I looked.
Convention-C excision is mechanical/settled work, which AGENTS.md gives ONE
owner; the measured-research-overlap relaxation does not apply to it.

Independent convergence worth recording: I ran the audit myself (137 confirmed
/ 26 blocking, against their 136) and independently flagged
`qbeta_precision_ladder_n5.py` as the one site that must NOT be ledgered as a
comparison — it emits a witness via `WitnessBuilder` and its `zC` docstring
says the ladder is z_C-locked. Their entry gets it right and introduces a
`deliberate-c-frame` verdict, which is exactly the third category the
comparison/leak binary was missing. No correction was needed.

Handed over on #6969 (comment 5559732847) the one thing they may not have: the
value audit's 26 blocking sites and `trace-convention-registry.json`'s
`blocked_on_rederivation` (13 rows) have **zero overlap**, and the two
registries carry OPPOSITE rules for what is now the same class — the registry
'accounts without excusing' and deliberately keeps its rows in the actionable
count, while a ledger entry is 'the ONLY thing that stops a binding from
blocking'. So the headline C number depends on which file an agent wrote in.
Their call, their PR.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-06 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (PR litlfred/qou#8222)
- **Status**: `in-progress` (awaiting PR merge)
- **PR**: https://github.com/litlfred/qou/pull/8222 (`95ddc04a72f67a43b1ccf1d77e08572625847a9b`, scriptCommitSha `4ed1888aba96f0c3e837a57c93b666bdd892604e`)
- **Summary**: Added `ramified_vs_unramified_diff_pos`, `ramified_index_div_unramified_eq_e`, and `dyadic_ramified_index_strict_gt_unramified` in `QOU/TraceFormula/TwoAdicSwanConductor.lean`, verified by 80-dps mpmath probe `keystone_writhe_ramified_stokes_ladder_probe.py` (`scriptHash: 75539ba8f436`).
