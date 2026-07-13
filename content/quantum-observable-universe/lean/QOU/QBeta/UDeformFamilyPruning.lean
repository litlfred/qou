import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.Calculus.MeanValue

/-!
# u(q₀) family pruning — the NZ leading-form kill-test laws

Formalization of the structural laws behind
`computations/qbeta/qbeta_udeform_map_constraint_probe.py` (the u(q₀)
constraint probe of the `conj:binding-qbeta-complex-volume` S-channel,
`SDeformedVolumeChannel`).  The 4₁ Neumann–Zagier **leading form** of the
deformed complex volume is `Im 𝔙(u) ≈ (√3/2)|u|²·sin 2φ = √3·Re(u)·Im(u)`;
here it is a *definition* (`nzLeading x y = √3·x·y` on the two real
components), and the family laws are proved **unconditionally** about it:

* `fixed_phase_family_excluded` — a fixed-phase family
  (`Re, Im` both `∝ (q − q*)`) yields `S ∝ (q − q*)²`, which **cannot**
  produce the measured sign flip `S(muon) > 0 > S(proton)`.  This is a
  sign/parity structural exclusion (scope-(b) with the invariant proved,
  per AGENTS.md §refuted): the family's product across any two points is a
  square.
* `cubic_ratio_law` — the minimal phase-crossing family
  (`Re ∝ d, Im ∝ d²`) obeys `S(q₁)·(q₂−q*)³ = S(q₂)·(q₁−q*)³`.  The
  measured violation (anchor ratio −4.075 vs the law's −67.7, off 16.6×)
  lives in the probe witness; the Lean supplies the exact law the
  measurement kills.
* `linear_family_eq` / `linear_family_sign_flip` /
  `hasDerivAt_linear_family` — the surviving family (one component linear
  through zero at `q*`, the other constant) IS `S = √3·a·c·(q − q*)`:
  it sign-flips across `q*` whenever `√3·a·c ≠ 0`, with derivative
  exactly `√3·a·c` — the probe's product-slope `k = S′(q*)/√3` identity.

**Honesty boundary.**  What is NOT formalized: any `SDeformedVolumeChannel`
*instance*.  The identification of a concrete `u(q₀)` (and of the measured
`k ≈ 2.216×10⁶`) would wire an anchor-inverted map as canonical — a fit,
forbidden by the anti-laundering rule.  These theorems are the kill-test
*laws*; the measured numbers stay in
`computations/qbeta/qbeta-udeform-map-constraint.witness.json`.

-- Ref: [manuscript] conj:binding-qbeta-complex-volume; computations/qbeta/qbeta_udeform_map_constraint_probe.py
-- Ref: [neumann-zagier1985] Neumann & Zagier, "Volumes of hyperbolic three-manifolds," Topology 24 (1985). https://doi.org/10.1016/0040-9383(85)90004-7
-/

namespace QOU.QBeta.UDeformFamilyPruning

/-- The 4₁ Neumann–Zagier **leading form** of the deformed complex volume on
    the two real components of the deformation: `Im 𝔙(u) ≈ √3·Re(u)·Im(u)`
    (equivalently `(√3/2)|u|²·sin 2φ`).  A definition — the theorems below
    are unconditional laws of this leading form; its identification with the
    actual `Im 𝔙` is the cited NZ expansion, not a Lean claim. -/
noncomputable def nzLeading (x y : ℝ) : ℝ := Real.sqrt 3 * x * y

/-- The fixed-phase family's product across any two substrate points is a
    perfect square — the sign of `S` is the SAME on both sides of `q*`. -/
theorem fixed_phase_product_nonneg (cx cy qs q₁ q₂ : ℝ) :
    0 ≤ nzLeading (cx * (q₁ - qs)) (cy * (q₁ - qs))
      * nzLeading (cx * (q₂ - qs)) (cy * (q₂ - qs)) := by
  have hsq := sq_nonneg (Real.sqrt 3 * cx * cy * (q₁ - qs) * (q₂ - qs))
  unfold nzLeading
  nlinarith [hsq]

/-- **F1 exclusion (structural, sign invariant).**  A fixed-phase
    leading-order family cannot reproduce a sign flip: if `S` agrees with
    the family and takes a positive and a negative value, contradiction.
    The measured `S(muon) > 0 > S(proton)` therefore excludes the family —
    the probe's F1 verdict as a theorem. -/
theorem fixed_phase_family_excluded (cx cy qs q₁ q₂ : ℝ) (S : ℝ → ℝ)
    (hfam : ∀ q, S q = nzLeading (cx * (q - qs)) (cy * (q - qs)))
    (h₁ : 0 < S q₁) (h₂ : S q₂ < 0) : False := by
  rw [hfam q₁] at h₁
  rw [hfam q₂] at h₂
  nlinarith [fixed_phase_product_nonneg cx cy qs q₁ q₂]

/-- **F2 ratio law.**  The minimal phase-crossing family (`Re ∝ d`,
    `Im ∝ d²`) satisfies the exact cross-anchor cubic ratio law.  The probe
    measures its violation (−4.075 vs −67.7): the law is what the
    measurement kills. -/
theorem cubic_ratio_law (a b qs q₁ q₂ : ℝ) :
    nzLeading (a * (q₁ - qs)) (b * (q₁ - qs) ^ 2) * (q₂ - qs) ^ 3
      = nzLeading (a * (q₂ - qs)) (b * (q₂ - qs) ^ 2) * (q₁ - qs) ^ 3 := by
  unfold nzLeading
  ring

/-- The surviving (F3) family — one component linear through zero at `q*`,
    the other constant — evaluates to the linear `S = √3·a·c·(q − q*)`. -/
theorem linear_family_eq (a c qs q : ℝ) :
    nzLeading (a * (q - qs)) c = Real.sqrt 3 * a * c * (q - qs) := by
  unfold nzLeading
  ring

/-- **F3 produces the sign flip**: for a nondegenerate linear family the
    `S` values on opposite sides of `q*` have opposite signs — exactly the
    measured hard fact the other two families cannot supply. -/
theorem linear_family_sign_flip (a c qs q₁ q₂ : ℝ)
    (hk : Real.sqrt 3 * a * c ≠ 0) (h₁ : q₁ < qs) (h₂ : qs < q₂) :
    nzLeading (a * (q₁ - qs)) c * nzLeading (a * (q₂ - qs)) c < 0 := by
  rw [linear_family_eq, linear_family_eq]
  have hkk : 0 < (Real.sqrt 3 * a * c) * (Real.sqrt 3 * a * c) :=
    mul_self_pos.mpr hk
  have hd : (q₁ - qs) * (q₂ - qs) < 0 :=
    mul_neg_of_neg_of_pos (by linarith) (by linarith)
  nlinarith [hkk, hd]

/-- **F3 slope identity.**  The linear family's derivative at every point —
    in particular at `q*` — is exactly `√3·a·c`: the probe's product-slope
    identity `k = S′(q*)/√3` (measured `k ≈ 2.216×10⁶`, matching the
    committed hypersensitivity witness; the number stays in the witness). -/
theorem hasDerivAt_linear_family (a c qs q : ℝ) :
    HasDerivAt (fun q' => nzLeading (a * (q' - qs)) c)
      (Real.sqrt 3 * a * c) q := by
  have hfun : (fun q' => nzLeading (a * (q' - qs)) c)
      = fun q' => Real.sqrt 3 * a * c * q' - Real.sqrt 3 * a * c * qs := by
    funext q'
    rw [linear_family_eq]
    ring
  rw [hfun]
  simpa using ((hasDerivAt_id q).const_mul (Real.sqrt 3 * a * c)).sub_const
    (Real.sqrt 3 * a * c * qs)

end QOU.QBeta.UDeformFamilyPruning
