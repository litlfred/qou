/-
  H4-2: the Fubini reduction — hyperbolic volume of a chimney collapses to a
  TWO-dimensional integral over its base.

  This is `qou-5gai` H4-2 / `qou-w3eg` H4-2, the step joining H3 (the region)
  to H4-1 (the vertical integral):

      hypVolume (chimney T R)  =  ∫⁻ (x,y) in T,  1 / (2(R² − x² − y²))

  for a base `T` inside the disk of radius `R`.  Milnor's computation is a
  two-dimensional integral over the base triangle; everything before H4-3 is
  the justification that one may pass from the solid to that base integral,
  and this file is that justification.

  THE TWO REAL STEPS, and both were flagged in `qou-w3eg` before being done.

  1. **The Pi/Prod split.**  H1's carrier is `Fin 3 → ℝ` (forced: only the Pi
     carrier carries `IsAddHaarMeasure`, which H2's dilation invariance needs),
     but Tonelli is stated for a product.  `splitEquiv` below is the bridge:
     `Fin 3 → ℝ ≃ᵐ ℝ × (ℝ × ℝ)`, height first, and it is measure-preserving
     because both halves are — `volume_preserving_piFinSuccAbove` splits one
     coordinate off the Pi, `volume_preserving_finTwoArrow` turns the remaining
     two into a pair.  The bean predicted this would be the cost of the Pi
     carrier; it is, and it is a one-definition cost, paid once here.

  2. **The `lintegral`/Bochner bridge.**  `hypVolume` is a `withDensity`
     measure, so its integrals are `ℝ≥0∞`-valued `∫⁻`; H4-1
     (`integral_Ioi_rpow_neg_three`) is a Bochner `∫`.  `fibreMass_eq`
     reconciles them through `ofReal_integral_eq_lintegral_ofReal`, which needs
     the integrand's honest integrability (`integrableOn_Ioi_rpow_of_lt`, valid
     exactly because the exponent `−3 < −1`) — i.e. the convergence H4-1
     established is what licenses the bridge, not a formality.

  WHY THE DISK HYPOTHESIS IS NOT COSMETIC.  `fibreMass_eq_top` proves the
  converse: over a base point ON or OUTSIDE the circle the chimney's floor
  degenerates to `z > 0` and the fibre carries INFINITE mass.  So
  `hypVolume_chimney_of_subset_disk`'s hypothesis is the exact boundary between
  a finite and an infinite answer, and is stated rather than assumed away.

  WHAT IS *NOT* HERE — read before citing.

  * **No triangle, no angles, no tetrahedron, no Λ.**  As in H3, `chimney` is
    over an ARBITRARY base.  H4-3 (evaluating the base integral over a triangle
    inscribed in the circle), H4-4 (the orthoscheme value `½Λ(θ)`) and H4-5
    (assembly into `Λ(α)+Λ(β)+Λ(γ)`) are open.  Nothing here says a chimney IS
    an ideal tetrahedron — that identification is Milnor's geometry and needs
    hyperbolic structure Mathlib does not have.
  * **The obtuse case is still untouched**, and is still the flagged place to
    go wrong: Milnor subdivides from the circumcentre only "if all three angles
    are acute", and otherwise a piece enters with a MINUS sign (`qou-w3eg`).
  * **H2 remains partial** — dilation and horizontal translation only; the
    Möbius/inversion half of `Isom(H³)` is not proved, so "hyperbolic volume"
    is still a name backed by two generators, not the full isometry group.
  * **Nothing wired.**  No mass, binding, or substrate claim.

  Archimedean (ℝ): Lebesgue measure, `sqrt`, ordering — §7c.

  -- Ref: [milnor1982] Appendix (the normalization and the base-integral route)
  -- Ref: [thurston1978] Ch. 7
  -- Ref: [leitner2026] beans qou-5gai (H4-2), qou-w3eg (H4-2), qou-idvt (T2)
-/

import QOU.Archimedean.IdealTetrahedronRegion
import Mathlib.MeasureTheory.Constructions.Pi
import Mathlib.MeasureTheory.Integral.Prod

namespace QOU.Archimedean.HyperbolicVolume

