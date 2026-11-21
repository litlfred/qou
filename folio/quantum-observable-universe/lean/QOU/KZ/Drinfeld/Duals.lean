import QOU.KZ.Drinfeld.Braided
import QOU.KZ.Drinfeld.BraidingVV
import QOU.KZ.ZigZag
import QOU.Mass.BraidedStrands
import Mathlib.CategoryTheory.Monoidal.Rigid.Basic
import QOU.MathlibExt.RigidTensorDual

/-!
# Duals in `D_ℏ`: the exact pairing `(V, V)` for every associator

Stage S4 of bean `qou-zoyv`. Let `Ψ` be any Drinfeld associator (`DrinfeldAssociator.Associator`)
and `ℏ` transcendental. After relabelling the legs of `(V ⊗ V) ⊗ V` as `Fin 3`, the associator of
`D_ℏ` is `Φ = Ψ(ℏ P₁₂, ℏ P₂₃)` (`αmat_VVV`). With `η = e₀ ⊗ e₁ − e₁ ⊗ e₀` and `ε` the invariant
form, the zigzag composite `(1 ⊗ ε) Φ (η ⊗ 1)` is a scalar `ν` (`zigΨ_scalar`: `Φ` is
`SL₂`-equivariant), and the other zigzag equals it (`zagΨ_eq_zigΨ`: conjugation by `P₁₃`).

**`ν ≠ 0` for every associator** (`νΨ_ne_zero`), by the braid relation alone. If `ν = 0`, then
`(1 ⊗ ε) Φ (η ⊗ 1) = 0`, so `Φ (η ⊗ 1)` lies in the `Sym²`-part of the last two legs and
`α⁻¹ (1 ⊗ β) α` acts on `η ⊗ 1` by `s`, while `β ⊗ 1` acts on it by `−t`. A common eigenvector
of the two braid generators with eigenvalues `−t` and `s` forces `s t (s + t) = 0` by
`σ₁σ₂σ₁ = σ₂σ₁σ₂`, and `s + t ≠ 0` for transcendental `ℏ` (`sV_add_tV_ne_zero`). No norm bound on
`ℏ` and no property of `Ψ` beyond the class laws is used.

So `(η, ν⁻¹ ε)` is an exact pairing and `D_ℏ` is right rigid for every associator and every
transcendental `ℏ`. This replaces the earlier KZ-only small-`ℏ` route
(`ZigZag.zig_ne_zero`, `‖ℏ‖ ≤ 1/12`). Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S4)
-- Ref: [kassel1995] Kassel, *Quantum Groups*, Thm XIII.1.3 (braided category ⇒ braid group action)
-/

noncomputable section

namespace QOU.KZ.Drinfeld

open QOU.KZ.DrinfeldAssociator CategoryTheory MonoidalCategory Finset QOU.KZ.FuchsianFormal
  QOU.KZ.BlockResidues QOU.KZ.KZPentagon QOU.KZ.GLnKZ QOU.KZ.ZigZag Obj

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

/-! ### Relabelling the legs of `(V ⊗ V) ⊗ V` -/

/-- The legs of `(V ⊗ V) ⊗ V` are `0, 1, 2`. -/
def e3L : Leaves (tensor (tensor V V) V) ≃ Fin 3 where
  toFun
    | Sum.inl (Sum.inl _) => 0
    | Sum.inl (Sum.inr _) => 1
    | Sum.inr _ => 2
  invFun i := if i = 0 then Sum.inl (Sum.inl ()) else if i = 1 then Sum.inl (Sum.inr ())
    else Sum.inr ()
  left_inv k := by rcases k with (k | k) | k <;> rfl
  right_inv i := by fin_cases i <;> rfl

theorem tB_single (i j : Fin 3) : tB ℂ 2 {i} {j} = P 2 i j := by
  simp [tB]; rfl

theorem e3_blkX : (blkX V V V).map e3L.toEmbedding = {0} := by
  ext i; fin_cases i <;> simp [blkX, e3L]
