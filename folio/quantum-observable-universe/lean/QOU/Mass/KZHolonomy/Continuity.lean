import QOU.Mass.KZHolonomy.BraidRep
import Mathlib.Analysis.Normed.Ring.Units

/-!
# Continuity of the KZ holonomy in the coupling `κ`

For a complete normed `ℂ`-algebra `A` and a coefficient `B : ℝ → A` continuous on `[0,1]`,
the endpoint value `U κ 1` of the fundamental solution of `U' = (κ • B) U`, `U 0 = 1`, depends
continuously on `κ ∈ ℂ` (`continuous_fundSol_param`).

The proof is a Grönwall estimate.  The difference `G = U κ' - U κ` satisfies
`G' - (κ • B) G = (κ' - κ) • B U κ'`, whose norm is `≤ ‖κ' - κ‖ · M · N`, where `M` bounds
`‖B‖` on `[0,1]` (compactness) and `N` bounds `‖U κ'‖` uniformly for `‖κ' - κ‖ ≤ 1`
(again Grönwall, against the zero solution).  Hence `‖U κ' 1 - U κ 1‖ = O(‖κ' - κ‖)`.

Applied to the KZ connection along the generator paths, this gives continuity in `κ` of the
image of every braid generator under `kzBraidRep` (`continuous_kzBraidRep_σ`), and then of
every braid (`continuous_kzBraidRep`), using continuity of `Ring.inverse` at units for the
inverses of generators.
-/

open Set Filter Topology

namespace QOU.Mass.KZHolonomy

section General

variable {A : Type*} [NormedRing A] [NormedAlgebra ℂ A]

