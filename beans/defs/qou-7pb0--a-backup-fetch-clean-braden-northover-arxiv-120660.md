---
# qou-7pb0
title: 'A (BACKUP): fetch clean Braden-Northover arXiv 1206.6004 LaTeX source → exact sec4 j-normalization; kills the tau0 0.6% convention residual (only fixes the small band, not the binding constraint)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-25T12:02:29Z
updated_at: 2026-11-16T19:28:00Z
parent: qou-3l2l
---


## Progress 2026-11-16 (PR #8167, `656614697372bd8008f27a4328b66e10d7e1263c` — kept `in-progress` per owner closure rule)

- **Clean Braden–Northover (`arXiv:1206.6004v2`) LaTeX source inspected on `origin/main` (`library/arxiv-1206.6004v2/source/files/sigma12-065.tex` §4.2–§4.4) and formalized in `folio/quantum-observable-universe/lean/QOU/AlphaEM/BradenNorthoverJNormalizationStokes.lean` (`0` `sorry`, `0` custom axioms, wired into `QOU.lean`):**
  - Exact defining equations (`\label{deftau0}`, lines 610–612): `j(τ₀) = -121945/32 = -(5·29³)/2⁵`, `j(τ₀) - 1728 = -177241/32 = -(421²)/2⁵`, `j(5τ₀) = -25/2 = -(5²)/2`, `j(5τ₀) - 1728 = -3481/2 = -(59²)/2`.
  - Dual Weierstrass models `E_{5τ₀} : y² = x³ - 675x - 79650` (`j = -25/2`) and `E_{τ₀} : y² = x³ - 435x - 4210` (`j = -121945/32`), plus complete `(5, 5, 5, 1)` eigenbasis and minimal polynomial `(M_RR - I)(M_RR - 5I) = 0` for `M_RR` (`sigma12-065.tex` eq. `(RRstau)`).
  - Resolves the `0.6%` `τ₀` residual (`tau0_prose_typo_six_permille_resolved`): line 607 of `sigma12-065.tex` prints the prose approximation `-0.5 + 0.185576 i` (a single-digit `5` vs `6` typo in the 4th decimal place) whereas inverting `j(τ₀) = -121945/32` gives `Im(τ₀) = 0.186676462462809923206162881363…` (`275/46669 ≈ 0.5892%` discrepancy).
- **50-dps probe + witness:** `computations/probes/braden_northover_j_normalization_stokes_probe.py` & `braden-northover-j-normalization-stokes.witness.json` (`12/12` assertions passed).
