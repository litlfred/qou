import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

/-!
# QOU.Mass.ColorSpectralCubicGeometry — branch geometry of the color spectral cubic

The color (formerly "coral") spectral curve of the Lever-1 binding kernel is the
cubic in the color coordinate `X`, over the spacetime ratio `z = √q − 1/√q`:

  `C_z(X) := X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)`        (color-spectral-cubic)

with Seiberg–Witten differential `λ_SW = X dz`. Its ramification (branch) points
in `z` — where two color sheets collide — are the zeros of the `X`-discriminant
`disc_X C_z`. They are the locations of the exceptional divisors `S_c` over which
the abelianised Cartan connection (`mi-sw-abelianisation-cartan`) and the
jet-prolongation `λ_SW^(n)` live, so the branch locus is the geometric substrate
of the prolongation residues.

This file formalises the (a)-baseline geometry that the Lever-1 first probe
(`lever1_color_sigma_geometry_probe.py`, PR #2755) established numerically:
the closed form of `disc_X C_z` and its palindromic `z ↦ 1/z` symmetry.

**Companion to** `QOU.Mass.ColorCubicPowerSums` (the color-root power sums
`p_n = −(zⁿ+1)`), which records that the spectral data is **q-free** — forcing
the binding prolongation to be a **q-difference** operator (z2bn second probe).
This file adds the orthogonal datum: the **branch locus** (discriminant + its
`z ↦ 1/z` symmetry), where the exceptional divisors `S_c` and the prolongation
residues sit.

**Scope.** A SUPPORTING brick for the #1765 prolongation identity
`a_D^(n) = ∮ λ_SW^(n) = lw(n−1)`. It does **not** construct the prolongation
operator itself (the owner-gated, multi-session keystone — the abelianised
`λ_SW` holonomy / the q-difference kernel `R(q,x)`); it only certifies the curve
geometry beneath it. The bare differential's residue route is already pinned
negative (`Res(X dz)=0` at every finite branch point, PR #2755); the open core
is the explicit `λ_SW^(n)` on `S_c`, not this geometry.

Ground ring `ℝ` (substrate-anchor regime; the identities are q-rational at the
fibre level). AGENTS.md §7c: pure field algebra, closed by `ring` / `field_simp`.
-/

namespace QOU.Mass.ColorSpectralCubicGeometry

/-- The **branch-locus sextic** `D(z) := 16z⁶+24z⁵+35z⁴+50z³+35z²+24z+16`
(`= −disc_X C_z`). Its six zeros are the ramification points of the color
spectral curve — the bases of the exceptional divisors `S_c`. -/
def branchSextic (z : ℝ) : ℝ :=
  16 * z ^ 6 + 24 * z ^ 5 + 35 * z ^ 4 + 50 * z ^ 3 + 35 * z ^ 2 + 24 * z + 16

/-- **Discriminant of the color spectral cubic.** For
`C_z(X) = X³ + bX² + cX + d` with `b = z+1`, `c = z²+z+1`, `d = z³+z²+z+1`, the
monic-cubic discriminant `b²c² − 4c³ − 4b³d + 18bcd − 27d²` equals the negative
branch-locus sextic `−branchSextic z` (cross-checked against `sympy.discriminant`). -/
theorem color_cubic_discriminant (z : ℝ) :
    (z ^ 2 + z + 1) ^ 2 * (z + 1) ^ 2 - 4 * (z ^ 2 + z + 1) ^ 3
        - 4 * (z + 1) ^ 3 * (z ^ 3 + z ^ 2 + z + 1)
        + 18 * (z + 1) * (z ^ 2 + z + 1) * (z ^ 3 + z ^ 2 + z + 1)
        - 27 * (z ^ 3 + z ^ 2 + z + 1) ^ 2
      = -branchSextic z := by
  unfold branchSextic
  ring

/-- **Palindromic symmetry of the branch locus.** `D` is palindromic, i.e.
`z⁶ · D(1/z) = D(z)`: the six ramification points are stable under `z ↦ 1/z`
(coefficients `[16,24,35,50,35,24,16]` read the same both ways). The reciprocal
symmetry of the branch locus is a constraint any prolongation residue sum on the
`S_c` must respect. -/
theorem branchSextic_palindromic (z : ℝ) (hz : z ≠ 0) :
    z ^ 6 * branchSextic z⁻¹ = branchSextic z := by
  unfold branchSextic
  field_simp
  ring

end QOU.Mass.ColorSpectralCubicGeometry
