---
# qou-glqg
title: Add reference for 1908.07065v3.pdf at computations/lever1_borel_half_singularity_probe.py
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:36:09Z
updated_at: 2026-08-21T17:03:37Z
---

No ref() entry; the corpus carries Garoufalidis-Gu-Marino 2021/2023 for the knot-invariant side of resurgence but nothing for the quantum-SW-curve side, which is the side its SW-period and Bridge-equation language belongs to.

**From the source**
- Sect. 4.2 (Comparison to Borel resummation) — The Borel resummation of the quantum periods is compared directly against instanton calculus and found to agree.
  Use here: A template for the corpus's Bridge-equation programme: it shows what a validated resummation-versus-enumeration cross-check looks like, which is the standard the corpus's A_omega Stokes work would have to meet.

Source: `library/arxiv-1908.07065v3/1908.07065v3.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-ghy5): this says 'no references.ts entry yet'.
There is one — the document is registered as **grassi-gu-marino2019qsw**
('Non-perturbative approaches to the quantum Seiberg-Witten curve', Grassi,
Gu, Marino). It was registered under the machine-fallback id
`arxiv-1908.07065v3` with no authors, because JHEP welds the affiliation
letter to each surname ('Alba Grassia, Jie Gu b and Marcos Marinob') and the
parse failed; nothing cited that id while a Lean proof cited
`grassi-gu-marino2019qsw`, which resolved to nothing. Renamed to the key in
use, authors filled from the byline.

Not closing this — it is not mine to close, and the technique note above is
separate from the reference existing.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/arxiv-1908.07065v3/  ->  [grassi-gu-marino2019qsw]
  Non-perturbative approaches to the quantum Seiberg–Witten curve

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
