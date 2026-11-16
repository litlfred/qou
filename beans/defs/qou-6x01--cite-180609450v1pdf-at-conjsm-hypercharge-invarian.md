---
# qou-6x01
title: Cite 1806.09450v1.pdf at conj:sm-hypercharge-invariant
status: in-progress
pr: 8216
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:36:32Z
updated_at: 2026-10-04T15:17:13Z
parent: qou-6t49
---

conj:sm-hypercharge-invariant's Z_6 compatibility battery cites only baez-huerta2010 (the representation-kernel route); the geometric route the corpus claims agrees with it is unsourced there.

**From the source**
- eq. (1.4) = eq. (4.4), sec. 4 — The intersection of the maximal-rank subgroups Spin(9) and SU(3)xSU(3)/Z_3 inside the compact automorphism group of the exceptional Jordan algebra is S[U(2)xU(3)] = (SU(3)xSU(2)xU(1))/Z_6, i.e. the Standard Model gauge group in its Z_6 global form.
  Use here: Sources the 'geometric F_4-stabilizer derivation' half of the Z_6 grounding claimed in prose:sm-open-problems and used as the battery condition tau/3 + w/2 + Y/2 in Z for conj:sm-hypercharge-invariant.

Source: `library/arxiv-1806.09450v1/1806.09450v1.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-1806.09450v1/  ->  [todorov2018]
  Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [todorov2018] as the citation key when you do it.

## Progress (2026-11-16, PR #8216)
- [x] Non-vacuous Lean 4 theorem proved (`0` `sorry`, `0` vacuity advisories) in `folio/quantum-observable-universe/lean/QOU/Eightfold/HyperchargeWritheRotationJordanGlobalGroupOctonionAndShellFilling.lean`
- [x] 50-dps `mpmath` probe and witness stamped (`4e815f9543024d961ef648f5d19347ad79739059`, `scriptHash: 34801c11045c`)
- [ ] Awaiting Merge Manager merge of `litlfred/qou#8216`
