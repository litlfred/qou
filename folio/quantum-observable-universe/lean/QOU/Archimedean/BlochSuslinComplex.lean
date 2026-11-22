import QOU.Knot.KummerUnitCircle

/-!
# The Bloch–Suslin uniqueness class, restated over `ℂ` (issue #7942)

`BlochSuslinUniqueness` in `mass-theory/archimedean-functor-uniqueness.lean` is
stated for `D : ℝ → ℝ`, and its `PentagonCoherent` relation has the last two
arguments inverted relative to Suslin.  That combination forces every solution to
`0` (`blochSuslinUniqueness_iff`).  This file gives the corrected statement:

* **Domain `ℂ \ {0,1}`.**  The Bloch–Wigner function vanishes on the real line,
  and the conjugation symmetry `D(z̄) = -D(z)` forces any solution to vanish
  there (`real_slice_eq_zero`).  So the real line is exactly where nothing can
  be seen; the content is off it.
* **Suslin's orientation.**  `SuslinFiveTerm` below is
  `[x] - [y] + [y/x] - [(1 - x⁻¹)/(1 - y⁻¹)] + [(1 - x)/(1 - y)] = 0`
  (Suslin 1991, §1).
* **Two hypotheses, not one.**  The old class bundled a classical identity with
  a rigidity theorem.  Here they are split, so each can be closed on its own:
  - `BlochWignerFiveTerm D` — `D` satisfies the five-term relation.  This is
    the classical identity (Bloch; Zagier 1991 §2).  It is **proved** for the
    full-plane Bloch–Wigner function `FiveTermProof.blochD`, as the instance
    `blochWignerFiveTerm_blochD` in `BlochWignerFiveTermInstance.lean`.  That
    function equals `BlochWigner_lob` on the upper half plane only:
    `BlochWigner_lob` is `0` below the real axis, so it is not the function
    the identity is about, and no instance is given for it.
  - `BlochSuslinRigidity D` — every continuous solution with the two
    symmetries is a real multiple of `D`.  This is the rigidity input
    (Bloch 1978; Suslin 1991), not in Mathlib.  It is **proved** for
    `FiveTermProof.blochD`, as the instance `blochSuslinRigidity_blochD` in
    `BlochRigidity/Instance.lean`.

With both, `archimedean_functor_uniqueness_complex` is proved, and the figure-8
calibration `figure8_calibration_complex` now evaluates at the genuine shape
`e^{iπ/3}`, where `BlochWigner_lob = Cl₂(π/3)` is already a theorem
(`QOU.Knot.Kummer.blochWigner_lob_exp`).  Neither class has an instance in this
file; both are instantiated for `FiveTermProof.blochD` downstream, and neither
for `BlochWigner_lob`.

-- Ref: [suslin1991] Suslin, K_3 of a field, and the Bloch group, Trudy Mat. Inst. Steklova 183 (1991) 217-239.
-- Ref: [bloch2000] Bloch, Higher Regulators, Algebraic K-Theory, and Zeta Functions of Elliptic Curves, AMS CRM 11 (2000).
-- Ref: [zagier1991] Zagier, "Polylogarithms, Dedekind zeta functions and the algebraic K-theory of fields" (1991).
-- Ref: [leitner2026] prop:archimedean-functor-uniqueness
-/

namespace QOU.Archimedean

open Complex

/-- The **five-term relation in Suslin's orientation**, on `ℂ \ {0,1}`. -/
def SuslinFiveTerm (f : ℂ → ℝ) : Prop :=
  ∀ x y : ℂ, x ≠ 0 → x ≠ 1 → y ≠ 0 → y ≠ 1 → x ≠ y →
    f x - f y + f (y / x) - f ((1 - x⁻¹) / (1 - y⁻¹)) + f ((1 - x) / (1 - y)) = 0

/-- The two symmetries of the Bloch–Wigner function. -/
structure BlochSymmetric (f : ℂ → ℝ) : Prop where
  inv : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → f z⁻¹ = -f z
  conj : ∀ z : ℂ, f ((starRingEnd ℂ) z) = -f z

/-- **Classical input 1:** `D` satisfies the five-term relation. -/
class BlochWignerFiveTerm (D : ℂ → ℝ) : Prop where
  five_term : SuslinFiveTerm D

