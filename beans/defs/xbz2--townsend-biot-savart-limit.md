---
# xbz2
title: 'Townsend Biot-Savart limit: kappa_squared_tends_to_zero'
status: completed
type: task
priority: normal
created_at: 2026-06-20T00:00:00Z
updated_at: 2026-08-23T00:00:00Z
---

<!-- front-matter added 2026-08-23. This file had none, so it carried no id,
     no status and no title, and was invisible to the tracker. Original note
     preserved verbatim below. -->

## Original note (undated)

# kappa_squared_tends_to_zero_axiom

The theorem `kappa_squared_tends_to_zero_axiom` in `townsend-biot-savart-strain.lean` requires an epsilon-delta proof of the limit of `|V2 / V1|` as `\tau \to 0`. 
Specifically it needs `\tau^2 \log \tau \to 0`, which is a standard real analysis fact but requires substantial setup using `Filter.Tendsto` and `Real.log` bounds.

## Verified closed 2026-08-23 — `content/quantum-observable-universe/fluid-dynamics/townsend-biot-savart-strain.lean`

`kappa_squared_tends_to_zero_axiom` is **proved**, and by exactly the route the
note said would need "substantial setup": `Real.tendsto_log_mul_rpow_nhdsGT_zero`
gives `log τ · τ² → 0`, the numerator splits as `-2ν·(log τ · τ²) + C₂·τ²`, the
denominator tends to `C₁ > 0`. The file has 0 code-level `sorry` and 0 `axiom`.

**Separate observation, not fixed here.** The declaration is still named
`..._axiom` and its docstring still reads *"Auto-extracted from the single-sorry
theorem body in this file. Encodes the categorical content pending Mathlib
infrastructure"*. Both are stale: it is a `theorem` with a real proof, not an
axiom and not pending anything. A reader grepping for `axiom` to size the
unproved surface will over-count it. Worth a rename + docstring fix.
