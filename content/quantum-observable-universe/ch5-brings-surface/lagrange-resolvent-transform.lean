/-!
# QOU.BringsSurface.lagrange_resolvent_transform — DFT diagonalises C₅ on Bring's surface

The discrete Fourier transform w_k = (1/√5) Σ ζ^{kj} x_j converts the
three power-sum constraints of the Bring surface into spectral form,
and the cyclic permutation σ acts diagonally: σ(w_k) = ζ^{-k} w_k.
-/
import Mathlib.Data.Complex.Basic
import Mathlib.Data.Fin.Basic
import Mathlib.Algebra.BigOperators.Group.Finset
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases

namespace QOU.BringsSurface

-- Ref: [manuscript] Ch. 6, §1
-- Ref: [bring1786] https://doi.org/10.1007/BF02386200
noncomputable def ζ : ℂ := Complex.exp (2 * Real.pi * Complex.I / 5)

/-- The Lagrange resolvent (DFT) of coordinates on the Bring surface. -/
noncomputable def lagrangeResolvent (x : Fin 5 → ℂ) (k : Fin 5) : ℂ :=
  (1 / Complex.ofReal (Real.sqrt 5)) * ∑ j : Fin 5, ζ ^ (k.val * j.val) * x j

/-- The cyclic permutation σ: x_j ↦ x_{j+1 mod 5}. -/
def cyclicPerm (x : Fin 5 → ℂ) : Fin 5 → ℂ :=
  fun j => x ⟨(j.val + 1) % 5, Nat.mod_lt _ (by omega)⟩

/-- Part (1): w_0 = 0 from the constraint Σx_i = 0.
    At k=0, ζ^0 = 1, so w_0 = (1/√5) Σ x_j = 0. -/
-- Ref: [manuscript] Ch. 6, §1
theorem lagrange_resolvent_w0_vanishes
    (x : Fin 5 → ℂ)
    (h_sum : ∑ i, x i = 0) :
    lagrangeResolvent x ⟨0, by omega⟩ = 0 := by
  unfold lagrangeResolvent
  simp only [Fin.val_mk, Nat.zero_mul, pow_zero, one_mul]
  rw [h_sum, mul_zero]

/-- Part (2): The cyclic permutation acts diagonally on Lagrange resolvents.
    σ(w_k) = ζ^{-k} · w_k for all k.
    Proof requires the root-of-unity shift property ζ^{(k·(j+1))} = ζ^k · ζ^{(k·j)}. -/
-- Ref: [manuscript] Ch. 6, §1
-- Ref: [bring1786] https://doi.org/10.1007/BF02386200
theorem lagrange_resolvent_diagonal_action
    (x : Fin 5 → ℂ) :
    ∀ k : Fin 5, lagrangeResolvent (cyclicPerm x) k = ζ⁻¹ ^ k.val * lagrangeResolvent x k := by
  -- The key identity: Σ_j ζ^{k(j+1)} f(j) = ζ^k · Σ_j ζ^{kj} f(j)
  -- which follows from factoring out ζ^k from each summand.
  -- Ref: [manuscript] Ch. 6, §1
  sorry

end QOU.BringsSurface
