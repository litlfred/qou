import QOU.KZ.SmallHbar
import QOU.KZ.KZFunctorial
import QOU.KZ.KZHexagonCentral
import QOU.KZ.GLnKZ

/-!
# The zigzag scalar of `D_ℏ` on `V = ℂ²` is nonzero for `|ℏ| ≤ 1/12`

Stage S4 of bean `qou-zoyv` (duals of the Drinfeld category), small-`ℏ` route.

Let `ε : V ⊗ V → ℂ` be the `SL₂`-invariant form `ε(e₀ ⊗ e₁) = 1 = −ε(e₁ ⊗ e₀)`, and
`η : ℂ → V ⊗ V` the invariant vector `e₀ ⊗ e₁ − e₁ ⊗ e₀`. In `D_ℏ` the associator on `V^{⊗3}` is
`Φ = Φ_KZ(ℏ P₁₂, ℏ P₂₃)`, so the two zigzags are

* `zig(Φ) = (1 ⊗ ε) ∘ Φ ∘ (η ⊗ 1)` (matrices `E1 · Φ · E2`), and
* `zag(Φ⁻¹) = (ε ⊗ 1) ∘ Φ⁻¹ ∘ (1 ⊗ η)` (matrices `E1' · Φ(B, A) · E2'`).

Proved here, for `|ℏ| ≤ 1/12`:

* `zig_scalar`: `zig(Φ) = ν · 1`. `Φ` commutes with `g^{⊗3}`, and `ε`, `η` are `SL₂`-invariant,
  so `zig(Φ)` commutes with the two unipotent generators of `SL₂`.
* `zag_eq_zig`: the second zigzag equals the first. Conjugation by the flip `P₁₃` exchanges
  `Φ(A, B)` and `Φ(B, A)` (`KZFunctorial.map_Φ`), and turns `E1, E2` into `−E1', −E2'`.
* `zig_ne_zero`: `ν ≠ 0`. `zig(1) = −1` and `‖zig(Φ) − zig(1)‖ ≤ 2 ‖Φ − 1‖ < 1`
  (`SmallHbar.norm_Φ_sub_one_lt_half`).

Hence `(η, ν⁻¹ ε)` satisfies both zigzag identities. The radius `1/12` is explicit; for
comparison (not used in any proof) the framework pin `q₀ ≈ 1.10998` corresponds to
`|ℏ₀| = log q₀ / π ≈ 0.0332 < 1/12`. Non-resonance of the residues is automatic for
`|ℏ| < 1/2` (`nonResonant_of_norm_lt`), so no arithmetic condition on `ℏ` is needed. Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S4)
-/

noncomputable section

namespace QOU.KZ.ZigZag

open Finset QOU.KZ.FuchsianFormal QOU.KZ.GLnResidues QOU.KZ.GLnKZ

/-! ### Enumerating `(Fin 3 → Fin 2)` -/

/-- `Fin 2 × Fin 2 × Fin 2 ≃ (Fin 3 → Fin 2)`. -/
def e3 : Fin 2 × Fin 2 × Fin 2 ≃ (Fin 3 → Fin 2) where
  toFun p := ![p.1, p.2.1, p.2.2]
  invFun x := (x 0, x 1, x 2)
  left_inv p := by simp
  right_inv x := by funext i; fin_cases i <;> rfl

theorem sum3 {M : Type*} [AddCommMonoid M] (f : (Fin 3 → Fin 2) → M) :
    ∑ x, f x = ∑ i : Fin 2, ∑ j : Fin 2, ∑ k : Fin 2, f ![i, j, k] := by
  rw [← e3.sum_comp, Fintype.sum_prod_type,
    Fintype.sum_congr _ _ (fun _ => Fintype.sum_prod_type _)]
  rfl

theorem forall3 {p : (Fin 3 → Fin 2) → Prop} (h : ∀ i j k : Fin 2, p ![i, j, k]) : ∀ x, p x := by
  intro x
  have := h (x 0) (x 1) (x 2)
  have e : ![x 0, x 1, x 2] = x := e3.right_inv x
  rwa [e] at this

/-! ### The invariant form and the zigzag matrices -/

/-- `ε`, as a matrix of coefficients: `ε(e₀ ⊗ e₁) = 1`, `ε(e₁ ⊗ e₀) = −1`. -/
def eps : Matrix (Fin 2) (Fin 2) ℂ := !![0, 1; -1, 0]

