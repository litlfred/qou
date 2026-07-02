/-
# 𝔙 fibre-descent — the ζ₄-partner relation of the complex-volume model

Advances `conj:binding-qbeta-complex-volume` (the descent of binding `Re 𝔙` and Q_β `Im 𝔙` from
one fibre object). `QOU.Mass.ComplexVolumeFibreDescent` (merged, #2951) states the descent class
and gives the `cosh/sinh` model `V₀(η) = cosh η + i·sinh η` as a non-vacuous instance.
`QOU.Mass.Zeta4ComplexVolumeModerator` (merged, #2941) proves the generator coupling
`cosh(z+iπ/2) = i·sinh z`.

This file proves the **ζ₄-partner relation** of the model on the complex fibre: rotating the
argument by `ζ₄ = i` (`z ↦ z + iπ/2`) sends `V₀` to `−cosh + i·sinh`, i.e. it **negates the
bar-even (binding / `Re`) channel and keeps the bar-odd (Q_β / `Im`) channel** — the exact
fibre-level signature of how `ζ₄` couples the two channels of one `𝔙 = Vol + i·CS` (for real `η`
this is `V₀(η + iπ/2) = −conj V₀(η)`, verified symbolically in
`computations/substrate/frakV_descent_zeta4_partner_probe.py`).

This is a structural advance on the descent, **not** a closure: the full descent of the *actual*
binding and Q_β observables from a single fibre `𝔙` remains the open keystone (gated on the Q_β
`c_k` Habiro element / SW-residue derivation; see the audit). Sorry-free.

-- Ref: [manuscript] docs/audits/2026-06-28-frakV-descent-zeta4-partner.md
-/
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Tactic

namespace QOU.Mass.ComplexVolumeZeta4Partner

open Complex

/-- The complex-volume fibre model on a complex argument: `V₀(z) = cosh z + i·sinh z`. -/
noncomputable def vModel (z : ℂ) : ℂ := Complex.cosh z + Complex.I * Complex.sinh z

/-- `cosh(z + iπ/2) = i·sinh z` (the ζ₄ moderator, re-derived self-contained). -/
private theorem cosh_rot (z : ℂ) :
    Complex.cosh (z + (↑(Real.pi / 2) : ℂ) * Complex.I) = Complex.I * Complex.sinh z := by
  rw [Complex.cosh_add]
  have h0 : Complex.cosh ((↑(Real.pi / 2) : ℂ) * Complex.I) = 0 := by
    rw [Complex.cosh_mul_I, ← Complex.ofReal_cos, Real.cos_pi_div_two, Complex.ofReal_zero]
  have h1 : Complex.sinh ((↑(Real.pi / 2) : ℂ) * Complex.I) = Complex.I := by
    rw [Complex.sinh_mul_I, ← Complex.ofReal_sin, Real.sin_pi_div_two, Complex.ofReal_one,
      one_mul]
  rw [h0, h1]; ring

/-- `sinh(z + iπ/2) = i·cosh z`. -/
private theorem sinh_rot (z : ℂ) :
    Complex.sinh (z + (↑(Real.pi / 2) : ℂ) * Complex.I) = Complex.I * Complex.cosh z := by
  rw [Complex.sinh_add]
  have h0 : Complex.cosh ((↑(Real.pi / 2) : ℂ) * Complex.I) = 0 := by
    rw [Complex.cosh_mul_I, ← Complex.ofReal_cos, Real.cos_pi_div_two, Complex.ofReal_zero]
  have h1 : Complex.sinh ((↑(Real.pi / 2) : ℂ) * Complex.I) = Complex.I := by
    rw [Complex.sinh_mul_I, ← Complex.ofReal_sin, Real.sin_pi_div_two, Complex.ofReal_one,
      one_mul]
  rw [h0, h1]; ring

/-- **ζ₄-partner relation.** The `ζ₄ = i` rotation `z ↦ z + iπ/2` sends the complex-volume model to
`V₀(z + iπ/2) = −cosh z + i·sinh z` — it **negates the bar-even (binding / Re) channel** and keeps
the bar-odd (Q_β / Im) channel. This is the fibre-level signature of how `ζ₄` couples the two
channels of `𝔙 = Vol + i·CS`. (For real `η` the RHS is `−conj V₀(η)`.) -/
theorem vModel_zeta4_partner (z : ℂ) :
    vModel (z + (↑(Real.pi / 2) : ℂ) * Complex.I)
      = -Complex.cosh z + Complex.I * Complex.sinh z := by
  rw [vModel, cosh_rot, sinh_rot]
  have hII : Complex.I * (Complex.I * Complex.cosh z) = -Complex.cosh z := by
    rw [← mul_assoc, Complex.I_mul_I]; ring
  rw [hII]; ring

/-! ## The full ζ₄ orbit and its isotypic decomposition (bean 5nx8, 2026-07-02)

One layer beyond the partner relation: the ζ₄ action on the model closes into an order-4 orbit
(`ζ₄² = −1`, `ζ₄³ = ` channel-conjugation), the two **non-faithful** isotypes vanish (orbit sum =
trivial isotype = 0; alternating sum = sign isotype = 0), and the model decomposes exactly into the
two **faithful** eigencomponents `(1 ± i)/2 · e^{±z}` (eigenvalues `±i` under the rotation). The
binding (`cosh`, bar-even) and Q_β (`i·sinh`, bar-odd) channels are the symmetric/antisymmetric
recombinations of the faithful pair. **Constraint on the open single-`𝔙` assembly** (the 5nx8 gap
map's OPEN piece): any candidate assembly must be ζ₄-faithful — a nonzero orbit sum or a nonzero
sign-isotype component falsifies it. Structural advance, not a closure. -/

/-- **ζ₄² = −1 on the model**: two rotations negate `V₀`. -/
theorem vModel_zeta4_sq (z : ℂ) :
    vModel (z + (↑(Real.pi / 2) : ℂ) * Complex.I + (↑(Real.pi / 2) : ℂ) * Complex.I)
      = -vModel z := by
  rw [vModel_zeta4_partner, cosh_rot, sinh_rot]
  have hII : Complex.I * (Complex.I * Complex.cosh z) = -Complex.cosh z := by
    rw [← mul_assoc, Complex.I_mul_I]; ring
  rw [hII, vModel]; ring

/-- **ζ₄³ = channel conjugation**: three rotations send `V₀` to `cosh − i·sinh` (Q_β channel
negated, binding channel kept — the partner relation's mirror). -/
theorem vModel_zeta4_cube (z : ℂ) :
    vModel (z + (↑(Real.pi / 2) : ℂ) * Complex.I + (↑(Real.pi / 2) : ℂ) * Complex.I
        + (↑(Real.pi / 2) : ℂ) * Complex.I)
      = Complex.cosh z - Complex.I * Complex.sinh z := by
  rw [vModel_zeta4_sq (z + (↑(Real.pi / 2) : ℂ) * Complex.I), vModel_zeta4_partner]; ring

/-- **Trivial isotype vanishes**: the full ζ₄-orbit of the model sums to zero — the assembly
carries NO ζ₄-invariant component. -/
theorem vModel_orbit_sum_zero (z : ℂ) :
    vModel z + vModel (z + (↑(Real.pi / 2) : ℂ) * Complex.I)
      + vModel (z + (↑(Real.pi / 2) : ℂ) * Complex.I + (↑(Real.pi / 2) : ℂ) * Complex.I)
      + vModel (z + (↑(Real.pi / 2) : ℂ) * Complex.I + (↑(Real.pi / 2) : ℂ) * Complex.I
          + (↑(Real.pi / 2) : ℂ) * Complex.I)
      = 0 := by
  rw [vModel_zeta4_partner, vModel_zeta4_sq, vModel_zeta4_cube]; ring

/-- **Sign isotype vanishes**: the alternating orbit sum is zero — the model has no component in
the sign character of `ℤ₄` either. Together with `vModel_orbit_sum_zero`, the model is supported
entirely on the two FAITHFUL characters `±i`. -/
theorem vModel_sign_isotype_zero (z : ℂ) :
    vModel z - vModel (z + (↑(Real.pi / 2) : ℂ) * Complex.I)
      + vModel (z + (↑(Real.pi / 2) : ℂ) * Complex.I + (↑(Real.pi / 2) : ℂ) * Complex.I)
      - vModel (z + (↑(Real.pi / 2) : ℂ) * Complex.I + (↑(Real.pi / 2) : ℂ) * Complex.I
          + (↑(Real.pi / 2) : ℂ) * Complex.I)
      = 0 := by
  rw [vModel_zeta4_partner, vModel_zeta4_sq, vModel_zeta4_cube]; ring

/-- `exp` is the `+i`-eigenvector of the ζ₄ rotation: `exp(z + iπ/2) = i·exp z`. -/
theorem exp_zeta4_eigen (z : ℂ) :
    Complex.exp (z + (↑(Real.pi / 2) : ℂ) * Complex.I) = Complex.I * Complex.exp z := by
  rw [Complex.exp_add]
  have hR : Complex.exp ((↑(Real.pi / 2) : ℂ) * Complex.I) = Complex.I := by
    rw [Complex.exp_mul_I, ← Complex.ofReal_cos, ← Complex.ofReal_sin,
      Real.cos_pi_div_two, Real.sin_pi_div_two]
    simp
  rw [hR]; ring

/-- `exp(−z)` is the `−i`-eigenvector: `exp(−(z + iπ/2)) = −i·exp(−z)`. -/
theorem exp_neg_zeta4_eigen (z : ℂ) :
    Complex.exp (-(z + (↑(Real.pi / 2) : ℂ) * Complex.I)) = -Complex.I * Complex.exp (-z) := by
  have hR : Complex.exp ((↑(Real.pi / 2) : ℂ) * Complex.I) = Complex.I := by
    rw [Complex.exp_mul_I, ← Complex.ofReal_cos, ← Complex.ofReal_sin,
      Real.cos_pi_div_two, Real.sin_pi_div_two]
    simp
  rw [neg_add, Complex.exp_add, Complex.exp_neg, Complex.exp_neg, hR, Complex.inv_I]; ring

/-- **Faithful decomposition.** The model is exactly the sum of its two faithful
ζ₄-eigencomponents: `V₀(z) = (1+i)/2·e^z + (1−i)/2·e^{−z}` (eigenvalues `+i` / `−i` by
`exp_zeta4_eigen` / `exp_neg_zeta4_eigen`). The binding and Q_β channels are the
symmetric/antisymmetric recombinations of this faithful pair. -/
theorem vModel_eq_faithful_sum (z : ℂ) :
    vModel z
      = (1 + Complex.I) / 2 * Complex.exp z + (1 - Complex.I) / 2 * Complex.exp (-z) := by
  rw [vModel, ← Complex.cosh_add_sinh z, ← Complex.cosh_sub_sinh z]; ring

end QOU.Mass.ComplexVolumeZeta4Partner
