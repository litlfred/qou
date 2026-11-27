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

/-! ### Group-likeness over `K` -/

section OverK

variable {K : Type*} [Field K] [Algebra ℚ K]

variable (K) in
/-- `Δ` with coefficients in `K`: `K ⊗ ℚ⟨X, Y⟩ → K ⊗ (ℚ⟨X, Y⟩ ⊗ ℚ⟨X, Y⟩)`. -/
noncomputable def copK : K ⊗[ℚ] F2 →ₐ[K] K ⊗[ℚ] (F2 ⊗[ℚ] F2) :=
  Algebra.TensorProduct.map (AlgHom.id K K) cop

variable (K) in
/-- `p ↦ p ⊗ 1` with coefficients in `K`. -/
noncomputable def i1K : K ⊗[ℚ] F2 →ₐ[K] K ⊗[ℚ] (F2 ⊗[ℚ] F2) :=
  Algebra.TensorProduct.map (AlgHom.id K K)
    (Algebra.TensorProduct.includeLeft : F2 →ₐ[ℚ] F2 ⊗[ℚ] F2)

variable (K) in
/-- `p ↦ 1 ⊗ p` with coefficients in `K`. -/
noncomputable def i2K : K ⊗[ℚ] F2 →ₐ[K] K ⊗[ℚ] (F2 ⊗[ℚ] F2) :=
  Algebra.TensorProduct.map (AlgHom.id K K)
    (Algebra.TensorProduct.includeRight : F2 →ₐ[ℚ] F2 ⊗[ℚ] F2)

@[simp] theorem copK_tmul (k : K) (p : F2) : copK K (k ⊗ₜ p) = k ⊗ₜ cop p := rfl

@[simp] theorem i1K_tmul (k : K) (p : F2) : i1K K (k ⊗ₜ p) = k ⊗ₜ (p ⊗ₜ (1 : F2)) := rfl

@[simp] theorem i2K_tmul (k : K) (p : F2) : i2K K (k ⊗ₜ p) = k ⊗ₜ ((1 : F2) ⊗ₜ p) := rfl

theorem i1K_one : i1K K 1 = 1 := by
  rw [Algebra.TensorProduct.one_def, i1K_tmul]; rfl

theorem i2K_one : i2K K 1 = 1 := by
  rw [Algebra.TensorProduct.one_def, i2K_tmul]; rfl

theorem copK_one : copK K 1 = 1 := by
  rw [Algebra.TensorProduct.one_def, copK_tmul, map_one]; rfl

variable (K) in
/-- `K ⊗ FF2 m`: the span of `k ⊗ (u ⊗ v)`, `u, v` words with `|u| + |v| ≥ m`. -/
def FF2K (m : ℕ) : Submodule ℚ (K ⊗[ℚ] (F2 ⊗[ℚ] F2)) :=
  Submodule.span ℚ {x | ∃ (k : K) (u v : List (Fin 2)), m ≤ u.length + v.length ∧
    x = k ⊗ₜ ((u.map (FreeAlgebra.ι ℚ)).prod ⊗ₜ[ℚ] (v.map (FreeAlgebra.ι ℚ)).prod)}

theorem tmul_mem_FF2K {m : ℕ} (k : K) {p : F2 ⊗[ℚ] F2} (hp : p ∈ FF2 m) :
    k ⊗ₜ p ∈ FF2K K m := by
  unfold FF2 at hp
  induction hp using Submodule.span_induction with
  | mem x hx =>
    obtain ⟨u, v, hw, rfl⟩ := hx
    exact Submodule.subset_span ⟨k, u, v, hw, rfl⟩
  | zero => simp
  | add a b _ _ ha hb => rw [tmul_add]; exact add_mem ha hb
  | smul r a _ ha => rw [tmul_smul]; exact Submodule.smul_mem _ r ha

theorem FF2K_anti {m n : ℕ} (h : m ≤ n) : FF2K K n ≤ FF2K K m :=
  Submodule.span_mono fun _ ⟨k, u, v, hw, e⟩ => ⟨k, u, v, le_trans h hw, e⟩

