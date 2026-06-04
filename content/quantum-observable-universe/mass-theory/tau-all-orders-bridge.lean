/-
  Status of the fibre functor τ at all orders of the h-expansion:
  order-mixing map or distinct invariants?

  Ref: [manuscript] §Mass Theory / Geom bridge status,
       conj:tau-all-orders-bridge
  Ref: [yekutieli2015] https://arxiv.org/abs/1007.1250
  Ref: [neumann-zagier1985] https://doi.org/10.1016/0040-9383(85)90004-7
-/

import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Basic

namespace QOU.MassTheory

/-- Hypothesis (1) of `conj:tau-all-orders-bridge`, parameterised by the
    FIXED algebraic coefficient sequence `α` (the h^{2k}-curvature traces
    of the Q₈ crossed module along the Borromean braid) and the FIXED
    Markov-trace sequence `κ` (the h^{2k} coefficients of the Jones
    polynomial of the same braid). Index `k : ℕ` stands for the even
    order 2k.

    The fibre functor τ is realised by a lower-triangular linear map on
    the h-graded expansion taking `α` to `κ`. Both `α` and `κ` are class
    parameters — NOT universally quantified inside the bridge field —
    so the class is satisfiable for the specific categorical sequences
    (Gemini + Copilot review #1830: a single `tauCoeff` cannot satisfy
    the bridge for *all* sequences, e.g. α = 0, κ = 1). -/
class TauOrderMixingMap (α κ : ℕ → ℝ) where
  /-- T_{k,j} for j ≤ k, the (k,j)-entry of the order-mixing map. -/
  tauCoeff : ℕ → ℕ → ℝ
  /-- Lower triangular: zero above the diagonal. -/
  lowerTriangular : ∀ i j : ℕ, j > i → tauCoeff i j = 0
  /-- Diagonal entries are non-zero (T is invertible on each truncation). -/
  diagonalNonzero : ∀ i : ℕ, tauCoeff i i ≠ 0
  /-- The bridge for the fixed sequences:
      κ_{2k} = Σ_{j ≤ k} T_{k,j} · α_{2j} for every k. -/
  bridgeAtOrder : ∀ k : ℕ,
      κ k = (Finset.range (k + 1)).sum (fun j => tauCoeff k j * α j)

/-- Hypothesis (2) of `conj:tau-all-orders-bridge`, parameterised by the
    same fixed sequences `α`, `κ`: no lower-triangular real map satisfies
    the bridge at all orders, so the algebraic and Markov-trace sides
    measure genuinely different categorical invariants of the Borromean
    braid that share only the h² value.

    Quantifier order (Gemini + Copilot review #1830): for the FIXED
    `α`, `κ`, every candidate lower-triangular map `T` fails at some
    order `k`. -/
class TauDistinctInvariants (α κ : ℕ → ℝ) where
  /-- For every candidate lower-triangular real map T, there is some
      order at which T fails the bridge equation for the fixed α, κ. -/
  noMapAtAllOrders :
    ∀ (T : ℕ → ℕ → ℝ),
      (∀ i j : ℕ, j > i → T i j = 0) →
      ∃ k : ℕ,
        κ k ≠ (Finset.range (k + 1)).sum (fun j => T k j * α j)

/-- **Conjecture (τ at all orders — dichotomy).**
    For the Borromean algebraic/Markov coefficient sequences `α`, `κ`,
    one of the two hypotheses holds: the fibre functor τ is an
    order-mixing linear map (`TauOrderMixingMap`), or no such map exists
    and the two sides measure distinct invariants (`TauDistinctInvariants`).

    Stated as a `Prop` parameterised by `α`, `κ` (Gemini review #1830:
    the proposition must accept the same parameters as the classes it
    instantiates). Neither class currently has an instance for the
    categorical sequences — the honest reflection of the open status.
    The two are mutually exclusive (an order-mixing map and a proof
    that none exists cannot coexist), so "one of" is also "exactly
    one". -/
def tau_all_orders_bridge (α κ : ℕ → ℝ) : Prop :=
  Nonempty (TauOrderMixingMap α κ) ∨ Nonempty (TauDistinctInvariants α κ)

/-! ### Anchor at h²

The h² coefficient of T is fixed regardless of which hypothesis holds:
the algebraic side gives α_2 = -12 (proved categorically in
`prop:crossed-module-euler-characteristic`) and the Markov side gives
κ_2 = 3/16 (clean rational, from the Jones polynomial of the Borromean
braid (σ₁σ₂⁻¹)³ evaluated at t = q², q = eʰ). Their ratio fixes
T_{1,1} = κ_2 / α_2 = -1/64. The disproof in
`phi0_normalization_disproof.py` then shows that *constant* extension
fails at h⁴ (α_4/κ_4 = +7.92 ≠ -64). The conjecture is about what
survives that disproof.
-/

/-- The h² anchor value of the order-mixing map, fixed by the proved
    algebraic Euler characteristic and the Markov-trace h² coefficient.
    This number is determined regardless of which hypothesis holds. -/
noncomputable def tau_h2_anchor : ℝ := -(1 : ℝ) / 64

theorem tau_h2_anchor_eq : tau_h2_anchor = -(1 : ℝ) / 64 := rfl

end QOU.MassTheory
