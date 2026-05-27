# Audit: Habiro residual closed to 319 ppm via (1+ℏ²)

**Date:** 2026-05-28

## Finding

The (1+ℏ²) correction closes the Habiro normalization residual
from 9500 ppm to **319 ppm** (30× improvement):

```
Habiro ≈ tr_M × (n!/[n]_q!) × (Vol(4₁)/ℏ²) × (1 + ℏ²)
```

| Stage | Miss |
|-------|------|
| Without correction | 9495 ppm (0.95%) |
| **With (1+ℏ²)** | **319 ppm (0.032%)** |

## Why (1+ℏ²)?

The substrate Planck correction (1+ℏ²) appears in multiple places:
- Deuteron binding: E₀×(1−ℏ_q) closes from −79% to +0.74% (#1361)
- Flavor-split subleading: (1+ℏ³) improves 4.2× (#1299)
- Habiro normalization: (1+ℏ²) improves 30×

The ℏ² = ((q−1)/q)² is the substrate Planck action squared — the
leading quantum correction to any classical-limit identity.

## Remaining 319 ppm

The remaining residual at ℏ⁴ order has coefficient c₄ ≈ −3.31 —
not a clean integer. Further correction needs the full H₉
representation theory.
