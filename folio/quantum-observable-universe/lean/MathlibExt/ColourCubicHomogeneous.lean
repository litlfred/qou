import MathlibExt.ColourCubicDiscriminant
import Mathlib.Tactic

/-!
# The colour cubic in homogeneous coordinates

Chip on `conj:hecke-monodromy-step-two` (`QOU.Mass.HeckeMonodromy`). The colour cubic
`P(X, z) = X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)` is studied in the probes on the affine
`z`-line, where the loop around `z = ∞` shows up as a separate object (the full twist `Δ²`,
`computations/probes/colour_cubic_braid_monodromy_probe.py`). This file puts the cubic in
homogeneous coordinates `[X : z : w]` and records what that makes visible, all as generic ring
identities:

* `colourCubicHom_eq_completeHom` — the homogenised cubic is the **complete homogeneous
  symmetric polynomial** `h₃(X, z, w) = Σ_{a+b+c=3} X^a z^b w^c`. So it is symmetric under
  **all** of `S₃` acting on `(X, z, w)`, not just under `z ↔ w`
  (`colourCubicHom_swap_zw`, `colourCubicHom_swap_Xz`).
* `colourCubicHom_dehom` — setting `w = 1` gives back the affine `P(X, z)`.
* `colourCubicHom_vandermonde` — the divided-difference form
  `(X−z)(X−w)(z−w)·h₃ = X⁵(z−w) − z⁵(X−w) + w⁵(X−z)`.
* `colourCubicHom_at_infinity` — at `w = 0` (the point `z = ∞` of the affine chart),
  `(X − z)·h₃(X, z, 0) = X⁴ − z⁴`: the three roots are `−z, ±iz`, the roots of `X³+X²z+Xz²+z³`.
* `colourCubicHom_smul` — homogeneity `h₃(tX, tz, tw) = t³ h₃(X, z, w)`, so the root set over
  `[tz : tw]` is `t` times the root set over `[z : w]`: the fibre coordinate `X` is a section of
  `O(1)`. This is the algebraic content behind reading the affine "loop at infinity = Δ²" as the
  winding of `O(1)`; the topological braid statement itself is NOT proved here (it rests on the
  probe).
* `colourDiscriminantHom_eq_disc` — the `X`-discriminant of the monic cubic, from the standard
  formula `a²b² − 4b³ − 4a³c − 27c² + 18abc`, equals `−D(z, w)` with
  `D(z, w) = 16z⁶ + 24z⁵w + 35z⁴w² + 50z³w³ + 35z²w⁴ + 24zw⁵ + 16w⁶`.
* `colourDiscriminantHom_swap` and `colourDiscriminantHom_dehom` — `D` is symmetric in `z ↔ w`
  (this is the reciprocity `z⁶D(1/z) = D(z)` of `ColourCubicDiscriminant`, now without a division),
  and `D(z, 1)` is the affine sextic.
* `colourDiscriminantHom_infinity` — `D(z, 0) = 16 z⁶`, so the point at infinity `[1 : 0]` is
  **not** a branch point (over any ring where `16` and `z` are nonzero divisors, e.g. a field of
  characteristic 0).

Base ring §7c: everything is a `CommRing` identity except the last corollary (`Field`, `CharZero`).

-- Ref: [leitner2026] computations/probes/colour_cubic_braid_monodromy_probe.py
-- Ref: [leitner2026] folio/quantum-observable-universe/mass-theory/hecke-monodromy-step-two.md
-/

namespace QOU.Mass.ColourCubicHomogeneous

section Generic

variable {R : Type*} [CommRing R]

/-- The affine colour cubic `P(X, z)`. -/
def colourCubic (X z : R) : R :=
  X ^ 3 + (z + 1) * X ^ 2 + (z ^ 2 + z + 1) * X + (z ^ 3 + z ^ 2 + z + 1)

/-- The homogenised colour cubic on `[X : z : w]`. -/
def colourCubicHom (X z w : R) : R :=
  X ^ 3 + (z + w) * X ^ 2 + (z ^ 2 + z * w + w ^ 2) * X + (z ^ 3 + z ^ 2 * w + z * w ^ 2 + w ^ 3)

/-- **The colour cubic is `h₃`.** The homogenised cubic is the complete homogeneous symmetric
polynomial of degree 3 in `X, z, w`. -/
theorem colourCubicHom_eq_completeHom (X z w : R) :
    colourCubicHom X z w =
      X ^ 3 + z ^ 3 + w ^ 3 + X ^ 2 * z + X ^ 2 * w + z ^ 2 * X + z ^ 2 * w + w ^ 2 * X
        + w ^ 2 * z + X * z * w := by
  unfold colourCubicHom; ring

/-- Dehomogenising at `w = 1` gives the affine cubic. -/
theorem colourCubicHom_dehom (X z : R) : colourCubicHom X z 1 = colourCubic X z := by
  unfold colourCubicHom colourCubic; ring

/-- Symmetry `z ↔ w` (hidden in the affine chart as `z ↦ 1/z`). -/
theorem colourCubicHom_swap_zw (X z w : R) : colourCubicHom X w z = colourCubicHom X z w := by
  unfold colourCubicHom; ring

