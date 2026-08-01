import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring

/-!
# QOU.Mass.ColorTubeSpectralBridge — the tube ↔ spectral coordinate change

The color cubic is carried in the corpus in **two coordinate systems**, and until
now the change of variable between them lived only in `.md` prose:

* **Spectral coordinate `X`** (the canonical one; `QOU.Mass.ColorSpectralCubicGeometry`,
  `QOU.Mass.ColorCubicPowerSums`):

    `C_z(X) = X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)`

  Its elementary symmetric data `e₁ = −(z+1)`, `e₂ = z²+z+1`, `e₃ = −(z³+z²+z+1)`
  is the **q-free** spectral datum (the z2bn power-sum result).

* **Tube coordinate `c`** (the shifted one; the `color-tube-cubic` /
  `color-tube-constraints` content blocks):

    `T_z(c) = c³ + (4z+1)c² + (6z²+3z+1)c + (4z³+3z²+2z+1)`

  with the block-level Vieta relations `Σcᵢ = −(4z+1)`, `Σ_{i<j}cᵢcⱼ = 6z²+3z+1`,
  `∏cᵢ = −(4z³+3z²+2z+1)`.

The `color-tube-cubic` block states that `T_z` is obtained from `C_z` by the
substitution `X = c + z` — i.e. the tube roots are the spectral roots shifted,
`cᵢ = wᵢ − z`. That claim was **prose-only**; this file discharges it and the
three induced Vieta transports, sorry-free.

**Why it matters.** The spectral coordinate is the canonical one (its symmetric
functions are the q-free spectral data), while the constraint blocks are written
in the shifted tube coordinate. This bridge is what makes transporting a
constraint between the two coordinate systems a *checked* rewrite rather than a
hand substitution — the prerequisite for restating the cubic constraints in the
spectral `wᵢ`.

**Scope (honest).** This is a coordinate-change certificate: pure polynomial
algebra, no new geometry, no claim about the prolongation operator or the branch
locus (see `ColorSpectralCubicGeometry` for the latter). It does not by itself
rewrite any constraint block; it licenses such rewrites.

Base ring (§7c): generic `[CommRing R]` — every identity here is a polynomial
identity closed by `ring`, with no archimedean construct. The substrate
specialisation (`z = √q − 1/√q` at `R := ℝ`) happens at the consumer.

-- Ref: [manuscript] content/quantum-observable-universe/brings-surface/color-tube-cubic.md
-/

namespace QOU.Mass.ColorTubeSpectralBridge

variable {R : Type*} [CommRing R]

/-- The **color spectral cubic** `C_z(X) = X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)`,
matching `QOU.Mass.ColorSpectralCubicGeometry`'s coefficients and the
`e₁, e₂, e₃` of `QOU.Mass.ColorCubicPowerSums`. -/
def spectralCubic (z X : R) : R :=
  X ^ 3 + (z + 1) * X ^ 2 + (z ^ 2 + z + 1) * X + (z ^ 3 + z ^ 2 + z + 1)

/-- The **color tube cubic** `T_z(c) = c³ + (4z+1)c² + (6z²+3z+1)c + (4z³+3z²+2z+1)`,
as stated in the `color-tube-cubic` content block. -/
def tubeCubic (z c : R) : R :=
  c ^ 3 + (4 * z + 1) * c ^ 2 + (6 * z ^ 2 + 3 * z + 1) * c
    + (4 * z ^ 3 + 3 * z ^ 2 + 2 * z + 1)

