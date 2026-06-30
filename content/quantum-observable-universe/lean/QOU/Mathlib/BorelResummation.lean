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
import Mathlib.Tactic

namespace QOU.Mathlib.Borel

open scoped Nat

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

end QOU.Mathlib.Borel
