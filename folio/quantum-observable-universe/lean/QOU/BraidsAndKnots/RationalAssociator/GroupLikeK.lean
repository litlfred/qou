import QOU.BraidsAndKnots.RationalAssociator.BaseChangeK

/-!
# Group-likeness over `K` and the primitive top layer

Bean `qou-3fdg` (epic `qou-dk7p`), audit §17c.

`inductionStep_of_primitiveLayer` (`BaseChangeK`) assumes `hprim`: the rational contractions of
the top layer `z` of a `K`-associator `1 ⊗ Φ + z` are primitive modulo the next filtration level.
This file derives that hypothesis from group-likeness of the `K`-associator, and shows that the
induction step returns a `K`-associator that is again group-like, so the hypothesis is
re-established one degree up.

* `FF2 m`: the span of `u ⊗ v` with `u, v` words of total length `≥ m`, in `ℚ⟨X, Y⟩ ⊗ ℚ⟨X, Y⟩`.
* `exists_primitive_layer`: if `p ∈ FF d` and `Δ p − p ⊗ 1 − 1 ⊗ p ∈ FF2 (d + 1)`, the degree-`d`
  part of `p` is primitive. This uses `Δ ∘ scF r = (scF r ⊗ scF r) ∘ Δ`.
-/

namespace QOU.BraidsAndKnots.RationalAssociator
open TensorProduct Friedrichs

local notation "F2" => FreeAlgebra ℚ (Fin 2)

/-! ### The word filtration of `ℚ⟨X, Y⟩ ⊗ ℚ⟨X, Y⟩` -/

section FF2

/-- The span of `u ⊗ v`, `u, v` words with `|u| + |v| ≥ m`. -/
def FF2 (m : ℕ) : Submodule ℚ (F2 ⊗[ℚ] F2) :=
  Submodule.span ℚ {p | ∃ u v : List (Fin 2), m ≤ u.length + v.length ∧
    p = (u.map (FreeAlgebra.ι ℚ)).prod ⊗ₜ[ℚ] (v.map (FreeAlgebra.ι ℚ)).prod}

theorem FF2_anti {m n : ℕ} (h : m ≤ n) : FF2 n ≤ FF2 m :=
  Submodule.span_mono fun _ ⟨u, v, hw, e⟩ => ⟨u, v, le_trans h hw, e⟩

theorem mul_mem_FF2 {a b : ℕ} {p q : F2 ⊗[ℚ] F2} (hp : p ∈ FF2 a) (hq : q ∈ FF2 b) :
    p * q ∈ FF2 (a + b) := by
  have h := Submodule.mul_mem_mul hp hq
  rw [FF2, FF2, Submodule.span_mul_span] at h
  refine Submodule.span_le.mpr ?_ h
  rintro _ ⟨_, ⟨u1, v1, h1, rfl⟩, _, ⟨u2, v2, h2, rfl⟩, rfl⟩
  refine Submodule.subset_span ⟨u1 ++ u2, v1 ++ v2, by simp; omega, ?_⟩
  simp [List.map_append, List.prod_append, Algebra.TensorProduct.tmul_mul_tmul]

theorem mul_mem_FF2' {a b c : ℕ} (h : a + b = c) {p q : F2 ⊗[ℚ] F2} (hp : p ∈ FF2 a)
    (hq : q ∈ FF2 b) : p * q ∈ FF2 c := h ▸ mul_mem_FF2 hp hq

