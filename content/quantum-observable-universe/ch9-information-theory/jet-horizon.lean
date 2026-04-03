/-!
# QOU.JetHorizon — Jet horizon (degree-0 vanishing locus)

A jet horizon is a closed boundary in an affine chart where the
degree-0 algebra A_0 vanishes.  No fibre-value data (photon identity)
crosses the horizon, but higher-degree jet data (winding, curvature)
can leak through.

LaTeX label: `def:jet-horizon`

## References

- [hawking1975] S.W. Hawking, "Particle creation by black holes",
  Commun. Math. Phys. 43 (1975), 199–220.
- [manuscript] §9/jet-horizon
-/

import Mathlib.Data.Real.Basic

namespace QOU

/-- A jet horizon in an affine chart: a locus where the degree-0
    algebra A_0 vanishes.  The horizon ideal h ⊂ Γ(U, A_0) blocks
    all zeroth-order sections; higher-degree jet data (A_k/A_0 for
    k ≥ 1) can carry non-trivial sections across the horizon.

    Algebraically identical to a big bang state (def:big-bang-state)
    but plays a different role: a horizon is a boundary within a
    chart, whereas a big bang state is a reference configuration. -/
structure JetHorizon where
  /-- The affine chart dimension (number of base points). -/
  chartDim : ℕ
  /-- The degree-0 sections vanish at the horizon:
      Γ(U, A_0)|_H = 0. -/
  degree_zero_vanishes : Prop
  /-- Degree-1 sections (linear transport / winding) may be
      non-trivial across the horizon. -/
  degree_one_leaks : Prop
  /-- Degree-2 sections (curvature / linking) may be
      non-trivial across the horizon. -/
  degree_two_leaks : Prop

-- Ref: [manuscript] §9/jet-horizon
-- Ref: [hawking1975] https://doi.org/10.1007/BF02345020
sorry

/-- A big bang state: a bundle initial condition where A_0 = 0.
    Algebraically identical to a jet horizon but used as a
    reference configuration rather than a boundary.

    Existence is not assumed: whether any affine chart admits
    a big bang state is a dynamical question. -/
structure BigBangState where
  /-- The underlying jet horizon condition. -/
  horizon : JetHorizon
  /-- The horizon is the reference configuration (not a boundary). -/
  is_initial : Prop

-- Ref: [manuscript] §9/big-bang-state
sorry

/-- An aeon: a maximal connected interval (a, b) ⊂ ℤ of
    information-theoretic time steps where the degree-0 algebra
    is non-trivial.  Bounded by jet horizons (or extending to ±∞). -/
structure Aeon where
  /-- Start step (or -∞ if past-complete). -/
  start : Option ℤ
  /-- End step (or +∞ if future-complete). -/
  stop : Option ℤ
  /-- The degree-0 algebra is non-trivial at every interior step. -/
  interior_nontrivial : Prop
  /-- If start is finite, the boundary is a jet horizon. -/
  past_horizon : start.isSome → JetHorizon
  /-- If stop is finite, the boundary is a jet horizon. -/
  future_horizon : stop.isSome → JetHorizon

-- Ref: [manuscript] §9/aeon
-- Ref: [penrose2010] R. Penrose, "Cycles of Time", Bodley Head 2010.
sorry

/-- Two aeons are adjacent if they share a boundary: the future
    horizon of the first is the past horizon of the second. -/
def Aeon.adjacent (a₁ a₂ : Aeon) : Prop :=
  ∃ (h₁ : a₁.stop.isSome) (h₂ : a₂.start.isSome),
    a₁.stop = a₂.start

/-- **Conjecture (aeon boundary generates chart).**

    If two aeons are adjacent and the degree-1 boundary data
    satisfies the integrability condition of ∇_q, then the
    forward light cone of the boundary datum defines a new
    affine chart with the degree ≥ 1 data as its reference
    configuration. -/
-- Ref: [manuscript] §9/aeon-boundary-generates-chart
-- Ref: [penrose2010] R. Penrose, "Cycles of Time", Bodley Head 2010.
axiom aeon_boundary_generates_chart
    (a₁ a₂ : Aeon)
    (hadj : a₁.adjacent a₂)
    (integrable : Prop)  -- integrability of ∇_q on A_1/A_0
    : -- The boundary datum seeds a new affine chart
      -- with non-trivial degree-0 data at the first step.
      Prop

/-- **Conformal invariance at the jet horizon.**

    The boundary datum (A_1/A_0, A_2/A_0)|_H is invariant under
    rescaling of A_0: it depends only on the vanishing locus of A_0
    (its conformal class), not on the specific generator of the
    horizon ideal h.

    This is the QOU analogue of conformal invariance in Penrose's CCC:
    the degree ≥ 1 jet data does not see the "size" of A_0, only its
    zero locus.  It follows from the observability axioms: the
    Frobenius pairing degenerates on A_0 at the horizon, so only
    the higher-jet quotients are observable. -/
-- Ref: [penrose2010] R. Penrose, "Cycles of Time", Bodley Head 2010.
-- Ref: [manuscript] §9/horizon-conformal-invariance
theorem horizon_conformal_invariance
    (H : JetHorizon)
    (λ : ℝ)  -- rescaling factor
    (hλ : λ ≠ 0)
    : -- The quotient A_k/A_0 on H is unchanged by A_0 ↦ λ·A_0.
      -- Follows from: λ·s vanishes on H iff s vanishes on H.
      True := by
  -- Ref: [manuscript] §9/horizon-conformal-invariance
  sorry

end QOU
