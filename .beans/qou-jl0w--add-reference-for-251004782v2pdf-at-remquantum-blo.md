---
# qou-jl0w
title: Add reference for 2510.04782v2.pdf at rem:quantum-bloch-group-framework-connection
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:36:33Z
updated_at: 2026-08-21T17:03:43Z
---

No ref() entry; the corpus has five Habiro entries but nothing on q-de Rham / Habiro cohomology, and no entry for the number-field Habiro ring it recovers.

**From the source**
- sec. 1.4 — The Habiro ring of a number field carries a regulator from K_3 into its Picard group, whose image line bundles have sections given by q-series from perturbative Chern-Simons theory; this geometry is invisible after (q-1)-completion.
  Use here: Directly parallels rem:quantum-bloch-group-framework-connection, which places the framework's traced volumes in a quantum Bloch group with a regulator to R and tags itself 'habiro'; it also identifies a missing primary reference (the number-field Habiro ring paper).

Source: `library/arxiv-2510.04782v2/2510.04782v2.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/arxiv-2510.04782v2/  ->  [wagner2025]
  q-Hodge complexes over the Habiro ring

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
