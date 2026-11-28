import QOU.Transcendental.BraidKnotOctonion.Clausen
import QOU.Transcendental.MassTheory.LeptonBundleRegulator

/-!
# The Bloch–Wigner function is positive on the upper half plane

**Theorem** (`blochD_pos`). If `0 < Im z` then `0 < D(z)`.

This is the analytic fact that makes a regulator nonzero. The proof is elementary
once the pieces in the corpus are put together:

* on the upper half plane `D(z) = Λ(α) + Λ(β) + Λ(γ)`, the Lobachevsky function at
  the three dihedral angles of the ideal tetrahedron of shape `z`
  (`FiveTermProof.blochD_eq_lob`); the angles lie in `(0, π)` and sum to `π`
  (`arg_mem_Ioo_of_im_pos`, `tet_im_pos`, `tetAngles_sum_eq_pi`);
* `Λ(t) = Cl₂(2t)/2` has derivative `−log(2 sin t)` on `(0, π)`
  (`QOU.Knot.hasDerivAt_Cl_2_series`), is continuous, odd, and `π`-periodic.

With `γ = π − α − β` and `Λ(π − x) = −Λ(x)`, the sum is
`φ(α) = Λ(α) + Λ(β) − Λ(α + β)` on `[0, π − β]`. It vanishes at both ends, and
`φ'(α) = log(sin(α + β)/sin α)`, whose sign is that of
`sin(α + β) − sin α = 2 sin(β/2) cos(α + β/2)`: positive before the midpoint
`(π − β)/2` and negative after. So `φ > 0` in the interior (`lob_sum_pos`).

Consequences:
* `regulator_nahmClass_pos`: a Nahm class with every shape in the upper half plane
  has positive regulator, so it is a nonzero element of `B(ℂ) ⊗ ℚ`.
* `regulator_muClass_pos`, `regulator_tauClass_pos`: the `μ` (`R²L`) and `τ`
  (`R⁴L`) classes at their upper-half-plane roots have positive regulator.

A single evaluation of `D`, no limit, no `[Coev E]` instance, no numerical value.

-- Ref: [zagier1986] DOI 10.1007/BFb0084581
-- Ref: [thurston1978] The geometry and topology of three-manifolds
-/

namespace QOU.Archimedean.BlochWignerPositive

open Real QOU.Archimedean QOU.Archimedean.FiveTermProof
open QOU.Archimedean.NahmBlochBridge QOU.Archimedean.LeptonBundleNahm
open QOU.Archimedean.NahmRegulator QOU.Archimedean.LeptonBundleRegulator

noncomputable section

theorem continuous_Lob : Continuous Lob := by
  have : Lob = fun t => Cl_2 (2 * t) / 2 := rfl
  rw [this]
  exact (QOU.Knot.continuous_Cl_2.comp (continuous_const.mul continuous_id)).div_const 2

theorem hasDerivAt_Lob {t : ℝ} (h0 : 0 < t) (hπ : t < π) :
    HasDerivAt Lob (-Real.log (2 * Real.sin t)) t := by
  have h := QOU.Knot.hasDerivAt_Cl_2_series (θ := 2 * t) (by linarith) (by linarith)
  have h2 : HasDerivAt (fun s : ℝ => 2 * s) 2 t := by
    simpa using (hasDerivAt_id t).const_mul (2 : ℝ)
  have h3 := (h.comp t h2).div_const 2
  have hfun : Lob = fun s => Cl_2 (2 * s) / 2 := rfl
  rw [hfun]
  convert h3 using 1
  rw [show 2 * t / 2 = t by ring]
  ring

theorem Lob_pi_sub (x : ℝ) : Lob (π - x) = -Lob x := by
  unfold Lob
  rw [show 2 * (π - x) = -(2 * x) + 2 * π by ring, Cl_2_add_two_pi, Cl_2_neg]
  ring

/-- `sin(α + β) − sin α = 2 sin(β/2) cos(α + β/2)`. -/
theorem sin_add_sub_sin (α β : ℝ) :
    Real.sin (α + β) - Real.sin α = 2 * Real.sin (β / 2) * Real.cos (α + β / 2) := by
  rw [Real.sin_sub_sin]
  congr 2 <;> ring_nf