theorem mul_mem_FF2K {a b : ℕ} {x y : K ⊗[ℚ] (F2 ⊗[ℚ] F2)} (hx : x ∈ FF2K K a)
    (hy : y ∈ FF2K K b) : x * y ∈ FF2K K (a + b) := by
  unfold FF2K at hx hy
  induction hx using Submodule.span_induction with
  | zero => simp
  | add a b _ _ ha hb => rw [add_mul]; exact add_mem ha hb
  | smul r a _ ha => rw [smul_mul_assoc]; exact Submodule.smul_mem _ r ha
  | mem x hx =>
    obtain ⟨k1, u1, v1, h1, rfl⟩ := hx
    induction hy using Submodule.span_induction with
    | zero => simp
    | add a b _ _ ha hb => rw [mul_add]; exact add_mem ha hb
    | smul r a _ ha => rw [mul_smul_comm]; exact Submodule.smul_mem _ r ha
    | mem y hy =>
      obtain ⟨k2, u2, v2, h2, rfl⟩ := hy
      refine Submodule.subset_span ⟨k1 * k2, u1 ++ u2, v1 ++ v2, by simp; omega, ?_⟩
      simp only [List.map_append, List.prod_append, Algebra.TensorProduct.tmul_mul_tmul]

theorem mul_mem_FF2K' {a b c : ℕ} (h : a + b = c) {x y : K ⊗[ℚ] (F2 ⊗[ℚ] F2)}
    (hx : x ∈ FF2K K a) (hy : y ∈ FF2K K b) : x * y ∈ FF2K K c := h ▸ mul_mem_FF2K hx hy

theorem mem_FF2K_zero (x : K ⊗[ℚ] (F2 ⊗[ℚ] F2)) : x ∈ FF2K K 0 := by
  induction x using TensorProduct.induction_on with
  | zero => exact zero_mem _
  | tmul k p => exact tmul_mem_FF2K k (mem_FF2_zero p)
  | add x y hx hy => exact add_mem hx hy

theorem FF2K_mul_left {m : ℕ} (a : K ⊗[ℚ] (F2 ⊗[ℚ] F2)) {x : K ⊗[ℚ] (F2 ⊗[ℚ] F2)}
    (hx : x ∈ FF2K K m) : a * x ∈ FF2K K m :=
  mul_mem_FF2K' (zero_add m) (mem_FF2K_zero a) hx

theorem FF2K_mul_right {m : ℕ} (a : K ⊗[ℚ] (F2 ⊗[ℚ] F2)) {x : K ⊗[ℚ] (F2 ⊗[ℚ] F2)}
    (hx : x ∈ FF2K K m) : x * a ∈ FF2K K m :=
  mul_mem_FF2K' (add_zero m) hx (mem_FF2K_zero a)

