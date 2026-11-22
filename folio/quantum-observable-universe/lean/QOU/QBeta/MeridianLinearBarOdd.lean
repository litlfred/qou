import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic

/-!
# The bar-odd linear meridian term: `Im S(u) ⊃ π·u` and its growth-rate response

PR #3691 measured, on the deformed figure-eight ladder at the substrate
meridian, that the real growth rate `Re α(u)` exceeds the pure-volume
prediction `2π·Vol(u)/(u² + 4π²)` by

    resid(u) = (1/2)·u + b·u² + O(u³),   a = 0.4999985 (≈ 1/2 to 5 digits).

This file formalizes the ALGEBRAIC layer of that finding — the exact response
model and its parity. If the deformed action carries the linear meridian term
`Im S(u) = Vol(u) + π·u + O(u²)`, then the induced growth-rate residual is
exactly

    meridianLinearResponse u = 2π²·u / (u² + 4π²),

which (i) is an ODD function of `u` — the bar involution acts as `u ↦ −u`
(`σ : q ↦ q⁻¹`, `u = 2 log q`), so this is a **bar-odd channel**, in contrast
to the bar-even volume channel (`Vol` even in `u` by amphichirality of 4₁);
(ii) equals `u/2` up to the exact remainder `u³/(2(u²+4π²))`, bounded by
`|u|³/(8π²)` — which is why the measured linear coefficient reads `1/2`.

Honest scope: the numerical extraction (that the 4₁ asymptotic really contains
`π·u`) is the witness's empirical content
(`qbeta-ohtsuki-deformed-meridian-rungs.witness.json`); the Lean proves the
exact response algebra and parity, NOT the analytic asymptotics of `J_N`.

Base ring is `ℝ` by necessity (§7c archimedean side): `π` and the ordering in
the bound are the content. No `sorry`.

-- Ref: [ohtsuki-takata-2015] deformed 4₁ asymptotic (theorem-grade regime)
--   (repointed from the dead key `murakami2013`, 2026-09-03. Evidence is in
--    this file: the witness it names is
--    `qbeta-ohtsuki-deformed-meridian-rungs.witness.json`, and
--    [ohtsuki-takata-2015] is the theorem-grade asymptotic for two-bridge
--    knots, of which 4₁ is one. The 2013 Murakami work the original key
--    named is not in `references.ts` nor in `library/`, `ocr/` tier
--    included. Inferred repoint, not a recovered citation.)
-- Ref: [leitner2026] docs/audits/2026-07-12-bar-odd-s-three-routes.md
-/

namespace QOU.QBeta

open Real

/-- Growth-rate residual produced by a linear meridian term `π·u` in `Im S(u)`:
    `2π²·u / (u² + 4π²)` — the model measured in PR #3691 with the leading
    coefficient `1/2`. -/
noncomputable def meridianLinearResponse (u : ℝ) : ℝ :=
  2 * π ^ 2 * u / (u ^ 2 + 4 * π ^ 2)

/-- **The response of an `Im S(u) ⊃ π·u` term is exactly
    `meridianLinearResponse`.** Adding `π·u` to the volume in the growth-rate
    formula `2π·(…)/(u² + 4π²)` shifts it by exactly the response model —
    the algebraic content of "the measured residual is the `π·u` term". -/
theorem alpha_resid_of_meridian_term (Vol : ℝ → ℝ) (u : ℝ) :
    2 * π * (Vol u + π * u) / (u ^ 2 + 4 * π ^ 2)
      - 2 * π * Vol u / (u ^ 2 + 4 * π ^ 2) = meridianLinearResponse u := by
  have hpos : (0 : ℝ) < u ^ 2 + 4 * π ^ 2 := by positivity
  unfold meridianLinearResponse
  field_simp [hpos.ne']
  ring

/-- **Bar-odd parity.** The bar involution `σ : q ↦ q⁻¹` acts on the meridian
    as `u ↦ −u`; the linear-meridian response is an odd function of `u` —
    a bar-ODD channel. -/
theorem meridianLinearResponse_odd (u : ℝ) :
    meridianLinearResponse (-u) = -meridianLinearResponse u := by
  unfold meridianLinearResponse
  rw [neg_sq]
  ring

/-- **The bar-even volume channel, for contrast.** For an even volume function
    (4₁ is amphichiral: `Vol(−u) = Vol(u)`), the volume term of the growth
    rate is even in `u` — the bar-EVEN channel. -/
theorem volChannel_even (Vol : ℝ → ℝ) (hV : ∀ u, Vol (-u) = Vol u) (u : ℝ) :
    2 * π * Vol (-u) / ((-u) ^ 2 + 4 * π ^ 2)
      = 2 * π * Vol u / (u ^ 2 + 4 * π ^ 2) := by
  rw [hV, neg_sq]

/-- **Exact `u/2` deficit identity.** The response equals `u/2` minus an
    explicit cubic remainder: `u/2 − resp(u) = u³ / (2(u² + 4π²))`. -/
theorem half_u_sub_response (u : ℝ) :
    u / 2 - meridianLinearResponse u = u ^ 3 / (2 * (u ^ 2 + 4 * π ^ 2)) := by
  have hpos : (0 : ℝ) < u ^ 2 + 4 * π ^ 2 := by positivity
  unfold meridianLinearResponse
  field_simp [hpos.ne']
  ring

/-- **Why the measured coefficient reads `1/2`.** The response deviates from
    `u/2` by at most `|u|³/(8π²)` — at the substrate meridian `u ≈ 0.209` this
    is `≈ 1.2×10⁻⁴`, far below the linear term, so the ladder fit returns
    `a = 1/2` to the observed precision. -/
theorem meridianLinearResponse_near_half_u (u : ℝ) :
    |u / 2 - meridianLinearResponse u| ≤ |u| ^ 3 / (8 * π ^ 2) := by
  have hden : (0 : ℝ) < 2 * (u ^ 2 + 4 * π ^ 2) := by positivity
  have hbound : 8 * π ^ 2 ≤ 2 * (u ^ 2 + 4 * π ^ 2) := by nlinarith [sq_nonneg u]
  rw [half_u_sub_response, abs_div, abs_of_pos hden, abs_pow]
  gcongr

end QOU.QBeta
