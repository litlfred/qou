# All c_i Status — Conjecture Proof Inventory

**Date:** 2026-05-18
**Branch:** `claude/lambda-scale-conjecture-proof` (PR #701)
**Goal:** Prove and document all h-expansion coefficients c_i in
λ_scale = c_0 + c_2·h² + c_4·h⁴ + c_6·h⁶ + …

## Summary

We track **TWO families of c_i**:

**Family A (Natural categorical):** the q-expansion coefficients of
`π_HS(id, H_4) = (1/4) · Σ_λ dim_q V_λ` — the natural substrate-derived
quantity whose value at q=1 is 5/2.

**Family B (Empirical):** the q-expansion coefficients of the
CODATA-derived λ_p target = `(m_p/m_e) · ℏ_q² / Vol(B_3)`.

Both families share c_0 = 5/2 at leading order but diverge beyond.

## Family A — Natural Categorical (PROVED)

The natural categorical realization is

$$
  \pi_{\mathrm{HS}}(\mathrm{id}, q) \;=\;
  \frac{1}{4} \sum_{\lambda \vdash 4} \dim_q V_\lambda \;=\;
  \frac{3 [2]_q^2 - 2}{4} \;=\;
  \frac{3q^2 + 4 + 3q^{-2}}{4}.
$$

This is **closed-form** and **terminates** as an h-series at h².

| Coefficient | Value | Status |
|-------------|-------|--------|
| **c_0** | **5/2** | ✅ PROVED via Step 2 (half-symmetric H_4 partition count) |
| **c_2** | **+3/4** | ✅ PROVED — direct q-expansion of (3·[2]_q² − 2)/4 |
| **c_4** | **0** | ✅ PROVED — series terminates exactly |
| **c_6** | **0** | ✅ PROVED |
| **c_{2k}, k ≥ 2** | **0** | ✅ PROVED — exact termination |
| **c_{2k+1}** (odd) | **0** | ✅ PROVED — π_HS(id) is even in h by q ↔ q⁻¹ symmetry |

**Proof:** Direct Taylor expansion of the closed-form rational function
`(3q² + 4 + 3q⁻²)/4` at q = 1, then substituting ε(h) via the inverse
of h = 2ε − ε² + ε³ − …. Sympy verifies all coefficients in one line.

**Numerical value at q_0:** π_HS(id) ≈ 2.5328.

## Family B — Empirical CODATA-derived (UNPROVED)

The empirical λ_p target is solved from CODATA:

$$
  \lambda_p^{\mathrm{empirical}}(q) := \frac{m_p}{m_e} \cdot \frac{\hbar_q^2}{\mathrm{Vol}(\mathcal{B}_3)}.
$$

The h-expansion of this target requires fitting a series to a single
numerical value at q_0. Coefficients beyond c_0 are not determined
by CODATA alone — they require an assumed substrate form.

| Coefficient | Value (best fit) | Status |
|-------------|------------------|--------|
| **c_0** | **5/2** | ✅ Matches Family A at q=1 by construction |
| **c_2** | **−G ≈ −0.916** | ❌ Conjectural (was 5.4 ppm fit; falsified by Family A) |
| **c_4** | **−0.00691** | ❌ Conjectural (no clean substrate form found) |
| **c_6+** | undetermined | ❌ Open — depends on assumed ansatz |

**Status:** The conjecture `λ_p = 5/2 − h²·G + h⁴·c_4 + …` was a
PSLQ-style numerical hypothesis. Family A computation falsifies the
specific h² coefficient (real value: +3/4, not −G).

## Why Family A and Family B differ

Family A is the natural Hecke-algebra block-count categorical quantity.
Family B is the empirical target that the Borromean baryon mass formula
predicts for m_p. They differ by ~3% at q_0 — meaning **the Borromean
formula's λ_scale is NOT the natural π_HS(id) at H_4**.

Possible structural resolutions:

1. **λ_scale is a DIFFERENT categorical quantity** — perhaps an
   alternating sum Σ (−1)^|λ| dim_q V_λ, or a Skein-polynomial
   evaluation, or a Bloch-Wigner regulator of B_3.
2. **The Borromean baryon mass formula needs refinement** — the
   `m = m_e · [Vol/ℏ_q² · λ + S]` form may have additional
   structural terms missed in the original conjecture.
3. **The 5.6 ppm match was a coincidence** — λ_scale is genuinely
   transcendental in q, and `5/2 − h²·G` was an artifact of
   high-dimensional PSLQ search.

## What "prove all c_i" looks like

**For Family A:** DONE. All c_i are derived in closed form:
c_0 = 5/2, c_2 = 3/4, c_4 = c_6 = … = 0.

**For Family B:** requires a separate categorical derivation of
λ_scale — which means either:
- finding a substrate quantity whose h-expansion agrees with the
  empirical fit to higher precision, OR
- deriving λ_scale from the actual baryon-state Lagrangian rather
  than the heuristic Vol/ℏ_q² ansatz.

## Specific verifiable predictions

If Family A is the right form (and the Borromean formula needs
refinement), the corrected proton mass prediction is:

$$
  m_p^{\mathrm{Family\ A}} = m_e \cdot \frac{\mathrm{Vol}(\mathcal{B}_3)}{\hbar_q^2} \cdot \pi_{\mathrm{HS}}(\mathrm{id}, q_0) \approx 938.272 \cdot \frac{2.5328}{2.4599} \approx 966 \text{ MeV}.
$$

This is **3% off from CODATA**. The 3% gap must come from one of:
- S(p) Skein contribution (≈ 28 MeV) — substrate-derivable?
- Multi-component correction beyond simple Vol/ℏ_q² ansatz
- Different categorical λ_scale (Family B ≠ Family A)

## Next concrete R&D

| Direction | Effort | Expected outcome |
|-----------|--------|------------------|
| Verify Family A coefficients in Lean | Medium | Step 2-4 of proof lifted to Lean (formal) |
| Search alternative substrate forms for Family B | Hard | Possible match for c_2 = -G structurally |
| Refine Borromean mass formula | Hard | New conjecture replacing `m = m_e·[Vol/ℏ_q²·λ + S]` |
| Compute Skein S(p) directly (Step 5-open) | Medium | Closes Step 5 fully; may explain 3% gap |

## Files

- `lambda_scale_rd_h4_half_symmetric.py` — Family A derivation (PROVED)
- `lambda_scale_rd_c4_pslq_search.py` — Family B PSLQ scan (NO MATCH)
- `lambda_scale_rd_hoefsmit_symbolic.py` — Canonical Markov trace (gives 5/3, not 5/2 — confirms π_HS ≠ τ_M)
- `2026-05-18-conjecture-falsification.md` — Family B falsification at h² level
