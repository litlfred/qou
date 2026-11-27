import QOU.BraidsAndKnots.RationalAssociator.AssociatorInduction

/-!
# Homogeneous parts and the transfer of the linearised conditions between truncations

Gap (B3) of audit §13 (bean `qou-3fdg`).
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open Polynomial

/-! ### Decomposition of a span of scaled generators -/

section Decomp

variable {V : Type*} [AddCommGroup V] [Module ℚ V]

/-- A decomposition of `Z` into eigencomponents of a family of scalings `σ λ`, with components
of degree below `k` zero and the component of degree `j` in `P j`. -/
def Decomp (σ : ℚ → V →ₗ[ℚ] V) (P : ℕ → Submodule ℚ V) (k : ℕ) (Z : V) : Prop :=
  ∃ (n : ℕ) (c : ℕ → V), (∀ j, n ≤ j → c j = 0) ∧ (∀ j, j < k → c j = 0) ∧ (∀ j, c j ∈ P j) ∧
    (∀ j (r : ℚ), σ r (c j) = r ^ j • c j) ∧ Z = ∑ j ∈ Finset.range n, c j

omit [Module ℚ V] in
theorem sum_range_of_zero {c : ℕ → V} {n m : ℕ} (hn : ∀ j, n ≤ j → c j = 0) (hm : n ≤ m) :
    ∑ j ∈ Finset.range m, c j = ∑ j ∈ Finset.range n, c j := by
  refine (Finset.sum_subset (Finset.range_mono hm) fun j _ hj => ?_).symm
  exact hn j (by simpa using hj)

