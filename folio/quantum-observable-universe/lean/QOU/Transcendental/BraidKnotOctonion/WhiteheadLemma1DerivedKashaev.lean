import BraidKnotOctonion.WhiteheadLemma1Derived
import QOU.Transcendental.BraidKnotOctonion.WhiteheadLemma1RootOfUnityKashaev

/-!
# The Whitehead Kashaev-point value is the limit of the quantum trace

Transcendental companion of `BraidKnotOctonion/WhiteheadLemma1Derived.lean` (strangler split,
bean `qou-dk7p`): continuity and limits at `s = e^{πi/N}`.

-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, Lemma 1 and its proof
-/

namespace QOU.Knot.FigureEightVolume

open Matrix QOU.Mass.QuantumSl2

/-! ### The Kashaev-point value is the limit of the trace

At `s = e^{πi/N}` the quantum integer `[N]` vanishes, so the trace identity above does not
hold there. The formula `vdvWhiteheadLinkJones` is continuous at that point (its only
denominators are `1 − s^{2j}` with `0 < j < N`), and the hypotheses of the trace identity
hold on a punctured neighbourhood of any square root `σ₀` of it. So the Kashaev-point value
`whiteheadLinkKashaev N` is the limit of the normalised quantum trace as `σ → σ₀`. -/

/-- The trace side of `vdvWhiteheadLinkJones_eq_trace`, as a function of `σ` (set to `0` at
`σ = 0`, where the representation is not defined). -/
noncomputable def whiteheadTraceSide (m : ℕ) (σ : ℂ) : ℂ :=
  if hσ : σ = 0 then 0 else
    (-1) ^ m * (qint (σ ^ 2) (m + 1))⁻¹ * trace (deltaK (σ ^ 2) m m
      * (beltW σ hσ m * ((σ ^ 2) ^ ((m : ℤ) * (m + 2)) • clasp σ hσ m)))