/-- **The Lobachevsky sum is positive.** For `0 < β < π` and `0 < α < π − β`,
`Λ(α) + Λ(β) − Λ(α + β) > 0`. -/
theorem lob_sum_pos {α β : ℝ} (hβ0 : 0 < β) (hβπ : β < π) (hα0 : 0 < α)
    (hα : α < π - β) : 0 < Lob α + Lob β - Lob (α + β) := by
  set φ : ℝ → ℝ := fun x => Lob x + Lob β - Lob (x + β) with hφ
  set m : ℝ := (π - β) / 2 with hm
  have hcont : Continuous φ :=
    ((continuous_Lob.add continuous_const).sub (continuous_Lob.comp (continuous_id.add
      continuous_const)))
  have hsinb : 0 < Real.sin (β / 2) :=
    Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
  have hderiv : ∀ x, 0 < x → x < π - β →
      HasDerivAt φ (-Real.log (2 * Real.sin x) + Real.log (2 * Real.sin (x + β))) x := by
    intro x hx0 hx
    have h1 := hasDerivAt_Lob hx0 (by linarith)
    have h2 := (hasDerivAt_Lob (t := x + β) (by linarith) (by linarith)).comp x
      ((hasDerivAt_id x).add_const β)
    have := (h1.add_const (Lob β)).sub h2
    convert this using 1
    simp
  have hsx : ∀ x, 0 < x → x < π - β → 0 < Real.sin x ∧ 0 < Real.sin (x + β) := fun x hx0 hx =>
    ⟨Real.sin_pos_of_pos_of_lt_pi hx0 (by linarith),
      Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)⟩
  have hinc : StrictMonoOn φ (Set.Icc 0 m) := by
    refine strictMonoOn_of_deriv_pos (convex_Icc 0 m) hcont.continuousOn ?_
    intro x hx
    rw [interior_Icc] at hx
    obtain ⟨hx0, hxm⟩ := hx
    rw [(hderiv x hx0 (by linarith)).deriv]
    obtain ⟨s1, s2⟩ := hsx x hx0 (by linarith)
    have hc : 0 < Real.cos (x + β / 2) :=
      Real.cos_pos_of_mem_Ioo ⟨by linarith, by linarith⟩
    have hlt : Real.sin x < Real.sin (x + β) := by
      have := sin_add_sub_sin x β; nlinarith [mul_pos hsinb hc]
    have := Real.log_lt_log (by linarith) (by linarith : 2 * Real.sin x < 2 * Real.sin (x + β))
    linarith
  have hdec : StrictAntiOn φ (Set.Icc m (π - β)) := by
    refine strictAntiOn_of_deriv_neg (convex_Icc m (π - β)) hcont.continuousOn ?_
    intro x hx
    rw [interior_Icc] at hx
    obtain ⟨hxm, hx⟩ := hx
    rw [(hderiv x (by linarith) hx).deriv]
    obtain ⟨s1, s2⟩ := hsx x (by linarith) hx
    have hc : Real.cos (x + β / 2) < 0 :=
      Real.cos_neg_of_pi_div_two_lt_of_lt (by linarith) (by linarith)
    have hlt : Real.sin (x + β) < Real.sin x := by
      have := sin_add_sub_sin x β; nlinarith [mul_pos hsinb (neg_pos.2 hc)]
    have := Real.log_lt_log (by linarith) (by linarith : 2 * Real.sin (x + β) < 2 * Real.sin x)
    linarith
  have hφ0 : φ 0 = 0 := by simp [hφ]
  have hφe : φ (π - β) = 0 := by
    simp only [hφ, show π - β + β = π by ring, Lob_pi, Lob_pi_sub]; ring
  show 0 < φ α
  rcases le_or_gt α m with h | h
  · have := hinc ⟨le_refl 0, by linarith⟩ ⟨hα0.le, h⟩ hα0
    linarith
  · have := hdec ⟨h.le, hα.le⟩ ⟨by linarith, le_refl _⟩ hα
    linarith

