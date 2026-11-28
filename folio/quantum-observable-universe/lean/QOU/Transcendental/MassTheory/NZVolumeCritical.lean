import QOU.Transcendental.MassTheory.BlochWignerPositive
import QOU.MassTheory.NeumannZagierBloch

/-!
# A volume maximum solves the modulus half of the gluing equations

Let `A, B` be square integer matrices with `A Bᵀ` symmetric (the Neumann–Zagier
symplectic property). An *angle structure* is a pair `α, β : ι → ℝ` with
`α_j, β_j > 0`, `α_j + β_j < π` and, for every row `k`,
`∑_j (A_kj α_j − B_kj β_j) = 0` (the argument half of the gluing equations, with
`arg z_j = α_j` and `arg(1 − z_j) = −β_j`). Its volume is
`∑_j V(α_j, β_j)`, `V(a, b) = Λ(a) + Λ(b) − Λ(a + b)`.

**Theorem** (`logModulus_gluing`). At a volume maximum over the angle structures,
for every row `k`,

  `∑_j (A_kj · log(sin β_j / sin(α_j + β_j)) + B_kj · log(sin α_j / sin(α_j + β_j))) = 0`.

By the law of sines, `sin β/sin(α + β) = |z|` and `sin α/sin(α + β) = |1 − z|` for the
triangle `0, 1, z` with angles `α` at `0` and `β` at `1`, so this is the modulus half
of `∏_j z_j^{A_kj} (1 − z_j)^{B_kj} = 1`.

Proof. Fix `k` and move along the direction `(dα, dβ) = (B_k·, A_k·)`. It stays among
angle structures: row `l` changes by `t · ((A Bᵀ)_lk − (A Bᵀ)_kl) = 0`, which is the
symplectic property, and positivity is an open condition. So `t = 0` is a local
maximum of the volume along this line, its derivative there is `0`, and by
`Λ'(t) = −log(2 sin t)` that derivative is minus the left side above.

**Theorem** (`exists_nzSolution_of_isVolMax`). The shapes
`z_j = (sin β_j / sin(α_j + β_j)) · e^{i α_j}` then solve every gluing row,
`∏_j z_j^{A_kj} (1 − z_j)^{B_kj} = 1`, and lie in the upper half plane; the identity
`1 − z_j = (sin α_j / sin(α_j + β_j)) · e^{−i β_j}` is the law of sines. With
`BlochWignerPositive.regulator_nzClass_pos` the Bloch class of this solution has positive
regulator (`regulator_pos_of_isVolMax`).

This is the critical-point half of Casson–Rivin. It does not show that a maximum
exists in the interior of the polytope.

-- Ref: [futer-gueritaud-angled] D. Futer, F. Guéritaud, From angled triangulations to hyperbolic structures
-- Ref: [neumann-zagier1985] Neumann, Zagier, Volumes of hyperbolic three-manifolds, Topology 24 (1985) 307-332.
-/

namespace QOU.Archimedean.NZVolumeCritical

open Real Matrix Filter Topology QOU.Archimedean QOU.Archimedean.BlochWignerPositive

set_option linter.unusedSimpArgs false

noncomputable section

variable {ι : Type*} [Fintype ι]

/-- Volume of the ideal tetrahedron with dihedral angles `a, b, π − a − b`. -/
def tetV (a b : ℝ) : ℝ := Lob a + Lob b - Lob (a + b)

/-- Total volume of an angle assignment. -/
def totV (α β : ι → ℝ) : ℝ := ∑ j, tetV (α j) (β j)

/-- Every triangle angle positive. -/
def Pos (α β : ι → ℝ) : Prop := ∀ j, 0 < α j ∧ 0 < β j ∧ α j + β j < π

/-- The argument half of the gluing rows `(A | B)`. -/
def Glue (A B : Matrix ι ι ℤ) (α β : ι → ℝ) : Prop :=
  ∀ k, ∑ j, ((A k j : ℝ) * α j - (B k j : ℝ) * β j) = 0

/-- `(α, β)` maximises the volume over the angle structures of `(A | B)`. -/
def IsVolMax (A B : Matrix ι ι ℤ) (α β : ι → ℝ) : Prop :=
  Pos α β ∧ Glue A B α β ∧
    ∀ α' β', Pos α' β' → Glue A B α' β' → totV α' β' ≤ totV α β

theorem hasDerivAt_affine (a u : ℝ) : HasDerivAt (fun t : ℝ => a + t * u) u 0 := by
  simpa using ((hasDerivAt_id (0 : ℝ)).mul_const u).const_add a

