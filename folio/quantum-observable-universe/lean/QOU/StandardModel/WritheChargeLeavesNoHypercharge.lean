import Mathlib.Data.Rat.Defs
import Mathlib.Tactic

/-!
# A writhe charge and a writhe isospin leave no room for a hypercharge

`def:coulomb-charge` names the halved writhe `Q = w/2` the Coulomb charge, and
`rem:flavor-charge-assignments` reads the isospin `I₃` as the writhe coordinate.
`conj:sm-hypercharge-invariant` (Lean class `QOU.StandardModel.HyperchargeInvariant`) asks for
a hypercharge `Y` with `Q = I₃ + Y/2` that does **not** factor through the writhe.

`hypercharge_factors_of_charge_and_isospin_factor` proves that if both `Q` and `I₃` are
functions of the writhe, then so is `Y = 2(Q − I₃)`. So the two readings cannot both hold in
any instance of that class: at least one of "`Q` is the halved writhe" and "`I₃` is the writhe
coordinate" has to go. `isospin_not_writhe_of_charge_writhe` states the consequence for the
intended instantiation `Q = w/2`.

The lemma was found and recorded, but not added, in bean `qou-tnho` (2026-08). It is elementary
and fixes nothing about `Y`.
-/

namespace QOU.StandardModel.WritheChargeHypercharge

/-- If `Q` and `I₃` factor through `w` and `Q = I₃ + Y/2`, then `Y` factors through `w`. -/
theorem hypercharge_factors_of_charge_and_isospin_factor {S : Type*}
    (w : S → ℤ) (Q I3 Y : S → ℚ)
    (hGMN : ∀ X, Q X = I3 X + Y X / 2)
    (hQ : ∃ f : ℤ → ℚ, ∀ X, Q X = f (w X))
    (hI : ∃ g : ℤ → ℚ, ∀ X, I3 X = g (w X)) :
    ∃ h : ℤ → ℚ, ∀ X, Y X = h (w X) := by
  obtain ⟨f, hf⟩ := hQ
  obtain ⟨g, hg⟩ := hI
  refine ⟨fun z => 2 * (f z - g z), fun X => ?_⟩
  have := hGMN X
  rw [hf X, hg X] at this
  simp only
  linarith

/-- **With the halved-writhe charge, a hypercharge forces a non-writhe isospin.** If
`Q = w/2` and `Q = I₃ + Y/2` with `Y` not a function of the writhe, then `I₃` is not a
function of the writhe either. -/
theorem isospin_not_writhe_of_charge_writhe {S : Type*}
    (w : S → ℤ) (I3 Y : S → ℚ)
    (hGMN : ∀ X, (w X : ℚ) / 2 = I3 X + Y X / 2)
    (hY : ¬∃ h : ℤ → ℚ, ∀ X, Y X = h (w X)) :
    ¬∃ g : ℤ → ℚ, ∀ X, I3 X = g (w X) := by
  intro hI
  exact hY (hypercharge_factors_of_charge_and_isospin_factor w (fun X => (w X : ℚ) / 2) I3 Y
    hGMN ⟨fun z => (z : ℚ) / 2, fun _ => rfl⟩ hI)

end QOU.StandardModel.WritheChargeHypercharge
