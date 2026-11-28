import QOU.StandardModel.BraidChiralityBlindToHyperchargeSign

/-!
# Where the complex volume can carry the hypercharge sign

Bean `qou-h0zz` (owner, 2026-11-28: "This might also help fix the sign ambiguity or at least
place it upstream", card pick "Formalize both CS facts").

The Chern–Simons part `CS` of the complex volume `Vol + i·CS` is **orientation-odd**: reversing
the orientation of a 3-manifold negates it, and keeps `Vol`. Here it is an abstract
orientation-odd invariant with values in a linearly ordered additive group `A`. No analytic
value enters. (The true `CS` lives in `ℝ / π²ℤ`, so its sign is taken on a chosen representative;
that choice belongs to the transcendental layer and is not made here.)

## Results

1. `ut_cs_blind`: on the unit tangent bundle `UT(Σ₄)` every isometry of Bring's surface lifts
   with orientation sign `+1` (`lift_orientation_sign`). So an invariant of the lifted
   orientation takes the same value on the lift of the reflection as on the identity.
   `no_hypercharge_from_ut_cs`: no hypercharge read off it can flip as the reflection-odd copy
   requires.
2. `mirror_flips_readout`: on a knot complement, mirroring reverses orientation. If `CS ≠ 0`,
   the readout `Y_K = sign(CS K) · Y` is negated by the mirror, exactly as the reflection acts in
   the reflection-odd copy (`act (-1) 1 true`). The one free bit becomes the mirror choice of
   the knot.
3. `amphichiral_cs_zero`, `amphichiral_readout_zero`: an amphichiral knot (mirror equal to
   itself, e.g. `4₁`) has `CS = 0`, so its readout is `0` and it cannot carry the bit.

So the complex volume does not fix the sign; it places it upstream, in the chirality of the
matter knot's braid word.
-/

namespace QOU.StandardModel.ComplexVolumeSign

open QOU.StandardModel.BringTwist QOU.StandardModel.BringOrientation
  QOU.StandardModel.BraidChiralityBlind

/-- **`CS` on `UT(Σ₄)` cannot see the reflection.** Any invariant of the orientation of the
lifted isometry takes the same value on the lift of an orientation-reversing isometry as on the
lift of an orientation-preserving one. -/
theorem ut_cs_blind {A : Type*} (cs : ℤˣ → A) : cs (liftSign (-1)) = cs (liftSign 1) := by
  rw [lift_orientation_sign, lift_orientation_sign]

/-- **No hypercharge read off `UT(Σ₄)`'s orientation flips under the reflection.** -/
theorem no_hypercharge_from_ut_cs {A : Type*} (cs : ℤˣ → A) (read : A → (Fin 5 → ℚ)) :
    ¬ (read (cs (liftSign 1)) = Y ∧ read (cs (liftSign (-1))) = act (-1) 1 true Y) :=
  no_equivariant_hypercharge_from_UT (fun ε => read (cs ε))

variable {A : Type*} [AddCommGroup A] [LinearOrder A] [IsOrderedAddMonoid A]

/-- Sign of an element of `A` as `-1, 0, 1`. -/
def sgn (a : A) : ℚ := if 0 < a then 1 else if a < 0 then -1 else 0

theorem sgn_neg (a : A) : sgn (-a) = - sgn a := by
  unfold sgn
  rcases lt_trichotomy a 0 with h | h | h
  · have : 0 < -a := neg_pos.mpr h
    simp [this, h, not_lt.mpr h.le]
  · subst h; simp
  · have : -a < 0 := neg_neg_iff_pos.mpr h
    simp [h, this, not_lt.mpr this.le]

/-- A knot's complex-volume sign, mirror-odd: `cs true` is the mirror of `cs false`. -/
structure MirrorOdd (cs : Bool → A) : Prop where
  odd : cs true = - cs false

/-- The hypercharge read off the sign of `CS`. -/
def readout (cs : Bool → A) (m : Bool) : Fin 5 → ℚ := fun i => sgn (cs m) * Y i

/-- **Mirroring the knot negates the readout**, matching the reflection in the reflection-odd
copy. -/
theorem mirror_flips_readout (cs : Bool → A) (h : MirrorOdd cs) :
    readout cs true = act (-1) 1 true (readout cs false) := by
  funext i
  simp only [readout, act_eq, h.odd, sgn_neg]
  simp [twist, readout]

/-- With `CS ≠ 0` the readout of the unmirrored knot is `±Y`, never `0`. -/
theorem readout_ne_zero (cs : Bool → A) (h0 : cs false ≠ 0) :
    readout cs false = Y ∨ readout cs false = -Y := by
  unfold readout sgn
  rcases lt_trichotomy (cs false) 0 with h | h | h
  · right; funext i; simp [h, not_lt.mpr h.le]
  · exact absurd h h0
  · left; funext i; simp [h]

/-- **An amphichiral knot has `CS = 0`.** -/
theorem amphichiral_cs_zero (cs : Bool → A) (h : MirrorOdd cs) (ham : cs true = cs false) :
    cs false = 0 := by
  have h2 : cs false + cs false = 0 := by
    have := h.odd; rw [ham] at this
    rw [← neg_add_cancel (cs false)]; rw [← this]
  rcases lt_trichotomy (cs false) 0 with hl | he | hg
  · have : cs false + cs false < 0 := add_neg hl hl
    rw [h2] at this; exact absurd this (lt_irrefl 0)
  · exact he
  · have : 0 < cs false + cs false := add_pos hg hg
    rw [h2] at this; exact absurd this (lt_irrefl 0)

/-- **An amphichiral knot cannot carry the sign bit.** -/
theorem amphichiral_readout_zero (cs : Bool → A) (h : MirrorOdd cs)
    (ham : cs true = cs false) : readout cs false = 0 := by
  funext i; simp [readout, sgn, amphichiral_cs_zero cs h ham]

end QOU.StandardModel.ComplexVolumeSign
