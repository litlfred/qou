import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# Colour-cubic discriminant: palindromic + strictly positive on ℝ

Companion to `QOU.Mass.ColorCubicNoBranch` (irreducibility route) and
`QOU.Mass.ColorCurveQIntegerForm` (q-integer coefficient form). Here we record
the **explicit** discriminant of the trefoil colour cubic

  `C(X;z) = X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)`
         `= [1]_z X³ + [2]_z X² + [3]_z X + [4]_z`   (the q-integer cubic),

which a symbolic computation (`sympy.discriminant`) gives as

  `Δ(z) = -(16z⁶ + 24z⁵ + 35z⁴ + 50z³ + 35z² + 24z + 16)`,

a sextic ⇒ the colour channel has exactly **6 branch points** (= the 6 saddle
points of Bring's surface). We prove two structural facts about the sextic
`P(z) := -Δ(z)`:

* `discSextic_palindromic` — **palindromic / reciprocal**: over a field, for
  `z ≠ 0`, `z⁶ · P(z⁻¹) = P(z)`. This is the `q ↦ q⁻¹` bar-symmetry of the
  colour channel, at the level of the branch locus.
* `discSextic_pos` — **strictly positive on ℝ**: `0 < P(z)` for every real `z`,
  via an exact SOS certificate. Hence `Δ(z) < 0` for all real `z`
  (`colorCubicDiscriminant_neg`): the colour cubic has **no real branch point**,
  i.e. all 6 saddle points are strictly off the real spacetime axis. The
  saddle-point orbit is genuinely complex — so a torus-knot offset relative to
  it has a nonzero angle by construction.

The SOS certificate (from an exact PSD Gram of the sextic):
`P = (1/400)(80z³+60z²+2z+17)² + c₁(504z²+426z−43)² + c₂(4386z+3721)² + D₃`
with `c₁, c₂, D₃ > 0` — the three squares are the `nlinarith` hints below.

§7c: `discSextic` and the palindromic functional equation are stated over a
generic `CommRing` / `Field`; positivity is an archimedean (`ℝ`) statement.

Bean `qou-vhv6` (well-posed torus-knot → q-Bring offset). Derived, not fitted:
the discriminant is computed from the corpus colour cubic and the SOS is a
machine-verifiable certificate. The identity `Δ(z) = disc_X C(X;z)` itself is
symbolic-exact (`sympy`), not re-proved in Lean here — `discSextic` is the
recorded result whose properties this file certifies.
-/

namespace QOU.Mass

/-- The trefoil colour-cubic discriminant sextic `P(z) = -Δ(z)`, where
`Δ(z) = disc_X (X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1))` (symbolic-exact). -/
def discSextic {R : Type*} [CommRing R] (z : R) : R :=
  16 * z ^ 6 + 24 * z ^ 5 + 35 * z ^ 4 + 50 * z ^ 3 + 35 * z ^ 2 + 24 * z + 16

/-- **Palindromic / reciprocal** (`q ↦ q⁻¹` bar-symmetry of the branch locus):
over a field, for `z ≠ 0`, `z⁶ · P(z⁻¹) = P(z)`. -/
theorem discSextic_palindromic {K : Type*} [Field K] (z : K) (hz : z ≠ 0) :
    z ^ 6 * discSextic z⁻¹ = discSextic z := by
  unfold discSextic
  field_simp
  ring

/-- **Strict positivity on ℝ** (exact SOS certificate): `0 < P(z)` for all real
`z`. The three `sq_nonneg` hints are the SOS squares. -/
theorem discSextic_pos (z : ℝ) : 0 < discSextic z := by
  unfold discSextic
  nlinarith [sq_nonneg (80 * z ^ 3 + 60 * z ^ 2 + 2 * z + 17),
             sq_nonneg (504 * z ^ 2 + 426 * z - 43),
             sq_nonneg (4386 * z + 3721),
             sq_nonneg z, sq_nonneg (z ^ 3), sq_nonneg (z ^ 2)]

/-- The colour-cubic discriminant `Δ(z) = -P(z)` (symbolic-exact result). -/
def colorCubicDiscriminant (z : ℝ) : ℝ := -discSextic z

/-- **No real branch point**: `Δ(z) < 0` for all real `z`. Consequently the
trefoil colour cubic has no real saddle — all 6 branch points are strictly off
the real spacetime axis, so the saddle-point orbit is genuinely complex. -/
theorem colorCubicDiscriminant_neg (z : ℝ) : colorCubicDiscriminant z < 0 := by
  unfold colorCubicDiscriminant
  simpa using discSextic_pos z

end QOU.Mass