theorem e3_blkY : (blkY V V V).map e3L.toEmbedding = {1} := by
  ext i; fin_cases i <;> simp [blkY, e3L]
theorem e3_blkZ : (blkZ V V V).map e3L.toEmbedding = {2} := by
  ext i; fin_cases i <;> simp [blkZ, e3L]

/-! ### The associator on `(V ⊗ V) ⊗ V` -/

variable (Ψ : Associator.{0}) {c : ℂ} (hc : Transcendental ℚ c)

include Ψ hc in
theorem nonResonant_P (i j : Fin 3) : NonResonant (c • P 2 i j) := by
  have h := nonResonant_tB Ψ hc ({i} : Finset (Fin 3)) {j}
  rwa [tB_single] at h

/-- `Φ = Ψ(ℏ P₁₂, ℏ P₂₃)` on `V^{⊗3}`, legs `Fin 3`. -/
def assocΨ : Matrix (Fin 3 → Fin 2) (Fin 3 → Fin 2) ℂ :=
  Ψ.ΦN (c • P 2 (0 : Fin 3) 1) (c • P 2 1 2) (nonResonant_P Ψ hc 0 1) (nonResonant_P Ψ hc 1 2)

/-- Its inverse `Ψ(ℏ P₂₃, ℏ P₁₂)`. -/
def assocInvΨ : Matrix (Fin 3 → Fin 2) (Fin 3 → Fin 2) ℂ :=
  Ψ.ΦN (c • P 2 (1 : Fin 3) 2) (c • P 2 0 1) (nonResonant_P Ψ hc 1 2) (nonResonant_P Ψ hc 0 1)

theorem assocΨ_mul_assocInvΨ : assocΨ Ψ hc * assocInvΨ Ψ hc = 1 ∧ assocInvΨ Ψ hc * assocΨ Ψ hc = 1 :=
  ⟨(Ψ.ΦN_swap_mul _ _ _ _).2, (Ψ.ΦN_swap_mul _ _ _ _).1⟩

theorem ΦB_fin3 : ΦB Ψ hc ({0} : Finset (Fin 3)) {1} {2} = assocΨ Ψ hc :=
  Ψ.ΦN_congr (by rw [tB_single]) (by rw [tB_single]) _ _ _ _

/-- The associator on `(V ⊗ V) ⊗ V` is `assocΨ`, relabelled. -/
theorem αmat_VVV :
    αmat Ψ hc V V V = reidx (assocLegs V V V) * (reidx e3L.symm * assocΨ Ψ hc * reidx e3L) := by
  have h := reidx_ΦB Ψ hc e3L (blkX V V V) (blkY V V V) (blkZ V V V)
  rw [e3_blkX, e3_blkY, e3_blkZ, ΦB_fin3] at h
  have hΦ : ΦB Ψ hc (blkX V V V) (blkY V V V) (blkZ V V V) =
      reidx e3L.symm * (assocΨ Ψ hc * reidx e3L) := by
    rw [← h, ← Matrix.mul_assoc, reidx_mul, Equiv.self_trans_symm, reidx_refl, Matrix.one_mul]
  rw [αmat, hΦ, Matrix.mul_assoc (reidx e3L.symm)]

theorem αinv_VVV :
    αinv Ψ hc V V V =
      reidx e3L.symm * assocInvΨ Ψ hc * reidx e3L * reidx (assocLegs V V V).symm := by
  set R := reidx e3L.symm * assocInvΨ Ψ hc * reidx e3L * reidx (assocLegs V V V).symm
  have hR : αmat Ψ hc V V V * R = 1 := by
    rw [αmat_VVV]
    simp only [R, Matrix.mul_assoc]
    rw [← Matrix.mul_assoc (reidx e3L) (reidx e3L.symm), reidx_mul, Equiv.symm_trans_self,
      reidx_refl, Matrix.one_mul, ← Matrix.mul_assoc (assocΨ Ψ hc),
      (assocΨ_mul_assocInvΨ Ψ hc).1, Matrix.one_mul,
      ← Matrix.mul_assoc (reidx e3L.symm) (reidx e3L), reidx_mul, Equiv.self_trans_symm,
      reidx_refl, Matrix.one_mul, reidx_mul, Equiv.symm_trans_self, reidx_refl]
  calc αinv Ψ hc V V V = αinv Ψ hc V V V * (αmat Ψ hc V V V * R) := by rw [hR, Matrix.mul_one]
    _ = R := by rw [← Matrix.mul_assoc, αinv_mul_αmat, Matrix.one_mul]

