---
# qou-lq88
title: Add reference for 0012035v3.pdf at rem:lattice-qcd-from-qou
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:36:25Z
updated_at: 2026-08-21T17:03:45Z
---

No ref() entry exists; the surface-ordered non-abelian Stokes form used in rem:lattice-qcd-from-qou currently has no source of any kind.

**From the source**
- eq. (14), sec. 2.2 ("Theorem") — In its operator form the non-Abelian Stokes theorem states that the path-ordered holonomy around a closed curve C = boundary(S) equals the surface-ordered exponential of the twisted curvature over S.
  Use here: Sources the surface-ordered-exponential formula that rem:lattice-qcd-from-qou states without a citation.
- sec. 2.3.1 ("Topology"), Fig. 9 — When the loop is knotted the naive surface-ordered form fails; the knotted loop is decomposed into a product of surface factors indexed by the genus of the spanning surface, giving the topologically-nontrivial version of the theorem.
  Use here: The corpus applies non-abelian Stokes to holonomy around knots with a Seifert spanning surface, i.e. exactly the topologically-nontrivial case; this flags that the untwisted statement does not cover it.

Source: `library/arxiv-math-ph-0012035v3/0012035v3.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/arxiv-math-ph-0012035v3/  ->  [broda2002]
  Non-Abelian Stokes theorem in action

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