/-- A uniform bound on a fundamental solution whose coefficient is bounded by `K`. -/
lemma norm_fundSol_le {X U : ℝ → A} {K : ℝ} (hU : IsFundSol X U) (hK : 0 ≤ K)
    (hX : ∀ t ∈ Icc (0:ℝ) 1, ‖X t‖ ≤ K) :
    ∀ t ∈ Icc (0:ℝ) 1, ‖U t‖ ≤ ‖(1:A)‖ * Real.exp K := by
  intro t ht
  have key := norm_le_gronwallBound_of_norm_deriv_right_le (f := U)
    (f' := fun s => X s * U s) (δ := ‖(1:A)‖) (K := K) (ε := 0) (a := 0) (b := 1)
    hU.continuousOn
    (fun s hs => hasDerivWithinAt_Ici_of_Icc hs (hU.2 s (Ico_subset_Icc_self hs)))
    (by rw [hU.1])
    (fun s hs => by
      rw [add_zero]
      exact (norm_mul_le _ _).trans
        (mul_le_mul_of_nonneg_right (hX s (Ico_subset_Icc_self hs)) (norm_nonneg _)))
    t ht
  rw [gronwallBound_ε0, sub_zero] at key
  exact key.trans (mul_le_mul_of_nonneg_left
    (Real.exp_le_exp.2 (mul_le_of_le_one_right hK ht.2)) (norm_nonneg _))

/-- **Continuity of the fundamental solution in the coupling.**  If `U κ` is the fundamental
solution of `U' = (κ • B) U` on `[0,1]` for every `κ ∈ ℂ`, then `κ ↦ U κ 1` is continuous. -/
theorem continuous_fundSol_param {B : ℝ → A} (hB : ContinuousOn B (Icc 0 1))
    {U : ℂ → ℝ → A} (hU : ∀ κ, IsFundSol (fun t => κ • B t) (U κ)) :
    Continuous (fun κ => U κ 1) := by
  obtain ⟨M₀, hM₀⟩ := (isCompact_Icc (a := (0:ℝ)) (b := 1)).exists_bound_of_continuousOn hB
  set M : ℝ := max M₀ 0
  have hM0 : 0 ≤ M := le_max_right _ _
  have hM : ∀ t ∈ Icc (0:ℝ) 1, ‖B t‖ ≤ M := fun t ht => (hM₀ t ht).trans (le_max_left _ _)
  have hXb : ∀ κ : ℂ, ∀ t ∈ Icc (0:ℝ) 1, ‖κ • B t‖ ≤ ‖κ‖ * M := fun κ t ht => by
    rw [norm_smul]
    exact mul_le_mul_of_nonneg_left (hM t ht) (norm_nonneg _)
  -- the Lipschitz constant at `κ`
  let N : ℂ → ℝ := fun κ => ‖(1:A)‖ * Real.exp ((‖κ‖ + 1) * M)
  let C : ℂ → ℝ := fun κ => M * N κ * gronwallBound 0 (‖κ‖ * M) 1 1
  have est : ∀ κ κ' : ℂ, ‖κ' - κ‖ ≤ 1 → ‖U κ' 1 - U κ 1‖ ≤ ‖κ' - κ‖ * C κ := by
    intro κ κ' hκ
    have hκ' : ‖κ'‖ ≤ ‖κ‖ + 1 := by
      have := norm_le_insert' κ' κ
      linarith
    have hN : ∀ t ∈ Icc (0:ℝ) 1, ‖U κ' t‖ ≤ N κ :=
      norm_fundSol_le (hU κ') (by positivity)
        (fun t ht => (hXb κ' t ht).trans (mul_le_mul_of_nonneg_right hκ' hM0))
    have h := norm_le_of_linear_defect (G := fun t => U κ' t - U κ t)
      (G' := fun t => κ' • B t * U κ' t - κ • B t * U κ t) (p := fun t => κ • B t)
      (K := ‖κ‖ * M) (r := ‖κ' - κ‖ * (M * N κ))
      (fun t ht => ((hU κ').2 t ht).sub ((hU κ).2 t ht))
      (by simp [(hU κ').1, (hU κ).1]) (hXb κ)
      (fun t ht => by
        have e : κ' • B t * U κ' t - κ • B t * U κ t - κ • B t * (U κ' t - U κ t)
            = (κ' - κ) • B t * U κ' t := by
          simp only [mul_sub, sub_smul, sub_mul]
          abel
        rw [e, smul_mul_assoc, norm_smul]
        gcongr
        exact (norm_mul_le _ _).trans (mul_le_mul (hM t ht) (hN t ht) (norm_nonneg _) hM0))
    rw [gronwallBound_zero_eq] at h
    simpa only [C, mul_assoc] using h
  refine continuous_iff_continuousAt.2 fun κ => ?_
  rw [ContinuousAt, tendsto_iff_norm_sub_tendsto_zero]
  refine squeeze_zero' (Eventually.of_forall fun _ => norm_nonneg _) ?_
    (g := fun κ' => ‖κ' - κ‖ * C κ) ?_
  · filter_upwards [Metric.closedBall_mem_nhds κ zero_lt_one] with κ' hκ'
    exact est κ κ' (by simpa [dist_eq_norm] using hκ')
  · have h0 : Tendsto (fun κ' : ℂ => ‖κ' - κ‖) (𝓝 κ) (𝓝 ‖κ - κ‖) :=
      ((continuous_id.sub continuous_const).norm).tendsto κ
    rw [sub_self, norm_zero] at h0
    simpa using h0.mul_const (C κ)

end General

section Braid

open QOU.MathlibExt.Braid

variable {m : ℕ} {A : Type*} [NormedRing A] [NormedAlgebra ℂ A] [CompleteSpace A]
variable (ρ : Equiv.Perm (Fin (m + 1)) →* A) (c : ℂ)

/-- The image of a braid generator under the KZ holonomy representation is continuous in the
coupling `κ`. -/
theorem continuous_kzBraidRep_σ (j : Fin m) :
    Continuous (fun κ : ℂ => (kzBraidRep ρ κ c (σ j) : A)) := by
  simp only [kzBraidRep_σ]
  refine continuous_const.mul ?_
  set B : ℝ → A := fun t => kzOp ρ c (genPath j t) (genPath' j t)
  have hB : ContinuousOn B (Icc 0 1) := by
    have := continuousOn_genCoeff ρ 1 c j
    simpa only [kzForm_apply, one_smul] using this
  refine continuous_fundSol_param hB (U := fun κ => genFund ρ κ c j) fun κ => ?_
  have h := genFund_spec ρ κ c j
  unfold IsTransport at h
  simpa only [kzForm_apply] using h

/-- The inverse of the image of a braid generator is continuous in `κ`. -/
lemma continuous_kzBraidRep_σ_inv (j : Fin m) :
    Continuous (fun κ : ℂ => (((kzBraidRep ρ κ c (σ j))⁻¹ : Aˣ) : A)) := by
  have hf := continuous_kzBraidRep_σ ρ c j
  have e : (fun κ : ℂ => (((kzBraidRep ρ κ c (σ j))⁻¹ : Aˣ) : A)) =
      fun κ => Ring.inverse (kzBraidRep ρ κ c (σ j) : A) := by
    funext κ
    rw [Ring.inverse_unit]
  rw [e, continuous_iff_continuousAt]
  intro κ
  exact ContinuousAt.comp (g := Ring.inverse) (f := fun κ : ℂ => (kzBraidRep ρ κ c (σ j) : A))
    (NormedRing.inverse_continuousAt (kzBraidRep ρ κ c (σ j))) hf.continuousAt

/-- **Continuity of the KZ holonomy in `κ`.**  For every braid `b`, the image of `b` under
`kzBraidRep ρ κ c` depends continuously on the coupling `κ`. -/
theorem continuous_kzBraidRep (b : BraidGroup m) :
    Continuous (fun κ : ℂ => (kzBraidRep ρ κ c b : A)) := by
  let H : Subgroup (BraidGroup m) :=
    { carrier := {b | Continuous (fun κ : ℂ => (kzBraidRep ρ κ c b : A)) ∧
        Continuous (fun κ : ℂ => (((kzBraidRep ρ κ c b)⁻¹ : Aˣ) : A))}
      mul_mem' := by
        intro a b ha hb
        simp only [Set.mem_setOf_eq] at ha hb ⊢
        refine ⟨?_, ?_⟩
        · simpa only [map_mul, Units.val_mul] using ha.1.mul hb.1
        · simpa only [map_mul, mul_inv_rev, Units.val_mul] using hb.2.mul ha.2
      one_mem' := by
        simp only [Set.mem_setOf_eq, map_one, inv_one, Units.val_one]
        exact ⟨continuous_const, continuous_const⟩
      inv_mem' := by
        intro a ha
        simp only [Set.mem_setOf_eq, map_inv, inv_inv] at ha ⊢
        exact ⟨ha.2, ha.1⟩ }
  have hgen : ∀ j : Fin m, PresentedGroup.of j ∈ H := fun j =>
    ⟨continuous_kzBraidRep_σ ρ c j, continuous_kzBraidRep_σ_inv ρ c j⟩
  exact (PresentedGroup.generated_by _ H hgen b).1

end Braid

end QOU.Mass.KZHolonomy
