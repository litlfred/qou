import QOU.BraidsAndKnots.RationalAssociator.BaseChangeAction
import QOU.BraidsAndKnots.RationalAssociator.Homogeneity
import QOU.BraidsAndKnots.RationalAssociator.Prop57Link

/-!
# Steps (2)–(4) of gap B1: shifts with coefficients in `K` and the induction step

Bean `qou-3fdg` (epic `qou-dk7p`), plan `docs/audits/2026-11-27-grt-action-pentagon-derivation.md`
§16b, write-up §17b.
-/

namespace QOU.BraidsAndKnots.RationalAssociator
open TensorProduct Polynomial

/-! ### Step (2), the tool: a polynomial over `S` that is right at every rational point -/

section PolyTrick

set_option linter.unusedSectionVars false

variable {K : Type*} [Field K] [Algebra ℚ K]
variable {S : Type*} [Ring S] [Algebra K S] [Algebra ℚ S] [IsScalarTower ℚ K S]

/-- Evaluation of a polynomial over `S` at the central element `c ∈ K`. -/
noncomputable def evT (c : K) : S[X] →ₐ[K] S :=
  Polynomial.eval₂AlgHom' (AlgHom.id K S) (algebraMap K S c)
    (fun a => (Algebra.commutes c a).symm)

@[simp] theorem evT_C (c : K) (a : S) : evT c (C a) = a := by simp [evT]

@[simp] theorem evT_X (c : K) : evT (S := S) c X = algebraMap K S c := by simp [evT]

theorem evT_eq_sum (c : K) (p : S[X]) :
    evT c p = ∑ i ∈ Finset.range (p.natDegree + 1), algebraMap K S c ^ i * p.coeff i := by
  change eval₂ (RingHom.id S) (algebraMap K S c) p = _
  rw [eval₂_eq_sum_range]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [← map_pow]; exact (Algebra.commutes _ _).symm

/-- **A polynomial right at every rational point is right at every point of `K`.** For a
`ℚ`-submodule `F` closed under multiplication by `K`: if `p(c) ∈ F` for every `c ∈ ℚ`, then
`p(c) ∈ F` for every `c ∈ K`. -/
theorem mem_of_forall_rat (F : Submodule ℚ S)
    (hF : ∀ (k : K) {s : S}, s ∈ F → algebraMap K S k * s ∈ F) (p : S[X])
    (h : ∀ x : ℚ, evT (algebraMap ℚ K x) p ∈ F) (c : K) : evT c p ∈ F := by
  have hc : ∀ j, j < p.natDegree + 1 → p.coeff j ∈ F := fun j hj => by
    refine coeff_mem_of_forall F (fun j => p.coeff j) _ (fun x => ?_) hj
    have := h x
    rw [evT_eq_sum] at this
    convert this using 2 with i
    rw [← IsScalarTower.algebraMap_apply, ← map_pow, ← Algebra.smul_def]
  rw [evT_eq_sum]
  refine Submodule.sum_mem _ fun j hj => ?_
  rw [← map_pow]
  exact hF _ (hc j (Finset.mem_range.1 hj))

/-- Equality version of `mem_of_forall_rat`. -/
theorem eq_of_forall_rat {p q : S[X]}
    (h : ∀ x : ℚ, evT (algebraMap ℚ K x) p = evT (algebraMap ℚ K x) q) (c : K) :
    evT c p = evT c q := by
  have := mem_of_forall_rat (⊥ : Submodule ℚ S) (fun k s hs => by
    rw [Submodule.mem_bot] at hs ⊢; rw [hs, mul_zero]) (p - q)
    (fun x => by rw [Submodule.mem_bot, map_sub, h x, sub_self]) c
  rwa [Submodule.mem_bot, map_sub, sub_eq_zero] at this

theorem evT_eval_C (c : K) (a b : S) (p : FreeAlgebra ℚ (Fin 2)) :
    evT c (eval (C a) (C b) p) = eval a b p := by
  rw [map_eval_K, evT_C, evT_C]

end PolyTrick

/-! ### The shift `Φ ↦ Φ ∘ exp(c h)` with `c ∈ K` -/

section ShiftK

