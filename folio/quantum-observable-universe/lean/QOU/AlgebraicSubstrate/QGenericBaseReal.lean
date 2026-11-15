/-
# `IsQGeneric` past the archimedean wall

The §7c archimedean half of [`QGenericBase.lean`](QGenericBase.lean), split out
because §7c keeps a generic-`R` statement and its `ℝ` specialisation in separate
files — even when, as here, the `ℝ` is warranted rather than gratuitous.

The `ℝ` is the point of this file: the proof genuinely needs the ordering.
`cyclotomic_pos'` holds because every root of `Φ_d` lies on the unit circle, so
`Φ_d` cannot vanish to the right of `1` — an archimedean fact, unavailable over a
generic commutative ring.

It also settles non-vacuity where it matters. `IsQGeneric` is not merely
inhabitable by some toy ring; it is satisfied at the value the framework actually
evaluates at (`q₀ ≈ 1.10998 > 1`), so a definition stated over `IsQGeneric`
reaches the substrate.

-- Ref: [leitner2026] AGENTS.md §7c
-/
import QOU.AlgebraicSubstrate.QGenericBase
import Mathlib.Analysis.SpecialFunctions.Pow.Real

namespace QOU.AlgebraicSubstrate

open Polynomial

/-- **The archimedean instance.** Every real `q > 1` is `q`-generic — the
substrate anchor `q₀ ≈ 1.10998` included.

`ℝ` here is not a §7c violation but the point of the exercise: this is the
specialisation past the archimedean wall, and it genuinely needs the ordering
(`cyclotomic_pos'` holds because every root of `Φ_d` lies on the unit circle, so
`Φ_d` cannot vanish to the right of `1`).

It also settles non-vacuity where it matters. The class is not merely
inhabitable by some toy ring; it is satisfied at the value the framework actually
evaluates at, so a definition stated over `IsQGeneric` reaches the substrate. -/
theorem isQGeneric_real {q : ℝ} (hq : 1 < q) : IsQGeneric ℝ q where
  isUnit_q := isUnit_iff_ne_zero.mpr (by linarith)
  isUnit_cyclotomic d _ := isUnit_iff_ne_zero.mpr (cyclotomic_pos' d hq).ne'

end QOU.AlgebraicSubstrate
