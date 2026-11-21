---
# qou-cqs9
title: Cross-check [yekutieli2010] at prop:yekutieli-lifting
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:40Z
updated_at: 2026-11-21T12:54:01Z
parent: qou-1qhv
---

The Thm 1.7 / Thm 4.5 / Def 2.1 locators relied on at yekutieli-lifting.lean:27, global-gluing-proof.md and ccg-crossed-module-structure.lean:42 are unverified because no copy of the document is present. Obtain it and confirm the locators before the next proof-integration pass leans on them.

Source: `yekutieli2010` (bib key; PDF not committed to this repo)
Relevance: **undetermined** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

2026-09-06 (bean qou-smw9, commit e95d30edd4): the paper is now held (library/arxiv-0801.0083v4). Checked: no Theorem 1.7, 3.4 or 4.5 exists; the lifting criterion is Thm 4.17 (obstruction to lifting objects, cl^2 of Def 4.15) and the corpus locators were remapped to it (yekutieli-lifting.lean, yekutieli-lifting-proof.md, yekutieli-mapping-table.md). 'Thm 4.5 twisted quantization map' is not in this paper: re-keyed to yekutieli2015-twisted-dq (arXiv 0905.0488) Thm 0.10.1 in global-gluing-proof.md and the TwistedQuantizationMap Ref lines. STILL UNVERIFIED: 'Definition 2.1' at ccg-crossed-module-structure.lean:42 (and 4 sibling Refs) and 'Theorem 4.2' (3 Refs) -- section 2 of the held text carries no numbered definitions and there is no Theorem 4.2; not remapped.

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **done** (commit `17a7f704c`, branch `claude/cite-intake-drain-2026-11-21`, PR #8818, issue #8814). yekutieli2010 holds no crossed groupoid; re-keyed to yekutieli2014-descent Def1.2/Rem1.3/Def1.5/§1

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences.

Status stays in-progress until PR #8818 merges.

## 2026-11-21 — PR #8818 merged

The cite-intake work above landed on main. Status set to completed.
