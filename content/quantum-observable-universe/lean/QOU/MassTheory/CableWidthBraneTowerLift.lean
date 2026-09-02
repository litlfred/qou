/-
# Cable-width / brane-tower level selection for the A=3 Δ_λ magnitude — a WALL

Route 2 to the A=3 Δ_λ residual `1.6×`: is the cable width / brane-tower level for
the Borromean A=3 nucleon **derived** (not chosen), and does the derived level
close the residual at **0 fit**?

Established upstream (merged, sorry-free):
* `#4360 BorromeanThreeBodyCluster` — the Brunnian cluster sign
  `c₃^Borr = E₀·(1 − τ_Borr) > 0` supplies the `μ₃ = +0.4708 > 0` sign.
* `#4364 BorromeanMagnitudeLift` — the `H₉` joint-trace lift: each nucleon a
  **width-3 cable** (9 strands), `c₃(H₉) = +0.297 MeV = 0.63× μ₃`;
  `lift_is_coefficient_ratio` proves a level lift is a pure `κ`-rescale (the `h⁴`
  cancels), so a lift can **never** change the leading `h`-order — the residual
  `1.6×` is a *coefficient* question.
* `#4320 AdditiveResidualSimplex` — `μ₃ = +0.4708`.

**The question this file settles.**  What sets the per-nucleon cable width `w`
(hence the level `H_{A·w}`)?  The **derived** width of a nucleon is `w = 3` — the
`SU(3)_color` / three-quark strand count, i.e. the canonical `n₀ = 3A` atomic-braid
rule (`def:confined-particle`, `def:atomic-braid`: three strands per nucleon).
That is **exactly** `#4364`'s width, so the derived level is `H₉` and the derived
magnitude is `0.297 ≠ μ₃`.  **The derived width does not close the residual.**

The one corpus candidate for a derived level `≠ 9` — the brane-tower
level-selection rule `n★ = ℓ·n₀ + k` (`conj:brane-level-selection`, GAP-A-3) — is
**refuted** (deprecated internal negative, 2026-05-09: `probe_phiq_n_star_rule.py`,
predicted values `(n★^D,n★^T,n★^{3He}) = (14,27,20)` diverge `10⁵–10⁷ %` in the
`Φ_q` truncation).  Its refutation direction is **overshoot**: deeper levels blow
the magnitude *up*, exactly as `lift_is_coefficient_ratio` predicts (more strands
⇒ larger `κ`).  So no derived rule that *raises* the level helps either.

**Verdict: WALL (scope-(a)).**  No substrate-derived cable width / brane-tower
level closes the A=3 residual `1.6×` at `0` fit: the derived (color) width gives
the near-miss `0.297`, and the only alternate derived rule is refuted.  A closing
coefficient always exists *mathematically* (pick `κ★ = μ₃/(E₀h⁴)`), but it is not
the derived one — selecting a width to hit `μ₃` is a **fit** and is declined.

Base ring (§7c): `ℝ` — archimedean magnitude/ordering facts (a numeric derived
value `≠` a numeric target; a coefficient ratio `> 1`).
-/
import Mathlib.Tactic

namespace QOU.MassTheory.CableWidthBraneTower

/-! ### The joint-trace level is set by the per-nucleon cable width -/

/-- The `A`-nucleon joint trace lives at level `H_n` with `n = A · w`, where `w`
is the per-nucleon cable width (strand count).  `#4364` used `A = 3`, `w = 3`
⇒ `H₉`. -/
def jointTraceStrands (A w : ℕ) : ℕ := A * w

/-- **The derived cable width of a nucleon is `3`** — the `SU(3)_color` /
three-quark strand count, i.e. the canonical `n₀ = 3A` atomic-braid rule (three
strands per nucleon).  This is *derived* from the color content of a confined
particle, **not** chosen to hit any target. -/
def cableWidthColor : ℕ := 3

/-- The A=3 derived level is `H₉`: three nucleons × derived color width `3`. -/
theorem derived_level_A3 : jointTraceStrands 3 cableWidthColor = 9 := rfl

/-- **Substrate width rule, as a predicate ON a given width function.**

`w` is a per-nucleon-count cable width; `SubstrateWidthRule w` asserts that this
particular `w` is the `SU(3)_color` rule.