/-- `1 ⊗ ε : V^{⊗3} → V`. -/
def E1 : Matrix (Fin 2) (Fin 3 → Fin 2) ℂ := Matrix.of fun a x => if x 0 = a then eps (x 1) (x 2) else 0
/-- `η ⊗ 1 : V → V^{⊗3}`. -/
def E2 : Matrix (Fin 3 → Fin 2) (Fin 2) ℂ := Matrix.of fun y b => if y 2 = b then eps (y 0) (y 1) else 0
/-- `ε ⊗ 1 : V^{⊗3} → V`. -/
def E1' : Matrix (Fin 2) (Fin 3 → Fin 2) ℂ := Matrix.of fun a x => if x 2 = a then eps (x 0) (x 1) else 0
/-- `1 ⊗ η : V → V^{⊗3}`. -/
def E2' : Matrix (Fin 3 → Fin 2) (Fin 2) ℂ := Matrix.of fun y b => if y 0 = b then eps (y 1) (y 2) else 0

/-- The first zigzag `(1 ⊗ ε) ∘ M ∘ (η ⊗ 1)`. -/
def zig (M : Matrix (Fin 3 → Fin 2) (Fin 3 → Fin 2) ℂ) : Matrix (Fin 2) (Fin 2) ℂ := E1 * M * E2
/-- The second zigzag `(ε ⊗ 1) ∘ M ∘ (1 ⊗ η)`. -/
def zag (M : Matrix (Fin 3 → Fin 2) (Fin 3 → Fin 2) ℂ) : Matrix (Fin 2) (Fin 2) ℂ := E1' * M * E2'

theorem zig_one : zig 1 = -1 := by
  ext a b
  simp only [zig, Matrix.mul_one, Matrix.mul_apply, E1, E2, Matrix.of_apply]
  rw [sum3]
  fin_cases a <;> fin_cases b <;> simp [eps, Fin.sum_univ_two]

theorem zag_one : zag 1 = -1 := by
  ext a b
  simp only [zag, Matrix.mul_one, Matrix.mul_apply, E1', E2', Matrix.of_apply]
  rw [sum3]
  fin_cases a <;> fin_cases b <;> simp [eps, Fin.sum_univ_two]

/-! ### Equivariance under `SL₂` -/

/-- `g^{⊗3}` on `V^{⊗3}`. -/
def G3 (g : Matrix (Fin 2) (Fin 2) ℂ) : Matrix (Fin 3 → Fin 2) (Fin 3 → Fin 2) ℂ :=
  Matrix.of fun x y => ∏ i, g (x i) (y i)

