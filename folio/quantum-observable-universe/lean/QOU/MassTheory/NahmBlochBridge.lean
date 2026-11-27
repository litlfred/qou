import QOU.MassTheory.PreArchimedeanBloch

/-!
# A non-vacuous pre-Archimedean bridge: Nahm data define Bloch classes

`TetraplecticDilogBridgeVacuity` shows that the proposed `TetraplecticDilogBridge`
carries no content, because its shapes, its dilogarithm and its algebraic volume are
all chosen by whoever builds the instance. This file states the algebraic half of the
bridge with those three things **defined**:

* **Shapes come from the state sum.** A rank-`r` Nahm datum is a symmetric integer
  matrix `A`. Its shapes are the solutions `z : ι → F^×` of the Nahm equations
  `1 − z_i = ∏_j z_j ^ A_ij` (`NahmSolution`). They are forced by `A`, not chosen.
* **The dilogarithm is the Bloch generator.** Each shape contributes `[z_i] ∈ P(F)`,
  the class of `gen (z i)` in Suslin's pre-Bloch group (`PreArchimedeanBloch.PreBloch`).
* **The algebraic volume is the sum.** `nahmClass s = ∑_i [z_i]`.

**Theorem** (`nahmClass_mem_blochGroup`): for every symmetric `A` and every solution,
`nahmClass s ∈ B(F) = ker (P(F) → Λ²_ℤ F^×)`. More generally Suslin's symbol of
`∑_i [z_i]` vanishes for every alternating pairing (`delta_nahmSum`). The proof is
one line of algebra: `δ ∑ [z_i] = ∑_{i,j} A_ij · z_i ∧ z_j`, which is zero because `A`
is symmetric and `∧` is alternating. There is no `ℝ`, no `ℂ` and no limit.

**It has content.** The conclusion is not automatic: `delta_gen_three_ne_zero` shows
`δ[3] ≠ 0` over `ℚ` for the alternating pairing `v₂ ∧ v₃`, so an arbitrary shape
does not give a Bloch class. And the shapes have no freedom: for the rank-one datum
`A = (−1)` the solutions are exactly the roots of `X² − X + 1`
(`nahmNegOne_iff_phi6`).

**The figure-eight knot.** The `q → 1` shift ratio of Habiro's `4₁` summand gives
the rank-one datum `A = (−1)` (`habiro41_nahm_iff`). The two-tetrahedron class
`fig8Class ζ = 2[ζ]` is the Nahm class of the rank-two datum `A = −I` at `(ζ, ζ)`
(`fig8Class_eq_nahmClass`).

## Scope

This is the pre-Archimedean statement only. The regulator `D` and the hyperbolic
volume belong to a separate Archimedean statement and are not assumed here. Which Nahm
datum the tetraplectic (Φ_b double `sinh`-lattice) state sum of a given knot produces
is not derived here except for `4₁`, where it is read off Habiro's summand. That the
class agrees with the Ptolemy / gluing-equation class for other knots is open, as in
`docs/audits/2026-11-27-dilog-bloch-pre-archimedean.md`.

-- Ref: [nahm2007] Nahm, Conformal field theory and torsion elements of the Bloch group, in Frontiers in Number Theory, Physics and Geometry II (2007) 67-132.
-- Ref: [zagier-dilogarithm] Zagier, The dilogarithm function, in Frontiers in Number Theory, Physics and Geometry II (2007), §II.3.
-- Ref: [suslin1991] Suslin, K_3 of a field, and the Bloch group, Trudy Mat. Inst. Steklova 183 (1991) 217-239.
-/

namespace QOU.Archimedean.NahmBlochBridge

open QOU.Archimedean.PreArchimedeanBloch QOU.Archimedean.SubstantiveFillers

set_option linter.unusedSectionVars false

noncomputable section

/-! ## A double sum of an antisymmetric array vanishes -/