open MeasureTheory Set

/-! ### The Pi/Prod split

Tonelli is stated for a product measure; H1's carrier is `Fin 3 → ℝ`.  This is
the measure-preserving bridge, with the HEIGHT coordinate split off first so
that `lintegral_prod_symm` leaves the base integral outermost — the order
Milnor's computation uses. -/

/-- **`Fin 3 → ℝ ≃ᵐ ℝ × (ℝ × ℝ)`, height first.**  Splits coordinate `2` off
the Pi type, then pairs the remaining two. -/
noncomputable def splitEquiv : (Fin 3 → ℝ) ≃ᵐ ℝ × (ℝ × ℝ) :=
  (MeasurableEquiv.piFinSuccAbove (fun _ : Fin 3 => ℝ) 2).trans
    (MeasurableEquiv.prodCongr (MeasurableEquiv.refl ℝ) MeasurableEquiv.finTwoArrow)

@[simp] theorem splitEquiv_symm_apply_zero (z : ℝ) (w : ℝ × ℝ) :
    splitEquiv.symm (z, w) 0 = w.1 := rfl

@[simp] theorem splitEquiv_symm_apply_one (z : ℝ) (w : ℝ × ℝ) :
    splitEquiv.symm (z, w) 1 = w.2 := rfl

@[simp] theorem splitEquiv_symm_apply_two (z : ℝ) (w : ℝ × ℝ) :
    splitEquiv.symm (z, w) 2 = z := rfl

/-- The split is measure-preserving: Lebesgue on `Fin 3 → ℝ` goes to Lebesgue
on `ℝ × (ℝ × ℝ)`.  Both halves are standard. -/
theorem measurePreserving_splitEquiv :
    MeasurePreserving splitEquiv (volume : Measure (Fin 3 → ℝ))
      (volume : Measure (ℝ × (ℝ × ℝ))) :=
  (volume_preserving_piFinSuccAbove (fun _ : Fin 3 => ℝ) 2).trans
    ((MeasurePreserving.id volume).prod (volume_preserving_finTwoArrow ℝ))

/-! ### The vertical fibre mass

The `ℝ≥0∞` mass a single vertical fibre of a chimney carries.  `chimney_fibre`
(H3) is what says this ray IS the fibre; H4-1 is what evaluates it. -/

/-- **The hyperbolic mass of one vertical fibre** over the base point `w`, above
the radius-`R` hemisphere. -/
noncomputable def fibreMass (R : ℝ) (w : ℝ × ℝ) : ENNReal :=
  ∫⁻ z in Ioi (Real.sqrt (R ^ 2 - w.1 ^ 2 - w.2 ^ 2)), ENNReal.ofReal (1 / z ^ 3)

/-! ### H4-2a — Fubini

The reduction itself: three dimensions collapse to two.  No hypothesis on where
the base sits; both sides may be `⊤`. -/

/-- **H4-2a (Fubini) — a chimney's hyperbolic volume is the base integral of
its fibre masses.**

