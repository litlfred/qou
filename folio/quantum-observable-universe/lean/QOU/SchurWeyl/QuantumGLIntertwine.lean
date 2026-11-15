/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.JimboGL
import QOU.SchurWeyl.QuantumGLAction

/-!
# The Hecke image lies in the `U_q(gl_d)` commutant

G3.1 (bean `qou-gl31`), the inclusion half of `gl_d` Schur–Weyl:

`ρ(H_{m+1}(q)) ⊆ End_{U'}((K^d)^{⊗(m+1)})`, `U' = ⟨K_c, E_i, F_i⟩`,

where `E_i = raiseOp`, `F_i = lowerOp` are the iterated coproducts with tail weight `κ_i`, and
`K_c = cartan c` is any product-weight diagonal (the Cartan torus).  Every `ρ(x)` commutes with each
of them (`jimbo_commute_raise`, `jimbo_commute_lower`, `jimbo_commute_cartan`).

The reverse inclusion — the image is the WHOLE commutant — is G3.4 (bean `qou-gl34`), open.

## Base ring (§7c)

Any field (the Jimbo action is stated over a field with `qi = q⁻¹`); the operator identities
themselves (`QuantumGLAction`) hold over any commutative ring with `q · qi = 1`.

-- Ref: [jimbo1986] M. Jimbo, Lett. Math. Phys. 11 (1986) 247–252.
-/

namespace QOU.SchurWeyl.QuantumGL

open QOU.IwahoriHecke.TensorEmbedGL QOU.SchurWeyl.JimboGL

variable {K : Type*} [Field K] {d : ℕ}

theorem jimbo_commute_of (q : K) (hq : q ≠ 0) (m : ℕ)
    (Y : Matrix (Fin (m + 1) → Fin d) (Fin (m + 1) → Fin d) K)
    (hY : ∀ a : Fin m, strandBraid q q⁻¹ a * Y = Y * strandBraid q q⁻¹ a)
    (x : Hecke K q q⁻¹ m) : jimbo d q hq m x * Y = Y * jimbo d q hq m x := by
  have := jimbo_mem q hq m (Subalgebra.centralizer K {Y})
    (fun a => by
      rw [Subalgebra.mem_centralizer_iff]
      rintro g rfl
      exact (hY a).symm) x
  rw [Subalgebra.mem_centralizer_iff] at this
  exact (this Y rfl).symm

/-- **Every `ρ(x)` commutes with `Δ⁽ⁿ⁾(E_i)`.** -/
theorem jimbo_commute_raise (q : K) (hq : q ≠ 0) (m : ℕ) {i j : Fin d}
    (hij : (j : ℕ) = i + 1) (x : Hecke K q q⁻¹ m) :
    jimbo d q hq m x * raiseOp q q⁻¹ i j = raiseOp q q⁻¹ i j * jimbo d q hq m x :=
  jimbo_commute_of q hq m _ (fun a => strandBraid_commute_raise (mul_inv_cancel₀ hq) a hij) x

/-- **Every `ρ(x)` commutes with `Δ⁽ⁿ⁾(F_i)`.** -/
theorem jimbo_commute_lower (q : K) (hq : q ≠ 0) (m : ℕ) {i j : Fin d}
    (hij : (j : ℕ) = i + 1) (x : Hecke K q q⁻¹ m) :
    jimbo d q hq m x * lowerOp q q⁻¹ i j = lowerOp q q⁻¹ i j * jimbo d q hq m x :=
  jimbo_commute_of q hq m _ (fun a => strandBraid_commute_lower (mul_inv_cancel₀ hq) a hij) x

/-- **Every `ρ(x)` commutes with every Cartan element.** -/
theorem jimbo_commute_cartan (q : K) (hq : q ≠ 0) (m : ℕ) (c : Fin d → K)
    (x : Hecke K q q⁻¹ m) :
    jimbo d q hq m x * cartan c = cartan c * jimbo d q hq m x :=
  jimbo_commute_of q hq m _ (fun a => strandBraid_commute_cartan a c) x

end QOU.SchurWeyl.QuantumGL
