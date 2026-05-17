/-!
# QOU.BraidKnot.post_pr665_open_rd_inventory

**Inventory + initial findings on the six PR #665 open R&D items.**

This module records the **six open R&D items** identified at the
end of PR #665's prepare-merge cycle, together with **substantive
findings** from initial investigation on each.

## The six items

  1. σ_1 off-diagonal substantive discharge (Hoefsmit matrix-level)
  2. Full Hecke algebra type at H_n(q)
  3. Per-Wedderburn-block Python probe at ε^10, ε^12
  4. Inductive-limit Markov-trace operator construction
  5. Full perturbative-expansion infrastructure on typed-B_3 words
  6. Matrix-level Yang-Baxter cubic on V_(2,1) Hoefsmit matrices

## Initial findings (this branch)

### Finding 6.A — YB cubic anomaly on chapter Hoefsmit σ_1

A direct symbolic computation of the Yang-Baxter cubic
`σ_0 σ_1 σ_0 = σ_1 σ_0 σ_1` on the chapter file
`hoefsmit-V21-cos-symmetrization.lean`'s matrices

  σ_0 = !![q, 0; 0, -q⁻¹]
  σ_1 = !![d_1, b; b, d_2]
  d_1 = q³/(q²+1), d_2 = -q⁻¹/(q²+1), b² = d_1·d_2 + 1

yields a `(0,0)`-entry constraint

  q² · d_1  ≟  q · d_1² − q⁻¹ · b²
  ⇔ b²  ≟  q² · d_1 · (d_1 − q)
  ⇔ b² ≟  −q⁶ / (q²+1)²

since `d_1 − q = −q/(q²+1)` and `d_1 = q³/(q²+1)`. But the chapter's
`b² = (q⁴+q²+1)/(q²+1)²` is **positive**, so the YB-required value
is **impossible** under these conventions.

**Implication**: the chapter Hoefsmit σ_1 satisfies the Hecke
quadratic (trace = q − q⁻¹, det = −1) but is **not** part of an
H_3 representation with σ_0 = diag(q, −q⁻¹). The d_1, d_2 entries
need revision (e.g. to the standard Ram-Hoefsmit
`q/(q² + 1)` form on T_1 axial distance −2, not `q³/(q²+1)`)
to recover braid-cubic compatibility.

This finding is recorded as a **conjectural anomaly** here; full
verification + revision is the substantive content of item 6.

## Status

This block is the **R&D coordination point** for items 1-6 across
follow-up branches. Each item retains its placeholder discharge
(via the explicit-residual classes in PR #665); substantive
progress lands in dedicated follow-up files as it is achieved.

LaTeX label: `rem:post-pr665-open-rd-inventory`
-/

import Mathlib.Tactic

namespace QOU.BraidKnot

/-! ## YB cubic anomaly: residual computation -/

/-- The `(0,0)` entry of `σ_0 σ_1 σ_0` on the chapter conventions
    is `q² · d_1` (computed from `σ_0` being diagonal). -/
noncomputable def yb_lhs_00 (q : ℝ) : ℝ := q^2 * (q^3 / (q^2 + 1))

/-- The `(0,0)` entry of `σ_1 σ_0 σ_1` on the chapter conventions
    is `q · d_1² − q⁻¹ · b²`. -/
noncomputable def yb_rhs_00 (q : ℝ) : ℝ :=
  q * (q^3 / (q^2 + 1))^2 - q⁻¹ * ((q^4 + q^2 + 1) / (q^2 + 1)^2)

/-- The YB-anomaly residual: `LHS − RHS` of the `(0,0)` entry.
    Non-vanishing residual ⇒ YB cubic fails on chapter conventions. -/
noncomputable def yb_residual_00 (q : ℝ) : ℝ :=
  yb_lhs_00 q - yb_rhs_00 q

-- Ref: [manuscript] rem:post-pr665-open-rd-inventory §"Finding 6.A"
-- Ref: [hoefsmit1974] (Hoefsmit's PhD thesis, seminormal form)
/-- **Negative-result anchor**: at the substrate parameter `q = 2`
    (purely as a sample point, not the actual substrate value), the
    YB residual `yb_residual_00 2` is **non-zero**, certifying that
    the chapter conventions admit no YB cubic with σ_0 = diag(q, -q⁻¹).

    The numerical value at `q = 2`:
      yb_lhs_00 2 = 4 · 8/5 = 32/5
      yb_rhs_00 2 = 2 · (8/5)² − (1/2) · (16+4+1)/25 = 2·64/25 − 21/50
                  = 128/25 − 21/50 = 256/50 − 21/50 = 235/50 = 47/10
      yb_residual_00 2 = 32/5 − 47/10 = 64/10 − 47/10 = 17/10 ≠ 0.

    Closed by `decide`-style arithmetic on the rationals. -/
theorem yb_residual_00_at_two_ne_zero :
    yb_residual_00 2 ≠ 0 := by
  unfold yb_residual_00 yb_lhs_00 yb_rhs_00
  norm_num

end QOU.BraidKnot