theorem tmul_mem_FF2 {i j : ℕ} {p q : F2} (hp : p ∈ FF i) (hq : q ∈ FF j) :
    p ⊗ₜ[ℚ] q ∈ FF2 (i + j) := by
  unfold FF at hp
  induction hp using Submodule.span_induction with
  | mem x hx =>
    obtain ⟨u, hu, rfl⟩ := hx
    unfold FF at hq
    induction hq using Submodule.span_induction with
    | mem y hy =>
      obtain ⟨v, hv, rfl⟩ := hy
      exact Submodule.subset_span ⟨u, v, by omega, rfl⟩
    | zero => simp
    | add a b _ _ ha hb => rw [tmul_add]; exact add_mem ha hb
    | smul r a _ ha => rw [tmul_smul]; exact Submodule.smul_mem _ r ha
  | zero => simp
  | add a b _ _ ha hb => rw [add_tmul]; exact add_mem ha hb
  | smul r a _ ha => rw [← smul_tmul']; exact Submodule.smul_mem _ r ha

theorem mem_FF2_zero (x : F2 ⊗[ℚ] F2) : x ∈ FF2 0 := by
  induction x using TensorProduct.induction_on with
  | zero => exact zero_mem _
  | tmul p q => simpa using tmul_mem_FF2 (mem_FF_zero p) (mem_FF_zero q)
  | add x y hx hy => exact add_mem hx hy

theorem cop_g (i : Fin 2) : cop (Friedrichs.g i) = Friedrichs.g i ⊗ₜ[ℚ] (1 : F2) + (1 : F2) ⊗ₜ[ℚ] Friedrichs.g i := by
  simp [cop]

/-- `Δ` respects the filtrations. -/
theorem cop_mem_FF2 {m : ℕ} {p : F2} (hp : p ∈ FF m) : cop p ∈ FF2 m := by
  have hw : ∀ w : List (Fin 2), cop (w.map (FreeAlgebra.ι ℚ)).prod ∈ FF2 w.length := by
    intro w
    induction w with
    | nil => simpa using mem_FF2_zero (cop 1)
    | cons i w ih =>
      rw [List.map_cons, List.prod_cons, map_mul]
      have hi : cop (FreeAlgebra.ι ℚ i) ∈ FF2 1 := by
        rw [show FreeAlgebra.ι ℚ i = Friedrichs.g i from rfl, cop_g]
        refine add_mem (Submodule.subset_span ⟨[i], [], by simp, by simp⟩)
          (Submodule.subset_span ⟨[], [i], by simp, by simp⟩)
      exact mul_mem_FF2' (by simp [Nat.add_comm]) hi ih
  unfold FF at hp
  induction hp using Submodule.span_induction with
  | mem p h =>
    obtain ⟨w, hw', rfl⟩ := h
    exact FF2_anti hw' (hw w)
  | zero => simp
  | add p q _ _ hp hq => rw [map_add]; exact add_mem hp hq
  | smul r p _ hp => rw [map_smul]; exact Submodule.smul_mem _ r hp

end FF2

/-! ### Scaling on `ℚ⟨X, Y⟩ ⊗ ℚ⟨X, Y⟩` and the primitive top layer -/

section Layer

/-- The scaling `scF r ⊗ scF r`. -/
noncomputable def sc2 (r : ℚ) : F2 ⊗[ℚ] F2 →ₐ[ℚ] F2 ⊗[ℚ] F2 :=
  Algebra.TensorProduct.map (scF r) (scF r)

/-- **`Δ` commutes with the scaling:** `Δ ∘ scF r = (scF r ⊗ scF r) ∘ Δ`. -/
theorem cop_scF (r : ℚ) (p : F2) : cop (scF r p) = sc2 r (cop p) := by
  have : cop.comp (scF r) = (sc2 r).comp cop := by
    apply FreeAlgebra.hom_ext
    funext i
    simp [cop, scF, sc2, smul_tmul', tmul_smul]
  exact congrArg (fun f : F2 →ₐ[ℚ] F2 ⊗[ℚ] F2 => f p) this

theorem decomp_FF2 (k : ℕ) {y : F2 ⊗[ℚ] F2} (hy : y ∈ FF2 k) :
    Decomp (fun r => (sc2 r).toLinearMap) FF2 k y := by
  refine decomp_span _ FF2 k _ ?_ hy
  rintro _ ⟨u, v, hw, rfl⟩
  refine ⟨u.length + v.length, hw, Submodule.subset_span ⟨u, v, le_rfl, rfl⟩, fun r => ?_⟩
  simp only [AlgHom.toLinearMap_apply, sc2, Algebra.TensorProduct.map_tmul, scF_word,
    smul_tmul_smul, pow_add]

/-- The primitivity defect `Δ p − p ⊗ 1 − 1 ⊗ p`. -/
noncomputable def primDef : F2 →ₗ[ℚ] F2 ⊗[ℚ] F2 :=
  cop.toLinearMap - (TensorProduct.mk ℚ F2 F2).flip 1 - TensorProduct.mk ℚ F2 F2 1

theorem primDef_apply (p : F2) : primDef p = cop p - p ⊗ₜ 1 - 1 ⊗ₜ p := rfl

theorem isPrimitive_iff (p : F2) : IsPrimitive p ↔ primDef p = 0 := by
  rw [primDef_apply, IsPrimitive, sub_sub, sub_eq_zero]

theorem primDef_mem_FF2 {m : ℕ} {p : F2} (hp : p ∈ FF m) : primDef p ∈ FF2 m := by
  rw [primDef_apply]
  refine sub_mem (sub_mem (cop_mem_FF2 hp) ?_) ?_
  · simpa using tmul_mem_FF2 hp (mem_FF_zero 1)
  · simpa using tmul_mem_FF2 (mem_FF_zero 1) hp

theorem primDef_sc2 {d : ℕ} {h : F2} (hh : Homog d h) (r : ℚ) :
    sc2 r (primDef h) = r ^ d • primDef h := by
  rw [primDef_apply, map_sub, map_sub, ← cop_scF, hh r, map_smul]
  simp only [sc2, Algebra.TensorProduct.map_tmul, hh r, map_one, smul_sub, smul_tmul']
  rw [tmul_smul, smul_tmul']

/-- **The primitive top layer.** If `p ∈ FF d` and `Δ p − p ⊗ 1 − 1 ⊗ p ∈ FF2 (d + 1)`, then the
degree-`d` part `h` of `p` is primitive: `p = h + (FF (d + 1))`, `h` homogeneous of degree `d`. -/
theorem exists_primitive_layer {d : ℕ} {p : F2} (hp : p ∈ FF d)
    (hδ : primDef p ∈ FF2 (d + 1)) :
    ∃ h, Homog d h ∧ p - h ∈ FF (d + 1) ∧ IsPrimitive h := by
  obtain ⟨h, -, hh, hph⟩ := exists_homog_part hp
  refine ⟨h, hh, hph, (isPrimitive_iff h).2 ?_⟩
  have hmem : primDef h ∈ FF2 (d + 1) := by
    have e : primDef h = primDef p - primDef (p - h) := by rw [map_sub]; abel
    rw [e]
    exact sub_mem hδ (primDef_mem_FF2 hph)
  exact eq_zero_of_decomp (fun r => (sc2 r).toLinearMap) FF2 (decomp_FF2 (d + 1) hmem)
    (fun r => primDef_sc2 hh r)

end Layer

end QOU.BraidsAndKnots.RationalAssociator
