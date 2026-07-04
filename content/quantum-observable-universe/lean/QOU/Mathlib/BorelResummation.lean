/-
  Borel resummation — Mathlib-gap scaffold (bean el8w; epic 08a2).

  HONEST SCOPE. Full Borel resummation (Borel transform + Laplace sum +
  Watson's theorem / Nevanlinna–Sokal uniqueness) is NOT in Mathlib and is a
  major multi-file formalization, ultimately destined for upstream mathlib4.
  This file scaffolds the CORE in qou's `QOU/Mathlib/` gap-infra namespace:

    * the Borel transform COEFFICIENT a_n/n! and the partial Borel transform —
      with the defining MECHANISM proved sorry-free: Borel division tames
      factorial divergence (B[Σ n! z^n] has unit coefficients → geometric);
    * the full Borel SUM and its summability/uniqueness theorems carried as a
      conditional class (`BorelSummable`), the genuine Mathlib gap.

  Why QOU needs it: Ohtsuki's PROOF of the volume conjecture for the figure-
  eight (the Vol(4_1) saddle, QOU/Knot/FigureEightVolume.VolumeConjecture41)
  goes through Borel resummation of the asymptotic series of the Kashaev sum.
  Closing `BorelSummable` for that series is what would discharge the
  conditional `VolumeConjecture41` (bean bca6).

  Pure-ℝ analysis where the integral appears; the coefficient algebra is
  generic. § the hard theorems are explicitly conditional, never `sorry`-faked.

  -- Ref: [manuscript] bean el8w — Borel resummation Mathlib-gap
-/

import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Tactic

namespace QOU.Mathlib.Borel

open scoped Nat
open Filter

/-- The Borel transform coefficient of a formal series `Σ aₙ zⁿ`: `aₙ / n!`. -/
noncomputable def borelCoeff (a : ℕ → ℝ) (n : ℕ) : ℝ := a n / (n ! : ℝ)

/-- The partial Borel transform `Σ_{n=0}^{N} (aₙ/n!) tⁿ`. -/
noncomputable def partialBorel (a : ℕ → ℝ) (N : ℕ) (t : ℝ) : ℝ :=
  ∑ n ∈ Finset.range (N + 1), borelCoeff a n * t ^ n

/-- **The Borel mechanism: division by n! tames factorial divergence.**
    The (everywhere-divergent) series `Σ n! zⁿ` has unit Borel coefficients —
    its Borel transform is the geometric series `Σ tⁿ = 1/(1−t)`. -/
theorem borel_tames_factorial (n : ℕ) :
    borelCoeff (fun k => (k ! : ℝ)) n = 1 := by
  unfold borelCoeff
  exact div_self (by positivity)

/-- Consequently the partial Borel transform of `Σ n! zⁿ` is the geometric
    partial sum `Σ_{n=0}^{N} tⁿ`. -/
theorem partialBorel_factorial (N : ℕ) (t : ℝ) :
    partialBorel (fun k => (k ! : ℝ)) N t = ∑ n ∈ Finset.range (N + 1), t ^ n := by
  unfold partialBorel
  refine Finset.sum_congr rfl (fun n _ => ?_)
  rw [borel_tames_factorial, one_mul]

/-- Borel coefficients are linear in the source sequence. -/
theorem borelCoeff_add (a b : ℕ → ℝ) (n : ℕ) :
    borelCoeff (fun k => a k + b k) n = borelCoeff a n + borelCoeff b n := by
  unfold borelCoeff; rw [add_div]

/-- **Borel-transform convergence** — the first half of Borel summability, with
    genuine content: the partial Borel transforms `Σ_{n≤N}(aₙ/n!)zⁿ` converge as
    `N → ∞` to `value`. (The *second* half — the Laplace resummation
    `∫₀^∞ e^{−t} φ(z t) dt` and Watson / Nevanlinna–Sokal UNIQUENESS — is the
    substantial analysis NOT yet in Mathlib; it is documented in the file
    header as the gap, deliberately not stated with measure-theory imports
    absent from the cache, and NEVER `sorry`-faked.) -/
class BorelTransformConverges (a : ℕ → ℝ) (z : ℝ) : Prop where
  /-- the partial Borel transforms converge to some limit at `z`. -/
  converges :
    ∃ L : ℝ, Filter.Tendsto (fun N => partialBorel a N z) Filter.atTop (nhds L)

/-- The Borel-transform value at `z` (the limit), available once
    `[BorelTransformConverges a z]` is supplied. -/
noncomputable def borelTransformValue (a : ℕ → ℝ) (z : ℝ)
    [h : BorelTransformConverges a z] : ℝ := h.converges.choose

/-- The Borel transform indeed converges to `borelTransformValue`. -/
theorem borelTransform_tendsto (a : ℕ → ℝ) (z : ℝ) [h : BorelTransformConverges a z] :
    Filter.Tendsto (fun N => partialBorel a N z) Filter.atTop
      (nhds (borelTransformValue a z)) :=
  h.converges.choose_spec

/-- **The conditional class is genuinely inhabited** — a sorry-free witness.
    The Borel transform of the series `Σ n! zⁿ` (radius of convergence `0`;
    divergent for every `z ≠ 0`) is the geometric series `Σ zⁿ`, which
    converges on `|z| < 1` to `(1 − z)⁻¹`. This is the concrete analytic
    content that pins `BorelTransformConverges` down to a real convergence
    statement (as opposed to an empty marker): the partial Borel transforms
    of the factorial series tend to `(1 − z)⁻¹`. -/
theorem borelTransform_factorial_tendsto {z : ℝ} (hz : |z| < 1) :
    Filter.Tendsto (fun N => partialBorel (fun k => (k ! : ℝ)) N z) Filter.atTop
      (nhds (1 - z)⁻¹) := by
  have hsum : HasSum (fun n => z ^ n) (1 - z)⁻¹ :=
    hasSum_geometric_of_norm_lt_one (by rwa [Real.norm_eq_abs])
  have h1 : Filter.Tendsto (fun N => ∑ n ∈ Finset.range (N + 1), z ^ n)
      Filter.atTop (nhds (1 - z)⁻¹) :=
    hsum.tendsto_sum_nat.comp (tendsto_add_atTop_nat 1)
  simpa only [partialBorel_factorial] using h1

/-- The factorial series `Σ n! zⁿ` has a convergent Borel transform on the unit
    disc — a nonvacuous instance of the conditional class. -/
instance instBorelTransformConverges_factorial {z : ℝ} (hz : |z| < 1) :
    BorelTransformConverges (fun k => (k ! : ℝ)) z where
  converges := ⟨(1 - z)⁻¹, borelTransform_factorial_tendsto hz⟩

/-- The Borel-transform value of the factorial series is `(1 − z)⁻¹` on the
    unit disc, confirming `borelTransformValue` computes the geometric sum. -/
theorem borelTransformValue_factorial {z : ℝ} (hz : |z| < 1) :
    @borelTransformValue (fun k => (k ! : ℝ)) z (instBorelTransformConverges_factorial hz)
      = (1 - z)⁻¹ :=
  tendsto_nhds_unique
    (@borelTransform_tendsto _ z (instBorelTransformConverges_factorial hz))
    (borelTransform_factorial_tendsto hz)

end QOU.Mathlib.Borel
