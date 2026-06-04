import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.Ring
import QOU.BraidKnot.QBetaPerBlockChiClosedForms

/-!
# QOU.BraidKnot — Explicit instance of `CanonicalMarkovWeightsH3`

**An explicit √q-bearing inhabitant of the `CanonicalMarkovWeightsH3`
class** (from `prop:qbeta-per-block-chi-closed-forms` §Extension #4,
PR #1764). The instance is built from the Markov parameter
`markov_parameter q = √q / (1 + q)`:

  y_(3)(q)    = z(q)
  y_(2,1)(q)  = 1/2 - z(q)
  y_(1,1,1)(q) = z(q)

The dimension-normalisation axiom holds for any `q > 0`:
  y_(3) + 2·y_(2,1) + y_(1,1,1) = z + (1 - 2z) + z = 1. ✓

**Honest scope.** This proves the class is INHABITABLE — making
the §3b-cond conditional theorems
(`delta_tau_M_canonical_has_q2_minus_1_factor` etc.) non-vacuous —
but is NOT a claim that this is THE canonical Wenzl–Markov instance.
The canonical Wenzl weights have a different closed form derived
from the Bratteli-diagram structure of H_3(q); see the accompanying
.md for the numerical comparison.

LaTeX label: `prop:qbeta-canonical-markov-weights-explicit-instance`
-/

namespace QOU.BraidKnot

/-- **Explicit √q-bearing instance of `CanonicalMarkovWeightsH3`.**

Constructed from the Markov parameter `z(q) = √q / (1 + q)`. The
sum-of-dimensions normalisation `y_(3) + 2·y_(2,1) + y_(1,1,1) = 1`
follows from `z + (1 - 2z) + z = 1` for any real-valued z.

**Not canonical.** This is one valid inhabitant of the class. The
canonical Wenzl weights differ; identifying THE canonical inhabitant
is open math (residue-A categorical ID; see 1ppQ-Q$_β$ ledger). -/
noncomputable instance CanonicalMarkovWeightsH3.explicitInstance :
    CanonicalMarkovWeightsH3 where
  y3   := fun q => markov_parameter q
  y21  := fun q => 1/2 - markov_parameter q
  y111 := fun q => markov_parameter q
  sum_dim_normalised := by
    intro q _
    -- y_(3)(q) + 2·y_(2,1)(q) + y_(1,1,1)(q)
    -- = z + 2·(1/2 - z) + z
    -- = z + 1 - 2z + z = 1.
    ring

/-- **Witness (sanity check): the class is inhabited.** This is
syntactic; it confirms that subsequent conditional theorems
`[CanonicalMarkovWeightsH3]` have at least one concrete dispatch
target. -/
theorem CanonicalMarkovWeightsH3.is_inhabited :
    Nonempty CanonicalMarkovWeightsH3 :=
  ⟨CanonicalMarkovWeightsH3.explicitInstance⟩

end QOU.BraidKnot
