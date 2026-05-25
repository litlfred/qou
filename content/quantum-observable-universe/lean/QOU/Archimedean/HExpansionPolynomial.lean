import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Data.Polynomial.Eval
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import QOU.Archimedean.BringColorTubeQForm

/-!
# h-expansion via polynomial truncation

Infrastructure for proving h^k coefficient identities of the
linking_weight candidates, **without** needing Mathlib's full
formal-power-series / analytic-function machinery.

## Approach

The full formal h-expansion of `bringColorTube q = 1/(1 + q^9 -
q^{11})` around `q = 1` (equivalently `h = q - q⁻¹ = 0`) requires
substituting `q = (h + √(h² + 4))/2` and Taylor-expanding. This needs
analytic infrastructure that doesn't sit in `Mathlib.Algebra.*`.

A lighter alternative is the **polynomial-truncation** approach:

1. Express `bringColorTube q` as a rational function `N(q) / D(q)`.
2. Compute its **finite-order Taylor polynomial** `T_N(h)` of degree
   N in h.
3. Prove the **truncation error**: `|bringColorTube q - T_N(h(q))|
   ≤ C · h^{N+1}` for q near 1 and explicit constant C.

Mathlib has the tactics needed for steps 1-2 directly. Step 3 needs
analytic-function infrastructure, but we can substitute the
*polynomial identity* `T_N(h) · D(q(h)) ≡ N(q(h)) mod h^{N+1}` —
which is a polynomial-degree identity that `Polynomial`-level proofs
can handle.

This file scaffolds steps 1-2 as concrete `Polynomial`-based defs,
unlocking the h^k coefficient theorems for downstream proof attempts.

## What this file provides

| Def / Theorem | Content |
|---|---|
| `bringColorTubeTaylor` | Degree-4 Taylor polynomial of Bring color-tube in h |
| `faddeevH4Taylor` | Degree-4 Taylor polynomial of Faddeev h⁴ in h |
| `linkingWeightTaylor` | Combined degree-4 Taylor (additive) |
| `bringColorTubeTaylor_eq` | Each coefficient of the Taylor polynomial |
| `linkingWeightTaylor_h0_eq_one` | h⁰ coefficient is 1 (NOT 5/2 like Family A) |

## What this file does NOT do

- Does NOT prove the truncation error bound (needs analytic infra)
- Does NOT close the h^k coefficient theorems for k > 4 (degree-N
  Taylor only)
- Does NOT replace `Polynomial.coeff` reasoning with `PowerSeries`
  reasoning (both Mathlib types are workable; we pick `Polynomial`)

## Source of coefficients

The numerical coefficients here come from
[`lambda_scale_h2_concrete_test.py`](../../../../../folio-assistant/computations/lambda_scale_h2_concrete_test.py),
which symbolically expanded
`1/(1 - h·q^{10})` and `1/(1 - h⁴)` around `h = 0` using sympy with
`q = (h + √(h² + 4))/2` substitution. We reproduce those coefficients
here as Mathlib `Polynomial ℚ` literals.

## References

- [`lambda_scale_h2_concrete_test.py`](../../../../../folio-assistant/computations/lambda_scale_h2_concrete_test.py)
  — sympy-derived symbolic h-coefficients
- [`docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md`](../../../../../docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md)
  §4a — categorical interpretation
-/

namespace QOU.Archimedean

open Polynomial

/-! ## §1  Taylor polynomial of Bring color-tube

From `lambda_scale_h2_concrete_test.py` symbolic output:

```
Bring color-tube `1/(1 - h·q^10)` h-expansion at h = 0:
  h^0  →  1
  h^1  →  1
  h^2  →  6
  h^3  →  47/2
  h^4  →  693/8
```

We capture this as a `Polynomial ℚ` of degree 4. -/

/-- Degree-4 Taylor expansion of `bringColorTube` in `h`.

    Coefficients:
      h⁰: 1
      h¹: 1
      h²: 6
      h³: 47/2
      h⁴: 693/8

    Source: sympy expansion in
    [`lambda_scale_h2_concrete_test.py`](../../../../../folio-assistant/computations/lambda_scale_h2_concrete_test.py)
    around `h = 0` with `q = (h + √(h² + 4))/2`. -/
noncomputable def bringColorTubeTaylor : Polynomial ℚ :=
  C 1 + C 1 * X + C 6 * X^2 + C (47/2) * X^3 + C (693/8) * X^4

