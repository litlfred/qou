import Mathlib.Tactic
import QOU.Mass.PalindromicInvolutionLift

/-!
# QOU.Mass.QGaugeSpectralRigidity — a Seiberg–Witten spectral cubic is not a q-gauge invariant

The W1 wall (`qou-d8de`) asks for a q-difference prolongation `D_q` on the colour
spectral curve `Σ : P(X,z) = 0`, `λ_SW = X dz`. Routes 1 (a q-shift on the base)
and 2 (the fibre monodromy eigenvalue) are closed; the bean's own next step is
**route 3** — import the q-difference module framework from the literature rather
than hand-rolling an operator.

This file records what that import actually requires, and why the obvious
instantiation does not exist.

## The datum route 3 needs

Ramis–Sauloy–Zhang define (Astérisque 355 §2.1.1, `library/arxiv-0903.0853v3`):

> *"We call difference field a pair `(K, σ)`, where `K` is a (commutative) field
> and `σ` a field automorphism of `K`."*

and a q-difference module is a finite-dimensional `K`-space with a `σ`-linear
automorphism (Di Vizio–Ramis–Sauloy–Zhang §2.5,
`library/equations-aux-q-differences`). A **system** `σ_q X = A X` is then read
modulo **gauge**, and the gauge law is *not* conjugation
(DVRSZ eq. 2.4.1, verbatim):

> *"la même transformation de jauge ramène le système (2.3.1) au système
> `σ_q Y = B Y`, où `B = (σ_q F)⁻¹ A F`."*

That one equation is the whole content of this file. In the **differential /
Hitchin** case a gauge acts on a Higgs field by conjugation `Φ ↦ F Φ F⁻¹`, so
`det(X·1 − Φ)` is gauge-invariant and the Seiberg–Witten spectral curve is
well-defined. In the **q-difference** case `A ↦ (σ_q F)⁻¹ A F` is a *twisted*
action: taking `F = z^k · 1` gives `A ↦ q^{-k} A` (`scalar_gauge_factor`), so the
characteristic cubic's roots are rescaled by `q^{-k}`. A spectral cubic is
therefore an invariant of a q-difference module only if it is stable under
`X ↦ t·X` for every `t ∈ q^ℤ`.

## What is proved here

`weight_relations` — the `X ↦ t·X` stability of a monic cubic
`X³ + a₂X² + a₁X + a₀` forces, coefficient by coefficient,

  `a₀(1 − t³) = 0`,  `a₁·t·(1 − t²) = 0`,  `a₂·t²·(1 − t) = 0`,

so (`coeffs_vanish_of_scaling`) if `t` is a nonzero scalar with `t, t², t³ ≠ 1` —
in particular any real `t > 1`, `no_scaling_survives_of_one_lt` — then
**every non-leading coefficient vanishes**: the only monic cubic stable under the
gauge scaling is `X³ = 0`. This is general; it is not a fact about this `Σ`.

For the colour cubic the conclusion is immediate and sharp
(`gauge_scaling_fixes_colorCubic_iff`): the fibre over `z = 0` is
`X³ + X² + X + 1`, whose three non-leading coefficients are all `1`, so `t = 1`.

## How this differs from the neighbouring results, and what it does NOT say