Unconditional: no assumption that the base lies inside the disk, so both sides
are permitted to be `⊤` (and by `fibreMass_eq_top` they are, as soon as the base
meets the exterior of the circle). -/
theorem hypVolume_chimney {T : Set (ℝ × ℝ)} (hT : MeasurableSet T) (R : ℝ) :
    hypVolume (chimney T R) = ∫⁻ w in T, fibreMass R w := by
  classical
  have hchim : MeasurableSet (chimney T R) := measurableSet_chimney hT R
  set F : (Fin 3 → ℝ) → ENNReal := (chimney T R).indicator hypDensity with hF_def
  have hF : Measurable F := measurable_hypDensity.indicator hchim
  have hFsplit : Measurable fun q : ℝ × (ℝ × ℝ) => F (splitEquiv.symm q) :=
    hF.comp splitEquiv.symm.measurable
  -- (1) the set integral as an indicator integral
  have step1 : hypVolume (chimney T R) = ∫⁻ p, F p ∂(volume : Measure (Fin 3 → ℝ)) := by
    rw [hypVolume_apply hchim, hF_def, lintegral_indicator hchim]
  -- (2) transport to split coordinates
  have step2 : ∫⁻ p, F p ∂(volume : Measure (Fin 3 → ℝ))
      = ∫⁻ q, F (splitEquiv.symm q) ∂(volume : Measure (ℝ × (ℝ × ℝ))) := by
    have h := measurePreserving_splitEquiv.lintegral_comp (f := fun q => F (splitEquiv.symm q))
      hFsplit
    simpa using h
  -- (3) Tonelli, base integral outermost
  have step3 : ∫⁻ q, F (splitEquiv.symm q) ∂(volume : Measure (ℝ × (ℝ × ℝ)))
      = ∫⁻ w, ∫⁻ z, F (splitEquiv.symm (z, w)) ∂(volume : Measure ℝ)
          ∂(volume : Measure (ℝ × ℝ)) := by
    have h := lintegral_prod_symm (μ := (volume : Measure ℝ)) (ν := (volume : Measure (ℝ × ℝ)))
      (fun q => F (splitEquiv.symm q)) hFsplit.aemeasurable
    rw [← Measure.volume_eq_prod] at h
    exact h
  -- (4) the inner integral is the fibre mass, cut off by the base
  have inner : ∀ w : ℝ × ℝ, ∫⁻ z, F (splitEquiv.symm (z, w)) ∂(volume : Measure ℝ)
      = T.indicator (fibreMass R) w := by
    intro w
    by_cases hw : w ∈ T
    · rw [Set.indicator_of_mem hw, fibreMass,
        ← lintegral_indicator (measurableSet_Ioi (a := Real.sqrt (R ^ 2 - w.1 ^ 2 - w.2 ^ 2)))]
      refine lintegral_congr fun z => ?_
      by_cases hz : Real.sqrt (R ^ 2 - w.1 ^ 2 - w.2 ^ 2) < z
      · rw [Set.indicator_of_mem (Set.mem_Ioi.mpr hz), hF_def,
          Set.indicator_of_mem (show splitEquiv.symm (z, w) ∈ chimney T R from
            ⟨by simpa using hw, by simpa using hz⟩)]
        simp [hypDensity]
      · rw [Set.indicator_of_notMem (by simpa using hz), hF_def, Set.indicator_of_notMem]
        rintro ⟨-, h⟩
        exact hz (by simpa using h)
    · rw [Set.indicator_of_notMem hw]
      have : ∀ z : ℝ, F (splitEquiv.symm (z, w)) = 0 := by
        intro z
        rw [hF_def, Set.indicator_of_notMem]
        rintro ⟨h, -⟩
        exact hw (by simpa using h)
      simp [this]
  rw [step1, step2, step3]
  simp only [inner]
  rw [lintegral_indicator hT]

/-! ### H4-2b — the `lintegral`/Bochner bridge

`hypVolume` integrates in `ℝ≥0∞`; H4-1 is a Bochner integral.  This is the
reconciliation, and it is where H4-1's convergence does real work: the bridge
lemma needs genuine integrability, which holds exactly because the exponent
`−3` is `< −1`. -/

/-- **H4-2b — the fibre mass over a base point strictly inside the circle.**

