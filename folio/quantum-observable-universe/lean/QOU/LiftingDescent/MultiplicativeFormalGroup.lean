import QOU.LiftingDescent.FormalGroupLaw

/-!
# The multiplicative formal group law `Ĝ_m`

`F(X, Y) = X + Y + XY` over any commutative ring. In the coordinate `t = q − 1` this is the
multiplication of `q`: `(1 + X)(1 + Y) = 1 + F(X, Y)`. It is the first coordinate of the
two-dimensional `affine` law of `FormalGroupLaw.lean`, and it is commutative.

Why it is here: the energy reading `U = −q ∂_q log m` is the logarithmic derivative along
`q ∂_q`, the invariant vector field of `G_m`, and the `(q − 1)`-adic tower of readings is the
formal completion of `G_m` at `q = 1`. `QOU.MassTheory.EnergyReadingTangent` uses the
first-order part of that statement to make the energy reading algebraic.

* `multiplicative`: the law, sorry-free.
* `multiplicative_isComm`.
* `one_add_mul_one_add`: `(1 + X)(1 + Y) = 1 + F(X, Y)`, i.e. `F` is the law of `q = 1 + t`.

-- Ref: [fred2005]
-/

namespace QOU.FormalGroups

open MvPowerSeries

noncomputable section

variable {R : Type*} [CommRing R]

/-- `F(X, Y) = X + Y + XY` in the one-dimensional variables `Fin 2 × Unit`. -/
def multiplicativeF (_ : Unit) : MvPowerSeries (Fin 2 × Unit) R :=
  X (0, ()) + X (1, ()) + X (0, ()) * X (1, ())

lemma subst2_multiplicativeF {τ : Type*} {a b : Unit → MvPowerSeries τ R} (ha : NoConst a)
    (hb : NoConst b) (j : Unit) :
    subst2 a b (multiplicativeF j) = a () + b () + a () * b () := by
  unfold multiplicativeF
  rw [subst2_add ha hb, subst2_add ha hb, subst2_mul ha hb]
  simp only [subst2_X ha hb]
  rfl

/-- **The multiplicative formal group law `Ĝ_m`.** -/
def multiplicative : FormalGroupLaw R Unit where
  F := multiplicativeF
  noConst j := by simp [multiplicativeF]
  unit_left := by
    funext j
    rw [subst2_multiplicativeF (noConst_coords 0) noConst_zero]
    simp [coords]
  unit_right := by
    funext j
    rw [subst2_multiplicativeF noConst_zero (noConst_coords 0)]
    simp [coords]
  assoc := by
    have nab : NoConst (fun i => subst2 (coords (R := R) (m := 3) 0) (coords 1)
        (multiplicativeF i)) :=
      noConst_subst2 (noConst_coords 0) (noConst_coords 1) (fun _ => by simp [multiplicativeF])
    have nbc : NoConst (fun i => subst2 (coords (R := R) (m := 3) 1) (coords 2)
        (multiplicativeF i)) :=
      noConst_subst2 (noConst_coords 1) (noConst_coords 2) (fun _ => by simp [multiplicativeF])
    funext j
    rw [subst2_multiplicativeF nab (noConst_coords 2), subst2_multiplicativeF (noConst_coords 0) nbc]
    simp only [subst2_multiplicativeF (noConst_coords _) (noConst_coords _)]
    ring

theorem multiplicative_isComm : (multiplicative (R := R)).IsComm := by
  intro j
  show subst2 (coords 1) (coords 0) (multiplicativeF j) = multiplicativeF j
  rw [subst2_multiplicativeF (noConst_coords 1) (noConst_coords 0)]
  simp [coords, multiplicativeF]
  ring

/-- **`F` is the group law of `q = 1 + t`:** `(1 + X)(1 + Y) = 1 + F(X, Y)`. -/
theorem one_add_mul_one_add (j : Unit) :
    (1 + X (0, ()) : MvPowerSeries (Fin 2 × Unit) R) * (1 + X (1, ())) =
      1 + (multiplicative (R := R)).F j := by
  show _ = 1 + multiplicativeF j
  unfold multiplicativeF
  ring

end

end QOU.FormalGroups
