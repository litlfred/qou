---
# qou-gl343
title: 'G3.4c: dim HW_λ = f^λ and HW_λ ≅ S_λ as H-modules'
status: in-progress
type: task
priority: normal
tags:
    - quark-state
    - schur-weyl
created_at: 2026-11-15T10:20:00Z
updated_at: 2026-11-15T11:10:00Z
parent: qou-gl34
---

Character route (coordinator suggestion): weight multiplicities in V^{⊗n} against Kostka numbers, the G2 trace identity Tr(K|λ-block) = s_λ(1,q²,…) and linear independence of Schur polynomials.

Owner ruling via coordinator 2026-11-15: "work G3.4, dispatch siblings". Direct highest-weight route (session 7a).

## Progress 2026-11-15
- Done (PR stacked on #7870): `finrank_hwSpace_le_numSYT` — for dominant μ, dim HW_μ ≤ #SYT(rowDiagram μ).
  Route: branching bound (peel the last site; first nonzero slice is HW of weight μ − e_x) +
  dominance + SYT branching rule. This is the inequality (★) needed by stream 14's double-centraliser
  argument (#7864). Sorry-free, standard axioms.
- Open: the bridge `rowDiagram μ = partitionShape λ` (sorted nonzero parts), so the bound reads
  with the `Fintype.card (StandardYoungTableau (partitionShape λ))` used in `finrank_range_jimbo`.
- Open (the "=" and HW_λ ≅ S_λ halves): follow from G3.4 itself once the sandwich closes.
