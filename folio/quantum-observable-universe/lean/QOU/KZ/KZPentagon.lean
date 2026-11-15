import QOU.KZ.KZEdge

/-!
# The pentagon for the four-point KZ system

Gluing the five edge solutions of `KZEdge` around the boundary of `Δ`. At a corner where the
divisor of one chart meets the divisor of the next, the two normalised solutions
`N b = F G₁` and `N a = F G₀` differ by a constant `K = a⁻¹ b`, and asymptotic uniqueness at the
normal crossing (`KZCorner.corner_eq_one`) forces `K = 1` (`corner_glue`).

Each edge gives `a = b Φ(P, Q)` (`edge_assoc`) and each corner gives `b_{i-1} = a_i`
(`corner_step`), so going once round the boundary yields `a₁ = a₁ Φ₅Φ₄Φ₃Φ₂Φ₁` and, `a₁` being a
unit, the pentagon identity (`pentagon`):

  `Φ(T₂₃₄, t₁₂) Φ(t₂₃, t₃₄) Φ(T₁₂₃, T₂₃₄) Φ(t₁₂, t₂₃) Φ(t₃₄, T₁₂₃) = 1`.

-- Ref: [drinfeld1990] Leningrad Math. J. 1 (1990) 1419–1457, §2
-- Ref: [leitner2026] docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md §2 Step 1
-/

namespace QOU.KZ.KZPentagon

open Set Filter Topology QOU.KZ.FuchsianFormal QOU.KZ.FuchsianAnalytic QOU.KZ.KZComplex
  QOU.KZ.FuchsianParam QOU.KZ.KZ4 QOU.KZ.KZCorner QOU.KZ.KZEdge

variable {R : Type*} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]

/-! ### Helpers -/

omit [CompleteSpace R] in
theorem commute_cseries {c : R} {H : ℕ → R} (h : ∀ k, Commute c (H k)) (z : ℂ) :
    Commute c (cseries H z) := by
  unfold cseries
  by_cases hs : Summable fun k => z ^ k • H k
  · change c * _ = _ * c
    rw [← hs.tsum_mul_left, ← hs.tsum_mul_right]
    congr 1; funext k
    rw [mul_smul_comm, smul_mul_assoc, (h k).eq]
  · rw [tsum_eq_zero_of_not_summable hs]; exact Commute.zero_right c

theorem analyticAt_cseries {H : ℕ → R} {r : ℝ} (hb : BoundedOn H r) {z : ℂ} (hz : ‖z‖ < r) :
    AnalyticAt ℂ (cseries H) z := by
  have hd : DifferentiableOn ℂ (cseries H) (Metric.ball 0 r) := fun w hw =>
    (hasDerivAt_cseries hb (by simpa using hw)).differentiableAt.differentiableWithinAt
  exact hd.analyticAt (Metric.isOpen_ball.mem_nhds (by simpa using hz))

theorem analyticAt_cpowA (X : R) {z : ℂ} (hz : z ∈ Complex.slitPlane) :
    AnalyticAt ℂ (cpowA X) z := by
  have hd : DifferentiableOn ℂ (cpowA X) Complex.slitPlane := fun w hw =>
    (hasDerivAt_cpowA X hw).differentiableAt.differentiableWithinAt
  exact hd.analyticAt (Complex.isOpen_slitPlane.mem_nhds hz)

omit [CompleteSpace R] in
theorem cpowA_one (X : R) : cpowA X 1 = 1 := by simp [cpowA]

theorem cpowA_mul_ofReal (X : R) {a b : ℝ} (ha : 0 < a) (hb : 0 < b) :
    cpowA X ((a : ℂ) * b) = cpowA X a * cpowA X b := by
  rw [← Complex.ofReal_mul, KZHexagon.cpowA_ofReal X (mul_pos ha hb), KZHexagon.cpowA_ofReal X ha,
    KZHexagon.cpowA_ofReal X hb]
  unfold tpow
  rw [Real.log_mul ha.ne' hb.ne', add_smul,
    NormedSpace.exp_add_of_commute (((Commute.refl X).smul_left _).smul_right _)]

