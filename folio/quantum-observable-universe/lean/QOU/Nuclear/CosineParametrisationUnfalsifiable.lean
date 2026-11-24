/-
# The cosine in the Q_β ladder is unfalsifiable at CODATA precision

Bean `qou-cds1`. Companion to
`computations/qbeta/qbeta_cosine_parametrisation_justification_probe.py`.

## What is at stake

The `c_k` ladder exists because the N=1 rung is written
`Q_N1 = Q_A · cos(α − u/2)` with `α = (z−1)h/2`. The corpus already records that
`α` is *defined* as the counit-minus-trace discrepancy — "α is neither free nor
fitted: it IS the discrepancy" — and that the coordinate was "manufactured by
writing a smooth correction as a cosine". `QOU.QBeta.BraidImageEigenphaseExclusion`
then closes two of the three ways a cosine could be earned: the class meant to
carry a spectral reading (`EigenphaseCarrier`) is vacuous, the braid-image branch
is excluded in every convention, and "any transfer matrix with spectrum `e^{±iα}`"
is circular. Only a holonomy of an independently-defined connection
(KZ / Kohno–Drinfeld) remains, and nothing in the corpus supplies one.

This file adds the **quantitative** half, which that exclusion does not reach:
even granting the phase, *calling the correction a cosine rather than a
quadratic in the phase adds no content the data can see.*

## The measurement it formalises

At the proton pin, convention C (probe figures, 50 dps):

| quantity | value | in σ of `Q_β/Q_A` |
|---|---|---|
| 1σ on the measured `Q_β/Q_A` | `7.784e-7` | 1 |
| `\|cos θ − (1 − θ²/2)\|` — the cosine's OWN signature | `4.274e-7` | **0.549** |
| residual the `c_k` tower must absorb | `7.382e-5` | **94.8** |

So the cosine's entire content beyond a quadratic is **half a standard
deviation**, while the residual it fails to explain is **95 standard
deviations**. Any function agreeing with `cos` to second order fits the data
identically well, and the `c_k` tower would be unchanged.

`cos_departure_le` and `ck_residual_dominates_cos_departure` below are that
statement, with the physical phase bounded by `|θ| ≤ 3/50` (the measured
`|θ| = 0.0566` under C, `0.0447` under D) and the residual by `r ≥ 7/10⁵`.

## And the parametrisation loses information the exact form keeps

`cos_parametrisation_not_injective`: because `cos` is even, two distinct Markov
parameters `z` give the *same* correction. The exact correction
`tr_M^z(Δ_S)/ε(Δ_S)` is affine in `z` (`QOU.QBeta.traceDelta_cross_mul`) and
therefore injective. So the cosine is 2-to-1 where the object it parametrises is
1-to-1 — the branch structure the corpus met as "a square-root branch point
0.062 % above q₀" seen from the algebraic side.

## Scope

Scope-(a). This does **not** show the cosine is wrong, does not propose a
replacement, and does not derive `α`. It shows the cosine is not *tested* by the
`Q_β` anchor: its distinguishing content sits below the experimental resolution
while the residual sits far above it. Branch 3 of the eigenphase trichotomy
remains the only place a derivation of `α` could live, and a derivation there
would justify the cosine independently of anything measured here.
-/
import Mathlib.Analysis.Complex.Trigonometric

namespace QOU.QBeta

open Real

/-- **The cosine's own signature is tiny on the physical phase.** For
`|θ| ≤ 3/50` — which covers the measured `|θ| = 0.0566` (convention C) and
`0.0447` (convention D) — the departure of `cos θ` from its quadratic truncation
is at most `7e-7`, i.e. below the `7.784e-7` one-sigma resolution of the measured
`Q_β/Q_A`. Everything that makes a cosine a cosine is invisible here. -/
theorem cos_departure_le {θ : ℝ} (hθ : |θ| ≤ 3 / 50) :
    |Real.cos θ - (1 - θ ^ 2 / 2)| ≤ 7 / 10 ^ 7 := by
  have h1 : |θ| ≤ 1 := hθ.trans (by norm_num)
  have hb := Real.cos_bound h1
  have h0 : (0 : ℝ) ≤ |θ| := abs_nonneg θ
  refine hb.trans ?_
  calc |θ| ^ 4 * (5 / 96) ≤ (3 / 50 : ℝ) ^ 4 * (5 / 96) := by gcongr
    _ ≤ 7 / 10 ^ 7 := by norm_num

/-- **The `c_k` residual dominates it by two orders of magnitude.** With the
physical phase and the measured residual `r ≥ 7e-5` that the ladder must absorb,
the cosine's entire signature is at most `r/100`.

This is the file's point: the `c_k` tower is not correcting a cosine, it is
correcting a quadratic — and it would be the same tower for any function with
the same second-order behaviour. -/
theorem ck_residual_dominates_cos_departure {θ r : ℝ}
    (hθ : |θ| ≤ 3 / 50) (hr : 7 / 10 ^ 5 ≤ r) :
    100 * |Real.cos θ - (1 - θ ^ 2 / 2)| ≤ r := by
  have h := cos_departure_le hθ
  linarith

/-- **The cosine parametrisation is 2-to-1.** Because `cos` is even, the two
Markov parameters `z₁ ≠ z₂` symmetric about `1 + u/h` give the *same* N=1
correction. The exact correction is affine in `z` (`traceDelta_cross_mul`) hence
injective, so passing to the cosine discards a distinction the underlying object
makes — the algebraic form of the branch ambiguity the corpus met as a
"square-root branch point 0.062 % above q₀". -/
theorem cos_parametrisation_not_injective {h u θ₀ : ℝ} (hh : h ≠ 0) (hθ : θ₀ ≠ 0) :
    (1 + 2 * (u / 2 + θ₀) / h) ≠ (1 + 2 * (u / 2 - θ₀) / h) ∧
      Real.cos ((1 + 2 * (u / 2 + θ₀) / h - 1) * h / 2 - u / 2)
        = Real.cos ((1 + 2 * (u / 2 - θ₀) / h - 1) * h / 2 - u / 2) := by
  constructor
  · intro hEq
    have : 2 * (u / 2 + θ₀) / h = 2 * (u / 2 - θ₀) / h := by linarith [hEq]
    have h4 : 2 * (u / 2 + θ₀) = 2 * (u / 2 - θ₀) := by
      field_simp at this; linarith
    exact hθ (by linarith)
  · have e₁ : (1 + 2 * (u / 2 + θ₀) / h - 1) * h / 2 - u / 2 = θ₀ := by
      field_simp; ring
    have e₂ : (1 + 2 * (u / 2 - θ₀) / h - 1) * h / 2 - u / 2 = -θ₀ := by
      field_simp; ring
    rw [e₁, e₂, Real.cos_neg]

end QOU.QBeta
