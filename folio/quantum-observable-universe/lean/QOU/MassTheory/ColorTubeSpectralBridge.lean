import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

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

-- Ref: [leitner2026] folio/quantum-observable-universe/brings-surface/color-tube-cubic.md
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

/-! ## Bring power sums: spectral form ⇒ tube-chart form

The same shift governs the **Bring's-surface constraints**. In the spectral
(Lagrange-resolvent) coordinates `w₀,…,w₄` the constraints are simply the
vanishing of the first three power sums,

  `p₁(w) = p₂(w) = p₃(w) = 0`,

which *is* the definition of Bring's surface — the clean spectral statement. The
`color-tube-constraints` block instead works in the shifted tube chart
`cₖ = wₖ − z` (`color-tube-coordinates`: `c_r = w₂−z`, `c_g = w₃−z`,
`c_b = w₄−z`, `σ = w₁−z`), where the constraints pick up `z`-dependence.

The theorems below transport the vanishing power sums through the shift and show
the tube-chart values are **forced**: `pₘ(c) = (−1)ᵐ · 5 · zᵐ` for `m = 1, 2, 3`.
This is the exact sense in which the spectral coordinates are the canonical ones
— in `w` the constraints are `0 = 0 = 0`, and every `z`-dependent term in the
tube chart is an artifact of the shift. -/

/-- Power sum `p₁` over the five spectral coordinates. -/
def psum1 (w₀ w₁ w₂ w₃ w₄ : R) : R := w₀ + w₁ + w₂ + w₃ + w₄

/-- Power sum `p₂` over the five spectral coordinates. -/
def psum2 (w₀ w₁ w₂ w₃ w₄ : R) : R :=
  w₀ ^ 2 + w₁ ^ 2 + w₂ ^ 2 + w₃ ^ 2 + w₄ ^ 2

/-- Power sum `p₃` over the five spectral coordinates. -/
def psum3 (w₀ w₁ w₂ w₃ w₄ : R) : R :=
  w₀ ^ 3 + w₁ ^ 3 + w₂ ^ 3 + w₃ ^ 3 + w₄ ^ 3

/-- **Shift law for `p₁`.** `p₁(w) = p₁(c) + 5z` when `wₖ = cₖ + z`. -/
theorem psum1_shift (z c₀ c₁ c₂ c₃ c₄ : R) :
    psum1 (c₀ + z) (c₁ + z) (c₂ + z) (c₃ + z) (c₄ + z)
      = psum1 c₀ c₁ c₂ c₃ c₄ + 5 * z := by
  unfold psum1; ring

/-- **Shift law for `p₂`.** `p₂(w) = p₂(c) + 2z·p₁(c) + 5z²`. -/
theorem psum2_shift (z c₀ c₁ c₂ c₃ c₄ : R) :
    psum2 (c₀ + z) (c₁ + z) (c₂ + z) (c₃ + z) (c₄ + z)
      = psum2 c₀ c₁ c₂ c₃ c₄ + 2 * z * psum1 c₀ c₁ c₂ c₃ c₄ + 5 * z ^ 2 := by
  unfold psum1 psum2; ring

/-- **Shift law for `p₃`.** `p₃(w) = p₃(c) + 3z·p₂(c) + 3z²·p₁(c) + 5z³`. -/
theorem psum3_shift (z c₀ c₁ c₂ c₃ c₄ : R) :
    psum3 (c₀ + z) (c₁ + z) (c₂ + z) (c₃ + z) (c₄ + z)
      = psum3 c₀ c₁ c₂ c₃ c₄ + 3 * z * psum2 c₀ c₁ c₂ c₃ c₄
        + 3 * z ^ 2 * psum1 c₀ c₁ c₂ c₃ c₄ + 5 * z ^ 3 := by
  unfold psum1 psum2 psum3; ring

/-- **Tube-chart `p₁` is forced.** The spectral constraint `p₁(w) = 0` forces
`p₁(c) = −5z` in the tube chart. -/
theorem tube_psum1_of_bring (z c₀ c₁ c₂ c₃ c₄ : R)
    (h1 : psum1 (c₀ + z) (c₁ + z) (c₂ + z) (c₃ + z) (c₄ + z) = 0) :
    psum1 c₀ c₁ c₂ c₃ c₄ = -(5 * z) := by
  rw [psum1_shift] at h1; linear_combination h1

