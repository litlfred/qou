/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import TwistedFrobeniusHopf.SweedlerJet
import Mathlib.Algebra.MonoidAlgebra.Basic
import Mathlib.Data.ZMod.Defs
import Mathlib.RingTheory.Ideal.Maps

/-!
# Sweedler's algebra is the noncommutative jet of `k[ℤ/2]`

Let `A = k[ℤ/2]` with generator `g`, and let `Ω¹ᵤ(A) = ker (m : A ⊗ A → A)` be the
module of universal (noncommutative) differentials, an `A`-bimodule with `a · ω · b =
(a ⊗ b) ω`. The element `dg = 1 ⊗ g - g ⊗ 1` satisfies `dg · g = -(g · dg)`, so
`Sweedler.toJet` gives an algebra map `H₄ → A ⋉ Ω¹ᵤ(A)`. This file proves that the map is
an isomorphism of `k`-algebras over any commutative ring `k` (`jetEquiv`).

No `sorry`.

## References
- [leitner2026] §3 Lifting and Descent
-/

namespace QOU.LiftingDescent.Sweedler

open TensorProduct

variable (k : Type*) [CommRing k]

/-- The cyclic group of order two, written multiplicatively. -/
abbrev Z2 : Type := Multiplicative (ZMod 2)

/-- The group algebra `k[ℤ/2]`. -/
abbrev KZ2 : Type _ := MonoidAlgebra k Z2

/-- The nontrivial element of `ℤ/2`. -/
def gZ : Z2 := Multiplicative.ofAdd (1 : ZMod 2)

theorem gZ_ne_one : gZ ≠ 1 := by decide

theorem gZ_mul_gZ : gZ * gZ = 1 := by decide

theorem z2_cases (m : Z2) : m = 1 ∨ m = gZ := by
  have h : ∀ n : ZMod 2, Multiplicative.ofAdd n = 1 ∨ Multiplicative.ofAdd n = gZ := by decide
  exact h m.toAdd

/-- The generator `g` of `k[ℤ/2]`. -/
noncomputable def g2 : KZ2 k := MonoidAlgebra.single gZ 1

theorem g2_mul_g2 : g2 k * g2 k = 1 := by
  rw [g2, MonoidAlgebra.single_mul_single, one_mul, gZ_mul_gZ, MonoidAlgebra.one_def]

/-- The tensor square `k[ℤ/2] ⊗ k[ℤ/2]`, a commutative ring. -/
abbrev T2 : Type _ := KZ2 k ⊗[k] KZ2 k

