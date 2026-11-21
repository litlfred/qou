---
# qou-wy2h
title: 'P≠NP #2: NP→Jones encoding — SAT instance → link L with J_L(q₀) deciding it (lands L∈P^#P)'
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-31T20:00:58Z
updated_at: 2026-11-21T12:18:11Z
parent: qou-b1je
---

## Progress Update (Round 94 — PR #8360)

- **Lean 4.24.0 Brick**: `folio/quantum-observable-universe/lean/QOU/QBeta/MagnitudeAssemblyAndConventionFrameBrick.lean` (`0` `sorry`, `0` `axiom`, `0` warnings; `0 CRITICAL, 0 major, 0 advisory` across all 7 directory-mode AST audits).
- **80-dps Probe & Witness**:
  - Probe: `computations/probes/qou_w49j_wjw8_wuxx_wy2h_xs2c_magnitude_and_frame_probe.py` (Commit 1: `f052782a9424286a40e40154d7ef1d0ab55a6d3e`, `scriptHash = 35f305f18243`).
  - Witness: `computations/probes/qou_w49j_wjw8_wuxx_wy2h_xs2c_magnitude_and_frame_probe.witness.json` (Commit 2 / HEAD: `687a015fcc42c84733dfecead6ca9f6e13e3d31d`, `allPassed = true`, `rawFloatCount = 0`).
- **PR**: `litlfred/qou#8360` (`feat/qou-b9cj-w49j-wjw8-wuxx-wy2h-xs2c`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8360, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-07-31: "beans: close 0pd5 (reconciliation done), drop wy2h (dup of SkeinNPEncoding)"). The work may be partly or fully done. Read the bean before you close it.


## 2026-11-21T12:18:11Z — scrapped as duplicate, with evidence (pnp-collatz drain, https://claude.ai/code/session_01Qmmkt4pcG1jyT27PJvFyQ3)

Superseded-premise check (owner request 2026-11-21): none used.

The main commit 8b8e785ac2 already says *"drop wy2h (dup of SkeinNPEncoding)"* (2026-07-31). The later claim-reset text flagged that commit for review, and I have now read it. `QOU/Information/SkeinNPEncoding.lean` (on main, sorry-free) carries the NP → Jones/Markov-trace encoding: `NPSkeinReduction` (poly-size encoding with `accepts i ↔ HaltsObserved (enc i)`), `decisionBudget` (poly∘poly transfer), and `not_uniform_polyObservable_of_superpoly`. A concrete SAT → link construction is deliberately left as structure fields (an honest open input, per that file's Honesty note), and the classical #P-hardness of Jones evaluation is cited (Jaeger–Vertigan–Welsh). The only progress entry here points at batch PR #8360, which the owner closed as vacuous. Nothing in this bean is not already carried by SkeinNPEncoding.