/-- `g^{⊗3}` commutes with every permutation of the tensor legs. -/
theorem commute_permP_G3 (σ : Equiv.Perm (Fin 3)) (g : Matrix (Fin 2) (Fin 2) ℂ) :
    Commute (permP ℂ 2 σ) (G3 g) := by
  show permP ℂ 2 σ * G3 g = G3 g * permP ℂ 2 σ
  ext x y
  simp only [Matrix.mul_apply, permP, permMat, G3, Matrix.of_apply, ite_mul, one_mul, zero_mul,
    mul_ite, mul_one, mul_zero]
  have h1 : ∀ z : Fin 3 → Fin 2, (z ∘ σ = x ↔ z = x ∘ σ.symm) := fun z => by
    constructor
    · rintro rfl; funext i; simp
    · rintro rfl; funext i; simp
  simp only [h1, Finset.sum_ite_eq', Finset.mem_univ, if_true]
  rw [Finset.sum_ite_eq Finset.univ (y ∘ σ)]
  simp only [Finset.mem_univ, if_true]
  rw [← Equiv.prod_comp σ]
  simp

theorem E1_G3' (g : Matrix (Fin 2) (Fin 2) ℂ) :
    E1 * G3 g = (g 0 0 * g 1 1 - g 0 1 * g 1 0) • (g * E1) := by
  ext a y
  revert y
  refine forall3 fun i j k => ?_
  simp only [Matrix.mul_apply, Matrix.smul_apply, E1, G3, Matrix.of_apply, smul_eq_mul]
  rw [sum3]
  fin_cases a <;> fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [eps, Fin.sum_univ_two, Fin.prod_univ_three] <;> ring

theorem G3_E2' (g : Matrix (Fin 2) (Fin 2) ℂ) :
    G3 g * E2 = (g 0 0 * g 1 1 - g 0 1 * g 1 0) • (E2 * g) := by
  ext y b
  revert y
  refine forall3 fun i j k => ?_
  simp only [Matrix.mul_apply, Matrix.smul_apply, E2, G3, Matrix.of_apply, smul_eq_mul]
  rw [sum3]
  fin_cases b <;> fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [eps, Fin.sum_univ_two, Fin.prod_univ_three] <;> ring

/-- If `M` commutes with `g^{⊗3}` and `det g = 1`, then `zig M` commutes with `g`. -/
theorem zig_mul_comm (M : Matrix (Fin 3 → Fin 2) (Fin 3 → Fin 2) ℂ) (g : Matrix (Fin 2) (Fin 2) ℂ)
    (hg : g 0 0 * g 1 1 - g 0 1 * g 1 0 = 1) (hM : Commute (G3 g) M) :
    zig M * g = g * zig M := by
  have h1 := E1_G3' g
  have h2 := G3_E2' g
  rw [hg, one_smul] at h1 h2
  simp only [zig]
  calc E1 * M * E2 * g = E1 * (M * G3 g) * E2 := by
        rw [Matrix.mul_assoc, ← h2]; simp only [Matrix.mul_assoc]
    _ = E1 * G3 g * M * E2 := by rw [← hM.eq]; simp only [Matrix.mul_assoc]
    _ = g * (E1 * M * E2) := by rw [h1]; simp only [Matrix.mul_assoc]

/-- A `2 × 2` matrix commuting with both unipotent generators of `SL₂` is scalar. -/
theorem eq_smul_one_of_commute (Z : Matrix (Fin 2) (Fin 2) ℂ)
    (hu : Z * !![1, 1; 0, 1] = !![1, 1; 0, 1] * Z) (hl : Z * !![1, 0; 1, 1] = !![1, 0; 1, 1] * Z) :
    Z = Z 0 0 • 1 := by
  have u01 := congrFun (congrFun hu 0) 1
  have u11 := congrFun (congrFun hu 1) 1
  have l00 := congrFun (congrFun hl 0) 0
  have u00 := congrFun (congrFun hu 0) 0
  simp [Matrix.mul_apply, Fin.sum_univ_two] at u01 u11 l00 u00
  ext i j
  fin_cases i <;> fin_cases j <;> simp [Matrix.one_apply] <;>
    first | exact l00 | exact u00 | linear_combination (-1 : ℂ) * u01

/-! ### Norms and small-residue non-resonance -/

section Norms

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra
  Matrix.linfty_opNormOneClass Matrix.linftyOpNormedAddCommGroup Matrix.linftyOpNormedSpace

theorem norm_permP_le {m n : ℕ} (σ : Equiv.Perm (Fin m)) : ‖permP ℂ n σ‖ ≤ 1 := by
  rw [Matrix.linfty_opNorm_def]
  have : (Finset.univ.sup fun i : Fin m → Fin n => ∑ j, ‖permP ℂ n σ i j‖₊) ≤ 1 := by
    refine Finset.sup_le fun i _ => ?_
    have h1 : ∀ j : Fin m → Fin n, (j ∘ σ = i ↔ j = i ∘ σ.symm) := fun j => by
      constructor
      · rintro rfl; funext t; simp
      · rintro rfl; funext t; simp
    simp only [permP, permMat, Matrix.of_apply, h1]
    rw [Finset.sum_congr rfl fun j _ => (apply_ite (fun x : ℂ => ‖x‖₊) _ _ _)]
    simp
  exact_mod_cast this

/-- **Small residues are non-resonant.** If `2‖A‖ < 1` then every `k − ad_A` (`k ≥ 1`) is
bijective: injective by the norm estimate, surjective by finite dimension. -/
theorem nonResonant_of_norm_lt {ι : Type*} [Fintype ι] [DecidableEq ι] (A : Matrix ι ι ℂ)
    (h : 2 * ‖A‖ < 1) : NonResonant A := by
  intro k hk
  let L : Matrix ι ι ℂ →ₗ[ℂ] Matrix ι ι ℂ :=
    { toFun := indicial A k
      map_add' := fun X Y => by simp only [indicial, ad]; noncomm_ring
      map_smul' := fun c X => by
        simp only [indicial, ad, RingHom.id_apply, smul_sub, Matrix.mul_smul, Matrix.smul_mul] }
  have hinj : Function.Injective L := by
    rw [← LinearMap.ker_eq_bot, LinearMap.ker_eq_bot']
    intro X hX
    have hX' : indicial A k X = 0 := hX
    have hk1 : (1 : ℝ) ≤ k := by exact_mod_cast hk
    have e : (k : Matrix ι ι ℂ) * X = (k : ℂ) • X := by
      rw [← nsmul_eq_mul, ← Nat.cast_smul_eq_nsmul ℂ]
    have h1 : ‖(k : Matrix ι ι ℂ) * X‖ = k * ‖X‖ := by
      rw [e, norm_smul, Complex.norm_natCast]
    have h2 : (k : Matrix ι ι ℂ) * X = ad A X := by
      have := hX'; simp only [indicial] at this; exact sub_eq_zero.1 this
    have h3 := FuchsianConvergence.norm_ad_le A X
    have : (k : ℝ) * ‖X‖ ≤ 2 * ‖A‖ * ‖X‖ := by rw [← h1, h2]; exact h3
    have hXn := norm_nonneg X
    have : ‖X‖ = 0 := by nlinarith
    exact norm_eq_zero.1 this
  exact ⟨hinj, LinearMap.injective_iff_surjective.1 hinj⟩

theorem norm_E1_le : ‖E1‖ ≤ 2 := by
  rw [Matrix.linfty_opNorm_def]
  have : (Finset.univ.sup fun a : Fin 2 => ∑ x, ‖E1 a x‖₊) ≤ 2 := by
    refine Finset.sup_le fun a _ => ?_
    rw [sum3]
    fin_cases a <;> simp [E1, eps, Fin.sum_univ_two] <;> norm_num
  exact_mod_cast this

theorem norm_E2_le : ‖E2‖ ≤ 1 := by
  rw [Matrix.linfty_opNorm_def]
  have : (Finset.univ.sup fun y : Fin 3 → Fin 2 => ∑ b, ‖E2 y b‖₊) ≤ 1 := by
    refine Finset.sup_le fun y _ => ?_
    revert y
    refine forall3 fun i j k => ?_
    fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [E2, eps, Fin.sum_univ_two]
  exact_mod_cast this

/-- `‖zig M − zig 1‖ ≤ 2 ‖M − 1‖`. -/
theorem norm_zig_sub_le (M : Matrix (Fin 3 → Fin 2) (Fin 3 → Fin 2) ℂ) :
    ‖zig M - zig 1‖ ≤ 2 * ‖M - 1‖ := by
  have e : zig M - zig 1 = E1 * (M - 1) * E2 := by
    simp only [zig, Matrix.mul_sub, Matrix.sub_mul]
  rw [e]
  calc ‖E1 * (M - 1) * E2‖ ≤ ‖E1 * (M - 1)‖ * ‖E2‖ := Matrix.linfty_opNorm_mul _ _
    _ ≤ (‖E1‖ * ‖M - 1‖) * 1 := by
        gcongr
        · exact Matrix.linfty_opNorm_mul _ _
        · exact norm_E2_le
    _ ≤ 2 * ‖M - 1‖ := by rw [mul_one]; gcongr; exact norm_E1_le

end Norms

/-! ### The zigzag scalar of the KZ associator -/

section Main

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra
  Matrix.linfty_opNormOneClass

variable {c : ℂ}

theorem norm_smul_P_le {m : ℕ} (i j : Fin m) : ‖c • P 2 i j‖ ≤ ‖c‖ := by
  rw [norm_smul]
  exact mul_le_of_le_one_right (norm_nonneg _) (norm_permP_le _)

/-- The residues are non-resonant for `|ℏ| < 1/2`. -/
theorem nonResonant_smul_P_small {m : ℕ} (i j : Fin m) (hc : ‖c‖ < 1 / 2) :
    NonResonant (c • P 2 i j) :=
  nonResonant_of_norm_lt _ (by linarith [norm_smul_P_le (c := c) i j])

/-- The associator `Φ = Φ_KZ(ℏ P₁₂, ℏ P₂₃)` of `D_ℏ` on `V^{⊗3}`, `V = ℂ²`, for `|ℏ| < 1/2`. -/
def assoc (hc : ‖c‖ < 1 / 2) : Matrix (Fin 3 → Fin 2) (Fin 3 → Fin 2) ℂ :=
  KZPentagon.Φ (c • P 2 (0 : Fin 3) 1) (c • P 2 1 2) (nonResonant_smul_P_small 0 1 hc)
    (nonResonant_smul_P_small 1 2 hc)

/-- Its inverse `Φ(ℏ P₂₃, ℏ P₁₂)`. -/
def assocInv (hc : ‖c‖ < 1 / 2) : Matrix (Fin 3 → Fin 2) (Fin 3 → Fin 2) ℂ :=
  KZPentagon.Φ (c • P 2 (1 : Fin 3) 2) (c • P 2 0 1) (nonResonant_smul_P_small 1 2 hc)
    (nonResonant_smul_P_small 0 1 hc)

theorem assoc_mul_assocInv (hc : ‖c‖ < 1 / 2) :
    assoc hc * assocInv hc = 1 ∧ assocInv hc * assoc hc = 1 :=
  ⟨(KZShiftPhi.Φ_swap_mul _ _ _ _).2, (KZShiftPhi.Φ_swap_mul _ _ _ _).1⟩

/-- **The first zigzag is a scalar**: `zig(Φ) = ν · 1`, `ν = zig(Φ)₀₀`. -/
theorem zig_scalar (hc : ‖c‖ < 1 / 2) : zig (assoc hc) = zig (assoc hc) 0 0 • 1 := by
  have hcomm : ∀ g : Matrix (Fin 2) (Fin 2) ℂ, Commute (G3 g) (assoc hc) := fun g =>
    KZHexagonCentral.commute_Φ _ _ ((commute_permP_G3 _ g).symm.smul_right c)
      ((commute_permP_G3 _ g).symm.smul_right c)
  exact eq_smul_one_of_commute _
    (zig_mul_comm _ _ (by simp) (hcomm _)) (zig_mul_comm _ _ (by simp) (hcomm _))

/-- **The zigzag scalar is nonzero for `|ℏ| ≤ 1/12`.** -/
theorem zig_ne_zero (hc : ‖c‖ ≤ 1 / 12) :
    zig (assoc (c := c) (by linarith)) 0 0 ≠ 0 := by
  have hc' : ‖c‖ < 1 / 2 := by linarith
  have hΦ : ‖assoc hc' - 1‖ < 1 / 2 :=
    SmallHbar.norm_Φ_sub_one_lt_half _ _ _ _ (norm_smul_P_le 0 1) (norm_smul_P_le 1 2) hc
  have hb := (norm_zig_sub_le (assoc hc')).trans_lt (by linarith : 2 * ‖assoc hc' - 1‖ < 1)
  rw [zig_scalar hc', zig_one, sub_neg_eq_add] at hb
  intro hν
  have hν' : zig (assoc hc') 0 0 = 0 := hν
  rw [hν', zero_smul, zero_add, norm_one] at hb
  exact lt_irrefl _ hb

/-- Conjugation by the flip `P₁₃` of the outer legs, as a `ℂ`-algebra map. -/
def conj13 : Matrix (Fin 3 → Fin 2) (Fin 3 → Fin 2) ℂ →ₐ[ℂ]
    Matrix (Fin 3 → Fin 2) (Fin 3 → Fin 2) ℂ where
  toFun X := P 2 (0 : Fin 3) 2 * X * P 2 0 2
  map_one' := by rw [Matrix.mul_one, P_mul_self]
  map_mul' X Y := by
    rw [show P 2 (0 : Fin 3) 2 * (X * Y) * P 2 0 2 =
      P 2 0 2 * X * (P 2 0 2 * P 2 0 2) * Y * P 2 0 2 by rw [P_mul_self]; simp only [Matrix.mul_one,
        Matrix.mul_assoc]]
    simp only [Matrix.mul_assoc]
  map_zero' := by simp
  map_add' X Y := by simp [Matrix.mul_add, Matrix.add_mul]
  commutes' r := by
    simp only [Algebra.algebraMap_eq_smul_one, Matrix.mul_smul, Matrix.smul_mul, Matrix.mul_one,
      P_mul_self]

theorem continuous_conj13 : Continuous conj13 :=
  LinearMap.continuous_of_finiteDimensional conj13.toLinearMap

theorem conj13_A : conj13 (c • P 2 (0 : Fin 3) 1) = c • P 2 1 2 := by
  show P 2 (0 : Fin 3) 2 * (c • P 2 0 1) * P 2 0 2 = c • P 2 1 2
  rw [Matrix.mul_smul, Matrix.smul_mul, P_mul_P, P, flipP, permP_mul]
  congr 2
  decide

theorem conj13_B : conj13 (c • P 2 (1 : Fin 3) 2) = c • P 2 0 1 := by
  show P 2 (0 : Fin 3) 2 * (c • P 2 1 2) * P 2 0 2 = c • P 2 0 1
  rw [Matrix.mul_smul, Matrix.smul_mul, P_mul_P, P, flipP, permP_mul]
  congr 2
  decide

/-- Conjugation by `P₁₃` exchanges `Φ(A, B)` and `Φ(B, A)`. -/
theorem conj13_assoc (hc : ‖c‖ < 1 / 2) : conj13 (assoc hc) = assocInv hc := by
  unfold assoc assocInv
  rw [KZFunctorial.map_Φ conj13 continuous_conj13 _ _ _ _
    (by rw [conj13_A]; exact nonResonant_smul_P_small 1 2 hc)
    (by rw [conj13_B]; exact nonResonant_smul_P_small 0 1 hc)]
  exact KZShiftPhi.Φ_congr conj13_A conj13_B _ _ _ _

theorem E1'_P : E1' * P 2 (0 : Fin 3) 2 = -E1 := by
  ext a x
  revert x
  refine forall3 fun i j k => ?_
  simp only [Matrix.mul_apply, Matrix.neg_apply, E1, E1', P, flipP, permP, permMat,
    Matrix.of_apply]
  rw [sum3]
  fin_cases a <;> fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [eps, Fin.sum_univ_two, Equiv.swap_apply_of_ne_of_ne, funext_iff, Fin.forall_fin_succ]

theorem P_E2' : P 2 (0 : Fin 3) 2 * E2' = -E2 := by
  ext y b
  revert y
  refine forall3 fun i j k => ?_
  simp only [Matrix.mul_apply, Matrix.neg_apply, E2, E2', P, flipP, permP, permMat,
    Matrix.of_apply]
  rw [sum3]
  fin_cases b <;> fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [eps, Fin.sum_univ_two, Equiv.swap_apply_of_ne_of_ne, funext_iff, Fin.forall_fin_succ]

/-- **The second zigzag equals the first**: `(ε ⊗ 1) Φ⁻¹ (1 ⊗ η) = (1 ⊗ ε) Φ (η ⊗ 1)`. -/
theorem zag_eq_zig (hc : ‖c‖ < 1 / 2) : zag (assocInv hc) = zig (assoc hc) := by
  rw [← conj13_assoc hc]
  show E1' * (P 2 (0 : Fin 3) 2 * assoc hc * P 2 0 2) * E2' = E1 * assoc hc * E2
  calc E1' * (P 2 (0 : Fin 3) 2 * assoc hc * P 2 0 2) * E2'
      = (E1' * P 2 (0 : Fin 3) 2) * assoc hc * (P 2 0 2 * E2') := by
        simp only [Matrix.mul_assoc]
    _ = _ := by rw [E1'_P, P_E2']; simp [Matrix.neg_mul, Matrix.mul_neg]

/-- **The corrected duality data satisfy both zigzag identities** (`|ℏ| ≤ 1/12`). With
`ν = zig(Φ)₀₀ ≠ 0` and `ε' = ν⁻¹ ε`:
`(1 ⊗ ε') Φ (η ⊗ 1) = 1_V` and `(ε' ⊗ 1) Φ⁻¹ (1 ⊗ η) = 1_V`. -/
theorem zigzag_identities (hc : ‖c‖ ≤ 1 / 12) :
    ∃ ν : ℂ, ν ≠ 0 ∧
      (ν⁻¹ • E1) * assoc (c := c) (by linarith) * E2 = 1 ∧
      (ν⁻¹ • E1') * assocInv (c := c) (by linarith) * E2' = 1 := by
  have hc' : ‖c‖ < 1 / 2 := by linarith
  obtain ⟨ν, hν⟩ : ∃ ν, ν = zig (assoc hc') 0 0 := ⟨_, rfl⟩
  have h : zig (assoc hc') = ν • 1 := hν ▸ zig_scalar hc'
  have hν0 : ν ≠ 0 := hν ▸ zig_ne_zero hc
  refine ⟨ν, hν0, ?_, ?_⟩
  · rw [Matrix.smul_mul, Matrix.smul_mul]
    show ν⁻¹ • zig (assoc hc') = 1
    rw [h, smul_smul, inv_mul_cancel₀ hν0, one_smul]
  · rw [Matrix.smul_mul, Matrix.smul_mul]
    show ν⁻¹ • zag (assocInv hc') = 1
    rw [zag_eq_zig hc', h, smul_smul, inv_mul_cancel₀ hν0, one_smul]

end Main

end QOU.KZ.ZigZag