/-! ### The zigzag scalar -/

/-- **The first zigzag is a scalar**: `Φ` commutes with `g^{⊗3}` (class law `commute`). -/
theorem zigΨ_scalar : zig (assocΨ Ψ hc) = zig (assocΨ Ψ hc) 0 0 • 1 := by
  have hcomm : ∀ g : Matrix (Fin 2) (Fin 2) ℂ, Commute (G3 g) (assocΨ Ψ hc) := fun g =>
    Ψ.commute_ΦN _ _ ((commute_permP_G3 _ g).symm.smul_right c)
      ((commute_permP_G3 _ g).symm.smul_right c)
  exact eq_smul_one_of_commute _
    (zig_mul_comm _ _ (by simp) (hcomm _)) (zig_mul_comm _ _ (by simp) (hcomm _))

/-- Conjugation by `P₁₃` exchanges `Ψ(A, B)` and `Ψ(B, A)` (class law `map`). -/
theorem conj13_assocΨ : conj13 (assocΨ Ψ hc) = assocInvΨ Ψ hc := by
  unfold assocΨ assocInvΨ
  rw [Ψ.map_ΦN conj13 continuous_conj13 _ _ _ _
    (by rw [conj13_A]; exact nonResonant_P Ψ hc 1 2)
    (by rw [conj13_B]; exact nonResonant_P Ψ hc 0 1)]
  exact Ψ.ΦN_congr conj13_A conj13_B _ _ _ _

/-- **The second zigzag equals the first.** -/
theorem zagΨ_eq_zigΨ : zag (assocInvΨ Ψ hc) = zig (assocΨ Ψ hc) := by
  rw [← conj13_assocΨ]
  show E1' * (P 2 (0 : Fin 3) 2 * assocΨ Ψ hc * P 2 0 2) * E2' = E1 * assocΨ Ψ hc * E2
  calc E1' * (P 2 (0 : Fin 3) 2 * assocΨ Ψ hc * P 2 0 2) * E2'
      = (E1' * P 2 (0 : Fin 3) 2) * assocΨ Ψ hc * (P 2 0 2 * E2') := by
        simp only [Matrix.mul_assoc]
    _ = _ := by rw [E1'_P, P_E2']; simp [Matrix.neg_mul, Matrix.mul_neg]

/-- The zigzag scalar `ν(Ψ, ℏ) = zig(Φ)₀₀`. -/
def νΨ : ℂ := zig (assocΨ Ψ hc) 0 0

/-! ### The pairing matrices -/

/-- `r · ε : V ⊗ V → 𝟙`. -/
def epsL (r : ℂ) : Matrix (Idx unit) (Idx (tensor V V)) ℂ :=
  Matrix.of fun _ x => r * eps (x (Sum.inl ())) (x (Sum.inr ()))

/-- `η : 𝟙 → V ⊗ V`. -/
def etaL : Matrix (Idx (tensor V V)) (Idx unit) ℂ :=
  Matrix.of fun y _ => eps (y (Sum.inl ())) (y (Sum.inr ()))

/-- `V ⊗ 𝟙 ≅ ℂ²`. -/
def Uout : Matrix (Idx (tensor V unit)) (Fin 2) ℂ :=
  Matrix.of fun y a => if y (Sum.inl ()) = a then 1 else 0

