---
# qou-vnct
title: Remark interpreting [dubois-violette-todorov2018] at QOU.MathlibExt.OctonionColourActionBaseModule
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:47Z
updated_at: 2026-11-24T13:03:49Z
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

## 2026-11-22 — fixed in PR #9116: Octonion files: added the Dubois-Violette–Todorov 2018 Sec. 2 citation (𝕆 = ℂ ⊕ ℂ³).

Session: https://claude.ai/code/session_01Qmmkt5c8TSSh1GGk4PoPDu



## 2026-11-24 — Tranche 3 origin/main reconciliation

Verified on origin/main (acb646cc6fe): [dubois-violette-todorov2018] Sec. 2 citation wired in octonion Lean modules in merged PR #9116 (05e3c5b5c29 / 3885f1e31ec).