`∫_{√(R²−d²)}^{∞} dz/z³ = 1/(2(R²−d²))`, now as an `ℝ≥0∞` mass.  This is H4-1's
value, transported across the `∫⁻`/`∫` boundary. -/
theorem fibreMass_eq {R : ℝ} {w : ℝ × ℝ} (hw : w.1 ^ 2 + w.2 ^ 2 < R ^ 2) :
    fibreMass R w = ENNReal.ofReal (1 / (2 * (R ^ 2 - w.1 ^ 2 - w.2 ^ 2))) := by
  have hpos : 0 < R ^ 2 - w.1 ^ 2 - w.2 ^ 2 := by linarith
  have hz₀ : 0 < Real.sqrt (R ^ 2 - w.1 ^ 2 - w.2 ^ 2) := Real.sqrt_pos.mpr hpos
  set z₀ := Real.sqrt (R ^ 2 - w.1 ^ 2 - w.2 ^ 2) with hz₀def
  -- rewrite the integrand as an rpow, valid because every `z > z₀ > 0` is positive
  have hcongr : fibreMass R w = ∫⁻ z in Ioi z₀, ENNReal.ofReal (z ^ (-3 : ℝ)) := by
    rw [fibreMass, ← hz₀def]
    refine setLIntegral_congr_fun measurableSet_Ioi fun z hz => ?_
    have hzpos : 0 < z := lt_trans hz₀ hz
    rw [Real.rpow_neg hzpos.le, show (3 : ℝ) = ((3 : ℕ) : ℝ) by norm_num,
      Real.rpow_natCast, one_div]
  rw [hcongr]
  -- the Bochner integral is honestly integrable, so `ofReal` commutes with it
  have hint : IntegrableOn (fun z : ℝ => z ^ (-3 : ℝ)) (Ioi z₀) volume :=
    integrableOn_Ioi_rpow_of_lt (by norm_num) hz₀
  have hnonneg : (0 : ℝ → ℝ) ≤ᵐ[volume.restrict (Ioi z₀)] fun z : ℝ => z ^ (-3 : ℝ) := by
    filter_upwards [ae_restrict_mem measurableSet_Ioi] with z hz
    exact Real.rpow_nonneg (lt_trans hz₀ hz).le _
  rw [← ofReal_integral_eq_lintegral_ofReal hint hnonneg, integral_Ioi_rpow_neg_three hz₀,
    hz₀def, Real.sq_sqrt hpos.le]

/-! ### The disk hypothesis is the exact finiteness boundary -/

/-- **Off the open disk the fibre carries infinite mass.**

`Real.sqrt` of a non-positive number is `0`, so the chimney's floor degenerates
to `z > 0` and `∫_0^∞ dz/z³` diverges.  Proved rather than asserted, because it
is what makes `hypVolume_chimney_of_subset_disk`'s hypothesis the exact
boundary between a finite and an infinite volume, not a convenience. -/
theorem fibreMass_eq_top {R : ℝ} {w : ℝ × ℝ} (hw : R ^ 2 ≤ w.1 ^ 2 + w.2 ^ 2) :
    fibreMass R w = ⊤ := by
  have hfloor : Real.sqrt (R ^ 2 - w.1 ^ 2 - w.2 ^ 2) = 0 :=
    Real.sqrt_eq_zero_of_nonpos (by linarith)
  rw [fibreMass, hfloor]
  refine ENNReal.eq_top_of_forall_nnreal_le fun r => ?_
  -- the tail from any `ε > 0` already has mass `1/(2ε²)`; take `ε = 1/(1+r)`
  set ε : ℝ := 1 / (1 + (r : ℝ)) with hε
  have hrnn : (0 : ℝ) ≤ (r : ℝ) := r.coe_nonneg
  have hεpos : 0 < ε := by rw [hε]; positivity
  have hmono : ∫⁻ z in Ioi ε, ENNReal.ofReal (1 / z ^ 3)
      ≤ ∫⁻ z in Ioi (0 : ℝ), ENNReal.ofReal (1 / z ^ 3) :=
    lintegral_mono_set (Ioi_subset_Ioi hεpos.le)
  -- evaluate the tail exactly, by the same bridge as `fibreMass_eq`
  have htail : ∫⁻ z in Ioi ε, ENNReal.ofReal (1 / z ^ 3)
      = ENNReal.ofReal (1 / (2 * ε ^ 2)) := by
    have hcongr : ∫⁻ z in Ioi ε, ENNReal.ofReal (1 / z ^ 3)
        = ∫⁻ z in Ioi ε, ENNReal.ofReal (z ^ (-3 : ℝ)) := by
      refine setLIntegral_congr_fun measurableSet_Ioi fun z hz => ?_
      have hzpos : 0 < z := lt_trans hεpos hz
      rw [Real.rpow_neg hzpos.le, show (3 : ℝ) = ((3 : ℕ) : ℝ) by norm_num,
        Real.rpow_natCast, one_div]
    have hint : IntegrableOn (fun z : ℝ => z ^ (-3 : ℝ)) (Ioi ε) volume :=
      integrableOn_Ioi_rpow_of_lt (by norm_num) hεpos
    have hnonneg : (0 : ℝ → ℝ) ≤ᵐ[volume.restrict (Ioi ε)] fun z : ℝ => z ^ (-3 : ℝ) := by
      filter_upwards [ae_restrict_mem measurableSet_Ioi] with z hz
      exact Real.rpow_nonneg (lt_trans hεpos hz).le _
    rw [hcongr, ← ofReal_integral_eq_lintegral_ofReal hint hnonneg,
      integral_Ioi_rpow_neg_three hεpos]
  -- and `1/(2ε²) = (1+r)²/2 ≥ r`
  have hval : (r : ℝ) ≤ 1 / (2 * ε ^ 2) := by
    have h1 : ε ^ 2 = 1 / (1 + (r : ℝ)) ^ 2 := by rw [hε, div_pow, one_pow]
    have hden : (0 : ℝ) < (1 + (r : ℝ)) ^ 2 := by positivity
    rw [h1]
    rw [show 2 * (1 / (1 + (r : ℝ)) ^ 2) = 2 / (1 + (r : ℝ)) ^ 2 by ring,
      one_div_div]
    rw [le_div_iff₀ (by norm_num : (0:ℝ) < 2)]
    nlinarith [sq_nonneg ((r : ℝ) - 1), sq_nonneg (r : ℝ)]
  calc (r : ENNReal) = ENNReal.ofReal (r : ℝ) := by
        simp [ENNReal.ofReal_coe_nnreal]
    _ ≤ ENNReal.ofReal (1 / (2 * ε ^ 2)) := ENNReal.ofReal_le_ofReal hval
    _ = ∫⁻ z in Ioi ε, ENNReal.ofReal (1 / z ^ 3) := htail.symm
    _ ≤ ∫⁻ z in Ioi (0 : ℝ), ENNReal.ofReal (1 / z ^ 3) := hmono