**Restated 2026-08-24 (bean `qou-2y13`).**  `w` was a *field* of the class and
`is_color` its only proposition, so the class pinned its own datum to a constant:
`SubstrateWidthRule` had exactly one model (up to `funext`), the global instance
`colorRule` supplied it, and `[SubstrateWidthRule]` was `w = fun _ => 3` spelled
as a hypothesis — a binder that constrained nothing.  Taking the width as a
*parameter* (the remedy worked in `QOU/Archimedean/JetOrderIndependence.lean`)
makes the hypothesis falsifiable: it holds of the colour width
(`colorRule`) and fails of any other (`not_widthRule_of_ne`, and concretely
`not_widthRule_width_four`).

Note what this does **not** touch: whether `cableWidthColor = 3` is derived from
the SU(3) colour content rather than fitted.  Take that at face value — it is a
claim about the physics, argued in the header, and the defect here was purely
structural. -/
class SubstrateWidthRule (w : ℕ → ℕ) : Prop where
  /-- The width is the colour count `3` for every nucleon count `A`. -/
  is_color : ∀ A, w A = cableWidthColor

/-- **The rule is satisfiable, at the derived colour width (PROVED).**  So
`[SubstrateWidthRule w]` for an *unspecified* `w` asserts only that some width
satisfies it; a downstream result must say which `w`. -/
instance colorRule : SubstrateWidthRule (fun _ => cableWidthColor) where
  is_color := fun _ => rfl

/-- **…and it fails at any width differing from `3` anywhere (PROVED).** -/
theorem not_widthRule_of_ne {w : ℕ → ℕ} {A : ℕ} (h : w A ≠ cableWidthColor) :
    ¬ SubstrateWidthRule w :=
  fun rule => h (rule.is_color A)

/-- **A concrete non-model (PROVED).**  A width-4 cable is not the colour width,
so the hypothesis is not satisfied by every width function.  This is the family
the header's `lift_is_coefficient_ratio` argument rules out: a wider cable is a
larger `κ`, never a different `h`-order. -/
theorem not_widthRule_width_four : ¬ SubstrateWidthRule (fun _ => 4) :=
  not_widthRule_of_ne (A := 0) (by decide)

/-- **From the derived width rule, the A=3 level is forced to be `H₉`** — the
level is *derived* from the width input, not chosen.

The parenthetical that used to sit here — *"Non-vacuous conditional: the level is
computed from the class field, not assumed"* — was the part to disbelieve, and it
is deleted.  The level *is* computed from the width, but `is_color` makes the
width `3` in every model, so `H₉` was never at risk and this said no more than
`derived_level_A3` above.  What the width actually buys is the `iff` below; this
statement is its forward half at the colour width. -/
theorem level_is_H9_of_rule (w : ℕ → ℕ) [rule : SubstrateWidthRule w] :
    jointTraceStrands 3 (w 3) = 9 := by
  rw [rule.is_color]; rfl

/-- **What the width buys, stated as an equivalence (PROVED).**  The A=3 level is
`H₉` **exactly when** the per-nucleon width is `3`.  Unlike
`level_is_H9_of_rule` this is falsifiable in both directions and needs no class
at all: it is the honest form of "the level is derived from the width". -/
theorem level_A3_eq_nine_iff (w : ℕ → ℕ) :
    jointTraceStrands 3 (w 3) = 9 ↔ w 3 = cableWidthColor := by
  unfold jointTraceStrands cableWidthColor
  omega

/-! ### Magnitude at a level = `E₀·h⁴·κ` (coefficient model, `BorromeanMagnitudeLift`) -/

/-- Level magnitude `c₃^L = E₀ · h⁴ · κ_L`, the coefficient model formalized in
`BorromeanMagnitudeLift` (`levelMagnitude`).  `κ_L` is the level's `h⁴`-coefficient
(count of Brunnian `h⁴` strand-pair configurations), set by the strand count. -/
noncomputable def levelMagnitude (E0 h κ : ℝ) : ℝ := E0 * (h ^ 4 * κ)

/-- The A=3 residual target moment (`AdditiveResidualSimplex #4320`). -/
def μ₃ : ℝ := 0.4708

/-- The derived (color width `3` ⇒ `H₉`) magnitude — the `0`-fit probe value from
`#4364`. -/
def derivedWidthMagnitude : ℝ := 0.297

/-! ### The derived width gives the near-miss, not a closure -/

/-- **Right sign at the derived width** (`#4360`): the derived-width magnitude is
strictly positive. -/
theorem derived_width_positive : 0 < derivedWidthMagnitude := by
  unfold derivedWidthMagnitude; norm_num

