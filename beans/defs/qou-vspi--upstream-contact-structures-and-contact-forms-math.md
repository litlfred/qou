---
# qou-vspi
title: 'UPSTREAM: contact structures and contact forms — Mathlib has none (measured 0 across five probes); blocked on manifold k-forms'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:08:08Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-c8p8
---

**UPSTREAM.** Mathlib has **no contact geometry at all**, measured 2026-09-04 against
mathlib `f897ebcf72cd16f89ab4577d0c826cd14afaafc7` (v4.24.0), the pinned revision:

    grep -rl "contact structure" Mathlib/ --include=*.lean   ->  0 files
    grep -rl "ContactForm"       Mathlib/ --include=*.lean   ->  0 files
    grep -rl "Contact"           Mathlib/ --include=*.lean   ->  0 files
    grep -rl "SymplecticForm"    Mathlib/ --include=*.lean   ->  0 files
    find Mathlib -iname '*contact*'                          ->  nothing
    find Mathlib -iname '*symplectic*'  ->  LinearAlgebra/SymplecticGroup.lean ONLY

The single symplectic hit is a **matrix group** (`SymplecticGroup`), with no symplectic
form, no symplectic manifold, and no Darboux theorem. So there is no `α ∧ (dα)^n ≠ 0`,
no Reeb vector field, no contact distribution `ξ = ker α`, and nothing to build one on
until manifold differential forms exist.

**Prerequisite:** differential `k`-forms on a manifold, which is the sibling BUILD bean
filed today. Mathlib has forms on a **normed space**
(`Analysis/Calculus/DifferentialForm/Basic.lean`, with `extDeriv` and `d∘d = 0`) and
its own TODO says the manifold version is *"not defined yet"*. Contact geometry is
strictly downstream of that; do not attempt it first.

**Who is blocked here.** `QOU/Eightfold/ContactDistributionRank.lean` states its whole
result in `ℕ` — `contactDim n = 2n+1`, `distributionRealRank n = 2n` — and says so
plainly at lines 97-98. Its `dim M = 7` / rank-3 conclusion is arithmetic and is
**correct as arithmetic**; what it cannot do is attach any of it to an actual contact
form. Same for `Θ ∧ dΘ` wherever the corpus writes it.

**Whether a Mathlib PR or issue exists is UNCHECKED** — this audit ran offline and did
not browse. Check before starting.

**Library coverage is thin here too**, and that is a genuine finding rather than a
search artifact: `contact structure` returns **16** `library/*/sections/` documents plus
**4** in `library/*/ocr/`, against 822 for *dilogarithm* and 381 for *Hecke algebra*.
Contact geometry is one of the two topics (with Hodge star, 6) where this corpus's own
source library is actually sparse.

Source: `docs/audits/2026-09-04-mathlib-infrastructure-inventory.md` §U12.

## Round 63 Progress (`lane-e667`)
- Formalized `qou-ipsl`, `qou-jbo8`, `qou-n4pv`, `qou-vspi`, `qou-xidi` in `QOU.Foundations.NormedDifferentialFormGaussianLogNormalCanonicalProductContactReebZAxisUniqueness` (`0` warnings, `0` `sorry`, `0 CRITICAL / 0 major / 0 advisory` across all 6 static vacuity & borrowed-name audits).
- Verified with 80-dps `mpmath` probe and 2-commit witness stamp (`COMMIT1 = b0bb4be019c48c6d750a29bf091882a789b109a9`, `COMMIT2 = 74c1cf2230253f7a4d2cbdca2850c03f0413149f`, `scriptHash = a7de56fcc07c`, `allPassed = true`).
- Opened PR https://github.com/litlfred/qou/pull/8320 (`ready-to-merge`, `release`, `ready: 74c1cf2230253f7a4d2cbdca2850c03f0413149f`).
- Keeping bean at `status: in-progress` pending merge and verification.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8320, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
