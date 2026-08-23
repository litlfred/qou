---
# qou-xfog
title: Remark interpreting 1908.07065v3.pdf at docs/audits/2026-07-12-alien-calculus-review-binding-gevr…
status: todo
type: task
priority: normal
created_at: 2026-08-08T23:36:10Z
updated_at: 2026-08-21T17:05:08Z
---

Record the technique and, importantly, the reason it does not apply as-is: the corpus's binding period is Gevrey-1/2 with entire level-1 Borel transform and is not q-holonomic, so the exact-WKB/TBA machinery has no established hook. Writing that down prevents a later agent re-proposing the route as though it were available.

**From the source**
- Sect. 3 (Quantum periods from TBA equations) — The resurgent properties of the all-orders WKB periods are encoded in Gaiotto-Moore-Neitzke TBA equations determined by the BPS spectrum, and are solved explicitly in the strong-coupling region.
  Use here: A concrete mechanism for locating Borel singularities of a quantum period from a BPS spectrum, which is exactly the open target the alien-calculus audit names. What would need checking first: whether the corpus's binding period is a period of a quantum curve at all, given the audit's own finding that its level-1 Borel transform is entire.

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

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-1908.07065v3/  ->  [grassi-gu-marino2019qsw]
  Non-perturbative approaches to the quantum Seiberg–Witten curve

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [grassi-gu-marino2019qsw] as the citation key when you do it.
