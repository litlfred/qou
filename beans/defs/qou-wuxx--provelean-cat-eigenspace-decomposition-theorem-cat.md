---
# qou-wuxx
title: 'cat_eigenspace_decomposition: orthogonal split refuted at free data; norm-additivity still open'
status: in-progress
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:09Z
updated_at: 2026-10-10T07:01:01Z
parent: qou-l2vh
---

**File:** `QOU/TopologicalMass/cat_eigenspace_decomposition.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/folio/quantum-observable-universe/lean/QOU/TopologicalMass/cat_eigenspace_decomposition.lean

### `cat_eigenspace_decomposition`  —  line 63  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem cat_eigenspace_decomposition [ctx : CatEigenspaceDecompositionContext] : ctx.m_rho = ctx.nrm (ctx.tr (ctx.tau_hat ctx.α)) + ctx.nrm (ctx.tr (ctx.α - ctx.tau_hat ctx.α)) `
- **Cited:** `[manuscript]`
  - [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-cat-eigenspace.md
- **Tractability:** m_rho = nrm(tr(τ̂ α)) + nrm(tr(α−τ̂ α)) eigenspace split; repo categorical-trace infra.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.


## 2026-10-10 — status update (title changed; survey for epic `qou-d8c7`, issue #7547)

Former title began 'PROVE(lean): cat_eigenspace_decomposition — theorem ...'.

Checked on `main` 2026-10-10: `cat_eigenspace_decomposition.lean:113` now declares `def cat_eigenspace_decomposition ... : Prop` (the statement as a proposition, not a theorem with a sorry), and the same file proves `not_cat_eigenspace_decomposition_of_free_data`: with the context's data left free the decomposition as stated is false. This is a scope-(a) negative for the statement as written. What remains open is the norm-additivity input that would make the split hold for the intended data.

Tracked under carrier M2 (`tmvac`) of epic `qou-d8c7`. Stays open (rule 13a).

## Progress Update (Round 94 — PR #8360)

- **Lean 4.24.0 Brick**: `folio/quantum-observable-universe/lean/QOU/QBeta/MagnitudeAssemblyAndConventionFrameBrick.lean` (`0` `sorry`, `0` `axiom`, `0` warnings; `0 CRITICAL, 0 major, 0 advisory` across all 7 directory-mode AST audits).
- **80-dps Probe & Witness**:
  - Probe: `computations/probes/qou_w49j_wjw8_wuxx_wy2h_xs2c_magnitude_and_frame_probe.py` (Commit 1: `f052782a9424286a40e40154d7ef1d0ab55a6d3e`, `scriptHash = 35f305f18243`).
  - Witness: `computations/probes/qou_w49j_wjw8_wuxx_wy2h_xs2c_magnitude_and_frame_probe.witness.json` (Commit 2 / HEAD: `687a015fcc42c84733dfecead6ca9f6e13e3d31d`, `allPassed = true`, `rawFloatCount = 0`).
- **PR**: `litlfred/qou#8360` (`feat/qou-b9cj-w49j-wjw8-wuxx-wy2h-xs2c`).