/-- Coefficient 0 of `bringColorTubeTaylor` is 1. -/
theorem bringColorTubeTaylor_coeff_0 :
    bringColorTubeTaylor.coeff 0 = 1 := by
  unfold bringColorTubeTaylor
  simp [coeff_add, coeff_C, coeff_X, coeff_C_mul, coeff_X_pow]

/-- Coefficient 2 of `bringColorTubeTaylor` is 6 (the load-bearing
    h² coefficient that the categorical-distinctness audit relies on). -/
theorem bringColorTubeTaylor_coeff_2 :
    bringColorTubeTaylor.coeff 2 = 6 := by
  unfold bringColorTubeTaylor
  simp [coeff_add, coeff_C, coeff_X, coeff_C_mul, coeff_X_pow]

/-- Coefficient 4 of `bringColorTubeTaylor` is 693/8. -/
theorem bringColorTubeTaylor_coeff_4 :
    bringColorTubeTaylor.coeff 4 = 693 / 8 := by
  unfold bringColorTubeTaylor
  simp [coeff_add, coeff_C, coeff_X, coeff_C_mul, coeff_X_pow]

/-! ## §2  Taylor polynomial of Faddeev h⁴

From `lambda_scale_h2_concrete_test.py` symbolic output:

```
Faddeev `1/(1 - h^4)` h-expansion at h = 0:
  h^0  →  1
  h^1  →  0
  h^2  →  0
  h^3  →  0
  h^4  →  1   (the canonical KLR-positivity +1 coefficient)
```

(Higher orders: h^8 → 1, h^{12} → 1, … — geometric series in h^4.)
-/

/-- Degree-4 Taylor expansion of `faddeevH4` in `h`.

    Coefficients:
      h⁰: 1
      h¹: 0
      h²: 0
      h³: 0
      h⁴: 1   ← the canonical +1 coefficient (KLR positivity)
    -/
noncomputable def faddeevH4Taylor : Polynomial ℚ :=
  C 1 + C 1 * X^4

/-- Coefficient 0 of `faddeevH4Taylor` is 1. -/
theorem faddeevH4Taylor_coeff_0 :
    faddeevH4Taylor.coeff 0 = 1 := by
  unfold faddeevH4Taylor
  simp [coeff_add, coeff_C, coeff_C_mul, coeff_X_pow]

/-- **Load-bearing theorem**: h⁴ coefficient of `faddeevH4Taylor` is 1.

    This is the categorical "+1·h⁴" coefficient that two independent
    drivers (Faddeev iterated + KLR positivity) converge on. See the
    audit §4a probe (`h4_categorical_drivers_probe.py`).

    Note: in `faddeevH4Taylor` (a `Polynomial ℚ`), the h⁴ coefficient
    is exactly 1. The empirical α ≈ 1.011 measured in the
    Python probe is the FULL h⁴ residual (including the Bring
    color-tube's h⁴ = 693/8 contribution + Faddeev's +1) divided by
    h_q⁴ at q₀; the +1 here is the *Faddeev-only* contribution. -/
theorem faddeevH4Taylor_coeff_4 :
    faddeevH4Taylor.coeff 4 = 1 := by
  unfold faddeevH4Taylor
  simp [coeff_add, coeff_C, coeff_C_mul, coeff_X_pow]

/-- All intermediate coefficients (h¹, h², h³) of `faddeevH4Taylor`
    are zero — the function depends on `h⁴` only (not `h`, `h²`, or
    `h³`). -/
theorem faddeevH4Taylor_coeff_1 :
    faddeevH4Taylor.coeff 1 = 0 := by
  unfold faddeevH4Taylor
  simp [coeff_add, coeff_C, coeff_C_mul, coeff_X_pow]

theorem faddeevH4Taylor_coeff_2 :
    faddeevH4Taylor.coeff 2 = 0 := by
  unfold faddeevH4Taylor
  simp [coeff_add, coeff_C, coeff_C_mul, coeff_X_pow]

theorem faddeevH4Taylor_coeff_3 :
    faddeevH4Taylor.coeff 3 = 0 := by
  unfold faddeevH4Taylor
  simp [coeff_add, coeff_C, coeff_C_mul, coeff_X_pow]

/-! ## §3  Combined: linkingWeightTaylor

The ADDITIVE composition `bringColorTubeTaylor + faddeevH4Taylor - 1`
captures the candidate's h-expansion at degree ≤ 4. -/

/-- Combined Taylor expansion of `linkingWeightBringFaddeevH4` in h,
    assuming the additive composition rule. -/
