import QOU.KZ.KZHalfMonodromy

/-!
# Asymptotic uniqueness at a normal-crossing corner

Pentagon groundwork (Step 1 of `docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md`).

Near a corner `{a = 0} ∩ {b = 0}` of a normal-crossing divisor, a solution of the two-variable
KZ system is normalised by its asymptotics `F(a, b) a^X b^Y` with `F` holomorphic and
`F(0, 0) = 1`. This file proves that such a normalisation determines the solution: if
`F₁ a^X b^Y = F₂ a^X b^Y K` on a small real quadrant, then `K = 1` (`corner_eq_one`).

* `gauge_const` — **one-variable step.** If `U` is holomorphic at `0` and, along the real
  segment `(0, δ)`, `U(t) = t^X C t^{−X}`, then `C = U(0)` and `[X, U(0)] = 0`, provided every
  indicial operator `Y ↦ kY − [X, Y]` (`k ≥ 1`) is injective. Proof: `g(z) = z U'(z) − [X, U(z)]`
  is holomorphic at `0` and vanishes on `(0, δ)` (differentiate `t^X C t^{−X}` along the real
  line), so by the identity theorem it vanishes near `0`; the constant `U(0)` solves the same
  gauge equation, and `eventuallyEq_of_gauge` gives `U = U(0)` near `0`.
* `corner_eq_one` — apply `gauge_const` in `a` for each small fixed `β`, to
  `U(a) = F₂(a, β)⁻¹ F₁(a, β)`, giving `F₂(0, β)⁻¹ F₁(0, β) = β^Y K β^{−Y}`; then apply it again
  in `b` to `V(b) = F₂(0, b)⁻¹ F₁(0, b)`, giving `K = V(0) = 1`.

No commutation hypothesis between `X` and `Y` is needed.

Base: complete normed `ℂ`-algebra (archimedean by necessity). Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md §2 Step 1
-/

namespace QOU.KZ.KZCorner
open Set Filter Topology QOU.KZ.FuchsianFormal QOU.KZ.KZComplex QOU.KZ.KZHalfMonodromy
variable {R : Type*} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]

theorem cpowA_mul_cpowA_neg (X : R) (z : ℂ) : cpowA X z * cpowA (-X) z = 1 := by
  unfold cpowA
  rw [← NormedSpace.exp_add_of_commute (((Commute.refl X).neg_right.smul_left _).smul_right _),
    smul_neg, add_neg_cancel, NormedSpace.exp_zero]

theorem cpowA_neg_mul_cpowA (X : R) (z : ℂ) : cpowA (-X) z * cpowA X z = 1 := by
  simpa using cpowA_mul_cpowA_neg (-X) z

omit [CompleteSpace R] in
theorem commute_cpowA {X Z : R} (h : Commute X Z) (z : ℂ) : Commute (cpowA X z) Z :=
  (h.smul_left _).exp_left ℂ

/-- `z ↦ z^X C z^{−X}` satisfies `z Φ' = [X, Φ]` on the slit plane. -/
theorem hasDerivAt_conj (X C : R) {z : ℂ} (hz : z ∈ Complex.slitPlane) :
    HasDerivAt (fun w => cpowA X w * C * cpowA (-X) w)
      (z⁻¹ • (X * (cpowA X z * C * cpowA (-X) z) - cpowA X z * C * cpowA (-X) z * X)) z := by
  have h := ((hasDerivAt_cpowA X hz).mul_const C).mul (hasDerivAt_cpowA (-X) hz)
  convert h using 1
  have hc : cpowA (-X) z * X = X * cpowA (-X) z := (commute_cpowA (Commute.refl X).neg_left z).eq
  rw [mul_assoc (cpowA X z * C), hc]
  simp only [sub_eq_add_neg, smul_add, smul_mul_assoc, mul_smul_comm, neg_mul, smul_neg,
    mul_neg, mul_assoc]