omit [CompleteSpace R] in
theorem H_zero (E A B : R) (hE : NonResonant E) (s : ℂ) : H E A B hE s 0 = 1 :=
  hpar_zero E hE (Mt A B) s

theorem analyticAt_H_e (E A B : R) (hE : NonResonant E) {s : ℂ} (hs : s ∈ U) :
    AnalyticAt ℂ (fun e => H E A B hE s e) 0 :=
  analyticAt_hpar E hE (Mt A B) (hC A B) (by norm_num) (by norm_num) hθ (hMb A B) hs

theorem analyticAt_H_s (E A B : R) (hE : NonResonant E) {s e : ℂ} (hs : s ∈ U)
    (he : ‖e‖ < 9 / 10) : AnalyticAt ℂ (fun w => H E A B hE w e) s :=
  (hasDerivAt_hpar_param E hE (Mt A B) isOpen_U (fun j _ => differentiableOn_Mt A B j) (hC A B)
    (by norm_num) (by norm_num) hθ (hMb A B) he).1.analyticAt (isOpen_U.mem_nhds hs)

theorem zero_mem_U : (0 : ℂ) ∈ U := by simpa using ofReal_mem_U (s := 0) (by simp)

/-! ### Gluing at a corner -/

/-- The chart-`i` edge coordinate `s = α(1−β)/(1−αβ)` of the corner point. -/
noncomputable def σc (a b : ℂ) : ℂ := a * (1 - b) / (1 - a * b)

/-- The factor `w = (1−β)/(1−αβ)`, so that `σ = α w`. -/
noncomputable def wc (a b : ℂ) : ℂ := (1 - b) / (1 - a * b)