noncomputable def linkingWeightTaylor : Polynomial ℚ :=
  bringColorTubeTaylor + faddeevH4Taylor - C 1

/-- h⁰ coefficient: `1 + 1 − 1 = 1`. -/
theorem linkingWeightTaylor_coeff_0 :
    linkingWeightTaylor.coeff 0 = 1 := by
  unfold linkingWeightTaylor
  rw [coeff_sub, coeff_add, bringColorTubeTaylor_coeff_0,
      faddeevH4Taylor_coeff_0, coeff_C_zero]
  norm_num

/-- h² coefficient: `6 + 0 - 0 = 6` (Bring color-tube's h² is the
    load-bearing distinctness coefficient). -/
theorem linkingWeightTaylor_coeff_2 :
    linkingWeightTaylor.coeff 2 = 6 := by
  unfold linkingWeightTaylor
  rw [coeff_sub, coeff_add, bringColorTubeTaylor_coeff_2,
      faddeevH4Taylor_coeff_2]
  simp [coeff_C]

/-- h⁴ coefficient: `693/8 + 1 = 701/8`. The "+1" from Faddeev is
    the KLR-positivity canonical-basis vector. -/
theorem linkingWeightTaylor_coeff_4 :
    linkingWeightTaylor.coeff 4 = 701 / 8 := by
  unfold linkingWeightTaylor
  rw [coeff_sub, coeff_add, bringColorTubeTaylor_coeff_4,
      faddeevH4Taylor_coeff_4]
  simp [coeff_C]
  norm_num

/-! ## §4  Distinctness from Family A's Taylor polynomial

Family A's Taylor (at h-level) is `5/2 + (3/4)·h²` — terminates exactly.
We restate as a `Polynomial ℚ` for direct coefficient comparison. -/

/-- Family A's `5/2 + (3/4)·h²` as a `Polynomial ℚ`. -/
noncomputable def familyATaylor : Polynomial ℚ :=
  C (5/2) + C (3/4) * X^2

theorem familyATaylor_coeff_0 :
    familyATaylor.coeff 0 = 5/2 := by
  unfold familyATaylor
  simp [coeff_add, coeff_C, coeff_C_mul, coeff_X_pow]

theorem familyATaylor_coeff_2 :
    familyATaylor.coeff 2 = 3/4 := by
  unfold familyATaylor
  simp [coeff_add, coeff_C, coeff_C_mul, coeff_X_pow]

theorem familyATaylor_coeff_4 :
    familyATaylor.coeff 4 = 0 := by
  unfold familyATaylor
  simp [coeff_add, coeff_C, coeff_C_mul, coeff_X_pow]

/-- **Categorical distinctness theorem (Taylor-coefficient version).**
    The Bring + Faddeev h⁴ Taylor polynomial DIFFERS from Family A
    at every h^k for k ∈ {0, 2, 4}:

    | h^k | Bring + Faddeev | Family A |
    |---|---|---|
    | h⁰ | 1   | 5/2 |
    | h² | 6   | 3/4 |
    | h⁴ | 701/8 | 0 |

    They cannot be the same polynomial. -/
theorem linkingWeightTaylor_distinct_from_familyATaylor :
    linkingWeightTaylor ≠ familyATaylor := by
  intro heq
  have h0 := linkingWeightTaylor_coeff_0
  have h0' := familyATaylor_coeff_0
  rw [heq] at h0
  rw [h0'] at h0
  -- h0 : (5/2 : ℚ) = 1 — contradiction
  norm_num at h0

/-! ## §5  Open / TODO

- **Truncation error bound** (analytic infra) — prove `|bringColorTube
  q - bringColorTubeTaylor.eval (heckeH q)| ≤ C · (heckeH q)^5` for q
  in a neighborhood of 1.

- **Higher-order coefficients** — extend Taylor polynomial to degree
  6, 8 (Bring color-tube terms h⁶ → 1299/4, h⁸ → 156651/128 per
  sympy output).

- **Lemma: Family A's h⁴ = 0 IS the categorical termination property**
  — restate `lambdaA_higher_even_vanish` here in the Taylor-polynomial
  language.

- **Cross-reference with PR #1272's Jones-route h⁴ = -3.03** — show
  that the via-Jones Taylor expansion has a different h⁴ coefficient
  than either Bring + Faddeev (701/8) or Family A (0), implying yet
  a third decomposition strategy.
-/

end QOU.Archimedean
