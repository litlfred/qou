---
# qou-tkp0
title: 'BUG(q0 triage harness): nonzero exit conflated with CRASH — a failing-assertion producer still writes its artifact'
status: completed
type: task
priority: normal
created_at: 2026-08-23T08:33:36Z
updated_at: 2026-08-23T08:37:21Z
---

RESOLVED. Two fixes to computations/audits/q0_muon_witness_staleness_triage.py.

1. CRASH no longer means "exited nonzero". Many producers emit their witness and
   THEN exit 1 because an assertion inside it failed. Measured:
   cyclic_intertwiner_verify.py exits 1, writes its artifact, reports
   PASS=False with max_abs=0.001150426. Calling that CRASH discarded a real
   staleness answer AND put a false claim in the #5519 PR body — that it
   "cannot be regenerated in either PR". It can. New verdicts: CRASH is now
   reserved for producing nothing at all; a nonzero exit that still wrote an
   artifact gets the real staleness verdict with an /ASSERT-FAIL suffix.
   Reclassified: cyclic_intertwiner_verify -> SUBSTANTIVE/ASSERT-FAIL.

2. `invocation` is now masked, matching scripts/precision-gates.sh (see bean
   qou-znxr — that divergence is deliberate and correct, not a defect). Needed
   here for a different reason than the gate's: a witness committed from a bare
   `python3 <script>` differs from this harness's run on argv ALONE, so without
   the mask such producers read SUBSTANTIVE for a non-staleness reason.
   Deliberately NOT masked: scriptHash and engineVersion — real signal.