/-- **The derived width does NOT close the A=3 residual.**  Its magnitude is
`0.297 ≠ 0.4708 = μ₃`.  (Stated with the derived value as an explicit hypothesis
so `μ₃` never sets the coefficient.) -/
theorem derived_width_not_closes {E0 h κ : ℝ}
    (hv : levelMagnitude E0 h κ = derivedWidthMagnitude) :
    levelMagnitude E0 h κ ≠ μ₃ := by
  rw [hv]; unfold derivedWidthMagnitude μ₃; norm_num

/-- **A closing coefficient always exists mathematically** — for `E₀ ≠ 0`, `h ≠ 0`
take `κ★ = μ₃/(E₀·h⁴)`.  This is the crux of the WALL: closure is a *coefficient
existence*, so the physics question is not "does some `κ` close?" (it always does)
but "is the closing `κ` **substrate-derived**?" — and the derived (color) width's
coefficient gives `0.297`, not `μ₃`. -/
theorem closing_coefficient_exists {E0 h : ℝ} (hE : E0 ≠ 0) (hh : h ≠ 0) :
    ∃ κ : ℝ, levelMagnitude E0 h κ = μ₃ := by
  refine ⟨μ₃ / (E0 * h ^ 4), ?_⟩
  unfold levelMagnitude
  have h4 : h ^ 4 ≠ 0 := pow_ne_zero 4 hh
  field_simp

/-- **Closing forces a strictly larger coefficient than the derived width's.**
If the derived width gives magnitude `0.297` at coefficient `κ₉` and a level with
coefficient `κ★` closes (`= μ₃`), then `κ★ / κ₉ = μ₃ / 0.297 > 1` (the shared
`E₀·h⁴` cancels).  So any closing level has a **strictly larger** `h⁴`-coefficient
than the derived (color) level — its width is not the derived width.  This
*quantifies* the missing `~1.585×` coefficient without inverting `μ₃` to set it. -/
theorem closing_needs_larger_coefficient {E0 h κ₉ κc : ℝ}
    (hE : E0 ≠ 0) (hh : h ≠ 0)
    (h9 : levelMagnitude E0 h κ₉ = derivedWidthMagnitude)
    (hs : levelMagnitude E0 h κc = μ₃) :
    κc / κ₉ = μ₃ / derivedWidthMagnitude ∧ (1 : ℝ) < μ₃ / derivedWidthMagnitude := by
  have h4 : h ^ 4 ≠ 0 := pow_ne_zero 4 hh
  refine ⟨?_, by unfold μ₃ derivedWidthMagnitude; norm_num⟩
  -- κc/κ₉ = μ₃/0.297 : the shared E₀·h⁴ cancels
  rw [← hs, ← h9]
  unfold levelMagnitude
  rw [mul_div_mul_left _ _ hE, mul_div_mul_left _ _ h4]

/-! ### The WALL summary -/

/-- **WALL (scope-(a)) — the derived cable width / brane-tower level does not close
the A=3 residual `0`-fit.**  At the derived (color) width `w = 3` (level `H₉`) the
magnitude is strictly positive (sign derived, `#4360`) but `≠ μ₃` (near-miss,
`0.63× μ₃`); and any level that *does* close needs a strictly larger derived
`h⁴`-coefficient (ratio `μ₃/0.297 > 1`), which no substrate rule supplies — the
one candidate (`n★ = ℓ·n₀ + k`) is refuted, overshooting.  Right sign, right order,
exact closure open — not a fit, not a hard structural exclusion. -/
theorem cable_width_wall {E0 h κ₉ : ℝ}
    (hE : E0 ≠ 0) (hh : h ≠ 0)
    (h9 : levelMagnitude E0 h κ₉ = derivedWidthMagnitude) :
    0 < levelMagnitude E0 h κ₉ ∧
      levelMagnitude E0 h κ₉ ≠ μ₃ ∧
      ∀ κc, levelMagnitude E0 h κc = μ₃ →
        (1 : ℝ) < μ₃ / derivedWidthMagnitude := by
  refine ⟨?_, derived_width_not_closes h9, ?_⟩
  · rw [h9]; exact derived_width_positive
  · intro κc hs
    exact (closing_needs_larger_coefficient hE hh h9 hs).2

end QOU.MassTheory.CableWidthBraneTower