`QOU.Mass.DilationBranchLocusRigidity` (#6769) moves the **base**: no dilation
`z ↦ l·z` preserves the branch locus, so none lifts to `Σ`. This file moves the
**fibre**: no scaling `X ↦ t·X` preserves the cubic. The two directions are
independent, and `colorCubic_weighted_rigid` proves the joint statement —
`P(λX, μz) = ν·P(X,z)` forces `λ = μ = ν = 1`.

The contrast with `QOU.Mass.PalindromicInvolutionLift` is the structural point.
The inversion `ι̃ : (X,z) ↦ (X/z, 1/z)` *does* preserve `Σ` because the colour
cubic is quasi-homogeneous for the paired action — `z³·P(X/z, 1/z) = P(X,z)`,
the coefficients being truncated geometric sums `a_k = 1 + z + ⋯ + z^{3−k}`. The
gauge scaling asks for an `X`-motion with **no compensating `z`-motion**, and for
that there is no weight to be had.

**Scope.** This excludes `Σ` as the *gauge-invariant spectral curve* of a rank-3
q-difference module. It does not exclude route 3: a q-difference module over
`(ℂ(z), σ_q)` is a perfectly good object, and `Σ` may still enter such a module
as data that is not a characteristic-polynomial curve (Newton polygon, slopes,
the Birkhoff connection matrix, the bundle on `E_q = ℂ*/q^ℤ` of RSZ §6.3).
Nothing here constructs `D_q`, and nothing is fitted or wired.

The bridge "the sought `D_q` would have `Σ` as its spectral curve" is an
**assumption**, not a theorem — it is what `λ_SW = X dz` sets up and what the
phrase *"a q-difference prolongation of `Σ`"* means, but it is stated as a
hypothesis, never used as a fact.

> **Currency note (2026-09-12).** This file originally closed by recording the
> covering/gauge dictionary as "not formalised, prose only … cited rather than
> re-proved in Lean". It is now proved, in `QOU.Mass.QDifferenceGaugeMatrix`:
> `scalar_gauge_eq` (DVRSZ eq. 2.4.1 for a scalar gauge, cleared of the inverse),
> `det_charMatrix_smul` (scaling the system matrix substitutes `X ↦ X/t` in the
> characteristic polynomial — the curve *moves*), and `det_charMatrix_conj` (the
> contrast: conjugation does not move it, which is why a Higgs field has a
> well-defined Seiberg–Witten spectral curve). `charCubic_smul` below remains the
> coefficient-level form; the matrix-level statements are the step before it.

Ground ring: `[CommRing K]` for the weight algebra, `[Field K] [CharZero K]`
where the two halves of an evaluation pair are divided (§7c). Nothing
archimedean appears except in the explicitly real substrate corollary.
-/

namespace QOU.Mass.QGaugeSpectralRigidity

open QOU.Mass.PalindromicInvolutionLift

variable {K : Type*}

section CommRing

variable [CommRing K]

/-- **Scaling the system matrix scales the spectral coefficients by weight.**
If a rank-3 system matrix has spectral roots `r₁, r₂, r₃`, then scaling it by `t`
sends its characteristic cubic to the one whose `X^{3−k}` coefficient carries an
extra `t^k`. This is the whole mechanism: the gauge `F = z^k·1` multiplies `A` by
a scalar (`scalar_gauge_factor`), and a scalar multiple moves the curve. -/
theorem charCubic_smul (t r₁ r₂ r₃ X : K) :
    (X - t * r₁) * (X - t * r₂) * (X - t * r₃)
      = X ^ 3 - t * (r₁ + r₂ + r₃) * X ^ 2
        + t ^ 2 * (r₁ * r₂ + r₁ * r₃ + r₂ * r₃) * X
        - t ^ 3 * (r₁ * r₂ * r₃) := by
  ring

/-- The **gauged colour cubic** — the colour cubic with the weights its
coefficients acquire under the gauge scaling by `t`. At `t = 1` it is the colour
cubic (`gaugedColorCubic_one`); `colorCubic_scale_eq` shows it is exactly the
rescaled curve, so the weights are read off rather than posited. -/
def gaugedColorCubic (t X z : K) : K :=
  X ^ 3 + t * (z + 1) * X ^ 2 + t ^ 2 * (z ^ 2 + z + 1) * X
    + t ^ 3 * (z ^ 3 + z ^ 2 + z + 1)

@[simp] theorem gaugedColorCubic_one (X z : K) :
    gaugedColorCubic 1 X z = colorCubic X z := by
  unfold gaugedColorCubic colorCubic; ring

end CommRing

section FieldScaling

variable [Field K]

/-- **The scalar gauge factor is a power of `q`.** DVRSZ eq. 2.4.1 with the gauge
matrix `F = z^k·1` and `σ_q : z ↦ q·z` gives `B = (σ_q F)⁻¹ A F = q^{-k}·A`. So
the scalars reachable by a monomial gauge are exactly `q^ℤ`, and a spectral curve
can be a gauge invariant only if it survives every `X ↦ q^k·X`. -/
theorem scalar_gauge_factor (q z : K) (k : ℕ) (hq : q ≠ 0) (hz : z ≠ 0) :
    z ^ k / (q * z) ^ k = (q ^ k)⁻¹ := by
  rw [mul_pow]
  field_simp

/-- **The gauged cubic IS the rescaled curve.** Scaling the spectral coordinate by
`t` and renormalising by the leading `t³` is the same as reweighting the
coefficients by `t⁻¹`. This is what makes `gaugedColorCubic` the right object
rather than an ansatz. -/
theorem colorCubic_scale_eq (t X z : K) (ht : t ≠ 0) :
    colorCubic (t * X) z = t ^ 3 * gaugedColorCubic t⁻¹ X z := by
  unfold colorCubic gaugedColorCubic
  field_simp

end FieldScaling

section Field

variable [Field K] [CharZero K]

/-- **The weight relations.** If a monic cubic `X³ + a₂X² + a₁X + a₀` is stable
under the gauge scaling `X ↦ t·X` (up to the leading factor `t³`), then each
non-leading coefficient is annihilated by its own weight defect.

Three evaluations do it: `X = 0` gives the constant relation, and the sum and
difference of `X = ±1` separate the quadratic from the linear one. Characteristic
zero is used only to halve those two. -/
theorem weight_relations (t a₂ a₁ a₀ : K)
    (h : ∀ X : K, (t * X) ^ 3 + a₂ * (t * X) ^ 2 + a₁ * (t * X) + a₀
          = t ^ 3 * (X ^ 3 + a₂ * X ^ 2 + a₁ * X + a₀)) :
    a₀ * (1 - t ^ 3) = 0 ∧ a₁ * t * (1 - t ^ 2) = 0 ∧ a₂ * t ^ 2 * (1 - t) = 0 := by
  have h0 := h 0
  have h1 := h 1
  have hm := h (-1)
  refine ⟨by linear_combination h0, ?_, ?_⟩
  · linear_combination (1 / 2 : K) * h1 - (1 / 2 : K) * hm
  · linear_combination (1 / 2 : K) * h1 + (1 / 2 : K) * hm - h0

/-- **No monic cubic with a non-leading coefficient survives the gauge scaling.**
If the scalar `t` is not a root of `X³ − 1` and not a root of `X² − 1` and is not
`1`, stability forces `a₂ = a₁ = a₀ = 0` — the cubic degenerates to `X³ = 0`.

So a Seiberg–Witten spectral cubic is a gauge invariant of a rank-3 q-difference
module only in the degenerate case. -/
theorem coeffs_vanish_of_scaling (t a₂ a₁ a₀ : K) (ht : t ≠ 0)
    (ht1 : t ≠ 1) (ht2 : t ^ 2 ≠ 1) (ht3 : t ^ 3 ≠ 1)
    (h : ∀ X : K, (t * X) ^ 3 + a₂ * (t * X) ^ 2 + a₁ * (t * X) + a₀
          = t ^ 3 * (X ^ 3 + a₂ * X ^ 2 + a₁ * X + a₀)) :
    a₂ = 0 ∧ a₁ = 0 ∧ a₀ = 0 := by
  obtain ⟨e0, e1, e2⟩ := weight_relations t a₂ a₁ a₀ h
  refine ⟨?_, ?_, ?_⟩
  · have hne : (1 : K) - t ≠ 0 := fun hc => ht1 (by linear_combination -hc)
    have := mul_eq_zero.mp e2
    rcases this with hz | hz
    · rcases mul_eq_zero.mp hz with hz' | hz'
      · exact hz'
      · exact absurd (pow_eq_zero_iff (n := 2) (by norm_num) |>.mp hz') ht
    · exact absurd hz hne
  · have hne : (1 : K) - t ^ 2 ≠ 0 := fun hc => ht2 (by linear_combination -hc)
    rcases mul_eq_zero.mp e1 with hz | hz
    · rcases mul_eq_zero.mp hz with hz' | hz'
      · exact hz'
      · exact absurd hz' ht
    · exact absurd hz hne
  · have hne : (1 : K) - t ^ 3 ≠ 0 := fun hc => ht3 (by linear_combination -hc)
    rcases mul_eq_zero.mp e0 with hz | hz
    · exact hz
    · exact absurd hz hne

/-- **The colour cubic, sharply.** If the gauge scaling by `t` fixes the colour
cubic then `t = 1`. Only the fibre over `z = 0` is used — it is `X³+X²+X+1`, all
three non-leading coefficients equal to `1`, so no weight can be absorbed. -/
theorem gauge_scaling_fixes_colorCubic_iff (t : K)
    (h : ∀ X z : K, gaugedColorCubic t X z = colorCubic X z) : t = 1 := by
  have h0 := h 0 0
  have h1 := h 1 0
  have hm := h (-1) 0
  simp only [gaugedColorCubic, colorCubic] at h0 h1 hm
  have e0 : t ^ 3 = 1 := by linear_combination h0
  have e1 : t + t ^ 3 = 2 := by
    linear_combination (1 / 2 : K) * h1 + (1 / 2 : K) * hm
  linear_combination e1 - e0

/-- **Joint rigidity: fibre scaling AND base dilation together.** If some pair
`(λ, μ)` of scalings — `X ↦ λ·X` in the fibre, `z ↦ μ·z` on the base — sends the
colour cubic to a constant multiple of itself, then all three of `λ, μ, ν` are
`1`. This is the statement that closes the *combined* move, which neither
#6769 (base only) nor `gauge_scaling_fixes_colorCubic_iff` (fibre only) reaches
on its own.

Four evaluations: `(0,0)` fixes `ν`, then `(±1, 0)` fix `λ`, then `(±1, 1)`
together with `(0,1)` fix `μ`. -/
theorem colorCubic_weighted_rigid (l m n : K)
    (h : ∀ X z : K, colorCubic (l * X) (m * z) = n * colorCubic X z) :
    l = 1 ∧ m = 1 ∧ n = 1 := by
  have c00 := h 0 0
  have c10 := h 1 0
  have cm0 := h (-1) 0
  simp only [colorCubic] at c00 c10 cm0
  -- `(0,0)`: the constant term is `1` on both sides, so `n = 1`.
  have hn : n = 1 := by linear_combination -c00
  subst hn
  -- `z = 0`: the cubic is `X³+X²+X+1`; `±1` give `l² = 1` and `l³ + l = 2`.
  have hl2 : l ^ 2 = 1 := by
    linear_combination (1 / 2 : K) * c10 + (1 / 2 : K) * cm0
  have hl3 : l ^ 3 + l = 2 := by
    linear_combination (1 / 2 : K) * c10 - (1 / 2 : K) * cm0
  have hl : l = 1 := by linear_combination (1 / 2 : K) * hl3 - (1 / 2 : K) * l * hl2
  subst hl
  refine ⟨rfl, ?_, rfl⟩
  -- With `l = n = 1` the identity is a statement about `m` alone.
  have d01 := h 0 1
  have d11 := h 1 1
  have dm1 := h (-1) 1
  simp only [colorCubic] at d01 d11 dm1
  -- `(±1, 1)` averaged is `m³+m²+2m−4`; subtracting `(0,1)`'s `m³+m²+m−3` leaves `m−1`.
  linear_combination (1 / 2 : K) * d11 + (1 / 2 : K) * dm1 - d01

end Field

/-- **The substrate case.** The gauge scalars are `q^ℤ` and the substrate modulus
is real with `q₀ > 1`, so every nontrivial gauge scalar is a real `t > 1`; no such
`t` leaves any non-leading coefficient of a monic cubic alive. Stated for a
general real `t > 1` so that no numerical value enters the Lean. -/
theorem no_scaling_survives_of_one_lt (t a₂ a₁ a₀ : ℝ) (ht : 1 < t)
    (h : ∀ X : ℝ, (t * X) ^ 3 + a₂ * (t * X) ^ 2 + a₁ * (t * X) + a₀
          = t ^ 3 * (X ^ 3 + a₂ * X ^ 2 + a₁ * X + a₀)) :
    a₂ = 0 ∧ a₁ = 0 ∧ a₀ = 0 := by
  have ht0 : (0 : ℝ) < t := by linarith
  have h2t : (1 : ℝ) < t ^ 2 := by nlinarith
  have h3t : (1 : ℝ) < t ^ 3 := by nlinarith
  exact coeffs_vanish_of_scaling t a₂ a₁ a₀ (ne_of_gt ht0) (ne_of_gt ht)
    (ne_of_gt h2t) (ne_of_gt h3t) h

/-- **The colour cubic is not degenerate**, so the previous theorem bites: its
fibre over `z = 0` has all three non-leading coefficients equal to `1`. -/
theorem colorCubic_fibre_at_zero_coeffs (X : ℝ) :
    colorCubic X (0 : ℝ) = X ^ 3 + 1 * X ^ 2 + 1 * X + 1 := by
  unfold colorCubic; ring

end QOU.Mass.QGaugeSpectralRigidity
