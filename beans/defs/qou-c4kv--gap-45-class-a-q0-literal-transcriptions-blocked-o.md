---
# qou-c4kv
title: 'GAP: 45 class-(a) q0 literal transcriptions blocked on the A->C muon re-pin (#5500)'
status: in-progress
pr: 8184
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T09:37:26Z
updated_at: 2026-11-16T20:16:00Z
parent: qou-2002
---

Ledger: computations/audits/q0-literal-classification.json (45 rows, substate a-blocked). Validator: computations/audits/q0_literal_classification_audit.py --strict. Audit doc: docs/audits/2026-08-23-q0-literal-transcription-classification.md. Opened by PR #5535.

BLOCKED ON: owner ruling 2026-08-22 (#5500) moves the muon anchor A -> C (CODATA 2022). 66 of the 69 live divergent literals are B (CODATA 2018), which #5500 declares out of its own scope. Migrating them now pins them to a superseded value and collides with #5500's 53-witness regeneration.

WHEN #5500 LANDS: (1) re-run hardcoded_q0_literal_families_audit -- its reference becomes C, so the 222 currently-'clean' A-prefix transcriptions become divergent and BASELINE_DIVERGENT must be re-baselined; (2) migrate the 45 to read the anchor, not to retype C; (3) fix the two mislabels (habiro_interpolation_wlambda Q0_PROTON, brane_tower_full_channel_trace_audit) and gap_a3_overshoot_robustness_check's now-expired 'do not fix this' comment in the same pass.


CORRECTED under review (same PR, before merge). The title says 45; the measured
number is 37, and the original blanket reason -- 'blocked on #5500' -- was
wrong. It argues against TRANSCRIBING C; it does not argue against READING the
anchor, which is what the migration is. Re-measured, the 45 split three ways:

  migratable now  10 -> 8 migrated here.  Emits NO witness, so reading the
                  anchor costs no regeneration at all and nothing deferred it.
                  Established by scanning for WitnessBuilder / json.dump /
                  .save( , not assumed from the family label. All 8 re-run at
                  exit 0, assertions intact, no witness file touched.
  cost-deferred   32.  Emits a witness: reading the anchor regenerates it B->A
                  now and #5500 regenerates it A->C, i.e. twice, and each
                  regeneration is a place an unexplained number slips through
                  (measured happening 3x in this PR).
  correctness     5.  Reading the anchor does NOT close the defect: 2 carry a
                  frozen tr_M from the same run (moving q0 alone CREATES a
                  straddle -- gap_a3_overshoot_robustness_check says so in its
                  own comment, and I migrated then reverted it), 2 read
                  y_lambda from a B-built witness, 1 computes nothing.

So THIS BEAN now covers the 32 cost-deferred only. The 5 correctness cases are
independent of #5500 and need their frozen companions recomputed, not a re-pin.
Ratchet 71 -> 61.

## Progress Update (2026-11-16, PR #8184)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/AnchorManifestTriageAndAmeFloatDrain.lean` (wired into `QOU.lean`, `0` `sorry`, `0` vacuity advisories across all 7 static audits).
- [x] Paired with 50-dps `mpmath` + `sympy` verification probe `computations/probes/anchor_manifest_triage_and_ame_float_drain_probe.py` and stamped witness `computations/probes/anchor-manifest-triage-and-ame-float-drain.witness.json` (`allPassed: true`, `0` raw `float64` fields, `scriptCommitSha: 100f1be37af2187c6d27ac18b72a859b25538c6c`).
- [ ] Awaiting merge of PR [`litlfred/qou#8184`](https://github.com/litlfred/qou/pull/8184) (`0a6bb0fe54cf925fb3bdc7285374e8ee0913d6dd`).

