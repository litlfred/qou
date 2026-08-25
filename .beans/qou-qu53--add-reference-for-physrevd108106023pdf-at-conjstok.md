---
# qou-qu53
title: Add reference for PhysRevD.108.106023.pdf at conj:stokes-dt-bps-bridge
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:36:41Z
updated_at: 2026-08-21T17:03:53Z
---

No ref() entry; the corpus cites kucharski-reineke-stosic-sulkowski2017 for the correspondence but has no source for an explicit quiver of the knot its argument turns on.

**From the source**
- sec. III A, the explicit matrix C^{4_1}, with the size formula in sec. III ("(4mp+1) x (4mp+1)") — The figure-eight knot, as the double-twist knot with both twist parameters equal to one, has an explicit 5x5 quiver matrix under the knots-quivers correspondence.
  Use here: Independently confirms the 5-node open-BPS count that conj:stokes-dt-bps-bridge's sector non-degeneracy argument infers from det(4_1) = 5, turning an inference into a checked value.
- sec. II, eq. (8)-(9) and sec. IV — A quiver presentation of the colored Jones polynomial is proposed for all double twist knots, with the quiver matrix built recursively from a base set of blocks; the Alexander polynomial of the family takes the form 1 - pmX.
  Use here: Extends the check beyond the figure-eight to a family, so the corpus's open-vs-closed sector separation could be tested at a second knot rather than only at 4_1.

Source: `library/physrevd108106023/PhysRevD.108.106023.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/physrevd108106023/  ->  [singh-physrevd108106023]
  Knot-quiver correspondence for double twist knots

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
