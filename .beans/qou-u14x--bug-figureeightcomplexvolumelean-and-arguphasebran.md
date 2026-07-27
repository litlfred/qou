---
# qou-u14x
title: "BUG: FigureEightComplexVolume.lean and ArgUPhaseBranchSelection.lean use INCONSISTENT NZ leading coefficients. FigureEight: Im V₄₁ = (√3/4)(Re²u−Im²u) from a₂=i√3/4. ArgU: nzImVolume = (√3/2)r²sin(2φ) from τ=2i√3, \U0001D519≈\U0001D519(0)−(τ/4)u². The correct Im[−(τ/4)u²] = −(√3/2)(Re²u−Im²u) = −(√3/2)r²cos(2φ), which is cos not sin and has opposite sign to the √3/4 version. Either: (1) the τ value is wrong, or (2) the a₂ value is wrong, or (3) the NZ normalisation convention differs. Must resolve before Δ_λ assembly."
status: todo
type: task
created_at: 2026-07-27T15:22:44Z
updated_at: 2026-07-27T15:22:44Z
---

