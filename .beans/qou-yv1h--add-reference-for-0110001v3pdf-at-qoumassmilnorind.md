---
# qou-yv1h
title: Add reference for 0110001v3.pdf at QOU.Mass.MilnorIndeterminacyGate
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:37:02Z
updated_at: 2026-08-21T17:04:04Z
---

Relevant, no ref() entry; the corpus's mu-bar cluster (milnor1954, habegger-masbaum2000, meilhan-yasuhara) has no entry for the Seifert-surface computation route.

**From the source**
- Theorem (p. 561), parts (1)-(3) — For any choice of Seifert surfaces F for three components, mu-bar(ijk) = m(ijk)(F) - t(ijk)(F) mod delta, and one may choose F making either t(F) = 0 or m(F) = 0 mod delta.
  Use here: A geometric (triple-point-count) computation of the same mu-bar the corpus computes by Magnus expansion, and an independent derivation of the mod-delta well-definedness that MilnorIndeterminacyGate.lean encodes as a modelling choice rather than a proved statement.

Source: `library/0110001v3/0110001v3.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/0110001v3/  ->  [mellor-melvin2003]
  A geometric interpretation of Milnor's triple linking numbers

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
