import QOU.MassTheory.HeckeSectorRep

/-!
# `H₃(q)` is free of rank 6, with basis `1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀`

`HeckeSectorRep` presents the Hecke algebra `Hₙ(q)` by generators and relations
(`Hn n q qi := RingQuot (HeckeRelN n q qi)`, quadratic relation
`σᵢ² = (q − qi)σᵢ + 1`). This file proves, for `n = 3`, over **any commutative
ring** `K` and **any** `q, qi : K`:

* `Hn3.span_eq_top`: the six words `1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀` span `H₃(q)`;
* `Hn3.linearIndependent`: they are linearly independent, witnessed by the
  6 × 6 left-regular representation `Hn3.ρ` (`ρ(w) e₀ = e_w`);
* `Hn3.basis`, `Hn3.finrank_eq_six`: so they are a basis, and `dim H₃(q) = 6 = 3!`;
* `Hn3.photon_eq`: the photon `γ = 1 + aσ₀ + bσ₁ + c·σ₀σ₁⁻¹` in this basis is
  `1 + (a − c(q − qi))σ₀ + bσ₁ + cσ₀σ₁`.

The six words are exactly the irreducible words of the Gröbner–Shirshov basis
`UGB.GrobnerShirshov.Hecke.heckeTwo_irreducible_iff` (branch
`claude/hecke-gs-three-2026-11-22`); this file is the linear-independence half
that the rewriting framework there does not reach, done directly by a
representation instead.

Neither `q · qi = 1` nor any ordering is used.
-/

namespace QOU.MassTheory.HeckeThreeBasis

open QOU.MassTheory.HeckeSectorRep

variable {K : Type*} [CommRing K] (q qi : K)

/-- `σ₀` in `H₃(q)`. -/
abbrev s₀ : Hn 3 q qi := Hn.gen 3 q qi 0
/-- `σ₁` in `H₃(q)`. -/
abbrev s₁ : Hn 3 q qi := Hn.gen 3 q qi 1

theorem gen_sq (i : ℕ) (hi : i + 1 < 3) :
    Hn.gen 3 q qi i * Hn.gen 3 q qi i = (q - qi) • Hn.gen 3 q qi i + 1 := by
  simp only [Hn.gen, dif_pos hi]
  rw [← map_mul, RingQuot.mkAlgHom_rel K (HeckeRelN.quad (n := 3) (q := q) (qi := qi) ⟨i, hi⟩),
    map_add, map_smul, map_one]

theorem s₀_sq : s₀ q qi * s₀ q qi = (q - qi) • s₀ q qi + 1 := gen_sq q qi 0 (by norm_num)
theorem s₁_sq : s₁ q qi * s₁ q qi = (q - qi) • s₁ q qi + 1 := gen_sq q qi 1 (by norm_num)

theorem braid : s₀ q qi * s₁ q qi * s₀ q qi = s₁ q qi * s₀ q qi * s₁ q qi := by
  simp only [s₀, s₁, Hn.gen, dif_pos (show (0 : ℕ) + 1 < 3 by norm_num),
    dif_pos (show (1 : ℕ) + 1 < 3 by norm_num)]
  rw [← map_mul, ← map_mul, ← map_mul, ← map_mul,
    RingQuot.mkAlgHom_rel K (HeckeRelN.braid (n := 3) (q := q) (qi := qi)
      ⟨0, by norm_num⟩ ⟨1, by norm_num⟩ rfl)]

/-- The six standard words. -/
def w : Fin 6 → Hn 3 q qi :=
  ![1, s₀ q qi, s₁ q qi, s₀ q qi * s₁ q qi, s₁ q qi * s₀ q qi, s₀ q qi * s₁ q qi * s₀ q qi]

/-! ## The left-regular representation -/

/-- Left multiplication by `σ₀` on the six words (column `j` = `σ₀ · w j`). -/
def A : Matrix (Fin 6) (Fin 6) K :=
  !![0, 1, 0, 0, 0, 0;
     1, q - qi, 0, 0, 0, 0;
     0, 0, 0, 1, 0, 0;
     0, 0, 1, q - qi, 0, 0;
     0, 0, 0, 0, 0, 1;
     0, 0, 0, 0, 1, q - qi]

/-- Left multiplication by `σ₁` on the six words. -/
def B : Matrix (Fin 6) (Fin 6) K :=
  !![0, 0, 1, 0, 0, 0;
     0, 0, 0, 0, 1, 0;
     1, 0, q - qi, 0, 0, 0;
     0, 0, 0, 0, 0, 1;
     0, 1, 0, 0, q - qi, 0;
     0, 0, 0, 1, 0, q - qi]

