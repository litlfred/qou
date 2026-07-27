# Convention bug: ArgUPhaseBranchSelection.lean `nzImVolume` uses sin(2φ) but should use cos(2φ)

## Date: 2026-07-27
## Bean: qou-u14x
## Branch: claude/delta-lambda-magnitude-derivation-2026-07-27

## Summary

The `nzImVolume` function in `ArgUPhaseBranchSelection.lean` is **defined with
sin(2φ) where the correct NZ formula has cos(2φ)**. This makes the function
compute the WRONG imaginary part of the complex volume.

## Evidence

Definitive check from the A-polynomial of 4₁ (CCGLS):

```
A(L,M) = M⁴L² − (M⁸−M⁶−2M⁴−M²+1)L + M⁴
Φ(u) = ∫₀ᵘ log(−L(t)) dt
```

Numerical evaluation at real u = 0.001, 0.01, 0.05, 0.1:

| u    | Im Φ / ((√3/4)u²) |
|------|-------------------|
| 0.001 | 2.0000           |
| 0.01  | 2.0000           |
| 0.05  | 2.0008           |
| 0.1   | 2.0033           |

So **Im Φ = (√3/2)u² = (√3/2)r²cos(2φ)** (not sin).

Also: **τ = v/u|₀ = +i√3** (geometric branch), NOT −i√3 or 2i√3.

## Convention map

| Object | Convention | Formula | Status |
|--------|-----------|---------|--------|
| `Φ` (NZ potential) | Full potential | Im Φ = (√3/2)r²cos(2φ) | **Ground truth** (A-polynomial) |
| `V₄₁` (FigureEight Lean) | Half-potential: V₄₁ = Φ/2 + const | Im V₄₁ = (√3/4)(Re²u − Im²u) = (√3/4)r²cos(2φ) | ✅ **CORRECT** |
| `nzImVolume` (ArgU Lean) | Full potential (claimed) | nzImVolume = (√3/2)r²**sin**(2φ) | ❌ **BUG: should be cos** |

## Affected theorems (all in ArgUPhaseBranchSelection.lean)

| Theorem | Claims | Status |
|---------|--------|--------|
| `nzImVolume_real_ray` | S = 0 on real ray | ❌ WRONG: Im Φ(real u) = (√3/2)u² ≠ 0 |
| `nzImVolume_quarter_turn` | S = (√3/2)r² at φ=π/4 | ❌ WRONG: Im Φ at φ=π/4 is cos(π/2)=0 |
| `nzImVolume_phase_hasDerivAt` | ∂S/∂φ|₀ = √3r² | ❌ WRONG: ∂(cos)/∂φ|₀ = 0 (stationary) |
| `phase_channel_anchor_swing_zero` | Anchor swing = 0 | ❌ WRONG: both anchors have same Im Φ > 0 (not 0) |
| `phase_sensitivity_times_frozen_displacement` | (∂S/∂φ)·Δφ = 0 | Mixed: Δφ=0 IS correct, but ∂S/∂φ|₀ = 0 (not √3r²) |
| `substrate_meridian_arg_zero` | arg(2·ln q₀) = 0 | ✅ CORRECT (independent of nzImVolume) |
| `anchor_phase_difference_zero` | Δ(arg u) = 0 | ✅ CORRECT (independent of nzImVolume) |

## Unaffected files

| File | Status | Reason |
|------|--------|--------|
| `FigureEightComplexVolume.lean` | ✅ CORRECT | Uses V₄₁ = half-potential, all theorems verified |
| `DeltaLambdaBindingAssembly.lean` | ✅ CORRECT | Uses V₄₁ directly, not nzImVolume |
| `PhiBSArgumentIdentification.lean` | ✅ CORRECT | SDeformedVolumeChannel uses abstract V, not nzImVolume |

## Physical consequence

The "wall" (real substrate → S = 0) is **wrong**. With the correct formula:
- Im Φ(real u) = (√3/2)u² > 0 for u ≠ 0
- Im V₄₁(real u) = (√3/4)u² > 0 for u ≠ 0
- The CS part is NONZERO for real deformations (this is physically correct — amphichirality only pins CS = 0 at the complete structure u = 0, not for all real u)

The S-leak for real substrate u = 2·ln q₀ ≈ 0.209 is:
- Im V₄₁ = (√3/4)·0.209² ≈ 0.0189 (without A_ω)
- 3·Im V₄₁ ≈ 0.0567 (with A_ω = 3)

Neither matches the measured S values (+0.0097 muon, −0.0395 proton), confirming that u must be complex (ϑ_K ≠ 0).

## Recommended fix

Replace `sin(2 * φ)` with `cos(2 * φ)` in the `nzImVolume` definition, then update all downstream theorems. The key change: `nzImVolume_real_ray` becomes `nzImVolume_real_ray : nzImVolume r 0 = (√3/2) * r ^ 2` (nonzero), and the wall theorem changes character.

Alternatively: deprecate `nzImVolume` and use `imV₄₁` from FigureEightComplexVolume (which is correct).