/-- If `f j i = − f i j` and `f i i = 0`, then `∑_i ∑_j f i j = 0`. -/
theorem sum_sum_eq_zero_of_antisymm {ι G : Type*} [Fintype ι] [AddCommGroup G]
    (f : ι → ι → G) (hanti : ∀ i j, f j i = - f i j) (hdiag : ∀ i, f i i = 0) :
    ∑ i, ∑ j, f i j = 0 := by
  rw [← Fintype.sum_prod_type']
  refine Finset.sum_involution (fun p _ => p.swap) ?_ ?_ (fun _ _ => Finset.mem_univ _)
    (fun _ _ => Prod.swap_swap _)
  · rintro ⟨i, j⟩ _
    simp [hanti i j]
  · rintro ⟨i, j⟩ _ hne heq
    have hij : j = i := (Prod.ext_iff.1 heq).1
    subst hij
    exact hne (hdiag j)

variable {F : Type*} [Field F] [DecidableEq F]
variable {G : Type*} [AddCommGroup G]

/-- An alternating biadditive pairing is antisymmetric. -/
theorem antisymm_of_alternating (β : Additive Fˣ →+ Additive Fˣ →+ G)
    (hβ : ∀ a, β a a = 0) (a b : Additive Fˣ) : β b a = - β a b := by
  have h := hβ (a + b)
  simp only [map_add, AddMonoidHom.add_apply, hβ a, hβ b, zero_add, add_zero] at h
  exact eq_neg_of_add_eq_zero_left h

/-- On a unit, `u` is `Additive.ofMul`. -/
theorem u_units (v : Fˣ) : u (v : F) = Additive.ofMul v := by
  simp [u, v.ne_zero]

/-! ## Nahm data and their solutions -/

/-- A solution of the Nahm equations `1 − z_i = ∏_j z_j ^ A_ij` of an integer
matrix `A`, with every shape a unit. -/
structure NahmSolution (F : Type*) [Field F] (ι : Type*) [Fintype ι]
    (A : Matrix ι ι ℤ) where
  /-- The shapes. -/
  w : ι → Fˣ
  /-- The Nahm equations. -/
  nahm : ∀ i, (1 : F) - w i = ((∏ j, w j ^ A i j : Fˣ) : F)

variable {ι : Type*} [Fintype ι] {A : Matrix ι ι ℤ}

/-- No shape equals `1`: the right-hand side of each Nahm equation is a unit. -/
theorem NahmSolution.ne_one (s : NahmSolution F ι A) (i : ι) : (s.w i : F) ≠ 1 := by
  intro h
  have := s.nahm i
  rw [h, sub_self] at this
  exact (Units.ne_zero _) this.symm

/-- The Nahm class `∑_i [z_i]` on the free group. -/
def nahmSum (s : NahmSolution F ι A) : PreBlochGroup F :=
  ∑ i, gen (s.w i : F)

/-- The Nahm class `∑_i [z_i] ∈ P(F)`. -/
def nahmClass (s : NahmSolution F ι A) : PreBloch F :=
  QuotientAddGroup.mk (nahmSum s)

/-- Suslin's symbol of one shape: `δ[z_i] = ∑_j A_ij · β(z_i, z_j)`. -/
theorem delta_gen_nahm (β : Additive Fˣ →+ Additive Fˣ →+ G)
    (s : NahmSolution F ι A) (i : ι) :
    delta β (gen (s.w i : F)) =
      ∑ j, A i j • β (Additive.ofMul (s.w i)) (Additive.ofMul (s.w j)) := by
  rw [delta_gen β (s.w i).ne_zero (s.ne_one i), s.nahm i, u_units, u_units, ofMul_prod,
    map_sum]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [ofMul_zpow, map_zsmul]

/-- **Nahm ⇒ Bloch, for every alternating pairing.** If `A` is symmetric, Suslin's
symbol of `∑_i [z_i]` vanishes for every alternating biadditive `β`. -/
theorem delta_nahmSum (β : Additive Fˣ →+ Additive Fˣ →+ G) (hβ : ∀ a, β a a = 0)
    (hA : A.IsSymm) (s : NahmSolution F ι A) :
    delta β (nahmSum s) = 0 := by
  rw [nahmSum, map_sum]
  simp_rw [delta_gen_nahm β s]
  refine sum_sum_eq_zero_of_antisymm _ (fun i j => ?_) (fun i => ?_)
  · rw [antisymm_of_alternating β hβ, smul_neg, show A j i = A i j from hA.apply i j]
  · rw [hβ, smul_zero]

/-- **The non-vacuous bridge, pre-Archimedean half.** For a symmetric Nahm datum, the
Nahm class of every solution lies in the Bloch group `B(F)`. -/
theorem nahmClass_mem_blochGroup (hA : A.IsSymm) (s : NahmSolution F ι A) :
    nahmClass s ∈ BlochGroup F := by
  simp only [BlochGroup, AddMonoidHom.mem_ker, nahmClass, deltaP_mk]
  exact delta_nahmSum (wedge F) (wedge_self) hA s

/-! ## The conclusion is not automatic -/

private theorem pv (p n : ℕ) [Fact p.Prime] (k : ℕ) (h : padicValNat p n = k) :
    padicValRat p ((n : ℕ) : ℚ) = k := by
  rw [padicValRat.of_nat, h]

/-- `v₂ ∧ v₃` is alternating. -/
theorem v23_self (a : Additive ℚˣ) : v23 a a = 0 := by
  simp only [v23, AddMonoidHom.mk'_apply]
  ring

/-- **An arbitrary shape is not a Bloch class.** Over `ℚ`, `δ[3] = 3 ∧ (−2)` has
`v₂ ∧ v₃`-symbol `−1`. So the conclusion of `delta_nahmSum` is false for the single
shape `3`: membership in `B(F)` is a real constraint, which the Nahm equations
supply. -/
theorem delta_gen_three : delta v23 (gen (3 : ℚ)) = -1 := by
  rw [delta_gen v23 (z := (3 : ℚ)) (by norm_num) (by norm_num),
    show (1 : ℚ) - 3 = -2 by norm_num]
  have h3 : (3 : ℚ) ≠ 0 := by norm_num
  have h2 : (-2 : ℚ) ≠ 0 := by norm_num
  have e23 : padicValRat 2 (3 : ℚ) = 0 := by
    have := pv 2 3 0 (by simp [padicValNat.eq_zero_of_not_dvd]); exact_mod_cast this
  have e33 : padicValRat 3 (3 : ℚ) = 1 := by
    have := pv 3 3 1 (by simp); exact_mod_cast this
  have e22 : padicValRat 2 (2 : ℚ) = 1 := by
    have := pv 2 2 1 (by simp); exact_mod_cast this
  simp [v23, vp, u, h3, h2, padicValRat.neg, e23, e33, e22]

theorem delta_gen_three_ne_zero : delta v23 (gen (3 : ℚ)) ≠ 0 := by
  rw [delta_gen_three]
  norm_num

/-! ## The figure-eight knot -/

/-- The rank-one Nahm datum `A = (−1)`. -/
def negOne : Matrix Unit Unit ℤ := fun _ _ => -1

theorem negOne_isSymm : negOne.IsSymm := Matrix.IsSymm.ext fun _ _ => rfl

/-- **The shapes are forced.** A unit `z` solves the Nahm equation of `A = (−1)`,
`1 − z = z⁻¹`, exactly when `z² − z + 1 = 0`. -/
theorem nahmNegOne_iff_phi6 (z : Fˣ) :
    (1 : F) - z = ((z ^ (-1 : ℤ) : Fˣ) : F) ↔ (z : F) ^ 2 - z + 1 = 0 := by
  have hz : (z : F) ≠ 0 := z.ne_zero
  rw [zpow_neg_one, Units.val_inv_eq_inv_val]
  constructor
  · intro h
    have : (z : F) * (1 - z) = z * (z : F)⁻¹ := by rw [h]
    rw [mul_inv_cancel₀ hz] at this
    linear_combination -this
  · intro h
    field_simp
    linear_combination -h

/-- **The `4₁` Habiro sum gives the datum `A = (−1)`.** Its `q → 1` shift ratio
`(1 − X)(1 − X⁻¹)` equals `1` exactly when `X` solves the Nahm equation of `(−1)`. -/
theorem habiro41_nahm_iff (z : Fˣ) :
    (1 - (z : F)) * (1 - (z : F)⁻¹) = 1 ↔ (1 : F) - z = ((z ^ (-1 : ℤ) : Fˣ) : F) := by
  rw [nahm41_iff_phi6 z.ne_zero, nahmNegOne_iff_phi6]

/-- The Nahm solution of `A = (−1)` at a root of `X² − X + 1`. -/
def fig8Nahm {ζ : F} (h : ζ ^ 2 - ζ + 1 = 0) : NahmSolution F Unit negOne where
  w _ := Units.mk0 ζ (phi6_facts h).1
  nahm _ := by
    simp only [negOne, Finset.univ_unique, Finset.prod_singleton]
    exact (nahmNegOne_iff_phi6 (Units.mk0 ζ (phi6_facts h).1)).2 h

/-- The rank-two datum `A = −I`: two tetrahedra, no interaction. -/
def negId : Matrix (Fin 2) (Fin 2) ℤ := -1

theorem negId_isSymm : negId.IsSymm := by
  simp [negId, Matrix.IsSymm]

/-- The Nahm solution of `A = −I` at `(ζ, ζ)`. -/
def fig8Nahm2 {ζ : F} (h : ζ ^ 2 - ζ + 1 = 0) : NahmSolution F (Fin 2) negId where
  w _ := Units.mk0 ζ (phi6_facts h).1
  nahm i := by
    have key := (nahmNegOne_iff_phi6 (F := F) (Units.mk0 ζ (phi6_facts h).1)).2 h
    rw [key]
    congr 1
    fin_cases i <;> simp [negId, Matrix.one_apply]

/-- **The two-tetrahedron class is a Nahm class:** `fig8Class ζ = 2[ζ]` is the Nahm
class of `A = −I` at `(ζ, ζ)`. -/
theorem fig8Class_eq_nahmClass {ζ : F} (h : ζ ^ 2 - ζ + 1 = 0) :
    fig8Class ζ = nahmClass (fig8Nahm2 h) := by
  simp only [fig8Class, nahmClass, nahmSum, fig8Nahm2, Units.val_mk0, Finset.sum_const,
    Finset.card_univ, Fintype.card_fin, QuotientAddGroup.mk_nsmul]

/-- `fig8Class_mem_blochGroup` recovered from the general theorem. -/
theorem fig8Class_mem_blochGroup' {ζ : F} (h : ζ ^ 2 - ζ + 1 = 0) :
    fig8Class ζ ∈ BlochGroup F := by
  rw [fig8Class_eq_nahmClass h]
  exact nahmClass_mem_blochGroup negId_isSymm _

end

end QOU.Archimedean.NahmBlochBridge