theorem hasDerivAt_tetV_line {a b u v : ℝ} (ha : 0 < a) (hb : 0 < b) (hab : a + b < π) :
    HasDerivAt (fun t => tetV (a + t * u) (b + t * v))
      (-(u * (Real.log (Real.sin a) - Real.log (Real.sin (a + b))) +
        v * (Real.log (Real.sin b) - Real.log (Real.sin (a + b))))) 0 := by
  have sa : Real.sin a ≠ 0 := (Real.sin_pos_of_pos_of_lt_pi ha (by linarith)).ne'
  have sb : Real.sin b ≠ 0 := (Real.sin_pos_of_pos_of_lt_pi hb (by linarith)).ne'
  have sab : Real.sin (a + b) ≠ 0 :=
    (Real.sin_pos_of_pos_of_lt_pi (by linarith) hab).ne'
  have h1 := HasDerivAt.comp_of_eq 0 (hasDerivAt_Lob ha (by linarith)) (hasDerivAt_affine a u) (by simp)
  have h2 := HasDerivAt.comp_of_eq 0 (hasDerivAt_Lob hb (by linarith)) (hasDerivAt_affine b v) (by simp)
  have h3 := HasDerivAt.comp_of_eq 0 (hasDerivAt_Lob (t := a + b) (by linarith) hab)
    ((hasDerivAt_affine a u).add (hasDerivAt_affine b v)) (by simp)
  have h := (h1.add h2).sub h3
  have hf : (fun t => tetV (a + t * u) (b + t * v)) =
      ((Lob ∘ fun t => a + t * u) + (Lob ∘ fun t => b + t * v)) -
        (Lob ∘ ((fun t => a + t * u) + fun t => b + t * v)) := by
    funext t; simp [tetV]
  rw [hf]
  convert h using 1
  rw [Real.log_mul two_ne_zero sa, Real.log_mul two_ne_zero sb, Real.log_mul two_ne_zero sab]
  ring

