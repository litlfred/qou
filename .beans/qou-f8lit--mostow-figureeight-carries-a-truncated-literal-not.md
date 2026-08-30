---
# qou-f8lit
title: 'MostowRigidity.figureEight carries a truncated literal, not the exact Vol(4_1)'
status: todo
type: task
priority: high
parent: qou-8mtd
tags:
    - hyperbolic-volume
    - lean
    - precision
created_at: 2026-08-29T19:10:00Z
updated_at: 2026-08-29T19:10:00Z
---

## The defect

`QOU/Encounter/MostowRigidity.lean:235`

    volume := 2.02988321281930   -- :leanval[Vol_4_1]{precision=15}

is a **15-significant-digit truncation**. The corpus records the exact value one
directory over, `QOU/Knot/FigureEightVolume.lean:88`:

    VOL_4_1         := 2 * Cl_2 (π/3)                       -- exact
    VOL_4_1_decimal := 2.029883212819307250011597804990     -- approximation carrier

They differ at the **16th significant digit**. So, in the corpus's own terms,

    volumeInvariant FigureEight  ≠  VOL_4_1

even though both are supposed to name the hyperbolic volume of the same manifold.

## Why it bites (not merely cosmetic)

`QOU/Knot/FigureEightTriangulation.lean` proves, **sorry-free**,

    figureEightTriangulation.volume = VOL_4_1

So instantiating `Encounter.MostowTriangulationBridge.figureEight_literal_eq_triangulation_volume`
— whose conclusion is `(2.02988321281930 : ℝ) = T.volume` — at the corpus's own
`figureEightTriangulation` forces a **false** conclusion. Its hypotheses are therefore
jointly unsatisfiable there: **no correct `HyperbolicVolumeBridge FigureEight` instance
can ever discharge them.**

That theorem is sound, derived, and sorry-free, and it is unusable at the one knot it
names. It is the vacuity trap `ManifoldVolumeBridge` documents — a degenerate model
satisfying every statement — reappearing one file later in the *numbers* rather than in
the relation. Worth internalising: **checking a carrier for degenerate models is not
finished when the relation is fixed; the constants can carry the same defect.**

## Done (2026-08-29)

- `QOU/Encounter/FigureEightVolumeBridge.lean` — the figure-eight statement keyed on the
  **exact** constant, so it applies: `vol_eq_VOL_4_1_of_realises`,
  `vol_eq_two_clausen_of_realises`, and `vol_pos_of_realises` / `vol_ne_zero_of_realises`
  — **positivity DERIVED** from `QOU.Knot.Cl_2_pi_div_three_pos`, closing (for this shape)
  the gap `ManifoldVolumeBridge` deliberately left open.
- The sibling theorem's docstring now carries the correction and points here. Kept rather
  than deleted, because the defect is instructive.

## Still open

1. **Exactify the Mostow instance** — `figureEight.volume := VOL_4_1` instead of the
   decimal. Blocked on three things, none hard but none free:
   - `volume_nonneg := by norm_num` must become a real proof (have:
     `Cl_2_pi_div_three_pos`);
   - `unknot_volume_lt_figureEight_volume` and `figureEight_volume_lt_knot5_2_volume`
     currently discharge by `norm_num` / `rfl` **on the literals** and would need
     genuine bounds on `Cl₂(π/3)`;
   - the `:leanval[Vol_4_1]{precision=15}` codemod contract (`codemod-leanval.ts`) syncs
     that literal from `hyperbolic-volumes.witness.json`; a symbolic value has to be
     taken out of the codemod's scope deliberately, not silently.
2. **Prove the inequality** `2.02988321281930 ≠ VOL_4_1` in Lean. Currently only a
   *numerical* observation — separating them needs a rigorous 16-digit lower bound on
   `Cl₂(π/3)`, which the corpus does not have. Do NOT state it as a Lean fact until it is.
3. **Audit the other `:leanval` literals** for the same truncation class — `vol_5_2`
   (`2.82812208833078`) is the obvious next one, and `VOL_5_2 := 3 * BlochWigner_lob
   fiveTwoShape` is exact in `Knot/FiveTwoVolumeConstant.lean`. Same shape of defect,
   unverified.
