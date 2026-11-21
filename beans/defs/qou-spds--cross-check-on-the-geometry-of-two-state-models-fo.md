---
# qou-spds
title: Cross-check On_the_geometry_of_two_state_models_for_the_colore.pdf at computations/aj_borromean_c…
status: completed
pr: 8397
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:57Z
updated_at: 2026-11-21T15:11:04Z
parent: qou-8hur
---

Cross-check the folio's colored Jones / Markov-trace values for (sigma_1 sigma_2^{-1})^2 and (sigma_1 sigma_2^{-1})^3 against the arc-graph state-sum this paper computes for 3-braid closures. A disagreement would be a real finding; an agreement is a corroboration only.

Source: `library/arxiv-2209.06973v1/On_the_geometry_of_two_state_models_for_the_colore.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-2209.06973v1/  ->  [arxiv-2209.06973v1]
  On the geometry of two state models for the colored Jones polynomial

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [arxiv-2209.06973v1] as the citation key when you do it.

In-progress in PR #8397 (`feat/qou-r6ki-sf0s-spds-ssly-t579-round67`, `QOU.QBeta.ModularDoubleSkeinRibbonRound67`, 80-dps probe `round67_modular_double_skein_ribbon_probe.py`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8397, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21T15:11:04Z cross-check result

Probe: computations/probes/weaving_link_rmatrix_state_sum_vs_borromean_tower_probe.py (commit bbb56765b12, branch claude/expo-cite-xcheck-wave2-2026-11-21). Exact sympy, ALL PASS with two amendments, thresholds unchanged.

- Implemented the paper's R-matrix state model (sec 5, eq Fterm, f_+ / f_-) for W(3,m) = closure of (s1^-1 s2)^m. The text layer does not fix the Figure 8 conventions (which strand is over, the (i,j) labels per crossing sign, the jump sign; sec 3 and sec 5 even state opposite jump directions). Scanned 64 conventions; pinned only by the paper's own framed-unknot examples U(+-1), split unknots, and RII/RIII. 4 pass and agree on every value.
- W(3,1) = 1 for n = 1..3.
- W(3,2) = 4_1: equals the corpus Habiro tower (basis sigma_k of aj_borromean_colored_jones_tower.py) for n = 1, 2, 3. Corroboration.
- W(3,3) = Borromean: equals corpus colored_jones_reduced(N,N,N) times [N]^2 at n = 1, 2. Normalization only: the paper divides by the long component, the corpus by every component. The pre-registered raw equality D failed for this reason (amendment 2). Corroboration.
- All values bar-symmetric (amphichirality).
- Finding (source, minor): the jump direction is stated both ways in the text layer (sec 3 "adding along an overcrossing" vs sec 5 "colours decrease on overcrossings"); the per-sign (i,j) labelling is only in Figure 8. Not a misprint in a formula, but a reader cannot implement the model from the text alone.
- Owner rulings: the Borromean core and 4_1 are standing objects; no superseded premise.
