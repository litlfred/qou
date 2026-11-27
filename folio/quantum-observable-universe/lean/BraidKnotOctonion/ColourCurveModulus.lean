/-
# The colour elliptic fibre's modulus is `z = s - s⁻¹`, and the bar
# involution is not one of its symmetries.

The Descartes colour elliptic curve `ℰ` is presented in
`prop:descartes-elliptic-curve` with `s = √q`, at "spacetime ratio
`z = s - s⁻¹`". Its second Weierstrass coefficient is written there in a
mixture of `q` and `√q`, and factored in `rem:golden-ratio-degeneration`
as a polynomial in `s`. This file records that **both are the same
polynomial in `z`**, and draws the three consequences.

The content is a chain of ring identities plus two sign facts, so it is
stated over a generic `CommRing` wherever possible (AGENTS.md §7c) and
specialised to `ℝ` only for the two statements that need an ordering.

No empirical input. Nothing here depends on the numerical value of `q₀`.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

namespace QOU.BringsSurface.ColourCurveModulus

section Generic

variable {R : Type*} [CommRing R]

/-- The second Weierstrass coefficient of the colour elliptic fibre, as a
polynomial in the spacetime ratio `z`.  This is the form given in
`t-duality-elliptic.md`: `q_W(z) = 5(4z³ + 3z² + 3z + 4)/27`, here cleared
of its denominator so the statement lives over any `CommRing`. -/
def weierstrassR27 (z : R) : R := 5 * (4 * z ^ 3 + 3 * z ^ 2 + 3 * z + 4)

/-- `weierstrassR27` factors as `5(z+1)(4z² - z + 4)`.  The linear factor
is the whole real degeneration locus; see `degenerate_iff` below. -/
theorem weierstrassR27_factor (z : R) :
    weierstrassR27 z = 5 * (z + 1) * (4 * z ^ 2 - z + 4) := by
  unfold weierstrassR27; ring

/-- **The two presentations agree.**  The `s`-polynomial of
`rem:golden-ratio-degeneration` equals `s³` times the `z`-polynomial of
`t-duality-elliptic.md`, once `z` is replaced by `s - s⁻¹`.  Needs a field
(the substitution inverts `s`), so this is the one statement here that is
not over a bare `CommRing`. -/
theorem s_form_eq_z_form {K : Type*} [Field K] (s : K) (hs : s ≠ 0) :
    5 * (s ^ 2 + s - 1) * (4 * s ^ 4 - s ^ 3 - 4 * s ^ 2 + s + 4)
      = s ^ 3 * weierstrassR27 (s - s⁻¹) := by
  unfold weierstrassR27
  field_simp
  ring

/-- `z = s - s⁻¹` is **invariant** under `s ↦ -s⁻¹`. -/
theorem z_invariant_neg_inv (s s' : R) : (-s') - (-s) = s - s' := by ring

/-- `z = s - s⁻¹` is **odd** under `s ↦ s⁻¹`, the sign-preserving lift of
`q ↦ q⁻¹`.  Since `weierstrassR27` is not even (`bar_defect` below), that
lift is *not* a symmetry of the curve. -/
theorem z_odd_inv (s s' : R) : s' - s = -(s - s') := by ring

/-- **The bar defect.**  `q ↦ q⁻¹` sends `z ↦ -z`, and the Weierstrass
coefficient fails to be even by exactly `10 z (4z² + 3)`.  This is the
framework's matter/antimatter asymmetry of the colour fibration, and it is
derived rather than posited. -/
theorem bar_defect (z : R) :
    weierstrassR27 z - weierstrassR27 (-z) = 10 * z * (4 * z ^ 2 + 3) := by
  unfold weierstrassR27; ring

end Generic

section Real

/-- `4z² - z + 4 > 0` for every real `z` (discriminant `1 - 64 = -63 < 0`). -/
theorem quadratic_factor_pos (z : ℝ) : 0 < 4 * z ^ 2 - z + 4 := by
  nlinarith [sq_nonneg (8 * z - 1), sq_nonneg z]

/-- `4z² + 3 > 0` for every real `z`. -/
theorem bar_cofactor_pos (z : ℝ) : 0 < 4 * z ^ 2 + 3 := by positivity

/-- **The degeneration locus is the single point `z = -1`.**  The golden
ratio enters only when this one condition is pulled back along `z = s - s⁻¹`
and `q = s²`, where it acquires the two preimages `q = φ⁻²` and `q = φ²`.
`rem:golden-ratio-degeneration` records only the first. -/
theorem degenerate_iff (z : ℝ) : weierstrassR27 z = 0 ↔ z = -1 := by
  rw [weierstrassR27_factor]
  constructor
  · intro h
    rcases mul_eq_zero.mp h with h' | h'
    · rcases mul_eq_zero.mp h' with h'' | h''
      · norm_num at h''
      · linarith
    · exact absurd h' (ne_of_gt (quadratic_factor_pos z))
  · intro h; subst h; ring

/-- **The bar involution is a symmetry of the colour fibre exactly at
`z = 0`.**  Together with `z = s - s⁻¹`, that is `s = s⁻¹`, i.e. `q = 1`:
the matter and antimatter colour curves coincide only at the interface. -/
theorem bar_symmetric_iff (z : ℝ) :
    weierstrassR27 z = weierstrassR27 (-z) ↔ z = 0 := by
  constructor
  · intro h
    have hd : 10 * z * (4 * z ^ 2 + 3) = 0 := by
      rw [← bar_defect z, h]; ring
    rcases mul_eq_zero.mp hd with h' | h'
    · rcases mul_eq_zero.mp h' with h'' | h''
      · norm_num at h''
      · exact h''
    · exact absurd h' (ne_of_gt (bar_cofactor_pos z))
  · intro h; subst h; norm_num

end Real

end QOU.BringsSurface.ColourCurveModulus
