/-
# S-channel magnitude — exact cofactor factorization at the simple zero `q*`

Companion to `SLeakMagnitudeOffsetRatio.lean` (leading-order slope cancellation +
the smoothness-wall scope-(b) exclusion) and to the Route-A probe
`computations/qbeta/qbeta_magnitude_taylor_qstar_probe.py`
(`qbeta-magnitude-taylor-qstar.witness.json`), which closes the observed
`|S_leak(proton)/S_leak(muon)| ≈ 4.075` to a **1-ppQ symbolic form**.

That probe writes the bar-odd residual near its simple zero `q*` as the Taylor
factorization

    S(q) = S'(q*)·(q − q*) + ½S''(q*)·(q − q*)² + …
         = L · (q − q*) · g(q),   L := S'(q*),   g(q) := 1 + a·(q−q*) + b·(q−q*)² + …

with `g` the **normalized analytic cofactor**: `g(q*) = 1` (it collects all
higher-order Taylor structure, `a = ½S''/S'`, `b = (1/6)S'''/S'`). This file proves
the *structural* content the numeric residual table rests on. None of the anchor
values `S(q_p)`, `S(q_m)`, nor the magnitude `4.075` enters as a constant — every
statement is generic in `(S, g, L, q*, q_p, q_m)`.

The four lemmas, in dependence order:

* `cofactor_is_normalized_deviation` — `g` is *exactly* the multiplicative
  deviation of `S` from its leading linear model `L·(q − q*)`. So the cofactor is
  not an ansatz: given the factorization it is forced, `g(q) = S(q)/(L·(q−q*))`.
* `exact_ratio_factorization` — the **exact** ratio identity
  `S(q_p)/S(q_m) = (q_p−q*)/(q_m−q*) · g(q_p)/g(q_m)`. The slope `L` cancels
  (sharpening `linear_ratio_slope_independent` from the leading case to the full
  cofactor), and the factorization is *exact*, not just leading-order — this is the
  identity the probe evaluates order-by-order.
* `offset_ratio_error_is_cofactor` — the error of the **leading** offset-ratio
  approximation `(q_p−q*)/(q_m−q*)` is *exactly* `(q_p−q*)/(q_m−q*) · (g(q_p)/g(q_m) − 1)`.
  This is the closed form of the probe's **order-0 residual** (`6.18e-7`): the
  leading offset ratio matches only to the extent the cofactor ratio departs from 1.
* `linear_model_relative_error` — using the normalization `g(q*) = 1`, the
  relative error of the linear model `L·(q_p−q*)` against `S(q_p)` is exactly
  `g(q_p) − g(q*)`, i.e. the cofactor's departure from its value at the zero. This
  is why a single Taylor order in `g` buys ~6–7 digits: the error is the cofactor's
  own increment away from the normalized `1`.

Discipline: these are exact algebraic identities of the factorization, derive-then-
check (the probe DERIVES `q*` and the coefficients; these lemmas prove the identities
those derived numbers satisfy). No `u(q₀)` map, no `c_k`, no `SDeformedVolumeChannel`
instance. **Scope: L1** — `|S_p/S_m|` is an internal cross-check of the residual's
near-zero structure, not an L2 observable. A *closed form for `q*`* (Route B) stays
OPEN; here `q*` is any simple zero, obtained numerically in the probe.

Archimedean field arithmetic (division on `ℝ`), so `ℝ` per §7c.

-- Ref: [leitner2026] docs/audits/2026-08-01-bring-embedding-magnitude.md
-/
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.QBeta.SLeakMagnitudeTaylorRatio

