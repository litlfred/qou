# Family A restated + variants investigation

**Date:** 2026-05-18
**Branch:** `claude/workplan-0b-mn-substrate` (PR #751)
**Trigger:** User question — "why 3% in Family A? was that just first/second order approx? maybe more? investigate"

## Family A: EXACT (not truncated)

Family A is `(1/4) · Σ_{λ ⊢ 4} dim_q V_λ`. The quantum dimensions at H_4 are **exact polynomials in h² = (q−q⁻¹)²** with NO higher-order corrections:

| λ | dim_q V_λ | exact polynomial in h² |
|---|-----------|------------------------|
| (4) | 1 | 1 |
| (3,1) | [3]_q | 3 + h² |
| (2,2) | [4]_q/[2]_q | 2 + h² |
| (2,1,1) | [3]_q | 3 + h² |
| (1,1,1,1) | 1 | 1 |

Sum: 10 + 3h². Divided by 4: **`λ_A(q) = 5/2 + (3/4)·h²` exactly**.

The series **terminates at h²**. The 3% gap to CODATA at q_0 is **NOT** due to truncated higher-order terms — Family A is a complete polynomial identity. The gap is **structural**: this particular Wedderburn-sum form gives `5/2 + (3/4)·h²`, which differs from the empirical target by an O(1) amount in the h² coefficient.

## Variant investigation — V7 wins

Investigated 14 natural Wedderburn-sum variants. Key results:

| Variant | h² coeff | at q_0 | rel to target |
|---------|----------|--------|---------------|
| V1: `(1/4)·Σ dim_q V_λ` (Family A) | **+3/4** | 2.5328 | +2.89% |
| **V7: `Σ_λ dim_q V_λ / [4]_q`** | **−13/16** | **2.4652** | **+0.144%** |
| V9: `Σ / [3]_q` | −1/9 | 3.33 | +35% |
| V10: `Σ / [2]_q²` | +1/8 | 2.5054 | +1.78% |
| V12: `Σ dim_q² / Σ dim_q` | +22/25 | 2.4385 | −0.94% (leading 12/5, not 5/2) |

**V7 is the structural winner:**
- Leading: 5/2 ✓ (matches the H_4 partition half-symmetric count)
- h² coefficient: **−13/16 = −0.8125** (NEGATIVE, structurally aligned with empirical)
- Gap to CODATA: 0.144% — **20× better than Family A**

Closed form: **`V7 = (10 + 3h²) / [4]_q`**.

## V7 vs. the empirical forms

The h² coefficient that fits CODATA exactly (computing it from `λ_target − 5/2 = h²·c_2`) is:

```
c_2_empirical ≈ (2.4616 − 2.5) / h² ≈ −0.879
```

| Form | c_2 value | Δ from empirical −0.879 |
|------|-----------|-------------------------|
| Family A | +0.75 | +186% (wrong sign) |
| **V7** | **−13/16 = −0.8125** | **+7.5%** |
| **PR #701 `−G`** | **−0.9160** | **−4.2%** |

V7 and `−G` bracket the empirical value — neither matches exactly. Both are close (within 5-8%).

## Structural meaning of V7

V7 = `Σ_λ dim_q V_λ / [4]_q` is the **average q-dimension per Hecke-algebra dimension unit**:
- Numerator: total q-dimension summed across all 5 Wedderburn blocks of H_4
- Denominator: [4]_q (the q-deformation of "4", related to the H_4 regular-representation parameter)

This has a clean categorical interpretation: it's the **q-deformed mean Wedderburn block dimension**, normalized by the underlying H_4 regular structure. The empirical match at 0.144% is significantly better than Family A's 3% — suggesting V7 is a closer fit to whatever the substrate-derived nucleon-mass quantity is.

## What's still open

1. **V7's h² coefficient is −13/16, not −G.** The empirical target is between them (~−0.879). Neither V7 nor `−G` is exact.

2. **No tested Wedderburn-sum variant gives both 5/2 leading AND h²≈−0.879 exactly.** Among 14 variants tested, V7 is closest at h² level but still 7.5% off the empirical h² coefficient.

3. **PR #701's `−G` (Catalan) match is at 4% from empirical** — also not exact. Both candidates bracket the true value but don't pin it.

## Updated structural picture

| Form | Status | Δ vs CODATA |
|------|--------|-------------|
| Family A (V1) `5/2 + (3/4)·h²` | PROVED (sympy + Lean), EXACT, NOT a truncation | +2.89% |
| **V7 `(10+3h²)/[4]_q = 5/2 − (13/16)·h² + ...`** | **NEW: closed-form variant with negative h²** | **+0.144%** |
| PR #701 empirical `5/2 − h²·G` | Empirical only, no derivation | −0.068% |
| PR #690 `A((4-q)/(4q+3))` | Empirical only, different h-series | +0.069% |

**The 3% Family A gap is structural, not a truncation error. The right Wedderburn-sum form has yet to be pinned down — V7 is the closest candidate but still 7% off the empirical h² coefficient.**

## Recommendation

Investigate richer Wedderburn-sum forms involving:
- Higher q-integer powers in denominator (e.g., [4]_q · [2]_q, [4]_q²)
- Operator-valued / character-weighted sums (PR #689 framework)
- Inclusion of partition-content factors (q^content_sum)

The structural target is: a single closed-form Wedderburn quantity matching `5/2 + c · h² + O(h^4)` with `c ≈ −0.879` (the empirical h² coefficient from CODATA m_p).