/-- `ℂ² ≅ 𝟙 ⊗ V`. -/
def Uin : Matrix (Fin 2) (Idx (tensor unit V)) ℂ :=
  Matrix.of fun b x => if x (Sum.inr ()) = b then 1 else 0

theorem zig_left (r : ℂ) :
    kron (1 : EndL (Leaves V)) (epsL r) * reidx (assocLegs V V V) * reidx e3L.symm =
      r • (Uout * E1) := by
  rw [Matrix.mul_assoc, reidx_mul]
  ext y x
  rw [mul_reidx_apply, kron_apply]
  simp [Matrix.mul_apply, Uout, E1, epsL, Matrix.one_apply, e3L, assocLegs, funext_iff,
    Unique.forall_iff]

theorem zig_right :
    reidx e3L * kron etaL (1 : EndL (Leaves V)) = E2 * Uin := by
  ext x w
  rw [reidx_mul_apply, kron_apply]
  simp [Matrix.mul_apply, Uin, E2, etaL, Matrix.one_apply, e3L, funext_iff, Unique.forall_iff]

theorem Uout_mul_Uin :
    Uout * Uin = reidx (rightLegs V).symm * reidx (leftLegs V) := by
  rw [reidx_mul]
  ext y x
  simp [Matrix.mul_apply, Uout, Uin, reidx, funext_iff, Unique.forall_iff, leftLegs, rightLegs]
  exact if_congr eq_comm rfl rfl

/-- `ℂ² ≅ 𝟙 ⊗ V` read on the right. -/
def Uin' : Matrix (Idx (tensor unit V)) (Fin 2) ℂ :=
  Matrix.of fun y a => if y (Sum.inr ()) = a then 1 else 0

/-- `V ⊗ 𝟙 ≅ ℂ²` read on the left. -/
def Uout' : Matrix (Fin 2) (Idx (tensor V unit)) ℂ :=
  Matrix.of fun b x => if x (Sum.inl ()) = b then 1 else 0

theorem zag_left (r : ℂ) :
    kron (epsL r) (1 : EndL (Leaves V)) * reidx e3L.symm = r • (Uin' * E1') := by
  ext y x
  rw [mul_reidx_apply, kron_apply]
  simp [Matrix.mul_apply, Uin', E1', epsL, Matrix.one_apply, e3L, funext_iff, Unique.forall_iff]

theorem zag_right :
    reidx e3L * reidx (assocLegs V V V).symm * kron (1 : EndL (Leaves V)) etaL = E2' * Uout' := by
  rw [reidx_mul]
  ext x w
  rw [reidx_mul_apply, kron_apply]
  simp [Matrix.mul_apply, Uout', E2', etaL, Matrix.one_apply, e3L, assocLegs, funext_iff,
    Unique.forall_iff]

theorem Uin'_mul_Uout' :
    Uin' * Uout' = reidx (leftLegs V).symm * reidx (rightLegs V) := by
  rw [reidx_mul]
  ext y x
  simp [Matrix.mul_apply, Uout', Uin', reidx, funext_iff, Unique.forall_iff, leftLegs, rightLegs]
  exact if_congr eq_comm rfl rfl

theorem sum_idxV {M : Type*} [AddCommMonoid M] (F : (Unit → Fin 2) → M) :
    ∑ u, F u = F (fun _ => 0) + F (fun _ => 1) := by
  rw [← (Equiv.funUnique Unit (Fin 2)).symm.sum_comp, Fin.sum_univ_two]
  rfl

theorem equivariant_etaL : Equivariant (X := unit) (Y := tensor V V) etaL := by
  intro a ha
  rw [Matrix.trace_fin_two] at ha
  ext y w
  simp [Matrix.mul_apply, kron_apply, ρ, etaL, sum_sumArrow, sum_idxV, Matrix.one_apply,
    funext_iff, Unique.forall_iff]
  generalize y (Sum.inl ()) = i
  generalize y (Sum.inr ()) = j
  fin_cases i <;> fin_cases j <;> simp [eps]
  all_goals first | exact ha | (rw [← neg_add, ha, neg_zero])

