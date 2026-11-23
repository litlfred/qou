import Mathlib.Tactic
import Mathlib.Data.Complex.Basic

/-!
# Elliptic stability locus (conjectural)

Class-axiomatized stub for `rem:elliptic-stability-locus`: the
nuclear degeneracy locus (valley of stability in (Z, N) integer
lattice) is the integer-point set of an elliptic curve over
Bring's surface. The Coulomb and pairing terms in the
liquid-drop ansatz reduce to a Weierstrass elliptic curve whose
integer points trace the valley.

-- Ref: [leitner2026]
Per `AGENTS.md §3b-cond`, opaque Props + class fields + sorry
instance per claim. Algebraic tier only — the numerical match
to the observed stable-isotope set belongs to a future
Archimedean tier (per gemini review on #721).

## References

- `[leitner2026]` `rem:elliptic-stability-locus`
- `[leitner2026]` `prop:integer-stability`
- `[leitner2026]` `def:color-tube-fibers`
-/

namespace QOU.EllipticStabilityLocus

/-- **Algebraic claim (Weierstrass form)**: the (Coulomb +
    pairing) part of the nuclear binding ansatz, after rescaling
    by m_e, reduces to a Weierstrass elliptic curve over the
    color-tube fibration of Bring's surface (`def:color-tube-fibers`). -/
opaque WeierstrassFormHolds : Prop

/-- **Algebraic claim (integer-point identification)**: the
    valley of stability in `(Z, N)` integer lattice coincides
    with the integer points of the Weierstrass curve above. -/
opaque IntegerPointIdentificationHolds : Prop

/-- **Elliptic-stability-locus conjecture** (class-axiomatized per §3b-cond). -/
class EllipticStabilityLocus : Prop where
  weierstrass_form : WeierstrassFormHolds
  integer_point_identification : IntegerPointIdentificationHolds

-- **No instance is provided — that is the honest open state** (AGENTS.md
-- §3b-tax).  An instance would have to supply the field(s) below, which is
-- exactly the open conjecture; supplying one asserts the conjecture.
--
-- History: this file previously carried
--     instance elliptic_stability_locus_conjecture : EllipticStabilityLocus where
--     axiom elliptic_stability_locus_weierstrass_form : WeierstrassFormHolds
--     axiom elliptic_stability_locus_integer_point_identification : IntegerPointIdentificationHolds
-- i.e. the conjecture was discharged by `axiom` and installed as a global
-- instance, so every downstream `[EllipticStabilityLocus]` resolved for free and the
-- assumption was invisible outside `#print axioms`.  Removed, not completed.
-- Downstream results must take `[EllipticStabilityLocus]` as an explicit hypothesis.

/-! ## Affine obstruction (proved)

After removing the quadratic term, a monic cubic is `Y³ + P·Y + Q`, and a
change of variable `X ↦ αX + β` sends `(P, Q) ↦ (α²P, α³Q)`. The ratio
`J = 4P³/(4P³ + 27Q²)` is therefore invariant. For the color cubic (C) at real
`z` it is positive; for the stability cubic (S) at real `p ≠ 0`, `c > 0` it is
negative. So no such change of variable carries (S) to (C) at real `z`.
This is a theorem, independent of the conjecture class below. -/

/-- Affine-invariance of the cubic invariant. If `P' = α² P` and `Q' = α³ Q`, then
`4P'³ · (4P³ + 27Q²) = 4P³ · (4P'³ + 27Q'²)`, i.e. `J = 4P³/(4P³+27Q²)` is unchanged. -/
theorem cubicInvariant_scale {R : Type*} [CommRing R] (P Q α : R) :
    4 * (α ^ 2 * P) ^ 3 * (4 * P ^ 3 + 27 * Q ^ 2)
      = 4 * P ^ 3 * (4 * (α ^ 2 * P) ^ 3 + 27 * (α ^ 3 * Q) ^ 2) := by
  ring

/-- Depressed linear coefficient of the color elliptic cubic (C). -/
def colorP {R : Type*} [Field R] (z : R) : R := (2 * z ^ 2 + z + 2) / 3
/-- Depressed constant coefficient of the color elliptic cubic (C). -/
def colorQ {R : Type*} [Field R] (z : R) : R := 5 * (z + 1) * (4 * z ^ 2 - z + 4) / 27
/-- Depressed linear coefficient of the stability cubic (S). -/
def stabP {R : Type*} [Field R] (c p : R) : R := -(c ^ 2 * p ^ 2) / 3
/-- Depressed constant coefficient of the stability cubic (S). -/
def stabQ {R : Type*} [Field R] (c p : R) : R := -(2 * p * (c ^ 3 * p ^ 2 + 27)) / 27

@[norm_cast] theorem colorP_ofReal (z : ℝ) : ((colorP z : ℝ) : ℂ) = colorP (z : ℂ) := by
  unfold colorP; push_cast; ring
@[norm_cast] theorem colorQ_ofReal (z : ℝ) : ((colorQ z : ℝ) : ℂ) = colorQ (z : ℂ) := by
  unfold colorQ; push_cast; ring
@[norm_cast] theorem stabP_ofReal (c p : ℝ) : ((stabP c p : ℝ) : ℂ) = stabP (c : ℂ) (p : ℂ) := by
  unfold stabP; push_cast; ring
@[norm_cast] theorem stabQ_ofReal (c p : ℝ) : ((stabQ c p : ℝ) : ℂ) = stabQ (c : ℂ) (p : ℂ) := by
  unfold stabQ; push_cast; ring

theorem colorP_pos (z : ℝ) : 0 < colorP z := by
  unfold colorP; nlinarith [sq_nonneg (z + 1 / 4)]

theorem color_disc_pos (z : ℝ) : 0 < 4 * colorP z ^ 3 + 27 * colorQ z ^ 2 := by
  have h := colorP_pos z
  have : 0 < colorP z ^ 3 := by positivity
  nlinarith [sq_nonneg (colorQ z)]

theorem stabP_neg (c p : ℝ) (hc : c ≠ 0) (hp : p ≠ 0) : stabP c p < 0 := by
  unfold stabP
  have : 0 < c ^ 2 * p ^ 2 := by positivity
  linarith

theorem stab_disc_pos (c p : ℝ) (hc : 0 < c) (hp : p ≠ 0) :
    0 < 4 * stabP c p ^ 3 + 27 * stabQ c p ^ 2 := by
  have e : 4 * stabP c p ^ 3 + 27 * stabQ c p ^ 2
      = 4 * p ^ 2 * (54 * c ^ 3 * p ^ 2 + 729) / 27 := by
    unfold stabP stabQ; ring
  rw [e]
  have : 0 < p ^ 2 := by positivity
  have : 0 < c ^ 3 := by positivity
  positivity

/-- **Affine obstruction.** For real `z`, real `p ≠ 0` and `c > 0`, no complex `α`
scales the depressed color cubic onto the depressed stability cubic
(`P_C = α² P_S`, `Q_C = α³ Q_S`): the invariant `J` is positive for (C) and
negative for (S). -/
theorem no_affine_match (z c p : ℝ) (hc : 0 < c) (hp : p ≠ 0) (α : ℂ) :
    ¬ ((colorP z : ℂ) = α ^ 2 * (stabP c p : ℂ) ∧ (colorQ z : ℂ) = α ^ 3 * (stabQ c p : ℂ)) := by
  rintro ⟨h1, h2⟩
  have key := cubicInvariant_scale (stabP c p : ℂ) (stabQ c p : ℂ) α
  rw [← h1, ← h2] at key
  have hreal : 4 * colorP z ^ 3 * (4 * stabP c p ^ 3 + 27 * stabQ c p ^ 2)
      = 4 * stabP c p ^ 3 * (4 * colorP z ^ 3 + 27 * colorQ z ^ 2) := by
    exact_mod_cast key
  have a := colorP_pos z
  have b := color_disc_pos z
  have d := stabP_neg c p hc.ne' hp
  have e := stab_disc_pos c p hc hp
  have l : 0 < 4 * colorP z ^ 3 * (4 * stabP c p ^ 3 + 27 * stabQ c p ^ 2) := by positivity
  have r : 4 * stabP c p ^ 3 * (4 * colorP z ^ 3 + 27 * colorQ z ^ 2) < 0 := by
    have : stabP c p ^ 3 < 0 := Odd.pow_neg (by decide) d
    nlinarith
  linarith

end QOU.EllipticStabilityLocus
