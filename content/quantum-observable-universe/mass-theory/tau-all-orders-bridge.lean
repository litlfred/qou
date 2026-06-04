/-
  Status of the fibre functor τ at all orders of the h-expansion:
  order-mixing map or distinct invariants?

  Ref: [manuscript] §Mass Theory / Geom bridge status,
       conj:tau-all-orders-bridge
  Ref: [yekutieli2015] https://arxiv.org/abs/1007.1250
  Ref: [neumann-zagier1985] https://doi.org/10.1016/0040-9383(85)90004-7
-/

import Mathlib.Data.Real.Basic
import Mathlib.LinearAlgebra.Matrix.Basic

namespace QOU.MassTheory

/-- Hypothesis (1) of `conj:tau-all-orders-bridge`: the fibre functor
    τ is realised by a lower-triangular linear map on the h-graded
    expansion, taking the algebraic h^k-coefficients α_k to the
    Markov-trace h^k-coefficients κ_k. The map is indexed by even
    orders 2k (we store its degree-doubled coefficients to keep
    indexing in ℕ).  -/
class TauOrderMixingMap where
  /-- T_{k,j} for j ≤ k, the (k,j)-entry of the order-mixing map. -/
  tauCoeff : ℕ → ℕ → ℝ
  /-- Lower triangular: zero above the diagonal. -/
  lowerTriangular : ∀ i j : ℕ, j > i → tauCoeff i j = 0
  /-- Diagonal entries are non-zero (T is invertible on each truncation). -/
  diagonalNonzero : ∀ i : ℕ, tauCoeff i i ≠ 0
  /-- The bridge: κ_{2k} = Σ_{j ≤ k} T_{k,j} · α_{2j} for every k.
      Stated as a class field rather than a theorem because the
      α_k and κ_k themselves depend on the categorical model. -/
  bridgeAtOrder : ∀ k : ℕ,
      ∀ (α κ : ℕ → ℝ),
        κ k = (Finset.range (k + 1)).sum (fun j => tauCoeff k j * α j)

/-- Hypothesis (2) of `conj:tau-all-orders-bridge`: no such
    order-mixing map exists at all orders, and the algebraic and
    Markov-trace sides measure genuinely different categorical
    invariants of the Borromean braid that share only the h²
    coincidence. -/
class TauDistinctInvariants where
  /-- For every candidate lower-triangular real map T, there is some
      order at which T fails the bridge equation. -/
  noMapAtAllOrders :
    ∀ (T : ℕ → ℕ → ℝ),
      (∀ i j : ℕ, j > i → T i j = 0) →
      ∃ k : ℕ, ∀ (α κ : ℕ → ℝ),
        κ k ≠ (Finset.range (k + 1)).sum (fun j => T k j * α j)

/-- **Conjecture (τ at all orders — dichotomy).**
    Exactly one of the two hypotheses holds: the fibre functor τ is
    an order-mixing linear map across all orders, or no such map
    exists and the two sides measure distinct invariants.

    Stated as a `Prop` whose proof would require resolving the
    open empirical computation; neither class currently has an
    instance, which is the honest reflection of the open status. -/
def tau_all_orders_bridge : Prop :=
  Nonempty TauOrderMixingMap ∨ Nonempty TauDistinctInvariants

/-! ### Anchor at h²

The h² coefficient of T is fixed regardless of which hypothesis
holds: the algebraic side gives α_2 = -12 (proved categorically in
`prop:crossed-module-euler-characteristic`) and the Markov side
gives κ_2 = 3/16 (clean rational, from the Jones polynomial of the
Borromean braid (σ₁σ₂⁻¹)³ evaluated at t = q², q = eʰ). Their
ratio fixes T_{1,1} = κ_2 / α_2 = -1/64. The disproof in
`phi0_normalization_disproof.py` then shows that *constant*
extension fails at h⁴ (α_4/κ_4 = +7.92 ≠ -64). The conjecture is
about what survives that disproof.
-/

/-- The h² anchor value of the order-mixing map, fixed by the
    proved algebraic Euler characteristic and the Markov-trace
    h² coefficient. This number is determined regardless of which
    hypothesis (1) or (2) holds. -/
noncomputable def tau_h2_anchor : ℝ := -(1 : ℝ) / 64

theorem tau_h2_anchor_eq : tau_h2_anchor = -(1 : ℝ) / 64 := rfl

end QOU.MassTheory