variable {K : Type*} [Field K] [Algebra ℚ K]
variable {S : Type*} [Ring S] [Algebra K S] [Algebra ℚ S] [IsScalarTower ℚ K S]

variable (K) in
/-- `X` with coefficient `1` in `K ⊗ ℚ⟨X, Y⟩`. -/
noncomputable abbrev X1 : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2) := (1 : K) ⊗ₜ FreeAlgebra.ι ℚ 0

variable (K) in
/-- `Y` with coefficient `1` in `K ⊗ ℚ⟨X, Y⟩`. -/
noncomputable abbrev Y1 : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2) := (1 : K) ⊗ₜ FreeAlgebra.ι ℚ 1

@[simp] theorem evK_X1 (a b : S) : evK a b (X1 K) = a := by simp

@[simp] theorem evK_Y1 (a b : S) : evK a b (Y1 K) = b := by simp

/-- **The right action of `G ∈ K ⊗ ℚ⟨X, Y⟩` on `Φ`**: `Φ(G · A · G(B, A), B) · G`, Drinfeld's
(5.16) with the inverse written through (5.12), now with both arguments over `K`. -/
noncomputable def compKK (Φ G : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)) : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2) :=
  evK (G * X1 K * evK (Y1 K) (X1 K) G) (Y1 K) Φ * G

theorem evK_compKK (a b : S) (Φ G : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)) :
    evK a b (compKK Φ G) = evK (evK a b G * a * evK b a G) b Φ * evK a b G := by
  simp only [compKK, map_mul, map_evK, evK_X1, evK_Y1]

/-- `exp(c h) = Σ_{k<n} c^k ⊗ e_k`, the truncated (5.16)-exponential of `c h`, `c ∈ K`. -/
noncomputable def GK (h : FreeAlgebra ℚ (Fin 2)) (n : ℕ) (c : K) : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2) :=
  ∑ k ∈ Finset.range n, (c ^ k) ⊗ₜ expTerm h k

theorem evK_GK (a b : S) (h : FreeAlgebra ℚ (Fin 2)) (n : ℕ) (c : K) :
    evK a b (GK h n c) = ∑ k ∈ Finset.range n, algebraMap K S c ^ k * eval a b (expTerm h k) := by
  simp [GK, map_sum, map_pow]

theorem evK_GK_rat (a b : S) (h : FreeAlgebra ℚ (Fin 2)) (n : ℕ) (x : ℚ) :
    evK a b (GK h n (algebraMap ℚ K x)) = eval a b (expPoly (x • h) n) := by
  rw [evK_GK, expPoly_smul, map_sum]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [map_smul, ← IsScalarTower.algebraMap_apply, ← map_pow, ← Algebra.smul_def]

/-- At rational `c`, the `K`-shift is the rational action of `GRT₁`. -/
theorem evK_compKK_rat (a b : S) (Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)) (h : FreeAlgebra ℚ (Fin 2))
    (n : ℕ) (x : ℚ) :
    evK a b (compKK Φ (GK h n (algebraMap ℚ K x))) = evK a b (compK Φ (expPoly (x • h) n)) := by
  rw [evK_compKK, evK_compK, evK_GK_rat, evK_GK_rat]

/-- `exp(T h)` evaluated at `(a, b)`, as a polynomial in `T` over `S`. -/
noncomputable def ΓT (h : FreeAlgebra ℚ (Fin 2)) (n : ℕ) (a b : S) : S[X] :=
  ∑ k ∈ Finset.range n, X ^ k * C (eval a b (expTerm h k))

/-- `Φ ∘ exp(T h)` evaluated at `(a, b)`, as a polynomial in `T` over `S`. -/
noncomputable def fT (Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)) (h : FreeAlgebra ℚ (Fin 2)) (n : ℕ)
    (a b : S) : S[X] :=
  evK (ΓT h n a b * C a * ΓT h n b a) (C b) Φ * ΓT h n a b

theorem evT_ΓT (c : K) (h : FreeAlgebra ℚ (Fin 2)) (n : ℕ) (a b : S) :
    evT c (ΓT h n a b) = evK a b (GK h n c) := by
  simp only [ΓT, evK_GK, map_sum, map_mul, map_pow, evT_X, evT_C]

