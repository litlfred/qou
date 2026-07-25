# The α_EM loop-measure `1/π` weight — the χ-vs-g obstruction (spectral-zeta side)

**Date:** 2026-07-25 · **Axis:** α_EM per-loop measure (`1/(8π)`) · **Tier:** research
attack (sharpens the open problem; no derivation manufactured) · **Discipline:**
`1/(8π)` stays a phase-4 identification; no instance registered; critical-distance —
no fit to the target.

## Two `1/π` pieces, two topological characters

The α_EM coupling on Bring's genus-4 surface has two `1/π`-type contributions with
**different** topological origins:

| piece | value | topological character | status |
|---|---|---|---|
| Bloch–Wigner term | `2/(3π) = 2g/(4π(g−1))`\|_{g=4} `= b₁/Area` | **Euler** (`Area = −2πχ = 12π`) | **PROVED** (Gauss–Bonnet; `bring_zero_mode_additive_form`) |
| per-loop **measure** | `1/(8π) = 1/(π·b₁) = 1/(2π·g)` | **genus** (`∝ g`) | **OPEN** |

## The obstruction, made precise

Every standard 2D spectral-zeta invariant is **Euler-characteristic-linear** (`∝ χ`)
or extensive:

- `a₀` (heat-kernel area term) `∝ Area` — extensive, μ-dependent (the fitting trap
  identified in `alpha_em_permode_weight_probe.py`);
- `a₁ = χ/6` (Gauss–Bonnet) `∝ χ`;
- `ζ_Δ(0) = χ/6 − 1` `∝ χ`;
- Ray–Singer torsion (scalar) — `χ`-controlled.

The **proved** `2/(3π)` term is exactly such an Euler quantity (`b₁/Area`, `Area =
12π`). But the **open** loop measure `1/(8π) = 1/(2π·g)` requires a **genus-linear**
(`∝ g`) source. Since `χ = 2 − 2g` is **not** proportional to `g`, **no standard
spectral invariant forces `1/(2π·g)`.** That is the precise obstruction: the loop
weight lives in a `g`-linear channel, and standard heat-kernel geometry produces
`χ`-linear ones.

## The `½·a₀` chiral decomposition is a g=4 coincidence

A tempting derivation writes `1/(8π) = ½·a₀` with `½ = dim H^{1,0}/dim H¹ = g/(2g)`
(the Hodge chiral ratio) and `a₀ = 1/(4π)` (the 2D heat-kernel unit). Both factors
are forced, and the product hits `1/(8π)` exactly. **But the chiral ratio is
`g`-independent** (`½` for every Riemann surface), so this decomposition gives
`1/(8π)` on *every* surface — it cannot select Bring (`g=4`). The numerical match at
`g=4` is therefore a **coincidence**, not the Bring-specific mechanism. (This is the
kind of shape-compatible-but-selection-free "derivation" the anti-fit discipline
flags — recorded honestly rather than claimed.)

## Verdict

The loop-measure `1/π` weight is **not forced by standard spectral-zeta
invariants**. A genuine derivation needs a **genus-linear** spectral quantity —
candidates that are `g`-linear rather than `χ`-linear:

1. **Ray–Singer / Quillen with an odd zero-mode structure.** The holomorphic
   `H^{1,0}` has `dim = g` (genus-linear); a determinant-of-`∂̄` (not the scalar
   Laplacian) counts `g`, not `χ`. The sibling Quillen-curvature attack (#4201)
   found `a₀ = 1/(4π)` from forced legs with "residual exactly 2 = the open ½" —
   consistent with the `½` being the genuine open factor here.
2. **The archimedean dilogarithm regulator** (`conj:dilogarithm-archimedean-limit`)
   — the framework's canonical μ-independent `π`, distinct from both the
   heat-kernel and Gauss–Bonnet `π`.

Neither is a standard heat-kernel invariant, which is exactly why `1/(8π)` is hard.

**This converges with** `alpha_em_permode_weight_probe.py` (the ζ-determinant is the
fitting trap) and the `τ=W` adversarial audit
([`2026-07-25-alpha-em-b2-tau-w-derivability-adversarial.md`](2026-07-25-alpha-em-b2-tau-w-derivability-adversarial.md),
the magnitude is a free scalar): **the α_EM `1/(8π)` magnitude is not derived by any
machinery currently in hand.** The form is forced; the magnitude is open; the
specific missing ingredient is a genus-linear (not Euler-linear) spectral source.

No fit; no instance; `1/(8π)` phase-4; nothing wired. Witness:
`alpha-em-1pi-spectral-zeta.witness.json`.
