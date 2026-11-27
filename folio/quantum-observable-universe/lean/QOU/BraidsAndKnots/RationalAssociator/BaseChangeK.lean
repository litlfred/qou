import QOU.BraidsAndKnots.RationalAssociator.BaseChangeAction
import QOU.BraidsAndKnots.RationalAssociator.Homogeneity
import QOU.BraidsAndKnots.RationalAssociator.Prop57Link
import QOU.BraidsAndKnots.RationalAssociator.Friedrichs

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

/-! ### Restriction `U4 N → U4 M` and `AssocK` at lower order -/

section Proj

variable {K : Type*} [Field K] [Algebra ℚ K] {M N : ℕ}

theorem word_eq_zero_of_le (w : List (Fin 6)) (hw : M ≤ w.length) :
    (w.map (t M)).prod = 0 := by
  rw [← List.take_append_drop M w, List.map_append, List.prod_append,
    word_eq_zero M (w.take M) (by simp [hw]), zero_mul]

/-- The quotient map `U4 N → U4 M`, `t_i ↦ t_i`, for `M ≤ N`. -/
noncomputable def projU (h : M ≤ N) : U4 N →ₐ[ℚ] U4 M :=
  lift N (t M) (dk4 M) fun w hw => word_eq_zero_of_le w (by omega)

@[simp] theorem projU_t (h : M ≤ N) (i : Fin 6) : projU h (t N i) = t M i := by
  simp [projU]

theorem projU_word (h : M ≤ N) (w : List (Fin 6)) :
    projU h (w.map (t N)).prod = (w.map (t M)).prod := by
  simp [map_list_prod, List.map_map, Function.comp_def]

theorem exists_projU_Fil (h : M ≤ N) {k : ℕ} {u : U4 M} (hu : u ∈ Fil M k) :
    ∃ v ∈ Fil N k, projU h v = u := by
  unfold Fil at hu
  induction hu using Submodule.span_induction with
  | mem x hx =>
    obtain ⟨w, hw, rfl⟩ := hx
    exact ⟨_, word_mem_Fil w hw, projU_word h w⟩
  | zero => exact ⟨0, zero_mem _, map_zero _⟩
  | add x y _ _ hx hy =>
    obtain ⟨a, ha, rfl⟩ := hx
    obtain ⟨b, hb, rfl⟩ := hy
    exact ⟨a + b, add_mem ha hb, map_add _ _ _⟩
  | smul c x _ hx =>
    obtain ⟨a, ha, rfl⟩ := hx
    exact ⟨c • a, Submodule.smul_mem _ c ha, map_smul _ _ _⟩

variable (K) in
/-- `K ⊗ U4 N → K ⊗ U4 M`. -/
noncomputable def projK (h : M ≤ N) : K ⊗[ℚ] U4 N →ₐ[K] K ⊗[ℚ] U4 M :=
  Algebra.TensorProduct.map (AlgHom.id K K) (projU h)

theorem projK_ιK (h : M ≤ N) (u : U4 N) : projK K h (ιK K N u) = ιK K M (projU h u) := by
  simp [projK, ιK_apply]

/-- A `K`-associator in `K ⊗ U4 N` is one in `K ⊗ U4 M` for `M ≤ N`. -/
theorem AssocK.proj {E : FreeAlgebra ℚ (Fin 2)} {Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)}
    (hΦ : AssocK K N E Φ) (h : M ≤ N) : AssocK K M E Φ := by
  refine ⟨hΦ.const, fun a b ha hb => ?_, ?_, ?_⟩
  · obtain ⟨a', ha', rfl⟩ := exists_projU_Fil h ha
    obtain ⟨b', hb', rfl⟩ := exists_projU_Fil h hb
    have := congrArg (projK K h) (hΦ.inv a' b' ha' hb')
    rwa [map_mul, map_one, map_evK, map_evK, projK_ιK, projK_ιK] at this
  · have e := hΦ.hex
    unfold HexagonF at e ⊢
    have := congrArg (projK K h) e
    simpa only [map_mul, map_add, map_zero, map_evK, map_eval_K, projK_ιK, projU_t] using this
  · have e := hΦ.pent
    unfold PentagonF at e ⊢
    have := congrArg (projK K h) e
    simpa only [map_mul, map_add, map_evK, projK_ιK, projU_t] using this

end Proj

/-! ### Step (3): the `K`-shift is `Φ + c ⊗ h` modulo the next filtration level -/

section Step3

variable {K : Type*} [Field K] [Algebra ℚ K]

