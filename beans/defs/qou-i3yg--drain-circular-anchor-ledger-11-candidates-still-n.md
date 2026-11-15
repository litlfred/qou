---
# qou-i3yg
title: 'Drain circular-anchor ledger: 11 candidates still needs-agent (docs/audits/circular-anchor-review-ledger.json). Run bun run content/pipeline/circular-anchor-audit.ts computations --review-ledger <ledger> then adjudicate each as genuine/legit/advisory with evidence. Already done: 6 genuine (T4 x4, T3 x2), 1 legit (awpk E_SUB false positive). Also: fix the 6 genuine ones (T4/T3) — the hardcoded check literals should be computed comparisons, and the T4-inverted theta values must carry ''conditional on A_omega=3'' wherever consumed.'
status: completed
type: task
priority: normal
created_at: 2026-08-01T21:25:06Z
updated_at: 2026-08-07T20:58:36Z
---

---

## 2026-08-07 DRAINED — 0 needs-agent, and the detector is the real finding

All 11 outstanding candidates adjudicated with evidence. Ledger now 10 genuine /
8 legit / 0 needs-agent; `--check-ledger` exits 0.

4 new genuine: VOL_41 (a REAL inversion — VOL_41 → q0 then a VERIFY print; in
_deprecated/), hecke_relation_verified and frobenius_passes (hardcoded True, no
computed counterpart), attractive_channel_confirmed (hardcoded True with the
genuine computed check on the line ABOVE it — **fixed**, bound to that
expression).

7 legit: two hardcoded-**False** recordings of genuine negative results, and
five outright false positives.

**`circ-anchor-inverted-roundtrip` fired 5 FPs of 6 candidates (~83%).** Filed
as **qou-yfsp** with both defects specified: it matches confirmation language
inside DOCSTRINGS, and "inverted to define" is really just "used downstream"
with no direction check (it calls an mpmath DPS knob an anchor inversion).

Applied here: `circ-vacuous-check` now splits severity by direction — a literal
False cannot launder a pass (advisory), a literal True can (critical). Verified
it does not suppress the genuine T4 cases.

Not fixed here, belongs with the T4 probe's other literals: `q0 = 1.11020` is
untraceable AND wrong vs canonical ~1.1099786 (surfaced by qou-skum).