omit [CompleteSpace R] in
/-- Restriction of a complex derivative to the real line, for `R`-valued maps. -/
theorem hasDerivAt_comp_ofReal {e : ℂ → R} {e' : R} {t : ℝ} (h : HasDerivAt e e' t) :
    HasDerivAt (fun s : ℝ => e s) e' t := by
  have := (h.hasFDerivAt.restrictScalars ℝ).comp_hasDerivAt t
    (Complex.ofRealCLM.hasDerivAt (x := t))
  simpa using this

theorem ofReal_mem_ball {t ε : ℝ} (ht : 0 < t) (htε : t < ε) :
    (t : ℂ) ∈ Metric.ball (0 : ℂ) ε := by
  simp [abs_of_pos ht, htε]

theorem analyticAt_inverse_mul {f g : ℂ → R} {z : ℂ} (hf : AnalyticAt ℂ f z)
    (hg : AnalyticAt ℂ g z) (hu : IsUnit (f z)) :
    AnalyticAt ℂ (fun w => Ring.inverse (f w) * g w) z := by
  obtain ⟨u, hu⟩ := hu
  have : AnalyticAt ℂ Ring.inverse (f z) := hu ▸ analyticAt_inverse u
  exact (this.comp hf).mul hg

/-- **One-variable asymptotic uniqueness.** A germ `U` holomorphic at `0` which equals
`t^X C t^{−X}` along a real segment `(0, δ)` is the constant `C`, and `C` commutes with `X`. -/
theorem gauge_const {X : R} (hX : ∀ k : ℕ, 0 < k → Function.Injective (indicial X k))
    {U : ℂ → R} (hU : AnalyticAt ℂ U 0) {C : R} {δ : ℝ} (hδ : 0 < δ)
    (h : ∀ t : ℝ, 0 < t → t < δ → U t = cpowA X t * C * cpowA (-X) t) :
    C = U 0 ∧ Commute X (U 0) := by
  set g : ℂ → R := fun z => z • deriv U z - (X * U z - U z * X) with hg
  have hgan : AnalyticAt ℂ g 0 :=
    (analyticAt_id.smul hU.deriv).sub ((analyticAt_const.mul hU).sub (hU.mul analyticAt_const))
  obtain ⟨r, hr, hball⟩ := Metric.mem_nhds_iff.mp hU.eventually_analyticAt
  have hgt : ∀ t : ℝ, 0 < t → t < δ → t < r → g t = 0 := by
    intro t ht htδ htr
    have hslit : (t : ℂ) ∈ Complex.slitPlane := Complex.ofReal_mem_slitPlane.mpr ht
    have h1 := hasDerivAt_comp_ofReal (hasDerivAt_conj X C hslit)
    have hev : (fun s : ℝ => U s) =ᶠ[𝓝 t] fun s : ℝ => cpowA X s * C * cpowA (-X) s := by
      filter_upwards [Ioo_mem_nhds ht htδ] with s hs
      exact h s hs.1 hs.2
    have hUt : AnalyticAt ℂ U t := hball (ofReal_mem_ball ht htr)
    have h2 := hasDerivAt_comp_ofReal hUt.differentiableAt.hasDerivAt
    have hd := h2.unique (h1.congr_of_eventuallyEq hev)
    have ht0 : (t : ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr ht.ne'
    simp only [hg, hd, smul_smul, mul_inv_cancel₀ ht0, one_smul, h t ht htδ, sub_self]
  have hfreq : ∃ᶠ z in 𝓝[≠] (0 : ℂ), g z = 0 := by
    have hT : Tendsto (fun t : ℝ => (t : ℂ)) (𝓝[>] 0) (𝓝[≠] 0) := by
      apply tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within
      · have := (Complex.continuous_ofReal.tendsto (0 : ℝ)).mono_left
          (nhdsWithin_le_nhds (s := Ioi (0 : ℝ)))
        simpa using this
      · filter_upwards [self_mem_nhdsWithin] with t ht
        exact Complex.ofReal_ne_zero.mpr (ne_of_gt ht)
    apply hT.frequently
    apply Eventually.frequently
    filter_upwards [Ioo_mem_nhdsGT (lt_min hδ hr)] with t ht
    exact hgt t ht.1 (ht.2.trans_le (min_le_left _ _)) (ht.2.trans_le (min_le_right _ _))
  have hev0 : ∀ᶠ z in 𝓝 (0 : ℂ), g z = 0 := hgan.frequently_zero_iff_eventually_zero.mp hfreq
  have hKe : ∀ᶠ z in 𝓝 (0 : ℂ),
      z • deriv U z + U z * X = (fun _ : ℂ => X) z * U z := by
    filter_upwards [hev0] with z hz
    have e : z • deriv U z = X * U z - U z * X := sub_eq_zero.mp hz
    rw [e]; abel
  have hcomm : U 0 * X = X * U 0 := by simpa using hKe.self_of_nhds
  have hHe : ∀ᶠ z in 𝓝 (0 : ℂ),
      z • deriv (fun _ : ℂ => U 0) z + U 0 * X = (fun _ : ℂ => X) z * U 0 :=
    Eventually.of_forall fun z => by simp [hcomm]
  have hUe : U =ᶠ[𝓝 0] fun _ => U 0 :=
    eventuallyEq_of_gauge hX hU analyticAt_const continuousAt_const rfl hKe hHe rfl
  have hXU : Commute X (U 0) := hcomm.symm
  refine ⟨?_, hXU⟩
  obtain ⟨ε, hε, hεb⟩ := Metric.mem_nhds_iff.mp hUe
  set t : ℝ := min ε δ / 2 with htdef
  have ht : 0 < t := by positivity
  have htε : t < ε := by have := min_le_left ε δ; simp only [htdef]; linarith
  have htδ : t < δ := by have := min_le_right ε δ; simp only [htdef]; linarith
  have hU0t : U 0 = cpowA X t * C * cpowA (-X) t := (hεb (ofReal_mem_ball ht htε)).symm.trans
    (h t ht htδ)
  have hPU : Commute (cpowA X t) (U 0) := commute_cpowA hXU t
  have e1 := cpowA_neg_mul_cpowA X (t : ℂ)
  calc C = (cpowA (-X) t * cpowA X t) * C * (cpowA (-X) t * cpowA X t) := by
        rw [e1, one_mul, mul_one]
    _ = cpowA (-X) t * (cpowA X t * C * cpowA (-X) t) * cpowA X t := by simp only [mul_assoc]
    _ = cpowA (-X) t * cpowA X t * U 0 := by rw [← hU0t, mul_assoc, ← hPU.eq, ← mul_assoc]
    _ = U 0 := by rw [e1, one_mul]

/-- **Asymptotic uniqueness at a normal-crossing corner.** If two normalised germs
`F₁, F₂` (holomorphic in each variable at the corner, `F(0,0) = 1`) satisfy
`F₁(α,β) α^X β^Y = F₂(α,β) α^X β^Y K` on a real quadrant `(0, δ)²`, then `K = 1`. -/
theorem corner_eq_one {X Y : R}
    (hX : ∀ k : ℕ, 0 < k → Function.Injective (indicial X k))
    (hY : ∀ k : ℕ, 0 < k → Function.Injective (indicial Y k))
    {F₁ F₂ : ℂ → ℂ → R} {δ : ℝ} (hδ : 0 < δ)
    (h₁a : ∀ β : ℝ, 0 < β → β < δ → AnalyticAt ℂ (fun a => F₁ a β) 0)
    (h₂a : ∀ β : ℝ, 0 < β → β < δ → AnalyticAt ℂ (fun a => F₂ a β) 0)
    (h₁b : AnalyticAt ℂ (fun b => F₁ 0 b) 0) (h₂b : AnalyticAt ℂ (fun b => F₂ 0 b) 0)
    (h₁0 : F₁ 0 0 = 1) (h₂0 : F₂ 0 0 = 1) {K : R}
    (heq : ∀ α β : ℝ, 0 < α → α < δ → 0 < β → β < δ →
      F₁ α β * (cpowA X α * cpowA Y β) = F₂ α β * (cpowA X α * cpowA Y β) * K) :
    K = 1 := by
  have hunit_b : ∀ᶠ b in 𝓝 (0 : ℂ), IsUnit (F₂ 0 b) :=
    h₂b.continuousAt.preimage_mem_nhds (t := {x : R | IsUnit x}) (by rw [h₂0]; exact Units.isOpen.mem_nhds isUnit_one)
  obtain ⟨εb, hεb, hballb⟩ := Metric.mem_nhds_iff.mp hunit_b
  have hβ : ∀ β : ℝ, 0 < β → β < min δ εb →
      Ring.inverse (F₂ 0 β) * F₁ 0 β = cpowA Y β * K * cpowA (-Y) β := by
    intro β hβ hβ2
    have hβδ : β < δ := hβ2.trans_le (min_le_left _ _)
    have hu0 : IsUnit (F₂ 0 β) := hballb (ofReal_mem_ball hβ (hβ2.trans_le (min_le_right _ _)))
    have hunit_a : ∀ᶠ a in 𝓝 (0 : ℂ), IsUnit (F₂ a β) :=
      (h₂a β hβ hβδ).continuousAt.preimage_mem_nhds (t := {x : R | IsUnit x}) (Units.isOpen.mem_nhds hu0)
    obtain ⟨εa, hεa, hballa⟩ := Metric.mem_nhds_iff.mp hunit_a
    have hU := analyticAt_inverse_mul (h₂a β hβ hβδ) (h₁a β hβ hβδ) hu0
    have hg := gauge_const hX hU (lt_min hδ hεa) (C := cpowA Y β * K * cpowA (-Y) β) (by
      intro t ht htd
      have hut : IsUnit (F₂ t β) := hballa (ofReal_mem_ball ht (htd.trans_le (min_le_right _ _)))
      have e := heq t β ht (htd.trans_le (min_le_left _ _)) hβ hβδ
      have hPQ : cpowA X t * cpowA Y β * (cpowA (-Y) β * cpowA (-X) t) = 1 := by
        rw [mul_assoc, ← mul_assoc (cpowA Y β), cpowA_mul_cpowA_neg Y, one_mul,
          cpowA_mul_cpowA_neg X]
      show Ring.inverse (F₂ t β) * F₁ t β = _
      calc Ring.inverse (F₂ t β) * F₁ t β
          = Ring.inverse (F₂ t β) * (F₁ t β * (cpowA X t * cpowA Y β) *
              (cpowA (-Y) β * cpowA (-X) t)) := by rw [mul_assoc (F₁ t β), hPQ, mul_one]
        _ = Ring.inverse (F₂ t β) * (F₂ t β * (cpowA X t * cpowA Y β) * K *
              (cpowA (-Y) β * cpowA (-X) t)) := by rw [e]
        _ = (Ring.inverse (F₂ t β) * F₂ t β) *
              (cpowA X t * (cpowA Y β * K * cpowA (-Y) β) * cpowA (-X) t) := by
              simp only [mul_assoc]
        _ = cpowA X t * (cpowA Y β * K * cpowA (-Y) β) * cpowA (-X) t := by
              rw [Ring.inverse_mul_cancel _ hut, one_mul])
    exact hg.1.symm
  have hV := analyticAt_inverse_mul h₂b h₁b (by rw [h₂0]; exact isUnit_one)
  have hK := (gauge_const hY hV (lt_min hδ hεb) hβ).1
  simpa [h₁0, h₂0] using hK

end QOU.KZ.KZCorner
