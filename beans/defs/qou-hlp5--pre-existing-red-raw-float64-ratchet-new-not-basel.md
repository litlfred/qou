---
# qou-hlp5
title: 'Pre-existing RED: raw-float64 ratchet (new_not_baselined=4) + 2 stale q0 audit witnesses on main'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-14T16:28:22Z
updated_at: 2026-10-04T15:22:09Z
parent: qou-9nnz
---


## Found 2026-08-14 (side finding of PR #5022 / bean qou-u5l3) — NOT caused by that PR

`bash scripts/precision-gates.sh` on a **clean tree** (stash-verified, no local
edits) reports:

    ADVISORY (not gating): no-free-parameter cert
    RED: raw-float64 ratchet

So the ratchet is red on `main` independently of any branch work. Regenerating
the audits shows real COUNT movement against the committed copies:

  witness-raw-float64-audit.witness.json
      dirty_witnesses      1572 -> 1575
      total_fields       536570 -> 536585
      new_not_baselined       0 -> 4      <-- this is the RED
      drained_files           0 -> 2

  q0-value-drift-audit.witness.json
      STALE                 320 -> 318
      proton-pin            745 -> 749
      canonical             616 -> 614
      (also: q0 value string 50 -> 68 digits; ppb_vs_canonical 4.17e-41 -> 0.0)

`new_not_baselined = 4` means four witnesses carry raw float64 that is in no
baseline. Per AGENTS.md the fix is AT THE PRODUCER — carry the value as
`mpmath.mpf` from source and serialize with `_precision.fmt`. Do NOT add them to
`raw-float64-baseline.json` and do NOT `--rebaseline`; baselines drain, never
grow. `drained_files = 2` is the good direction and should be committed once the
4 are fixed.

WHY NOT FIXED IN #5022: (a) out of that PR's scope (a c_3 registry adjudication),
(b) the sandbox there lacked numpy/scipy/sympy/clarabel — visible as the
dependency list SHRINKING in the regenerated
`q0-anchor-consistency-audit.witness.json` — so any witness regenerated there
would have been written under a degraded environment and could not be trusted.
All three regenerated witnesses were therefore REVERTED, not committed.

NEXT: on a full-dependency environment, (1) re-run the two audits and confirm
the counts, (2) identify the 4 `new_not_baselined` witnesses, (3) fix each at
its producer, (4) commit the regenerated audits naming which counts moved.
