import QOU.KZ.KZPentagon

/-!
# Functoriality of the KZ associator under continuous algebra maps

Stage S2 prerequisite of bean `qou-zoyv`. If `f : R →ₐ[ℂ] S` is a continuous algebra map between
complete normed `ℂ`-algebras, and `A, B` and `f A, f B` are non-resonant, then
`f (Φ(A, B)) = Φ(f A, f B)` (`map_Φ`). This identifies whiskered associators: under the leg
embedding `End(V^{⊗3}) → End(V^{⊗4})`, `X ↦ X ⊗ 1`, the associator `Φ^{123}` computed in the small
algebra goes to `Φ(t₁₂, t₂₃)` computed in the big one.

The proof: `f` maps normalised formal solutions to normalised formal solutions (uniqueness), and
it commutes with `∑ tᵏ Hₖ` (continuity) and with `t^A = exp(log t · A)` (`NormedSpace.map_exp`).
So `f` carries the connection relation `G₀ = G₁ Φ` to the one for `f A, f B`, and uniqueness in
`kz_associator` concludes. Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S2)
-/

namespace QOU.KZ.KZFunctorial

open Set QOU.KZ.FuchsianFormal QOU.KZ.FuchsianAnalytic QOU.KZ.AssociatorKZ QOU.KZ.KZPentagon

variable {R S : Type*} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]
  [NormedRing S] [NormedAlgebra ℂ S] [CompleteSpace S]

omit [NormedAlgebra ℂ R] [CompleteSpace R] [NormedAlgebra ℂ S] [CompleteSpace S] in
theorem map_isFormalGauge {F : Type*} [FunLike F R S] [RingHomClass F R S] (f : F)
    {M H : ℕ → R} (h : IsFormalGauge M H) : IsFormalGauge (fun k => f (M k)) (fun k => f (H k)) := by
  intro k
  have := congrArg f (h k)
  simpa [map_add, map_mul, map_natCast, map_sum] using this

omit [NormedAlgebra ℂ R] [CompleteSpace R] [NormedAlgebra ℂ S] [CompleteSpace S] in
theorem map_kzM0 {F : Type*} [FunLike F R S] [RingHomClass F R S] (f : F) (A B : R) :
    (fun k => f (kzM0 A B k)) = kzM0 (f A) (f B) := by
  funext k; rcases k with _ | k <;> simp [kzM0]

omit [CompleteSpace R] [CompleteSpace S] in
/-- `f` maps the normalised formal solution to the normalised formal solution. -/
theorem map_H0 (f : R →ₐ[ℂ] S) (A B : R) (hA : NonResonant A) (hfA : NonResonant (f A)) :
    (fun k => f (H0 A B hA k)) = H0 (f A) (f B) hfA := by
  refine formalGauge_unique _ _ _ (fun k hk => (hfA k hk).1) (by simp [H0_zero])
    (H0_zero _ _ hfA) ?_ (H0_gauge _ _ hfA)
  rw [← map_kzM0 f]
  exact map_isFormalGauge f (H0_gauge A B hA)

omit [CompleteSpace S] in
theorem map_series (f : R →ₐ[ℂ] S) (hf : Continuous f) {H : ℕ → R} (hb : BoundedOn H 1)
    {t : ℝ} (ht : |t| < 1) : f (series H t) = series (fun k => f (H k)) t := by
  unfold series
  rw [(summable_norm_of_bounded hb ht).of_norm.map_tsum f hf]
  exact tsum_congr fun k => map_real_smul f hf _ _

omit [CompleteSpace S] in
theorem map_tpow (f : R →ₐ[ℂ] S) (hf : Continuous f) (A : R) (t : ℝ) :
    f (tpow A t) = tpow (f A) t := by
  unfold tpow
  rw [NormedSpace.map_exp ℝ f hf, map_real_smul f hf]

/-- **Functoriality of `Φ_KZ`.** -/
theorem map_Φ (f : R →ₐ[ℂ] S) (hf : Continuous f) (A B : R) (hA : NonResonant A)
    (hB : NonResonant B) (hfA : NonResonant (f A)) (hfB : NonResonant (f B)) :
    f (Φ A B hA hB) = Φ (f A) (f B) hfA hfB := by
  obtain ⟨hu, hΦ⟩ := phiKZ_spec A B (H0 A B hA) (H0 B A hB) (H0_zero _ _ hA) (H0_gauge _ _ hA)
    (H0_zero _ _ hB) (H0_gauge _ _ hB)
  have e₀ := map_H0 f A B hA hfA
  have e₁ := map_H0 f B A hB hfB
  refine ((kz_associator (f A) (f B) (H0 (f A) (f B) hfA) (H0 (f B) (f A) hfB)
    (H0_zero _ _ hfA) (H0_gauge _ _ hfA) (H0_zero _ _ hfB) (H0_gauge _ _ hfB)).unique
    ⟨hu.map f, fun t ht => ?_⟩ (phiKZ_spec _ _ _ _ _ _ _ _))
  have h := congrArg f (hΦ t ht)
  have ht0 : |t| < 1 := by rw [abs_of_pos ht.1]; exact ht.2
  have ht1 : |1 - t| < 1 := by rw [abs_of_pos (by linarith [ht.2])]; linarith [ht.1]
  simp only [G₀, G₁, map_mul, map_series f hf (boundedOn_H0 A B hA) ht0,
    map_series f hf (boundedOn_H0 B A hB) ht1, map_tpow f hf, e₀, e₁] at h
  simpa only [G₀, G₁, Φ] using h

end QOU.KZ.KZFunctorial
