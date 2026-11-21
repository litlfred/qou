import QOU.MathlibExt.BraidGroup
import Mathlib.Tactic.Group

/-!
# Electron and positron words are a mirror pair, told apart by the writhe

Owner ruling 2026-11-21: the electron is `e⁻ = σ₀σ₁σ₀ ∈ B₃`, whose closure is
the positive Hopf link. The positron is the mirror word
`e⁺ = σ₀⁻¹σ₁⁻¹σ₀⁻¹`, whose closure is the negative Hopf link.

The trefoil, the backup electron, is chiral as an unoriented knot. The Hopf
link is not: its mirror is itself with one component reversed. So under the
ruling the electron–positron distinction cannot be read off the unoriented
closure. This file records where it does live, at the level of the braid
group:

* `positron_eq_inv` — `e⁺ = (e⁻)⁻¹`;
* `exponentSum_electron`, `exponentSum_positron` — writhe `+3` and `−3`, a
  well-defined invariant of the braid (`QOU.MathlibExt.Braid.exponentSum`);
* `electron_ne_positron` — hence `e⁻ ≠ e⁺` in `B₃`.

-- Ref: [leitner2026] predicted-spectra, chirality-trefoil-electron-positron
-- Ref: docs/coordination/owner-rulings.md (electron word, 2026-11-21)
-/

namespace QOU.BraidKnot.ElectronPositronWrithe

open QOU.MathlibExt.Braid

/-- The electron word `e⁻ = σ₀σ₁σ₀ ∈ B₃`. -/
def electron : BraidGroup 2 := σ 0 * σ 1 * σ 0

/-- The positron word `e⁺ = σ₀⁻¹σ₁⁻¹σ₀⁻¹ ∈ B₃`. -/
def positron : BraidGroup 2 := (σ 0)⁻¹ * (σ 1)⁻¹ * (σ 0)⁻¹

/-- The mirror word is the inverse braid. -/
theorem positron_eq_inv : positron = electron⁻¹ := by
  unfold positron electron
  group

/-- The electron word has writhe `+3`. -/
theorem exponentSum_electron :
    exponentSum 2 electron = Multiplicative.ofAdd (3 : ℤ) := by
  unfold electron
  simp only [map_mul, exponentSum_σ]
  rfl

/-- The positron word has writhe `−3`. -/
theorem exponentSum_positron :
    exponentSum 2 positron = Multiplicative.ofAdd (-3 : ℤ) := by
  rw [positron_eq_inv, map_inv, exponentSum_electron]
  rfl

/-- **The electron and positron words are distinct braids.** -/
theorem electron_ne_positron : electron ≠ positron := by
  intro h
  have h3 := congrArg (exponentSum 2) h
  rw [exponentSum_electron, exponentSum_positron] at h3
  exact absurd (Multiplicative.ofAdd.injective h3) (by decide)

end QOU.BraidKnot.ElectronPositronWrithe