theorem FFK_anti {m n : ℕ} (h : m ≤ n) : FFK K n ≤ FFK K m := by
  rintro _ ⟨z, rfl⟩
  refine ⟨LinearMap.lTensor K (Submodule.inclusion (FF_anti h)) z, ?_⟩
  rw [← LinearMap.comp_apply, ← LinearMap.lTensor_comp, Submodule.subtype_comp_inclusion]

theorem mul_mem_FFK {m n : ℕ} {x y : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)} (hx : x ∈ FFK K m)
    (hy : y ∈ FFK K n) : x * y ∈ FFK K (m + n) := by
  obtain ⟨z, rfl⟩ := hx
  obtain ⟨z', rfl⟩ := hy
  induction z using TensorProduct.induction_on with
  | zero => simp
  | add a b ha hb => rw [map_add, add_mul]; exact add_mem ha hb
  | tmul k u =>
    induction z' using TensorProduct.induction_on with
    | zero => simp
    | add a b ha hb => rw [map_add, mul_add]; exact add_mem ha hb
    | tmul k' u' =>
      simp only [LinearMap.lTensor_tmul, Submodule.subtype_apply,
        Algebra.TensorProduct.tmul_mul_tmul]
      exact tmul_mem_FFK _ (mul_mem_FF u.2 u'.2)

theorem mul_mem_FFK' {m n c : ℕ} (h : m + n = c) {x y : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)}
    (hx : x ∈ FFK K m) (hy : y ∈ FFK K n) : x * y ∈ FFK K c := h ▸ mul_mem_FFK hx hy

theorem mem_FFK_zero (x : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)) : x ∈ FFK K 0 := by
  induction x using TensorProduct.induction_on with
  | zero => exact zero_mem _
  | tmul k p => exact tmul_mem_FFK k (mem_FF_zero p)
  | add x y hx hy => exact add_mem hx hy

theorem FFK_mul_left {m : ℕ} (a : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2))
    {x : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)} (hx : x ∈ FFK K m) : a * x ∈ FFK K m :=
  mul_mem_FFK' (zero_add m) (mem_FFK_zero a) hx

theorem FFK_mul_right {m : ℕ} (a : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2))
    {x : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)} (hx : x ∈ FFK K m) : x * a ∈ FFK K m :=
  mul_mem_FFK' (add_zero m) hx (mem_FFK_zero a)

