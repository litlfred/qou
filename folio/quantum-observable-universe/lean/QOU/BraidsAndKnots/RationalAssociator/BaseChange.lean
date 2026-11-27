import QOU.BraidsAndKnots.RationalAssociator.AssociatorInduction

namespace QOU.BraidsAndKnots.RationalAssociator
open TensorProduct

variable {K : Type*} [Field K] [Algebra ℚ K]

section EvalK
variable {S : Type*} [Ring S] [Algebra K S] [Algebra ℚ S] [IsScalarTower ℚ K S]

/-- Evaluation of a polynomial with coefficients in `K`, written `K ⊗[ℚ] ℚ⟨X, Y⟩`, at two
elements of a `K`-algebra. -/
noncomputable def evK (a b : S) : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2) →ₐ[K] S :=
  Algebra.TensorProduct.lift (Algebra.ofId K S) (eval a b)
    (fun k _ => Algebra.commute_algebraMap_left k _)

@[simp] theorem evK_tmul (a b : S) (k : K) (p : FreeAlgebra ℚ (Fin 2)) :
    evK a b (k ⊗ₜ p) = algebraMap K S k * eval a b p := by
  simp [evK]

@[simp] theorem evK_one_tmul (a b : S) (p : FreeAlgebra ℚ (Fin 2)) :
    evK a b ((1 : K) ⊗ₜ p) = eval a b p := by
  simp

end EvalK

variable (K) in
/-- `ι : U4 N → K ⊗ U4 N`. -/
noncomputable abbrev ιK (N : ℕ) : U4 N →ₐ[ℚ] K ⊗[ℚ] U4 N := Algebra.TensorProduct.includeRight

theorem ιK_apply {N : ℕ} (u : U4 N) : ιK K N u = (1 : K) ⊗ₜ u := rfl

theorem algebraMap_mul_ιK {N : ℕ} (k : K) (u : U4 N) :
    algebraMap K (K ⊗[ℚ] U4 N) k * ιK K N u = k ⊗ₜ u := by
  simp [Algebra.TensorProduct.algebraMap_apply, Algebra.TensorProduct.tmul_mul_tmul]

theorem evK_ιK {N : ℕ} (a b : U4 N) (k : K) (p : FreeAlgebra ℚ (Fin 2)) :
    evK (ιK K N a) (ιK K N b) (k ⊗ₜ p) = k ⊗ₜ eval a b p := by
  rw [evK_tmul, ← map_eval, algebraMap_mul_ιK]


/-! ### The filtrations after base change -/

section FilK

variable {N : ℕ}

variable (K) in
/-- `K ⊗ Fil N m` inside `K ⊗ U4 N`. -/
noncomputable def FilK (N m : ℕ) : Submodule ℚ (K ⊗[ℚ] U4 N) :=
  LinearMap.range (LinearMap.lTensor K (Fil N m).subtype)

theorem tmul_mem_FilK {m : ℕ} (k : K) {u : U4 N} (hu : u ∈ Fil N m) : k ⊗ₜ u ∈ FilK K N m :=
  ⟨k ⊗ₜ ⟨u, hu⟩, by simp⟩

theorem mem_FilK_zero (x : K ⊗[ℚ] U4 N) : x ∈ FilK K N 0 := by
  induction x using TensorProduct.induction_on with
  | zero => exact zero_mem _
  | tmul k u => exact tmul_mem_FilK k (mem_Fil_zero u)
  | add x y hx hy => exact add_mem hx hy