theorem A_sq : A q qi * A q qi = (q - qi) • A q qi + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [A, Matrix.mul_apply, Fin.sum_univ_six, Matrix.one_apply] <;> ring

theorem B_sq : B q qi * B q qi = (q - qi) • B q qi + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [B, Matrix.mul_apply, Fin.sum_univ_six, Matrix.one_apply] <;> ring

/-- `A · B` written out. -/
def AB : Matrix (Fin 6) (Fin 6) K :=
  !![0, 0, 0, 0, 1, 0;
     0, 0, 1, 0, q - qi, 0;
     0, 0, 0, 0, 0, 1;
     1, 0, q - qi, 0, 0, q - qi;
     0, 0, 0, 1, 0, q - qi;
     0, 1, 0, q - qi, q - qi, (q - qi) ^ 2]

/-- `B · A` written out. -/
def BA : Matrix (Fin 6) (Fin 6) K :=
  !![0, 0, 0, 1, 0, 0;
     0, 0, 0, 0, 0, 1;
     0, 1, 0, q - qi, 0, 0;
     0, 0, 0, 0, 1, q - qi;
     1, q - qi, 0, 0, 0, q - qi;
     0, 0, 1, q - qi, q - qi, (q - qi) ^ 2]

/-- `A · B · A = B · A · B` written out. -/
def ABA : Matrix (Fin 6) (Fin 6) K :=
  !![0, 0, 0, 0, 0, 1;
     0, 0, 0, 1, 0, q - qi;
     0, 0, 0, 0, 1, q - qi;
     0, 1, 0, q - qi, q - qi, (q - qi) ^ 2;
     0, 0, 1, q - qi, q - qi, (q - qi) ^ 2;
     1, q - qi, q - qi, (q - qi) ^ 2, (q - qi) ^ 2, (q - qi) ^ 3 + (q - qi)]

theorem A_mul_B : A q qi * B q qi = AB q qi := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [A, B, AB, Matrix.mul_apply, Fin.sum_univ_six] <;> ring

theorem B_mul_A : B q qi * A q qi = BA q qi := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [A, B, BA, Matrix.mul_apply, Fin.sum_univ_six] <;> ring

theorem AB_mul_A : AB q qi * A q qi = ABA q qi := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [A, AB, ABA, Matrix.mul_apply, Fin.sum_univ_six] <;> ring

theorem BA_mul_B : BA q qi * B q qi = ABA q qi := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [B, BA, ABA, Matrix.mul_apply, Fin.sum_univ_six] <;> ring

theorem AB_braid : A q qi * B q qi * A q qi = B q qi * A q qi * B q qi := by
  rw [A_mul_B, B_mul_A, AB_mul_A, BA_mul_B]

