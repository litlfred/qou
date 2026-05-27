# Audit: Habiro correction product (1+ℏ²)(1−ℏ²/p(n)) closes to 7.8 ppm

**Date:** 2026-05-28

## Finding

The Habiro normalization bridge has a product correction:

```
Habiro ≈ tr_M × (n!/[n]_q!) × (Vol(4₁)/ℏ²) × (1+ℏ²)(1−ℏ²/p(n))
```

where p(n) = p(9) = 30 is the number of partitions of 9 (= number
of Wedderburn blocks in H₉(q)).

| Level | Correction | Residual |
|-------|-----------|----------|
| 0 | bare | 9495 ppm |
| 1 | ×(1+ℏ²) | 319 ppm |
| **2** | **×(1+ℏ²)(1−ℏ²/p(n))** | **7.8 ppm** |

This is a **41× improvement** over the (1+ℏ²) correction alone,
and a **1218× improvement** over the bare bridge.

## Product structure

Expanding:
```
(1+ℏ²)(1 − ℏ²/30) = 1 + (29/30)ℏ² − ℏ⁴/30
```

This gives:
- c₂ = 29/30 ≈ 0.9667 (observed: 0.9671 — match to 0.04%)
- c₄ = −1/30 ≈ −0.0333

## Why p(n) = 30?

p(9) = 30 is the number of irreducible representations of S₉,
equivalently the number of Wedderburn blocks of H₉(q). The 1/p(n)
factor suggests a **block-averaging** effect: the Habiro cyclotomic
basis distributes over all p(n) blocks, while the Wenzl/seminormal
basis used by tr_M has non-uniform weights y_λ. The mismatch at ℏ²
order is exactly 1/p(n).

## Remaining 7.8 ppm

The third correction factor c₃ ≈ 0.000796 has PSLQ candidates:
- 1/(2·p(n)²) = 1/1800 ≈ 0.000556 → residual 2.4 ppm
- 1/p(n)² = 1/900 ≈ 0.00111 → residual −3.1 ppm

Both are structurally motivated (powers of p(n)), but neither is
exact. The 7.8 ppm residual at ℏ⁶ order may need the full H₉
character theory for closure.

## Cross-references

- Prior: `2026-05-28-habiro-residual-319ppm.md` (Level 1)
- Prior: `2026-05-27-habiro-normalization-decomposition.md` (Level 0)
- Compute: `habiro_correction_product_verify.py`
- Witness: `habiro-correction-product.witness.json`
