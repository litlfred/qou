import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

/-!
# α_D is bar-MIXED — the obstruction to porting the C bar-split to D (qou-qb8g / qou-cds1)

Convention C pins the c₃ bar-even channel because the C rung phase
`α_C = (z_C − 1)·h/2` is **pure bar-odd** (`α_C(1/q) = −α_C(q)`, already proved
sorry-free as `QOU.Interactions.eigenphase_bar_involution`, since `z_C` is
bar-even). This file supplies the contrasting D fact: the convention-D rung
phase `α_D = (z_D − 1)·h/2`, with the sqrt-free canonical `z_D = q³/(q²+1)`, is
**bar-MIXED** — its bar-even part is nonzero — because `z_D` is not
bar-homogeneous. So the pure-odd-phase mechanism that pinned the C split has
**no D analog**, which is the exact structural obstruction recorded in the
2026-08-29 convention-D front audit (bean qou-qb8g).

`h = q − q⁻¹` is bar-odd; the bar involution is `q ↦ q⁻¹`. Archimedean by the
ordering/positivity used for nonvanishing, so `ℝ` per AGENTS.md §7c.

Verified symbolically (sympy) before formalising:
`2α_D(1/q) + 2α_D(q) = (q²−1)²/q²`, nonzero for `q ∉ {0, ±1}`.

-- Ref: [leitner2026] docs/audits/2026-08-29-convention-d-qbeta-front-adversarial-audit.md
-/

namespace QOU.QBeta.EigenphaseBarMixedD

/-- Convention-D Markov parameter (sqrt-free): `z_D(q) = q³/(q²+1)`. Matches the
    canonical `QOU.BraidKnot.JonesNuclearQuotient.markovZ`. -/
noncomputable def zD (q : ℝ) : ℝ := q ^ 3 / (q ^ 2 + 1)

/-- Hecke–Skein differential `h(q) = q − q⁻¹` (bar-odd). -/
noncomputable def heckeH (q : ℝ) : ℝ := q - q⁻¹

/-- Twice the D rung phase, `2α_D(q) = (z_D(q) − 1)·h(q)` — the counit-minus-trace
    gap in the D frame. -/
noncomputable def twoAlphaD (q : ℝ) : ℝ := (zD q - 1) * heckeH q

/-- **α_D's bar-even part is nonzero (closed form).** Under `q ↦ q⁻¹`,
    `2α_D(1/q) + 2α_D(q) = (q²−1)²/q²`. A pure bar-odd phase would give `0`
    (cf. `α_C`, `QOU.Interactions.eigenphase_bar_involution`); this is the
    D-frame contrast. -/
theorem twoAlphaD_bar_even_sum (q : ℝ) (hq : q ≠ 0) :
    twoAlphaD q⁻¹ + twoAlphaD q = (q ^ 2 - 1) ^ 2 / q ^ 2 := by
  unfold twoAlphaD zD heckeH
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  have h2 : (q⁻¹) ^ 2 + 1 ≠ 0 := by positivity
  field_simp
  ring

/-- **α_D is NOT bar-odd** at any admissible substrate point (`q ∉ {0, ±1}`): its
    bar-even part `(q²−1)²/q²` is strictly positive, so it cannot vanish the way a
    pure bar-odd phase would. This is the obstruction: no D analog of the C
    even-channel pin exists via the bar involution. -/
theorem twoAlphaD_not_bar_odd (q : ℝ) (hq : q ≠ 0) (hq1 : q ^ 2 ≠ 1) :
    twoAlphaD q⁻¹ + twoAlphaD q ≠ 0 := by
  rw [twoAlphaD_bar_even_sum q hq]
  have hnum : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr hq1
  have : (0 : ℝ) < (q ^ 2 - 1) ^ 2 / q ^ 2 := by positivity
  exact ne_of_gt this

end QOU.QBeta.EigenphaseBarMixedD

#print axioms QOU.QBeta.EigenphaseBarMixedD.twoAlphaD_not_bar_odd
#print axioms QOU.QBeta.EigenphaseBarMixedD.twoAlphaD_bar_even_sum
