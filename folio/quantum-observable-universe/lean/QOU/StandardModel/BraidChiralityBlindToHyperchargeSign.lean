import QOU.StandardModel.HyperchargeSignIsBringOrientation

/-!
# Braid chirality on `UT(Σ₄)` cannot fix the hypercharge sign

Bean `qou-h0zz` (owner pick "Orientation from braid chirality", 2026-11-28).

`prop:hypercharge-sign-is-bring-orientation` identifies the open hypercharge sign with the
orientation of Bring's surface: in the reflection-odd copy of `H¹` the orientation reversal `c`
sends `Y` to `−Y` (`minus_copy_c_flips`). The question here is whether the braid side fixes
that orientation. The corpus puts the strands on the unit tangent bundle `UT(Σ₄)` and fixes
their crossing signs by `q₀ > 1` and the canonical contact orientation `α ∧ dα`
(`QOU/BringsSurface/BringUTContactChirality.lean`, owner ruling 2026-10-12, geodesic `α`).

## The obstruction

An isometry `φ` of the base with orientation sign `ε = det dφ` lifts to `UT(Σ)` with Jacobian
`ε` on the base and `ε` on the fibre angle, so its orientation sign on `UT(Σ)` is `ε · ε = 1`
(`lift_orientation_sign`). This is `iota_lift_det` (`diag(−1, 1, −1)`, determinant `+1`) for
`z ↦ −z̄`, and it is why `iota_pullback_alpha` finds conjugation preserving `α` itself. So
`c` preserves the orientation of `UT(Σ₄)`, the contact form, every crossing sign and the
canonical residue `−1/6`, while it sends `Y` to `−Y`.

`no_equivariant_hypercharge_from_UT` makes this exact: no rule that reads a hypercharge vector
off the `UT(Σ₄)` orientation can send the two base orientations to `Y` and `−Y`. This is a
structural exclusion for this one ingredient, with the invariant `ε² = 1`. It does not exclude a
source that sees the base orientation directly, for example the complex structure of Bring's
curve itself.

Integer and rational arithmetic only. No empirical value enters.
-/

namespace QOU.StandardModel.BraidChiralityBlind

open QOU.StandardModel.BringTwist QOU.StandardModel.BringOrientation

/-- Orientation sign on `UT(Σ)` of the lift of a base isometry with orientation sign `ε`: the
base contributes `ε` and the fibre angle contributes `ε`. -/
def liftSign (ε : ℤˣ) : ℤˣ := ε * ε

theorem lift_orientation_sign (ε : ℤˣ) : liftSign ε = 1 := by
  rcases Int.units_eq_one_or ε with h | h <;> simp [liftSign, h]

theorem Y_ne_neg_Y : Y ≠ -Y := by
  intro h; have := congrFun h 3; simp [Y] at this; norm_num at this

/-- **No hypercharge from the `UT(Σ₄)` orientation.** A rule `h` reading a charge vector off
the orientation of `UT(Σ₄)` cannot give `Y` for one base orientation and `−Y` for the other,
which is what the orientation reversal `c` does in the reflection-odd copy. -/
theorem no_equivariant_hypercharge_from_UT (h : ℤˣ → (Fin 5 → ℚ)) :
    ¬ (h (liftSign 1) = Y ∧ h (liftSign (-1)) = act (-1) 1 true Y) := by
  rintro ⟨h1, h2⟩
  rw [minus_copy_c_flips, lift_orientation_sign] at h2
  rw [lift_orientation_sign] at h1
  exact Y_ne_neg_Y (h1.symm.trans h2)

end QOU.StandardModel.BraidChiralityBlind