theorem decomp_span (σ : ℚ → V →ₗ[ℚ] V) (P : ℕ → Submodule ℚ V) (k : ℕ) (G : Set V)
    (hG : ∀ g ∈ G, ∃ l, k ≤ l ∧ g ∈ P l ∧ ∀ r : ℚ, σ r g = r ^ l • g) {Z : V}
    (hZ : Z ∈ Submodule.span ℚ G) : Decomp σ P k Z := by
  induction hZ using Submodule.span_induction with
  | mem g hg =>
    obtain ⟨l, hl, hP, hs⟩ := hG g hg
    refine ⟨l + 1, fun j => if j = l then g else 0, ?_, ?_, ?_, ?_, ?_⟩
    · intro j hj; simp only; rw [if_neg (by omega)]
    · intro j hj; simp only; rw [if_neg (by omega)]
    · intro j; simp only; split_ifs with h
      · exact h ▸ hP
      · exact zero_mem _
    · intro j r; simp only; split_ifs with h
      · subst h; exact hs r
      · simp
    · rw [Finset.sum_ite_eq']; simp
  | zero => exact ⟨0, fun _ => 0, by simp, by simp, by simp, by simp, by simp⟩
  | add x y _ _ hx hy =>
    obtain ⟨n1, c1, a1, b1, p1, s1, e1⟩ := hx
    obtain ⟨n2, c2, a2, b2, p2, s2, e2⟩ := hy
    refine ⟨n1 + n2, c1 + c2, fun j hj => ?_, fun j hj => ?_, fun j => add_mem (p1 j) (p2 j),
      fun j r => ?_, ?_⟩
    · simp [a1 j (by omega), a2 j (by omega)]
    · simp [b1 j hj, b2 j hj]
    · simp [s1 j r, s2 j r, smul_add]
    · simp only [Pi.add_apply, Finset.sum_add_distrib]
      rw [sum_range_of_zero a1 (by omega), sum_range_of_zero a2 (by omega), e1, e2]
  | smul r x _ hx =>
    obtain ⟨n, c, a, b, p, s, e⟩ := hx
    refine ⟨n, r • c, fun j hj => by simp [a j hj], fun j hj => by simp [b j hj],
      fun j => Submodule.smul_mem _ r (p j), fun j r' => ?_, ?_⟩
    · simp [s j r', smul_comm r]
    · simp [e, Finset.smul_sum]

/-- **A homogeneous element of degree `d` all of whose components have degree `> d` is zero.** -/
theorem eq_zero_of_decomp (σ : ℚ → V →ₗ[ℚ] V) (P : ℕ → Submodule ℚ V) {d : ℕ} {Z : V}
    (hZ : Decomp σ P (d + 1) Z) (hh : ∀ r : ℚ, σ r Z = r ^ d • Z) : Z = 0 := by
  obtain ⟨n, c, a, b, -, s, e⟩ := hZ
  set m := n + d + 1
  have em : Z = ∑ j ∈ Finset.range m, c j := by rw [sum_range_of_zero a (by omega), e]
  set c' : ℕ → V := fun j => c j - if j = d then Z else 0
  have key : ∀ r : ℚ, ∑ j ∈ Finset.range m, r ^ j • c' j ∈ (⊥ : Submodule ℚ V) := by
    intro r
    rw [Submodule.mem_bot]
    simp only [c', smul_sub, Finset.sum_sub_distrib, smul_ite, smul_zero]
    rw [Finset.sum_ite_eq', if_pos (Finset.mem_range.2 (by omega)), ← hh r, em, map_sum]
    simp [s]
  have := coeff_mem_of_forall ⊥ c' m key (j := d) (by omega)
  simpa [c', b d (by omega)] using this

end Decomp


/-! ### Left multiplication on a quotient by a left ideal -/

section LmQ

variable {A : Type*} [Ring A] [Algebra ℚ A] (Q : Submodule ℚ A)

/-- Left multiplication of `A` on `A ⧸ Q`, for `Q` closed under left multiplication. -/
noncomputable def lmQ (hQ : ∀ (a : A) {q : A}, q ∈ Q → a * q ∈ Q) :
    A →ₐ[ℚ] Module.End ℚ (A ⧸ Q) where
  toFun a := Q.mapQ Q (LinearMap.mulLeft ℚ a) (fun q hq => hQ a hq)
  map_one' := by ext x; simp
  map_mul' a b := by ext x; simp
  map_zero' := by ext x; simp
  map_add' a b := by ext x; simp [add_mul]
  commutes' r := by
    ext x
    simp [Algebra.algebraMap_eq_smul_one]

variable {Q}

theorem lmQ_mk (hQ : ∀ (a : A) {q : A}, q ∈ Q → a * q ∈ Q) (a b : A) :
    lmQ Q hQ a (Submodule.Quotient.mk b) = Submodule.Quotient.mk (a * b) := rfl

/-- `lmQ` kills `Q` when `Q` is also closed under right multiplication. -/
theorem lmQ_eq_zero (hQ : ∀ (a : A) {q : A}, q ∈ Q → a * q ∈ Q)
    (hQ' : ∀ {q : A} (a : A), q ∈ Q → q * a ∈ Q) {q : A} (hq : q ∈ Q) : lmQ Q hQ q = 0 := by
  ext x
  simp only [LinearMap.coe_comp, Function.comp_apply, Submodule.mkQ_apply, lmQ_mk,
    LinearMap.zero_comp, LinearMap.zero_apply]
  exact (Submodule.Quotient.mk_eq_zero Q).2 (hQ' x hq)

/-- `lmQ a = 0` gives `a ∈ Q`. -/
theorem mem_of_lmQ_eq_zero (hQ : ∀ (a : A) {q : A}, q ∈ Q → a * q ∈ Q) {a : A}
    (h : lmQ Q hQ a = 0) : a ∈ Q := by
  have := congrArg (fun f : Module.End ℚ (A ⧸ Q) => f (Submodule.Quotient.mk 1)) h
  simp only [lmQ_mk, mul_one, LinearMap.zero_apply] at this
  exact (Submodule.Quotient.mk_eq_zero Q).1 this

end LmQ

/-! ### Scaling and homogeneity in `ℚ⟨X, Y⟩` -/

section ScaleF

/-- The scaling `X ↦ r X`, `Y ↦ r Y`. -/
noncomputable def scF (r : ℚ) : FreeAlgebra ℚ (Fin 2) →ₐ[ℚ] FreeAlgebra ℚ (Fin 2) :=
  FreeAlgebra.lift ℚ fun i => r • FreeAlgebra.ι ℚ i

/-- `p` is homogeneous of degree `d`. -/
def Homog (d : ℕ) (p : FreeAlgebra ℚ (Fin 2)) : Prop := ∀ r : ℚ, scF r p = r ^ d • p

theorem scF_word (r : ℚ) (w : List (Fin 2)) :
    scF r (w.map (FreeAlgebra.ι ℚ)).prod = r ^ w.length • (w.map (FreeAlgebra.ι ℚ)).prod := by
  induction w with
  | nil => simp
  | cons i w ih =>
    rw [List.map_cons, List.prod_cons, map_mul, ih]
    simp only [scF, FreeAlgebra.lift_ι_apply] at *
    rw [smul_mul_smul_comm, List.length_cons, pow_succ, mul_comm]

theorem eval_smul_smul {R : Type*} [Ring R] [Algebra ℚ R] (r : ℚ) (a b : R)
    (p : FreeAlgebra ℚ (Fin 2)) : eval (r • a) (r • b) p = eval a b (scF r p) := by
  have : eval (r • a) (r • b) = (eval a b).comp (scF r) := by
    apply FreeAlgebra.hom_ext; funext i; fin_cases i <;> simp [scF, eval]
  rw [this]; rfl

theorem eval_smul_of_homog {R : Type*} [Ring R] [Algebra ℚ R] {d : ℕ} {p : FreeAlgebra ℚ (Fin 2)}
    (hp : Homog d p) (r : ℚ) (a b : R) : eval (r • a) (r • b) p = r ^ d • eval a b p := by
  rw [eval_smul_smul, hp, map_smul]

theorem scF_swapPoly (r : ℚ) (p : FreeAlgebra ℚ (Fin 2)) :
    scF r (swapPoly p) = swapPoly (scF r p) := by
  have : (scF r).comp (FreeAlgebra.lift ℚ ![FreeAlgebra.ι ℚ 1, FreeAlgebra.ι ℚ 0]) =
      (FreeAlgebra.lift ℚ ![FreeAlgebra.ι ℚ 1, FreeAlgebra.ι ℚ 0]).comp (scF r) := by
    apply FreeAlgebra.hom_ext; funext i; fin_cases i <;> simp [scF]
  exact congrArg (fun f : FreeAlgebra ℚ (Fin 2) →ₐ[ℚ] FreeAlgebra ℚ (Fin 2) => f p) this

theorem Homog.swap {d : ℕ} {p : FreeAlgebra ℚ (Fin 2)} (hp : Homog d p) : Homog d (swapPoly p) :=
  fun r => by
    rw [scF_swapPoly, hp]
    exact map_smul (FreeAlgebra.lift ℚ ![FreeAlgebra.ι ℚ 1, FreeAlgebra.ι ℚ 0]) _ p

theorem Homog.add {d : ℕ} {p q : FreeAlgebra ℚ (Fin 2)} (hp : Homog d p) (hq : Homog d q) :
    Homog d (p + q) := fun r => by rw [map_add, hp, hq, smul_add]

theorem decomp_FF (k : ℕ) {y : FreeAlgebra ℚ (Fin 2)} (hy : y ∈ FF k) :
    Decomp (fun r => (scF r).toLinearMap) FF k y := by
  refine decomp_span _ FF k _ ?_ hy
  rintro _ ⟨w, hw, rfl⟩
  exact ⟨w.length, hw, word_mem_FF w le_rfl, fun r => scF_word r w⟩

/-- **The degree-`d` part.** Every `y ∈ FF d` is a homogeneous `h` of degree `d` plus an
element of `FF (d + 1)`. -/
theorem exists_homog_part {d : ℕ} {y : FreeAlgebra ℚ (Fin 2)} (hy : y ∈ FF d) :
    ∃ h, h ∈ FF d ∧ Homog d h ∧ y - h ∈ FF (d + 1) := by
  obtain ⟨n, c, a, b, p, s, e⟩ := decomp_FF d hy
  refine ⟨c d, p d, fun r => s d r, ?_⟩
  have hm : d ∈ Finset.range (n + d + 1) := Finset.mem_range.2 (by omega)
  rw [e, ← sum_range_of_zero a (show n ≤ n + d + 1 by omega), ← Finset.add_sum_erase _ _ hm,
    add_sub_cancel_left]
  refine Submodule.sum_mem _ fun j hj => ?_
  rcases lt_or_gt_of_ne (Finset.ne_of_mem_erase hj) with h | h
  · rw [b j h]; exact zero_mem _
  · exact FF_anti h (p j)

/-- A homogeneous polynomial of degree `d` in `FF (d + 1)` is zero. -/
theorem eq_zero_of_homog_mem_FF {d : ℕ} {w : FreeAlgebra ℚ (Fin 2)} (hw : Homog d w)
    (hmem : w ∈ FF (d + 1)) : w = 0 :=
  eq_zero_of_decomp _ FF (decomp_FF (d + 1) hmem) hw

end ScaleF

/-! ### Scaling in `U4 M` -/

section ScaleU

variable {M : ℕ}

theorem dk4_smul (r : ℚ) : DK4 (r • t M 0) (r • t M 1) (r • t M 2) (r • t M 3) (r • t M 4)
    (r • t M 5) := by
  have h := dk4 M
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    (try simp only [← smul_add]) <;> apply Commute.smul_left <;> apply Commute.smul_right
  exacts [h.f12_34, h.f13_24, h.f14_23, h.n12_3, h.n13_2, h.n23_1, h.n12_4, h.n14_2, h.n24_1,
    h.n13_4, h.n14_3, h.n34_1, h.n23_4, h.n24_3, h.n34_2]

theorem prod_map_smul (r : ℚ) (w : List (Fin 6)) :
    (w.map fun i => r • t M i).prod = r ^ w.length • (w.map (t M)).prod := by
  induction w with
  | nil => simp
  | cons i w ih =>
    rw [List.map_cons, List.prod_cons, ih, List.map_cons, List.prod_cons, smul_mul_smul_comm,
      List.length_cons, pow_succ, mul_comm]

/-- The scaling `tᵢⱼ ↦ r tᵢⱼ` of `U4 M`. -/
noncomputable def scU (M : ℕ) (r : ℚ) : U4 M →ₐ[ℚ] U4 M :=
  lift M (fun i => r • t M i) (dk4_smul r) fun w hw => by
    rw [prod_map_smul, word_eq_zero M w hw, smul_zero]

@[simp] theorem scU_t (r : ℚ) (i : Fin 6) : scU M r (t M i) = r • t M i := by
  simp [scU]

theorem scU_word (r : ℚ) (w : List (Fin 6)) :
    scU M r (w.map (t M)).prod = r ^ w.length • (w.map (t M)).prod := by
  rw [map_list_prod, List.map_map]
  simp only [Function.comp_def, scU_t]
  exact prod_map_smul r w

theorem decomp_Fil (k : ℕ) {X : U4 M} (hX : X ∈ Fil M k) :
    Decomp (fun r => (scU M r).toLinearMap) (Fil M) k X := by
  refine decomp_span _ (Fil M) k _ ?_ hX
  rintro _ ⟨w, hw, rfl⟩
  exact ⟨w.length, hw, word_mem_Fil w le_rfl, fun r => scU_word r w⟩

/-- A degree-`d` element of `Fil M (d + 1)` is zero. -/
theorem eq_zero_of_scU {d : ℕ} {X : U4 M} (hX : X ∈ Fil M (d + 1))
    (hs : ∀ r : ℚ, scU M r X = r ^ d • X) : X = 0 :=
  eq_zero_of_decomp _ (Fil M) (decomp_Fil (d + 1) hX) hs

theorem scU_eval_of_homog {d : ℕ} {h : FreeAlgebra ℚ (Fin 2)} (hh : Homog d h) (r : ℚ)
    (a b : U4 M) {a' b' : U4 M} (ha : scU M r a = r • a') (hb : scU M r b = r • b')
    (ea : a = a') (eb : b = b') : scU M r (eval a b h) = r ^ d • eval a b h := by
  rw [map_eval, ha, hb, eval_smul_of_homog hh, ea, eb]

end ScaleU

/-! ### Transfer from `U4 (d + 1)` to every `U4 M` -/

section Transfer

variable {M : ℕ}

theorem fil_mul_left (d : ℕ) (a : U4 M) {q : U4 M} (hq : q ∈ Fil M (d + 1)) :
    a * q ∈ Fil M (d + 1) := by
  simpa using mul_mem_Fil (mem_Fil_zero a) hq

theorem fil_mul_right (d : ℕ) {q : U4 M} (a : U4 M) (hq : q ∈ Fil M (d + 1)) :
    q * a ∈ Fil M (d + 1) := by
  simpa using mul_mem_Fil hq (mem_Fil_zero a)

/-- `U4 (d + 1)` acts on `U4 M ⧸ Fil M (d + 1)` through left multiplication by the generators. -/
noncomputable def toQuot (M d : ℕ) : U4 (d + 1) →ₐ[ℚ] Module.End ℚ (U4 M ⧸ Fil M (d + 1)) :=
  lift (d + 1) (fun i => lmQ (Fil M (d + 1)) (fil_mul_left d) (t M i))
    (DK4.map' (lmQ (Fil M (d + 1)) (fil_mul_left d)).toRingHom (dk4 M)) fun w hw => by
      have : (w.map fun i => lmQ (Fil M (d + 1)) (fil_mul_left d) (t M i)).prod =
          lmQ (Fil M (d + 1)) (fil_mul_left d) (w.map (t M)).prod := by
        rw [map_list_prod, List.map_map]; rfl
      rw [this]
      exact lmQ_eq_zero _ (fil_mul_right d) (word_mem_Fil w hw.ge)

@[simp] theorem toQuot_t (d : ℕ) (i : Fin 6) :
    toQuot M d (t (d + 1) i) = lmQ (Fil M (d + 1)) (fil_mul_left d) (t M i) := by
  simp [toQuot]

/-- The map `U4 M → U4 (d + 1)`-images: an identity among generator evaluations in
`U4 (d + 1)` holds in `U4 M` modulo `Fil M (d + 1)`. -/
theorem mem_Fil_of_toQuot {d : ℕ} {X : U4 M} {Y : U4 (d + 1)} (hY : Y = 0)
    (hXY : toQuot M d Y = lmQ (Fil M (d + 1)) (fil_mul_left d) X) : X ∈ Fil M (d + 1) := by
  rw [hY, map_zero] at hXY
  exact mem_of_lmQ_eq_zero _ hXY.symm

theorem ff_mul_left (d : ℕ) (a : FreeAlgebra ℚ (Fin 2)) {q : FreeAlgebra ℚ (Fin 2)}
    (hq : q ∈ FF (d + 1)) : a * q ∈ FF (d + 1) := by
  simpa using mul_mem_FF (mem_FF_zero a) hq

theorem ff_mul_right (d : ℕ) {q : FreeAlgebra ℚ (Fin 2)} (a : FreeAlgebra ℚ (Fin 2))
    (hq : q ∈ FF (d + 1)) : q * a ∈ FF (d + 1) := by
  simpa using mul_mem_FF hq (mem_FF_zero a)

/-- The free pair: `t₁₂ ↦ X`, `t₁₃ ↦ −X − Y`, `t₂₃ ↦ Y`, the others `↦ 0`. -/
noncomputable def pairVals : Fin 6 → FreeAlgebra ℚ (Fin 2) :=
  ![FreeAlgebra.ι ℚ 0, -FreeAlgebra.ι ℚ 0 - FreeAlgebra.ι ℚ 1, 0, FreeAlgebra.ι ℚ 1, 0, 0]

theorem pairVals_mem (i : Fin 6) : pairVals i ∈ FF 1 := by
  fin_cases i <;> simp [pairVals, ι_mem_FF_one, zero_mem, sub_mem]

theorem prod_pairVals_mem (w : List (Fin 6)) : (w.map pairVals).prod ∈ FF w.length := by
  induction w with
  | nil => simpa using mem_FF_zero (1 : FreeAlgebra ℚ (Fin 2))
  | cons i w ih => simpa [Nat.add_comm] using mul_mem_FF (pairVals_mem i) ih

theorem dk4_pairVals {S : Type*} [Ring S] [Algebra ℚ S] (f : FreeAlgebra ℚ (Fin 2) →ₐ[ℚ] S) :
    DK4 (f (pairVals 0)) (f (pairVals 1)) (f (pairVals 2)) (f (pairVals 3)) (f (pairVals 4))
      (f (pairVals 5)) := by
  have h : DK3 (f (pairVals 0)) (f (pairVals 1)) (f (pairVals 3)) :=
    dk3_of_sum_zero (by simp [pairVals, map_sub, map_neg]; abel)
  have h4 := h.toDK4
  simpa [pairVals] using h4

/-- `U4 (d + 1)` maps the pair `(t₁₂, t₂₃)` onto `(X, Y)` acting on `ℚ⟨X, Y⟩ ⧸ FF (d + 1)`. -/
noncomputable def toFree (d : ℕ) :
    U4 (d + 1) →ₐ[ℚ] Module.End ℚ (FreeAlgebra ℚ (Fin 2) ⧸ FF (d + 1)) :=
  lift (d + 1) (fun i => lmQ (FF (d + 1)) (ff_mul_left d) (pairVals i))
    (dk4_pairVals (lmQ (FF (d + 1)) (ff_mul_left d))) fun w hw => by
      have : (w.map fun i => lmQ (FF (d + 1)) (ff_mul_left d) (pairVals i)).prod =
          lmQ (FF (d + 1)) (ff_mul_left d) (w.map pairVals).prod := by
        rw [map_list_prod, List.map_map]; rfl
      rw [this]
      exact lmQ_eq_zero _ (ff_mul_right d) (hw ▸ prod_pairVals_mem w)

theorem eval_ι_ι (p : FreeAlgebra ℚ (Fin 2)) :
    eval (FreeAlgebra.ι ℚ 0) (FreeAlgebra.ι ℚ 1) p = p := by
  have : eval (FreeAlgebra.ι ℚ 0) (FreeAlgebra.ι ℚ 1) = AlgHom.id ℚ (FreeAlgebra ℚ (Fin 2)) := by
    apply FreeAlgebra.hom_ext; funext i; fin_cases i <;> simp [eval]
  rw [this]; rfl

/-- **The linearised (5.12) for a homogeneous element holds in `ℚ⟨X, Y⟩`** as soon as it holds
at `(t₁₂, t₂₃)` in `U4 (d + 1)`. -/
theorem add_swap_eq_zero {d : ℕ} {h : FreeAlgebra ℚ (Fin 2)} (hh : Homog d h)
    (h512 : eval (t (d + 1) 0) (t (d + 1) 3) h + eval (t (d + 1) 3) (t (d + 1) 0) h = 0) :
    h + swapPoly h = 0 := by
  have e := congrArg (toFree d) h512
  rw [map_zero, map_add, map_eval, map_eval] at e
  simp only [toFree, lift_t, pairVals, Matrix.cons_val_zero, Matrix.cons_val] at e
  rw [← map_eval, ← map_eval, ← map_add, eval_ι_ι, ← eval_swapPoly, eval_ι_ι] at e
  exact eq_zero_of_homog_mem_FF (hh.add hh.swap) (mem_of_lmQ_eq_zero _ e)

end Transfer

/-! ### The kernel of the degree-`d` system is `grt`, given (B2) -/

section Grt

/-- The linearised (5.14), as it appears in `GrtU4`: the content of gap (B2). -/
def Lin514 (M : ℕ) (y : FreeAlgebra ℚ (Fin 2)) : Prop :=
  ∀ u v w : U4 M, u ∈ Fil M 1 → v ∈ Fil M 1 → w ∈ Fil M 1 → DK3 u v w →
    eval v w y * v + v * eval w v y = eval u w y * (v + w) + (v + w) * eval w u y

variable {M d : ℕ}

theorem toQuot_eval {h : FreeAlgebra ℚ (Fin 2)} {a b : U4 (d + 1)} {a' b' : U4 M}
    (ha : toQuot M d a = lmQ (Fil M (d + 1)) (fil_mul_left d) a')
    (hb : toQuot M d b = lmQ (Fil M (d + 1)) (fil_mul_left d) b') :
    toQuot M d (eval a b h) = lmQ (Fil M (d + 1)) (fil_mul_left d) (eval a' b' h) := by
  rw [map_eval, ha, hb, ← map_eval]

theorem toQuot_t_add (i j : Fin 6) :
    toQuot M d (t (d + 1) i + t (d + 1) j) =
      lmQ (Fil M (d + 1)) (fil_mul_left d) (t M i + t M j) := by
  rw [map_add, toQuot_t, toQuot_t, map_add]

theorem scU_t_add (r : ℚ) (i j : Fin 6) : scU M r (t M i + t M j) = r • (t M i + t M j) := by
  rw [map_add, scU_t, scU_t, smul_add]

/-- The three-term (5.18) expression. -/
noncomputable def lin513Expr (M : ℕ) (y : FreeAlgebra ℚ (Fin 2)) : U4 M :=
  eval (t M 1) (t M 0) y + eval (t M 3) (t M 1) y + eval (t M 0) (t M 3) y

/-- The five-term (5.20) expression, in the form of `assocLin`. -/
noncomputable def lin515Expr (M : ℕ) (y : FreeAlgebra ℚ (Fin 2)) : U4 M :=
  eval (t M 3) (t M 5) y + eval (t M 0 + t M 1) (t M 4 + t M 5) y + eval (t M 0) (t M 3) y -
    eval (t M 0) (t M 3 + t M 4) y - eval (t M 1 + t M 3) (t M 5) y

theorem toQuot_lin513 (y : FreeAlgebra ℚ (Fin 2)) :
    toQuot M d (lin513Expr (d + 1) y) =
      lmQ (Fil M (d + 1)) (fil_mul_left d) (lin513Expr M y) := by
  simp only [lin513Expr, map_add]
  rw [toQuot_eval (toQuot_t d 1) (toQuot_t d 0), toQuot_eval (toQuot_t d 3) (toQuot_t d 1),
    toQuot_eval (toQuot_t d 0) (toQuot_t d 3)]

theorem toQuot_lin515 (y : FreeAlgebra ℚ (Fin 2)) :
    toQuot M d (lin515Expr (d + 1) y) =
      lmQ (Fil M (d + 1)) (fil_mul_left d) (lin515Expr M y) := by
  simp only [lin515Expr, map_add, map_sub]
  rw [toQuot_eval (toQuot_t d 3) (toQuot_t d 5),
    toQuot_eval (toQuot_t_add 0 1) (toQuot_t_add 4 5),
    toQuot_eval (toQuot_t d 0) (toQuot_t d 3),
    toQuot_eval (toQuot_t d 0) (toQuot_t_add 3 4),
    toQuot_eval (toQuot_t_add 1 3) (toQuot_t d 5)]

theorem scU_lin513 {y : FreeAlgebra ℚ (Fin 2)} (hy : Homog d y) (r : ℚ) :
    scU M r (lin513Expr M y) = r ^ d • lin513Expr M y := by
  simp only [lin513Expr, map_add, map_eval, scU_t, eval_smul_of_homog hy, smul_add]

theorem scU_lin515 {y : FreeAlgebra ℚ (Fin 2)} (hy : Homog d y) (r : ℚ) :
    scU M r (lin515Expr M y) = r ^ d • lin515Expr M y := by
  have e : ∀ a b : U4 M, scU M r a = r • a → scU M r b = r • b →
      scU M r (eval a b y) = r ^ d • eval a b y := fun a b ha hb => by
    rw [map_eval, ha, hb, eval_smul_of_homog hy]
  rw [lin515Expr, map_sub, map_sub, map_add, map_add, e _ _ (scU_t r 3) (scU_t r 5),
    e _ _ (scU_t_add r 0 1) (scU_t_add r 4 5), e _ _ (scU_t r 0) (scU_t r 3),
    e _ _ (scU_t r 0) (scU_t_add r 3 4), e _ _ (scU_t_add r 1 3) (scU_t r 5)]
  simp only [smul_add, smul_sub]

/-- **Gap (B3), modulo (B2).** A homogeneous `y ∈ FF d` of degree `d ≥ 1` in the kernel of the
degree-`d` system (`assocLin (d + 1) y = 0`: the linearised (5.12), (5.13), (5.15) in
`U4 (d + 1)`) satisfies the linearised (5.12), (5.13), (5.15) in every `U4 M`; together with
the linearised (5.14) in `U4 M` (the (B2) hypothesis `Lin514 M y`), `y ∈ grt` in `U4 M`. -/
theorem grtU4_of_lin (hd : 1 ≤ d) {y : FreeAlgebra ℚ (Fin 2)} (hF : y ∈ FF d)
    (hy : Homog d y) (hlin : assocLin (d + 1) y = 0) (h514 : Lin514 M y) : GrtU4 M y := by
  have h1 := congrArg Prod.fst hlin
  have h2 := congrArg (fun z => z.2.1) hlin
  have h3 := congrArg (fun z => z.2.2) hlin
  simp only [assocLin, LinearMap.coe_mk, AddHom.coe_mk, Prod.fst_zero, Prod.snd_zero] at h1 h2 h3
  have hsw : y + swapPoly y = 0 :=
    add_swap_eq_zero hy (congrFun h1 ⟨(t (d + 1) 0, t (d + 1) 3), t_mem_Fil_one 0,
      t_mem_Fil_one 3⟩)
  have h513 : lin513Expr (d + 1) y = 0 := neg_eq_zero.1 h2
  have h515 : lin515Expr (d + 1) y = 0 := h3
  have z513 : lin513Expr M y = 0 :=
    eq_zero_of_scU (mem_Fil_of_toQuot h513 (toQuot_lin513 y)) (scU_lin513 hy)
  have z515 : lin515Expr M y = 0 :=
    eq_zero_of_scU (mem_Fil_of_toQuot h515 (toQuot_lin515 y)) (scU_lin515 hy)
  refine ⟨algebraMapInv_eq_zero_of_mem_FF hd hF, fun a b _ _ => ?_, z513, h514, ?_⟩
  · rw [← eval_swapPoly a b y, ← map_add, hsw, map_zero]
  · rw [← sub_eq_zero]
    rw [lin515Expr] at z515
    rw [← neg_eq_zero, ← z515]
    abel

end Grt

end QOU.BraidsAndKnots.RationalAssociator
