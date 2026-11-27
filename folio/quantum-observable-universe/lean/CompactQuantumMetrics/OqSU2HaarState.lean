import CompactQuantumMetrics.OqSU2Coproduct
import Mathlib.LinearAlgebra.Finsupp.LinearCombination
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Tactic.Module
import Mathlib.Tactic.FieldSimp

/-!
# The Haar state on `O_q(SU(2))`, built algebraically: torus invariance and modularity

Over any commutative ring `R` and unit `q : Rˣ` (no analysis, no Hilbert space), this
module realises the left regular representation of `O_q(SU(2))` on the free module with
basis the ordered monomials, reads off the weight-zero part, and proves the two properties
the q-Navier–Stokes energy identities need.

## The model

Basis `e(a, b, c)`, `(a, b, c) ∈ ℤ × ℕ × ℕ`, standing for `α^a β^b γ^c` (`0 ≤ a`) or
`δ^(-a) β^b γ^c` (`a < 0`). Left multiplication by the generators is
`mA, mB, mG, mD` (explicit `q`-power formulas); the seven Woronowicz relations hold on
basis vectors (`monoQuad`), so the universal property gives `monoRep : O_q(SU(2)) →ₐ End`.
Faithfulness (the PBW theorem) is **not** needed and not proved: every statement below is
about functionals defined through `monoRep`.

## Zero-weight functionals and torus invariance

For moments `λ : ℕ → R`, `zeroWeightFunctional q λ x = Λ_λ (π(x) e(0,0,0))`, where `Λ_λ`
reads `e(0,b,b) ↦ λ_b` and kills every other basis vector. The diagonal operator
`D_{u,v} e(a,b,c) = u^a v^(b-c) e(a,b,c)` intertwines `π ∘ θ_{u,v}` with `π`
(`monoRep_torus`), so every zero-weight functional is invariant under every torus
automorphism (`zeroWeightFunctional_torus`), hence under left and right translation by the
diagonal character through the coproduct (`zeroWeightFunctional_rightTrans_diagChar`,
`zeroWeightFunctional_leftTrans_diagChar`). No hypothesis on `λ` is needed.

## The modular property

Right multiplication by the generators is realised by operators `rA, rB, rG, rD` commuting
with the left action (`monoRep_comm_rA`, …). With `σ = modularAut q`,
`(α, β, γ, δ) ↦ (q⁻² α, β, γ, q² δ)`, `zeroWeightFunctional_modular` proves
`h(x y) = h(y σ(x))` for all `x, y` whenever `λ` satisfies the modular recursion
`λ_k + q λ_{k+1} = q^(-2-2k) (λ_k + q⁻¹ λ_{k+1})` (`IsModularMoments`).

## The Haar state

