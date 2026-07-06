# H₂O bond angle: the `q²` lone/bond ratio is derived, not fitted

**Date:** 2026-06-09. **Status:** derivation (the ratio); kernel-conditional
residual. **Compute:**
[`h2o_angle_q2_symmetric_block.py`](../../computations/h2o_angle_q2_symmetric_block.py)
→ witness `h2o-angle-q2-symmetric-block`.

## Context

The trace-weighted VSEPR model gives a leading H–O–H angle of 107.19°
(observed 104.5°). An inverse probe
([`h2o_angle_gb_truncation_inverse.py`](../../computations/h2o_angle_gb_truncation_inverse.py))
found that the lone/bond weight ratio that lands on 104.5° is `r* ≈ 1.244`,
with `q² = 1.232` a −0.98% **near-match** — which the kernel-robustness scan
demoted to "Coulomb-conditional" (r* drifts at other repulsion exponents).
The owner asked: **does `q²` follow from the C₂ᵥ assembly projector selecting
the symmetric Wedderburn block?**

## Result — yes, exactly

`rem:h2o-c2v-from-projector` establishes that water's C₂ᵥ point symmetry is
the **S₂ stabiliser** (H₁↔H₂ exchange) of the assembly projector `e_{λ,μ}`,
`λ=(24,2,2)`. The S₂-symmetric (trivial) representation is the **symmetric
Wedderburn block** `V₍₃₎` of the local `H₃(q)` — the block the projector
selects (it pairs each hydrogen's electron with oxygen in the symmetric
channel).

On the trivial rep every generator acts as the scalar `q` (`σ_i ↦ q`). Hence

| operator | length | image on `V₍₃₎` |
|---|---|---|
| bonding `σ` | 1 | `q` |
| lone pair `e⁻ = σ₀σ₁σ₀` | 3 | `q³` |

so the lone/bond weight ratio is

$$ \frac{w_{\text{lone}}}{w_{\text{bond}}} = \frac{q^3}{q} = q^2 \qquad\text{(exact — a ratio of Hecke eigenvalues).} $$

**Cross-check across all three blocks** (numerical, Hoefsmit seminormal):

| block | `σ ↦` | `e⁻ ↦` | lone/bond |
|---|---|---|---|
| **sym `V₍₃₎`** (C₂ᵥ-selected) | `q` | `q³` | **`q² = 1.23205`** (matches to 1e-9) |
| std `V₍₂,₁₎` | `q, −q⁻¹` | `±1` | `0` (e⁻ trace cancels) |
| alt `V₍₁,₁,₁₎` | `−q⁻¹` | `−q⁻³` | `q⁻²` |

Only the symmetric block — the one the projector selects — gives `q²`.

## What this promotes, and what it does not

- **Promoted:** the ratio `q²` is now **derived** from the block projection +
  the Hecke eigenvalues. It is **kernel-independent** — it is not a fit to the
  angle, and it does not depend on the VSEPR repulsion exponent. The earlier
  "Coulomb-conditional near-match" framing no longer applies to the ratio.
- **Still approximate:** feeding the derived `r = q²` into the trace-weighted
  VSEPR (Coulomb, n=1) gives `θ = 104.72°` — a **+0.22°** residual to observed
  104.5°. That residual carries the VSEPR-kernel + points-on-a-sphere geometric
  approximation (the bending potential's exact shape), **not** the ratio.

So the lever the owner named ("weighting of active sets / GB order changes the
angle") resolves on its principal axis: the lone-pair-to-bond weight ratio is
`q²`, forced by the C₂ᵥ-selected symmetric Wedderburn channel.

## Follow-ups

1. A one-line Lean lemma: on the trivial rep of `H₃(q)`, `ρ(σ₀σ₁σ₀) = q² · ρ(σ₀)`
   (immediate from `ρ(σ_i) = q`) — would anchor the ratio formally.
2. Promote to a `remark` interpreting `prop:h2o-bond-angle-shift` with
   `interprets`, citing this witness, once the `q²`-from-projector statement is
   wanted in the narrative.
3. The +0.22° residual is a geometry/kernel question (exact bending potential),
   separate from the now-settled ratio.
