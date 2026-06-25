import QOU.QBeta.ReebTowerJacobiAnger

/-!
# QOU.Mass.BindingJacobiAngerBridge — the Layer-1 ↔ Layer-2 bridge

Sibling PR #2795 left two recurrence layers for the binding prolongation `a_D^(n)`:
**Layer 1** (`BindingHyperbolicRecurrence`) the hyperbolic cosh/sinh tower (depth-2 SL₂, `n ≤ 4`
fit), and **Layer 2** (`BindingQBesselKernel`) the super-exponential q-Bessel tower. This file
records the **bridge** between them — the elementary Jacobi–Anger structure already formalised in
`QOU.QBeta.ReebTowerJacobiAnger` — and the binding-specific payoff it implies: a **confinement
criterion**.

## One operator, two conics (Jacobi–Anger)

Both towers solve the *same* three-term operator `p_{k+1} = 2t·p_k − p_{k−1}`
(`reeb_tower_cosh_step`, `reeb_rotation_sin_three_term`), with the multiplier `t` selecting the
branch:

| `t` | regime | tower | conic | Bessel |
|---|---|---|---|---|
| `t = cosh η ≥ 1` (`reeb_growth_one_le_cosh`) | **growth** | binding Layer-1 `cosh/sinh(nθ)` | hyperbola `cosh²−sinh²=1` | `I_ν` |
| `t = cos θ`, `|t| ≤ 1` (`reeb_rotation_abs_cos_le_one`) | **rotation** | `sin(nθ)` | circle `cos²+sin²=1` | `J_ν` |

These are the two faces of `I_ν(x) = i^{−ν} J_ν(i x)` — the Jacobi–Anger shadow
(`reeb_growth_hyperbola` vs `reeb_rotation_circle`). Layer 2 (the q-Bessel kernel,
`BindingQBesselKernel`) is the **q-deformation** of the radial `J_ν` side; the binding multiplier
`t = τ/2 = cosh θ_binding ≥ 1` puts binding on the **growth / `I_ν`** branch — which is exactly
why the binding tower *grows* (super-exp at the q-Bessel level, exp at the SL₂ level) rather than
oscillating.

## Confinement criterion (the binding payoff)

The binding transfer kernel `R(q,x) = x² − τx + 1` (`BindingHyperbolicRecurrence`) has **real,
reciprocal** roots — a *confined* (bound) hyperbolic `SL₂(ℝ)` state — iff its discriminant
`τ² − 4 ≥ 0`, i.e. `|τ| ≥ 2`. With `τ = 2 cosh θ` (`binding_trace_two_cosh`) this holds
identically, with discriminant `4 sinh²θ`: the cosh-form of `τ` *guarantees* confinement (the
opposite, `|τ| < 2`, is the elliptic / `J_ν`-rotation / scattering regime).

Ground ring `ℝ` (archimedean hyperbolic functions), §7c.
-/

namespace QOU.Mass.BindingJacobiAngerBridge

open Real QOU.QBeta

/-- **Binding trace lies in the `|τ| ≥ 2` confined regime.** `τ = 2 cosh θ ≥ 2`, since
`1 ≤ cosh θ` (`reeb_growth_one_le_cosh`). The depth-2 binding transfer is therefore always
hyperbolic `SL₂(ℝ)` (a real binding angle `θ` exists), never elliptic. -/
theorem binding_trace_ge_two (θ : ℝ) : 2 ≤ 2 * cosh θ := by
  have h := reeb_growth_one_le_cosh θ
  linarith

/-- **The binding transfer discriminant is `4 sinh²θ`.** For `τ = 2 cosh θ`,
`τ² − 4 = 4 cosh²θ − 4 = 4 sinh²θ` (via the growth hyperbola `cosh²θ − sinh²θ = 1`,
`reeb_growth_hyperbola`). The discriminant of `R(q,x) = x² − τx + 1`. -/
theorem binding_discriminant_eq_four_sinh_sq (θ : ℝ) :
    (2 * cosh θ) ^ 2 - 4 = 4 * sinh θ ^ 2 := by
  linear_combination 4 * reeb_growth_hyperbola θ

/-- **Confinement: the binding discriminant is non-negative.** `τ² − 4 = 4 sinh²θ ≥ 0`, so the
binding kernel `x² − τx + 1` has real reciprocal roots `e^{±θ}` — a confined hyperbolic bound
state — for every real binding angle `θ`. This is the structural reason the cosh-form of `τ`
(built from the bar-even gap `[2]_q`, `NaStokesKeystone`) describes a *bound* nucleus. -/
theorem binding_discriminant_nonneg (θ : ℝ) : 0 ≤ (2 * cosh θ) ^ 2 - 4 := by
  rw [binding_discriminant_eq_four_sinh_sq]
  positivity

/-- **The binding growth tower lives on the `I_ν` hyperbola** (not the `J_ν` circle):
`cosh²θ − sinh²θ = 1`. The binding-context restatement of `reeb_growth_hyperbola`; together with
`binding_discriminant_nonneg` it places binding firmly on the growth side of the Jacobi–Anger
bridge `I_ν(x) = i^{−ν} J_ν(i x)`, whose q-deformation is the Layer-2 q-Bessel kernel. -/
theorem binding_on_growth_hyperbola (θ : ℝ) : cosh θ ^ 2 - sinh θ ^ 2 = 1 :=
  reeb_growth_hyperbola θ

end QOU.Mass.BindingJacobiAngerBridge
