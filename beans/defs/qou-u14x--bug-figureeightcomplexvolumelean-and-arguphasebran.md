---
# qou-u14x
title: "BUG: FigureEightComplexVolume.lean and ArgUPhaseBranchSelection.lean use INCONSISTENT NZ leading coefficients. FigureEight: Im V₄₁ = (√3/4)(Re²u−Im²u) from a₂=i√3/4. ArgU: nzImVolume = (√3/2)r²sin(2φ) from τ=2i√3, \U0001D519≈\U0001D519(0)−(τ/4)u². The correct Im[−(τ/4)u²] = −(√3/2)(Re²u−Im²u) = −(√3/2)r²cos(2φ), which is cos not sin and has opposite sign to the √3/4 version. Either: (1) the τ value is wrong, or (2) the a₂ value is wrong, or (3) the NZ normalisation convention differs. Must resolve before Δ_λ assembly."
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-27T15:22:44Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: DONE.** Done: sin→cos fixed (d60d98d484). qou-pzzl was scrapped into this bean, so the residual factor-2 (Φ vs 𝔙) question should be recorded on qou-yh67. Residual inconsistency: the docstrings disagree on τ (FigureEight says −i√3, the audit +i√3, this title 2i√3). Absolute sign and scale depend on the meridian normalisation (u=log M vs ½log λ), which no file pins.

Evidence: Fix landed in d60d98d484: `ArgUPhaseBranchSelection.lean:59 nzImVolume = (√3/2) r² cos(2φ)` (was sin), with audit `docs/audits/2026-07-27-nzImVolume-sincos-convention-bug.md`. Both files now give Im ∝ +(Re²u−Im²u). The remaining factor 2 is the documented Φ=2𝔙 object choice (`ObservableComplexVolumeVsFullPotential.lean`, sorry-free), tracked by qou-yh67. My A-polynomial check (scratchpad apoly5.py) reproduces the cos form. Its magnitude depends on the meridian normalisation: u=log M gives Im Φ/((√3/4)u²) = ±4.000003 at u=0.001, with sign set by branch.

Status: `todo` → `completed`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