Over a field, `haarMoment q k = (-q)^k / [k+1]_{q²}` (Woronowicz's `h((βγ)^k)`), and
`haarState q := zeroWeightFunctional q (haarMoment q)`. It has `h(1) = 1`, is torus- and
diagonal-translation invariant, satisfies the rank-one relations of
`haar_cleared_alpha_delta` when `1 + q² ≠ 0` (`haarState_rankOne`), and is modular
(`haarState_modular`) when no `[k+1]_{q²}` vanishes. Invariance under the full coproduct,
`(id ⊗ h) Δ = h(·) 1`, is not proved here.

References: S. L. Woronowicz (1987); A. Klimyk & K. Schmüdgen (1997) §4.3.
-- Ref: [woronowicz1987]
-/

namespace QOU.AlgebraicSubstrate.OqSU2

open Finsupp

variable {R : Type*} [CommRing R]

/-- Index of the ordered-monomial basis: `(a, b, c)` stands for `α^a β^b γ^c` when
`0 ≤ a` and for `δ^(-a) β^b γ^c` when `a < 0`. -/
abbrev MonoIdx := ℤ × ℕ × ℕ

/-- The model module `R^(ℤ × ℕ × ℕ)`. -/
abbrev MonoMod (R : Type*) [CommRing R] := MonoIdx →₀ R

/-- Basis vector `e(a, b, c)`. -/
noncomputable abbrev eb (R : Type*) [CommRing R] (a : ℤ) (b c : ℕ) : MonoMod R :=
  Finsupp.single (a, b, c) 1

/-- `q ^ z` in `R` for an integer `z`. -/
noncomputable def qz (q : Rˣ) (z : ℤ) : R := ((q ^ z : Rˣ) : R)

@[simp] theorem qz_mul (q : Rˣ) (x y : ℤ) : qz q x * qz q y = qz q (x + y) := by
  simp [qz, zpow_add]

@[simp] theorem qz_zero (q : Rˣ) : qz q 0 = 1 := by simp [qz]

theorem val_eq_qz (q : Rˣ) : (q : R) = qz q 1 := by simp [qz]

theorem val_inv_eq_qz (q : Rˣ) : ((q⁻¹ : Rˣ) : R) = qz q (-1) := by simp [qz]

theorem qz_mul_smul (q : Rˣ) (x y : ℤ) (v : MonoMod R) :
    qz q x • qz q y • v = qz q (x + y) • v := by
  rw [smul_smul, qz_mul]

section Model

variable (q : Rˣ)

/-- Left multiplication by `α` on ordered monomials. -/
noncomputable def mA : Module.End R (MonoMod R) :=
  linearCombination R fun i : MonoIdx =>
    if 0 ≤ i.1 then eb R (i.1 + 1) i.2.1 i.2.2
    else eb R (i.1 + 1) i.2.1 i.2.2 + qz q (-2 * i.1 - 1) • eb R (i.1 + 1) (i.2.1 + 1) (i.2.2 + 1)

/-- Left multiplication by `δ` on ordered monomials. -/
noncomputable def mD : Module.End R (MonoMod R) :=
  linearCombination R fun i : MonoIdx =>
    if i.1 ≤ 0 then eb R (i.1 - 1) i.2.1 i.2.2
    else eb R (i.1 - 1) i.2.1 i.2.2 + qz q (1 - 2 * i.1) • eb R (i.1 - 1) (i.2.1 + 1) (i.2.2 + 1)

/-- Left multiplication by `β` on ordered monomials. -/
noncomputable def mB : Module.End R (MonoMod R) :=
  linearCombination R fun i : MonoIdx => qz q (-i.1) • eb R i.1 (i.2.1 + 1) i.2.2

/-- Left multiplication by `γ` on ordered monomials. -/
noncomputable def mG : Module.End R (MonoMod R) :=
  linearCombination R fun i : MonoIdx => qz q (-i.1) • eb R i.1 i.2.1 (i.2.2 + 1)

theorem mA_e (a : ℤ) (b c : ℕ) : mA q (eb R a b c) =
    if 0 ≤ a then eb R (a + 1) b c
    else eb R (a + 1) b c + qz q (-2 * a - 1) • eb R (a + 1) (b + 1) (c + 1) := by
  simp [mA, linearCombination_single]

theorem mA_e_nonneg {a : ℤ} (ha : 0 ≤ a) (b c : ℕ) : mA q (eb R a b c) = eb R (a + 1) b c := by
  rw [mA_e, if_pos ha]

theorem mA_e_neg {a : ℤ} (ha : a < 0) (b c : ℕ) : mA q (eb R a b c) =
    eb R (a + 1) b c + qz q (-2 * a - 1) • eb R (a + 1) (b + 1) (c + 1) := by
  rw [mA_e, if_neg (not_le.2 ha)]

theorem mD_e (a : ℤ) (b c : ℕ) : mD q (eb R a b c) =
    if a ≤ 0 then eb R (a - 1) b c
    else eb R (a - 1) b c + qz q (1 - 2 * a) • eb R (a - 1) (b + 1) (c + 1) := by
  simp [mD, linearCombination_single]

theorem mD_e_nonpos {a : ℤ} (ha : a ≤ 0) (b c : ℕ) : mD q (eb R a b c) = eb R (a - 1) b c := by
  rw [mD_e, if_pos ha]

theorem mD_e_pos {a : ℤ} (ha : 0 < a) (b c : ℕ) : mD q (eb R a b c) =
    eb R (a - 1) b c + qz q (1 - 2 * a) • eb R (a - 1) (b + 1) (c + 1) := by
  rw [mD_e, if_neg (not_le.2 ha)]

@[simp] theorem mB_e (a : ℤ) (b c : ℕ) : mB q (eb R a b c) = qz q (-a) • eb R a (b + 1) c := by
  simp [mB, linearCombination_single]

@[simp] theorem mG_e (a : ℤ) (b c : ℕ) : mG q (eb R a b c) = qz q (-a) • eb R a b (c + 1) := by
  simp [mG, linearCombination_single]

/-- Two endomorphisms of the model agree once they agree on every `e(a, b, c)`. -/
theorem mono_ext {f g : Module.End R (MonoMod R)}
    (h : ∀ a b c, f (eb R a b c) = g (eb R a b c)) : f = g := by
  apply Finsupp.lhom_ext'
  rintro ⟨a, b, c⟩
  apply LinearMap.ext_ring
  exact h a b c

/-- The four model operators satisfy Woronowicz's seven relations. -/
theorem monoQuad : IsOqSU2Quadruple (R := R) q (mA q) (mB q) (mG q) (mD q) := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> apply mono_ext <;> intro a b c <;>
    simp only [Module.End.mul_apply, LinearMap.smul_apply, LinearMap.sub_apply,
      Module.End.one_apply, mB_e, mG_e, map_smul, mA_e, mD_e] <;>
    (try rw [val_inv_eq_qz]) <;> (try rw [val_eq_qz]) <;>
    split_ifs <;>
    simp only [mB_e, mG_e, map_smul, map_add, smul_add, smul_smul, qz_mul, mA_e, mD_e,
      sub_add_cancel, add_sub_cancel_right] <;>
    (try split_ifs) <;> (try omega) <;>
    ring_nf <;> (try abel_nf)

/-- The model representation `π : O_q(SU(2)) → End_R (R^(ℤ×ℕ×ℕ))`. -/
noncomputable def monoRep : OqSU2 R q →ₐ[R] Module.End R (MonoMod R) :=
  liftQuadruple q (mA q) (mB q) (mG q) (mD q) (monoQuad q)

end Model

/-! ## Generation and intertwiners -/

section Gen

variable {q : Rˣ}

/-- A subalgebra of `O_q(SU(2))` containing the four generators is everything. -/
theorem mem_of_gens (S : Subalgebra R (OqSU2 R q)) (hα : α q ∈ S) (hβ : β q ∈ S)
    (hγ : γ q ∈ S) (hδ : δ q ∈ S) (x : OqSU2 R q) : x ∈ S := by
  let f : OqSU2 R q →ₐ[R] S := liftQuadruple q ⟨α q, hα⟩ ⟨β q, hβ⟩ ⟨γ q, hγ⟩ ⟨δ q, hδ⟩
    { ab := Subtype.ext (by simpa using rel_ab q)
      ag := Subtype.ext (by simpa using rel_ag q)
      bd := Subtype.ext (by simpa using rel_bd q)
      gd := Subtype.ext (by simpa using rel_gd q)
      bg := Subtype.ext (by simpa using rel_bg q)
      det_left := Subtype.ext (by simpa using rel_det_left q)
      det_right := Subtype.ext (by simpa using rel_det_right q) }
  have hf : S.val.comp f = AlgHom.id R _ := algHom_ext (by simp [f]) (by simp [f])
    (by simp [f]) (by simp [f])
  have hx := (f x).2
  have e : ((f x : S) : OqSU2 R q) = x := AlgHom.congr_fun hf x
  rwa [e] at hx

/-- Intertwining `φ(x) T = T ψ(x)` propagates from generators to all of `O_q(SU(2))`. -/
theorem intertwine_of_gens {B : Type*} [Ring B] [Algebra R B] (φ ψ : OqSU2 R q →ₐ[R] B) (T : B)
    (hα : φ (α q) * T = T * ψ (α q)) (hβ : φ (β q) * T = T * ψ (β q))
    (hγ : φ (γ q) * T = T * ψ (γ q)) (hδ : φ (δ q) * T = T * ψ (δ q)) (x : OqSU2 R q) :
    φ x * T = T * ψ x := by
  let S : Subalgebra R (OqSU2 R q) :=
    { carrier := {x | φ x * T = T * ψ x}
      mul_mem' := by
        intro x y hx hy
        simp only [Set.mem_setOf_eq, map_mul] at *
        rw [mul_assoc, hy, ← mul_assoc, hx, mul_assoc]
      add_mem' := by
        intro x y hx hy
        simp only [Set.mem_setOf_eq, map_add, add_mul, mul_add] at *
        rw [hx, hy]
      algebraMap_mem' := by
        intro r
        simp only [Set.mem_setOf_eq, AlgHom.commutes]
        exact Algebra.commutes r T }
  exact mem_of_gens S hα hβ hγ hδ x

end Gen

/-! ## The torus and the zero-weight functionals -/

/-- Rewrite one unit scalar into another. -/
theorem smul_units_congr {X Y : Rˣ} (h : X = Y) (e : MonoMod R) : (X : R) • e = (Y : R) • e := by
  rw [h]

/-- Decide an identity between products of integer powers of units, by passing to `Additive`. -/
macro "units_ac" : tactic =>
  `(tactic| (apply Additive.ofMul.injective <;>
    simp only [ofMul_mul, ofMul_zpow, ofMul_inv, Nat.cast_add, Nat.cast_one, Nat.cast_zero] <;>
    module))

section Torus

variable (q : Rˣ)

/-- The diagonal operator `D_{u,v} e(a,b,c) = u^a v^(b-c) e(a,b,c)`. -/
noncomputable def torusDiag (u v : Rˣ) : Module.End R (MonoMod R) :=
  linearCombination R fun i : MonoIdx =>
    ((u ^ i.1 * v ^ ((i.2.1 : ℤ) - i.2.2) : Rˣ) : R) • eb R i.1 i.2.1 i.2.2

@[simp] theorem torusDiag_e (u v : Rˣ) (a : ℤ) (b c : ℕ) :
    torusDiag u v (eb R a b c) = ((u ^ a * v ^ ((b : ℤ) - c) : Rˣ) : R) • eb R a b c := by
  simp [torusDiag, linearCombination_single]

theorem torusDiag_e000 (u v : Rˣ) : torusDiag u v (eb R 0 0 0) = eb R 0 0 0 := by simp

/-- `π(θ_{u,v} x) D_{u,v} = D_{u,v} π(x)`. -/
theorem monoRep_torus (u v : Rˣ) (x : OqSU2 R q) :
    monoRep q (torusScaleAlgHom q u v x) * torusDiag u v = torusDiag u v * monoRep q x := by
  refine intertwine_of_gens ((monoRep q).comp (torusScaleAlgHom q u v)) (monoRep q) _
    ?_ ?_ ?_ ?_ x <;> apply mono_ext <;> intro a b c <;>
    simp only [AlgHom.comp_apply, torusScaleAlgHom, liftQuadruple_alpha, liftQuadruple_beta,
      liftQuadruple_gamma, liftQuadruple_delta, monoRep, map_smul, Module.End.mul_apply,
      LinearMap.smul_apply, torusDiag_e, mA_e, mB_e, mG_e, mD_e] <;>
    (try split_ifs) <;>
    simp only [map_add, map_smul, torusDiag_e, smul_add, smul_smul, qz, ← Units.val_mul] <;>
    first
      | exact smul_units_congr (by units_ac) _
      | (congr 1 <;> exact smul_units_congr (by units_ac) _)

/-- `Λ_λ`: pair the weight-zero coordinates `e(0,b,b)` with the moments `λ`. -/
noncomputable def zeroRead (lam : ℕ → R) : MonoMod R →ₗ[R] R :=
  linearCombination R fun i : MonoIdx => if i.1 = 0 ∧ i.2.1 = i.2.2 then lam i.2.1 else 0

@[simp] theorem zeroRead_e (lam : ℕ → R) (a : ℤ) (b c : ℕ) :
    zeroRead lam (eb R a b c) = if a = 0 ∧ b = c then lam b else 0 := by
  simp [zeroRead, linearCombination_single]

@[simp] theorem zeroRead_single (lam : ℕ → R) (a : ℤ) (b c : ℕ) (r : R) :
    zeroRead lam (Finsupp.single (a, b, c) r) = r * if a = 0 ∧ b = c then lam b else 0 := by
  simp [zeroRead, linearCombination_single]

theorem zeroRead_torusDiag (lam : ℕ → R) (u v : Rˣ) (w : MonoMod R) :
    zeroRead lam (torusDiag u v w) = zeroRead lam w := by
  have : (zeroRead lam).comp (torusDiag u v) = zeroRead lam := by
    apply Finsupp.lhom_ext'
    rintro ⟨a, b, c⟩
    apply LinearMap.ext_ring
    simp only [LinearMap.comp_apply, Finsupp.lsingle_apply]
    rw [torusDiag_e, map_smul, zeroRead_e]
    split_ifs with h
    · obtain ⟨rfl, rfl⟩ := h
      simp
    · simp
  exact LinearMap.congr_fun this w

/-- The zero-weight functional with moments `λ`: `x ↦ Λ_λ (π(x) e(0,0,0))`. -/
noncomputable def zeroWeightFunctional (lam : ℕ → R) : OqSU2 R q →ₗ[R] R :=
  (zeroRead lam).comp ((LinearMap.applyₗ (eb R 0 0 0)).comp (monoRep q).toLinearMap)

theorem zeroWeightFunctional_apply (lam : ℕ → R) (x : OqSU2 R q) :
    zeroWeightFunctional q lam x = zeroRead lam (monoRep q x (eb R 0 0 0)) := rfl

/-- **Torus invariance.** Every zero-weight functional is invariant under every torus
automorphism `θ_{u,v}`. -/
theorem zeroWeightFunctional_torus (lam : ℕ → R) (u v : Rˣ) (x : OqSU2 R q) :
    zeroWeightFunctional q lam (torusScaleAlgHom q u v x) = zeroWeightFunctional q lam x := by
  rw [zeroWeightFunctional_apply, zeroWeightFunctional_apply, ← torusDiag_e000 u v,
    ← Module.End.mul_apply, monoRep_torus, Module.End.mul_apply, zeroRead_torusDiag,
    torusDiag_e000]

/-- Right translation by the diagonal character (through the coproduct) preserves every
zero-weight functional. -/
theorem zeroWeightFunctional_rightTrans_diagChar (lam : ℕ → R) (u : Rˣ) (x : OqSU2 R q) :
    zeroWeightFunctional q lam (rightTrans q (diagCharAlgHom q u) x) =
      zeroWeightFunctional q lam x := by
  rw [rightTrans_diagChar]
  exact zeroWeightFunctional_torus q lam u u⁻¹ x

/-- Left translation by the diagonal character preserves every zero-weight functional. -/
theorem zeroWeightFunctional_leftTrans_diagChar (lam : ℕ → R) (u : Rˣ) (x : OqSU2 R q) :
    zeroWeightFunctional q lam (leftTrans q (diagCharAlgHom q u) x) =
      zeroWeightFunctional q lam x := by
  rw [leftTrans_diagChar]
  exact zeroWeightFunctional_torus q lam u u x

theorem zeroWeightFunctional_torusEquiv (lam : ℕ → R) (u v : Rˣ) (x : OqSU2 R q) :
    zeroWeightFunctional q lam (torusScaleAlgEquiv q u v x) = zeroWeightFunctional q lam x :=
  zeroWeightFunctional_torus q lam u v x

theorem zeroWeightFunctional_one (lam : ℕ → R) : zeroWeightFunctional q lam 1 = lam 0 := by
  simp [zeroWeightFunctional_apply]

theorem zeroWeightFunctional_beta_gamma (lam : ℕ → R) :
    zeroWeightFunctional q lam (β q * γ q) = lam 1 := by
  simp [zeroWeightFunctional_apply, monoRep]

end Torus

/-! ## Right multiplication and the modular property -/

section Modular

variable (q : Rˣ)

/-- Right multiplication by `α` on ordered monomials. -/
noncomputable def rA : Module.End R (MonoMod R) :=
  linearCombination R fun i : MonoIdx =>
    if 0 ≤ i.1 then qz q (-((i.2.1 : ℤ) + i.2.2)) • eb R (i.1 + 1) i.2.1 i.2.2
    else qz q (-((i.2.1 : ℤ) + i.2.2)) •
      (eb R (i.1 + 1) i.2.1 i.2.2 + qz q (-1) • eb R (i.1 + 1) (i.2.1 + 1) (i.2.2 + 1))

/-- Right multiplication by `δ` on ordered monomials. -/
noncomputable def rD : Module.End R (MonoMod R) :=
  linearCombination R fun i : MonoIdx =>
    if i.1 ≤ 0 then qz q ((i.2.1 : ℤ) + i.2.2) • eb R (i.1 - 1) i.2.1 i.2.2
    else qz q ((i.2.1 : ℤ) + i.2.2) •
      (eb R (i.1 - 1) i.2.1 i.2.2 + qz q 1 • eb R (i.1 - 1) (i.2.1 + 1) (i.2.2 + 1))

/-- Right multiplication by `β` on ordered monomials. -/
noncomputable def rB : Module.End R (MonoMod R) :=
  linearCombination R fun i : MonoIdx => eb R i.1 (i.2.1 + 1) i.2.2

/-- Right multiplication by `γ` on ordered monomials. -/
noncomputable def rG : Module.End R (MonoMod R) :=
  linearCombination R fun i : MonoIdx => eb R i.1 i.2.1 (i.2.2 + 1)

theorem rA_e (a : ℤ) (b c : ℕ) : rA q (eb R a b c) =
    if 0 ≤ a then qz q (-((b : ℤ) + c)) • eb R (a + 1) b c
    else qz q (-((b : ℤ) + c)) • (eb R (a + 1) b c + qz q (-1) • eb R (a + 1) (b + 1) (c + 1)) := by
  simp [rA, linearCombination_single]

theorem rD_e (a : ℤ) (b c : ℕ) : rD q (eb R a b c) =
    if a ≤ 0 then qz q ((b : ℤ) + c) • eb R (a - 1) b c
    else qz q ((b : ℤ) + c) • (eb R (a - 1) b c + qz q 1 • eb R (a - 1) (b + 1) (c + 1)) := by
  simp [rD, linearCombination_single]

@[simp] theorem rB_e (a : ℤ) (b c : ℕ) : rB (R := R) (eb R a b c) = eb R a (b + 1) c := by
  simp [rB, linearCombination_single]

@[simp] theorem rG_e (a : ℤ) (b c : ℕ) : rG (R := R) (eb R a b c) = eb R a b (c + 1) := by
  simp [rG, linearCombination_single]

/-- Close a commutation goal between a left generator and a right operator on `e(a,b,c)`. -/
macro "comm_tac" : tactic =>
  `(tactic| (apply mono_ext <;> intro a b c <;>
    simp only [monoRep, liftQuadruple_alpha, liftQuadruple_beta, liftQuadruple_gamma,
      liftQuadruple_delta, Module.End.mul_apply, mA_e, mB_e, mG_e, mD_e, rA_e, rB_e, rG_e,
      rD_e, map_smul] <;>
    (try split_ifs) <;>
    simp only [mB_e, mG_e, map_smul, map_add, smul_add, smul_smul, qz_mul, mA_e, mD_e,
      rA_e, rD_e, rB_e, rG_e, sub_add_cancel, add_sub_cancel_right] <;>
    (try split_ifs) <;> (try omega) <;>
    simp only [smul_add, smul_smul, qz_mul, Nat.cast_add, Nat.cast_one] <;>
    ring_nf <;> (try abel_nf) <;>
    first
      | done
      | (have h' : a = -1 := by omega
         subst h'; ring_nf)
      | (have h' : a = 0 := by omega
         subst h'; ring_nf)
      | (have h' : a = 1 := by omega
         subst h'; ring_nf)))

theorem monoRep_comm_rA (y : OqSU2 R q) : monoRep q y * rA q = rA q * monoRep q y := by
  refine intertwine_of_gens (monoRep q) (monoRep q) _ ?_ ?_ ?_ ?_ y <;> comm_tac

theorem monoRep_comm_rB (y : OqSU2 R q) : monoRep q y * rB = rB * monoRep q y := by
  refine intertwine_of_gens (monoRep q) (monoRep q) _ ?_ ?_ ?_ ?_ y <;> comm_tac

theorem monoRep_comm_rG (y : OqSU2 R q) : monoRep q y * rG = rG * monoRep q y := by
  refine intertwine_of_gens (monoRep q) (monoRep q) _ ?_ ?_ ?_ ?_ y <;> comm_tac

theorem monoRep_comm_rD (y : OqSU2 R q) : monoRep q y * rD q = rD q * monoRep q y := by
  refine intertwine_of_gens (monoRep q) (monoRep q) _ ?_ ?_ ?_ ?_ y <;> comm_tac

/-- The modular automorphism `σ : (α, β, γ, δ) ↦ (q⁻² α, β, γ, q² δ)`. -/
noncomputable def modularAut : OqSU2 R q →ₐ[R] OqSU2 R q := torusScaleAlgHom q (q⁻¹ ^ 2) 1

/-- Moments `λ` satisfying the modular recursion
`λ_k + q λ_{k+1} = q^(-2-2k) (λ_k + q⁻¹ λ_{k+1})`. -/
def IsModularMoments (lam : ℕ → R) : Prop :=
  ∀ k : ℕ, lam k + qz q 1 * lam (k + 1) = qz q (-2 - 2 * k) * (lam k + qz q (-1) * lam (k + 1))

theorem modular_of_gen (lam : ℕ → R) (g : OqSU2 R q) (T : Module.End R (MonoMod R))
    (hcomm : ∀ y, monoRep q y * T = T * monoRep q y)
    (h0 : T (eb R 0 0 0) = monoRep q (modularAut q g) (eb R 0 0 0))
    (hΛ : ∀ w, zeroRead lam (monoRep q g w) = zeroRead lam (T w)) (y : OqSU2 R q) :
    zeroWeightFunctional q lam (g * y) = zeroWeightFunctional q lam (y * modularAut q g) := by
  rw [zeroWeightFunctional_apply, zeroWeightFunctional_apply, map_mul, map_mul,
    Module.End.mul_apply, Module.End.mul_apply, hΛ, ← h0, ← Module.End.mul_apply T,
    ← hcomm, Module.End.mul_apply]

theorem zeroRead_comp_ext (lam : ℕ → R) {f g : Module.End R (MonoMod R)}
    (h : ∀ a b c, zeroRead lam (f (eb R a b c)) = zeroRead lam (g (eb R a b c))) (w : MonoMod R) :
    zeroRead lam (f w) = zeroRead lam (g w) := by
  have : (zeroRead lam).comp f = (zeroRead lam).comp g := by
    apply Finsupp.lhom_ext'
    rintro ⟨a, b, c⟩
    apply LinearMap.ext_ring
    exact h a b c
  exact LinearMap.congr_fun this w

/-- **The modular property.** If the moments satisfy the modular recursion, the zero-weight
functional `h` satisfies `h (x y) = h (y σ(x))` for all `x, y`. -/
theorem zeroWeightFunctional_modular (lam : ℕ → R) (hlam : IsModularMoments q lam)
    (x y : OqSU2 R q) :
    zeroWeightFunctional q lam (x * y) = zeroWeightFunctional q lam (y * modularAut q x) := by
  let S : Subalgebra R (OqSU2 R q) :=
    { carrier := {x | ∀ y, zeroWeightFunctional q lam (x * y) =
        zeroWeightFunctional q lam (y * modularAut q x)}
      mul_mem' := by
        intro x₁ x₂ h₁ h₂ y
        simp only [Set.mem_setOf_eq] at *
        rw [mul_assoc, h₁, mul_assoc, h₂, map_mul (modularAut q) x₁ x₂, mul_assoc]
      add_mem' := by
        intro x₁ x₂ h₁ h₂ y
        simp only [Set.mem_setOf_eq] at *
        rw [add_mul, map_add, map_add, mul_add, map_add, h₁, h₂]
      algebraMap_mem' := by
        intro r y
        rw [AlgHom.commutes, Algebra.commutes] }
  refine mem_of_gens S ?_ ?_ ?_ ?_ x y
  · refine modular_of_gen q lam _ (qz q (-2) • rA q) (fun y => ?_) ?_ ?_
    · rw [mul_smul_comm, smul_mul_assoc, monoRep_comm_rA q]
    · simp [modularAut, torusScaleAlgHom, monoRep, mA_e, rA_e, qz]
      rw [← Units.val_pow_eq_pow_val, inv_pow]
      rfl
    · refine zeroRead_comp_ext lam fun a b c => ?_
      simp only [monoRep, liftQuadruple_alpha, LinearMap.smul_apply, mA_e, rA_e]
      by_cases ha : a = -1
      · subst ha
        simp only [show ¬ (0 : ℤ) ≤ -1 by omega, if_false, map_add, map_smul, zeroRead_e,
          smul_eq_mul, show (-1 : ℤ) + 1 = 0 by norm_num, true_and, add_left_inj]
        split_ifs with hbc
        · subst hbc
          rw [show (-2 * (-1 : ℤ) - 1) = 1 by norm_num, hlam b, ← mul_assoc, qz_mul]
          ring_nf
        · simp
      · split_ifs <;> simp [show a + 1 ≠ 0 by omega]
  · refine modular_of_gen q lam _ rB (fun y => monoRep_comm_rB q y)
      ?_ ?_
    · simp [modularAut, torusScaleAlgHom, monoRep]
    · refine zeroRead_comp_ext lam fun a b c => ?_
      simp only [monoRep, liftQuadruple_beta, mB_e, rB_e, map_smul, zeroRead_e, smul_eq_mul]
      split_ifs with h
      · simp [h.1]
      · simp
  · refine modular_of_gen q lam _ rG
      (fun y => monoRep_comm_rG q y) ?_ ?_
    · simp [modularAut, torusScaleAlgHom, monoRep]
    · refine zeroRead_comp_ext lam fun a b c => ?_
      simp only [monoRep, liftQuadruple_gamma, mG_e, rG_e, map_smul, zeroRead_e, smul_eq_mul]
      split_ifs with h
      · simp [h.1]
      · simp
  · refine modular_of_gen q lam _ (qz q 2 • rD q) (fun y => ?_) ?_ ?_
    · rw [mul_smul_comm, smul_mul_assoc,
        monoRep_comm_rD q]
    · simp [modularAut, torusScaleAlgHom, monoRep, mD_e, rD_e, qz]
      rw [← Units.val_pow_eq_pow_val]
      rfl
    · refine zeroRead_comp_ext lam fun a b c => ?_
      simp only [monoRep, liftQuadruple_delta, LinearMap.smul_apply, mD_e, rD_e]
      by_cases ha : a = 1
      · subst ha
        simp only [show ¬ (1 : ℤ) ≤ 0 by omega, if_false, map_add, map_smul, zeroRead_e,
          smul_eq_mul, show (1 : ℤ) - 1 = 0 by norm_num, true_and, add_left_inj]
        split_ifs with hbc
        · subst hbc
          rw [show (1 - 2 * (1 : ℤ)) = -1 by norm_num, hlam b, ← mul_assoc, ← mul_assoc, qz_mul,
            qz_mul]
          ring_nf
          simp
        · simp
      · split_ifs <;> simp [show a - 1 ≠ 0 by omega]

end Modular

/-! ## The Haar moments over a field -/

section Haar

variable {K : Type*} [Field K] (q : Kˣ)

/-- `[k+1]_{q²} = 1 + q² + ⋯ + q^(2k)`. -/
def qSqNum (k : ℕ) : K := ∑ j ∈ Finset.range (k + 1), (q : K) ^ (2 * j)

theorem qSqNum_succ (k : ℕ) : qSqNum q (k + 1) = qSqNum q k + (q : K) ^ (2 * (k + 1)) := by
  rw [qSqNum, Finset.sum_range_succ]; rfl

theorem qSqNum_succ' (k : ℕ) : qSqNum q (k + 1) = 1 + (q : K) ^ 2 * qSqNum q k := by
  rw [qSqNum, Finset.sum_range_succ', qSqNum, Finset.mul_sum]
  simp only [mul_zero, pow_zero]
  rw [add_comm]
  congr 1
  refine Finset.sum_congr rfl fun j _ => ?_
  ring

/-- Woronowicz's Haar moments `h((βγ)^k) = (-q)^k / [k+1]_{q²}`. -/
noncomputable def haarMoment (k : ℕ) : K := (-(q : K)) ^ k / qSqNum q k

theorem qz_eq_zpow (z : ℤ) : qz q z = (q : K) ^ z := by
  simp [qz, Units.val_zpow_eq_zpow_val]

/-- If no `[k+1]_{q²}` vanishes (e.g. `q` is not a root of unity), the Haar moments satisfy
the modular recursion. -/
theorem haarMoment_modular (hq : ∀ k, qSqNum q k ≠ 0) : IsModularMoments q (haarMoment q) := by
  intro k
  have h1 := hq k
  have h2 := hq (k + 1)
  have hq0 : (q : K) ≠ 0 := q.ne_zero
  have ha := qSqNum_succ q k
  have hb := qSqNum_succ' q k
  simp only [haarMoment, qz_eq_zpow]
  rw [show (-2 - 2 * (k : ℤ)) = -((2 * (k + 1) : ℕ) : ℤ) by push_cast; ring, zpow_neg,
    zpow_natCast, zpow_one, zpow_neg, zpow_one]
  have e1 : (-(q : K)) ^ k / qSqNum q k + (q : K) * ((-(q : K)) ^ (k + 1) / qSqNum q (k + 1)) =
      (-(q : K)) ^ k / (qSqNum q k * qSqNum q (k + 1)) := by
    field_simp
    rw [hb]; ring
  have e2 : (-(q : K)) ^ k / qSqNum q k + (q : K)⁻¹ * ((-(q : K)) ^ (k + 1) / qSqNum q (k + 1)) =
      (-(q : K)) ^ k * (q : K) ^ (2 * (k + 1)) / (qSqNum q k * qSqNum q (k + 1)) := by
    field_simp
    rw [ha]; ring
  rw [e1, e2]
  have hp : (q : K) ^ (2 * (k + 1)) ≠ 0 := pow_ne_zero _ hq0
  field_simp

/-- The Haar functional on `O_q(SU(2))`, built algebraically. -/
noncomputable def haarState : OqSU2 K q →ₗ[K] K := zeroWeightFunctional q (haarMoment q)

theorem haarState_one : haarState q 1 = 1 := by
  simp [haarState, zeroWeightFunctional_one, haarMoment, qSqNum]

theorem haarState_beta_gamma : haarState q (β q * γ q) = -(q : K) / (1 + (q : K) ^ 2) := by
  simp [haarState, zeroWeightFunctional_beta_gamma, haarMoment, qSqNum, Finset.sum_range_succ]

/-- `haarState` is invariant under every torus automorphism. -/
theorem haarState_torus (u v : Kˣ) (x : OqSU2 K q) :
    haarState q (torusScaleAlgHom q u v x) = haarState q x :=
  zeroWeightFunctional_torus q _ u v x

/-- `haarState` is invariant under right translation by every diagonal character. -/
theorem haarState_rightTrans_diagChar (u : Kˣ) (x : OqSU2 K q) :
    haarState q (rightTrans q (diagCharAlgHom q u) x) = haarState q x :=
  zeroWeightFunctional_rightTrans_diagChar q _ u x

/-- `haarState` is invariant under left translation by every diagonal character. -/
theorem haarState_leftTrans_diagChar (u : Kˣ) (x : OqSU2 K q) :
    haarState q (leftTrans q (diagCharAlgHom q u) x) = haarState q x :=
  zeroWeightFunctional_leftTrans_diagChar q _ u x

/-- **Modular property of the Haar state**: `h(x y) = h(y σ(x))`, with
`σ = (α, β, γ, δ) ↦ (q⁻² α, β, γ, q² δ)`, whenever no `[k+1]_{q²}` vanishes. -/
theorem haarState_modular (hq : ∀ k, qSqNum q k ≠ 0) (x y : OqSU2 K q) :
    haarState q (x * y) = haarState q (y * modularAut q x) :=
  zeroWeightFunctional_modular q _ (haarMoment_modular q hq) x y

theorem modularAut_alpha : modularAut q (α q) = (q : K)⁻¹ ^ 2 • α q := by
  simp [modularAut, torusScaleAlgHom]

theorem modularAut_beta : modularAut q (β q) = β q := by
  simp [modularAut, torusScaleAlgHom]

theorem modularAut_gamma : modularAut q (γ q) = γ q := by
  simp [modularAut, torusScaleAlgHom]

theorem modularAut_delta : modularAut q (δ q) = (q : K) ^ 2 • δ q := by
  simp [modularAut, torusScaleAlgHom]

/-- Woronowicz's rank-one Haar relations hold for `haarState` when `1 + q² ≠ 0`. -/
theorem haarState_rankOne (hq : 1 + (q : K) ^ 2 ≠ 0) :
    (1 + (q : K) ^ 2) * haarState q (β q * γ q) = -(q : K) * haarState q 1 ∧
      (1 + (q : K) ^ 2) * haarState q (α q * δ q) = haarState q 1 ∧
      (1 + (q : K) ^ 2) * haarState q (δ q * α q) = (q : K) ^ 2 * haarState q 1 := by
  have hbg := haarState_beta_gamma q
  have h1 := haarState_one q
  have had : α q * δ q = 1 + (q : K) • (β q * γ q) := det_left' q
  have hda : δ q * α q = 1 + (((q⁻¹ : Kˣ) : K)) • (β q * γ q) := by
    rw [← rel_det_right q]; abel
  have hq0 : (q : K) ≠ 0 := q.ne_zero
  refine ⟨?_, ?_, ?_⟩
  · rw [hbg, h1]; field_simp
  · rw [had, map_add, map_smul, hbg, h1, smul_eq_mul]; field_simp; ring
  · rw [hda, map_add, map_smul, hbg, h1, smul_eq_mul, Units.val_inv_eq_inv_val]
    field_simp; ring

end Haar

end QOU.AlgebraicSubstrate.OqSU2