/-- **The coordinate change (the block's prose claim, now machine-checked).**
The tube cubic is the spectral cubic in the shifted variable: `T_z(c) = C_z(c + z)`.
Equivalently the tube coordinate is `c = X − z`. -/
theorem tubeCubic_eq_spectralCubic_shift (z c : R) :
    tubeCubic z c = spectralCubic z (c + z) := by
  unfold tubeCubic spectralCubic
  ring

/-- The reverse reading: the spectral cubic is the tube cubic in `X − z`. -/
theorem spectralCubic_eq_tubeCubic_shift (z X : R) :
    spectralCubic z X = tubeCubic z (X - z) := by
  unfold tubeCubic spectralCubic
  ring

/-- **Root correspondence.** `w` is a root of the spectral cubic iff `w − z` is a
root of the tube cubic — the statement `cᵢ = wᵢ − z` at the level of roots. -/
theorem spectral_root_iff_tube_root (z w : R) :
    spectralCubic z w = 0 ↔ tubeCubic z (w - z) = 0 := by
  rw [← spectralCubic_eq_tubeCubic_shift]

/-! ## Vieta transport

The three symmetric functions transport by the shift. Stated as identities on the
spectral symmetric data `(e₁, e₂, e₃) = (−(z+1), z²+z+1, −(z³+z²+z+1))`, they
reproduce exactly the tube-cubic coefficients recorded in the content block.
Each is the generic three-variable shift identity specialised to the spectral
values, so the block's Vieta table is derived, not asserted. -/

/-- Generic shift identity for the first symmetric function. -/
theorem esym1_shift (z w₁ w₂ w₃ : R) :
    (w₁ - z) + (w₂ - z) + (w₃ - z) = (w₁ + w₂ + w₃) - 3 * z := by ring

/-- Generic shift identity for the second symmetric function. -/
theorem esym2_shift (z w₁ w₂ w₃ : R) :
    (w₁ - z) * (w₂ - z) + (w₁ - z) * (w₃ - z) + (w₂ - z) * (w₃ - z)
      = (w₁ * w₂ + w₁ * w₃ + w₂ * w₃) - 2 * z * (w₁ + w₂ + w₃) + 3 * z ^ 2 := by
  ring

/-- Generic shift identity for the third symmetric function. -/
theorem esym3_shift (z w₁ w₂ w₃ : R) :
    (w₁ - z) * (w₂ - z) * (w₃ - z)
      = w₁ * w₂ * w₃ - z * (w₁ * w₂ + w₁ * w₃ + w₂ * w₃)
        + z ^ 2 * (w₁ + w₂ + w₃) - z ^ 3 := by
  ring

/-- **Tube Vieta sum is derived.** With the spectral value `Σwᵢ = −(z+1)`, the
shift gives the block's `Σcᵢ = −(4z+1)`. -/
theorem tube_vieta_sum (z w₁ w₂ w₃ : R) (h : w₁ + w₂ + w₃ = -(z + 1)) :
    (w₁ - z) + (w₂ - z) + (w₃ - z) = -(4 * z + 1) := by
  rw [esym1_shift, h]; ring

/-- **Tube Vieta pair-sum is derived.** With the spectral values `Σwᵢ = −(z+1)`
and `Σ_{i<j}wᵢwⱼ = z²+z+1`, the shift gives the block's `6z²+3z+1`. -/
theorem tube_vieta_pair (z w₁ w₂ w₃ : R)
    (h1 : w₁ + w₂ + w₃ = -(z + 1))
    (h2 : w₁ * w₂ + w₁ * w₃ + w₂ * w₃ = z ^ 2 + z + 1) :
    (w₁ - z) * (w₂ - z) + (w₁ - z) * (w₃ - z) + (w₂ - z) * (w₃ - z)
      = 6 * z ^ 2 + 3 * z + 1 := by
  rw [esym2_shift, h1, h2]; ring

/-- **Tube Vieta product is derived.** With all three spectral symmetric values,
the shift gives the block's `∏cᵢ = −(4z³+3z²+2z+1)`. -/
theorem tube_vieta_product (z w₁ w₂ w₃ : R)
    (h1 : w₁ + w₂ + w₃ = -(z + 1))
    (h2 : w₁ * w₂ + w₁ * w₃ + w₂ * w₃ = z ^ 2 + z + 1)
    (h3 : w₁ * w₂ * w₃ = -(z ^ 3 + z ^ 2 + z + 1)) :
    (w₁ - z) * (w₂ - z) * (w₃ - z) = -(4 * z ^ 3 + 3 * z ^ 2 + 2 * z + 1) := by
  rw [esym3_shift, h1, h2, h3]; ring

end QOU.Mass.ColorTubeSpectralBridge
