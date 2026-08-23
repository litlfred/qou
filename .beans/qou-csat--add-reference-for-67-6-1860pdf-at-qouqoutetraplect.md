---
# qou-csat
title: Add reference for 67-6-1860.pdf at qou:QOU.Tetraplectic.su2L_su2R_commute
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:36:52Z
updated_at: 2026-08-21T17:03:29Z
---

A library Lean file reproduces a published construction with no citation; the entry is the minimum required for honest provenance.

**From the source**
- Abstract and Sec. 1 — Formulating fermions and Higgs mesons over the quaternions reproduces the left-right symmetric SU(2)_L x SU(2)_R x U(1) electroweak theory phenomenologically, gives an algebraic account of the replication of quarks and leptons in flavour doublets, and correlates the breakdown to U(1)_em with the existence of a Fock space for gauge singlets but not for quaternionic states.
  Use here: Supplies the missing attribution for the corpus's quaternionic-electroweak Lean file and, more usefully, tells the corpus what its own construction predicts: a left-right symmetric gauge group, which is a testable consequence of the interpretive identification bring_tetraplectic.md already flags as underived.

Source: `library/67-6-1860/67-6-1860.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/67-6-1860/  ->  [morita1982]
  Quaternionic Weinberg-Salam Theory

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
