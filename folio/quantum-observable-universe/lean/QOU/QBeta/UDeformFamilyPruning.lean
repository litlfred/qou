import QOU.Knot.FigureEightComplexVolume

/-!
# u(q₀) family pruning — the corrected harmonic-form kill-test laws

Formalization of the structural laws behind
`computations/qbeta/qbeta_udeform_map_constraint_probe.py` and
`computations/probes/sdeformed_channel_signflip_probe.py` (the `u(q₀)`
constraint probe of the `conj:binding-qbeta-complex-volume` S-channel,
`SDeformedVolumeChannel`).

**The leading form (corrected).** The figure-eight (4₁) A-polynomial cusp
modulus is `τ = −i√3` (purely imaginary, ℚ(√−3)), so the leading
Neumann–Zagier complex-volume coefficient is `a₂ = i·√3/4` (purely
imaginary) and the leading imaginary part of the deformed complex volume is
the HARMONIC quadratic form

    Im 𝔙(u) = (√3/4)·(Re²u − Im²u)      (NOT the earlier `√3·Re u·Im u`).

The concrete `𝔙` is `QOU.Knot.FigureEightComplexVolume.V₄₁`; this file feeds
the family's real/imaginary components into it via
`familyIm x y := (V₄₁ ⟨x, y⟩).im = (√3/4)(x² − y²)` (`familyIm_eq`) and reuses
`imV₄₁` / `imV₄₁_pos_iff` / `imV₄₁_neg_iff` / `signflip_forces_diagonal_cross`
/ `f3_re_linear_same_sign`. It does **not** re-define a standalone
`√3·x·y` leading form (that was the wrong-`a₂` artefact, refuted by `τ = −i√3`).

**All three `u(q₀)` kill-test families are REFUTED** — each is even in
`d = q − q*`, hence same-signed on both sides of `q*`, so none can produce the
measured bar-odd flip `S(muon) ≈ +0.00968 > 0 > S(proton) ≈ −0.03946`:

* **F1 — fixed-phase** (`Re = cx·d`, `Im = cy·d`):
  `familyIm = (√3/4)(cx² − cy²)d²`, EVEN in `d`. Its product across any two
  substrate points is a perfect square (`fixed_phase_product_nonneg`), so the
  sign is the SAME on both sides of `q*` and the family CANNOT sign-flip
  (`fixed_phase_family_excluded`). A scope-(b) structural sign exclusion
  (invariant proved), per AGENTS.md §refuted.
* **F2 — phase-crossing** (`Re = a·d`, `Im = b·d²`):
  `familyIm = (√3/4)(a²d² − b²d⁴)`, EVEN in `d` with leading `∝ d²` (the old
  `cubic_ratio_law`/`∝d³` was a wrong-form artefact). Within the small
  excursion `b²d² ≤ a²` the value is `≥ 0` (`phase_crossing_nonneg`), its
  cross-anchor product is `≥ 0` (`phase_crossing_product_nonneg`), so the
  family CANNOT sign-flip near `q*` (`phase_crossing_family_excluded`).
* **F3 — transverse-constant** (`Re = a·d`, `Im = c₀`):
  `familyIm = (√3/4)((a·d)² − c₀²)`, EVEN in `d`. Within `(a·d)² < c₀²` the
  value is `< 0` (`transverse_const_neg`, reusing `f3_re_linear_same_sign`),
  its cross-anchor product is `> 0` (`transverse_const_product_nonneg`), so
  both anchors are NEGATIVE and the family CANNOT sign-flip
  (`transverse_const_family_excluded`). This REPLACES the earlier
  `linear_family_sign_flip`/`linear_family_eq`/`hasDerivAt_linear_family`,
  which claimed F3 sign-flips/survives — the CORE ERROR of the `√3·x·y` form.

**Surviving necessary condition.** `S = Im 𝔙` sign-flips only where
`Re²u − Im²u` changes sign, i.e. `u(q₀)` must CROSS the diagonal
`|Re u| = |Im u|` between the anchors (`signflip_requires_diagonal_cross`,
via `signflip_forces_diagonal_cross`). No family with both anchors on the same
side of that diagonal survives.

