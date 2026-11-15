/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.QuantumGLDominance

/-!
# Branching bound for highest-weight spaces

G3.4c (bean `qou-gl343`), part 1.

Split a vector on `n + 1` sites by its last letter: `v_x(a) = v(a x)`.  The coproduct
`Δ(E) = E ⊗ κ + 1 ⊗ E` gives

`(E v)(a x) = κ(x) (E v_x)(a) + [x = i+1] v_i(a)`  (`raiseOp_mulVec_snoc`).

So if `v` is a highest-weight vector of weight `λ` and `v_y = 0` for every `y < x`, then `v_x` is
a highest-weight vector of weight `λ − e_x`.  Filtering by the first nonzero slice gives

`dim HW_λ(n+1) ≤ Σ_x dim HW_{λ − e_x}(n)`  (`finrank_hwSpace_succ_le`),

the representation-side half of the branching recursion `f^λ = Σ_{corners} f^{λ − □}`.

## Base ring (§7c)

Any field; `q ≠ 0` (no genericity needed for this part).

-- Ref: [kassel1995] C. Kassel, *Quantum Groups*, GTM 155, Ch. VI–VII.
-/

namespace QOU.SchurWeyl.QuantumGL

open QOU.IwahoriHecke.TensorEmbedGL Matrix

section Slice

variable {R : Type*} [CommRing R] {d n : ℕ}

/-- The slice of `v` at last letter `y`. -/
def slice (v : (Fin (n + 1) → Fin d) → R) (y : Fin d) : (Fin n → Fin d) → R :=
  fun a => v (Fin.snoc a y)