theorem qint_ne_zero_of_pow {q : ℂ} (hq : q ≠ 0) (h1 : q ^ 2 ≠ 1) {i : ℕ} (hi : q ^ (2 * i) ≠ 1) :
    qint q i ≠ 0 := by
  unfold qint
  refine div_ne_zero ?_ ?_
  · intro h
    apply hi
    have h' : q ^ i = q⁻¹ ^ i := sub_eq_zero.mp h
    calc q ^ (2 * i) = q ^ i * q ^ i := by ring
      _ = q⁻¹ ^ i * q ^ i := by rw [← h']
      _ = 1 := by rw [← mul_pow, inv_mul_cancel₀ hq, one_pow]
  · intro h
    apply h1
    have h' : q = q⁻¹ := sub_eq_zero.mp h
    calc q ^ 2 = q * q := by ring
      _ = q⁻¹ * q := by rw [← h']
      _ = 1 := inv_mul_cancel₀ hq

/-- Away from a point, `σ^k ≠ 1` holds on a punctured neighbourhood (finitely many roots). -/
theorem eventually_pow_ne_one (σ₀ : ℂ) {k : ℕ} (hk : 0 < k) :
    ∀ᶠ σ in nhdsWithin σ₀ {σ₀}ᶜ, σ ^ k ≠ 1 := by
  set T : Set ℂ := ((Polynomial.nthRoots k (1 : ℂ)).toFinset : Set ℂ) \ {σ₀}
  have hT : IsClosed T := ((Polynomial.nthRoots k (1 : ℂ)).toFinset.finite_toSet.diff).isClosed
  have h1 : ∀ᶠ σ in nhds σ₀, σ ∉ T := hT.isOpen_compl.mem_nhds (by simp [T])
  filter_upwards [nhdsWithin_le_nhds h1, self_mem_nhdsWithin] with σ h1 h2 h
  apply h1
  simp only [T, Set.mem_diff, Finset.mem_coe, Multiset.mem_toFinset,
    Polynomial.mem_nthRoots hk, Set.mem_singleton_iff]
  exact ⟨h, h2⟩

theorem kpoint_den_ne_zero {N j : ℕ} (hj : j + 1 < N) :
    1 - Complex.exp (((Real.pi / N : ℝ) : ℂ) * Complex.I) ^ (2 * ((j : ℤ) + 1)) ≠ 0 := by
  have hsin : Real.sin ((((j : ℤ) + 1 : ℤ) : ℝ) * (Real.pi / N)) ≠ 0 := by
    have := sin_grid_pos (N := N) (j := j + 1) (by omega) (by omega)
    push_cast at this ⊢; exact this.ne'
  have h := kpoint_clasp_den (N := N) _ hsin
  intro h0
  rw [h0, div_zero] at h
  have hc : (((2 * Real.sin ((((j : ℤ) + 1 : ℤ) : ℝ) * (Real.pi / N))) : ℝ) : ℂ) ≠ 0 := by
    exact_mod_cast mul_ne_zero two_ne_zero hsin
  exact (div_ne_zero (mul_ne_zero Complex.I_ne_zero (Complex.exp_ne_zero _)) hc) h.symm

/-- `vdvWhiteheadLinkJones` is continuous at the Kashaev point `s = e^{πi/N}`. -/
theorem vdvWhiteheadLinkJones_continuousAt_kashaev (N : ℕ) :
    ContinuousAt (fun s => vdvWhiteheadLinkJones s N)
      (Complex.exp (((Real.pi / N : ℝ) : ℂ) * Complex.I)) := by
  set s₀ := Complex.exp (((Real.pi / N : ℝ) : ℂ) * Complex.I)
  have hs0 : s₀ ≠ 0 := Complex.exp_ne_zero _
  have hz : ∀ k : ℤ, ContinuousAt (fun s : ℂ => s ^ k) s₀ :=
    fun k => continuousAt_id.zpow₀ k (Or.inl hs0)
  unfold vdvWhiteheadLinkJones
  refine tendsto_finset_sum _ fun n hn => ?_
  have hn' := Finset.mem_range.mp hn
  refine ContinuousAt.mul ?_ ?_
  · unfold vdvBeltFused
    exact tendsto_finset_sum _ fun j _ => hz _
  · unfold vdvClasp
    refine (hz _).mul (tendsto_finset_sum _ fun k _ => (hz _).mul
      (tendsto_finset_prod _ fun j hj => ?_))
    have hj' := Finset.mem_range.mp hj
    exact (((continuousAt_const.sub (hz _)).mul (continuousAt_const.sub (hz _))).div
      (continuousAt_const.sub (hz _)) (kpoint_den_ne_zero (by omega)))

/-- **The Kashaev-point value is the limit of the quantum trace.** For any square root `σ₀`
of `e^{πi/N}` (`N = m + 1`), the normalised quantum trace `(−1)^{N−1}[N]⁻¹ tr(Δ(K)·B·φX)` on
`V_N ⊗ V_N` tends to `whiteheadLinkKashaev N` as `σ → σ₀`, `σ ≠ σ₀`. -/
theorem whiteheadTraceSide_tendsto_kashaev (m : ℕ) {σ₀ : ℂ}
    (hσ₀ : σ₀ ^ 2 = Complex.exp (((Real.pi / ((m + 1 : ℕ) : ℝ) : ℝ) : ℂ) * Complex.I)) :
    Filter.Tendsto (whiteheadTraceSide m) (nhdsWithin σ₀ {σ₀}ᶜ)
      (nhds (whiteheadLinkKashaev (m + 1))) := by
  have hc : ContinuousAt (fun σ : ℂ => vdvWhiteheadLinkJones (σ ^ 2) (m + 1)) σ₀ := by
    have h := vdvWhiteheadLinkJones_continuousAt_kashaev (m + 1)
    rw [← hσ₀] at h
    exact h.comp (f := fun σ : ℂ => σ ^ 2) (continuous_pow 2).continuousAt
  have hval : vdvWhiteheadLinkJones (σ₀ ^ 2) (m + 1) = whiteheadLinkKashaev (m + 1) := by
    rw [hσ₀]; exact vdvWhiteheadLinkJones_at_kashaev_point (by omega)
  have hlim := hc.tendsto.mono_left (nhdsWithin_le_nhds (s := {σ₀}ᶜ))
  rw [hval] at hlim
  refine hlim.congr' ?_
  have hall : ∀ᶠ σ in nhdsWithin σ₀ {σ₀}ᶜ, ∀ i ∈ Finset.range (2 * m + 2), σ ^ (4 * (i + 1)) ≠ 1 :=
    (Filter.eventually_all_finset _).mpr fun i _ => eventually_pow_ne_one σ₀ (by omega)
  have hne : ∀ᶠ σ in nhdsWithin σ₀ {σ₀}ᶜ, σ ≠ 0 := by
    have : σ₀ ^ 2 ≠ 0 := by rw [hσ₀]; exact Complex.exp_ne_zero _
    exact nhdsWithin_le_nhds (isOpen_ne.mem_nhds (by rintro rfl; simp at this))
  filter_upwards [hall, hne] with σ hall hσ
  have hq : σ ^ 2 ≠ 0 := pow_ne_zero 2 hσ
  have hpow : ∀ i, 0 < i → i ≤ 2 * m + 1 → (σ ^ 2) ^ (2 * i) ≠ 1 := by
    intro i h0 hi
    have := hall (i - 1) (Finset.mem_range.mpr (by omega))
    rwa [← pow_mul, show 2 * (2 * i) = 4 * (i - 1 + 1) by omega]
  have h1 : (σ ^ 2) ^ 2 ≠ 1 := by simpa using hpow 1 (by omega) (by omega)
  have hint : ∀ i, 0 < i → i ≤ 2 * m + 1 → qint (σ ^ 2) i ≠ 0 :=
    fun i h0 hi => qint_ne_zero_of_pow hq h1 (hpow i h0 hi)
  have hq2 : σ ^ 2 - (σ ^ 2)⁻¹ ≠ 0 := by
    have := hint 1 (by omega) (by omega)
    intro h; apply this; unfold qint; rw [h, div_zero]
  unfold whiteheadTraceSide
  rw [dif_neg hσ, vdvWhiteheadLinkJones_eq_trace σ hσ m hq2 hint]

end QOU.Knot.FigureEightVolume
