---
# qou-zs4r
title: '[TOOLS T4] Parity harness: witness-parity Tool'
status: todo
type: feature
priority: normal
tags:
    - migration
    - tools
created_at: 2026-10-04T16:35:42Z
updated_at: 2026-11-21T13:00:00Z
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



## Built 2026-10-04/05 (session_01NdDGeP1SyShmoUssLuRZ91), platform PR folio-assistant#2133
`witness:parity` re-runs the COMMITTED producer in a scratch git worktree, so the qou tree is never written, and compares the result with the run-specific fields masked (`WITNESS_EPHEMERAL_FIELDS` = qou's `_EPHEMERAL_META_FIELDS`, unchanged).

Calibration on qou, measured:
- Without pyhecke_native: chi-sym-alt-closed-form gives **unknown**, naming pyhecke_native and clarabel. This matches the done-when.
- With pyhecke_native 0.9.0 built from today's source plus clarabel 0.11.1: also **unknown**, not pass. The committed witness records build `88833bbb2bd7f717` and today's source builds `fd6b97f9ca5fec82`. The re-run's values differ from the committed ones only near the 60th significant digit (relative 1e-48 to 1e-60), at the 60-digit output precision. The tool now reads the re-run's own `environment` and calls any difference unknown, so this is reported as a different build, not as pass or fail. No numeric tolerance was added. The done-when's expected pass for this witness is not reproducible here, because the recorded native build is not the one current source produces.
- Sample, the 10 cheapest witnesses whose recorded environment matches this container: **10 pass, 0 fail**. The qou tree was untouched and no worktree was left. Run with pyhecke_native installed, the same 10 come back unknown, because the producer records the extra package; that is correct, since it is a different environment.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Not started. This story is owner-gated (AGENTS.md 'ask the owner before changing things') and needs work in a platform repo as well as qou, so it was not started in the wave-1 drain.
