---
# qou-vnct
title: Remark interpreting [dubois-violette-todorov2018] at QOU.MathlibExt.OctonionColourActionBaseModule
status: in-progress
pr: 8216
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:47Z
updated_at: 2026-10-04T15:23:45Z
parent: qou-2srd
---

OctonionComplexStructure.lean:9 and OctonionColourActionBaseModule.lean:10 name the key only inside prose docstrings, so the standard '-- Ref: [key]' grep does not find them. Add the canonical Ref lines so both files register as citation sites in the bibliography audits.

Source: `library/arxiv-1808.08110v1/1808.08110v1.pdf` (`dubois-violette-todorov2018`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## Progress (2026-11-16, PR #8216)
- [x] Non-vacuous Lean 4 theorem proved (`0` `sorry`, `0` vacuity advisories) in `folio/quantum-observable-universe/lean/QOU/Eightfold/HyperchargeWritheRotationJordanGlobalGroupOctonionAndShellFilling.lean`
- [x] 50-dps `mpmath` probe and witness stamped (`4e815f9543024d961ef648f5d19347ad79739059`, `scriptHash: 34801c11045c`)
- [ ] Awaiting Merge Manager merge of `litlfred/qou#8216`