theorem equivariant_epsL (r : ℂ) : Equivariant (X := tensor V V) (Y := unit) (epsL r) := by
  intro a ha
  rw [Matrix.trace_fin_two] at ha
  ext w x
  simp [Matrix.mul_apply, kron_apply, ρ, epsL, sum_sumArrow, sum_idxV, Matrix.one_apply,
    funext_iff, Unique.forall_iff]
  generalize x (Sum.inl ()) = i
  generalize x (Sum.inr ()) = j
  fin_cases i <;> fin_cases j <;> simp [eps]
  all_goals first | exact Or.inr ha | exact Or.inr (by rw [add_comm]; exact ha)


/-! ### The zigzag composites in matrix form -/

theorem zig_eps_eta (r : ℂ) :
    kron (1 : EndL (Leaves V)) (epsL r) * αmat Ψ hc V V V * kron etaL (1 : EndL (Leaves V)) =
      (r * νΨ Ψ hc) • (Uout * Uin) := by
  rw [αmat_VVV]
  calc kron (1 : EndL (Leaves V)) (epsL r) *
        (reidx (assocLegs V V V) * (reidx e3L.symm * assocΨ Ψ hc * reidx e3L)) *
          kron etaL (1 : EndL (Leaves V))
      = (kron (1 : EndL (Leaves V)) (epsL r) * reidx (assocLegs V V V) *
          reidx e3L.symm) * assocΨ Ψ hc * (reidx e3L * kron etaL (1 : EndL (Leaves V))) := by
        simp only [Matrix.mul_assoc]
    _ = (r • (Uout * E1)) * assocΨ Ψ hc * (E2 * Uin) := by rw [zig_left, zig_right]
    _ = r • (Uout * zig (assocΨ Ψ hc) * Uin) := by
        simp only [zig, Matrix.smul_mul, Matrix.mul_assoc]
    _ = (r * νΨ Ψ hc) • (Uout * Uin) := by
        rw [zigΨ_scalar, Matrix.mul_smul, Matrix.smul_mul, smul_smul, Matrix.mul_one]; rfl

theorem zig_mat (hν : νΨ Ψ hc ≠ 0) :
    kron (1 : EndL (Leaves V)) (epsL (νΨ Ψ hc)⁻¹) * αmat Ψ hc V V V *
        kron etaL (1 : EndL (Leaves V)) =
      reidx (rightLegs V).symm * reidx (leftLegs V) := by
  rw [zig_eps_eta, inv_mul_cancel₀ hν, one_smul, Uout_mul_Uin]

theorem zag_mat (hν : νΨ Ψ hc ≠ 0) :
    kron (epsL (νΨ Ψ hc)⁻¹) (1 : EndL (Leaves V)) * αinv Ψ hc V V V *
        kron (1 : EndL (Leaves V)) etaL =
      reidx (leftLegs V).symm * reidx (rightLegs V) := by
  rw [αinv_VVV, ← Uin'_mul_Uout']
  calc kron (epsL (νΨ Ψ hc)⁻¹) (1 : EndL (Leaves V)) *
        (reidx e3L.symm * assocInvΨ Ψ hc * reidx e3L * reidx (assocLegs V V V).symm) *
          kron (1 : EndL (Leaves V)) etaL
      = (kron (epsL (νΨ Ψ hc)⁻¹) (1 : EndL (Leaves V)) * reidx e3L.symm) * assocInvΨ Ψ hc *
          (reidx e3L * reidx (assocLegs V V V).symm * kron (1 : EndL (Leaves V)) etaL) := by
        simp only [Matrix.mul_assoc]
    _ = ((νΨ Ψ hc)⁻¹ • (Uin' * E1')) * assocInvΨ Ψ hc * (E2' * Uout') := by
        rw [zag_left, zag_right]
    _ = (νΨ Ψ hc)⁻¹ • (Uin' * zag (assocInvΨ Ψ hc) * Uout') := by
        simp only [zag, Matrix.smul_mul, Matrix.mul_assoc]
    _ = Uin' * Uout' := by
        rw [zagΨ_eq_zigΨ, zigΨ_scalar, show zig (assocΨ Ψ hc) 0 0 = νΨ Ψ hc from rfl,
          Matrix.mul_smul, Matrix.smul_mul, smul_smul, inv_mul_cancel₀ hν, one_smul,
          Matrix.mul_one]