/-- The direction `(B_k·, A_k·)` preserves the gluing rows, by the symplectic property. -/
theorem glue_line {A B : Matrix ι ι ℤ} (hS : (A * Bᵀ).IsSymm) {α β : ι → ℝ}
    (hg : Glue A B α β) (k : ι) (t : ℝ) :
    Glue A B (fun j => α j + t * (B k j : ℝ)) (fun j => β j + t * (A k j : ℝ)) := by
  intro l
  have h2 : (∑ j, A l j * B k j) = ∑ j, A k j * B l j := by
    simpa [mul_apply] using hS.apply k l
  have h3 : ((∑ j, A l j * B k j : ℤ) : ℝ) = ((∑ j, A k j * B l j : ℤ) : ℝ) := by rw [h2]
  push_cast at h3
  have hsym : ∑ j, ((A l j : ℝ) * B k j - (B l j : ℝ) * A k j) = 0 := by
    rw [Finset.sum_sub_distrib, h3, sub_eq_zero]
    exact Finset.sum_congr rfl fun j _ => mul_comm _ _
  have e : ∑ j, ((A l j : ℝ) * (α j + t * B k j) - (B l j : ℝ) * (β j + t * A k j)) =
      ∑ j, ((A l j : ℝ) * α j - (B l j : ℝ) * β j) +
        t * ∑ j, ((A l j : ℝ) * B k j - (B l j : ℝ) * A k j) := by
    rw [Finset.mul_sum, ← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl fun j _ => by ring
  rw [e, hg l, hsym]; ring

/-- **The modulus half of the gluing equations holds at a volume maximum.** -/
theorem logModulus_gluing {A B : Matrix ι ι ℤ} (hS : (A * Bᵀ).IsSymm) {α β : ι → ℝ}
    (h : IsVolMax A B α β) (k : ι) :
    ∑ j, ((A k j : ℝ) * (Real.log (Real.sin (β j)) - Real.log (Real.sin (α j + β j))) +
      (B k j : ℝ) * (Real.log (Real.sin (α j)) - Real.log (Real.sin (α j + β j)))) = 0 := by
  obtain ⟨hp, hg, hmax⟩ := h
  set u : ι → ℝ := fun j => (B k j : ℝ)
  set v : ι → ℝ := fun j => (A k j : ℝ)
  set g : ℝ → ℝ := fun t => totV (fun j => α j + t * u j) (fun j => β j + t * v j)
  have hev : ∀ᶠ t in 𝓝 (0 : ℝ), Pos (fun j => α j + t * u j) (fun j => β j + t * v j) := by
    refine eventually_all.2 fun j => ?_
    have cα : Continuous (fun t : ℝ => α j + t * u j) := by fun_prop
    have cβ : Continuous (fun t : ℝ => β j + t * v j) := by fun_prop
    have cs : Continuous (fun t : ℝ => (α j + t * u j) + (β j + t * v j)) := by fun_prop
    refine ((continuousAt_const.eventually_lt cα.continuousAt (by simpa using (hp j).1)).and
      ((continuousAt_const.eventually_lt cβ.continuousAt (by simpa using (hp j).2.1)).and
        (cs.continuousAt.eventually_lt continuousAt_const
          (by simpa using (hp j).2.2)))).mono fun t ht => ?_
    exact ⟨ht.1, ht.2.1, ht.2.2⟩
  have hloc : IsLocalMax g 0 := by
    refine hev.mono fun t ht => ?_
    have h0 : g 0 = totV α β := by simp [g]
    rw [h0]
    exact hmax _ _ ht (glue_line hS hg k t)
  have hd : HasDerivAt g (∑ j, -(u j * (Real.log (Real.sin (α j)) -
      Real.log (Real.sin (α j + β j))) + v j * (Real.log (Real.sin (β j)) -
      Real.log (Real.sin (α j + β j))))) 0 := by
    have : g = fun t => ∑ j ∈ Finset.univ, tetV (α j + t * u j) (β j + t * v j) := rfl
    rw [this]
    exact HasDerivAt.fun_sum fun j _ => hasDerivAt_tetV_line (hp j).1 (hp j).2.1 (hp j).2.2
  have hz := hloc.hasDerivAt_eq_zero hd
  rw [← neg_eq_zero, ← hz, ← Finset.sum_neg_distrib]
  exact Finset.sum_congr rfl fun j _ => by simp only [u, v]; ring

/-! ## The complex shapes -/

open Complex in
/-- The shape with argument `a` and modulus `sin b / sin(a + b)`, written as an
exponential. -/
def shapeExp (a b : ℝ) : ℂ :=
  ((Real.log (Real.sin b) - Real.log (Real.sin (a + b)) : ℝ) : ℂ) + (a : ℂ) * I

open Complex in
/-- The complementary shape `1 − z`, with argument `−b` and modulus `sin a / sin(a + b)`. -/
def shapeExp' (a b : ℝ) : ℂ :=
  ((Real.log (Real.sin a) - Real.log (Real.sin (a + b)) : ℝ) : ℂ) - (b : ℂ) * I

open Complex in
theorem exp_shapeExp {a b : ℝ} (ha : 0 < a) (hb : 0 < b) (hab : a + b < π) :
    cexp (shapeExp a b) =
      ((Real.sin b / Real.sin (a + b) : ℝ) : ℂ) * (Real.cos a + Real.sin a * I) := by
  have sb := Real.sin_pos_of_pos_of_lt_pi hb (by linarith)
  have sab := Real.sin_pos_of_pos_of_lt_pi (by linarith) hab
  rw [shapeExp, Complex.exp_add, ← Complex.ofReal_exp, Real.exp_sub, Real.exp_log sb,
    Real.exp_log sab, Complex.exp_mul_I, ← Complex.ofReal_cos, ← Complex.ofReal_sin]

open Complex in
theorem exp_shapeExp' {a b : ℝ} (ha : 0 < a) (hb : 0 < b) (hab : a + b < π) :
    cexp (shapeExp' a b) = 1 - cexp (shapeExp a b) := by
  have sa := Real.sin_pos_of_pos_of_lt_pi ha (by linarith)
  have sab := Real.sin_pos_of_pos_of_lt_pi (by linarith) hab
  rw [exp_shapeExp ha hb hab, shapeExp', sub_eq_add_neg, Complex.exp_add, ← Complex.ofReal_exp,
    Real.exp_sub, Real.exp_log sa, Real.exp_log sab, ← neg_mul, ← Complex.ofReal_neg,
    Complex.exp_mul_I, ← Complex.ofReal_cos, ← Complex.ofReal_sin]
  rw [Real.cos_neg, Real.sin_neg]
  apply Complex.ext <;> simp only [Complex.sub_re, Complex.sub_im, Complex.one_re, Complex.one_im, Complex.mul_re, Complex.mul_im, Complex.add_re, Complex.add_im, Complex.ofReal_re, Complex.ofReal_im, Complex.I_re, Complex.I_im] <;> field_simp <;> rw [Real.sin_add] <;> ring

open Complex in
theorem im_exp_shapeExp_pos {a b : ℝ} (ha : 0 < a) (hb : 0 < b) (hab : a + b < π) :
    0 < (cexp (shapeExp a b)).im := by
  have sa := Real.sin_pos_of_pos_of_lt_pi ha (by linarith)
  have sb := Real.sin_pos_of_pos_of_lt_pi hb (by linarith)
  have sab := Real.sin_pos_of_pos_of_lt_pi (by linarith) hab
  rw [exp_shapeExp ha hb hab]
  have e : (((Real.sin b / Real.sin (a + b) : ℝ) : ℂ) * (Real.cos a + Real.sin a * I)).im =
      Real.sin b / Real.sin (a + b) * Real.sin a := by
    simp only [Complex.sub_re, Complex.sub_im, Complex.one_re, Complex.one_im, Complex.mul_re, Complex.mul_im, Complex.add_re, Complex.add_im, Complex.ofReal_re, Complex.ofReal_im, Complex.I_re, Complex.I_im]; ring
  rw [e]; positivity



open Complex in
/-- **A volume maximum gives a solution of the gluing equations.** The shapes
`z_j = (sin β_j / sin(α_j + β_j)) · e^{i α_j}` satisfy
`∏_j z_j^{A_kj} (1 − z_j)^{B_kj} = 1` for every row and lie in the upper half plane. -/
theorem exists_nzSolution_of_isVolMax {A B : Matrix ι ι ℤ} (hS : (A * Bᵀ).IsSymm)
    {α β : ι → ℝ} (h : IsVolMax A B α β) :
    ∃ s : NeumannZagierBloch.NZSolution ℂ ι A B, ∀ j,
      (s.w j : ℂ) = cexp (shapeExp (α j) (β j)) ∧ 0 < (s.w j : ℂ).im := by
  have hp := h.1
  refine ⟨⟨fun j => Units.mk0 _ (Complex.exp_ne_zero (shapeExp (α j) (β j))),
    fun j => Units.mk0 _ (Complex.exp_ne_zero (shapeExp' (α j) (β j))),
    fun j => exp_shapeExp' (hp j).1 (hp j).2.1 (hp j).2.2, fun k => ?_⟩,
    fun j => ⟨rfl, im_exp_shapeExp_pos (hp j).1 (hp j).2.1 (hp j).2.2⟩⟩
  ext
  simp only [Units.coe_prod, Units.val_mul, Units.val_zpow_eq_zpow_val, Units.val_mk0,
    Units.val_one]
  simp_rw [← Complex.exp_int_mul, ← Complex.exp_add, ← Complex.exp_sum]
  rw [← Complex.exp_zero]
  congr 1
  have hm := logModulus_gluing hS h k
  have hg := h.2.1 k
  have e : ∑ j, ((A k j : ℂ) * shapeExp (α j) (β j) + (B k j : ℂ) * shapeExp' (α j) (β j)) =
      ((∑ j, ((A k j : ℝ) * (Real.log (Real.sin (β j)) - Real.log (Real.sin (α j + β j))) +
        (B k j : ℝ) * (Real.log (Real.sin (α j)) - Real.log (Real.sin (α j + β j)))) : ℝ) : ℂ) +
      ((∑ j, ((A k j : ℝ) * α j - (B k j : ℝ) * β j) : ℝ) : ℂ) * I := by
    push_cast
    rw [Finset.sum_mul, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun j _ => ?_
    simp only [shapeExp, shapeExp']
    push_cast
    ring
  rw [e, hm, hg]; simp

/-- **The regulator of a volume maximum is positive**, so its Bloch class is nonzero. -/
theorem regulator_pos_of_isVolMax [Nonempty ι] {A B : Matrix ι ι ℤ} (hS : (A * Bᵀ).IsSymm)
    {α β : ι → ℝ} (h : IsVolMax A B α β) :
    ∃ s : NeumannZagierBloch.NZSolution ℂ ι A B,
      0 < NahmRegulator.regulator (NeumannZagierBloch.nzClass s) := by
  obtain ⟨s, hs⟩ := exists_nzSolution_of_isVolMax hS h
  exact ⟨s, regulator_nzClass_pos s fun j => (hs j).2⟩

/-! ## A maximum exists on the closed polytope -/

/-- The closed angle polytope: angles `≥ 0` and `α + β ≤ π`, with the gluing rows. -/
def closedPolytope (A B : Matrix ι ι ℤ) : Set ((ι → ℝ) × (ι → ℝ)) :=
  {p | (∀ j, 0 ≤ p.1 j ∧ 0 ≤ p.2 j ∧ p.1 j + p.2 j ≤ π) ∧ Glue A B p.1 p.2}

theorem isClosed_closedPolytope (A B : Matrix ι ι ℤ) : IsClosed (closedPolytope A B) := by
  have h1 : IsClosed {p : (ι → ℝ) × (ι → ℝ) |
      ∀ j, 0 ≤ p.1 j ∧ 0 ≤ p.2 j ∧ p.1 j + p.2 j ≤ π} := by
    simp only [Set.setOf_forall, Set.setOf_and]
    refine isClosed_iInter fun j => ?_
    refine (isClosed_le continuous_const (by fun_prop)).inter
      ((isClosed_le continuous_const (by fun_prop)).inter
        (isClosed_le (by fun_prop) continuous_const))
  have h2 : IsClosed {p : (ι → ℝ) × (ι → ℝ) | Glue A B p.1 p.2} := by
    simp only [Glue, Set.setOf_forall]
    exact isClosed_iInter fun k => isClosed_eq (by fun_prop) continuous_const
  exact h1.inter h2

theorem isCompact_closedPolytope (A B : Matrix ι ι ℤ) : IsCompact (closedPolytope A B) := by
  refine Metric.isCompact_of_isClosed_isBounded (isClosed_closedPolytope A B) ?_
  refine (Metric.isBounded_iff_subset_closedBall 0).2 ⟨π, fun p hp => ?_⟩
  rw [Metric.mem_closedBall, dist_zero_right, Prod.norm_def, max_le_iff]
  have hb : ∀ j, |p.1 j| ≤ π ∧ |p.2 j| ≤ π := fun j => by
    obtain ⟨a, b, c⟩ := hp.1 j
    exact ⟨by rw [abs_of_nonneg a]; linarith, by rw [abs_of_nonneg b]; linarith⟩
  exact ⟨(pi_norm_le_iff_of_nonneg pi_pos.le).2 fun j => by
      rw [Real.norm_eq_abs]; exact (hb j).1,
    (pi_norm_le_iff_of_nonneg pi_pos.le).2 fun j => by rw [Real.norm_eq_abs]; exact (hb j).2⟩

theorem continuous_totV : Continuous fun p : (ι → ℝ) × (ι → ℝ) => totV p.1 p.2 := by
  unfold totV tetV
  refine continuous_finset_sum _ fun j _ => ?_
  exact ((continuous_Lob.comp (by fun_prop)).add (continuous_Lob.comp (by fun_prop))).sub
    (continuous_Lob.comp (by fun_prop))

/-- **The volume attains a maximum on the closed polytope**, whenever it is nonempty. -/
theorem exists_isMaxOn_closedPolytope {A B : Matrix ι ι ℤ}
    (hne : (closedPolytope A B).Nonempty) :
    ∃ p ∈ closedPolytope A B, IsMaxOn (fun q => totV q.1 q.2) (closedPolytope A B) p :=
  (isCompact_closedPolytope A B).exists_isMaxOn hne continuous_totV.continuousOn

/-- **Reduction to the boundary question.** If a maximum of the volume on the closed
polytope has every angle strictly inside `(0, π)`, it is a volume maximum over the angle
structures, so it gives an upper-half-plane solution of the gluing rows. -/
theorem exists_nzSolution_of_interior_max {A B : Matrix ι ι ℤ} (hS : (A * Bᵀ).IsSymm)
    {p : (ι → ℝ) × (ι → ℝ)} (hp : p ∈ closedPolytope A B)
    (hmax : IsMaxOn (fun q => totV q.1 q.2) (closedPolytope A B) p) (hint : Pos p.1 p.2) :
    ∃ s : NeumannZagierBloch.NZSolution ℂ ι A B, ∀ j,
      (s.w j : ℂ) = Complex.exp (shapeExp (p.1 j) (p.2 j)) ∧ 0 < (s.w j : ℂ).im := by
  have hv : IsVolMax A B p.1 p.2 := by
    refine ⟨hint, hp.2, fun α' β' h1 h2 => ?_⟩
    have hmem : (α', β') ∈ closedPolytope A B := by
      refine ⟨fun j => ?_, h2⟩
      exact ⟨(h1 j).1.le, (h1 j).2.1.le, (h1 j).2.2.le⟩
    have h3 := (isMaxOn_iff.1 hmax) (α', β') hmem
    exact h3
  exact exists_nzSolution_of_isVolMax hS hv

end

end QOU.Archimedean.NZVolumeCritical
