import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic.IntervalCases

/-!
# QOU.Core.FlavourVolumeForcesDimThree — `Λ³W ≅ 𝟙` forces `dim W = 3`, at the fibre

Bean `qou-x08k`.  Flavour twin of `VolumeConstraintForcesFibreTwo`
(`exteriorSquareDim_eq_one_iff`: `C(N,2) = 1 ↔ N = 2`).

`QOU.Core.FlavourLabelCarrier.unit_flavour_meets_axioms` shows that the categorical flavour
fields of `FlavouredQuantumObservableUniverse` are met by a one-dimensional `W`.  The reason
is that `exteriorCube` is only required to be *some* quotient of `W^{⊗3}`, not the
antisymmetric one.  Read at a fibre where `exteriorCube` **is** `Λ³` of an `N`-dimensional
space, the iso `Λ³W ≅ 𝟙` says `C(N,3) = 1`, and that has the unique solution `N = 3`:

* `exteriorCubeDim_eq_one_iff` — `C(N,3) = 1 ↔ N = 3` (strong, iso reading).
* `exteriorCubeDim_ne_zero_iff` — `C(N,3) ≠ 0 ↔ 3 ≤ N` (weak, epi reading).
* `exteriorCubeDim_one` — `C(1,3) = 0`: the one-dimensional `W` of the label carrier is
  excluded at the fibre, so it meets the categorical fields only because the quotient is
  not pinned.

## Honest label

This does not change the axiom set.  It locates the gap: the flavour fields force
`dim W = 3` once `exteriorCube` is pinned as the antisymmetric quotient.  The same is true of
`V` and `exteriorSquare` (`C(N,2) = 1 ↔ N = 2`), whose quotient is also left unpinned on
purpose, since the braiding eigenvalue on `Λ²` is `-q⁻¹`, not `-1`.  Pinning either needs an
antisymmetriser in the category, which is an owner decision.  Combinatorics only.
-/

namespace QOU.FlavourVolumeForcesDimThree

/-- Fibre dimension of `Λ³W` for `dim W = N`. -/
def exteriorCubeDim (N : ℕ) : ℕ := Nat.choose N 3

/-- **Weak (epi) reading**: `Λ³W ↠ 𝟙` needs `Λ³W ≠ 0`, i.e. `N ≥ 3`. -/
theorem exteriorCubeDim_ne_zero_iff (N : ℕ) : exteriorCubeDim N ≠ 0 ↔ 3 ≤ N := by
  unfold exteriorCubeDim
  rw [Ne, Nat.choose_eq_zero_iff]
  omega

/-- **Strong (iso) reading**: `Λ³W ≅ 𝟙` forces `N = 3`. -/
theorem exteriorCubeDim_eq_one_iff (N : ℕ) : exteriorCubeDim N = 1 ↔ N = 3 := by
  unfold exteriorCubeDim
  refine ⟨fun h => ?_, fun h => by subst h; rfl⟩
  by_contra hne
  rcases Nat.lt_or_ge N 4 with hlt | hge
  · interval_cases N <;> first | exact hne rfl | (revert h; decide)
  · have hmono : Nat.choose 4 3 ≤ Nat.choose N 3 := Nat.choose_le_choose 3 hge
    have h4 : Nat.choose 4 3 = 4 := rfl
    omega

/-- The one-dimensional `W` has `Λ³W = 0` at the fibre. -/
theorem exteriorCubeDim_one : exteriorCubeDim 1 = 0 := rfl

/-- The `SU(2)` fibre `N = 2` has no flavour volume form either. -/
theorem exteriorCubeDim_two : exteriorCubeDim 2 = 0 := rfl

end QOU.FlavourVolumeForcesDimThree
