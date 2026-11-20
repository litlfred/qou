---
# qou-85o2
title: canonical-isotope-witness Z21-Z99 (98 shards) predate the C-excision; a spot re-run moved 2.19x and the cause is NOT isolated
status: todo
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T08:08:03Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

Surfaced by the qou-zzwm survey. Filed separately because the cause is NOT
isolated and it must not be reported as convention drift.

THE OBSERVATION: computations/ canonical-isotope-witness-Z*.json split cleanly
across the C-excision commit a24fdac8a1 (2026-08-24T11:04) in the symbolic
Hecke core:
    Z00..Z20  computedAt 2026-08-24T14:40  -- AFTER  (regenerated)
    Z21..Z99  computedAt 2026-08-23T17:15  -- BEFORE (98 shards, not regenerated)
Declared by content/.../appendix-knot-periodic-table/recursive-atom-knot-atlas-registry.md.
They carry layer "L4-qclt-colour-weighted" -> channel_binding, which is
z-dependent, so the boundary is at least suspicious.

WHY IT IS NOT (YET) A CONVENTION FINDING -- this is the load-bearing part.
A spot re-run of Z=26, N=19 gives qclt_binding = 120.70 MeV against the
recorded 55.088 MeV: a factor of 2.19. The survey that found this had PREDICTED
a move of x0.73 from the log-ratio of f_pn(std) between the two conventions
(0.3948 C vs 0.5082 D). 2.19 is not 0.73, and not its inverse. So convention
alone does NOT explain the gap, and something else moved in that producer's
cone as well.

Reporting it as "98 stale convention-C shards" would be the exact error class
AGENTS.md warns about: a topic match plus a plausible mechanism, asserted
without the arithmetic agreeing.

NEXT STEP, in order:
  1. Reproduce Z=26,N=19 twice more to confirm 120.70 is stable (one run is
     not a measurement).
  2. Bisect the producer's import cone across 2026-08-23..24 to find what ELSE
     changed. witness_import_cone_staleness_audit.py exists for exactly this --
     a producer's own source can be byte-stable while a module it calls moved.
  3. ONLY THEN decide whether regenerating the 98 shards is the fix, and say
     which change actually moved the number.

Do not mass-regenerate first and diagnose after: 98 shards regenerated on an
unexplained 2.19x would bake in whatever the unidentified second cause is.

## DIAGNOSIS (2026-08-31, PR #6390, branch claude/85o2-isotope-shard-2x-cause-2026-08-31)

Probe: `computations/isotope_shard_2x_cause_probe.py` (default mode + `--generalize`).

### 1. Stable. And 2.19 is not a ratio of anything.

Z=26,N=19 re-runs bit-identical three times: `qclt_binding = 120.7011740021478585985088`.

The bean's refusal to call this convention drift was right, but the reason is
not a second cause. The L4 row is

    prediction = qclt_binding(Z,N) - coulomb_energy_mev(Z,A)

`120.70` is the PRE-Coulomb strong term; the recorded `55.088` is the
POST-Coulomb prediction. `2.191048078 = 120.70/55.088` divides one pipeline
stage by the other. The probe rebuilds that exact figure from the two real
quantities to 10 digits. **Nothing moved by 2.19x.**

### 2. The like-for-like moves

    qclt_binding   166.7625 -> 120.7012   x0.7238   (predicted x0.7283)
    L4 prediction   55.0883 ->   9.0270   x0.1639

x0.7238 vs the survey's predicted x0.7283 is **0.63%** -- the convention
prediction was correct all along. The post-Coulomb x0.1639 is that move
amplified: a CONSTANT 111.674 MeV Coulomb term (byte-identical across the
boundary) subtracted from a shrinking strong term. A 28% drop in the strong
term becomes an 84% drop in the residual.

### 3. Single cause, attributed per file

`a24fdac8a1` touches exactly two Python files; each overlaid at its
pre-excision revision INDEPENDENTLY:

| file | contribution |
|---|---|
| `channel_binding.py` | **0.0 MeV** (comment + hardcoded self-test constant only) |
| `substrate/hecke_core_symbolic.py` | **46.061288 MeV** (z: convention C -> D) |
| both together | 46.061288 MeV |

`hecke_core_symbolic` alone == both, so the move is single-cause. With both
reverted the L4 row reproduces the committed `55.0883274583714925` to 1.2e-16
relative -- float64 resolution, from the producer's own
`float(qclt_binding(...))` cast at `canonical_isotope_witness.py:347`.

The producer is byte-stable across the boundary (`scriptHash e56cabeee1ea`
both sides), which is exactly why no scriptHash-keyed staleness check sees
this. Import-cone drift -- the `binding_canonical` / `tr_m_atom_via_transfer`
class AGENTS.md documents.

### 4. It generalises: 8/8

`--generalize` samples L4 rows from the stale shards (3152 available) and
checks pre-excision against each committed value. **8/8 reproduce**, with
`err/qclt` uniformly 1.5e-17 .. 7.3e-17.

Z=71,N=80 first read as a miss at 1.27e-15 -- judged against its own residual.
That judgement is wrong in the way this bean is about: its residual is 5.7% of
the pre-Coulomb term, so cancellation amplifies the floor by `qclt/L4 = 17.4x`.
Predicted bound `eps*qclt/L4 = 1.93e-15`; measured 1.27e-15 is UNDER it. The
same amplification, showing up in the ERROR instead of the VALUE.

### 5. RECOMMENDATION: regeneration IS the fix

The cause is fully identified and single. Nothing unexplained would be baked
in. But regeneration is **deliberately not done in this PR** -- it is a
separate, reviewable change.

Scope caveats for whoever runs it:
- Verified on 9 L4 rows (Z=26/N=19 plus a seeded sample of 8). Scope-limited
  (a): I did not verify all 3152, and rows on OTHER layers (L1/L3/magic-A)
  were not tested at all -- they may have their own drift.
- The producer's `float(qclt_binding(...))` at `canonical_isotope_witness.py:347`
  is a live NO-FLOAT64 violation. It caps every L4 row at float64 and, via the
  Coulomb cancellation, costs more than 1 ulp on small residuals (17.4x at
  Z=71,N=80). Worth fixing BEFORE regenerating, so the regeneration is not
  re-baked at the float64 floor. Own bean.
- The L4 branch is `A > 40`, so the Z00..Z20 shards contain rows that never
  enter it; the boundary is not a clean C/D split of the whole corpus.

### 6. Method note worth keeping

The per-file overlay was first done by `sys.path` ordering and SILENTLY LOST to
`_path_bridge`, which inserts `computations/` and every subdir at `sys.path[0]`.
The run reported "0.0 MeV contribution" for `hecke_core_symbolic` -- which
reads exactly like a real single-cause negative, and I nearly recorded it as
one. Now installed via `sys.modules` pre-registration (cannot be overtaken)
plus an assertion on each module's `__file__` before any number is trusted.
An attribution probe that cannot prove its counterfactual took effect is worse
than no probe.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8296, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