theorem evT_fT (c : K) (Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)) (h : FreeAlgebra ℚ (Fin 2)) (n : ℕ)
    (a b : S) : evT c (fT Φ h n a b) = evK a b (compKK Φ (GK h n c)) := by
  rw [fT, map_mul, map_evK, map_mul, map_mul, evT_ΓT, evT_ΓT, evT_C, evT_C, evK_compKK]

end ShiftK

/-! ### Step (2): `AssocK` is closed under `exp(c h)` for `c ∈ K` -/

section Step2

variable {K : Type*} [Field K] [Algebra ℚ K] {N : ℕ}

theorem evK_compKK_eq_evT (c : K) {S : Type*} [Ring S] [Algebra K S] [Algebra ℚ S]
    [IsScalarTower ℚ K S] (Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)) (h : FreeAlgebra ℚ (Fin 2))
    (n : ℕ) (a b : S) : evK a b (compKK Φ (GK h n c)) = evT c (fT Φ h n a b) :=
  (evT_fT c Φ h n a b).symm

/-- **Step (2) of gap B1.** If `exp(x h)` (truncated at `n`) satisfies the `GRT₁` conditions in
`U4 N` for every rational `x`, then the `K`-associators in `K ⊗ U4 N` are closed under the shift
by `exp(c h)` for every `c ∈ K`. -/
theorem assocK_shiftK {E : FreeAlgebra ℚ (Fin 2)} {Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)}
    (hΦ : AssocK K N E Φ) {h : FreeAlgebra ℚ (Fin 2)} {n : ℕ}
    (hg : ∀ x : ℚ, GRT1U4 N (expPoly (x • h) n)) (c : K) :
    AssocK K N E (compKK Φ (GK h n c)) := by
  have hr := fun x => assocK_compK hΦ (hg x)
  refine ⟨?_, ?_, ?_, ?_⟩
  · rw [evK_compKK_eq_evT]
    rw [show (1 : K) = evT c (C (1 : K)) by simp]
    refine eq_of_forall_rat (fun x => ?_) c
    rw [← evK_compKK_eq_evT, evK_compKK_rat, evT_C]
    exact (hr x).const
  · intro a b ha hb
    simp only [evK_compKK_eq_evT, ← map_mul]
    rw [show (1 : K ⊗[ℚ] U4 N) = evT c 1 by simp]
    refine eq_of_forall_rat (fun x => ?_) c
    rw [map_mul, ← evK_compKK_eq_evT, ← evK_compKK_eq_evT, evK_compKK_rat, evK_compKK_rat,
      map_one]
    exact (hr x).inv a b ha hb
  · have key := eq_of_forall_rat (K := K)
      (p := eval (C (ιK K N (t N 1) + ιK K N (t N 3))) (C 0) E)
      (q := fT Φ h n (ιK K N (t N 1)) (ιK K N (t N 0)) * eval (C (ιK K N (t N 1))) (C 0) E *
        fT Φ h n (ιK K N (t N 3)) (ιK K N (t N 1)) * eval (C (ιK K N (t N 3))) (C 0) E *
        fT Φ h n (ιK K N (t N 0)) (ιK K N (t N 3))) (fun x => by
        simp only [map_mul, evT_eval_C, evT_fT, evK_compKK_rat]
        exact (hr x).hex) c
    simp only [map_mul, evT_eval_C, evT_fT] at key
    exact key
  · have key := eq_of_forall_rat (K := K)
      (p := fT Φ h n (ιK K N (t N 0)) (ιK K N (t N 3) + ιK K N (t N 4)) *
        fT Φ h n (ιK K N (t N 1) + ιK K N (t N 3)) (ιK K N (t N 5)))
      (q := fT Φ h n (ιK K N (t N 3)) (ιK K N (t N 5)) *
        fT Φ h n (ιK K N (t N 0) + ιK K N (t N 1)) (ιK K N (t N 4) + ιK K N (t N 5)) *
        fT Φ h n (ιK K N (t N 0)) (ιK K N (t N 3))) (fun x => by
        simp only [map_mul, evT_fT, evK_compKK_rat]
        exact (hr x).pent) c
    simp only [map_mul, evT_fT] at key
    exact key

end Step2

end QOU.BraidsAndKnots.RationalAssociator