/-- Changing the first argument by an element of `FFK m` changes any value by `FFK m`. -/
theorem eval_sub_mem_FFK {m : ℕ} (a a' b : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2))
    (h : a - a' ∈ FFK K m) (p : FreeAlgebra ℚ (Fin 2)) :
    eval a b p - eval a' b p ∈ FFK K m := by
  induction p using FreeAlgebra.induction with
  | grade0 r => simp
  | grade1 i => fin_cases i <;> simp [eval, h]
  | mul p q hp hq =>
    have e : eval a b (p * q) - eval a' b (p * q) =
        (eval a b p - eval a' b p) * eval a b q + eval a' b p * (eval a b q - eval a' b q) := by
      rw [map_mul, map_mul, sub_mul, mul_sub]; abel
    rw [e]
    exact add_mem (FFK_mul_right _ hp) (FFK_mul_left _ hq)
  | add p q hp hq => rw [map_add, map_add, add_sub_add_comm]; exact add_mem hp hq

theorem evK_sub_mem_FFK {m : ℕ} (a a' b : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2))
    (h : a - a' ∈ FFK K m) (x : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)) :
    evK a b x - evK a' b x ∈ FFK K m := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul k p =>
    rw [evK_tmul, evK_tmul, ← mul_sub]
    exact FFK_mul_left _ (eval_sub_mem_FFK a a' b h p)
  | add x y hx hy => rw [map_add, map_add, add_sub_add_comm]; exact add_mem hx hy

theorem eval_mem_FFK {a b : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)} (ha : a ∈ FFK K 1) (hb : b ∈ FFK K 1)
    {m : ℕ} {p : FreeAlgebra ℚ (Fin 2)} (hp : p ∈ FF m) : eval a b p ∈ FFK K m := by
  have hw : ∀ w : List (Fin 2), eval a b (w.map (FreeAlgebra.ι ℚ)).prod ∈ FFK K w.length := by
    intro w
    induction w with
    | nil => exact mem_FFK_zero _
    | cons i w ih =>
      rw [List.map_cons, List.prod_cons, map_mul]
      have hi : eval a b (FreeAlgebra.ι ℚ i) ∈ FFK K 1 := by
        fin_cases i
        · simpa [eval] using ha
        · simpa [eval] using hb
      exact mul_mem_FFK' (by simp [Nat.add_comm]) hi ih
  unfold FF at hp
  induction hp using Submodule.span_induction with
  | mem p h =>
    obtain ⟨w, hw', rfl⟩ := h
    exact FFK_anti hw' (hw w)
  | zero => simp
  | add p q _ _ hp hq => rw [map_add]; exact add_mem hp hq
  | smul r p _ hp => rw [map_smul]; exact Submodule.smul_mem _ r hp

theorem evK_mem_FFK {a b : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)} (ha : a ∈ FFK K 1) (hb : b ∈ FFK K 1)
    {m : ℕ} {x : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)} (hx : x ∈ FFK K m) : evK a b x ∈ FFK K m := by
  obtain ⟨z, rfl⟩ := hx
  induction z using TensorProduct.induction_on with
  | zero => simp
  | tmul k p =>
    simp only [LinearMap.lTensor_tmul, Submodule.subtype_apply, evK_tmul]
    exact FFK_mul_left _ (eval_mem_FFK ha hb p.2)
  | add x y hx hy => rw [map_add, map_add]; exact add_mem hx hy

theorem X1_mem_FFK : X1 K ∈ FFK K 1 := tmul_mem_FFK _ (ι_mem_FF_one 0)

theorem Y1_mem_FFK : Y1 K ∈ FFK K 1 := tmul_mem_FFK _ (ι_mem_FF_one 1)

theorem evK_X1_Y1 (Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)) : evK (X1 K) (Y1 K) Φ = Φ := by
  induction Φ using TensorProduct.induction_on with
  | zero => simp
  | tmul k p =>
    have e : eval (X1 K) (Y1 K) p = (1 : K) ⊗ₜ p := by
      rw [show X1 K = Algebra.TensorProduct.includeRight (FreeAlgebra.ι ℚ 0) from rfl,
        show Y1 K = Algebra.TensorProduct.includeRight (FreeAlgebra.ι ℚ 1) from rfl,
        ← map_eval, eval_ι_ι]
      rfl
    rw [evK_tmul, e, Algebra.TensorProduct.algebraMap_apply, Algebra.TensorProduct.tmul_mul_tmul]
    simp
  | add x y hx hy => rw [map_add, hx, hy]

theorem GK_sub_mem {d n : ℕ} {h : FreeAlgebra ℚ (Fin 2)} (hh : h ∈ FF d) (hn : 2 ≤ n) (c : K) :
    GK h n c - 1 - c ⊗ₜ h ∈ FFK K (2 * d) := by
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 2 := ⟨n - 2, by omega⟩
  have e : GK h (m + 2) c - 1 - c ⊗ₜ h =
      ∑ k ∈ Finset.range m, (c ^ (k + 1 + 1)) ⊗ₜ expTerm h (k + 1 + 1) := by
    rw [GK, Finset.sum_range_succ', Finset.sum_range_succ']
    simp only [expTerm_zero, expTerm_one, pow_zero, pow_one, zero_add,
      ← Algebra.TensorProduct.one_def]
    abel
  rw [e]
  exact Submodule.sum_mem _ fun k _ => tmul_mem_FFK _
    (FF_anti (Nat.mul_le_mul_right d (show 2 ≤ k + 1 + 1 by omega)) (expTerm_mem_FF_mul hh (k + 1 + 1)))

/-- **Step (3) of gap B1, the `K`-congruence.** For `h ∈ FF d`, `d ≥ 1`, and `Φ ≡ 1` modulo
`FFK 1`, the shift of `Φ` by `exp(c h)` is `Φ + c ⊗ h` modulo `FFK (d + 1)`. -/
theorem compKK_congr {d : ℕ} (hd : 1 ≤ d) {n : ℕ} (hn : 2 ≤ n) {h : FreeAlgebra ℚ (Fin 2)}
    (hh : h ∈ FF d) {Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)} (hΦ : Φ - 1 ∈ FFK K 1) (c : K) :
    compKK Φ (GK h n c) - Φ - c ⊗ₜ h ∈ FFK K (d + 1) := by
  have hG2 := GK_sub_mem hh hn c
  have hch : c ⊗ₜ h ∈ FFK K d := tmul_mem_FFK c hh
  have hG : GK h n c - 1 ∈ FFK K d := by
    have e : GK h n c - 1 = (GK h n c - 1 - c ⊗ₜ h) + c ⊗ₜ h := by abel
    rw [e]; exact add_mem (FFK_anti (by omega) hG2) hch
  have hG' : evK (Y1 K) (X1 K) (GK h n c) - 1 ∈ FFK K d := by
    have := evK_mem_FFK Y1_mem_FFK X1_mem_FFK hG
    rwa [map_sub, map_one] at this
  have hconj : GK h n c * X1 K * evK (Y1 K) (X1 K) (GK h n c) - X1 K ∈ FFK K (d + 1) := by
    have e : GK h n c * X1 K * evK (Y1 K) (X1 K) (GK h n c) - X1 K =
        (GK h n c - 1) * X1 K * evK (Y1 K) (X1 K) (GK h n c) +
          X1 K * (evK (Y1 K) (X1 K) (GK h n c) - 1) := by
      simp only [sub_mul, mul_sub, one_mul, mul_one]; abel
    rw [e]
    exact add_mem (FFK_mul_right _ (mul_mem_FFK hG X1_mem_FFK))
      (mul_mem_FFK' (by omega) X1_mem_FFK hG')
  have hσ := evK_sub_mem_FFK _ (X1 K) (Y1 K) hconj Φ
  rw [evK_X1_Y1] at hσ
  have e : compKK Φ (GK h n c) - Φ - c ⊗ₜ h =
      (evK (GK h n c * X1 K * evK (Y1 K) (X1 K) (GK h n c)) (Y1 K) Φ - Φ) * GK h n c +
        Φ * (GK h n c - 1 - c ⊗ₜ h) + (Φ - 1) * (c ⊗ₜ h) := by
    rw [compKK]; simp only [sub_mul, mul_sub, one_mul, mul_one]; abel
  rw [e]
  exact add_mem (add_mem (FFK_mul_right _ hσ) (FFK_mul_left _ (FFK_anti (by omega) hG2)))
    (mul_mem_FFK' (by omega) hΦ hch)

end Step3

/-! ### Step (4): shifting along finitely many directions -/

section Step4

variable {K : Type*} [Field K] [Algebra ℚ K] {N d : ℕ}

/-- **Step (4) of gap B1.** Shifting a `K`-associator `Ψ₀ ≡ 1 (FFK 1)` successively by
`exp(c_i h_i)`, `i ∈ s`, with `h_i ∈ FF d` whose rational exponentials are in `GRT₁(U4 N)`,
gives a `K`-associator `Ψ ≡ Ψ₀ + Σ c_i ⊗ h_i` modulo `FFK (d + 1)`. -/
theorem assocK_shift_finset (hd : 1 ≤ d) {n : ℕ} (hn : 2 ≤ n) {ι : Type*} (s : Finset ι)
    (c : ι → K) (h : ι → FreeAlgebra ℚ (Fin 2)) (hh : ∀ i, h i ∈ FF d)
    (hg : ∀ i (x : ℚ), GRT1U4 N (expPoly (x • h i) n)) {E : FreeAlgebra ℚ (Fin 2)}
    {Ψ₀ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)} (hΨ₀ : AssocK K N E Ψ₀) (h1 : Ψ₀ - 1 ∈ FFK K 1) :
    ∃ Ψ, AssocK K N E Ψ ∧ Ψ - Ψ₀ - ∑ i ∈ s, c i ⊗ₜ h i ∈ FFK K (d + 1) := by
  classical
  induction s using Finset.induction_on with
  | empty => exact ⟨Ψ₀, hΨ₀, by simp⟩
  | @insert a s ha ih =>
    obtain ⟨Ψ, hΨ, hmem⟩ := ih
    have hsum : ∑ i ∈ s, c i ⊗ₜ h i ∈ FFK K 1 :=
      Submodule.sum_mem _ fun i _ => tmul_mem_FFK _ (FF_anti hd (hh i))
    have hΨ1 : Ψ - 1 ∈ FFK K 1 := by
      have e : Ψ - 1 = (Ψ - Ψ₀ - ∑ i ∈ s, c i ⊗ₜ h i) + ∑ i ∈ s, c i ⊗ₜ h i + (Ψ₀ - 1) := by
        abel
      rw [e]; exact add_mem (add_mem (FFK_anti (by omega) hmem) hsum) h1
    refine ⟨compKK Ψ (GK (h a) n (c a)), assocK_shiftK hΨ (hg a) (c a), ?_⟩
    have hc := compKK_congr hd hn (hh a) hΨ1 (c a)
    rw [Finset.sum_insert ha]
    have e : compKK Ψ (GK (h a) n (c a)) - Ψ₀ - (c a ⊗ₜ h a + ∑ i ∈ s, c i ⊗ₜ h i) =
        (compKK Ψ (GK (h a) n (c a)) - Ψ - c a ⊗ₜ h a) + (Ψ - Ψ₀ - ∑ i ∈ s, c i ⊗ₜ h i) := by
      abel
    rw [e]; exact add_mem hc hmem

end Step4

end QOU.BraidsAndKnots.RationalAssociator
