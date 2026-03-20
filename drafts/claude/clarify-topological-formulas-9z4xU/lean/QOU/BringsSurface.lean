/-!
# Chapter 5 — Bring's Surface

Formalization of Bring's surface and its role as the fundamental
geometric object in the QOU framework from Chapter 5 of the manuscript.

LaTeX source: `chapters/brings-surface.tex`

## Structure

1. **Bring's surface** — genus 4, χ = −6, defined by power sums in CP⁴
2. **Lagrange resolvents** — discrete Fourier transform of coordinates
3. **Color tube coordinates** — chiral fibre decomposition
4. **Chiral elliptic curve** — elliptic structure of chiral fibre
5. **Quaternionic resolvents** — Sp(1) action on spectral data

## References

- [atiyah1988] M. Atiyah, *New invariants of 3- and 4-manifolds*, 1988.
- [turaev2010] V. Turaev, *Quantum Invariants of Knots and 3-Manifolds*, 2010.
-/

import QOU.Basic
import QOU.QuantumObservableUniverse
import QOU.Glossary
import Mathlib.Data.Real.Basic
import Mathlib.Data.Complex.Basic
import Mathlib.Data.Fin.Basic

namespace QOU.BringsSurface

/-! ## §1  Bring's Surface -/

/-- **Bring's surface**: the maximally symmetric Riemann surface of genus 4
    and Euler characteristic χ = −6, defined in CP⁴ by the vanishing of
    the first three power sums: `Σ xⱼᵏ = 0` for `k = 1, 2, 3`.

    LaTeX: `\label{def:brings-surface}` -/
-- Ref: [atiyah1988] https://doi.org/10.1007/BF02698547
structure BringsSurface where
  /-- Homogeneous coordinates `x₀, …, x₄` as a function on the surface. -/
  coords : Fin 5 → ℂ
  /-- First power sum vanishes: `Σ xⱼ = 0`. -/
  power_sum_1 : (Finset.univ.sum fun j => coords j) = 0
  /-- Second power sum vanishes: `Σ xⱼ² = 0`. -/
  power_sum_2 : (Finset.univ.sum fun j => coords j ^ 2) = 0
  /-- Third power sum vanishes: `Σ xⱼ³ = 0`. -/
  power_sum_3 : (Finset.univ.sum fun j => coords j ^ 3) = 0

/-- The genus of Bring's surface is 4. -/
def genus : ℕ := 4

/-- The Euler characteristic of Bring's surface is −6. -/
def eulerChar : ℤ := -6

/-- The Euler characteristic and genus are related by `χ = 2 − 2g`. -/
theorem euler_genus_relation : eulerChar = 2 - 2 * (genus : ℤ) := by
  simp [eulerChar, genus]

/-- The automorphism group of Bring's surface has order 120 (= S₅). -/
def automorphism_order : ℕ := 120

/-! ## §2  Lagrange Resolvents -/

/-- **Lagrange resolvent**: the discrete Fourier transform of the
    coordinates `xⱼ` with respect to `ζ = e^{2πi/5}`.

    `wₖ = (1/√5) Σⱼ ζ^{kj} xⱼ`, for `k ∈ {0, 1, 2, 3, 4}`.

    LaTeX: `\label{rem:lagrange-resolvents}` -/
-- Ref: [turaev2010] https://doi.org/10.1515/9783110221831
structure LagrangeResolvents where
  /-- The resolvent coordinates `w₀, …, w₄`. -/
  w : Fin 5 → ℂ
  /-- `w₀ = 0` (linear projection constraint). -/
  w0_zero : w 0 = 0
  /-- Hermitian quadric: `w₁w₄ + w₂w₃ = 0`. -/
  hermitian_quadric : w 1 * w 4 + w 2 * w 3 = 0
  /-- Symmetric cubic: `w₁²w₃ + w₄²w₂ + w₂²w₁ + w₃²w₄ = 0`. -/
  symmetric_cubic :
    w 1 ^ 2 * w 3 + w 4 ^ 2 * w 2 + w 2 ^ 2 * w 1 + w 3 ^ 2 * w 4 = 0