/-- **Classical input 2 (rigidity):** every function on `ℂ \ {0,1}` that is
    continuous, has the Bloch–Wigner symmetries and satisfies the five-term
    relation is a real multiple of `D`. -/
class BlochSuslinRigidity (D : ℂ → ℝ) : Prop where
  uniqueness :
    ∀ φ : ℂ → ℝ, ContinuousOn φ {0, 1}ᶜ → BlochSymmetric φ → SuslinFiveTerm φ →
      ∃ c : ℝ, ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ z = c * D z

/-- **Why the real slice carries nothing.**  The conjugation symmetry alone
    forces `f x = 0` at every real `x`. -/
theorem real_slice_eq_zero (f : ℂ → ℝ) (hf : BlochSymmetric f) (x : ℝ) :
    f (x : ℂ) = 0 := by
  have h := hf.conj (x : ℂ)
  rw [Complex.conj_ofReal] at h
  linarith

/-- **Uniqueness of the archimedean realisation (conditional, complex form).** -/
theorem archimedean_functor_uniqueness_complex (D τ_arch : ℂ → ℝ)
    [hD : BlochSuslinRigidity D]
    (h_cont : ContinuousOn τ_arch {0, 1}ᶜ) (h_sym : BlochSymmetric τ_arch)
    (h_five : SuslinFiveTerm τ_arch) :
    ∃ c : ℝ, ∀ z : ℂ, z ≠ 0 → z ≠ 1 → τ_arch z = c * D z :=
  hD.uniqueness τ_arch h_cont h_sym h_five

/-- **Figure-8 calibration at the genuine shape `e^{iπ/3}`.**  If `τ_arch` is a
    multiple `c` of the Bloch–Wigner function, then at the regular ideal
    tetrahedron `τ_arch(e^{iπ/3}) = c · Cl₂(π/3)`, so two tetrahedra give
    `c · Vol(4₁) = c · 2 Cl₂(π/3)`.  The value of `D` here is a theorem, not an
    input. -/
theorem figure8_calibration_complex (τ_arch : ℂ → ℝ) (c : ℝ)
    (h : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → τ_arch z = c * BlochWigner_lob z) :
    2 * τ_arch (Complex.exp (((Real.pi / 3 : ℝ) : ℂ) * Complex.I))
      = c * (2 * Cl_2 (Real.pi / 3)) := by
  have hπ := Real.pi_pos
  have h0 : (0 : ℝ) < Real.pi / 3 := by positivity
  have h1 : Real.pi / 3 < Real.pi := by linarith
  have hne0 : Complex.exp (((Real.pi / 3 : ℝ) : ℂ) * Complex.I) ≠ 0 :=
    Complex.exp_ne_zero _
  have hne1 : Complex.exp (((Real.pi / 3 : ℝ) : ℂ) * Complex.I) ≠ 1 := by
    intro hz
    have him := congrArg Complex.im hz
    rw [Complex.exp_ofReal_mul_I_im] at him
    simp only [Complex.one_im] at him
    have : 0 < Real.sin (Real.pi / 3) := Real.sin_pos_of_pos_of_lt_pi h0 h1
    linarith
  rw [h _ hne0 hne1, QOU.Knot.Kummer.blochWigner_lob_exp h0 h1]
  ring

/-- **The full chain, conditional on the two classical inputs.**  Any
    continuous `τ_arch` with the Bloch–Wigner symmetries and the five-term
    relation gives the figure-8 value up to one real scalar. -/
theorem figure8_from_rigidity (τ_arch : ℂ → ℝ)
    [BlochSuslinRigidity BlochWigner_lob]
    (h_cont : ContinuousOn τ_arch {0, 1}ᶜ) (h_sym : BlochSymmetric τ_arch)
    (h_five : SuslinFiveTerm τ_arch) :
    ∃ c : ℝ, 2 * τ_arch (Complex.exp (((Real.pi / 3 : ℝ) : ℂ) * Complex.I))
      = c * (2 * Cl_2 (Real.pi / 3)) := by
  obtain ⟨c, hc⟩ :=
    archimedean_functor_uniqueness_complex BlochWigner_lob τ_arch h_cont h_sym h_five
  exact ⟨c, figure8_calibration_complex τ_arch c hc⟩

end QOU.Archimedean
