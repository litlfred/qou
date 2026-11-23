import Mathlib.Algebra.BigOperators.Group.Finset.Defs
import Mathlib.Data.Real.Basic
import Mathlib.Data.Fintype.Fin

/-!
# QOU.Shared.OperatorSelectionLP — shared context for LP-dual claims

An *LP-selection claim* is any proposition that bundles:
- A target `n_target ∈ ℝ_{>0}`
- A `d`-dimensional NF basis with Markov-trace coefficients `t_i`
- A `d × d` Frobenius Gram matrix `G_{ij}`
- The LP primal optimum `x* : Fin d → ℝ`
- The LP dual optima `(y_0*, y* : Fin d → ℝ)`

Per `local/lean-substantive-pass`, ~10 blocks share this shape
(operator-selection / confinement / shadow-price / strong-duality
content).  This typeclass extracts the shared structure so per-block
claims only need to specify which LP-property they encode (primal
feasibility / strong duality / active-set characterisation / etc.).

**Usage**:

```lean
class MyLPClaim extends QOU.Shared.OperatorSelectionLPContext where
  -- block-specific assertion
  claim_active_set_size :
    (Finset.filter (fun i => 0 < y_star i) Finset.univ).card = 3
```

-- Ref: [leitner2026] particle-interactions/operator-selection-lp.md (shared)
-/

namespace QOU.Shared

/-- Shared context for any block whose claim involves the
    operator-selection LP and its dual certificate. -/
class OperatorSelectionLPContext where
  /-- Strand number `n ≥ 2`. -/
  n : ℕ
  /-- Basis dimension `d` (usually `n!`). -/
  d : ℕ
  /-- The target net value `n_target ∈ ℝ_{>0}`. -/
  n_target : ℝ
  /-- The Markov-trace coefficient vector `t : Fin d → ℝ`. -/
  t : Fin d → ℝ
  /-- The Frobenius Gram matrix `G : Fin d → Fin d → ℝ`. -/
  G : Fin d → Fin d → ℝ
  /-- The primal optimum `x* : Fin d → ℝ`. -/
  x_star : Fin d → ℝ
  /-- The Markov-trace dual variable `y_0* : ℝ`. -/
  y_0_star : ℝ
  /-- The Frobenius-positivity dual variables `y* : Fin d → ℝ`. -/
  y_star : Fin d → ℝ
  /-- LP-active set: the indices `i` with strictly positive dual
      variable, `A* = {i : y*_i > 0}`. -/
  A_star : Finset (Fin d)
  /-- Strong-duality identity: `Σ t_i · x*_i = n_target · y_0*`.
      (Still an assumption, but not for the reason once given here: finite LP strong
      duality IS proved in-repo, unconditionally, as
      `QOU.Optimization.lp_strong_duality_uncond` (via Farkas from
      `QOU.Mathlib.isClosed_coneSpan`). It cannot discharge this field because the
      carrier records the objective values as free reals with no feasibility or
      optimality data; discharging it needs the carrier to carry `(A, a, c, x)` with
      `PrimalOptimal`. Bean `qou-9h4t`.) -/
  strong_duality :
    (Finset.univ.sum fun i : Fin d => t i * x_star i)
      = n_target * y_0_star

end QOU.Shared
