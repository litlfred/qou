/-
# The Borromean 3-body MAGNITUDE lift is a coefficient rescale, not an order change
# — and the A=3 Δ_λ magnitude closure is a conditional coefficient identity.

Companion to `QOU.MassTheory.BorromeanThreeBodyCluster` (#4360), which proved the
Brunnian cluster `c₃ = E₀·(1 − τ_Borr) ≥ 0` supplies the `μ₃ = +0.4708 > 0`
**sign** the multiplicative pairwise route cannot — but at the **bare `H₃`** level
its magnitude is `≈ +0.006 MeV`, `~78×` below `μ₃`.  The one honest gap #4360 left
is the **magnitude**.

**This file formalizes the structural invariant behind the H₉ magnitude-lift probe**
(`computations/deltalambda/borromean_h9_magnitude_lift_probe.py`).  The probe lifts
the Borromean cluster to the *same* `H₉` joint-trace level `ρ_F` used (three width-3
nucleon cables, `g = Σ_{λ⊢9} y_λ|χ_λ|·E₀`, the cabled linking `(Δ_A·Δ_B⁻¹)³`), 0
fit, and MEASURES the deficit's leading `h`-exponent to be `4.098` — i.e. **the
cabling PRESERVES the Brunnian order-suppression**: like the bare `H₃` deficit
`h⁴(3+h²)/(h²+4)`, the cabled deficit is `O(h⁴)`.

The invariant we prove:

* **`brunnianDeficit` shape.**  A Brunnian-order-suppressed level deficit is
  `D_L(h) = h⁴ · κ_L(h)` with the level's `h⁴`-coefficient `κ_L(0)`.  (Every
  2-sub-link trivial kills the `O(h), O(h²), O(h³)` parts; the leading term is
  exactly order 4.)  The bare `H₃` deficit realises this with
  `κ_bare(h) = (3 + h²)/(h² + 4)`, `κ_bare(0) = 3/4 > 0`.

* **Order-invariance of a level lift (`lift_is_coefficient_ratio`).**  For two
  levels with deficits `h⁴·κ₁ h` and `h⁴·κ₂ h` (`h ≠ 0`, `κ₂ h ≠ 0`), the lift
  ratio is `κ₁ h / κ₂ h` — the `h⁴` cancels.  **A level lift is a coefficient
  rescale; it can NEVER change the leading `h`-order.**  This is why the `~49×`
  `H₃ → H₉` lift is a derived *coefficient* enhancement (three width-3 cables
  ⇒ `~49×` more `h⁴` strand-pairs), not a fit and not an order change.

* **Closure is a conditional coefficient identity (`magnitude_closes_iff`).**  The
  A=3 magnitude closes at level `L` iff `E₀·κ_L·h⁴ = μ₃`.  The `H₉` level yields
  the derived value `v_{H₉} = E₀·κ_{H₉}·h⁴ = 0.297` (probe, 0 fit), and
  `μ₃ = 0.4708`, with `v_{H₉} ≠ μ₃` (`~1.6×` short).  Hence
  `not_closed_at_H9`: the `H₉` level does **not** close the A=3 magnitude.

This is the honest **scope-(a) NEAR-MISS LEAD**, NOT a Δ_λ closure and NOT a fit:
the sign is derived (#4360), the magnitude *order* is recovered 0-fit (`O(h⁴)`,
`0.63× μ₃`), the exact coefficient identity `E₀·κ·h⁴ = μ₃` is **open**.  `μ₃` is
never inverted to set any `κ`; nothing is wired.  Closing the residual `1.6×` by a
tuned cable width / tower height would be a FIT and is declined.

Base ring (§7c): `ℝ`, because the statements are archimedean magnitude/ordering
facts (positive coefficients, a numeric value `≠` a numeric target).
-/
import Mathlib.Tactic

-- Declarations here are nested one namespace deeper than the module's
-- parent so this module and QOU.MassTheory.BraneTowerLevelAmplitude
-- can be imported together: both declared the same fully-qualified
-- name(s), and Lean rejects the second import with "environment already
-- contains" (bean `qou-kfcl`). Nothing imports this module, so the
-- nesting costs no consumer.
namespace QOU.MassTheory.BorromeanMagnitudeLift

/-! ### Brunnian-order-suppressed level deficit: `D_L(h) = h⁴ · κ_L(h)` -/

/-- A Brunnian (order-`h⁴`-suppressed) level deficit with `h⁴`-coefficient
function `κ`: `D_L(h) = h⁴ · κ h`.  The leading order is exactly 4 whenever
`κ 0 ≠ 0` — every 2-sub-link of a Brunnian object is trivial, so the `O(h)`,
`O(h²)`, `O(h³)` parts vanish. -/
noncomputable def brunnianDeficit (κ : ℝ → ℝ) (h : ℝ) : ℝ := h ^ 4 * κ h

/-- The bare-`H₃` Borromean `h⁴`-coefficient (from #4360's closed form
`1 − τ_Borr = h⁴(3 + h²)/(h² + 4)`): `κ_bare(h) = (3 + h²)/(h² + 4)`. -/
noncomputable def kappaBare (h : ℝ) : ℝ := (3 + h ^ 2) / (h ^ 2 + 4)

/-- The bare-`H₃` deficit realises the `brunnianDeficit` shape with `κ = κ_bare`:
`h⁴(3+h²)/(h²+4) = brunnianDeficit κ_bare h`. -/
theorem bare_deficit_eq_brunnian (h : ℝ) :
    h ^ 4 * (3 + h ^ 2) / (h ^ 2 + 4) = brunnianDeficit kappaBare h := by
  unfold brunnianDeficit kappaBare
  ring