/-- The kernel of multiplication `A ⊗ A → A`. -/
noncomputable def omegaIdeal : Ideal (T2 k) :=
  RingHom.ker (Algebra.TensorProduct.lmul' k : T2 k →ₐ[k] KZ2 k)

/-- Universal differentials `Ω¹ᵤ(k[ℤ/2])`. -/
def OmegaU : Type _ := omegaIdeal k

noncomputable instance : AddCommGroup (OmegaU k) := inferInstanceAs (AddCommGroup (omegaIdeal k))
noncomputable instance : Module (T2 k) (OmegaU k) := inferInstanceAs (Module (T2 k) (omegaIdeal k))

/-- The right-action ring map `Aᵐᵒᵖ → A ⊗ A`, `op b ↦ 1 ⊗ b`. -/
noncomputable def opHom : (KZ2 k)ᵐᵒᵖ →+* T2 k where
  toFun b := (1 : KZ2 k) ⊗ₜ[k] b.unop
  map_one' := rfl
  map_mul' a b := by
    rw [MulOpposite.unop_mul, Algebra.TensorProduct.tmul_mul_tmul, one_mul, mul_comm]
  map_zero' := by simp
  map_add' a b := by simp [TensorProduct.tmul_add]

noncomputable instance : Module (KZ2 k) (OmegaU k) :=
  Module.compHom (OmegaU k) (Algebra.TensorProduct.includeLeftRingHom : KZ2 k →+* T2 k)
noncomputable instance : Module (KZ2 k)ᵐᵒᵖ (OmegaU k) := Module.compHom (OmegaU k) (opHom k)
noncomputable instance : Module k (OmegaU k) := Module.compHom (OmegaU k) (algebraMap k (T2 k))

theorem smul_left (a : KZ2 k) (w : OmegaU k) :
    a • w = (a ⊗ₜ[k] (1 : KZ2 k) : T2 k) • w := rfl
theorem smul_right (b : (KZ2 k)ᵐᵒᵖ) (w : OmegaU k) :
    b • w = ((1 : KZ2 k) ⊗ₜ[k] b.unop : T2 k) • w := rfl
theorem smul_scalar (c : k) (w : OmegaU k) : c • w = algebraMap k (T2 k) c • w := rfl

instance : SMulCommClass (KZ2 k) (KZ2 k)ᵐᵒᵖ (OmegaU k) where
  smul_comm a b w := by rw [smul_left, smul_right, smul_left, smul_right, smul_smul, smul_smul,
    mul_comm]

instance : IsScalarTower k (KZ2 k) (OmegaU k) where
  smul_assoc c a w := by
    rw [smul_left, smul_left, smul_scalar, smul_smul]
    congr 1
    rw [← Algebra.smul_def]
    rfl

instance : IsScalarTower k (KZ2 k)ᵐᵒᵖ (OmegaU k) where
  smul_assoc c b w := by
    rw [smul_right, smul_right, smul_scalar, smul_smul]
    congr 1
    rw [← Algebra.smul_def, MulOpposite.unop_smul]
    first | rfl | exact (TensorProduct.tmul_smul _ _ _)

/-! ### Coordinates on `k[ℤ/2]` and `k[ℤ/2] ⊗ k[ℤ/2]` -/

/-- The coefficient of `m` in an element of `k[ℤ/2]`. -/
def coef (m : Z2) : KZ2 k →ₗ[k] k where
  toFun x := x m
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

@[simp] theorem coef_one_one : coef k 1 (1 : KZ2 k) = 1 :=
  Finsupp.single_eq_same
@[simp] theorem coef_g_one : coef k gZ (1 : KZ2 k) = 0 :=
  Finsupp.single_eq_of_ne gZ_ne_one
@[simp] theorem coef_one_g : coef k 1 (g2 k) = 0 :=
  Finsupp.single_eq_of_ne gZ_ne_one.symm
@[simp] theorem coef_g_g : coef k gZ (g2 k) = 1 :=
  Finsupp.single_eq_same

/-- Every element of `k[ℤ/2]` is `x₁ · 1 + x_g · g`. -/
theorem kz2_decomp (x : KZ2 k) : x = coef k 1 x • (1 : KZ2 k) + coef k gZ x • g2 k := by
  ext m
  rcases z2_cases m with rfl | rfl
  · change coef k 1 x = coef k 1 (coef k 1 x • (1 : KZ2 k) + coef k gZ x • g2 k)
    rw [map_add, map_smul, map_smul, coef_one_one, coef_one_g, smul_eq_mul, smul_eq_mul,
      mul_one, mul_zero, add_zero]
  · change coef k gZ x = coef k gZ (coef k 1 x • (1 : KZ2 k) + coef k gZ x • g2 k)
    rw [map_add, map_smul, map_smul, coef_g_one, coef_g_g, smul_eq_mul, smul_eq_mul,
      mul_one, mul_zero, zero_add]

/-- The bilinear coordinate `x ⊗ y ↦ x_e y_f` on `k[ℤ/2] ⊗ k[ℤ/2]`. -/
noncomputable def coef2 (e f : Z2) : T2 k →ₗ[k] k :=
  TensorProduct.lift ((LinearMap.mul k k).compl₁₂ (coef k e) (coef k f))

@[simp] theorem coef2_tmul (e f : Z2) (x y : KZ2 k) :
    coef2 k e f (x ⊗ₜ[k] y) = coef k e x * coef k f y := rfl

/-- Every element of `k[ℤ/2] ⊗ k[ℤ/2]` is a combination of `1⊗1, 1⊗g, g⊗1, g⊗g`. -/
theorem t2_decomp (t : T2 k) : ∃ p q r s : k, t = p • ((1 : KZ2 k) ⊗ₜ[k] (1 : KZ2 k)) +
    q • ((1 : KZ2 k) ⊗ₜ[k] g2 k) + r • (g2 k ⊗ₜ[k] (1 : KZ2 k)) + s • (g2 k ⊗ₜ[k] g2 k) := by
  induction t using TensorProduct.induction_on with
  | zero => exact ⟨0, 0, 0, 0, by simp⟩
  | tmul x y =>
    refine ⟨coef k 1 x * coef k 1 y, coef k 1 x * coef k gZ y, coef k gZ x * coef k 1 y,
      coef k gZ x * coef k gZ y, ?_⟩
    conv_lhs => rw [kz2_decomp k x, kz2_decomp k y]
    simp only [TensorProduct.add_tmul, TensorProduct.tmul_add, TensorProduct.smul_tmul_smul,
      mul_smul]
    abel
  | add t u ht hu =>
    obtain ⟨p, q, r, s, rfl⟩ := ht
    obtain ⟨p', q', r', s', rfl⟩ := hu
    exact ⟨p + p', q + q', r + r', s + s', by simp only [add_smul]; abel⟩

/-! ### The differential `dg` -/

/-- The underlying element of `A ⊗ A` of a differential. -/
def val (w : OmegaU k) : T2 k := (show omegaIdeal k from w).1

theorem val_injective : Function.Injective (val k) := Subtype.val_injective

theorem val_smulT (r : T2 k) (w : OmegaU k) : val k (r • w) = r * val k w := rfl
theorem val_add (w w' : OmegaU k) : val k (w + w') = val k w + val k w' := rfl
theorem val_zero : val k 0 = 0 := rfl
theorem val_smul_k (c : k) (w : OmegaU k) : val k (c • w) = c • val k w := by
  rw [smul_scalar, val_smulT]
  exact (Algebra.smul_def c (val k w)).symm
theorem val_smul_A (a : KZ2 k) (w : OmegaU k) :
    val k (a • w) = (a ⊗ₜ[k] (1 : KZ2 k)) * val k w := rfl

/-- `dg = 1 ⊗ g - g ⊗ 1` in `A ⊗ A`. -/
noncomputable def dgT : T2 k := (1 : KZ2 k) ⊗ₜ[k] g2 k - g2 k ⊗ₜ[k] (1 : KZ2 k)

theorem dgT_mem : dgT k ∈ omegaIdeal k := by
  rw [omegaIdeal, RingHom.mem_ker]
  simp [dgT]

/-- The universal differential `dg ∈ Ω¹ᵤ(k[ℤ/2])`. -/
noncomputable def dg : OmegaU k := (⟨dgT k, dgT_mem k⟩ : omegaIdeal k)

theorem val_dg : val k (dg k) = dgT k := rfl

theorem g_dgT : (g2 k ⊗ₜ[k] (1 : KZ2 k)) * dgT k =
    g2 k ⊗ₜ[k] g2 k - (1 : KZ2 k) ⊗ₜ[k] (1 : KZ2 k) := by
  rw [dgT, mul_sub, Algebra.TensorProduct.tmul_mul_tmul, Algebra.TensorProduct.tmul_mul_tmul,
    mul_one, one_mul, g2_mul_g2, mul_one]

/-- `dg · g = -(g · dg)`. -/
theorem dg_anti : MulOpposite.op (g2 k) • dg k = -(g2 k • dg k) := by
  apply val_injective
  change ((1 : KZ2 k) ⊗ₜ[k] g2 k) * dgT k = -((g2 k ⊗ₜ[k] (1 : KZ2 k)) * dgT k)
  rw [g_dgT, dgT, mul_sub]
  simp only [Algebra.TensorProduct.tmul_mul_tmul, mul_one, one_mul, g2_mul_g2]
  rw [neg_sub]

/-! ### The isomorphism -/

/-- The algebra map `H₄ → k[ℤ/2] ⋉ Ω¹ᵤ`, `G ↦ g`, `X ↦ dg`. -/
noncomputable def jetMap : Sweedler k →ₐ[k] TrivSqZeroExt (KZ2 k) (OmegaU k) :=
  toJet (g2 k) (dg k) (g2_mul_g2 k) (dg_anti k)

/-- Every element of `H₄` is a combination of `1, G, X, G X`. -/
theorem exists_coords (s : Sweedler k) :
    ∃ a b c d : k, s = a • 1 + b • G k + c • X k + d • (G k * X k) := by
  have hs : s ∈ Submodule.span k (basisSet k) := by rw [span_basisSet]; trivial
  simp only [basisSet] at hs
  obtain ⟨a, z1, hz1, rfl⟩ := Submodule.mem_span_insert.mp hs
  obtain ⟨b, z2, hz2, rfl⟩ := Submodule.mem_span_insert.mp hz1
  obtain ⟨c, z3, hz3, rfl⟩ := Submodule.mem_span_insert.mp hz2
  obtain ⟨d, rfl⟩ := Submodule.mem_span_singleton.mp hz3
  exact ⟨a, b, c, d, by abel⟩

theorem jetMap_coords (a b c d : k) :
    jetMap k (a • 1 + b • G k + c • X k + d • (G k * X k)) =
      TrivSqZeroExt.inl (a • (1 : KZ2 k) + b • g2 k) +
        TrivSqZeroExt.inr (c • dg k + d • (g2 k • dg k)) := by
  simp only [map_add, map_smul, map_mul, map_one, jetMap, toJet_G, toJet_X,
    TrivSqZeroExt.inl_mul_inr, TrivSqZeroExt.inl_add, TrivSqZeroExt.inr_add,
    TrivSqZeroExt.inl_smul, TrivSqZeroExt.inr_smul, TrivSqZeroExt.inl_one]
  abel

theorem jetMap_injective : Function.Injective (jetMap k) := by
  rw [injective_iff_map_eq_zero]
  intro s hs
  obtain ⟨a, b, c, d, rfl⟩ := exists_coords k s
  rw [jetMap_coords] at hs
  have hfst := congrArg TrivSqZeroExt.fst hs
  have hsnd := congrArg (fun t => val k (TrivSqZeroExt.snd t)) hs
  simp only [TrivSqZeroExt.fst_add, TrivSqZeroExt.fst_inl, TrivSqZeroExt.fst_inr, add_zero,
    TrivSqZeroExt.fst_zero] at hfst
  simp only [TrivSqZeroExt.snd_add, TrivSqZeroExt.snd_inl, TrivSqZeroExt.snd_inr, zero_add,
    TrivSqZeroExt.snd_zero, val_add, val_smul_k, val_smul_A, val_dg, g_dgT, val_zero] at hsnd
  have ha := congrArg (coef k 1) hfst
  have hb := congrArg (coef k gZ) hfst
  have hc := congrArg (coef2 k 1 gZ) hsnd
  have hd := congrArg (coef2 k gZ gZ) hsnd
  simp [dgT, map_sub] at ha hb hc hd
  simp [ha, hb, hc, hd]

theorem jetMap_surjective : Function.Surjective (jetMap k) := by
  intro t
  obtain ⟨p, q, r, s, hw⟩ := t2_decomp k (val k t.snd)
  have hmem : val k t.snd ∈ omegaIdeal k := (show omegaIdeal k from t.snd).2
  rw [omegaIdeal, RingHom.mem_ker, hw] at hmem
  simp only [map_add, map_smul, Algebra.TensorProduct.lmul'_apply_tmul, mul_one, one_mul,
    g2_mul_g2] at hmem
  have h1 := congrArg (coef k 1) hmem
  have hg := congrArg (coef k gZ) hmem
  simp at h1 hg
  refine ⟨coef k 1 t.fst • 1 + coef k gZ t.fst • G k + q • X k + (-p) • (G k * X k), ?_⟩
  rw [jetMap_coords]
  refine TrivSqZeroExt.ext ?_ ?_
  · simp only [TrivSqZeroExt.fst_add, TrivSqZeroExt.fst_inl, TrivSqZeroExt.fst_inr, add_zero]
    exact (kz2_decomp k t.fst).symm
  · apply val_injective
    simp only [TrivSqZeroExt.snd_add, TrivSqZeroExt.snd_inl, TrivSqZeroExt.snd_inr, zero_add,
      val_add, val_smul_k, val_smul_A, val_dg, g_dgT]
    rw [hw, dgT]
    have hs : s = -p := by linear_combination h1
    have hr : r = -q := by linear_combination hg
    rw [hs, hr]
    module

/-- **Sweedler's algebra is the noncommutative jet of `k[ℤ/2]`.** The map
`H₄ → k[ℤ/2] ⋉ Ω¹ᵤ(k[ℤ/2])`, `G ↦ g`, `X ↦ dg`, is an isomorphism of `k`-algebras. -/
noncomputable def jetEquiv : Sweedler k ≃ₐ[k] TrivSqZeroExt (KZ2 k) (OmegaU k) :=
  AlgEquiv.ofBijective (jetMap k) ⟨jetMap_injective k, jetMap_surjective k⟩

end QOU.LiftingDescent.Sweedler