/-! ### `η` and the flip on `V ⊗ V` -/

theorem PV_mul_etaL : PV * etaL = -etaL := by
  ext y u
  rw [← reidx_swapLegs_VV, reidx_mul_apply]
  simp only [etaL, Matrix.of_apply, Matrix.neg_apply, swapLegs, Function.comp_apply,
    Equiv.sumComm_apply, Sum.swap_inl, Sum.swap_inr]
  generalize y (Sum.inl ()) = i
  generalize y (Sum.inr ()) = j
  fin_cases i <;> fin_cases j <;> simp [eps]

theorem Pm_mul_etaL : Pm * etaL = etaL := by
  rw [Pm, Matrix.smul_mul, Matrix.sub_mul, PV_mul_etaL, Matrix.one_mul, sub_neg_eq_add]
  module

/-- `P₋ = ½ η ε`. -/
theorem Pm_eq_etaL_epsL : Pm = (1 / 2 : ℂ) • (etaL * epsL 1) := by
  rw [Pm, ← reidx_swapLegs_VV]
  ext y x
  simp only [Matrix.smul_apply, Matrix.sub_apply, Matrix.mul_apply, etaL, epsL, reidx,
    Matrix.of_apply, Matrix.one_apply, smul_eq_mul, Finset.univ_unique, Finset.sum_singleton,
    one_mul]
  have e1 : (y = x) ↔ (y (Sum.inl ()) = x (Sum.inl ()) ∧ y (Sum.inr ()) = x (Sum.inr ())) := by
    constructor
    · rintro rfl; exact ⟨rfl, rfl⟩
    · rintro ⟨h1, h2⟩; funext k; rcases k with ⟨⟩ | ⟨⟩ <;> assumption
  have e2 : (x = y ∘ swapLegs V V) ↔
      (x (Sum.inl ()) = y (Sum.inr ()) ∧ x (Sum.inr ()) = y (Sum.inl ())) := by
    constructor
    · rintro rfl; exact ⟨rfl, rfl⟩
    · rintro ⟨h1, h2⟩; funext k; rcases k with ⟨⟩ | ⟨⟩ <;> assumption
  simp only [e1, e2]
  generalize y (Sum.inl ()) = i
  generalize y (Sum.inr ()) = j
  generalize x (Sum.inl ()) = k
  generalize x (Sum.inr ()) = l
  fin_cases i <;> fin_cases j <;> fin_cases k <;> fin_cases l <;> simp [eps]

theorem βmat_VV_mul_etaL (c : ℂ) : βmat c V V * etaL = (-tV c) • etaL := by
  have hp : Pp * etaL = 0 := by
    rw [show Pp = 1 - Pm by rw [← Pp_add_Pm, add_sub_cancel_right], Matrix.sub_mul,
      Pm_mul_etaL, Matrix.one_mul, sub_self]
  rw [βmat_VV, Matrix.sub_mul, Matrix.smul_mul, Matrix.smul_mul, hp, Pm_mul_etaL, smul_zero,
    zero_sub, neg_smul]

theorem kron_sub_right {α β α' β' : Type*} (f : Matrix (α → Fin 2) (β → Fin 2) ℂ)
    (g g' : Matrix (α' → Fin 2) (β' → Fin 2) ℂ) : kron f (g - g') = kron f g - kron f g' := by
  ext y x; simp [kron_apply, mul_sub]

