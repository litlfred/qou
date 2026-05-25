import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Data.Polynomial.Eval
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import QOU.Archimedean.HExpansionPolynomial

/-!
# h-expansion at degree 8 — Bring color-tube + via-Jones cross-comparison

Extends [`HExpansionPolynomial.lean`](HExpansionPolynomial.lean) to degree 8,
incorporating the **CORRECTED** via-Jones h-expansion from sibling PR #1272
(`claude/brave-mendel-FPxFl`, commit
[`9c7baaea`](https://github.com/litlfred/qou/blob/9c7baaea41c55cf5e4c7e93b0933bf8a7f0fa0d0/folio-assistant/computations/gamma_gamma_pair_production_decomposition.py)).

## via-Jones expansion (CORRECTED per PR #1272's edit)

PR #1272 fixed a bug in the first version of their probe: the
Markov-trace normalization was wrong (they used `(q^{1/2} + q^{-1/2})²`
which equals `q + 2 + q⁻¹`, not the standard Kauffman-Jones
`[2]_q² = (q + q⁻¹)² = q² + 2 + q⁻²`). The CORRECTED normalization
matches the Lean-proved closed form in
[`BorromeanMarkovTrace.lean § h2_coefficient_cancellation`](../../BraidsAndKnots/BorromeanMarkovTrace.lean).

Under the CORRECTED normalization, the Markov trace of β_Bor =
`(σ₀σ₁⁻¹)³` is

  tr_M(β_Bor, q) = (4 + h² − 3h⁴ − h⁶) / (h² + 4)

with h-expansion (Lean-proved):

  tr_M(β_Bor, q) = 1 + 0·h² − (3/4)·h⁴ − (1/16)·h⁶ + (1/64)·h⁸ + …

PR #1272's bridge formula `linking_weight_via_jones(q) := 5/2 + 4·(tr_M − 1)`
then gives:

  via_jones(q) = 5/2 + 4·[−(3/4)h⁴ − (1/16)h⁶ + (1/64)h⁸ + …]
              = 5/2 + 0·h² − 3·h⁴ − (1/4)·h⁶ + (1/16)·h⁸ + …

## Headline structural finding (from PR #1272's CORRECTED probe)

| coefficient | Family A | via-Jones | Bring color-tube |
|---|---|---|---|
| h⁰ | **5/2** | **5/2** | **1** |
| h² | **3/4** | **0** | **6** |
| h⁴ | 0 | −3 | 693/8 |
| h⁶ | 0 | −1/4 | 156651/128 |
| h⁸ | 0 | 1/16 | 17743341/1024 |

**Three structural findings:**

1. **Family A and via-Jones DISAGREE at h²**: Family A's +3/4 vs
   via-Jones's 0. Per PR #1272's CORRECTED finding, the H_4
   Wedderburn dim sum (Family A) and the H_3 Markov trace
   (via-Jones) are different categorical objects — not the same
   linking_weight under different parameterizations.

2. **Bring color-tube is in a DIFFERENT normalization class**:
   h⁰ = 1, not 5/2 like Family A and via-Jones. This means
   `bringColorTube` is NOT a linking_weight in the same sense —
   it is a different scalar function that happens to give a
   numerically-close value at q₀ via the q^{10} factor amplifying
   the small h_q term.

3. **The numerical match at q₀ is substrate-specific** (per the
   audit §6 open question). At q₀ ≈ 1.110, `q₀^{10} ≈ 2.84`, so
   `1/(1 − h_q·q₀^{10}) ≈ 1/(1 − 0.594) ≈ 2.46`, coinciding with
   Family A's `5/2 + (3/4)h² ≈ 2.533` and via-Jones's `5/2 − 3·h⁴
   ≈ 2.494` within ~3 %. These three forms agree numerically at
   the substrate but are categorically distinct.

## References

- PR [#1272](https://github.com/litlfred/qou/pull/1272) — via_jones
  decomposition + CORRECTED normalization
- [`BorromeanMarkovTrace.lean`](../../BraidsAndKnots/BorromeanMarkovTrace.lean) — Lean-proved tr_M closed form
- [`HExpansionPolynomial.lean`](HExpansionPolynomial.lean) — degree-4 expansion for Bring, Faddeev, Family A
- [`docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md`](../../../../../docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md) §4a
-/

namespace QOU.Archimedean

open Polynomial

/-! ## §1  Extended Bring color-tube Taylor (degree 8)

Coefficients from
[`lambda_scale_h2_concrete_test.py`](../../../../../folio-assistant/computations/lambda_scale_h2_concrete_test.py)
extended via sympy to degree 9:

```
h^0: 1
h^1: 1
h^2: 6
h^3: 47/2
h^4: 693/8
h^5: 1299/4
h^6: 156651/128
h^7: 294787/64
h^8: 17743341/1024
h^9: 33377825/512
```
-/

/-- Degree-8 Taylor expansion of `bringColorTube` in `h`. Source:
    sympy-derived from `1/(1 - h·q^{10})` with q = (h + √(h²+4))/2. -/
noncomputable def bringColorTubeTaylor8 : Polynomial ℚ :=
  C 1 + C 1 * X + C 6 * X^2 + C (47/2) * X^3
    + C (693/8) * X^4 + C (1299/4) * X^5
    + C (156651/128) * X^6 + C (294787/64) * X^7
    + C (17743341/1024) * X^8

/-- h⁶ coefficient: 156651/128. -/
theorem bringColorTubeTaylor8_coeff_6 :
    bringColorTubeTaylor8.coeff 6 = 156651 / 128 := by
  unfold bringColorTubeTaylor8
  simp [coeff_add, coeff_C, coeff_X, coeff_C_mul, coeff_X_pow]

/-- h⁸ coefficient: 17743341/1024. -/
theorem bringColorTubeTaylor8_coeff_8 :
    bringColorTubeTaylor8.coeff 8 = 17743341 / 1024 := by
  unfold bringColorTubeTaylor8
  simp [coeff_add, coeff_C, coeff_X, coeff_C_mul, coeff_X_pow]

/-! ## §2  via-Jones Taylor polynomial (CORRECTED per PR #1272)

PR #1272's bridge:
  `linking_weight_via_jones(q) := 5/2 + 4·(tr_M(β_Bor) − 1)`

With Lean-proved tr_M = `(4 + h² − 3h⁴ − h⁶) / (h² + 4)` from
`BorromeanMarkovTrace.lean`, h-expansion:
  tr_M = 1 + 0·h² − (3/4)h⁴ − (1/16)h⁶ + (1/64)h⁸ + …

Therefore:
  via_jones = 5/2 + 4·[−(3/4)h⁴ − (1/16)h⁶ + (1/64)h⁸ + …]
            = 5/2 − 3·h⁴ − (1/4)h⁶ + (1/16)h⁸ + …
-/

/-- Degree-8 Taylor expansion of the via-Jones bridge (PR #1272's
    CORRECTED form). -/
noncomputable def viaJonesTaylor : Polynomial ℚ :=
  C (5/2) + C (-3) * X^4 + C (-1/4) * X^6 + C (1/16) * X^8

theorem viaJonesTaylor_coeff_0 :
    viaJonesTaylor.coeff 0 = 5/2 := by
  unfold viaJonesTaylor
  simp [coeff_add, coeff_C, coeff_C_mul, coeff_X_pow]

/-- **Load-bearing finding** (PR #1272 CORRECTED): via_jones h² = 0,
    NOT 3/4 like Family A. -/
theorem viaJonesTaylor_coeff_2 :
    viaJonesTaylor.coeff 2 = 0 := by
  unfold viaJonesTaylor
  simp [coeff_add, coeff_C, coeff_C_mul, coeff_X_pow]

theorem viaJonesTaylor_coeff_4 :
    viaJonesTaylor.coeff 4 = -3 := by
  unfold viaJonesTaylor
  simp [coeff_add, coeff_C, coeff_C_mul, coeff_X_pow]

theorem viaJonesTaylor_coeff_6 :
    viaJonesTaylor.coeff 6 = -1/4 := by
  unfold viaJonesTaylor
  simp [coeff_add, coeff_C, coeff_C_mul, coeff_X_pow]

theorem viaJonesTaylor_coeff_8 :
    viaJonesTaylor.coeff 8 = 1/16 := by
  unfold viaJonesTaylor
  simp [coeff_add, coeff_C, coeff_C_mul, coeff_X_pow]

/-! ## §3  Three-way categorical-distinctness theorems

The three candidate forms differ at multiple h^k orders. Formalize
the disagreement pattern. -/

/-- **Three-way h² distinctness**: Family A (+3/4), via-Jones (0),
    and Bring color-tube (+6) all have DIFFERENT h² coefficients. -/
theorem h2_three_way_distinct :
    familyATaylor.coeff 2 ≠ viaJonesTaylor.coeff 2 ∧
    familyATaylor.coeff 2 ≠ bringColorTubeTaylor.coeff 2 ∧
    viaJonesTaylor.coeff 2 ≠ bringColorTubeTaylor.coeff 2 := by
  refine ⟨?_, ?_, ?_⟩
  · rw [familyATaylor_coeff_2, viaJonesTaylor_coeff_2]; norm_num
  · rw [familyATaylor_coeff_2, bringColorTubeTaylor_coeff_2]; norm_num
  · rw [viaJonesTaylor_coeff_2, bringColorTubeTaylor_coeff_2]; norm_num

/-- **Three-way h⁰ distinctness**: Family A (5/2), via-Jones (5/2),
    and Bring color-tube (1).

    Family A and via-Jones AGREE at h⁰ (both = 5/2 = the standard
    linking_weight scale). Bring color-tube DISAGREES (h⁰ = 1),
    formalizing the audit §1 finding "Bring is in a different
    normalization class than linking_weight". -/
theorem h0_bring_distinct_from_linking_weight_class :
    bringColorTubeTaylor.coeff 0 ≠ familyATaylor.coeff 0 ∧
    bringColorTubeTaylor.coeff 0 ≠ viaJonesTaylor.coeff 0 ∧
    familyATaylor.coeff 0 = viaJonesTaylor.coeff 0 := by
  refine ⟨?_, ?_, ?_⟩
  · rw [bringColorTubeTaylor_coeff_0, familyATaylor_coeff_0]; norm_num
  · rw [bringColorTubeTaylor_coeff_0, viaJonesTaylor_coeff_0]; norm_num
  · rw [familyATaylor_coeff_0, viaJonesTaylor_coeff_0]

/-- **h⁴ distinctness**: Family A (0), via-Jones (-3),
    Bring color-tube (693/8), Faddeev h⁴ (+1) — all different. -/
theorem h4_three_way_distinct :
    familyATaylor.coeff 4 ≠ viaJonesTaylor.coeff 4 ∧
    familyATaylor.coeff 4 ≠ bringColorTubeTaylor.coeff 4 ∧
    viaJonesTaylor.coeff 4 ≠ bringColorTubeTaylor.coeff 4 := by
  refine ⟨?_, ?_, ?_⟩
  · rw [familyATaylor_coeff_4, viaJonesTaylor_coeff_4]; norm_num
  · rw [familyATaylor_coeff_4, bringColorTubeTaylor_coeff_4]; norm_num
  · rw [viaJonesTaylor_coeff_4, bringColorTubeTaylor_coeff_4]; norm_num

/-! ## §4  Pairwise polynomial-level distinctness

Combine coefficient-level disagreement into polynomial-equality
refutations. -/

/-- **Via-Jones ≠ Family A** as polynomials. They differ at the h²
    coefficient (0 vs 3/4) and at every h⁴ and higher even coefficient. -/
theorem viaJonesTaylor_ne_familyATaylor :
    viaJonesTaylor ≠ familyATaylor := by
  intro heq
  have h2_diff : viaJonesTaylor.coeff 2 ≠ familyATaylor.coeff 2 := by
    rw [viaJonesTaylor_coeff_2, familyATaylor_coeff_2]; norm_num
  rw [heq] at h2_diff
  exact h2_diff rfl

/-- **Bring color-tube ≠ via-Jones** as polynomials. They differ at h⁰
    (1 vs 5/2) — Bring is not in the linking_weight normalization
    class. -/
theorem bringColorTubeTaylor_ne_viaJonesTaylor :
    bringColorTubeTaylor ≠ viaJonesTaylor := by
  intro heq
  have h0_diff : bringColorTubeTaylor.coeff 0 ≠ viaJonesTaylor.coeff 0 := by
    rw [bringColorTubeTaylor_coeff_0, viaJonesTaylor_coeff_0]; norm_num
  rw [heq] at h0_diff
  exact h0_diff rfl

/-! ## §5  Honest-accounting note

The three-way distinctness theorems formalise an honest structural
finding from the cross-PR collaboration:

- **Family A** (`(1/4)·Σ_{λ⊢4} dim_q V_λ`) — proved Wedderburn dim
  sum at H_4. Terminates at h².
- **via-Jones** (`5/2 + 4·(tr_M(β_Bor) − 1)`) — bridge from H_3
  Markov trace. Has non-trivial h⁴, h⁶, h⁸ corrections.
- **Bring color-tube** (`1/(1 − h_q·q^{10})`) — Φ_q functional
  equation ratio. Has h⁰ = 1, h¹ = 1 (not in linking_weight class).

These are **three different mathematical objects**. The numerical
match at q₀ (all give 2.46-2.53) is substrate-specific. The
categorically-correct `linking_weight` is the OPEN question — neither
Family A nor via-Jones nor Bring + Faddeev h⁴ has been proved to be
the canonical choice.

This is consistent with:

1. CLAUDE.md §"Critical framing — do NOT treat λ_scale as a separate
   object" — λ_scale was absorbed into per-knot Geom_full, and the
   remaining R&D direction is `Geom_full(𝓑₃)` refinement, not
   λ_scale calibration.

2. The audit §4b open work — "Specific partition-channel assignment
   of Bring color-tube vs Faddeev h⁴ at H_4" is the load-bearing
   step. Without it, the three forms remain candidate decompositions
   without a categorical decider.

3. PR #1272's CORRECTED §gap_localisation interpretation: "Open
   question: which is the categorically-correct `linking_weight`?
   The simple bridge `linking_weight = 5/2 + 4·(tr_M − 1)` is itself
   a hack (forces tr_M(q=1)=1 to equal Family A's 5/2 by adding a
   constant)."

The honest framing: the framework currently has THREE candidate
decompositions for `Geom_full(𝓑₃)`'s linking_weight factor, none with
a categorical proof of canonicity. The Bring + Faddeev h⁴ candidate
(this branch) gives the closest numerical match (108 ppm m_p), but
is structurally the most "different" of the three. Whichever
ultimately enters production will require the categorical proof.

-/

end QOU.Archimedean
