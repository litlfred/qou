---
# qou-pbjv
title: 'Infra: Hecke algebra H_n(q) as braided monoidal category in Lean (n≥3) — τ-functor F1/F2 source'
status: todo
type: feature
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-07-18T23:53:03Z
updated_at: 2026-10-04T15:14:38Z
parent: qou-o9ge
---

The dominant Mathlib gap behind the τ-functor (PR #4028). Mathlib has no H_n(q) braided monoidal category for n≥3. Needed to state τ:C→Vec_ℝ as a genuine braided monoidal functor (F1 monoidal, F2 braided/R-matrix→braiding). Multi-week, tiered: honest §3b conjecture-classes at the apex, concrete proved slices at n=2,3 (H3.trM already sorry-free). Build the category object + braiding from the R-matrix + hom-spaces incrementally. Blocks qou-msof (braided morphism action).