/-- **Gluing at a corner.** The previous chart has `ε`-residue `X` and the next `ε`-residue `Y`,
with `X` the next chart's `s`-residue at `0` and `Y` the previous chart's `s`-residue at `1`.
If along the corner the reference `N` satisfies `N b = F' G₁'` and `N a = F G₀` (with the
three-point series `H₁` of the previous chart and `H₀` of the next), then `b = a`. -/
theorem corner_glue {X Y A' B' A B : R} (hX : NonResonant X) (hY : NonResonant Y)
    (hXY : Commute X Y) {H₁ H₀ : ℕ → R} (hb₁ : BoundedOn H₁ 1) (hb₀ : BoundedOn H₀ 1)
    (h₁0 : H₁ 0 = 1) (h₀0 : H₀ 0 = 1) (hc₁ : ∀ k, Commute X (H₁ k))
    (hc₀ : ∀ k, Commute Y (H₀ k)) {a b : R} (ha : IsUnit a) {Npt : ℝ → ℝ → R} {δ : ℝ}
    (hδ : 0 < δ)
    (hbeq : ∀ α β : ℝ, 0 < α → α < δ → 0 < β → β < δ →
      Npt α β * b = F X A' B' hX (1 - β) α * (cseries H₁ β * cpowA Y β))
    (haeq : ∀ α β : ℝ, 0 < α → α < δ → 0 < β → β < δ →
      Npt α β * a = F Y A B hY (σc α β) β * (cseries H₀ (σc α β) * cpowA X (σc α β))) :
    b = a := by
  set δ' : ℝ := min δ (1 / 2) with hδ'
  have hδ'0 : 0 < δ' := lt_min hδ (by norm_num)
  have hδ'1 : δ' ≤ δ := min_le_left _ _
  have hδ'2 : δ' ≤ 1 / 2 := min_le_right _ _
  set F₁ : ℂ → ℂ → R := fun a b => H X A' B' hX (1 - b) a * cseries H₁ b with hF₁
  set F₂ : ℂ → ℂ → R := fun a b =>
    H Y A B hY (σc a b) b * cseries H₀ (σc a b) * cpowA X (wc a b) with hF₂
  set K : R := Ring.inverse a * b with hK
  have hσ0 : ∀ b : ℂ, σc 0 b = 0 := fun b => by simp [σc]
  have hw0 : ∀ b : ℂ, wc 0 b = 1 - b := fun b => by simp [wc]
  have hU1 : ∀ β : ℝ, 0 ≤ β → β ≤ 1 → (1 : ℂ) - β ∈ U := fun β h0 h1 => by
    simpa using ofReal_mem_U (s := 1 - β) ⟨by linarith, by linarith⟩
  have hK1 : K = 1 := by
    refine corner_eq_one (fun k hk => (hX k hk).1) (fun k hk => (hY k hk).1) hδ'0
      (F₁ := F₁) (F₂ := F₂) ?_ ?_ ?_ ?_ ?_ ?_ ?_
    · -- analytic in `α`, previous chart
      intro β hβ hβδ
      exact (analyticAt_H_e X A' B' hX (hU1 β hβ.le (by linarith))).mul analyticAt_const
    · -- analytic in `α`, next chart
      intro β hβ hβδ
      have hβn : ‖(β : ℂ)‖ < 9 / 10 := by
        rw [Complex.norm_real, Real.norm_of_nonneg hβ.le]; linarith
      have hσa : AnalyticAt ℂ (fun a => σc a β) 0 :=
        (analyticAt_id.mul analyticAt_const).div
          (analyticAt_const.sub (analyticAt_id.mul analyticAt_const)) (by simp)
      have hwa : AnalyticAt ℂ (fun a => wc a β) 0 :=
        analyticAt_const.div (analyticAt_const.sub (analyticAt_id.mul analyticAt_const))
          (by simp)
      have hslit : wc 0 β ∈ Complex.slitPlane := by
        rw [hw0, show (1 : ℂ) - β = ((1 - β : ℝ) : ℂ) by push_cast; ring]
        exact Complex.ofReal_mem_slitPlane.2 (by linarith)
      refine ((AnalyticAt.comp_of_eq' (analyticAt_H_s Y A B hY zero_mem_U hβn) hσa
        (hσ0 β)).mul (AnalyticAt.comp_of_eq' (analyticAt_cseries hb₀ (z := 0) (by simp)) hσa
        (hσ0 β))).mul (AnalyticAt.comp_of_eq' (analyticAt_cpowA X hslit) hwa rfl)
    · -- analytic in `β` at `α = 0`, previous chart
      simp only [hF₁, H_zero, one_mul]
      exact analyticAt_cseries hb₁ (by simp)
    · -- analytic in `β` at `α = 0`, next chart
      simp only [hF₂, hσ0, hw0, KZHalfMonodromy.cseries_zero, h₀0, mul_one]
      exact (analyticAt_H_e Y A B hY zero_mem_U).mul
        (AnalyticAt.comp_of_eq' (analyticAt_cpowA X (z := 1) Complex.one_mem_slitPlane)
          (analyticAt_const.sub analyticAt_id) (by simp))
    · simp [hF₁, H_zero, KZHalfMonodromy.cseries_zero, h₁0]
    · simp [hF₂, hσ0, hw0, H_zero, KZHalfMonodromy.cseries_zero, h₀0, cpowA_one]
    · intro α β hα hαδ hβ hβδ
      have hαδ1 : α < δ := hαδ.trans_le hδ'1
      have hβδ1 : β < δ := hβδ.trans_le hδ'1
      have hαβ : α * β < 1 := by nlinarith
      have hwpos : 0 < (1 - β) / (1 - α * β) := div_pos (by linarith) (by linarith)
      have hσw : σc α β = (α : ℂ) * (((1 - β) / (1 - α * β) : ℝ) : ℂ) := by
        simp only [σc]; push_cast; ring
      have hwr : wc α β = (((1 - β) / (1 - α * β) : ℝ) : ℂ) := by
        simp only [wc]; push_cast; ring
      have e1 := hbeq α β hα hαδ1 hβ hβδ1
      have e2 := haeq α β hα hαδ1 hβ hβδ1
      rw [hσw, cpowA_mul_ofReal X hα hwpos, ← hσw] at e2
      have hb' : Npt α β * b = Npt α β * a * K := by
        rw [hK, mul_assoc, ← mul_assoc a, Ring.mul_inverse_cancel _ ha, one_mul]
      have hS₁ : Commute (cpowA X α) (cseries H₁ β) :=
        commute_cpowA (commute_cseries hc₁ β) α
      have hS₀ : Commute (cpowA Y β) (cseries H₀ (σc α β)) :=
        commute_cpowA (commute_cseries hc₀ _) β
      have hXYc : Commute (cpowA Y β) (cpowA X α) :=
        commute_cpowA (commute_cpowA hXY α).symm β
      have hXwY : Commute (cpowA Y β) (cpowA X (wc α β)) :=
        commute_cpowA (commute_cpowA hXY _).symm β
      have hXwX : Commute (cpowA X α) (cpowA X (wc α β)) :=
        commute_cpowA (commute_cpowA (Commute.refl X) _).symm α
      have L : F₁ α β * (cpowA X α * cpowA Y β) = Npt α β * b := by
        rw [e1]; simp only [hF₁, F]
        rw [show (1 : ℂ) - β = ((1 - β : ℝ) : ℂ) by push_cast; ring]
        simp only [mul_assoc]; rw [← mul_assoc (cpowA X α), hS₁.eq]; simp only [mul_assoc]
      have Rr : F₂ α β * (cpowA X α * cpowA Y β) = Npt α β * a := by
        rw [e2]; simp only [hF₂, F, ← hwr]
        simp only [mul_assoc]
        rw [← mul_assoc (cpowA Y β) (cseries H₀ _), hS₀.eq, mul_assoc (cseries H₀ _),
          ← mul_assoc (cpowA Y β) (cpowA X α), hXYc.eq, mul_assoc (cpowA X α),
          hXwY.eq, ← mul_assoc (cpowA X α), hXwX.eq]
        simp only [mul_assoc]
      rw [L, Rr, hb']
  calc b = a * K := by rw [hK, ← mul_assoc, Ring.mul_inverse_cancel _ ha, one_mul]
    _ = a := by rw [hK1, mul_one]

/-! ### Edge solutions with the three-point normalisations -/

/-- The normalised formal solution of the three-point KZ system at `0` (residues `P, Q`). -/
noncomputable def H0 (P Q : R) (hP : NonResonant P) : ℕ → R := formalSol (kzM0 P Q) hP

omit [NormedAlgebra ℂ R] [CompleteSpace R] in
theorem H0_zero (P Q : R) (hP : NonResonant P) : H0 P Q hP 0 = 1 := formalSol_zero _ _

omit [NormedAlgebra ℂ R] [CompleteSpace R] in
theorem H0_gauge (P Q : R) (hP : NonResonant P) : IsFormalGauge (kzM0 P Q) (H0 P Q hP) :=
  formalSol_isFormalGauge _ _

omit [CompleteSpace R] in
theorem boundedOn_H0 (P Q : R) (hP : NonResonant P) : BoundedOn (H0 P Q hP) 1 :=
  boundedOn_kz_solution P Q _ (H0_zero P Q hP) (H0_gauge P Q hP)

omit [NormedAlgebra ℂ R] [CompleteSpace R] in
theorem commute_H0 {c P Q : R} (hP : NonResonant P) (hcP : Commute c P) (hcQ : Commute c Q)
    (k : ℕ) : Commute c (H0 P Q hP k) := by
  refine commute_formalSol _ _ c (fun j => ?_) k
  rcases j with _ | j
  · exact hcP
  · exact hcQ.neg_right

/-- The KZ associator `Φ_KZ(P, Q)` built from the normalised formal solutions. -/
noncomputable def Φ (P Q : R) (hP : NonResonant P) (hQ : NonResonant Q) : R :=
  AssociatorKZ.phiKZ P Q (H0 P Q hP) (H0 Q P hQ) (H0_zero P Q hP) (H0_gauge P Q hP)
    (H0_zero Q P hQ) (H0_gauge Q P hQ)

variable {t : Res R}

/-- **The edge theorem with the three-point normalisations.** For an edge chart and a reference
solution `N` on `Δ`, there are constants `a` (a unit) and `b` with `a = b Φ_KZ(P, Q)`,
`N a = F G₀` and `N b = F G₁` along the edge. -/
theorem edge_assoc (ch : Chart t) (hE : NonResonant ch.E) (hP : NonResonant ch.P)
    (hQ : NonResonant ch.Q) (hEP : Commute ch.E ch.P) (hEQ : Commute ch.E ch.Q)
    {N : ℝ × ℝ → R}
    (hN : ∀ p ∈ Δ, HasFDerivAt N ((ContinuousLinearMap.mul ℝ R).flip (N p) ∘L
      Flat2D.form t.Ωx t.Ωy p) p)
    (hNu : ∀ p ∈ Δ, IsUnit (N p)) :
    ∃ δ > 0, δ < 1 ∧ ∃ a b : R, IsUnit a ∧ a = b * Φ ch.P ch.Q hP hQ ∧
      ∀ s ∈ Ioo (0 : ℝ) 1, ∀ ε ∈ Ioo (0 : ℝ) δ,
        N (ch.ψ (s, ε)) * a = F ch.E ch.A ch.B hE s ε * KZComplex.G₀ ch.P (H0 ch.P ch.Q hP) s ∧
        N (ch.ψ (s, ε)) * b = F ch.E ch.A ch.B hE s ε * KZComplex.G₁ ch.Q (H0 ch.Q ch.P hQ) s := by
  have hsol : Flat2D.IsSol2 (fun q => Ωs ch.P ch.Q ch.B q.1 q.2) (fun q => Ωe ch.E ch.A ch.B q.1 q.2)
      (N ∘ ch.ψ) sq :=
    Flat2D.isSol2_comp_of_eq hN ch.maps ch.da ch.db (fun q hq => (ch.pa q hq).symm)
      (fun q hq => (ch.pb q hq).symm)
  obtain ⟨δ, hδ, hδ1, c, hcu, hFN, hG⟩ := edge ch.P ch.Q ch.E ch.A ch.B hE hEP hEQ hsol
    (fun q hq => hNu _ (ch.maps q hq))
  set H₀ := H0 ch.P ch.Q hP
  set H₁ := H0 ch.Q ch.P hQ
  obtain ⟨a, ha⟩ := hG _ (AssociatorKZ.isKZSol_G₀ ch.P ch.Q H₀ (H0_zero _ _ _) (H0_gauge _ _ _))
  obtain ⟨b, hb⟩ := hG _ (AssociatorKZ.isKZSol_G₁ ch.P ch.Q H₁ (H0_zero _ _ _) (H0_gauge _ _ _))
  have hspec := AssociatorKZ.phiKZ_spec ch.P ch.Q H₀ H₁ (H0_zero _ _ _) (H0_gauge _ _ _)
    (H0_zero _ _ _) (H0_gauge _ _ _)
  have h12 : (1 / 2 : ℝ) ∈ Ioo (0 : ℝ) 1 := ⟨by norm_num, by norm_num⟩
  have hab : a = b * Φ ch.P ch.Q hP hQ := by
    rw [← ha _ h12, ← hb _ h12, hspec.2 _ h12, ← mul_assoc]; rfl
  have hau : IsUnit a := by
    obtain ⟨δ₀, hδ₀, hδ₀1, hu⟩ := AssociatorKZ.exists_isUnit_series (boundedOn_H0 ch.P ch.Q hP)
      (H0_zero _ _ _)
    have hs : δ₀ / 2 ∈ Ioo (0 : ℝ) 1 := ⟨by positivity, by linarith⟩
    rw [← ha _ hs]
    exact (hcu _ hs).mul ((hu _ ⟨by positivity, by linarith⟩).mul (AssociatorKZ.isUnit_tpow _ _))
  refine ⟨δ, hδ, hδ1, a, b, hau, hab, fun s hs ε hε => ⟨?_, ?_⟩⟩
  · rw [KZHexagon.G₀_ofReal _ _ hs.1, hFN s hs ε hε, mul_assoc, ha s hs]; rfl
  · rw [KZHexagon.G₁_ofReal _ _ hs.2, hFN s hs ε hε, mul_assoc, hb s hs]; rfl

/-! ### One corner -/

/-- **One corner of the pentagon.** The previous chart has `ε`-residue `X` and `s`-residue `Y`
at `1`; the next has `ε`-residue `Y` and `s`-residue `X` at `0`; the two charts agree at the
corner, `ψ'(1−β, α) = ψ(α(1−β)/(1−αβ), β)`. Then the previous chart's `b` equals the next
chart's `a`. -/
theorem corner_step {X Y P' A' B' Q A B : R} (hX : NonResonant X) (hY : NonResonant Y)
    (hXY : Commute X Y) (hXP' : Commute X P') (hYQ : Commute Y Q)
    {ψ' ψ : ℝ × ℝ → ℝ × ℝ}
    (hψ : ∀ α β : ℝ, 0 < α → α < 1 → 0 < β → β < 1 →
      ψ' (1 - β, α) = ψ (α * (1 - β) / (1 - α * β), β))
    {N : ℝ × ℝ → R} {δ' δ : ℝ} (hδ'0 : 0 < δ') (hδ'1 : δ' < 1) (hδ0 : 0 < δ) (hδ1 : δ < 1)
    {b' a : R} (ha : IsUnit a)
    (h' : ∀ s ∈ Ioo (0 : ℝ) 1, ∀ ε ∈ Ioo (0 : ℝ) δ',
      N (ψ' (s, ε)) * b' = F X A' B' hX s ε * KZComplex.G₁ Y (H0 Y P' hY) s)
    (h : ∀ s ∈ Ioo (0 : ℝ) 1, ∀ ε ∈ Ioo (0 : ℝ) δ,
      N (ψ (s, ε)) * a = F Y A B hY s ε * KZComplex.G₀ X (H0 X Q hX) s) :
    b' = a := by
  have hm0 : 0 < min δ' δ := lt_min hδ'0 hδ0
  refine corner_glue (A' := A') (B' := B') (A := A) (B := B) hX hY hXY (boundedOn_H0 Y P' hY) (boundedOn_H0 X Q hX) (H0_zero _ _ _)
    (H0_zero _ _ _) (commute_H0 hY hXY hXP') (commute_H0 hX hXY.symm hYQ) ha
    (Npt := fun α β => N (ψ (α * (1 - β) / (1 - α * β), β))) hm0 ?_ ?_
  · intro α β hα hαδ hβ hβδ
    have hαδ' : α < δ' := hαδ.trans_le (min_le_left _ _)
    have hβ1 : β < 1 := (hβδ.trans_le (min_le_right _ _)).trans hδ1
    simp only
    rw [← hψ α β hα (hαδ'.trans hδ'1) hβ hβ1, h' (1 - β) ⟨by linarith, by linarith⟩ α ⟨hα, hαδ'⟩]
    simp only [KZComplex.G₁]
    push_cast
    rw [sub_sub_cancel]
  · intro α β hα hαδ hβ hβδ
    have hβδ' : β < δ := hβδ.trans_le (min_le_right _ _)
    have hα1 : α < 1 := (hαδ.trans_le (min_le_left _ _)).trans hδ'1
    have hαβ : α * β < 1 := by nlinarith
    have hσ : α * (1 - β) / (1 - α * β) ∈ Ioo (0 : ℝ) 1 :=
      ⟨div_pos (by nlinarith) (by linarith), by rw [div_lt_one (by linarith)]; nlinarith⟩
    simp only
    rw [h _ hσ β ⟨hβ, hβδ'⟩]
    simp only [KZComplex.G₀, σc]
    push_cast
    rfl

/-! ### Corner geometry -/

section Geometry

variable (t)

omit [CompleteSpace R] in
theorem W_corner {α β : ℝ} (h1 : 1 - α * β ≠ 0) :
    1 - β * (1 - α * (1 - β) / (1 - α * β)) = (1 - β) / (1 - α * β) := by
  have h1' : 1 - β * α ≠ 0 := by rwa [mul_comm]
  field_simp; ring

omit [CompleteSpace R] in
theorem corner12 {α β : ℝ} (h1 : 1 - α * β ≠ 0) (h2 : 1 - β ≠ 0) :
    (chart1 t).ψ (1 - β, α) = (chart2 t).ψ (α * (1 - β) / (1 - α * β), β) := by
  simp only [chart1, chart2, W_corner h1]
  have h1' : 1 - β * α ≠ 0 := by rwa [mul_comm]
  ext
  all_goals (simp only; field_simp)
  all_goals ring

omit [CompleteSpace R] in
theorem corner23 {α β : ℝ} (h1 : 1 - α * β ≠ 0) (h2 : 1 - β ≠ 0) :
    (chart2 t).ψ (1 - β, α) = (chart3 t).ψ (α * (1 - β) / (1 - α * β), β) := by
  simp only [chart2, chart3, W_corner h1, sub_sub_cancel]
  have h1' : 1 - β * α ≠ 0 := by rwa [mul_comm]
  ext
  all_goals (simp only; field_simp)

omit [CompleteSpace R] in
theorem corner34 {α β : ℝ} (h1 : 1 - α * β ≠ 0) (_h2 : 1 - β ≠ 0) :
    (chart3 t).ψ (1 - β, α) = (chart4 t).ψ (α * (1 - β) / (1 - α * β), β) := by
  simp only [chart3, chart4, W_corner h1, sub_sub_cancel]

omit [CompleteSpace R] in
theorem corner45 {α β : ℝ} (h1 : 1 - α * β ≠ 0) (h2 : 1 - β ≠ 0) :
    (chart4 t).ψ (1 - β, α) = (chart5 t).ψ (α * (1 - β) / (1 - α * β), β) := by
  simp only [chart4, chart5, W_corner h1]
  have h1' : 1 - β * α ≠ 0 := by rwa [mul_comm]
  ext
  all_goals (simp only; field_simp)
  all_goals ring

omit [CompleteSpace R] in
theorem corner51 {α β : ℝ} (h1 : 1 - α * β ≠ 0) :
    (chart5 t).ψ (1 - β, α) = (chart1 t).ψ (α * (1 - β) / (1 - α * β), β) := by
  simp only [chart5, chart1, sub_sub_cancel]
  have h1' : 1 - β * α ≠ 0 := by rwa [mul_comm]
  ext
  all_goals (simp only; field_simp)
  all_goals ring

end Geometry

/-! ### The pentagon -/

/-- **The pentagon for the KZ associator.** For four-point residues satisfying the infinitesimal
braid relations, with the five boundary residues non-resonant, the KZ associators of the five
boundary divisors of `M̄_{0,5}` multiply to `1`:
`Φ(T₂₃₄, t₁₂) Φ(t₂₃, t₃₄) Φ(T₁₂₃, T₂₃₄) Φ(t₁₂, t₂₃) Φ(t₃₄, T₁₂₃) = 1`. -/
theorem pentagon (t : Res R) (h : t.Rel) (h12 : NonResonant t.t12) (h123 : NonResonant t.T123)
    (h23 : NonResonant t.t23) (h234 : NonResonant t.T234) (h34 : NonResonant t.t34) :
    Φ t.T234 t.t12 h234 h12 * Φ t.t23 t.t34 h23 h34 * Φ t.T123 t.T234 h123 h234 *
      Φ t.t12 t.t23 h12 h23 * Φ t.t34 t.T123 h34 h123 = 1 := by
  obtain ⟨N, hN, hNu, -⟩ := Flat2D.exists_reference2 isOpen_Δ (convex_Δ.starConvex mem_Δ_center)
    (fun p hp => hasFDerivAt_Ωx t hp) (fun p hp => hasFDerivAt_Ωy t hp)
    (continuousOn_fderiv_Ωx t) (continuousOn_fderiv_Ωy t) (fun p hp => Res.Rel.curvature t h hp)
  obtain ⟨δ1, hδ1, hδ1', a1, b1, ha1, hab1, he1⟩ :=
    edge_assoc (chart1 t) h12 h34 h123 h.c5.symm h.c1 hN hNu
  obtain ⟨δ2, hδ2, hδ2', a2, b2, ha2, hab2, he2⟩ :=
    edge_assoc (chart2 t) h123 h12 h23 h.c1.symm h.c2 hN hNu
  obtain ⟨δ3, hδ3, hδ3', a3, b3, ha3, hab3, he3⟩ :=
    edge_assoc (chart3 t) h23 h123 h234 h.c2.symm h.c3 hN hNu
  obtain ⟨δ4, hδ4, hδ4', a4, b4, ha4, hab4, he4⟩ :=
    edge_assoc (chart4 t) h234 h23 h34 h.c3.symm h.c4 hN hNu
  obtain ⟨δ5, hδ5, hδ5', a5, b5, ha5, hab5, he5⟩ :=
    edge_assoc (chart5 t) h34 h234 h12 h.c4.symm h.c5 hN hNu
  have hne : ∀ α β : ℝ, 0 < α → α < 1 → 0 < β → β < 1 → 1 - α * β ≠ 0 :=
    fun α β hα hα1 hβ hβ1 => (show 0 < 1 - α * β by nlinarith).ne'
  have hne' : ∀ β : ℝ, β < 1 → 1 - β ≠ 0 := fun β hβ => (show 0 < 1 - β by linarith).ne'
  have k12 : b1 = a2 := corner_step h12 h123 h.c1 h.c5.symm h.c2
    (fun α β hα hα1 hβ hβ1 => corner12 t (hne α β hα hα1 hβ hβ1) (hne' β hβ1))
    hδ1 hδ1' hδ2 hδ2' ha2 (fun s hs ε hε => (he1 s hs ε hε).2) (fun s hs ε hε => (he2 s hs ε hε).1)
  have k23 : b2 = a3 := corner_step h123 h23 h.c2 h.c1.symm h.c3
    (fun α β hα hα1 hβ hβ1 => corner23 t (hne α β hα hα1 hβ hβ1) (hne' β hβ1))
    hδ2 hδ2' hδ3 hδ3' ha3 (fun s hs ε hε => (he2 s hs ε hε).2) (fun s hs ε hε => (he3 s hs ε hε).1)
  have k34 : b3 = a4 := corner_step h23 h234 h.c3 h.c2.symm h.c4
    (fun α β hα hα1 hβ hβ1 => corner34 t (hne α β hα hα1 hβ hβ1) (hne' β hβ1))
    hδ3 hδ3' hδ4 hδ4' ha4 (fun s hs ε hε => (he3 s hs ε hε).2) (fun s hs ε hε => (he4 s hs ε hε).1)
  have k45 : b4 = a5 := corner_step h234 h34 h.c4 h.c3.symm h.c5
    (fun α β hα hα1 hβ hβ1 => corner45 t (hne α β hα hα1 hβ hβ1) (hne' β hβ1))
    hδ4 hδ4' hδ5 hδ5' ha5 (fun s hs ε hε => (he4 s hs ε hε).2) (fun s hs ε hε => (he5 s hs ε hε).1)
  have k51 : b5 = a1 := corner_step h34 h12 h.c5 h.c4.symm h.c1
    (fun α β hα hα1 hβ hβ1 => corner51 t (hne α β hα hα1 hβ hβ1))
    hδ5 hδ5' hδ1 hδ1' ha1 (fun s hs ε hε => (he5 s hs ε hε).2) (fun s hs ε hε => (he1 s hs ε hε).1)
  have key : a1 * 1 = a1 * (Φ t.T234 t.t12 h234 h12 * Φ t.t23 t.t34 h23 h34 *
      Φ t.T123 t.T234 h123 h234 * Φ t.t12 t.t23 h12 h23 * Φ t.t34 t.T123 h34 h123) := by
    calc a1 * 1 = a1 := mul_one _
      _ = b5 * Φ t.T234 t.t12 h234 h12 * Φ t.t23 t.t34 h23 h34 * Φ t.T123 t.T234 h123 h234 *
          Φ t.t12 t.t23 h12 h23 * Φ t.t34 t.T123 h34 h123 := by
        rw [hab1, k12, hab2, k23, hab3, k34, hab4, k45, hab5]
        simp only [mul_assoc]; rfl
      _ = _ := by rw [k51]; simp only [mul_assoc]
  exact (ha1.mul_left_cancel key).symm

end QOU.KZ.KZPentagon
