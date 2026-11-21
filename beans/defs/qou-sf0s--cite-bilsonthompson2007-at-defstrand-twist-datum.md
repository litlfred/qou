---
# qou-sf0s
title: Cite [bilsonthompson2007] at def:strand-twist-datum
status: completed
pr: 8397
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:49Z
updated_at: 2026-11-21T12:54:01Z
parent: qou-1qhv
---

def:strand-twist-datum and rem:flavor-charge-assignments cite bilson-thompson2005 but not its braided-ribbon-graph successor (this upload, bilsonthompson2007), which is the version supplying the conserved-quantum-number and stability arguments those blocks lean on.

**From the source**
- Abstract; §I — In theories whose Hilbert space has a basis of ribbon graphs embedded up to diffeomorphism with dynamics by local moves, braiding gives conserved non-geometrical quantum numbers that are noiseless subsystems and can be mapped to first-generation Standard Model fermion charges; the paper does not claim to reproduce the interactions.
  Use here: The braid-to-charge assignment and its explicit non-claim about interactions is the honest scope bound for def:strand-twist-datum and rem:flavor-charge-assignments, which currently cite only the earlier preon paper.

Source: `library/0603022v2/0603022v2.pdf` (`bilsonthompson2007`)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

In-progress in PR #8397 (`feat/qou-r6ki-sf0s-spds-ssly-t579-round67`, `QOU.QBeta.ModularDoubleSkeinRibbonRound67`, 80-dps probe `round67_modular_double_skein_ribbon_probe.py`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8397, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **done-partial** (commit `f1dd59aff4e`, branch `claude/cite-intake-drain-2026-11-21`, PR #8818, issue #8814). BMS2007 §V cited at strand-twist-datum; rem:flavor-charge-assignments not edited

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences. The block uses the helon/quark twist picture as a candidate only; it states no electron braid form, so the σ₀σ₁σ₀ electron ruling is not contradicted.

Status stays in-progress until PR #8818 merges.

## 2026-11-21 — PR #8818 merged

The cite-intake work above landed on main. Status set to completed.