**Honesty boundary.** What is NOT formalized: any `SDeformedVolumeChannel`
*instance*. The identification of a concrete `u(q₀)` (and of the measured
product-slope `k`) would wire an anchor-inverted map as canonical — a fit,
forbidden by the anti-laundering rule. `u(q₀)` stays OPEN. These theorems are
the kill-test *laws* over the corrected harmonic form; the measured numbers
stay in
`computations/qbeta/qbeta-udeform-map-constraint.witness.json`.

-- Ref: [leitner2026] conj:binding-qbeta-complex-volume;
     computations/qbeta/qbeta_udeform_map_constraint_probe.py;
     docs/audits/2026-07-26-sdeformed-channel-signflip.md
-- Ref: [neumann-zagier1985] Neumann & Zagier, "Volumes of hyperbolic three-manifolds," Topology 24 (1985). https://doi.org/10.1016/0040-9383(85)90004-7
-/

namespace QOU.QBeta.UDeformFamilyPruning

open QOU.Knot.FigureEightComplexVolume

/-- The family's imaginary part: the deformed complex volume's Chern–Simons
    part evaluated on the two real components `(x, y)` of the deformation,
    `familyIm x y = (𝔙₄₁⟨x, y⟩).im`. Its identification with the concrete
    figure-eight complex volume is `QOU.Knot.FigureEightComplexVolume.V₄₁`,
    not a fresh Lean claim. -/
noncomputable def familyIm (x y : ℝ) : ℝ := (V₄₁ ⟨x, y⟩).im

/-- The corrected leading form: `familyIm x y = (√3/4)(x² − y²)` — a HARMONIC
    quadratic form (vanishing on the diagonals `|x| = |y|`), NOT the earlier
    `√3·x·y`. Direct from `imV₄₁`. -/
theorem familyIm_eq (x y : ℝ) :
    familyIm x y = cuspModulus * (x ^ 2 - y ^ 2) := by
  unfold familyIm
  rw [imV₄₁]

/-! ## F1 — fixed-phase family: even in `d`, cannot sign-flip -/

/-- The fixed-phase family's product across any two substrate points is a
    perfect square — the sign of `familyIm` is the SAME on both sides of `q*`.
    `familyIm(cx·d, cy·d) = (√3/4)(cx² − cy²)d²`, even in `d`. -/
theorem fixed_phase_product_nonneg (cx cy qs q₁ q₂ : ℝ) :
    0 ≤ familyIm (cx * (q₁ - qs)) (cy * (q₁ - qs))
      * familyIm (cx * (q₂ - qs)) (cy * (q₂ - qs)) := by
  rw [familyIm_eq, familyIm_eq]
  nlinarith [sq_nonneg (cuspModulus * (cx ^ 2 - cy ^ 2) * (q₁ - qs) * (q₂ - qs)),
    cuspModulus_pos]

/-- **F1 exclusion (structural, sign invariant).** A fixed-phase leading-order
    family cannot reproduce a sign flip: if `S` agrees with the family and
    takes a positive and a negative value, contradiction. The measured
    `S(muon) > 0 > S(proton)` therefore excludes the family. -/
theorem fixed_phase_family_excluded (cx cy qs q₁ q₂ : ℝ) (S : ℝ → ℝ)
    (hfam : ∀ q, S q = familyIm (cx * (q - qs)) (cy * (q - qs)))
    (h₁ : 0 < S q₁) (h₂ : S q₂ < 0) : False := by
  rw [hfam q₁] at h₁
  rw [hfam q₂] at h₂
  have hprod := fixed_phase_product_nonneg cx cy qs q₁ q₂
  have hneg := mul_neg_of_pos_of_neg h₁ h₂
  linarith

/-! ## F2 — phase-crossing family: even in `d`, leading `∝ d²`, cannot sign-flip -/

