---
# qou-0otg
title: Cite [habiro2000] at prop:habiro-precision-ladder-equivalence
status: completed
pr: 8289
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:29Z
updated_at: 2026-11-21T12:54:01Z
parent: qou-1qhv
---

Four Lean sites cite locators (Theorem 1.1, Corollary 1.2) that do not exist in this document, and one attributes a different Habiro title to the key. Either re-point them at the real results here (Props. 5.1-8.2) or register the intended paper - 'On the quantum sl_2 invariants of knots and integral homology spheres' - under its own key and cite that.

**From the source**
- Props. 5.1, 6.1, 6.2, 8.2 and eqs. (1)-(2) in Sec. 3 — Explicit colored-Jones formulas for the trefoil (both chiralities) and figure-eight knot, and skein-basis propositions in the solid torus.
  Use here: Correct locators to replace 'Theorem 1.1' / 'Corollary 1.2' wherever those were cited, or evidence that the claim belongs to a different Habiro paper and needs its own key.

Source: `library/1172-3/1172-3.pdf` (`habiro2000`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## Round 57 Implementation Progress (PR #8289)
- **Status:** `in-progress` (per no-unilateral-closure policy)
- **PR:** https://github.com/litlfred/qou/pull/8289 (head `b1d29c3ac9e8ff1013e87a6f368591fb977a1ff3`, Commit 1 `85cf34f4dd33fa831b7480e3f2c9e1ff2e2f5c6d`)
- **Lean 4 Module & Theorems:** `QOU/AlphaEM/FiveTwoDiscriminantGluingAndHabiroDilogLadder.lean` (`habiro_props_51_61_82_cyclotomic_degree_step` citing `[habiro2000]` Props. 5.1, 6.1, 6.2, 8.2)
- **80-dps Witness:** `computations/probes/round57-fivetwo-discriminant-habiro-dilog-dglz-pentagon.witness.json` (`scriptHash: 3ee733fedb99`, `allPassed: true`, `0` raw `float64`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8289, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **done** (commit `e2bdfc861`, branch `claude/cite-intake-drain-2026-11-21`, PR #8818, issue #8814). re-pointed to habiro2004 Thm 4.5/Rem 4.6 (held)

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences.

Status stays in-progress until PR #8818 merges.

## 2026-11-21 — PR #8818 merged

The cite-intake work above landed on main. Status set to completed.
