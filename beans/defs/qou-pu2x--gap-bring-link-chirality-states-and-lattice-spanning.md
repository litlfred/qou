---
# qou-pu2x
title: 'GAP: Bring-link chirality — which object are the states, and does Γ₄ span M₂(ℝ) (Borel density)'
status: todo
type: task
priority: normal
tags:
    - 8f-open
created_at: 2026-11-15T12:00:00Z
updated_at: 2026-11-15T12:00:00Z
parent: qou-wqto
---

Created from step (b) of issue #7783 / PR #7820. See `QOU/BringConeSplitChirality.lean`.

The split model of Bring's link `UT(Σ₄) = SL₂(ℝ)/Γ₄` carries an sl₂ triad. Proved there, sorry-free: the Hopf-model flip `M_j` has fixed rays; the fibre rotation `M_i` is the only ray-free Reeb operator; `M_j` is itself a grading that `M_i` flips. A left multiplication `L_u` commuting with a set whose span contains `i` and `j` is a scalar.

**Open, exactly:**
1. **Lattice spanning.** `commutes_span_scalar` takes as a hypothesis that the ℝ-span of Bring's surface group `Γ₄ ⊂ SL₂(ℝ)` contains `i, j`. This follows from Borel density (a cocompact lattice is Zariski dense), which is neither in the corpus nor in `library/`. Grep `library/INDEX.md`, `sections/` and `ocr/` before formalising; cite or formalise it.
2. **What the states are.** On points of `SL₂/Γ₄` only `M_i` (reduced norm +1) acts; right multiplication by `j` or `k` (norm −1) leaves `SL₂`. So the pair (grading `M_j`, flip `M_i`) is a statement about the module `M₂(R)` and its rays, not about points of the link. Which object V10's `State` should be on Bring's cone is not fixed anywhere: rays of the module, points of `UT(Σ₄)` (where `M_i`, right translation by the quarter-turn rotation in `SL₂`, should act as the fibre half-turn `v ↦ −v` under `PSL₂(ℝ) ≅ UT(ℍ²)`; that is standard, but NOT verified or formalised here), or sections over `Σ₄`. That is the CR-geometry step `archimedean-chirality.md` asserts without deriving.

Do not choose (2) by which option reproduces the SM labels (NO FITTING).