/-- Symmetry `X ↔ z`: together with `z ↔ w` this generates all of `S₃` on `(X, z, w)`. -/
theorem colourCubicHom_swap_Xz (X z w : R) : colourCubicHom z X w = colourCubicHom X z w := by
  unfold colourCubicHom; ring

/-- Divided-difference (Vandermonde) form of `h₃`. -/
theorem colourCubicHom_vandermonde (X z w : R) :
    (X - z) * (X - w) * (z - w) * colourCubicHom X z w =
      X ^ 5 * (z - w) - z ^ 5 * (X - w) + w ^ 5 * (X - z) := by
  unfold colourCubicHom; ring

/-- At infinity (`w = 0`): `(X − z)·h₃(X, z, 0) = X⁴ − z⁴`. -/
theorem colourCubicHom_at_infinity (X z : R) :
    (X - z) * colourCubicHom X z 0 = X ^ 4 - z ^ 4 := by
  unfold colourCubicHom; ring

/-- Homogeneity of degree 3. -/
theorem colourCubicHom_smul (t X z w : R) :
    colourCubicHom (t * X) (t * z) (t * w) = t ^ 3 * colourCubicHom X z w := by
  unfold colourCubicHom; ring

/-- Roots scale with the base point: `X` is a section of `O(1)`. -/
theorem colourCubicHom_root_smul {t X z w : R} (h : colourCubicHom X z w = 0) :
    colourCubicHom (t * X) (t * z) (t * w) = 0 := by
  rw [colourCubicHom_smul, h, mul_zero]

/-- On the fixed line `z = w` of the swap `z ↔ w`, the cubic is `X³ + 2zX² + 3z²X + 4z³`. -/
theorem colourCubicHom_diag (X z : R) :
    colourCubicHom X z z = X ^ 3 + 2 * z * X ^ 2 + 3 * z ^ 2 * X + 4 * z ^ 3 := by
  unfold colourCubicHom; ring

/-- The isolated fixed point `[0 : 1 : −1]` of the swap lies on the curve. -/
theorem colourCubicHom_antidiag_zero : colourCubicHom (0 : R) 1 (-1) = 0 := by
  unfold colourCubicHom; ring

/-- The homogenised discriminant sextic `D(z, w)`. -/
def colourDiscriminantHom (z w : R) : R :=
  16 * z ^ 6 + 24 * z ^ 5 * w + 35 * z ^ 4 * w ^ 2 + 50 * z ^ 3 * w ^ 3 + 35 * z ^ 2 * w ^ 4
    + 24 * z * w ^ 5 + 16 * w ^ 6

/-- **The discriminant.** For the monic cubic `X³ + aX² + bX + c` with the coefficients of
`h₃(X, z, w)`, the discriminant `a²b² − 4b³ − 4a³c − 27c² + 18abc` equals `−D(z, w)`. -/
theorem colourDiscriminantHom_eq_disc (z w : R) :
    let a := z + w
    let b := z ^ 2 + z * w + w ^ 2
    let c := z ^ 3 + z ^ 2 * w + z * w ^ 2 + w ^ 3
    a ^ 2 * b ^ 2 - 4 * b ^ 3 - 4 * a ^ 3 * c - 27 * c ^ 2 + 18 * a * b * c
      = - colourDiscriminantHom z w := by
  simp only []
  unfold colourDiscriminantHom; ring

/-- `D` is symmetric under `z ↔ w`. -/
theorem colourDiscriminantHom_swap (z w : R) :
    colourDiscriminantHom w z = colourDiscriminantHom z w := by
  unfold colourDiscriminantHom; ring

/-- Dehomogenising at `w = 1` gives the affine sextic of `ColourCubicDiscriminant`. -/
theorem colourDiscriminantHom_dehom (z : R) :
    colourDiscriminantHom z 1 = QOU.Mass.ColourCubicDiscriminant.colourDiscriminant z := by
  unfold colourDiscriminantHom QOU.Mass.ColourCubicDiscriminant.colourDiscriminant; ring

/-- At infinity, `D(z, 0) = 16 z⁶`. -/
theorem colourDiscriminantHom_infinity (z : R) : colourDiscriminantHom z 0 = 16 * z ^ 6 := by
  unfold colourDiscriminantHom; ring

/-- Homogeneity of degree 6. -/
theorem colourDiscriminantHom_smul (t z w : R) :
    colourDiscriminantHom (t * z) (t * w) = t ^ 6 * colourDiscriminantHom z w := by
  unfold colourDiscriminantHom; ring

end Generic

section Field

variable {K : Type*} [Field K] [CharZero K]

/-- **Infinity is not a branch point.** Over a field of characteristic 0, the point
`[z : 0]` with `z ≠ 0` (the affine `z = ∞`) is not a root of `D`. -/
theorem infinity_not_branch_point {z : K} (hz : z ≠ 0) : colourDiscriminantHom z 0 ≠ 0 := by
  rw [colourDiscriminantHom_infinity]
  exact mul_ne_zero (by norm_num) (pow_ne_zero 6 hz)

end Field

end QOU.Mass.ColourCubicHomogeneous