/-- Within the small excursion `b²d² ≤ a²`, the phase-crossing family value is
    non-negative: `familyIm(a·d, b·d²) = (√3/4)·d²·(a² − b²d²) ≥ 0`. The old
    `cubic_ratio_law` (`∝ d³`) was a wrong-form artefact; the corrected leading
    behaviour is `∝ d²`, even in `d`. -/
theorem phase_crossing_nonneg {a b d : ℝ} (h : b ^ 2 * d ^ 2 ≤ a ^ 2) :
    0 ≤ familyIm (a * d) (b * d ^ 2) := by
  rw [familyIm_eq]
  have h1 : (0 : ℝ) ≤ a ^ 2 - b ^ 2 * d ^ 2 := by linarith
  have h2 : (0 : ℝ) ≤ d ^ 2 * (a ^ 2 - b ^ 2 * d ^ 2) := mul_nonneg (sq_nonneg d) h1
  nlinarith [cuspModulus_pos, h2]

/-- The phase-crossing family's cross-anchor product is non-negative when both
    anchors stay inside the small-excursion regime — same sign, no flip. -/
theorem phase_crossing_product_nonneg {a b qs q₁ q₂ : ℝ}
    (hq₁ : b ^ 2 * (q₁ - qs) ^ 2 ≤ a ^ 2) (hq₂ : b ^ 2 * (q₂ - qs) ^ 2 ≤ a ^ 2) :
    0 ≤ familyIm (a * (q₁ - qs)) (b * (q₁ - qs) ^ 2)
      * familyIm (a * (q₂ - qs)) (b * (q₂ - qs) ^ 2) :=
  mul_nonneg (phase_crossing_nonneg hq₁) (phase_crossing_nonneg hq₂)

/-- **F2 exclusion.** The minimal phase-crossing family cannot reproduce the
    sign flip near `q*`: with both anchors in the small-excursion regime the
    cross-anchor product is `≥ 0`, contradicting one positive and one negative
    anchor value. -/
theorem phase_crossing_family_excluded {a b qs q₁ q₂ : ℝ} (S : ℝ → ℝ)
    (hfam : ∀ q, S q = familyIm (a * (q - qs)) (b * (q - qs) ^ 2))
    (hq₁ : b ^ 2 * (q₁ - qs) ^ 2 ≤ a ^ 2) (hq₂ : b ^ 2 * (q₂ - qs) ^ 2 ≤ a ^ 2)
    (h₁ : 0 < S q₁) (h₂ : S q₂ < 0) : False := by
  rw [hfam q₁] at h₁
  rw [hfam q₂] at h₂
  have hprod := phase_crossing_product_nonneg hq₁ hq₂
  have hneg := mul_neg_of_pos_of_neg h₁ h₂
  linarith

/-! ## F3 — transverse-constant family: even in `d`, cannot sign-flip

This REPLACES the earlier `linear_family_sign_flip`/`linear_family_eq`/
`hasDerivAt_linear_family`, which claimed F3 sign-flips/survives — the CORE
ERROR of the `√3·x·y` form. Under the corrected harmonic form F3 is refuted. -/

/-- Within `(a·d)² < c₀²` the transverse-constant family value is NEGATIVE:
    `familyIm(a·d, c₀) = (√3/4)((a·d)² − c₀²) < 0`. Reuses
    `FigureEightComplexVolume.f3_re_linear_same_sign`. -/
theorem transverse_const_neg {a c₀ d : ℝ} (h : (a * d) ^ 2 < c₀ ^ 2) :
    familyIm (a * d) c₀ < 0 := by
  unfold familyIm
  exact f3_re_linear_same_sign (k := a) (d := d) (c₀ := c₀) h

/-- The transverse-constant family's cross-anchor product is POSITIVE when both
    anchors stay inside the small-excursion regime (both values negative) —
    same sign, no flip. -/
theorem transverse_const_product_nonneg {a c₀ qs q₁ q₂ : ℝ}
    (hq₁ : (a * (q₁ - qs)) ^ 2 < c₀ ^ 2) (hq₂ : (a * (q₂ - qs)) ^ 2 < c₀ ^ 2) :
    0 < familyIm (a * (q₁ - qs)) c₀ * familyIm (a * (q₂ - qs)) c₀ :=
  mul_pos_of_neg_of_neg (transverse_const_neg hq₁) (transverse_const_neg hq₂)

