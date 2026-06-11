/-
  Status of the fibre functor τ at all orders of the h-expansion:
  order-mixing map or distinct invariants?

  Ref: [manuscript] §Mass Theory / Geom bridge status,
       conj:tau-all-orders-bridge
  Ref: [yekutieli2015] https://arxiv.org/abs/1007.1250
  Ref: [neumann-zagier1985] https://doi.org/10.1016/0040-9383(85)90004-7
-/

import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

namespace QOU.MassTheory

/-- Hypothesis (1) of `conj:tau-all-orders-bridge`, **naive form**,
    parameterised by the FIXED algebraic coefficient sequence `α` (the
    h^{2k}-curvature traces of the Q₈ crossed module along the Borromean
    braid) and the FIXED Markov-trace sequence `κ` (the h^{2k}
    coefficients of the Jones polynomial of the same braid). Index
    `k : ℕ` stands for the even order 2k.

    The fibre functor τ is realised by a lower-triangular linear map on
    the h-graded expansion taking `α` to `κ`. Both `α` and `κ` are class
    parameters — NOT universally quantified inside the bridge field —
    so the class is satisfiable for the specific categorical sequences
    (Gemini + Copilot review #1830: a single `tauCoeff` cannot satisfy
    the bridge for *all* sequences, e.g. α = 0, κ = 1).

    **CAVEAT (#1837 — trivially inhabited *for the probed dataset*).**
    The h⁶ empirical probe (`tau_all_orders_h6_empirical.py`) showed that
    at a fixed substrate `q₀` both `α` and `κ` are constant sequences,
    and `tauCoeff` has *independent free entries per row*, so every row
    `κ k = Σ_{j ≤ k} tauCoeff k j · α j` is a one-equation /
    `k`-unknowns underdetermined system solved on its own — *provided
    each such row has at least one nonzero `α j`, `j ≤ k`*, which holds
    for the Borromean sequences (`α₂ = -12`, `α₄ = -6` nonzero). Under
    that condition `Nonempty (TauOrderMixingMap α κ)` is trivially
    inhabited and does NOT capture the open question. (Copilot review
    #1858: for *arbitrary* fixed `α, κ` the class can be uninhabited —
    e.g. `α j = 0` for all `j ≤ k` but `κ k ≠ 0` makes row `k`
    unsatisfiable — so this is a statement about the specific
    categorical dataset, not all sequences.) The genuine refinement is
    `TauBandedKernelMap` below, which forces a SINGLE finite-support
    convolution kernel across all orders. -/
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

/-- Hypothesis (1) of `conj:tau-all-orders-bridge`, **refined
    (non-trivial) form** — the genuine open content per #1837.

    A fibre-functor realisation of τ does not supply an arbitrary
    lower-triangular `T` (which is vacuously available, see the caveat
    on `TauOrderMixingMap`); it supplies a SINGLE convolution operator
    with **finitely many** degrees of freedom — a kernel `f` of bounded
    support, with `T_{k,j} = f(k − j)`. The bridge then reads
    `κ = f ⋆ α` and must hold at EVERY order `k` with the *same* `f`,
    so a band of width `bandWidth + 1` real unknowns faces infinitely
    many equations. That is the over-determined, non-vacuous constraint:
    `Nonempty (TauBandedKernelMap α κ)` is a substantive claim about the
    categorical sequences, not an artefact of per-row freedom.

    (Structurally `f(0)` is the diagonal — `T_{k,k} = f(0)` — pinned at
    `h²` to `f(0) = κ₂/α₂ = -1/64`; the disproof in
    `phi0_normalization_disproof.py` shows no *constant* kernel
    `f = (f(0), 0, 0, …)` works past `h²`, so the open question is
    whether a *wider* finite band closes the bridge.) -/
class TauBandedKernelMap (α κ : ℕ → ℝ) where
  /-- The convolution kernel: `T_{k,j} = kernel (k − j)`. -/
  kernel : ℕ → ℝ
  /-- The band half-width: the kernel vanishes beyond `bandWidth`. -/
  bandWidth : ℕ
  /-- Finite support — the defining restriction that makes the map a
      single operator with finitely many parameters. -/
  finiteSupport : ∀ d : ℕ, d > bandWidth → kernel d = 0
  /-- The leading (diagonal) coefficient `T_{k,k} = kernel 0` is
      non-zero. -/
  leadingNonzero : kernel 0 ≠ 0
  /-- The bridge as a convolution with the SAME kernel at every order:
      `κ_k = Σ_{j ≤ k} kernel(k − j) · α_j`. -/
  bridge : ∀ k : ℕ,
      κ k = (Finset.range (k + 1)).sum (fun j => kernel (k - j) * α j)

/-- Hypothesis (2) of `conj:tau-all-orders-bridge`, parameterised by the
    same fixed sequences `α`, `κ`: no finite-support convolution kernel
    satisfies the bridge at all orders, so the algebraic and Markov-trace
    sides measure genuinely different categorical invariants of the
    Borromean braid that share only the h² value.

    Quantifier order (Gemini + Copilot review #1830): for the FIXED
    `α`, `κ`, every candidate finitely-supported kernel `f` fails the
    convolution bridge at some order `k`. Stated against the *banded*
    kernel (not an arbitrary lower-triangular `T`) so that it is the
    genuine negation of the refined hypothesis (1) — the arbitrary-`T`
    negation would be vacuously false (#1837). -/
class TauDistinctInvariants (α κ : ℕ → ℝ) where
  /-- For every finitely-supported kernel `f` (vanishing beyond some
      band `N`), the convolution bridge fails at some order `k`. -/
  noKernelAtAllOrders :
    ∀ (f : ℕ → ℝ) (N : ℕ),
      (∀ d : ℕ, d > N → f d = 0) →
      ∃ k : ℕ,
        κ k ≠ (Finset.range (k + 1)).sum (fun j => f (k - j) * α j)

/-- **Conjecture (τ at all orders — dichotomy, refined per #1837).**
    For the Borromean algebraic/Markov coefficient sequences `α`, `κ`,
    one of the two hypotheses holds: the fibre functor τ is a
    finite-support convolution kernel (`TauBandedKernelMap`), or no such
    kernel exists and the two sides measure distinct invariants
    (`TauDistinctInvariants`).

    This is the **non-trivial** form. The earlier
    `tau_order_mixing_naive_hyp1` below (arbitrary lower-triangular `T`)
    is excluded-middle-vacuous because hypothesis (1) is always
    inhabited there (#1837); the banded-kernel constraint is what makes
    the disjunction informative. Neither class currently has an instance
    for the categorical sequences — the honest reflection of the open
    status. -/
def tau_all_orders_bridge (α κ : ℕ → ℝ) : Prop :=
  Nonempty (TauBandedKernelMap α κ) ∨ Nonempty (TauDistinctInvariants α κ)

/-- The **naive hypothesis (1)** alone (retained for the record) — NOT a
    dichotomy/disjunction, just the existence of an arbitrary
    lower-triangular order-mixing map (Copilot review #1858: the body is
    `Nonempty (TauOrderMixingMap α κ)`, a single existence claim, so the
    name now reflects that). For the probed Borromean sequences this is
    trivially inhabited (#1837), which is precisely why it is superseded
    by the banded dichotomy `tau_all_orders_bridge`. -/
def tau_order_mixing_naive_hyp1 (α κ : ℕ → ℝ) : Prop :=
  Nonempty (TauOrderMixingMap α κ)

/-! ### Anchor at h²

The h² coefficient of T is fixed regardless of which hypothesis holds:
the algebraic side gives α_2 = -12 (proved categorically in
`prop:crossed-module-euler-characteristic`) and the Markov side gives
κ_2 = 3/16 (clean rational, from the Jones polynomial of the Borromean
braid (σ₁σ₂⁻¹)³ at t = q², skein parametrization h = q − q⁻¹). Their
ratio fixes the leading kernel coefficient
kernel 0 = T_{1,1} = κ_2 / α_2 = -1/64. The disproof in
`phi0_normalization_disproof.py` then shows that the *constant* kernel
(band width 0) fails at h⁴ (α_4/κ_4 = +7.92 ≠ -64). The conjecture is
whether a wider finite band closes the bridge.
-/

/-- The h² anchor value of the kernel's leading coefficient, fixed by
    the proved algebraic Euler characteristic and the Markov-trace h²
    coefficient. This number is determined regardless of which
    hypothesis holds. -/
noncomputable def tau_h2_anchor : ℝ := -(1 : ℝ) / 64

theorem tau_h2_anchor_eq : tau_h2_anchor = -(1 : ℝ) / 64 := rfl

end QOU.MassTheory
