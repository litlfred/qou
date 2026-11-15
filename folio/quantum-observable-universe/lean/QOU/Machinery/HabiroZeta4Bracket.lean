/-
# The ζ₄ modular zero of the categorical bracket — the monodromy point in the Habiro lattice

Small formal anchor for the Habiro ζ₄ bridge (bean qou-vegn). The
corpus's α_EM Habiro element `H(q) = [2]_q (1 − h²α)` has an exact
modular zero at `ζ₄ = i` (block `alpha-em-habiro-bar-involution`), the
SAME evaluation point as the `q = i` monodromy of the τ-assignment
tower. The zero and the bar-symmetry both live entirely in the
categorical factor `[2]_q = q + q⁻¹`, and this file pins them in Lean:

* **`two_bracket_zeta4_eq_zero`** — `[2]_{ζ₄} = i + i⁻¹ = 0`: the
  modular zero at the monodromy point.
* **`two_bracket_bar_fixed`** — `[2]_{q⁻¹} = [2]_q` for every `q : ℂ`:
  bar-involution fixedness of the bracket, with no nonvanishing
  hypothesis (Lean's `0⁻¹ = 0` convention makes it unconditional).

In the GSWZ picture (arXiv:2412.04241, `library/arxiv-2412.04241v2/2412.04241v2.pdf`)
these are the fibre-at-ζ₄ facts of a classical Habiro-ring element; the
p = 2 gluing edge ζ₄ → ζ₈ is verified concretely for this factor in
`computations/probes/zeta4_zeta8_habiro_gluing_probe.py`. The
root-of-unity FAMILY for the τ-assignment tower remains the open half
of bean qou-vegn — nothing about it is claimed here.

HONESTY (STRICT): sorry-free, no axioms, no `decide`; two elementary
facts, named for their role in the bridge. Nothing wired; `1/(8π)`
stays phase-4.

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import Mathlib.Data.Complex.Basic

namespace QOU.Machinery.CoxeterParabolic

open Complex

/-- **The modular zero at the monodromy point**: `[2]_{ζ₄} = 0`. -/
theorem two_bracket_zeta4_eq_zero : (I : ℂ) + I⁻¹ = 0 := by
  rw [Complex.inv_I]
  ring

/-- **Bar-fixedness of the categorical bracket**: `[2]_{q⁻¹} = [2]_q`,
unconditionally over `ℂ`. -/
theorem two_bracket_bar_fixed (q : ℂ) : q⁻¹ + (q⁻¹)⁻¹ = q + q⁻¹ := by
  rw [inv_inv]
  ring

end QOU.Machinery.CoxeterParabolic
