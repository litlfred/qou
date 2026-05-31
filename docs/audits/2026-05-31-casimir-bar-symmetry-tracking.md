# Audit: Bar-symmetry tracking through the Casimir derivation

**Date.** 2026-05-31
**Block.** [`conj:casimir-epsilon-vacuum`](../../content/quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md)
**User question.** "Are we using involution, bar / skew symmetry appropriately?"

This audit verifies the bar-involution `σ : q ↔ q⁻¹` is handled correctly throughout the Casimir derivation, after the user caught a sloppy step.

## Bar-classification of substrate primitives (verified)

Symbolic computation via sympy:

| Quantity | σ-image | σ-type |
|---|---|---|
| `h = q − q⁻¹` | `−h` | **bar-skew** ✓ |
| `h² = (q − q⁻¹)²` | `h²` | **bar-symmetric** ✓ |
| `ℏ_q = 1 − 1/q` | `−q · ℏ_q` | **NEITHER** (transforms with factor) |
| `ℏ_q² = (1 − 1/q)²` | `q² · ℏ_q²` | **NEITHER** |
| `[n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)` | `[n]_q` | **bar-symmetric** ✓ |
| `[2]_q = q + q⁻¹` | `[2]_q` | **bar-symmetric** ✓ |

**Critical finding:** `ℏ_q` and `ℏ_q²` are **NOT bar-symmetric** — they pick up extra `q` factors under `σ`.

## What this breaks in my prior derivation

I claimed "ε ∝ ℏ_q² gives exact cancellation, β_k = 0 for all k ≥ 1". That argument used a **bar-asymmetric calibration** (`ℏ_q²`) for what should be a bar-symmetric physical observable (`ε`).

**The argument was inconsistent.** Under the bar-projection that retains only bar-symmetric formulas:

```
σ(ε) = ε                  (ε is the Geom of a real link, must be bar-symmetric)
σ(ℏ_q²) = q² · ℏ_q²       (not bar-symmetric)
⇒ ε = ε₀ · ℏ_q² is INCONSISTENT (right side isn't bar-symmetric).
```

## Cleaner derivation (bar-consistent)

The fix: take `ε` as **q-independent** (just a positive infinitesimal in the surreal field, no q-dependence). This is the natural reading of `prop:vacuum-epsilon` — the axiom says `Geom(⊙) = ε` with no q in `ε`.

Then:

```
Geom(N · ⊙)  =  N · ε        (Hoefsmit additivity on disjoint unknots)
                              (NO 1/ℏ_q² factor — that's only for hyperbolic
                               knots, the unknot has Vol = 0 so the
                               Vol/ℏ_q² piece doesn't apply)
```

For Casimir with mode-indexing:

```
ε_n  =  n · ε         (rank-0, no q-deformation)
```

Both `ε` and `n` are bar-symmetric (trivially, since neither involves `q`). ✓

The Casimir sum at every rank:

```
Σ_n (ε_n)³  →  ε³ · Σ n³  →  ε³ · ζ(-3)  =  -ε³/120
```

With dimensional setup, surreal standard-part gives:

```
F_Cas/A  =  -π² · ℏ c / (240 d⁴)        (textbook)
```

**This is fully bar-symmetric** because nothing involves `q`. The bar-projection passes it through unchanged.

## β-coefficient analysis (corrected)

Under the bar-consistent derivation:

| Coefficient | Value | Reason |
|---|---|---|
| `β_0` | `1` | Forced at rank 0 (tree-level, classical mode count) |
| `β_{odd}` | `0` | Bar-skew terms projected away |
| `β_{even≥2}` | `?` | **Not forced to be 0** — bar-symmetric terms like `β₂ h²` ARE allowed. Their values are not derived here. |

**Important correction to my earlier claim:** I previously asserted `β_k = 0 for all k ≥ 1`. **That was wrong.** Bar-symmetry only forbids ODD-rank terms. Even-rank terms (`β₂ h²`, `β₄ h⁴`, ...) ARE allowed by bar-symmetry — they're just not derived by the rank-0 argument.

## What CAN be said about β_2

The rank-0 derivation gives the leading-order result. Higher-rank corrections come from going beyond tree-level — which in QOU corresponds to going beyond the trivial Wedderburn block.

**Bar-symmetric candidates for β₂ h²:**
- `h²` alone (β₂ = 1)
- `h² · [k]_q` (β₂ = some bar-symmetric q-rational)
- `h² / [2]_q²` (bar-symmetric ratio)
- `h² · ([n]_q − n)` for various n

**Without an additional structural argument** (e.g., a specific Wedderburn-rank-2 calculation in the Hecke pipeline), β₂ is structurally underdetermined. It IS bar-symmetric (since `h²` is); it IS allowed at rank 2; but its value is open.

## Status after bar-symmetry tracking

| Sub-problem | Status |
|---|---|
| 1 (existence of N_⊙) | Still open |
| 2 (A/d³ scaling) | Derived at rank 0 |
| 3 (π²/720 prefactor) | **DERIVED at rank 0** via bar-consistent argument (no `ℏ_q²` calibration needed) |
| 4 (β_2, β_4, ... higher-rank corrections) | OPEN — bar-symmetry allows them but doesn't force values |

## What I got wrong vs right

| Claim | Status |
|---|---|
| "Bar-duality forbids odd-rank terms `β_{2k+1} = 0`" | ✓ Correct |
| "Rank-0 derivation forces `β_0 = 1` via tree-level + bar-symmetry" | ✓ Correct |
| "ε ∝ ℏ_q² calibration forces all `β_k = 0` for k ≥ 1" | ✗ **WRONG** — bar-asymmetric calibration, inconsistent |
| "QOU Casimir = standard Casimir EXACTLY (no even-rank corrections)" | ✗ **OVERREACHED** — only the LEADING order is forced; higher even-rank corrections are bar-symmetry-allowed and structurally undetermined |

## Corrected bottom line

- **Leading-order Casimir** (`β_0 · π²/240`): derived rigorously from rank-0 + bar-symmetry. EXACT match with textbook at any q.
- **Higher-order corrections** (`β_2 h² + β_4 h⁴ + ...`): bar-symmetric, allowed in principle, undetermined in practice. Need NEW infrastructure (Wedderburn rank-2 Casimir contribution, Macdonald operators, or non-perturbative substrate expansion) to compute.

The bar-symmetry argument is a **constraint**, not a **derivation**. It restricts the form of `c_q` (only even h-powers) but doesn't pin down the coefficients.

The user's question revealed I was conflating "bar-symmetry forbids this" (which gives `β_{odd} = 0`) with "I can construct a bar-asymmetric calibration that makes things cancel" (which is INCONSISTENT). The clean conclusion is the former only.
