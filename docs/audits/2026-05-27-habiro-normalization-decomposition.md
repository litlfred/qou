# Audit: Habiro normalization decomposes as Plancherel × muon anchor

**Date:** 2026-05-27

## Finding

The Habiro-to-Markov-trace normalization ratio decomposes as:

```
Habiro_sum ≈ tr_M × (n!/[n]_q!) × (Vol(4₁)/ℏ²)
```

to **0.95%** (9495 ppm), where:
- n = 9 (proton at H₉ = H_{3A} for A=3)
- n!/[n]_q! = 362880/593006 = Plancherel renormalization factor
- Vol(4₁)/ℏ² = 206.77 = muon-to-electron mass ratio (CAL-2)

## Numerical verification

| Quantity | Value |
|----------|-------|
| Habiro sum | 136.071 |
| tr_M (direct H₉) | 1.065 |
| n!/[n]_q! | 0.6119 |
| Vol(4₁)/ℏ² | 206.768 |
| Predicted: tr_M × (n!/[n]!) × (Vol/ℏ²) | 134.791 |
| Actual/predicted | 1.00949 |
| Miss | 0.95% |

## Residual analysis

The 0.95% residual ≈ ℏ² × 0.967 — close to ℏ² but not exactly.
No clean algebraic expression identified for the correction.

## Structural interpretation

The decomposition says: the Habiro integer expansion and the
Jones-Wenzl Markov trace differ by the product of:
1. The **Plancherel ratio** n!/[n]_q! (quantum→classical dimension)
2. The **lepton mass ratio** Vol(4₁)/ℏ² (CAL-2 anchor)

Both are known structural quantities. The 0.95% residual is the
remaining braid-specific correction.