/-- **`D(z) > 0` on the upper half plane.** -/
theorem blochD_pos {z : ℂ} (hz : 0 < z.im) : 0 < blochD z := by
  rw [blochD_eq_lob hz]
  obtain ⟨h2, h3⟩ := tet_im_pos z hz
  obtain ⟨a0, aπ⟩ := arg_mem_Ioo_of_im_pos z hz
  obtain ⟨b0, bπ⟩ := arg_mem_Ioo_of_im_pos _ h2
  obtain ⟨c0, cπ⟩ := arg_mem_Ioo_of_im_pos _ h3
  have hsum := tetAngles_sum_eq_pi z hz
  unfold BlochWigner_lob
  unfold tetAngle₁ tetAngle₂ tetAngle₃ at *
  have hc : (1 - 1 / z).arg = π - (z.arg + (1 / (1 - z)).arg) := by linarith
  rw [hc, Lob_pi_sub]
  have := lob_sum_pos b0 bπ a0 (by linarith)
  linarith

/-- **A Nahm class with every shape in the upper half plane has positive regulator.** -/
theorem regulator_nahmClass_pos {ι : Type*} [Fintype ι] [Nonempty ι] {A : Matrix ι ι ℤ}
    (s : NahmSolution ℂ ι A) (h : ∀ i, 0 < (s.w i : ℂ).im) : 0 < regulator (nahmClass s) := by
  rw [regulator_nahmClass]
  exact Finset.sum_pos (fun i _ => blochD_pos (h i)) Finset.univ_nonempty

/-- **The `μ` regulator is positive** at the upper-half-plane root. -/
theorem regulator_muClass_pos {y : ℂ} (hy : 2 * y ^ 2 - 3 * y + 2 = 0) (him : 0 < y.im) :
    0 < regulator (nahmClass (muSolution hy)) := by
  rw [regulator_muClass]
  have h1 : 0 < (1 / 2 + y).im := by simpa using him
  have := blochD_pos h1
  have := blochD_pos him
  linarith

/-- At a non-real root of the `τ` cubic, `Re s < 1`. -/
theorem tau_root_re_lt_one {s : ℂ} (hs : s ^ 3 - 6 * s ^ 2 + 8 * s - 4 = 0) (him : 0 < s.im) :
    s.re < 1 := by
  have hre := congrArg Complex.re hs
  have hi := congrArg Complex.im hs
  simp [pow_succ, Complex.mul_re, Complex.mul_im] at hre hi
  set x := s.re
  set y := s.im
  have hy2 : y ^ 2 = 3 * x ^ 2 - 12 * x + 8 := by
    have : y * (3 * x ^ 2 - y ^ 2 - 12 * x + 8) = 0 := by linear_combination hi
    have := (mul_eq_zero.1 this).resolve_left him.ne'
    linarith
  have hg : 2 * x ^ 3 - 12 * x ^ 2 + 22 * x - 11 = 0 := by
    have : x ^ 3 - 3 * x * y ^ 2 - 6 * (x ^ 2 - y ^ 2) + 8 * x - 4 = 0 := by
      linear_combination hre
    rw [hy2] at this
    linarith
  by_contra hx
  push_neg at hx
  have hpos : 0 < 3 * x ^ 2 - 12 * x + 8 := by rw [← hy2]; positivity
  nlinarith [sq_nonneg (x - 2), sq_nonneg (x - 3)]

/-- **The `τ` regulator is positive** at the upper-half-plane root. -/
theorem regulator_tauClass_pos {s : ℂ} (hs : s ^ 3 - 6 * s ^ 2 + 8 * s - 4 = 0)
    (him : 0 < s.im) : 0 < regulator (nahmClass (tauSolution hs)) := by
  rw [regulator_tauClass]
  have hre := tau_root_re_lt_one hs him
  have hA : 0 < (tauA s).im := by
    simp [tauA, pow_two, Complex.mul_im]; nlinarith
  have hB : 0 < (tauB s).im := by
    simp [tauB, pow_two, Complex.mul_im]; nlinarith
  have := blochD_pos hA
  have := blochD_pos hB
  have := blochD_pos him
  linarith

end

end QOU.Archimedean.BlochWignerPositive
