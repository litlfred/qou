---
# qou-nap3
title: Add reference for 2412.04241v2.pdf at content/quantum-observable-universe/lean/QOU/Machinery/Heck…
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:35:42Z
updated_at: 2026-08-21T17:03:46Z
---

Cited by bare arXiv id in 4 Lean library files, 7 audit docs and 2 probe script names, with no ref() entry — the citation is unverifiable and no Lean -- Ref: key exists for it.

**From the source**
- Def. 1.1 (§1.4) — An element of the Habiro ring of a number field is a collection of power series f_m(x) in R[zeta_m][[x]], one per root of unity, satisfying a Frobenius-twisted p-adic re-expansion gluing f_m(x + zeta_pm - zeta_m) = (phi_p f_pm)(x).
  Use here: This is the executable form of the 'vertical edges' the tau-assignment gauge gate cites in prose; registering it lets HeckeTauAssignmentGaugeGate.lean carry a real -- Ref: key instead of a bare arXiv id in a docstring.

Source: `library/arxiv-2412.04241v2/2412.04241v2.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/arxiv-2412.04241v2/  ->  [garoufalidis-scholze-wheeler-zagier2024]
  The Habiro ring of a number field

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