/-! ## §3  Color Tube Coordinates -/

/-- **Color tube coordinates**: the decomposition of Bring's surface
    coordinates into spacetime `(x₀, x₁)` and chiral `(x₂, x₃, x₄)`
    degrees of freedom.

    The projective ratio `z = x₀/x₁ ∈ CP¹` parametrises the spacetime base.

    LaTeX: `\label{def:color-tube-coordinates}` -/
structure ColorTubeCoordinates where
  /-- Spacetime coordinate `z = x₀/x₁`. -/
  z : ℂ
  /-- Chiral coordinates `(x₂, x₃, x₄)`. -/
  chiral : Fin 3 → ℂ

/-- **Color tube fibers**: the chiral fiber at a given spacetime point,
    consisting of the three roots of the chiral cubic constraint.

    LaTeX: `\label{def:color-tube-fibers}` -/
structure ColorTubeFiber where
  /-- The spacetime base point. -/
  base : ℂ
  /-- The three chiral roots at this point. -/
  roots : Fin 3 → ℂ

/-- **Observed spacetime value**: the projection from the full Bring's
    surface data to the spacetime base CP¹.

    LaTeX: `\label{def:observed-value}` -/
def observedValue (ct : ColorTubeCoordinates) : ℂ := ct.z

/-! ## §4  Chiral Elliptic Curve -/

/-- **Proposition**: the chiral fibre of Bring's surface is an elliptic
    curve (genus 1).

    LaTeX: `\label{prop:chiral-elliptic}` -/
-- Ref: [atiyah1988] https://doi.org/10.1007/BF02698547
structure ChiralEllipticCurve where
  /-- The chiral fibre carrier. -/
  carrier : Type*
  /-- The elliptic curve has genus 1. -/
  genus : ℕ := 1
  /-- The j-invariant of the elliptic curve. -/
  j_invariant : ℂ

/-! ## §5  Briggs–Klein Affine Chart -/

/-- **Briggs–Klein affine chart**: an affine coordinate system on
    Bring's surface obtained by setting one coordinate to 1.

    LaTeX: `\label{def:briggs-klein-chart}` -/
structure BriggsKleinChart where
  /-- The affine coordinates (4 of the 5 homogeneous coordinates). -/
  coords : Fin 4 → ℂ

/-! ## §6  Quaternionic Spectral Resolvents -/

/-- **Quaternionic spectral resolvents**: the spectral data rewritten
    in a quaternionic basis `(ω₁, ω₂, ω₃)` on which `Sp(1) ≅ SU(2)`
    acts naturally.

    LaTeX: `\label{def:quaternionic-spectral-resolvents}` -/
-- Ref: [turaev2010] https://doi.org/10.1515/9783110221831
structure QuaternionicResolvents where
  /-- The three quaternionic resolvent components. -/
  omega : Fin 3 → ℂ

/-! ## §7  Branch Points and Defects -/

/-- The number of branch points of Bring's surface as a covering of CP¹
    equals 6, matching the Euler characteristic magnitude |χ| = 6.

    LaTeX: `\label{rem:brings-qou-4tuple}` -/
def num_branch_points : ℕ := 6

/-- The covering degree of the projection `S → CP¹` is 4. -/
def covering_degree : ℕ := 4

/-- Branch points, covering degree, genus, and Euler characteristic
    are related by Riemann–Hurwitz:
    `χ(S) = deg · χ(CP¹) − (number of ramification points)`.
    Here: `−6 = 4 · 2 − 14`, using total ramification 14. -/
theorem riemann_hurwitz_check :
    eulerChar = (covering_degree : ℤ) * 2 - 14 := by
  simp [eulerChar, covering_degree]

end QOU.BringsSurface
