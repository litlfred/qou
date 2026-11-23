import QOU.Braiding.JimboGl3Singlet
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Tactic.LinearCombination

/-!
# Colour singlets and the colour–flavour mirror (issue #9106 follow-up)

A strand carries colour `K³` and flavour `M`; the strand braid is the tensor braiding
`X = Ř_colour ⊗ B`, with `Ř` Jimbo's `U_q(gl₃)` braiding and `B` a flavour braid operator.
The *q-exterior* condition on a three-strand state is `X₁₂ w = −w` and `X₂₃ w = −w`.

This file proves the colour-singlet slice of quantum skew Howe duality at `n = 3`:
a state `ε_q ⊗ f` with colour part the colour singlet `ε_q` is q-exterior if and only if
its flavour part is totally q-symmetric, `B₁ f = q f` and `B₂ f = q f`
(`singlet_exterior_iff`). So colour column `(1³)` pairs with flavour row `(3)`: the
transpose of partitions that the coideal route sees as the Hecke involution `σ ↦ −σ⁻¹`.
A q-antisymmetric flavour part instead gives eigenvalue `q⁻²`, not `−1`
(`singlet_antisym_eigen`). No numerical input enters.

Flavour is an arbitrary `K`-module with two linear braid operators; colour states are
`M`-valued colour tensors `Fin 3 → Fin 3 → Fin 3 → M`.
-/

namespace QOU.Braiding.ColourFlavourMirror

open QOU.Braiding.JimboGl3Singlet

variable {K : Type*} [Field K] {M : Type*} [AddCommGroup M] [Module K M]

/-- Colour ⊗ flavour states on three strands. -/
abbrev St (M : Type*) := Fin 3 → Fin 3 → Fin 3 → M

/-- Jimbo's braiding on `M`-valued colour 2-tensors. -/
def RM (q : K) (v : Fin 3 → Fin 3 → M) : Fin 3 → Fin 3 → M := fun a b =>
  if a = b then q • v a a else v b a + (if b < a then (q - q⁻¹) • v a b else 0)

/-- Colour braiding on strands 1, 2. -/
def RM12 (q : K) (w : St M) : St M := fun a b c => RM q (fun x y => w x y c) a b

/-- Colour braiding on strands 2, 3. -/
def RM23 (q : K) (w : St M) : St M := fun a b c => RM q (fun x y => w a x y) b c

/-- Tensor strand braid `X₁₂ = Ř₁₂ ⊗ B₁`. -/
def X12 (q : K) (B : M →ₗ[K] M) (w : St M) : St M := fun a b c => B (RM12 q w a b c)

/-- Tensor strand braid `X₂₃ = Ř₂₃ ⊗ B₂`. -/
def X23 (q : K) (B : M →ₗ[K] M) (w : St M) : St M := fun a b c => B (RM23 q w a b c)

/-- Pure state `ε ⊗ f`. -/
def pure (e : T3 K) (f : M) : St M := fun a b c => e a b c • f

theorem RM12_pure (q : K) (e : T3 K) (f : M) : RM12 q (pure e f) = pure (R12 q e) f := by
  funext a b c
  simp only [RM12, RM, pure, R12, R]
  split_ifs <;> simp [add_smul, mul_smul]

theorem RM23_pure (q : K) (e : T3 K) (f : M) : RM23 q (pure e f) = pure (R23 q e) f := by
  funext a b c
  simp only [RM23, RM, pure, R23, R]
  split_ifs <;> simp [add_smul, mul_smul]

theorem eps_012 (q : K) : eps q 0 1 2 = 1 := by simp [eps]

/-- `ε ⊗ g = ε ⊗ h` forces `g = h` (read off the `(0,1,2)` component). -/
theorem pure_eps_inj (q : K) {g h : M} (H : pure (eps q) g = pure (eps q) h) : g = h := by
  have := congrFun (congrFun (congrFun H 0) 1) 2
  simpa [pure, eps_012] using this

theorem X12_singlet (q : K) (hq : q ≠ 0) (B : M →ₗ[K] M) (f : M) :
    X12 q B (pure (eps q) f) = pure (eps q) ((-q⁻¹) • B f) := by
  funext a b c
  simp only [X12, RM12_pure, R12_eps q hq, pure, map_smul, smul_smul]
  rw [mul_comm]

theorem X23_singlet (q : K) (hq : q ≠ 0) (B : M →ₗ[K] M) (f : M) :
    X23 q B (pure (eps q) f) = pure (eps q) ((-q⁻¹) • B f) := by
  funext a b c
  simp only [X23, RM23_pure, R23_eps q hq, pure, map_smul, smul_smul]
  rw [mul_comm]

/-- One generator: `X (ε ⊗ f) = −(ε ⊗ f)` iff `B f = q f`. -/
theorem neg_one_iff (q : K) (hq : q ≠ 0) (B : M →ₗ[K] M) (f : M) :
    pure (eps q) ((-q⁻¹) • B f) = pure (eps q) (-f) ↔ B f = q • f := by
  constructor
  · intro H
    have h1 := pure_eps_inj q H
    have h2 : q • ((-q⁻¹) • B f) = q • (-f) := by rw [h1]
    rw [smul_smul, smul_neg] at h2
    simp only [mul_neg, mul_inv_cancel₀ hq, neg_smul, one_smul, neg_inj] at h2
    exact h2
  · intro H
    rw [H, smul_smul]
    simp [inv_mul_cancel₀ hq]

/-- **Colour-singlet slice of quantum skew Howe duality.** The state `ε_q ⊗ f` is
q-exterior (`X₁₂ = X₂₃ = −1` on it) iff its flavour part is totally q-symmetric. -/
theorem singlet_exterior_iff (q : K) (hq : q ≠ 0) (B₁ B₂ : M →ₗ[K] M) (f : M) :
    (X12 q B₁ (pure (eps q) f) = -pure (eps q) f ∧ X23 q B₂ (pure (eps q) f) = -pure (eps q) f)
      ↔ (B₁ f = q • f ∧ B₂ f = q • f) := by
  have hneg : -pure (eps q) f = pure (eps q) (-f) := by
    funext a b c; simp [pure]
  rw [X12_singlet q hq, X23_singlet q hq, hneg, neg_one_iff q hq, neg_one_iff q hq]

/-- A q-antisymmetric flavour part (`B f = −q⁻¹ f`) gives the eigenvalue `q⁻²`. -/
theorem singlet_antisym_eigen (q : K) (hq : q ≠ 0) (B : M →ₗ[K] M) (f : M)
    (hf : B f = (-q⁻¹) • f) :
    X12 q B (pure (eps q) f) = pure (eps q) ((q⁻¹ ^ 2) • f) := by
  rw [X12_singlet q hq, hf, smul_smul]
  congr 2
  ring

/-- And `q⁻² ≠ −1` when `q² + 1 ≠ 0`, so such a state is not q-exterior. -/
theorem inv_sq_ne_neg_one (q : K) (hq : q ≠ 0) (h : q ^ 2 + 1 ≠ 0) : q⁻¹ ^ 2 ≠ -1 := by
  intro H
  apply h
  have : q ^ 2 * q⁻¹ ^ 2 = 1 := by rw [← mul_pow, mul_inv_cancel₀ hq, one_pow]
  rw [H] at this
  linear_combination -this

end QOU.Braiding.ColourFlavourMirror
