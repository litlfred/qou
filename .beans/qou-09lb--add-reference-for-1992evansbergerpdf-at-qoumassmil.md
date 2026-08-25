---
# qou-09lb
title: Add reference for 1992EvansBerger.pdf at QOU.Mass.MilnorIndeterminacyGate
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:37:05Z
updated_at: 2026-08-21T17:03:12Z
---

Core and orphan; the EM-linking reference cluster in references.ts has no entry for a braid-level higher-order winding number, which is the one construction its recorded obstructions do not cover.

**From the source**
- eq. (21)-(22), p. 6 — The one-form psi_ijk = lambda_ij d lambda_jk + lambda_jk d lambda_ki + lambda_ki d lambda_ij is closed by the Arnol'd relation, so Psi_ijk = Re integral over gamma of psi_ijk is a homotopy-invariant third-order winding number of a 3-string braid, well defined whether or not the net second-order winding numbers vanish.
  Use here: A braid-level third-order invariant that is NOT killed by a Hopf-linked spectator, unlike the mu-bar residue that MilnorIndeterminacyGate.lean collapses to ZMod 1. It is the natural candidate for the mixed-multibond shared channel that the mu-bar-idempotent probe refuted, and it lives on braid words, which is what the corpus actually manipulates.

Source: `library/1992evansberger/1992EvansBerger.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/1992evansberger/  ->  [evans-berger1992]
  A Hierarchy of Linking Integrals

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