theorem etaL_ne_zero_kron : kron etaL (1 : EndL (Leaves V)) ≠ 0 := by
  intro h
  have := congrFun (congrFun h (Sum.elim (Sum.elim (fun _ => 0) (fun _ => 1)) (fun _ => 0)))
    (fun _ => 0)
  simp [kron_apply, Matrix.one_apply, etaL, eps] at this
  exact this rfl

/-! ### `ν ≠ 0` for every associator, from the braid relation -/

section BraidRelation

variable (c) [hcF : Fact (Transcendental ℚ c)]

/-- The braid relation on `(V ⊗ V) ⊗ V` in matrix form: `σ₁ = β ⊗ 1`,
`σ₂ = α⁻¹ (1 ⊗ β) α`, `σ₁σ₂σ₁ = σ₂σ₁σ₂` (`isYB_braiding`, from the hexagons). -/
theorem yb_mat :
    kron (βmat c V V) (1 : EndL (Leaves V)) *
        (αinv Ψ hcF.out V V V * kron (1 : EndL (Leaves V)) (βmat c V V) * αmat Ψ hcF.out V V V) *
        kron (βmat c V V) (1 : EndL (Leaves V)) =
      (αinv Ψ hcF.out V V V * kron (1 : EndL (Leaves V)) (βmat c V V) * αmat Ψ hcF.out V V V) *
        kron (βmat c V V) (1 : EndL (Leaves V)) *
        (αinv Ψ hcF.out V V V * kron (1 : EndL (Leaves V)) (βmat c V V) * αmat Ψ hcF.out V V V) :=
  congrArg Subtype.val (QOU.Mass.BraidedStrands.isYB_braiding (C := DH Ψ c) (Obj.V : DH Ψ c))

/-- **The zigzag scalar is nonzero for every associator `Ψ` and transcendental `ℏ`.** -/
theorem νΨ_ne_zero : νΨ Ψ hcF.out ≠ 0 := by
  intro hν
  set T1 := kron (βmat c V V) (1 : EndL (Leaves V)) with hT1
  set T2 := αinv Ψ hcF.out V V V * kron (1 : EndL (Leaves V)) (βmat c V V) * αmat Ψ hcF.out V V V
    with hT2
  set N := kron etaL (1 : EndL (Leaves V)) with hN
  have h1 : T1 * N = (-tV c) • N := by
    rw [hT1, hN, kron_mul, βmat_VV_mul_etaL, Matrix.one_mul, kron_smul_left]
  -- `(1 ⊗ ε) α N = 0`, so `(1 ⊗ P₋) α N = 0`.
  have hε : kron (1 : EndL (Leaves V)) (epsL 1) * (αmat Ψ hcF.out V V V * N) = 0 := by
    rw [← Matrix.mul_assoc, hN, zig_eps_eta, hν, mul_zero, zero_smul]
  have hβ : kron (1 : EndL (Leaves V)) (βmat c V V) =
      sV c • 1 - (sV c + tV c) • kron (1 : EndL (Leaves V)) Pm := by
    rw [βmat_VV, show Pp = 1 - Pm by rw [← Pp_add_Pm, add_sub_cancel_right], kron_sub_right,
      kron_smul_right, kron_smul_right, kron_sub_right, kron_one]
    module
  have hPm : kron (1 : EndL (Leaves V)) Pm * (αmat Ψ hcF.out V V V * N) = 0 := by
    rw [Pm_eq_etaL_epsL, kron_smul_right, Matrix.smul_mul,
      show kron (1 : EndL (Leaves V)) (etaL * epsL 1) =
        kron (1 : EndL (Leaves V)) etaL * kron (1 : EndL (Leaves V)) (epsL 1) by
          rw [kron_mul, Matrix.one_mul],
      Matrix.mul_assoc, hε, Matrix.mul_zero, smul_zero]
  have h2 : T2 * N = sV c • N := by
    rw [hT2, Matrix.mul_assoc, Matrix.mul_assoc, hβ, Matrix.sub_mul, Matrix.smul_mul,
      Matrix.smul_mul, hPm, smul_zero, sub_zero, Matrix.one_mul, Matrix.mul_smul,
      ← Matrix.mul_assoc, αinv_mul_αmat, Matrix.one_mul]
  have e := congrArg (· * N) (yb_mat Ψ c)
  simp only [← hT1, ← hT2] at e
  simp only [Matrix.mul_assoc, h1, h2, Matrix.mul_smul, smul_smul] at e
  have hs := sV_ne_zero c
  have ht := tV_ne_zero c
  have hst := sV_add_tV_ne_zero c hcF.out
  have e2 := sub_eq_zero.2 e
  rw [← sub_smul] at e2
  have hk := (smul_eq_zero.1 e2).resolve_right etaL_ne_zero_kron
  apply mul_ne_zero (mul_ne_zero hs ht) hst
  linear_combination hk