/-- Products respect congruence modulo `FF2K m`. -/
theorem mul_sub_mul_mem_FF2K {m : ℕ} {x x' y y' : K ⊗[ℚ] (F2 ⊗[ℚ] F2)}
    (hx : x - x' ∈ FF2K K m) (hy : y - y' ∈ FF2K K m) : x * y - x' * y' ∈ FF2K K m := by
  have e : x * y - x' * y' = (x - x') * y + x' * (y - y') := by
    rw [sub_mul, mul_sub]; abel
  rw [e]; exact add_mem (FF2K_mul_right _ hx) (FF2K_mul_left _ hy)

/-- A rational contraction of `FF2K m` lies in `FF2 m`. -/
theorem contract_mem_FF2 (μ : K →ₗ[ℚ] ℚ) {m : ℕ} {x : K ⊗[ℚ] (F2 ⊗[ℚ] F2)}
    (hx : x ∈ FF2K K m) : contract μ (F2 ⊗[ℚ] F2) x ∈ FF2 m := by
  unfold FF2K at hx
  induction hx using Submodule.span_induction with
  | mem x hx =>
    obtain ⟨k, u, v, hw, rfl⟩ := hx
    rw [contract_tmul]
    exact Submodule.smul_mem _ _ (Submodule.subset_span ⟨u, v, hw, rfl⟩)
  | zero => simp
  | add a b _ _ ha hb => rw [map_add]; exact add_mem ha hb
  | smul r a _ ha => rw [map_smul]; exact Submodule.smul_mem _ r ha

/-- A filtered algebra map `F2 → F2 ⊗ F2`, with coefficients in `K`, maps `FFK m` into
`FF2K m`. -/
theorem mapK_mem_FF2K {f : F2 →ₐ[ℚ] F2 ⊗[ℚ] F2} (hf : ∀ {m : ℕ} {p : F2}, p ∈ FF m → f p ∈ FF2 m)
    {m : ℕ} {x : K ⊗[ℚ] F2} (hx : x ∈ FFK K m) :
    Algebra.TensorProduct.map (AlgHom.id K K) f x ∈ FF2K K m := by
  obtain ⟨z, rfl⟩ := hx
  induction z using TensorProduct.induction_on with
  | zero => simp
  | add a b ha hb => rw [map_add, map_add]; exact add_mem ha hb
  | tmul k p =>
    simp only [LinearMap.lTensor_tmul, Submodule.subtype_apply, Algebra.TensorProduct.map_tmul,
      AlgHom.id_apply]
    exact tmul_mem_FF2K k (hf p.2)

theorem copK_mem {m : ℕ} {x : K ⊗[ℚ] F2} (hx : x ∈ FFK K m) : copK K x ∈ FF2K K m :=
  mapK_mem_FF2K (fun hp => cop_mem_FF2 hp) hx

theorem i1K_mem {m : ℕ} {x : K ⊗[ℚ] F2} (hx : x ∈ FFK K m) : i1K K x ∈ FF2K K m :=
  mapK_mem_FF2K (fun {m p} hp => by simpa using tmul_mem_FF2 hp (mem_FF_zero (1 : F2))) hx

theorem i2K_mem {m : ℕ} {x : K ⊗[ℚ] F2} (hx : x ∈ FFK K m) : i2K K x ∈ FF2K K m :=
  mapK_mem_FF2K (fun {m p} hp => by simpa using tmul_mem_FF2 (mem_FF_zero (1 : F2)) hp) hx

/-- The two inclusions commute. -/
theorem i1K_mul_i2K (x y : K ⊗[ℚ] F2) : i1K K x * i2K K y = i2K K y * i1K K x := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | add a b ha hb => rw [map_add, add_mul, mul_add, ha, hb]
  | tmul k p =>
    induction y using TensorProduct.induction_on with
    | zero => simp
    | add a b ha hb => rw [map_add, add_mul, mul_add, ha, hb]
    | tmul k' q =>
      simp only [i1K_tmul, i2K_tmul, Algebra.TensorProduct.tmul_mul_tmul, mul_one, one_mul,
        mul_comm k k']

variable (K) in
/-- **Group-likeness modulo `FF2K m`:** `Δ Ψ ≡ Ψ ⊗ Ψ`. -/
def GLK (m : ℕ) (Ψ : K ⊗[ℚ] F2) : Prop :=
  copK K Ψ - i1K K Ψ * i2K K Ψ ∈ FF2K K m

variable (K) in
/-- **Primitivity modulo `FF2K m`:** `Δ a ≡ a ⊗ 1 + 1 ⊗ a`. -/
def PrimK (m : ℕ) (a : K ⊗[ℚ] F2) : Prop :=
  copK K a - (i1K K a + i2K K a) ∈ FF2K K m

theorem GLK.mul {m : ℕ} {Ψ Φ : K ⊗[ℚ] F2} (hΨ : GLK K m Ψ) (hΦ : GLK K m Φ) :
    GLK K m (Ψ * Φ) := by
  unfold GLK at *
  have hc := i1K_mul_i2K Φ Ψ
  have e : i1K K (Ψ * Φ) * i2K K (Ψ * Φ) = (i1K K Ψ * i2K K Ψ) * (i1K K Φ * i2K K Φ) := by
    calc i1K K (Ψ * Φ) * i2K K (Ψ * Φ) = i1K K Ψ * ((i1K K Φ * i2K K Ψ) * i2K K Φ) := by
          simp only [map_mul, mul_assoc]
      _ = i1K K Ψ * ((i2K K Ψ * i1K K Φ) * i2K K Φ) := by rw [hc]
      _ = _ := by simp only [mul_assoc]
  rw [map_mul, e]
  exact mul_sub_mul_mem_FF2K hΨ hΦ

theorem GLK.congr {m : ℕ} {Ψ Ψ' : K ⊗[ℚ] F2} (hΨ : GLK K m Ψ) (h : Ψ - Ψ' ∈ FFK K m) :
    GLK K m Ψ' := by
  unfold GLK at *
  have h1 := i1K_mem h
  have h2 := i2K_mem h
  have hc := copK_mem h
  rw [map_sub] at h1 h2 hc
  have hm := mul_sub_mul_mem_FF2K h1 h2
  have e : copK K Ψ' - i1K K Ψ' * i2K K Ψ' =
      (copK K Ψ - i1K K Ψ * i2K K Ψ) - (copK K Ψ - copK K Ψ') +
        (i1K K Ψ * i2K K Ψ - i1K K Ψ' * i2K K Ψ') := by abel
  rw [e]
  exact add_mem (sub_mem hΨ hc) hm

theorem GLK.anti {m n : ℕ} (h : m ≤ n) {Ψ : K ⊗[ℚ] F2} (hΨ : GLK K n Ψ) : GLK K m Ψ :=
  FF2K_anti h hΨ

/-- **Rational group-likeness modulo `FF2 m`:** `Δ y ≡ y ⊗ y`. -/
def GL (m : ℕ) (y : F2) : Prop := cop y - y ⊗ₜ y ∈ FF2 m

/-- Group-likeness of `1 ⊗ y` over `K` gives group-likeness of `y` over `ℚ`. -/
theorem GL_of_GLK {m : ℕ} {y : F2} (h : GLK K m ((1 : K) ⊗ₜ y)) : GL m y := by
  obtain ⟨π, hπ⟩ := exists_retraction (k := ℚ) (K := K)
  have := contract_mem_FF2 π h
  simp only [copK_tmul, i1K_tmul, i2K_tmul, Algebra.TensorProduct.tmul_mul_tmul, mul_one,
    one_mul, ← tmul_sub, contract_tmul, hπ, one_smul] at this
  exact this

/-- The defect `Δ − i₁ − i₂` on `K ⊗ FF d`. -/
theorem copK_sub_lTensor {d : ℕ} (z : K ⊗[ℚ] FF d) :
    copK K (LinearMap.lTensor K (FF d).subtype z) - i1K K (LinearMap.lTensor K (FF d).subtype z) -
      i2K K (LinearMap.lTensor K (FF d).subtype z) =
        LinearMap.lTensor K (primDef ∘ₗ (FF d).subtype) z := by
  induction z using TensorProduct.induction_on with
  | zero => simp
  | add a b ha hb => simp only [map_add] at ha hb ⊢; rw [← ha, ← hb]; abel
  | tmul k p =>
    simp only [LinearMap.lTensor_tmul, Submodule.subtype_apply, copK_tmul, i1K_tmul, i2K_tmul,
      LinearMap.coe_comp, Function.comp_apply, primDef_apply, tmul_sub]

/-- **The primitive top layer from group-likeness.** If `1 ⊗ Φ + z` (`z ∈ K ⊗ FF d`, `d ≥ 1`,
`ε(Φ) = 1`) is group-like modulo `FF2K (d + 1)`, then for all functionals `μ, ν : K → ℚ` the
combination `μ(1)·c_ν(z) − ν(1)·c_μ(z)` agrees modulo `FF (d + 1)` with a primitive homogeneous
element of degree `d`. -/
theorem primLayer_of_GLK {d : ℕ} (hd : 1 ≤ d) {Φ : F2}
    (hΦ : FreeAlgebra.algebraMapInv Φ = 1) (z : K ⊗[ℚ] FF d)
    (hGL : GLK K (d + 1) ((1 : K) ⊗ₜ Φ + LinearMap.lTensor K (FF d).subtype z))
    (μ ν : K →ₗ[ℚ] ℚ) :
    ∃ h : F2, Homog d h ∧
      μ 1 • (contract ν (FF d) z : F2) - ν 1 • (contract μ (FF d) z : F2) - h ∈ FF (d + 1) ∧
        IsPrimitive h := by
  set Z := LinearMap.lTensor K (FF d).subtype z with hZ
  set ρ : F2 ⊗[ℚ] F2 := cop Φ - Φ ⊗ₜ Φ with hρ
  have hZd : Z ∈ FFK K d := ⟨z, rfl⟩
  have hP1 : (1 : K) ⊗ₜ[ℚ] Φ - (1 : K ⊗[ℚ] F2) ∈ FFK K 1 := by
    have e : (1 : K) ⊗ₜ[ℚ] Φ - (1 : K ⊗[ℚ] F2) = (1 : K) ⊗ₜ (Φ - algebraMap ℚ _ (FreeAlgebra.algebraMapInv Φ)) := by
      rw [hΦ, map_one, tmul_sub, ← Algebra.TensorProduct.one_def]
    rw [e]; exact tmul_mem_FFK _ (sub_algebraMapInv_mem_FF Φ)
  -- the top-layer defect
  have hT : copK K Z - i1K K Z - i2K K Z + (1 : K) ⊗ₜ ρ ∈ FF2K K (d + 1) := by
    have a1 : (i1K K ((1 : K) ⊗ₜ Φ) - 1) * i2K K Z ∈ FF2K K (d + 1) := by
      have := i1K_mem hP1; rw [map_sub, i1K_one] at this
      exact mul_mem_FF2K' (by omega) this (i2K_mem hZd)
    have a2 : i1K K Z * (i2K K ((1 : K) ⊗ₜ Φ) - 1) ∈ FF2K K (d + 1) := by
      have := i2K_mem hP1; rw [map_sub, i2K_one] at this
      exact mul_mem_FF2K' (by omega) (i1K_mem hZd) this
    have a3 : i1K K Z * i2K K Z ∈ FF2K K (d + 1) :=
      FF2K_anti (by omega) (mul_mem_FF2K (i1K_mem hZd) (i2K_mem hZd))
    have e : copK K Z - i1K K Z - i2K K Z + (1 : K) ⊗ₜ ρ =
        (copK K ((1 : K) ⊗ₜ Φ + Z) - i1K K ((1 : K) ⊗ₜ Φ + Z) * i2K K ((1 : K) ⊗ₜ Φ + Z)) +
          (i1K K ((1 : K) ⊗ₜ Φ) - 1) * i2K K Z + i1K K Z * (i2K K ((1 : K) ⊗ₜ Φ) - 1) +
            i1K K Z * i2K K Z := by
      simp only [map_add, copK_tmul, i1K_tmul, i2K_tmul, hρ, tmul_sub, add_mul, mul_add,
        sub_mul, mul_sub, one_mul, Algebra.TensorProduct.tmul_mul_tmul, mul_one]
      abel
    rw [e]
    exact add_mem (add_mem (add_mem hGL a1) a2) a3
  -- contract
  have hR : ∀ κ : K →ₗ[ℚ] ℚ,
      primDef (contract κ (FF d) z : F2) + κ 1 • ρ ∈ FF2 (d + 1) := by
    intro κ
    have := contract_mem_FF2 κ hT
    rwa [map_add, copK_sub_lTensor, contract_lTensor, contract_tmul] at this
  set p : F2 := μ 1 • (contract ν (FF d) z : F2) - ν 1 • (contract μ (FF d) z : F2) with hp
  have hpd : p ∈ FF d :=
    sub_mem (Submodule.smul_mem _ _ (contract ν (FF d) z).2)
      (Submodule.smul_mem _ _ (contract μ (FF d) z).2)
  have hδ : primDef p ∈ FF2 (d + 1) := by
    have e : primDef p = μ 1 • (primDef (contract ν (FF d) z : F2) + ν 1 • ρ) -
        ν 1 • (primDef (contract μ (FF d) z : F2) + μ 1 • ρ) := by
      rw [hp, map_sub, map_smul, map_smul, smul_add, smul_add, smul_smul, smul_smul, mul_comm]
      abel
    rw [e]
    exact sub_mem (Submodule.smul_mem _ _ (hR ν)) (Submodule.smul_mem _ _ (hR μ))
  obtain ⟨h, hh, hph, hprim⟩ := exists_primitive_layer hpd hδ
  exact ⟨h, hh, hph, hprim⟩

end OverK

/-! ## Group-likeness of the rational exponential (piece 2, rational half) -/

section ExpGroupLike

theorem dY_primitive {y : F2} (hy : IsPrimitive y) (i : Fin 2) : IsPrimitive (dY y i) := by
  fin_cases i
  · unfold IsPrimitive at *
    simp only [dY, Fin.zero_eta, Matrix.cons_val_zero, map_sub, map_mul, hy, cop_g]
    simp only [add_mul, mul_add, Algebra.TensorProduct.tmul_mul_tmul, one_mul, mul_one, sub_tmul,
      tmul_sub]
    abel
  · simp [IsPrimitive, dY]

theorem Ly_g_mul (y : F2) (i : Fin 2) (z : F2) :
    Ly y (Friedrichs.g i * z) = Friedrichs.g i * Ly y z + dY y i * z := by
  rw [Ly, Ly, leibD_mul, leibD_ι]; noncomm_ring

/-- `L_y ⊗ id + id ⊗ L_y`. -/
noncomputable def LyT (y : F2) : F2 ⊗[ℚ] F2 →ₗ[ℚ] F2 ⊗[ℚ] F2 :=
  LinearMap.rTensor F2 (LyL y) + LinearMap.lTensor F2 (LyL y)

theorem LyT_tmul (y a b : F2) : LyT y (a ⊗ₜ b) = Ly y a ⊗ₜ b + a ⊗ₜ Ly y b := rfl

theorem LyT_cop_g_mul {y : F2} (hy : IsPrimitive y) (i : Fin 2) (t : F2 ⊗[ℚ] F2) :
    LyT y ((Friedrichs.g i ⊗ₜ 1 + 1 ⊗ₜ Friedrichs.g i) * t) =
      (Friedrichs.g i ⊗ₜ 1 + 1 ⊗ₜ Friedrichs.g i) * LyT y t + cop (dY y i) * t := by
  rw [dY_primitive hy i]
  induction t using TensorProduct.induction_on with
  | zero => simp
  | tmul a b =>
    simp only [add_mul, mul_add, Algebra.TensorProduct.tmul_mul_tmul, one_mul, map_add, LyT_tmul,
      Ly_g_mul, add_tmul, tmul_add]
    abel
  | add x z hx hz => rw [mul_add, map_add, hx, hz, map_add, mul_add, mul_add]; abel

/-- `Δ ∘ L_y = (L_y ⊗ id + id ⊗ L_y) ∘ Δ` for primitive `y`. -/
theorem cop_Ly {y : F2} (hy : IsPrimitive y) (p : F2) : cop (Ly y p) = LyT y (cop p) := by
  induction p using induction_left with
  | h1 =>
    rw [cop_one, LyT_tmul]
    simp only [Ly, leibD_one, one_mul, zero_add]
    exact hy
  | hg i z hz => rw [Ly_g_mul, map_add, map_mul, map_mul, hz, cop_g_mul, LyT_cop_g_mul hy, cop_g]
  | hadd a b ha hb => rw [Ly_add, map_add, map_add, ha, hb, map_add]
  | hsmul c z hz => rw [Ly_smul_right, map_smul, map_smul, hz, map_smul]

theorem cop_iterate_Ly {y : F2} (hy : IsPrimitive y) (k : ℕ) :
    cop ((Ly y)^[k] 1) = (LyT y ^ k) ((1 : F2) ⊗ₜ (1 : F2)) := by
  induction k with
  | zero => simp [cop_one]
  | succ k ih => rw [Function.iterate_succ_apply', cop_Ly hy, ih, pow_succ', Module.End.mul_apply]

theorem cop_iterate_Ly_sum {y : F2} (hy : IsPrimitive y) (k : ℕ) :
    cop ((Ly y)^[k] 1) = ∑ m ∈ Finset.range (k + 1),
      (k.choose m : ℚ) • ((Ly y)^[m] 1 ⊗ₜ (Ly y)^[k - m] 1) := by
  have hc : Commute (LinearMap.rTensor F2 (LyL y)) (LinearMap.lTensor F2 (LyL y)) := by
    show _ * _ = _ * _
    rw [Module.End.mul_eq_comp, Module.End.mul_eq_comp, LinearMap.rTensor_comp_lTensor,
      LinearMap.lTensor_comp_rTensor]
  rw [cop_iterate_Ly hy, LyT, hc.add_pow, LinearMap.sum_apply]
  refine Finset.sum_congr rfl fun m _ => ?_
  rw [Module.End.mul_apply, Module.End.mul_apply, LinearMap.rTensor_pow, LinearMap.lTensor_pow,
    Module.End.natCast_apply, map_nsmul, map_nsmul, LinearMap.lTensor_tmul, LinearMap.rTensor_tmul,
    Module.End.pow_apply, Module.End.pow_apply, Nat.cast_smul_eq_nsmul]
  rfl

/-- **The coproduct of the exponential terms**: `Δ e_k = Σ_{m ≤ k} e_m ⊗ e_{k − m}`. -/
theorem cop_expTerm {y : F2} (hy : IsPrimitive y) (k : ℕ) :
    cop (expTerm y k) = ∑ m ∈ Finset.range (k + 1), expTerm y m ⊗ₜ expTerm y (k - m) := by
  rw [expTerm, map_smul, cop_iterate_Ly_sum hy, Finset.smul_sum]
  refine Finset.sum_congr rfl fun m hm => ?_
  have hmk : m ≤ k := Nat.lt_succ_iff.1 (Finset.mem_range.1 hm)
  rw [expTerm, expTerm]
  simp only [← smul_tmul', tmul_smul, smul_smul]
  congr 1
  have h := Nat.choose_mul_factorial_mul_factorial hmk
  have h1 : (m.factorial : ℚ) ≠ 0 := by positivity
  have h2 : ((k - m).factorial : ℚ) ≠ 0 := by positivity
  have h3 : (k.factorial : ℚ) ≠ 0 := by positivity
  rw [← h]; push_cast
  have hC : ((k.choose m : ℕ) : ℚ) ≠ 0 := by
    exact_mod_cast (Nat.choose_pos hmk).ne'
  rw [mul_inv, mul_inv, mul_comm _ ((k.choose m : ℕ) : ℚ), ← mul_assoc, ← mul_assoc,
    mul_inv_cancel₀ hC, one_mul, mul_comm]

/-- **The truncated exponential of a primitive element is group-like modulo `FF2 n`.** -/
theorem GL_expPoly {y : F2} (hy : IsPrimitive y) (hy1 : y ∈ FF 1) (n : ℕ) :
    GL n (expPoly y n) := by
  unfold GL expPoly
  rw [map_sum]
  simp only [cop_expTerm hy]
  rw [Finset.sum_range_diag_flip n (fun m j => expTerm y m ⊗ₜ[ℚ] expTerm y j), sum_tmul]
  simp only [tmul_sum]
  rw [← Finset.sum_sub_distrib]
  refine Submodule.sum_mem _ fun m hm => ?_
  have hmn : m ≤ n := (Finset.mem_range.1 hm).le
  rw [← Finset.sum_range_add_sum_Ico _ (Nat.sub_le n m), sub_add_cancel_left, neg_mem_iff]
  refine Submodule.sum_mem _ fun j hj => ?_
  have hj' := (Finset.mem_Ico.1 hj).1
  exact FF2_anti (by omega) (tmul_mem_FF2 (expTerm_mem_FF hy1 m) (expTerm_mem_FF hy1 j))

end ExpGroupLike

end QOU.BraidsAndKnots.RationalAssociator
