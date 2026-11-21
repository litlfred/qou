import Mathlib.Analysis.SpecificLimits.Basic
import QOU.Shared.ArchimedeanEval

/-!
# QOU.Observations.brane_tower_q_laplacian_decay

**Proposition** ([`prop:brane-tower-q-laplacian-decay`](../../../quantum-observable-universe/observations/brane-tower-q-laplacian-decay.md)).

Dropping the locality assumption for composite physical observables
requires summing over the brane tower — an infinite jet prolongation
`T(ρ) = ∑_{n ≥ 1} ℏ_q^{2n} Δ⁽ⁿ⁾(ρ)`, where `Δ⁽ⁿ⁾` is the `n`-th iterated
q-Laplacian on the Reeb bundle. The remainder past the single-jet term
decays geometrically with ratio `q⁻² < 1` for `q > 1`.

## Disposition (derived, not projected)

The previous encoding **postulated** the boxed closed-form bound
`|T(ρ) − ℏ_q²Δ⁽¹⁾(ρ)| ≤ ℏ_q⁴‖ρ‖·q⁻²/(1 − q⁻²)` directly as a class field
`remainder_bound`; the "theorem" just rewrote it via `ratio_eq` and
re-emitted it (pure self-assuming projection).

Here the class carries the genuine **inputs** the physics supplies:

  * `0 ≤ r`, `r < 1` — the geometric ratio `r = q⁻²` is `< 1` in the
    regime `q > 1` (the exponential q-Laplacian mode damping);
  * `remainder_le_geom` — the tail `T(ρ) − ℏ_q²Δ⁽¹⁾(ρ)` is dominated,
    **level by level**, by the geometric majorant `∑' k, ℏ_q⁴‖ρ‖·r^{k+1}`
    (the `.md`'s displayed geometric-series line: each iterated Laplacian
    `Δ⁽ⁿ⁾` on a fixed mode contributes `≲ ℏ_q⁴‖ρ‖·r^{k+1}`).

The theorem then **derives** the manuscript's closed form by actually
*summing the geometric series* — `∑' k, M·r^{k+1} = M·r/(1 − r)`
(Mathlib `tsum_geometric_of_lt_one`), the exact `=` step of the `.md`'s
"Geometric-series tail" paragraph. The closed form is a *consequence*,
not a hypothesis.

## Cross-references

  - [folio/quantum-observable-universe/observations/brane-tower-q-laplacian-decay.md]
-/

namespace QOU.Observations

/-- Dual-feasibility / decay **inputs** for the brane-tower bound. Every
    field is a genuine hypothesis supplied by the q-Laplacian spectrum;
    the manuscript's closed-form remainder bound is **derived** in
    `brane_tower_q_laplacian_decay`, not carried here.

    Extends `QOU.Shared.ArchimedeanEval` (beans `qou-mt7r`, `qreal`) so
    `q_real := eval q` is derived from the inherited substrate parameter
    `q : R` via the assumed evaluation `eval : R →+* ℝ` rather than posited
    as an unrelated free real field. -/
class BraneTowerQLaplacianDecayContext extends QOU.Shared.ArchimedeanEval where
  /-- Substrate q-Planck constant `ℏ_q = (q − 1)/q`. -/
  hbar_q : ℝ
  /-- L² norm of the Reeb-bundle density `ρ`. -/
  rho_L2 : ℝ
  /-- The brane-tower sum `T(ρ) = ∑_{n ≥ 1} ℏ_q^{2n} Δ⁽ⁿ⁾(ρ)`. -/
  T_rho : ℝ
  /-- The single-jet (n = 1) local Laplacian contribution `Δ⁽¹⁾(ρ)`. -/
  delta1_rho : ℝ
  /-- The geometric ratio of the tail decay, `r = q⁻²`. -/
  r : ℝ
  /-- The ratio is the substrate `q⁻²` (`q_real := toArchimedeanEval.q_real`). -/
  ratio_eq : r = toArchimedeanEval.q_real ^ (-2 : ℤ)
  /-- Positivity: `0 ≤ r`. -/
  r_nonneg : 0 ≤ r
  /-- Contraction: `r < 1` (i.e. `q > 1`). -/
  r_lt_one : r < 1
  /-- **Termwise exponential-decay input.** The tail past the single-jet
      term is majorised, level by level, by the geometric series with
      coefficient `M = ℏ_q⁴‖ρ‖` — the `.md`'s displayed
      `∑ ℏ_q^{2n}·q^{-2(n-1)}` bound. This is the genuine physical
      hypothesis (bounded iterated-Laplacian modes), NOT the closed
      form. -/
  remainder_le_geom :
    |T_rho - hbar_q ^ 2 * delta1_rho|
      ≤ ∑' k : ℕ, (hbar_q ^ 4 * rho_L2) * r ^ (k + 1)

/-- **Brane-tower convergence via q-Laplacian decay** ([`prop:brane-tower-q-laplacian-decay`]).

    For `q > 1` the remainder of the brane tower past the local
    single-jet term is bounded by the manuscript's closed form
    `ℏ_q⁴‖ρ‖·q⁻²/(1 − q⁻²)`.

    **Derived**: the geometric majorant `∑' k, M·r^{k+1}` supplied by the
    termwise-decay input is *summed* here to its closed form
    `M·r/(1 − r)` via `tsum_geometric_of_lt_one` — the actual `=` step of
    the manuscript's geometric-series tail. Not a restatement of a class
    field. -/
-- Ref: [wenzl1988] https://doi.org/10.1007/BF01393695
-- Ref: [leitner2026] quantum-observable-universe/observations/brane-tower-q-laplacian-decay.md
theorem brane_tower_q_laplacian_decay [ctx : BraneTowerQLaplacianDecayContext] :
    |ctx.T_rho - ctx.hbar_q ^ 2 * ctx.delta1_rho|
      ≤ ctx.hbar_q ^ 4 * ctx.rho_L2 *
        (ctx.q_real ^ (-2 : ℤ) / (1 - ctx.q_real ^ (-2 : ℤ))) := by
  set r := ctx.r with hr
  set M := ctx.hbar_q ^ 4 * ctx.rho_L2 with hM
  -- Sum the geometric majorant to closed form: ∑' k, M·r^{k+1} = M·r/(1 − r).
  have hgeom : ∑' k : ℕ, M * r ^ (k + 1) = M * r / (1 - r) := by
    have hbase : ∑' k : ℕ, r ^ k = (1 - r)⁻¹ :=
      tsum_geometric_of_lt_one ctx.r_nonneg ctx.r_lt_one
    calc
      ∑' k : ℕ, M * r ^ (k + 1)
          = ∑' k : ℕ, (M * r) * r ^ k := by
            refine tsum_congr (fun k => ?_); ring
      _ = (M * r) * ∑' k : ℕ, r ^ k := by rw [tsum_mul_left]
      _ = (M * r) * (1 - r)⁻¹ := by rw [hbase]
      _ = M * r / (1 - r) := by ring
  -- Chain: |remainder| ≤ (geometric sum) = closed form, then rewrite r = q⁻².
  calc
    |ctx.T_rho - ctx.hbar_q ^ 2 * ctx.delta1_rho|
        ≤ ∑' k : ℕ, M * r ^ (k + 1) := ctx.remainder_le_geom
    _ = M * r / (1 - r) := hgeom
    _ = ctx.hbar_q ^ 4 * ctx.rho_L2 *
          (ctx.q_real ^ (-2 : ℤ) / (1 - ctx.q_real ^ (-2 : ℤ))) := by
        rw [hM, hr, ctx.ratio_eq]; ring

end QOU.Observations
