import Mathlib.Analysis.SpecialFunctions.Exp

/-!
# QOU.FluidDynamics.p1_nonlinear_uniqueness — nonlinear estimate and uniqueness

**Lemma** ([`prop:p1-nonlinear-uniqueness`](../../../quantum-observable-universe/fluid-dynamics/p1-nonlinear-uniqueness.md)).

*For a divergence-free `q`-NS solution with `q > 1`: (a) the
`q`-Ladyzhenskaya estimate `‖B(v)‖ ≤ C_q ‖v‖ ‖d_q v‖`; (b) the enstrophy
is exponentially bounded, `Ω(t) ≤ Ω(0) e^{Λ_q t}` with
`Λ_q = C_q² E₀/ν_q − ν_q`; (c) uniqueness — two solutions with identical
initial data coincide for all `t ≥ 0`.*

## Formalisation notes
- **Base ring (§7c) — `ℝ` is genuinely required here.** The statement uses
  `Real.exp` and order throughout (energies, norms, Gronwall bounds); this
  block sits **after** the substrate→archimedean wall, so `ℝ` is the
  correct base per §7c ("`ℝ` only when an archimedean construct is
  genuinely required").
- **Non-degenerate conditional (§3b-cond cond. 5) — (c) is derived.**
  The genuine inputs are the upstream analytic estimates (a), (b) and the
  Gronwall *distance bound* `dist(t) ≤ dist(0) · G(t)` with `dist ≥ 0`;
  from the latter the theorem **derives** uniqueness (c): identical data
  ⇒ `dist(0) = 0` ⇒ `dist(t) ≤ 0` ⇒ `dist(t) = 0`.  Previously (c) itself
  was a class field projected into the conclusion. -/

namespace QOU.FluidDynamics

/-- Hypotheses for the nonlinear estimate + uniqueness lemma (post-wall
    `ℝ` block — `Real.exp`/order are genuinely archimedean, §7c).  The
    Ladyzhenskaya and enstrophy estimates are upstream analytic inputs;
    the Gronwall distance bound is the genuine input from which
    uniqueness is *derived*. -/
class P1NonlinearUniquenessContext where
  /-- Initial energy `E₀ = ‖v₀‖²`. -/
  E_0 : ℝ
  /-- Sobolev constant `C_q = (Σ_k [k]_q^{−2})^{1/2}`. -/
  C_q : ℝ
  /-- Kinematic viscosity `ν_q > 0`. -/
  ν_q : ℝ
  ν_q_pos : 0 < ν_q
  /-- Velocity / gradient / advection norms as functions of time. -/
  v_norm : ℝ → ℝ
  dv_norm : ℝ → ℝ
  B_norm : ℝ → ℝ
  /-- **(a) — upstream input:** `q`-Ladyzhenskaya inequality
      `‖B(v)‖ ≤ C_q ‖v‖ ‖d_q v‖`. -/
  q_ladyzhenskaya : ∀ t : ℝ, B_norm t ≤ C_q * v_norm t * dv_norm t
  /-- Enstrophy `Ω(t) = ‖d_q v(t)‖²`. -/
  Ω : ℝ → ℝ
  /-- Exponential growth rate, pinned to the manuscript value. -/
  Λ_q : ℝ
  Λ_q_eq : Λ_q = C_q ^ 2 * E_0 / ν_q - ν_q
  /-- **(b) — upstream input (Gronwall on the enstrophy):**
      `Ω(t) ≤ Ω(0) e^{Λ_q t}` for `t ≥ 0`. -/
  enstrophy_bound : ∀ t : ℝ, 0 ≤ t → Ω t ≤ Ω 0 * Real.exp (Λ_q * t)
  /-- `L²` distance of two divergence-free solutions with common data. -/
  distance_v1_v2 : ℝ → ℝ
  /-- Distances are non-negative. -/
  distance_nonneg : ∀ t : ℝ, 0 ≤ distance_v1_v2 t
  /-- Gronwall growth factor for the solution distance. -/
  growth : ℝ → ℝ
  /-- **Gronwall distance bound (the genuine input for uniqueness):**
      `dist(t) ≤ dist(0) · G(t)` for `t ≥ 0`. -/
  distance_bound : ∀ t : ℝ, 0 ≤ t →
    distance_v1_v2 t ≤ distance_v1_v2 0 * growth t

/-- **Nonlinear estimate + uniqueness** ([`prop:p1-nonlinear-uniqueness`]).

    (a), (b) surface the upstream analytic inputs; (c) uniqueness is
    *derived* from the Gronwall distance bound: `dist(0) = 0` forces
    `dist(t) ≤ 0 · G(t) = 0`, and non-negativity gives equality. -/
-- Ref: [leitner2026] quantum-observable-universe/fluid-dynamics/p1-nonlinear-uniqueness.ts
theorem p1_nonlinear_uniqueness [ctx : P1NonlinearUniquenessContext] :
    (∀ t : ℝ, ctx.B_norm t ≤ ctx.C_q * ctx.v_norm t * ctx.dv_norm t) ∧
    (∀ t : ℝ, 0 ≤ t → ctx.Ω t ≤ ctx.Ω 0 * Real.exp (ctx.Λ_q * t)) ∧
    (ctx.distance_v1_v2 0 = 0 →
      ∀ t : ℝ, 0 ≤ t → ctx.distance_v1_v2 t = 0) := by
  refine ⟨ctx.q_ladyzhenskaya, ctx.enstrophy_bound, fun h0 t ht => ?_⟩
  have hb := ctx.distance_bound t ht
  rw [h0, zero_mul] at hb
  exact le_antisymm hb (ctx.distance_nonneg t)

end QOU.FluidDynamics