end BraidRelation

/-! ### `V` is self-dual in `D_ℏ` -/

section Pairing

variable (Ψ : Associator.{0}) (c : ℂ) [hc : Fact (Transcendental ℚ c)]

/-- **`V` is self-dual in `D_ℏ`** for every associator and transcendental `ℏ`:
`η = e₀ ⊗ e₁ − e₁ ⊗ e₀`, `ε' = ν⁻¹ ε`, `ν ≠ 0` by `νΨ_ne_zero`. -/
instance exactPairingV : ExactPairing (C := DH Ψ c) Obj.V Obj.V where
  coevaluation' := ⟨etaL, equivariant_etaL⟩
  evaluation' := ⟨epsL (νΨ Ψ hc.out)⁻¹, equivariant_epsL _⟩
  coevaluation_evaluation' := hom_ext (by
    show kron (epsL (νΨ Ψ hc.out)⁻¹) (1 : EndL (Leaves V)) *
        αinv Ψ hc.out V V V * kron (1 : EndL (Leaves V)) etaL =
      reidx (leftLegs V).symm * reidx (rightLegs V)
    exact zag_mat Ψ hc.out (νΨ_ne_zero Ψ c))
  evaluation_coevaluation' := hom_ext (by
    show kron (1 : EndL (Leaves V)) (epsL (νΨ Ψ hc.out)⁻¹) *
        αmat Ψ hc.out V V V * kron etaL (1 : EndL (Leaves V)) =
      reidx (rightLegs V).symm * reidx (leftLegs V)
    exact zig_mat Ψ hc.out (νΨ_ne_zero Ψ c))

/-- The dual word: `𝟙ᘁ = 𝟙`, `Vᘁ = V`, `(X ⊗ Y)ᘁ = Yᘁ ⊗ Xᘁ`. -/
def dualObj : Obj → Obj
  | .unit => .unit
  | .V => .V
  | .tensor X Y => .tensor (dualObj Y) (dualObj X)

/-- The exact pairing `(X, Xᘁ)`, built from `(V, V)` by `tensorExactPairing`. -/
def pairing : (X : Obj) → ExactPairing (C := DH Ψ c) X (dualObj X)
  | .unit => (exactPairingUnit : ExactPairing (C := DH Ψ c) (𝟙_ (DH Ψ c)) (𝟙_ (DH Ψ c)))
  | .V => exactPairingV Ψ c
  | .tensor X Y =>
      @QOU.MathlibExt.tensorExactPairing (DH Ψ c) _ _ X (dualObj X) Y (dualObj Y)
        (pairing X) (pairing Y)

/-- **`D_ℏ` is right rigid** for every associator `Ψ` and transcendental `ℏ`. -/
instance rightRigid : RightRigidCategory (DH Ψ c) where
  rightDual X := ({ rightDual := (dualObj X : DH Ψ c), exact := pairing Ψ c X } :
    HasRightDual (C := DH Ψ c) X)

end Pairing

end QOU.KZ.Drinfeld
