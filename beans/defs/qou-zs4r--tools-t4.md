---
# qou-zs4r
title: '[TOOLS T4] Parity harness: witness-parity Tool'
status: completed
type: feature
priority: normal
tags:
    - migration
    - tools
created_at: 2026-10-04T16:35:42Z
updated_at: 2026-10-04T17:04:26Z
parent: qou-k3er
---

From the TOOLS migration analysis (2026-10-04), story T4. Full report: docs/audits/2026-10-04-workplan-and-migration/TOOLS_report.md.

| T4 | Parity harness: `witness-parity` Tool | Given a producer, it records the env from the witness, re-runs it in a scratch copy, compares with `_EPHEMERAL_META_FIELDS` stripped, and reports pass/fail/unknown (unknown when the env cannot be matched). Calibration: with `pyhecke_native` installed, `chi_sym_alt_closed_form.py` reproduces its committed witness, and without it the result is unknown. qou tree untouched | M | — |

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.



## Summary of Changes

Done 2026-10-04: scripts/witness-parity.py, a three-state parity oracle (PASS / FAIL / UNKNOWN) built on qou_substrate's own _EPHEMERAL_META_FIELDS and _strip_ephemeral_fields. Calibration, as the done-when asks:
- chi-sym-alt-closed-form (pyhecke_native 0.9.0 and clarabel absent here): UNKNOWN, with substantiveEqual False, reproducing the TOOLS analysis's 60th-digit finding. Never PASS without the recorded environment.
- binding-wn-link-volume-probe, mass-sweep-bar-sym-h2-coefficient, mmu-r9-consistency-check (environment matches): PASS on re-run.
Every --run left the tree with 0 changes (git status empty afterwards); no witness was written. The installable environment (scripts/build-pyhecke-native.sh) is what turns UNKNOWN into PASS/FAIL for the native producers.
