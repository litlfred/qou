---
# qou-0xpf
title: Add reference for 2304.12545v1.pdf at conj:borromean-bloch-group-element
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:36:12Z
updated_at: 2026-08-21T17:03:13Z
---

No ref() entry, and the closest existing key (garoufalidis-zagier2023) is a different paper with an adjacent arXiv id; minting a distinct id and noting the near-collision in its note field prevents a mis-keyed citation later.

**From the source**
- Sect. 3 (The Bloch group and the extended Bloch group) — Construction of the extended Bloch group and the chain complex in which it sits, as the home of the complex-volume invariant.
  Use here: The natural citation for the corpus's 8G regulator claim and for the group in which the corpus's fraktur-V = Vol + i CS analogy actually lives; conj:borromean-bloch-group-element currently asserts a K_3(C) class without pointing at the extended-Bloch construction.

Source: `library/arxiv-2304.12545v1/2304.12545v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/arxiv-2304.12545v1/  ->  [arxiv-2304.12545v1]
  HYPERBOLIC 3-MANIFOLDS, THE BLOCH GROUP, AND THE WORK OF WALTER NEUMANN

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
