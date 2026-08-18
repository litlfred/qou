---
# dgap
title: 'EPIC: drain the derivation-chain gap (tiered, 1299 actionable)'
status: in-progress
type: milestone
priority: normal
created_at: 2026-08-18T21:00:00Z
updated_at: 2026-08-18T21:00:00Z
---

Program: docs/coordination/derivation-chain-drain-program.md
Tool:    computations/audits/derivation_gap_categorize.py  (re-run; do not quote stale numbers)

The validator reported ONE number (~2.6k after the #5269 recursive-scan fix). True but not
workable: it mixed QA-tool outputs, exploratory probes and production compute, which need
completely different work. Tiered by the work each witness actually needs:

  A audit-only  737  EXEMPT (landed) — declares auditOnly; chaining a sorry-counter's output
                     is a category error. Reported as its own `audit-only-exempt` bucket in
                     the summary line, never dropped (hiding a gap inside the measurement is
                     the exact defect #5269 fixed).
  B probe       287  exploratory scope-(a), low priority
  C family       66  ONE chain drains the whole family (audit matches producers by basename)
  D singleton  1233  per-compute authoring — the irreducible bulk
  E orphan      186  no producer on disk; provenance triage before any chain

ACTIONABLE = C + D = 1299.

Landed this pass: canonical_isotope_witness family chain -> 122 witnesses drained
(2630 -> 1746 computational-only, of which 762 moved to the exempt bucket).

Children: dgpc (tier C families), dgpd (tier D singletons), dgpe (tier E orphans).
DISCIPLINE: a chain that CITES is not a chain that DERIVES. A composition chain records
assembly + provenance; it does not make its inputs derived, and must never be described as
if it did. Authoring a chain for compute you do not understand is laundering.
