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
updated_at: 2026-10-04T16:36:18Z
parent: qou-k3er
---

From the TOOLS migration analysis (2026-10-04), story T4. Full report: docs/audits/2026-10-04-workplan-and-migration/TOOLS_report.md.

| T4 | Parity harness: `witness-parity` Tool | Given a producer, it records the env from the witness, re-runs it in a scratch copy, compares with `_EPHEMERAL_META_FIELDS` stripped, and reports pass/fail/unknown (unknown when the env cannot be matched). Calibration: with `pyhecke_native` installed, `chi_sym_alt_closed_form.py` reproduces its committed witness, and without it the result is unknown. qou tree untouched | M | — |

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.