/-- The generator images. -/
def genMat (i : {i : ℕ // i + 1 < 3}) : Matrix (Fin 6) (Fin 6) K :=
  if i.1 = 0 then A q qi else B q qi

/-- **The left-regular representation** `ρ : H₃(q) → M₆(K)`. -/
def ρ : Hn 3 q qi →ₐ[K] Matrix (Fin 6) (Fin 6) K :=
  RingQuot.liftAlgHom K ⟨FreeAlgebra.lift K (genMat q qi), by
    intro x y h
    cases h with
    | quad i =>
      simp only [map_mul, map_add, map_smul, map_one, FreeAlgebra.lift_ι_apply]
      obtain ⟨i, hi⟩ := i
      by_cases h0 : i = 0
      · simp [genMat, h0, A_sq]
      · simp [genMat, h0, B_sq]
    | braid i j hj =>
      simp only [map_mul, FreeAlgebra.lift_ι_apply]
      obtain ⟨i, hi⟩ := i
      obtain ⟨j, hj'⟩ := j
      simp only at hj
      have hi0 : i = 0 := by omega
      have hj1 : j = 1 := by omega
      subst hi0 hj1
      simp [genMat, AB_braid]
    | comm i k h =>
      exfalso
      obtain ⟨i, hi⟩ := i
      obtain ⟨k, hk⟩ := k
      simp only at h
      omega⟩

theorem ρ_s₀ : ρ q qi (s₀ q qi) = A q qi := by
  simp [ρ, s₀, Hn.gen, genMat]

theorem ρ_s₁ : ρ q qi (s₁ q qi) = B q qi := by
  simp [ρ, s₁, Hn.gen, genMat]

/-- `x ↦ ρ(x) e₀`, a `K`-linear map `H₃(q) → K⁶`. -/
def evE₀ : Hn 3 q qi →ₗ[K] (Fin 6 → K) where
  toFun x := fun j => ρ q qi x j 0
  map_add' x y := by ext j; simp
  map_smul' c x := by ext j; simp

theorem evE₀_w (k : Fin 6) : evE₀ q qi (w q qi k) = Pi.single k 1 := by
  ext j
  fin_cases k <;> fin_cases j <;>
    simp [evE₀, w, ρ_s₀, ρ_s₁, A, B, Fin.sum_univ_six, Matrix.mul_apply,
      Pi.single_apply, Matrix.one_apply]

/-- **The six words are linearly independent in `H₃(q)`.** -/
theorem linearIndependent : LinearIndependent K (w q qi) := by
  apply LinearIndependent.of_comp (evE₀ q qi)
  have : (evE₀ q qi) ∘ (w q qi) = fun k => Pi.basisFun K (Fin 6) k := by
    funext k; simp [evE₀_w]
  rw [this]
  exact (Pi.basisFun K (Fin 6)).linearIndependent

/-! ## Spanning -/

/-- The span of the six words. -/
abbrev S : Submodule K (Hn 3 q qi) := Submodule.span K (Set.range (w q qi))

theorem w_mem (k : Fin 6) : w q qi k ∈ S q qi := Submodule.subset_span ⟨k, rfl⟩

theorem lin_mem (c : K) (k l : Fin 6) : c • w q qi k + w q qi l ∈ S q qi :=
  Submodule.add_mem _ (Submodule.smul_mem _ c (w_mem q qi k)) (w_mem q qi l)

theorem s₀_mul_w (k : Fin 6) : s₀ q qi * w q qi k ∈ S q qi := by
  have h := s₀_sq q qi
  fin_cases k
  · simpa [w] using w_mem q qi 1
  · simp only [w]; simpa [h] using lin_mem q qi (q - qi) 1 0
  · simpa [w] using w_mem q qi 3
  · have e : s₀ q qi * (s₀ q qi * s₁ q qi) = (q - qi) • (s₀ q qi * s₁ q qi) + s₁ q qi := by
      rw [← mul_assoc, h, add_mul, smul_mul_assoc, one_mul]
    simp only [w]; simpa [e] using lin_mem q qi (q - qi) 3 2
  · have e : s₀ q qi * (s₁ q qi * s₀ q qi) = s₀ q qi * s₁ q qi * s₀ q qi := by
      rw [mul_assoc]
    simp only [w]; simpa [e] using w_mem q qi 5
  · have e : s₀ q qi * (s₀ q qi * s₁ q qi * s₀ q qi)
        = (q - qi) • (s₀ q qi * s₁ q qi * s₀ q qi) + s₁ q qi * s₀ q qi := by
      rw [show s₀ q qi * (s₀ q qi * s₁ q qi * s₀ q qi)
          = (s₀ q qi * s₀ q qi) * (s₁ q qi * s₀ q qi) by noncomm_ring, h, add_mul,
        smul_mul_assoc, one_mul, ← mul_assoc]
    simp only [w]; simpa [e] using lin_mem q qi (q - qi) 5 4

theorem s₁_mul_w (k : Fin 6) : s₁ q qi * w q qi k ∈ S q qi := by
  have h := s₁_sq q qi
  have hb := braid q qi
  fin_cases k
  · simpa [w] using w_mem q qi 2
  · simpa [w] using w_mem q qi 4
  · simp only [w]; simpa [h] using lin_mem q qi (q - qi) 2 0
  · have e : s₁ q qi * (s₀ q qi * s₁ q qi) = s₀ q qi * s₁ q qi * s₀ q qi := by
      rw [hb, mul_assoc]
    simp only [w]; simpa [e] using w_mem q qi 5
  · have e : s₁ q qi * (s₁ q qi * s₀ q qi) = (q - qi) • (s₁ q qi * s₀ q qi) + s₀ q qi := by
      rw [← mul_assoc, h, add_mul, smul_mul_assoc, one_mul]
    simp only [w]; simpa [e] using lin_mem q qi (q - qi) 4 1
  · have e : s₁ q qi * (s₀ q qi * s₁ q qi * s₀ q qi)
        = (q - qi) • (s₀ q qi * s₁ q qi * s₀ q qi) + s₀ q qi * s₁ q qi := by
      rw [hb, show s₁ q qi * (s₁ q qi * s₀ q qi * s₁ q qi)
          = (s₁ q qi * s₁ q qi) * (s₀ q qi * s₁ q qi) by noncomm_ring, h, add_mul,
        smul_mul_assoc, one_mul, ← mul_assoc, ← hb]
    simp only [w]; simpa [e] using lin_mem q qi (q - qi) 5 3

theorem gen_mul_mem (i : {i : ℕ // i + 1 < 3}) (y : Hn 3 q qi) (hy : y ∈ S q qi) :
    RingQuot.mkAlgHom K (HeckeRelN 3 q qi) (FreeAlgebra.ι K i) * y ∈ S q qi := by
  obtain ⟨i, hi⟩ := i
  have hgen : RingQuot.mkAlgHom K (HeckeRelN 3 q qi) (FreeAlgebra.ι K ⟨i, hi⟩)
      = Hn.gen 3 q qi i := by simp [Hn.gen, hi]
  rw [hgen]
  induction hy using Submodule.span_induction with
  | mem x hx =>
    obtain ⟨k, rfl⟩ := hx
    have : i = 0 ∨ i = 1 := by omega
    rcases this with rfl | rfl
    · exact s₀_mul_w q qi k
    · exact s₁_mul_w q qi k
  | zero => simp
  | add x y _ _ hx hy => rw [mul_add]; exact Submodule.add_mem _ hx hy
  | smul c x _ hx => rw [mul_smul_comm]; exact Submodule.smul_mem _ c hx

theorem mk_mul_mem (a : FreeAlgebra K {i : ℕ // i + 1 < 3}) :
    ∀ y ∈ S q qi, RingQuot.mkAlgHom K (HeckeRelN 3 q qi) a * y ∈ S q qi := by
  induction a using FreeAlgebra.induction with
  | grade0 r =>
    intro y hy
    rw [AlgHom.commutes, Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul]
    exact Submodule.smul_mem _ r hy
  | grade1 i => exact gen_mul_mem q qi i
  | mul a b ha hb =>
    intro y hy
    rw [map_mul, mul_assoc]
    exact ha _ (hb y hy)
  | add a b ha hb =>
    intro y hy
    rw [map_add, add_mul]
    exact Submodule.add_mem _ (ha y hy) (hb y hy)

/-- **The six words span `H₃(q)`.** -/
theorem span_eq_top : S q qi = ⊤ := by
  rw [eq_top_iff]
  intro x _
  obtain ⟨a, rfl⟩ := RingQuot.mkAlgHom_surjective K (HeckeRelN 3 q qi) x
  simpa using mk_mul_mem q qi a 1 (by simpa [w] using w_mem q qi 0)

/-- **The six words are a basis of `H₃(q)`.** -/
noncomputable def basis : Module.Basis (Fin 6) K (Hn 3 q qi) :=
  Module.Basis.mk (linearIndependent q qi) (span_eq_top q qi).ge

theorem basis_apply (k : Fin 6) : basis q qi k = w q qi k := by simp [basis]

/-- **`dim H₃(q) = 6 = 3!`**, over any nontrivial commutative ring. -/
theorem finrank_eq_six [Nontrivial K] : Module.finrank K (Hn 3 q qi) = 6 := by
  rw [Module.finrank_eq_card_basis (basis q qi), Fintype.card_fin]

/-! ## The photon in this basis -/

/-- **The photon `γ = 1 + aσ₀ + bσ₁ + c·σ₀σ₁⁻¹` in the standard basis:**
`1 + (a − c(q − qi))σ₀ + bσ₁ + cσ₀σ₁`, since `σ₁⁻¹ = σ₁ − (q − qi)`. -/
theorem photon_eq (a b c : K) :
    Hn.photon 3 q qi a b c 0
      = w q qi 0 + (a - c * (q - qi)) • w q qi 1 + b • w q qi 2 + c • w q qi 3 := by
  simp only [Hn.photon, Hn.genInv, w, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.head_cons, Matrix.cons_val_two, Matrix.tail_cons, Matrix.cons_val_three]
  rw [mul_sub, Algebra.algebraMap_eq_smul_one, mul_smul_comm, mul_one, smul_sub]
  simp only [s₀, s₁, zero_add]
  module

end QOU.MassTheory.HeckeThreeBasis