theorem sum_snoc {M : Type*} [AddCommMonoid M] (f : (Fin (n + 1) → Fin d) → M) :
    ∑ b, f b = ∑ b : Fin n → Fin d, ∑ y : Fin d, f (Fin.snoc b y) := by
  rw [← Fintype.sum_prod_type', ← Fintype.sum_equiv (snocW n).symm]
  intro b
  show f b = f (Fin.snoc (Fin.init b) (b (Fin.last n)))
  rw [Fin.snoc_init_self]

/-- **`Δ(E) = E ⊗ κ + 1 ⊗ E` on vectors.** -/
theorem raiseOp_mulVec_snoc (q qi : R) (i j : Fin d) (v : (Fin (n + 1) → Fin d) → R)
    (a : Fin n → Fin d) (x : Fin d) :
    (raiseOp q qi i j *ᵥ v) (Fin.snoc a x)
      = kap q qi i j x * (raiseOp q qi i j *ᵥ slice v x) a
        + (if x = j then slice v i a else 0) := by
  classical
  simp only [mulVec, dotProduct]
  rw [sum_snoc]
  simp only [raiseOp, siteOp_succ_apply, Fin.init_snoc, Fin.snoc_last, add_mul,
    Finset.sum_add_distrib]
  congr 1
  · rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun b _ => ?_
    rw [Finset.sum_eq_single x]
    · simp [slice]; ring
    · intro y _ hy; simp [Ne.symm hy]
    · simp
  · rw [Finset.sum_eq_single a]
    · by_cases hx : x = j
      · subst hx
        rw [Finset.sum_eq_single i]
        · simp [slice, single_apply']
        · intro y _ hy; simp [single_apply', Ne.symm hy]
        · simp
      · simp [single_apply', hx]
    · intro b _ hb; simp [Ne.symm hb]
    · simp

theorem content_snoc (a : Fin n → Fin d) (x : Fin d) :
    content (Fin.snoc a x : Fin (n + 1) → Fin d) = content a + Pi.single x 1 := by
  funext y
  rw [Pi.add_apply, content_eq_sum, content_eq_sum, Fin.sum_univ_castSucc]
  simp only [Fin.snoc_castSucc, Fin.snoc_last, Pi.add_apply, Pi.single_apply]
  rcases eq_or_ne x y with rfl | h
  · simp
  · simp [h, Ne.symm h]

end Slice

section Peel

variable {K : Type*} [Field K] {d : ℕ}

/-- The slice at `y`, as a linear map. -/
def sliceMap (n : ℕ) (y : Fin d) :
    ((Fin (n + 1) → Fin d) → K) →ₗ[K] ((Fin n → Fin d) → K) where
  toFun v := slice v y
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

theorem kap_ne_zero {q : K} (hq : q ≠ 0) (i j x : Fin d) : kap q q⁻¹ i j x ≠ 0 := by
  unfold kap; split_ifs <;> simp [hq]

/-- Highest-weight vectors whose slices below `x` vanish. -/
def peelSpace (q : K) (m : ℕ) (μ : Fin d → ℕ) (x : ℕ) :
    Submodule K ((Fin (m + 2) → Fin d) → K) where
  carrier := {v | v ∈ hwSpace q (m + 1) μ ∧ ∀ y : Fin d, (y : ℕ) < x → slice v y = 0}
  add_mem' {v w} hv hw := ⟨add_mem hv.1 hw.1, fun y hy => by
    funext a
    have h1 := congrFun (hv.2 y hy) a
    have h2 := congrFun (hw.2 y hy) a
    simp only [slice, Pi.zero_apply] at h1 h2 ⊢
    simp [h1, h2]⟩
  zero_mem' := ⟨zero_mem _, fun _ _ => rfl⟩
  smul_mem' c v hv := ⟨Submodule.smul_mem _ c hv.1, fun y hy => by
    funext a
    have h1 := congrFun (hv.2 y hy) a
    simp only [slice, Pi.zero_apply] at h1 ⊢
    simp [h1]⟩

theorem peelSpace_zero (q : K) (m : ℕ) (μ : Fin d → ℕ) : peelSpace q m μ 0 = hwSpace q (m + 1) μ := by
  ext v; simp [peelSpace]

theorem peelSpace_d (q : K) (m : ℕ) (μ : Fin d → ℕ) : peelSpace q m μ d = ⊥ := by
  rw [Submodule.eq_bot_iff]
  rintro v ⟨-, hv⟩
  funext b
  rw [← Fin.snoc_init_self b]
  exact congrFun (hv (b (Fin.last _)) (b (Fin.last _)).isLt) (Fin.init b)

theorem weightProj_mulVec_apply (μ : Fin d → ℕ) {n : ℕ} (v : (Fin n → Fin d) → K) (a : Fin n → Fin d) :
    (weightProj μ *ᵥ v) a = if content a = μ then v a else 0 := by
  rw [weightProj, mulVec_diagonal]; split_ifs <;> simp

/-- **The first nonzero slice of a highest-weight vector is a highest-weight vector** of weight
`λ − e_x`. -/
theorem slice_mem_hwSpace (q : K) (hq : q ≠ 0) (m : ℕ) (μ : Fin d → ℕ) {x : Fin d}
    {v : (Fin (m + 2) → Fin d) → K} (hv : v ∈ peelSpace q m μ x) :
    slice v x ∈ hwSpace q m (μ - Pi.single x 1) := by
  obtain ⟨⟨hw, hE⟩, hlow⟩ := hv
  refine ⟨?_, fun i j hij => ?_⟩
  · funext a
    rw [weightProj_mulVec_apply]
    split_ifs with h
    · rfl
    · have := congrFun hw (Fin.snoc a x)
      rw [weightProj_mulVec_apply, if_neg] at this
      · exact this.symm.symm ▸ rfl
      · intro hc
        apply h
        rw [← hc, content_snoc]
        funext y; simp
  · funext a
    have h := congrFun (hE i j hij) (Fin.snoc a x)
    rw [raiseOp_mulVec_snoc] at h
    have h2 : (if x = j then slice v i a else 0) = 0 := by
      split_ifs with hx
      · rw [hlow i (by rw [hx]; omega)]; rfl
      · rfl
    rw [h2, add_zero] at h
    exact (mul_eq_zero.mp h).resolve_left (kap_ne_zero hq i j x)

theorem finrank_peelSpace_le (q : K) (hq : q ≠ 0) (m : ℕ) (μ : Fin d → ℕ) (x : Fin d) :
    Module.finrank K (peelSpace q m μ x)
      ≤ Module.finrank K (peelSpace q m μ (x + 1))
        + Module.finrank K (hwSpace q m (μ - Pi.single x 1)) := by
  set f : peelSpace q m μ x →ₗ[K] hwSpace q m (μ - Pi.single x 1) :=
    { toFun := fun v => ⟨slice v.1 x, slice_mem_hwSpace q hq m μ v.2⟩
      map_add' := fun _ _ => rfl
      map_smul' := fun _ _ => rfl }
  have hker : Module.finrank K (LinearMap.ker f) ≤ Module.finrank K (peelSpace q m μ (x + 1)) := by
    let g : LinearMap.ker f →ₗ[K] peelSpace q m μ (x + 1) :=
      { toFun := fun v => ⟨v.1.1, v.1.2.1, fun y hy => by
          rcases Nat.lt_succ_iff_lt_or_eq.mp hy with hy | hy
          · exact v.1.2.2 y hy
          · have := v.2
            rw [LinearMap.mem_ker] at this
            have hyx : y = x := Fin.ext hy
            subst hyx
            exact congrArg Subtype.val this⟩
        map_add' := fun _ _ => rfl
        map_smul' := fun _ _ => rfl }
    exact LinearMap.finrank_le_finrank_of_injective (f := g) fun a b h => by
      have h' : a.1.1 = b.1.1 :=
        congrArg (fun z : peelSpace q m μ (x + 1) => (z : (Fin (m + 2) → Fin d) → K)) h
      exact Subtype.ext (Subtype.ext h')
  have hr := LinearMap.finrank_range_add_finrank_ker f
  have hrange := Submodule.finrank_le (LinearMap.range f)
  omega

/-- **Branching bound**: `dim HW_λ(n+1) ≤ Σ_x dim HW_{λ − e_x}(n)`. -/
theorem finrank_hwSpace_succ_le (q : K) (hq : q ≠ 0) (m : ℕ) (μ : Fin d → ℕ) :
    Module.finrank K (hwSpace q (m + 1) μ)
      ≤ ∑ x : Fin d, Module.finrank K (hwSpace q m (μ - Pi.single x 1)) := by
  have key : ∀ k, k ≤ d → Module.finrank K (peelSpace q m μ (d - k))
      ≤ ∑ x ∈ Finset.univ.filter (fun y : Fin d => d - k ≤ (y : ℕ)),
          Module.finrank K (hwSpace q m (μ - Pi.single x 1)) := by
    intro k
    induction k with
    | zero =>
        intro _
        rw [Nat.sub_zero, peelSpace_d, finrank_bot]
        exact Nat.zero_le _
    | succ k ih =>
        intro hk
        set x : Fin d := ⟨d - (k + 1), by omega⟩
        have hx1 : (x : ℕ) + 1 = d - k := by simp [x]; omega
        have h1 := finrank_peelSpace_le q hq m μ x
        rw [hx1] at h1
        have h2 := ih (by omega)
        have hsplit : (Finset.univ.filter fun y : Fin d => d - (k + 1) ≤ (y : ℕ))
            = insert x (Finset.univ.filter fun y : Fin d => d - k ≤ (y : ℕ)) := by
          ext y
          simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_insert, x]
          constructor
          · intro h
            rcases Nat.eq_or_lt_of_le h with h | h
            · exact Or.inl (Fin.ext h.symm)
            · exact Or.inr (by omega)
          · rintro (h | h)
            · rw [h]
            · omega
        rw [hsplit, Finset.sum_insert (by simp [x]; omega)]
        exact h1.trans (by omega)
  have := key d le_rfl
  rw [Nat.sub_self, peelSpace_zero] at this
  refine this.trans (Finset.sum_le_sum_of_subset (by intro y _; simp))

end Peel

end QOU.SchurWeyl.QuantumGL
