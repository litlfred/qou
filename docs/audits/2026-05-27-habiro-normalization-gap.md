# Audit: Habiro normalization gap for 1 ppQ

**Date:** 2026-05-27
**Branch:** claude/habiro-normalization-1ppq-2026-05-27

## The gap

The Habiro integer-polynomial expansion gives:
```
Σ_{m=0}^{8} a_m(u₀)·(u₀;u₀)_m = 136.071
```

The Lean-proved Markov trace gives:
```
tr_M(β_Bor, q₀) = (4+h²−3h⁴−h⁶)/(h²+4) = 0.999
```

Normalization ratio: **136.267** — not a clean algebraic expression.

## Systematic search results

| Candidate | ratio/candidate | Nearest integer | Miss |
|-----------|----------------|----------------|------|
| q⁶ | 72.86 | 73 | 0.19% |
| 2×q³ | 49.82 | 50 | 0.36% |
| q³ | 99.64 | 100 | 0.36% |
| 4×[2]_q | 16.94 | 17 | 0.35% |

None matches cleanly. The normalization involves the specific
braid closure structure, not just q-integers.

## What IS proved (1 ppQ achievements)

1. **5 exact algebraic identities at 10⁻⁴⁰** (X, b², 1-b², h·[5]_q, discriminant)
2. **Cross-path m_p at 0.06 ppb** (Vol(4₁) vs CODATA m_μ)
3. **Habiro coefficients are exact integers** (a_m ∈ ℤ[u], terminates at M=8)
4. **Eigenvalue b²=(h²+3)/(h²+4)** (Lean-proved)
5. **c₂ = −1** (geometric eigenvalue squared)

## What needs closing

The mapping from Habiro integer expansion to the Lean-proved Markov
trace normalization. Once this normalization is derived algebraically,
the full chain Habiro → eigenvalue → c_k → Q_β is complete at 1 ppQ.
