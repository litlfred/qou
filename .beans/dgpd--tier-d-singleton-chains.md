---
# dgpd
title: 'Tier D: singleton chains — per-compute authoring (the bulk)'
status: todo
type: task
priority: normal
created_at: 2026-08-18T21:00:00Z
updated_at: 2026-08-18T21:00:00Z
---

Parent dgap. 1233 production witnesses, each with its own producer. This is the irreducible
bulk and it does NOT parallelise mechanically: a chain is only honest if its author
understands that specific compute.

Suggested sequencing: by domain cluster (qbeta/, deltalambda/, alpha_em/, substrate/), each
taken by an agent already loaded on that domain, rather than by a single sweep. List a tier:
  python3 computations/audits/derivation_gap_categorize.py --tier D-singleton

ANTI-LAUNDERING: do not author a chain for compute you have not read. A chain asserting a
trust_basis it cannot support is worse than no chain — it converts an honest gap into a false
claim of provenance.