theorem mul_mem_FilK {m n : ℕ} {x y : K ⊗[ℚ] U4 N} (hx : x ∈ FilK K N m) (hy : y ∈ FilK K N n) :
    x * y ∈ FilK K N (m + n) := by
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
      exact tmul_mem_FilK _ (mul_mem_Fil u.2 u'.2)

theorem mul_mem_FilK' {m n c : ℕ} (h : m + n = c) {x y : K ⊗[ℚ] U4 N} (hx : x ∈ FilK K N m)
    (hy : y ∈ FilK K N n) : x * y ∈ FilK K N c := h ▸ mul_mem_FilK hx hy

theorem FilK_anti {m n : ℕ} (h : m ≤ n) : FilK K N n ≤ FilK K N m := by
  rintro _ ⟨z, rfl⟩
  induction z using TensorProduct.induction_on with
  | zero => simp
  | add a b ha hb => rw [map_add]; exact add_mem ha hb
  | tmul k u => simpa using tmul_mem_FilK k (Fil_anti h u.2)

theorem eq_zero_of_mem_FilK {x : K ⊗[ℚ] U4 N} (hx : x ∈ FilK K N N) : x = 0 := by
  obtain ⟨z, rfl⟩ := hx
  induction z using TensorProduct.induction_on with
  | zero => simp
  | add a b ha hb => rw [map_add, ha, hb, add_zero]
  | tmul k u => simp [eq_zero_of_mem_Fil u.2]

theorem ιK_mem_FilK {m : ℕ} {u : U4 N} (hu : u ∈ Fil N m) : ιK K N u ∈ FilK K N m :=
  tmul_mem_FilK 1 hu

variable (K) in
/-- `K ⊗ Fil N 1` as a two-sided ideal of `K ⊗ U4 N`. -/
noncomputable def filKIdeal (N : ℕ) : TwoSidedIdeal (K ⊗[ℚ] U4 N) :=
  TwoSidedIdeal.mk' (FilK K N 1 : Set (K ⊗[ℚ] U4 N)) (zero_mem _) add_mem neg_mem
    (fun {x y} hy => mul_mem_FilK' (by omega) (mem_FilK_zero x) hy)
    (fun {x y} hx => mul_mem_FilK' (by omega) hx (mem_FilK_zero y))

theorem mem_filKIdeal {x : K ⊗[ℚ] U4 N} : x ∈ filKIdeal K N ↔ x ∈ FilK K N 1 := by
  simp [filKIdeal]

/-- In `K ⊗ U4 (d + 1)` with `d ≥ 1`, `K ⊗ Fil d` is a top layer for `K ⊗ Fil 1`. -/
theorem isTop_FilK {d : ℕ} (hd : 1 ≤ d) :
    IsTop (filKIdeal K (d + 1)) (FilK K (d + 1) d).toAddSubgroup where
  le x hx := mem_filKIdeal.2 (FilK_anti hd hx)
  mul_left x hx z hz := eq_zero_of_mem_FilK (mul_mem_FilK' rfl hx (mem_filKIdeal.1 hz))
  mul_right x hx z hz := eq_zero_of_mem_FilK (mul_mem_FilK' (by omega) (mem_filKIdeal.1 hz) hx)

end FilK

/-! ### Polynomials with coefficients in `K` -/

section FFK

variable (K) in
/-- `K ⊗ FF m` inside `K ⊗ ℚ⟨X, Y⟩`. -/
noncomputable def FFK (m : ℕ) : Submodule ℚ (K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)) :=
  LinearMap.range (LinearMap.lTensor K (FF m).subtype)

theorem tmul_mem_FFK {m : ℕ} (k : K) {p : FreeAlgebra ℚ (Fin 2)} (hp : p ∈ FF m) :
    k ⊗ₜ p ∈ FFK K m :=
  ⟨k ⊗ₜ ⟨p, hp⟩, by simp⟩

/-- Evaluating `K ⊗ FF m` at two elements of `ι (Fil N 1)` lands in `K ⊗ Fil N m`. -/
theorem evK_mem_FilK {N m : ℕ} {a b : U4 N} (ha : a ∈ Fil N 1) (hb : b ∈ Fil N 1)
    {x : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)} (hx : x ∈ FFK K m) :
    evK (ιK K N a) (ιK K N b) x ∈ FilK K N m := by
  obtain ⟨z, rfl⟩ := hx
  induction z using TensorProduct.induction_on with
  | zero => simp
  | add u v hu hv => rw [map_add, map_add]; exact add_mem hu hv
  | tmul k p =>
    simp only [LinearMap.lTensor_tmul, Submodule.subtype_apply, evK_ιK]
    exact tmul_mem_FilK k (eval_mem_Fil ha hb p.2)

/-- Evaluation at rational points commutes with `lTensor`. -/
theorem evK_lTensor {N m : ℕ} (a b : U4 N) (z : K ⊗[ℚ] FF m) :
    evK (ιK K N a) (ιK K N b) (LinearMap.lTensor K (FF m).subtype z) =
      LinearMap.lTensor K ((eval a b).toLinearMap ∘ₗ (FF m).subtype) z := by
  induction z using TensorProduct.induction_on with
  | zero => simp
  | add u v hu hv => rw [map_add, map_add, hu, hv, map_add]
  | tmul k p =>
    simp only [LinearMap.lTensor_tmul, Submodule.subtype_apply, LinearMap.coe_comp,
      Function.comp_apply, AlgHom.toLinearMap_apply]
    exact evK_ιK a b k p.1

end FFK


/-! ### Associators with coefficients in `K` -/

section AssocK

/-- The pentagon for an evaluation function `f` (Drinfeld's form, `t₁₄` does not occur). -/
def PentagonF {R : Type*} [Ring R] (f : R → R → R) (t12 t13 t23 t24 t34 : R) : Prop :=
  f t12 (t23 + t24) * f (t13 + t23) t34 = f t23 t34 * f (t12 + t13) (t24 + t34) * f t12 t23

/-- The hexagon for an evaluation function `f`, with the exponential `E ∈ ℚ⟨X, Y⟩`. -/
def HexagonF {R : Type*} [Ring R] [Algebra ℚ R] (f : R → R → R) (E : FreeAlgebra ℚ (Fin 2))
    (t12 t13 t23 : R) : Prop :=
  eval (t13 + t23) 0 E = f t13 t12 * eval t13 0 E * f t23 t13 * eval t23 0 E * f t12 t23

variable (K) in
/-- `Φ ∈ K ⊗ ℚ⟨X, Y⟩` is an associator in `K ⊗ U4 N` for the rational exponential `E`: constant
term `1`, (5.12) at every pair of `Fil N 1`, the hexagon and the pentagon at the universal
family. -/
structure AssocK (N : ℕ) (E : FreeAlgebra ℚ (Fin 2)) (Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)) :
    Prop where
  const : evK (0 : K) 0 Φ = 1
  inv : ∀ a b : U4 N, a ∈ Fil N 1 → b ∈ Fil N 1 →
    evK (ιK K N a) (ιK K N b) Φ * evK (ιK K N b) (ιK K N a) Φ = 1
  hex : HexagonF (fun a b => evK a b Φ) E (ιK K N (t N 0)) (ιK K N (t N 1)) (ιK K N (t N 3))
  pent : PentagonF (fun a b => evK a b Φ) (ιK K N (t N 0)) (ιK K N (t N 1)) (ιK K N (t N 3))
    (ιK K N (t N 4)) (ιK K N (t N 5))

end AssocK

/-! ### (B0): a `K`-associator agreeing with `Φ` modulo `FF d` gives a rational lift -/

section B0

variable {d : ℕ}

/-- The (5.12) component of the target at a pair. -/
noncomputable def projInv {N : ℕ} (p : InvIdx N) : AssocTarget N →ₗ[ℚ] U4 N :=
  LinearMap.proj p ∘ₗ LinearMap.fst ℚ _ _

/-- The hexagon component of the target. -/
noncomputable def projHex (N : ℕ) : AssocTarget N →ₗ[ℚ] U4 N :=
  LinearMap.fst ℚ _ _ ∘ₗ LinearMap.snd ℚ _ _

/-- The pentagon component of the target. -/
noncomputable def projPent (N : ℕ) : AssocTarget N →ₗ[ℚ] U4 N :=
  LinearMap.snd ℚ _ _ ∘ₗ LinearMap.snd ℚ _ _

theorem target_ext {N : ℕ} {u v : AssocTarget N} (h1 : ∀ p, projInv p u = projInv p v)
    (h2 : projHex N u = projHex N v) (h3 : projPent N u = projPent N v) : u = v :=
  Prod.ext (funext h1) (Prod.ext h2 h3)

variable (K) in
/-- `z ∈ K ⊗ FF d` solves the base-changed homogeneous degree-`d` system, component by
component. -/
def KerK (d : ℕ) (z : K ⊗[ℚ] FF d) : Prop :=
  (∀ p, LinearMap.lTensor K (projInv p ∘ₗ linFF d) z = 0) ∧
    LinearMap.lTensor K (projHex (d + 1) ∘ₗ linFF d) z = 0 ∧
    LinearMap.lTensor K (projPent (d + 1) ∘ₗ linFF d) z = 0

theorem contract_lTensor {V W : Type*} [AddCommGroup V] [Module ℚ V] [AddCommGroup W]
    [Module ℚ W] (π : K →ₗ[ℚ] ℚ) (L : V →ₗ[ℚ] W) (z : K ⊗[ℚ] V) :
    contract π W (LinearMap.lTensor K L z) = L (contract π V z) := by
  induction z using TensorProduct.induction_on with
  | zero => simp
  | tmul a v => simp
  | add x y hx hy => simp only [map_add, hx, hy]

/-- The value of `ΦK` at rational points, split as `Φ` plus the top layer. -/
theorem evK_split {N : ℕ} {Φ : FreeAlgebra ℚ (Fin 2)} (z : K ⊗[ℚ] FF d) (u v : U4 N) :
    evK (ιK K N u) (ιK K N v) ((1 : K) ⊗ₜ Φ + LinearMap.lTensor K (FF d).subtype z) =
      ιK K N (eval u v Φ) + LinearMap.lTensor K ((eval u v).toLinearMap ∘ₗ (FF d).subtype) z := by
  rw [map_add, evK_one_tmul, ← map_eval, evK_lTensor]

/-- **(B0).** Let `d ≥ 1`, `ε(Φ) = ε(E) = 1`, and let `ΦK = 1 ⊗ Φ + z` with `z ∈ K ⊗ FF d` be an
associator in `K ⊗ U4 (d + 1)`. Then there is a rational `x ∈ FF d` with `Φ + x` an associator
in `U4 (d + 1)`, and `1 ⊗ x − z` solves the base-changed homogeneous system. -/
theorem rational_lift_of_assocK (hd : 1 ≤ d) {E Φ : FreeAlgebra ℚ (Fin 2)}
    (hE : FreeAlgebra.algebraMapInv E = 1) (hΦ : FreeAlgebra.algebraMapInv Φ = 1)
    (z : K ⊗[ℚ] FF d)
    (hK : AssocK K (d + 1) E ((1 : K) ⊗ₜ Φ + LinearMap.lTensor K (FF d).subtype z)) :
    ∃ x : FF d, AssocU4 (d + 1) E (Φ + x) ∧ KerK K d ((1 : K) ⊗ₜ x - z) := by
  set N := d + 1
  have hJ := isTop_FilK (K := K) hd
  have hI : ∀ {u v : U4 N}, u ∈ Fil N 1 → v ∈ Fil N 1 →
      ∀ {p : FreeAlgebra ℚ (Fin 2)}, FreeAlgebra.algebraMapInv p = 1 →
        ιK K N (eval u v p) - 1 ∈ filKIdeal K N := by
    intro u v hu hv p hp
    have := eval_sub_mem nilIdeal_Fil hu hv p
    rw [hp, map_one] at this
    rw [← map_one (ιK K N), ← map_sub]
    exact mem_filKIdeal.2 (ιK_mem_FilK this)
  have hX : ∀ {u v : U4 N}, u ∈ Fil N 1 → v ∈ Fil N 1 →
      LinearMap.lTensor K ((eval u v).toLinearMap ∘ₗ (FF d).subtype) z ∈
        (FilK K N d).toAddSubgroup := by
    intro u v hu hv
    rw [← evK_lTensor]
    exact evK_mem_FilK hu hv ⟨z, rfl⟩
  have m := fun i => t_mem_Fil_one (N := N) i
  have m0 : (0 : U4 N) ∈ Fil N 1 := zero_mem _
  have hE0 : ∀ u : U4 N, eval (ιK K N u) 0 E = ιK K N (eval u 0 E) := fun u => by
    rw [map_eval, map_zero]
  -- the three families of component equations
  have cInv : ∀ p : InvIdx N, LinearMap.lTensor K (projInv p ∘ₗ linFF d) z =
      (1 : K) ⊗ₜ projInv p (-assocDefect N E Φ) := by
    intro p
    have h := hK.inv _ _ p.2.1 p.2.2
    rw [evK_split, evK_split] at h
    have h' := inversion_linear hJ (hI p.2.1 p.2.2 hΦ) (hI p.2.2 p.2.1 hΦ) (hX p.2.1 p.2.2)
      (hX p.2.2 p.2.1)
    rw [h, sub_self, ← map_mul] at h'
    have e : LinearMap.lTensor K (projInv p ∘ₗ linFF d) z =
        LinearMap.lTensor K ((eval p.1.1 p.1.2).toLinearMap ∘ₗ (FF d).subtype) z +
          LinearMap.lTensor K ((eval p.1.2 p.1.1).toLinearMap ∘ₗ (FF d).subtype) z := by
      rw [← LinearMap.add_apply, ← LinearMap.lTensor_add]; rfl
    rw [e, eq_neg_of_add_eq_zero_right h'.symm]
    simp only [projInv, assocDefect, LinearMap.coe_comp, Function.comp_apply, LinearMap.coe_fst,
      LinearMap.coe_proj, Prod.fst_neg, Pi.neg_apply, Function.eval, neg_sub,
      TensorProduct.tmul_sub, ← Algebra.TensorProduct.one_def]
    rfl
  have cHex : LinearMap.lTensor K (projHex N ∘ₗ linFF d) z =
      (1 : K) ⊗ₜ projHex N (-assocDefect N E Φ) := by
    have h := hK.hex
    simp only [HexagonF] at h
    rw [← map_add, hE0, hE0, hE0, evK_split, evK_split, evK_split] at h
    have h' := hexagon_linear hJ (hI (m 1) (m 0) hΦ) (hI (m 3) (m 1) hΦ) (hI (m 0) (m 3) hΦ)
      (hI (m 1) m0 hE) (hI (m 3) m0 hE) (hX (m 1) (m 0)) (hX (m 3) (m 1)) (hX (m 0) (m 3))
      (E := ιK K N (eval (t N 1 + t N 3) 0 E))
    rw [← h, sub_self] at h'
    have e : LinearMap.lTensor K (projHex N ∘ₗ linFF d) z =
        -(LinearMap.lTensor K ((eval (t N 1) (t N 0)).toLinearMap ∘ₗ (FF d).subtype) z +
          LinearMap.lTensor K ((eval (t N 3) (t N 1)).toLinearMap ∘ₗ (FF d).subtype) z +
          LinearMap.lTensor K ((eval (t N 0) (t N 3)).toLinearMap ∘ₗ (FF d).subtype) z) := by
      rw [← LinearMap.add_apply, ← LinearMap.add_apply, ← LinearMap.lTensor_add,
        ← LinearMap.lTensor_add, ← LinearMap.neg_apply, ← LinearMap.lTensor_neg]; rfl
    rw [e, ← eq_of_sub_eq_zero h'.symm]
    simp only [projHex, assocDefect, LinearMap.coe_comp, Function.comp_apply, LinearMap.coe_fst,
      LinearMap.coe_snd, Prod.snd_neg, Prod.fst_neg]
    rw [← ιK_apply]
    simp only [map_neg, map_sub, map_mul]
  have cPent : LinearMap.lTensor K (projPent N ∘ₗ linFF d) z =
      (1 : K) ⊗ₜ projPent N (-assocDefect N E Φ) := by
    have h := hK.pent
    simp only [PentagonF] at h
    simp only [← map_add, evK_split] at h
    have h' := pentagon_linear hJ (hI (m 0) (m 3) hΦ) (hI (m 0) (add_mem (m 3) (m 4)) hΦ)
      (hI (add_mem (m 0) (m 1)) (add_mem (m 4) (m 5)) hΦ) (hI (add_mem (m 1) (m 3)) (m 5) hΦ)
      (hI (m 3) (m 5) hΦ) (hX (m 0) (m 3)) (hX (m 0) (add_mem (m 3) (m 4)))
      (hX (add_mem (m 0) (m 1)) (add_mem (m 4) (m 5))) (hX (add_mem (m 1) (m 3)) (m 5))
      (hX (m 3) (m 5))
    rw [← h, sub_self] at h'
    have e : LinearMap.lTensor K (projPent N ∘ₗ linFF d) z =
        LinearMap.lTensor K ((eval (t N 3) (t N 5)).toLinearMap ∘ₗ (FF d).subtype) z +
          LinearMap.lTensor K ((eval (t N 0 + t N 1) (t N 4 + t N 5)).toLinearMap ∘ₗ
            (FF d).subtype) z +
          LinearMap.lTensor K ((eval (t N 0) (t N 3)).toLinearMap ∘ₗ (FF d).subtype) z -
          LinearMap.lTensor K ((eval (t N 0) (t N 3 + t N 4)).toLinearMap ∘ₗ (FF d).subtype) z -
          LinearMap.lTensor K ((eval (t N 1 + t N 3) (t N 5)).toLinearMap ∘ₗ (FF d).subtype) z := by
      simp only [← LinearMap.add_apply, ← LinearMap.sub_apply, ← LinearMap.lTensor_add,
        ← LinearMap.lTensor_sub]; rfl
    rw [e, eq_neg_of_add_eq_zero_right h'.symm]
    simp only [projPent, assocDefect, LinearMap.coe_comp, Function.comp_apply,
      LinearMap.coe_snd, Prod.snd_neg]
    rw [← ιK_apply]
    simp only [map_neg, map_sub, map_mul]
  -- contract along a retraction
  obtain ⟨π, hπ⟩ := exists_retraction (k := ℚ) (K := K)
  have hc : ∀ (c : AssocTarget N →ₗ[ℚ] U4 N),
      LinearMap.lTensor K (c ∘ₗ linFF d) z = (1 : K) ⊗ₜ c (-assocDefect N E Φ) →
        c (linFF d (contract π (FF d) z)) = c (-assocDefect N E Φ) := by
    intro c hcz
    rw [← LinearMap.comp_apply, ← contract_lTensor, hcz, contract_tmul, hπ, one_smul]
  set x := contract π (FF d) z
  have hlin : assocLin N x.1 = -assocDefect N E Φ :=
    target_ext (fun p => hc _ (cInv p)) (hc _ cHex) (hc _ cPent)
  refine ⟨x, (assocU4_add_iff hd hE hΦ x.2).2 hlin, ?_, ?_, ?_⟩
  · intro p
    rw [map_sub, LinearMap.lTensor_tmul, cInv p, LinearMap.comp_apply, hc _ (cInv p), sub_self]
  · rw [map_sub, LinearMap.lTensor_tmul, cHex, LinearMap.comp_apply, hc _ cHex, sub_self]
  · rw [map_sub, LinearMap.lTensor_tmul, cPent, LinearMap.comp_apply, hc _ cPent, sub_self]

end B0

end QOU.BraidsAndKnots.RationalAssociator