/-- The bare-`H₃` `h⁴`-coefficient at `h = 0` is `3/4 > 0`: the leading-order-4
coefficient is genuinely nonzero, so the bare deficit is exactly `O(h⁴)`. -/
theorem kappaBare_zero_pos : 0 < kappaBare 0 := by
  unfold kappaBare; norm_num

/-- `κ_bare(h) > 0` for every real `h` (`3 + h² > 0`, `h² + 4 > 0`): the bare
level's `h⁴`-coefficient never vanishes, so the deficit is a *positive* `O(h⁴)`. -/
theorem kappaBare_pos (h : ℝ) : 0 < kappaBare h := by
  unfold kappaBare
  apply div_pos <;> positivity

/-! ### A level lift is a coefficient ratio — never an order change -/

/-- **Order-invariance of a level lift.**  For two Brunnian-order-suppressed
levels with deficits `h⁴·κ₁ h` and `h⁴·κ₂ h`, the lift ratio is `κ₁ h / κ₂ h`:
the shared `h⁴` factor cancels.  A level lift therefore rescales the *coefficient*
and **cannot change the leading `h`-order**.  (The measured `H₃→H₉` exponent stays
`4.098`; the `~49×` lift lives entirely in `κ_{H₉}/κ_bare`.) -/
theorem lift_is_coefficient_ratio {κ₁ κ₂ : ℝ → ℝ} {h : ℝ}
    (hh : h ≠ 0) (hκ₂ : κ₂ h ≠ 0) :
    brunnianDeficit κ₁ h / brunnianDeficit κ₂ h = κ₁ h / κ₂ h := by
  unfold brunnianDeficit
  have h4 : h ^ 4 ≠ 0 := pow_ne_zero 4 hh
  field_simp

/-- The physical magnitude at a level is `c₃^L = E₀ · D_L(h) = E₀ · h⁴ · κ_L`
(the `κ` evaluated at the physical `h`, treated as the level's coefficient). -/
noncomputable def levelMagnitude (E0 h κ : ℝ) : ℝ := E0 * (h ^ 4 * κ)

/-- **Positive `O(h⁴)` magnitude.**  With `E₀ > 0`, `h ≠ 0`, and a positive
level coefficient `κ > 0`, the level magnitude is strictly positive — the same
`+` sign #4360 derived, at any Brunnian-order-suppressed level. -/
theorem levelMagnitude_pos {E0 h κ : ℝ} (hE : 0 < E0) (hh : h ≠ 0) (hκ : 0 < κ) :
    0 < levelMagnitude E0 h κ := by
  unfold levelMagnitude
  have h4 : 0 < h ^ 4 := by positivity
  positivity

/-! ### A=3 Δ_λ magnitude closure is a conditional coefficient identity -/

/-- **Magnitude-closure predicate.**  The A=3 Δ_λ magnitude closes at a level with
coefficient `κ` iff its magnitude equals the target moment `μ₃`:
`E₀ · h⁴ · κ = μ₃`.  This is a *coefficient* identity — the level (hence `κ`) is
FIXED and derived, `μ₃` is the target; a `κ` tuned to satisfy it would be a FIT. -/
def MagnitudeCloses (E0 h κ μ₃ : ℝ) : Prop := levelMagnitude E0 h κ = μ₃

theorem magnitude_closes_iff {E0 h κ μ₃ : ℝ} :
    MagnitudeCloses E0 h κ μ₃ ↔ E0 * (h ^ 4 * κ) = μ₃ := Iff.rfl

/-- **The `H₉` level does NOT close the A=3 magnitude (near-miss).**  The derived
`H₉` cabled-Borromean magnitude is `v_{H₉} = 0.297` (probe, 0 fit) and the target
is `μ₃ = 0.4708`; since `0.297 ≠ 0.4708`, closure fails at the `H₉` level.  This is
the honest near-miss: right sign, right order (`O(h⁴)`, `0.63× μ₃`), exact
coefficient identity **open**.  (Stated with the derived value as an explicit
hypothesis so `μ₃` never sets any coefficient.) -/
theorem not_closed_at_H9 {E0 h κ : ℝ}
    (hv : levelMagnitude E0 h κ = (0.297 : ℝ)) :
    ¬ MagnitudeCloses E0 h κ (0.4708 : ℝ) := by
  unfold MagnitudeCloses
  rw [hv]
  norm_num

/-- **Order recovered, coefficient open (the scope-(a) summary).**  At the `H₉`
level (`E₀ > 0`, `h ≠ 0`, derived coefficient `κ > 0`) the magnitude is strictly
positive (sign derived, #4360) AND, given the derived numeric value `0.297`, it is
*not* equal to `μ₃ = 0.4708`.  So the magnitude *order/sign* is recovered 0-fit
while the exact closure `= μ₃` stays open — NEAR-MISS LEAD, not a closure. -/
theorem borromean_H9_near_miss {E0 h κ : ℝ}
    (hE : 0 < E0) (hh : h ≠ 0) (hκ : 0 < κ)
    (hv : levelMagnitude E0 h κ = (0.297 : ℝ)) :
    0 < levelMagnitude E0 h κ ∧ ¬ MagnitudeCloses E0 h κ (0.4708 : ℝ) :=
  ⟨levelMagnitude_pos hE hh hκ, not_closed_at_H9 hv⟩

end QOU.MassTheory.BorromeanMagnitudeLift
