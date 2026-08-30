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

---

## 2026-08-30 — the `:leanval` audit, run. The defect class is BOUNDED.

Follow-up item 3 ("audit the other `:leanval` literals") is done. **16 sites, 7 keys.**

| key | sites | exact closed form in corpus? | verdict |
|---|---|---|---|
| `Vol_4_1` / `vol_4_1` | 7 | **yes** — `2·Cl₂(π/3)` | **DEFECT** (15- and 11-digit truncations) |
| `vol_5_2` | 2 | **yes** — `3·BlochWigner_lob fiveTwoShape` | **DEFECT** (15-digit truncation) |
| `m_p_MeV` | 1 | no — CODATA measurement | not a defect |
| `m_e_MeV` | 3 | no — CODATA measurement | not a defect |
| `q_0` | 2 | no — root of a transcendental eq; the 50-dps witness IS canonical | not a defect |
| `mostow_gap_4_1` | 1 | no — a deliberate conservative under-approximation | not a defect |

**The discriminator, stated so nobody "fixes" the wrong half:** a truncated literal is a
defect only where the corpus **also** carries an exact closed form for the same quantity
*and* something treats the two as interchangeable. A CODATA mass has no closed form to
disagree with; truncation is the correct representation of a measurement. `mostow_gap`
is deliberately loose. Only the two hyperbolic volumes qualify.

**`vol_5_2` confirmed to carry the identical defect.** `MostowRigidity.knot5_2.volume
:= 2.82812208833078` against exact `2.8281220883307831627638988092766…` — diverging at
digit 16 — and `fiveTwoTriangulation_volume : fiveTwoTriangulation.volume = VOL_5_2` is
proved sorry-free, so the unsatisfiability argument transfers verbatim.

### Done: `QOU/Encounter/FiveTwoVolumeBridge.lean`

`vol_eq_VOL_5_2_of_realises`, `vol_eq_three_blochWigner_of_realises`, and
`vol_lt_iff_of_realises` — the last stated as an **equivalence**, not an inequality,
because the corpus does not carry `VOL_4_1 < VOL_5_2` as a proved fact:
`MostowRigidity`'s comparison discharges by `norm_num` on the two **truncated literals**,
which is a statement about the decimals rather than about the constants.

### ⚠ The 4₁ positivity was a SPECIAL CASE, not the start of a pattern

`FigureEightVolumeBridge.vol_pos_of_realises` exists; the 5₂ analogue **does not, and
that is the honest outcome**. The 4₁ proof went through `Cl_2_pi_div_three_pos`, which
exists only because the 4₁ shape sits on the unit circle so its Bloch–Wigner value *is*
a Clausen value. The 5₂ shape is a root of `X³ − 2X² + 3X − 1` and is not.

Measured: the corpus has **no** `0 < BlochWigner_lob z` for `0 < z.im`. What it has is
`BlochWigner_lob_real_eq_zero` — vanishing *on the reals*, the opposite boundary.

So the general positivity `ManifoldVolumeBridge` declined to assume is still open.
Recorded explicitly because "we proved it for 4₁" invites the assumption that 5₂
follows.

### Still open, unchanged

1. Exactify both Mostow instances (`figureEight` and now `knot5_2`) — still needs real
   bounds for the comparison theorems and a deliberate `:leanval` codemod decision.
2. The inequalities as Lean facts (needs rigorous 16-digit bounds).
3. General `0 < D(z)` on the upper half plane.
