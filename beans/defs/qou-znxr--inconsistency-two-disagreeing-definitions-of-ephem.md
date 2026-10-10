---
# qou-znxr
title: 'INCONSISTENCY: two disagreeing definitions of ephemeral witness field — _EPHEMERAL_META_FIELDS omits invocation, precision-gates masks it'
status: completed
type: task
priority: normal
created_at: 2026-08-23T08:33:36Z
updated_at: 2026-08-23T08:35:13Z
---

NOT A DEFECT — closing. The divergence is deliberate and documented in
scripts/precision-gates.sh:434, with the rationale spelled out:

  "Masked here rather than in witness.py because `invocation` is genuine
   provenance -- it tells a reader how to reproduce the number -- and 309
   in-repo importers depend on that module's comparison semantics. Widening
   the shared mask to fix one gate's churn is the wrong blast radius."

That is the right call and I am not changing it. What I got wrong was assuming
two definitions disagreeing implies one is broken.

CONSEQUENCE I DID need to act on: any comparison-based staleness measurement
must adopt the SAME local widening, or a producer whose committed witness was
written under different argv reads as SUBSTANTIVE on argv alone. Applied to
computations/audits/q0_muon_witness_staleness_triage.py (bean qou-tkp0), citing
this rationale rather than restating it.
