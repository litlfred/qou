import QOU.BraidsAndKnots.NucleonIsospinExclusions
import Mathlib.Tactic.Linarith

/-!
# The neutron's `q⁻²` from the nucleon's own-sector quantum trace

The mass identity has a volume term (a whole-space Markov trace, the same for p and n) and a
constant term (`−12 mₑ` on the proton, not derived: issue #8809). This file derives the neutron's
constant from **one structural premise**: the constant is the convention-D quantum trace of some
braid element `w`, taken on the nucleon's own weight space, times a normalisation `κ` common to
p and n.

Under that premise the neutron's constant is `q⁻²` times the proton's. This holds for **every**
signed braid word `w` and every `κ`, because `T_p = q²·T_n` word by word
(`NucleonIsospinExclusions.restrictedTrace_ratio`, from the intertwiner `P`). Fixing the proton
value to its count `12 mₑ` then gives `12 q⁻² mₑ` for the neutron, so
`m_n − m_p = 12(1 − q⁻²) mₑ`, and the neutron is heavier for `q > 1`.

* `neutron_constant_ratio` : `κ·T_n(w) = q⁻²·(κ·T_p(w))`.
* `neutron_constant_of_proton` : if `κ·T_p(w) = 12 mₑ`, then `κ·T_n(w) = 12 q⁻² mₑ`.
* `split_of_sector_qtrace` : `m_n − m_p = 12(1 − q⁻²) mₑ`.
* `neutron_heavier_of_sector_qtrace` : `m_p < m_n` for `q > 1`, `mₑ > 0`.
* `bare_sector_constant_no_split` : with the bare (unweighted) sector trace there is no split.

Not derived here: that the constant is a sector quantum trace, and the count `12`. No measured
value enters.
-/

namespace QOU.MassTheory.NeutronSectorQTraceConstant

open Matrix QOU.BraidsAndKnots.NucleonWeightSpaceTraces QOU.BraidsAndKnots.NucleonIsospinExclusions

section Field

variable {R : Type*} [Field R]

/-- Word by word, the neutron's own-sector quantum trace is `q⁻²` times the proton's. -/
theorem neutron_constant_ratio (q κ : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (w : List Letter) :
    κ * Tn q w = q⁻¹ ^ 2 * (κ * Tp q w) := by
  rw [restrictedTrace_ratio q hq hq2 w]
  field_simp

/-- Fixing the proton's constant to `12 mₑ` fixes the neutron's to `12 q⁻² mₑ`. -/
theorem neutron_constant_of_proton (q κ me : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (w : List Letter) (hp : κ * Tp q w = 12 * me) :
    κ * Tn q w = 12 * q⁻¹ ^ 2 * me := by
  rw [neutron_constant_ratio q κ hq hq2 w, hp]
  ring

/-- The split: same volume term `v` for both, constants from the own-sector quantum trace. -/
theorem split_of_sector_qtrace (q κ me v : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (w : List Letter) (hp : κ * Tp q w = 12 * me) :
    (v - κ * Tn q w) - (v - κ * Tp q w) = 12 * (1 - q⁻¹ ^ 2) * me := by
  rw [neutron_constant_of_proton q κ me hq hq2 w hp, hp]
  ring

/-- With the bare sector trace (no Cartan weight) the constants agree: no split. -/
theorem bare_sector_constant_no_split (q κ : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (w : List Letter) :
    κ * trace (sword q (A₁ q) (A₂ q) w) = κ * trace (sword q (B₁ q) (B₂ q) w) := by
  rw [trace_sword_eq q hq hq2 w]

end Field

section Ordered

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- For `q > 1` and `mₑ > 0` the neutron is heavier under the own-sector premise. -/
theorem neutron_heavier_of_sector_qtrace (q κ me v : R) (hq : 1 < q) (hme : 0 < me)
    (w : List Letter) (hp : κ * Tp q w = 12 * me) :
    v - κ * Tp q w < v - κ * Tn q w := by
  have hq0 : q ≠ 0 := (lt_trans zero_lt_one hq).ne'
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hs := split_of_sector_qtrace q κ me v hq0 hq2 w hp
  have hinv : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  have hinv0 : 0 < q⁻¹ := inv_pos.mpr (lt_trans zero_lt_one hq)
  have hsq : q⁻¹ ^ 2 < 1 := by nlinarith
  have : 0 < 12 * (1 - q⁻¹ ^ 2) * me := by
    apply mul_pos _ hme
    linarith
  linarith

end Ordered

end QOU.MassTheory.NeutronSectorQTraceConstant
