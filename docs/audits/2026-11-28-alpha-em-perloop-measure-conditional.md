# Per-loop measure μ₁ = 1/(8π) as a conditional (qou-l4t2)

**Date:** 2026-11-28 · **Bean:** `qou-l4t2` · **Status:** conditional only. μ₁ is not derived.

## Request

Coordinator, on Carl's standing pick: derive μ₁ = 1/(8π) from the phase-4
identification, with the analytic part in `QOU/Transcendental/`.

## What the corpus already settles (corpus-grep)

- 1/(8π) is derived only conditional on R2. The owner ruling of 2026-07-19 says R2 is
  "not lean/derived proved" and declines to canonize it
  (`2026-07-19-alpha-em-r2-owner-ruling.md`).
- Clause B, the channel count 2, is derived (`PerLoopMeasureShadowAssembly.pairCount`).
  Clause A, a₀ = 1/(4π), is conditional (`2026-08-02-alpha-em-perloop-clauses-obstruction.md`).
- R2 reduces to the period map Φ. Φ is proved not derivable from the E⁴ model
  (`2026-08-02-moc-gauss-manin-not-derivable.md`). The next real step is the 08a2
  Gauss–Manin keystone, which is owner-gated and multi-week.
- The germ-viability probe (`qou-rrgk`, completed) found the germ route live
  (m_F = −h/[2]_q), and recorded that this is necessary, not sufficient.

## What this PR adds

| file | content |
|---|---|
| `QOU/MassTheory/EmPerLoopMeasureConditional.lean` | generic field. Class `GermPeriodShare μ₁ a₀` (Φ / R2: `channelCount · μ₁ = a₀`). Conclusion `μ₁ = a₀/2`. The class is satisfiable for every a₀, and μ₁ is unique given a₀. |
| `QOU/Transcendental/MassTheory/EmPerLoopMeasureConditionalReal.lean` | ℝ. Class `HeatKernelLeadingCoeff a₀` (Clause A: `a₀ = 1/(4π)`). Both classes give `μ₁ = 1/(8π)`, and the Form B two-loop coefficient becomes `−s h²/(8π)`. |

Neither class has an instance. All theorems are sorry-free, with axioms
`propext, Classical.choice, Quot.sound`. The transcendental boundary audit is unchanged
(378 outside the boundary, the same as the baseline).

## What this does not do

It does not derive 1/(8π). `perLoop_share_satisfiable` shows that the generic class
contributes only the factor 1/2, so everything else sits in the two hypotheses. Nothing
downstream may use `perLoop_eq_inv_eight_pi` as a derived value. Starting the 08a2
keystone, which would discharge Φ, is Carl's own call.
