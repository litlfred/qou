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

end QOU.BraidsAndKnots.RationalAssociator