/-- **F3 exclusion (the #3773 survivor, refuted against the corrected form).**
    With both anchors in the small-excursion regime `(a·dᵢ)² < c₀²` both family
    values are negative (same sign), contradicting one positive and one negative
    anchor value: F3 CANNOT reproduce the measured `S(muon) > 0 > S(proton)`. -/
theorem transverse_const_family_excluded {a c₀ qs q₁ q₂ : ℝ} (S : ℝ → ℝ)
    (hfam : ∀ q, S q = familyIm (a * (q - qs)) c₀)
    (hq₁ : (a * (q₁ - qs)) ^ 2 < c₀ ^ 2) (hq₂ : (a * (q₂ - qs)) ^ 2 < c₀ ^ 2)
    (h₁ : 0 < S q₁) (h₂ : S q₂ < 0) : False := by
  rw [hfam q₁] at h₁
  rw [hfam q₂] at h₂
  have hprod := transverse_const_product_nonneg hq₁ hq₂
  have hneg := mul_neg_of_pos_of_neg h₁ h₂
  linarith

/-! ## Surviving necessary condition — the sign flip forces a diagonal crossing -/

/-- **The sign flip forces a diagonal crossing (surviving necessary
    condition).** If `familyIm` is positive at one substrate point and negative
    at another, the two `u`-values lie in OPPOSITE regions relative to the
    diagonal `|Re u| = |Im u|`: `|Im u₁| < |Re u₁|` but `|Re u₂| < |Im u₂|`. So
    any `u(q₀)` realizing the measured flip must CROSS that diagonal between the
    anchors. Via `FigureEightComplexVolume.signflip_forces_diagonal_cross`. -/
theorem signflip_requires_diagonal_cross {x₁ y₁ x₂ y₂ : ℝ}
    (h₁ : 0 < familyIm x₁ y₁) (h₂ : familyIm x₂ y₂ < 0) :
    y₁ ^ 2 < x₁ ^ 2 ∧ x₂ ^ 2 < y₂ ^ 2 :=
  signflip_forces_diagonal_cross (u₁ := ⟨x₁, y₁⟩) (u₂ := ⟨x₂, y₂⟩) h₁ h₂

/-- `familyIm` is even under simultaneous negation `(x, y) ↦ (-x, -y)`. -/
theorem familyIm_neg_both (x y : ℝ) :
    familyIm (-x) (-y) = familyIm x y := by
  rw [familyIm_eq, familyIm_eq]
  ring

/-- `familyIm` is antisymmetric under exchanging the real and imaginary parts
`(x, y) ↦ (y, x)`. -/
theorem familyIm_swap_antisymm (x y : ℝ) :
    familyIm y x = -familyIm x y := by
  rw [familyIm_eq, familyIm_eq]
  ring

/-- **Biconditional diagonal-crossing criterion.** A pair of deformation points
`(x₁, y₁)` and `(x₂, y₂)` has `familyIm x₁ y₁ > 0` and `familyIm x₂ y₂ < 0`
if and only if `(x₁, y₁)` lies in the real-dominant cone `y₁² < x₁²` and
`(x₂, y₂)` lies in the imaginary-dominant cone `x₂² < y₂²`. -/
theorem signflip_iff_diagonal_cross {x₁ y₁ x₂ y₂ : ℝ} :
    (0 < familyIm x₁ y₁ ∧ familyIm x₂ y₂ < 0) ↔
      (y₁ ^ 2 < x₁ ^ 2 ∧ x₂ ^ 2 < y₂ ^ 2) := by
  constructor
  · rintro ⟨h₁, h₂⟩
    exact signflip_requires_diagonal_cross h₁ h₂
  · rintro ⟨h₁, h₂⟩
    rw [familyIm_eq, familyIm_eq]
    have hc : 0 < cuspModulus := cuspModulus_pos
    exact ⟨by nlinarith, by nlinarith⟩

end QOU.QBeta.UDeformFamilyPruning
