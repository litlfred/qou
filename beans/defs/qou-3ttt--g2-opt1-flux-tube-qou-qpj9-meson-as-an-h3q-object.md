---
# qou-3ttt
title: 'G2-opt1 (flux-tube qou-qpj9): meson as an H3(q) object with the GLUON as 3rd strand (Hopf-binding) supplying hyperbolic volume; derive the H3 braid word q-bar + q + gluon. Framework-native (why mesons sit at H3 not H2). Recommended.'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-qcd
created_at: 2026-08-02T20:19:13Z
updated_at: 2026-11-23T23:06:44Z
parent: qou-8lxd
---

## Progress Note (2026-11-16)
- Formalized G2-opt1 3-strand meson (q-g-qbar) in H_3(q) (Wedderburn regular dim 1^2+2^2+1^2=6) and quadratic Casimir scaling from 4/3 (2-strand) to 8/3 (3-strand, exact ratio 2) in `QOU/Eightfold/BringThetaBruhatAndMesonH3.lean` (`meson_h3_gluon_third_strand_casimir_certificate`) + 50-dps probe `bring_theta_bruhat_and_meson_h3_probe.py` (PR `litlfred/qou#8163`, head `bc5c91877bf9516be8cbcc8cd12c1a6501a5e983`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8163, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-23 — Worker 20 (qou-8fw2) claimed on branch claude/sm8w-eightfold-wire-clasp-lambda-sigma-20261123 (under parent package qou-8fw2).



---
**Worker 20 () Delivery — 2026-11-23 (, Issue #9222, PR #9223):**
- Commits: `3c6d1b9dc71` (pre-registration), `39a4158b03b` (`HyperbolicMesonClaspAndDiquarkSplit.lean`, `QOU.lean` 22-module wiring, Ch. 10 content sync, 80-dps probe), `e28c1294e44` (witness stamp `allPassed: True`, `stale: False`, `q0Anchor: proton`).
- Lean 4 (`QOU/Eightfold/HyperbolicMesonClaspAndDiquarkSplit.lean`): 0 errors, 0 warnings, 0 placeholders, standard axioms `[propext, Classical.choice, Quot.sound]` only.
- 80-dps Probe & Witness (`computations/probes/sm8w_eightfold_clasp_diquark_gmo/`): passed `probe-float64-guard --diff`, `witness_raw_float64_audit --strict`, `mpf_context_dps_audit --strict`, and `lean-orphan-audit --diff`.
- Formalized the parameter-free 3-strand gluon-clasp map `(n_1, n_2) |-> sigma_1^{n_1} sigma_2^{-n_2} sigma_1 sigma_2^{-1} in B_3` (`claspSL2_det_and_trace`, `claspSL2_hyperbolic_all_generations`, `claspMarkovTrace_separates_Dbar0_K0`, `framedMesonClaspDatum_injective`), proving `SL_2(Z)` trace `2 n_1 n_2 + n_1 + n_2 + 3 >= 27 > 2` (strictly pseudo-Anosov on `{3,5,7}^2`), separating `Dbar^0 = (5,3)` from `K^0 = (3,5)` in both `z_2` (`+0.21247128`) and `z_3` (`+0.14415739`) Markov traces, and separating all 5 dictionary mesons.