/-- **Tube-chart `p₂` is forced.** The spectral constraints `p₁(w) = p₂(w) = 0`
force `p₂(c) = 5z²` — the `z`-dependence is entirely a shift artifact. -/
theorem tube_psum2_of_bring (z c₀ c₁ c₂ c₃ c₄ : R)
    (h1 : psum1 (c₀ + z) (c₁ + z) (c₂ + z) (c₃ + z) (c₄ + z) = 0)
    (h2 : psum2 (c₀ + z) (c₁ + z) (c₂ + z) (c₃ + z) (c₄ + z) = 0) :
    psum2 c₀ c₁ c₂ c₃ c₄ = 5 * z ^ 2 := by
  have e1 := tube_psum1_of_bring z c₀ c₁ c₂ c₃ c₄ h1
  rw [psum2_shift, e1] at h2
  linear_combination h2

/-- **Tube-chart `p₃` is forced.** The spectral constraints `p₁ = p₂ = p₃ = 0`
force `p₃(c) = −5z³`. Together with the two lemmas above this is the complete
`spectral ⇒ tube` transport of Bring's surface: `pₘ(c) = (−1)ᵐ·5·zᵐ`. -/
theorem tube_psum3_of_bring (z c₀ c₁ c₂ c₃ c₄ : R)
    (h1 : psum1 (c₀ + z) (c₁ + z) (c₂ + z) (c₃ + z) (c₄ + z) = 0)
    (h2 : psum2 (c₀ + z) (c₁ + z) (c₂ + z) (c₃ + z) (c₄ + z) = 0)
    (h3 : psum3 (c₀ + z) (c₁ + z) (c₂ + z) (c₃ + z) (c₄ + z) = 0) :
    psum3 c₀ c₁ c₂ c₃ c₄ = -(5 * z ^ 3) := by
  have e1 := tube_psum1_of_bring z c₀ c₁ c₂ c₃ c₄ h1
  have e2 := tube_psum2_of_bring z c₀ c₁ c₂ c₃ c₄ h1 h2
  rw [psum3_shift, e1, e2] at h3
  linear_combination h3

/-! ## The three `color-tube-constraints` equations, in spectral form

The three constraint equations of the `color-tube-constraints` block are written
in the shifted tube chart and are visibly `z`-dependent. Transported to the
spectral resolvents `wₖ` they become **`z`-free**: every `z` cancels identically.

Conventions are the block's own (`aggregate-color-quantities`), with the tube
chart `(σ, c_r, c_g, c_b) = (w₁−z, w₂−z, w₃−z, w₄−z)`:

* `p₁(c) = σ + c_r + c_g + c_b`  (first power sum)
* `h₂(c) = σ·c_b + c_r·c_g`  — the **Hermitian quadric**: it pairs *conjugate*
  resolvents `wₖ ↔ w₅₋ₖ`. It is **not** the full `e₂`; this is exactly the
  convention that had to be pinned before the restatement could be written.
* `h₃(c) = σ²c_g + c_b²c_r + c_r²σ + c_g²c_b`  (Hermitian cubic, skip-one)
* `S = Σₖ wₖ = p₁(c) + 4z`, `D = Σₖ ζ⁻ᵏwₖ = χ_ζ(c) − z`  (block identities)

The spectral invariants the constraints turn into:

* `H₂(w) = w₁w₄ + w₂w₃`  (spectral Hermitian quadric — conjugate pairing)
* `H₃(w) = w₁²w₃ + w₂²w₁ + w₄²w₂ + w₃²w₄`  (spectral Hermitian cubic) -/

/-- Spectral Hermitian quadric `H₂(w) = w₁w₄ + w₂w₃` (pairs `wₖ` with `w₅₋ₖ`). -/
def H2 (w₁ w₂ w₃ w₄ : R) : R := w₁ * w₄ + w₂ * w₃

/-- Spectral Hermitian cubic `H₃(w) = w₁²w₃ + w₂²w₁ + w₄²w₂ + w₃²w₄`. -/
def H3 (w₁ w₂ w₃ w₄ : R) : R :=
  w₁ ^ 2 * w₃ + w₂ ^ 2 * w₁ + w₄ ^ 2 * w₂ + w₃ ^ 2 * w₄

/-- Tube-chart first power sum `p₁(c)`. -/
def p1c (z w₁ w₂ w₃ w₄ : R) : R := (w₁ - z) + (w₂ - z) + (w₃ - z) + (w₄ - z)