/-! ### H4-2 assembled

The statement H4-3 consumes: over a base inside the disk, the three-dimensional
hyperbolic volume IS Milnor's two-dimensional base integral. -/

/-- **H4-2 — the Fubini reduction, in the form H4-3 will consume.**

    Vol(chimney T R)  =  ∫∫_T  dA / (2(R² − x² − y²)).

The hypothesis is **almost-everywhere**, and that is not a technical
generalisation — it is what makes the statement applicable at all.  Milnor's
base triangle is *inscribed* in the circle, so its three VERTICES lie exactly
ON it, where `R² − x² − y² = 0` and the fibre mass is `⊤` (`fibreMass_eq_top`).
A pointwise `∀ w ∈ T` hypothesis would therefore exclude the closed triangle —
precisely the case H4-3 needs.  The vertices are a null set, so a.e. is both
sufficient and honest. -/
theorem hypVolume_chimney_of_ae_lt {T : Set (ℝ × ℝ)} (hT : MeasurableSet T) {R : ℝ}
    (hTR : ∀ᵐ w ∂(volume.restrict T), w.1 ^ 2 + w.2 ^ 2 < R ^ 2) :
    hypVolume (chimney T R)
      = ∫⁻ w in T, ENNReal.ofReal (1 / (2 * (R ^ 2 - w.1 ^ 2 - w.2 ^ 2))) := by
  rw [hypVolume_chimney hT R]
  refine lintegral_congr_ae ?_
  filter_upwards [hTR] with w hw using fibreMass_eq hw

/-- The pointwise corollary, for a base in the OPEN disk. -/
theorem hypVolume_chimney_of_subset_disk {T : Set (ℝ × ℝ)} (hT : MeasurableSet T) {R : ℝ}
    (hTR : ∀ w ∈ T, w.1 ^ 2 + w.2 ^ 2 < R ^ 2) :
    hypVolume (chimney T R)
      = ∫⁻ w in T, ENNReal.ofReal (1 / (2 * (R ^ 2 - w.1 ^ 2 - w.2 ^ 2))) := by
  rw [hypVolume_chimney hT R]
  exact setLIntegral_congr_fun hT fun w hw => fibreMass_eq (hTR w hw)

end QOU.Archimedean.HyperbolicVolume
