# The A=3 branching reduction and the modulus lift are a Pythagorean pair — and the branching's own asymmetry nearly closes only at the CABLED level

**Date:** 2026-08-09 · **Bean:** `qou-jqof` (derive the off-block amplitude) / `qou-prjo`
(transverse surviving object) · **Branch:** `claude/z-c-k-f-map-keystone-ub5yix` · **Tier:**
formalize-first (Lean sorry-free) + scope-(a) numeric. **Scope:** structural + near-miss lead;
nothing fitted, nothing wired, `1.585` NOT closed.

## The composition

`A3OffBlockDerivation` derives from the `H₃(q)` Wedderburn branching, with **no** freedom, the
super-blocks `A = D = (a+b)/2`, `B = C = (a−b)/2` (bar-odd), and the self-adjoint even-face
**reduction** `factor_sa = 1 − x²`, `x = (a−b)/(a+b)` (`magnitudeFactor_le_one`: `≤ 1`).
`BirkhoffBarOddPythagorasBridge` proves the bar-odd unit-modulus carrier squares to `−1`, so the
modulus lift is the quadrature `factor_sa² + s²`. Composing them
([`A3BranchingModulusReflection.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/A3BranchingModulusReflection.lean),
sorry-free):

> **`pythagorean_triple`:** `(1 + x²)² = (1 − x²)² + (2x)²`.
> **`lift_eq_two_sub_reduction`:** `lift = 1 + x² = 2 − factor_sa`.

The branching **reduction** `1 − x²` is one leg, the **transverse** datum `2x` the other, the
**lift** `1 + x²` the hypotenuse. The bar-odd unit-modulus reading reflects the reduction
(`≤ 1`) into a lift (`≥ 1`) across `1`.

## The numeric test — can the branching supply `x`?

The observed lift `r* = μ₃/c₃ ≈ 1.585` needs `x² ≈ 0.585` (`x ≈ 0.765`). The Borromean
`β = (σ₁σ₂⁻¹)³` gives **equal** 1-dim characters (`χ₍₃₎ = χ₍₁,₁,₁₎ = 1`), so `x` comes purely
from the bar-asymmetric weight
([`a3_branching_asymmetry_vs_required_probe.py`](../../computations/qbeta/a3_branching_asymmetry_vs_required_probe.py),
0 free params):

| weight | `x²` | `r* = 1 + x²` |
|---|---|---|
| symmetric Wedderburn `d_q²/[n]!` (bar-even) | 0 | 1.00 |
| content `q^{±3}` (bare H₃) | 0.09 | 1.09 |
| content `q^{±6}` | 0.31 | 1.31 |
| **content `q^{±9}` (≈ H₉ cabling scale)** | **0.54** | **1.54** |
| *required* | *0.585* | *1.585* |

- **Bare H₃ is ~6× short** in `x²` — the fixed 3-strand branching cannot supply the magnitude.
- **The CABLED level nearly closes.** `c₃` is computed at **H₉** (three width-3 cables, 9
  strands). Content `c ≈ 9` gives `r* ≈ 1.54`, only ~3% short of 1.585 (exact needs
  `c ≈ 9.66`). The transverse leg `2x` lives at the **cabled/transverse** level, not the bare
  branching — exactly bean `qou-prjo`'s transverse (H₉ Birkhoff/Stokes surface-curvature)
  object — where the modulus bridge **nearly** reproduces the magnitude.

## Honest status

- **Proved (Lean):** the Pythagorean structure `lift = 2 − factor_sa`, the reflection about 1,
  `reduction ≤ 1`.
- **Near-miss lead (numeric):** the cabled content `c ≈ 9` gives `r* ≈ 1.54`; the residual
  `9 → 9.66` (equivalently `1.54 → 1.585`) is the open fine structure — plausibly the same
  order-normalized coefficient gap seen elsewhere in the A-scaling.
- **NOT closed:** `q^{content}` is one weight convention; the exact cabled-content interpretation
  (why `c ≈ 9` and not the H₉ trivial content `36`) and the `9 → 9.66` residual are unresolved;
  the E-scale normalization `κ = a+b` is assumed. No fit; `r*`/`μ₃`/`c₃` never inverted; nothing
  wired.

## Cross-references
- Bridge: `2026-08-09-a3-barodd-unitmodulus-pythagoras-bridge.md`, `BirkhoffBarOddPythagorasBridge.lean`
- Branching: `A3OffBlockDerivation.lean` (`magnitudeFactor_eq`, `magnitudeFactor_le_one`)
- Surviving transverse object: bean `qou-prjo`; off-block derivation: bean `qou-jqof`
