---
# qou-1aof
title: Cite [hornig-mayer2002] at docs/audits/2026-08-01-em-linking-reads-round1.md
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:09Z
updated_at: 2026-10-04T15:17:39Z
parent: qou-mub3
---

Move the two verified findings out of the references.ts note and into a refid-keyed citation site so they are discoverable by the dependency graph. The audit doc discusses them in prose but never writes the key, so no grep finds them.

**From the source**
- Conclusions, p. 715–716 — 'the antisymmetry of H^(3)(B1,B2,B3) seems to be one of the key problems for a further generalization analogous to helicity' — an independent physics-side confirmation of the antisymmetry obstruction.
  Use here: Corroborates obstruction O1 for the third-order-helicity / EM-linking route; belongs in a durable content or audit artifact, not a bib note.
- Conclusions, p. 709 — 'only expressions quadratic and cubic in magnetic flux' can be obtained; the quadratic slot is occupied by cross-helicity, which vanishes for Brunnian configurations.
  Use here: The scaling trap: a Coulomb-like pair energy needs Flux², which the third-order invariant cannot supply.

Source: `library/arxiv-physics-0203048v1/0203048v1.pdf` (`hornig-mayer2002`)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.