/-- **The cofactor is the forced deviation from the linear model.** Given the
factorization `S(q) = L·(q − q*)·g(q)` of a function with a simple zero at `q*`
(slope `L ≠ 0`), the cofactor `g` at any `qp ≠ q*` equals the multiplicative
deviation `S(qp) / (L·(qp − q*))` of `S` from its leading linear model. So `g` is
not a free ansatz — it is pinned by the factorization, and the normalization
`g(q*) = 1` (used below) is the statement that this deviation is `1` at the zero. -/
theorem cofactor_is_normalized_deviation
    {S g : ℝ → ℝ} {L qstar qp : ℝ}
    (hS : ∀ q, S q = L * (q - qstar) * g q)
    (hL : L ≠ 0) (hqp : qp - qstar ≠ 0) :
    S qp / (L * (qp - qstar)) = g qp := by
  rw [hS qp]
  field_simp

/-- **Exact ratio factorization (slope cancels, cofactor exact).** For a function
with the simple-zero factorization `S(q) = L·(q − q*)·g(q)` (`L ≠ 0`), and anchors
`qm ≠ q*` with `g(qm) ≠ 0`, the exact ratio of two evaluations factors as the
product of the anchor-offset ratio and the cofactor ratio:

  `S(qp)/S(qm) = (qp − q*)/(qm − q*) · g(qp)/g(qm)`.

The slope `L` drops out entirely — sharpening `linear_ratio_slope_independent` from
the leading-order (`g ≡ 1`) case to the full cofactor. This is the identity the
Route-A probe evaluates order-by-order in the Taylor truncation of `g`. -/
theorem exact_ratio_factorization
    {S g : ℝ → ℝ} {L qstar qm qp : ℝ}
    (hS : ∀ q, S q = L * (q - qstar) * g q)
    (hL : L ≠ 0) (hqm : qm - qstar ≠ 0) (hgm : g qm ≠ 0) :
    S qp / S qm = (qp - qstar) / (qm - qstar) * (g qp / g qm) := by
  rw [hS qp, hS qm]
  field_simp

/-- **The leading offset-ratio error is exactly the cofactor deviation.** The error
of approximating the exact ratio `S(qp)/S(qm)` by the *leading* anchor-offset ratio
`(qp − q*)/(qm − q*)` equals `(qp − q*)/(qm − q*) · (g(qp)/g(qm) − 1)`. This is the
closed form of the probe's **order-0 residual** (`≈ 6.18e-7`): the leading offset
ratio matches the exact magnitude only to the extent the cofactor ratio `g(qp)/g(qm)`
departs from `1`, so each Taylor order restored to `g` shrinks the miss. -/
theorem offset_ratio_error_is_cofactor
    {S g : ℝ → ℝ} {L qstar qm qp : ℝ}
    (hS : ∀ q, S q = L * (q - qstar) * g q)
    (hL : L ≠ 0) (hqm : qm - qstar ≠ 0) (hgm : g qm ≠ 0) :
    S qp / S qm - (qp - qstar) / (qm - qstar)
      = (qp - qstar) / (qm - qstar) * (g qp / g qm - 1) := by
  rw [exact_ratio_factorization hS hL hqm hgm]
  ring

/-- **Linear-model relative error under the normalization `g(q*) = 1`.** With the
cofactor normalized so that `g(q*) = 1`, the relative error of the leading linear
model `L·(qp − q*)` against the exact `S(qp)` is exactly `g(qp) − g(q*)`, the
cofactor's increment away from its value at the zero. This quantifies why one Taylor
order in `g` buys several digits: the linear model's miss *is* the cofactor's own
departure from the normalized `1` at `q*`. -/
theorem linear_model_relative_error
    {S g : ℝ → ℝ} {L qstar qp : ℝ}
    (hS : ∀ q, S q = L * (q - qstar) * g q)
    (hL : L ≠ 0) (hqp : qp - qstar ≠ 0) (hg1 : g qstar = 1) :
    (S qp - L * (qp - qstar)) / (L * (qp - qstar)) = g qp - g qstar := by
  rw [hg1, hS qp]
  field_simp

end QOU.QBeta.SLeakMagnitudeTaylorRatio