/-- Tube-chart Hermitian quadric `h₂(c) = σ·c_b + c_r·c_g`. -/
def h2c (z w₁ w₂ w₃ w₄ : R) : R := (w₁ - z) * (w₄ - z) + (w₂ - z) * (w₃ - z)

/-- Tube-chart Hermitian cubic `h₃(c) = σ²c_g + c_b²c_r + c_r²σ + c_g²c_b`. -/
def h3c (z w₁ w₂ w₃ w₄ : R) : R :=
  (w₁ - z) ^ 2 * (w₃ - z) + (w₄ - z) ^ 2 * (w₂ - z)
    + (w₂ - z) ^ 2 * (w₁ - z) + (w₃ - z) ^ 2 * (w₄ - z)

/-- **`p₁(c) = S − 4z`** — the block's own shift identity, derived. -/
theorem p1c_eq (z w₁ w₂ w₃ w₄ : R) :
    p1c z w₁ w₂ w₃ w₄ = (w₁ + w₂ + w₃ + w₄) - 4 * z := by
  unfold p1c; ring

/-- **Shifted quadric is `H₂(w)`, exactly.** The block's
`h₂(c) + z·p₁(c) + 2z² ` equals the spectral Hermitian quadric `H₂(w)` — all
`z`-dependence cancels identically, so the constraint reads `H₂(w) = 0`. -/
theorem shifted_quadric_eq_H2 (z w₁ w₂ w₃ w₄ : R) :
    h2c z w₁ w₂ w₃ w₄ + z * p1c z w₁ w₂ w₃ w₄ + 2 * z ^ 2 = H2 w₁ w₂ w₃ w₄ := by
  unfold h2c p1c H2; ring

/-- **Shifted cubic is `H₃(w)`, exactly.** The block's
`h₃(c) + z(p₁(c)² − 2h₂(c)) + 3z²p₁(c) + 4z³` equals the spectral Hermitian
cubic `H₃(w)`; again every `z` cancels, so the constraint reads `H₃(w) = 0`. -/
theorem shifted_cubic_eq_H3 (z w₁ w₂ w₃ w₄ : R) :
    h3c z w₁ w₂ w₃ w₄
        + z * ((p1c z w₁ w₂ w₃ w₄) ^ 2 - 2 * h2c z w₁ w₂ w₃ w₄)
        + 3 * z ^ 2 * p1c z w₁ w₂ w₃ w₄ + 4 * z ^ 3
      = H3 w₁ w₂ w₃ w₄ := by
  unfold h3c p1c h2c H3; ring

/-- **Spacetime recovery is `S − zD`, exactly.** Using the block's identities
`χ_ζ(c) = D + z` and `p₁(c) = S − 4z`, the equation
`z² − (χ_ζ(c) − 4)z + p₁(c)` reduces to `S − z·D` — i.e. the constraint is
precisely `z = S/D`, the block's own `eq:z-from-SD`. Stated on the spectral
aggregates `S`, `D` (no `ζ` needed: it enters only through `D`). -/
theorem spacetime_recovery_eq (z S D : R) :
    z ^ 2 - ((D + z) - 4) * z + (S - 4 * z) = S - z * D := by ring

/-- **All three constraints are `z`-free in spectral coordinates.** Packaging the
above: each tube-chart equation equals a spectral invariant with no residual `z`.
So in the `wₖ` the Bring constraint system reads `S − zD = 0`, `H₂(w) = 0`,
`H₃(w) = 0` — the `z`-dependence visible in the tube chart is entirely a shift
artifact. -/
theorem constraints_spectral_form (z S D w₁ w₂ w₃ w₄ : R) :
    (z ^ 2 - ((D + z) - 4) * z + (S - 4 * z) = S - z * D) ∧
    (h2c z w₁ w₂ w₃ w₄ + z * p1c z w₁ w₂ w₃ w₄ + 2 * z ^ 2 = H2 w₁ w₂ w₃ w₄) ∧
    (h3c z w₁ w₂ w₃ w₄
        + z * ((p1c z w₁ w₂ w₃ w₄) ^ 2 - 2 * h2c z w₁ w₂ w₃ w₄)
        + 3 * z ^ 2 * p1c z w₁ w₂ w₃ w₄ + 4 * z ^ 3 = H3 w₁ w₂ w₃ w₄) :=
  ⟨spacetime_recovery_eq z S D, shifted_quadric_eq_H2 z w₁ w₂ w₃ w₄,
   shifted_cubic_eq_H3 z w₁ w₂ w₃ w₄⟩

end QOU.Mass.ColorTubeSpectralBridge
