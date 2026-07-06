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

/-! ### Evaluation of `delta_tau_M_canonical` at the explicit instance

The three lemmas below make the §3b-cond conditional theorems concrete at
the one in-repo instance (`explicitInstance`), closing the loop between
the class hypothesis and a downstream computation. They feed the
numerical companion
[`qbeta_delta_tau_M_canonical_explicit_instance.py`](../../../../../computations/qbeta/qbeta_delta_tau_M_canonical_explicit_instance.py)
(witness `qbeta-delta-tau-m-canonical-explicit-instance.witness.json`),
which evaluates the SAME object at substrate q₀ and reports the
cross-anchor swing against the rational surrogate. -/

/-- **Lemma (explicit-instance unfolding).** With the explicit √q-bearing
instance, the canonical Δτ_M is the concrete `z`-weighted block sum, where
`z = markov_parameter q = √q / (1 + q)`:

  `Δτ_M^can(q) = z · χ_(3) + (1/2 − z) · χ_(2,1) + z · χ_(1,1,1)`.

Pure definitional unfolding (the instance projections β/ι-reduce). -/
theorem delta_tau_M_canonical_explicit_eq (q : ℝ) :
    @delta_tau_M_canonical CanonicalMarkovWeightsH3.explicitInstance q
      = markov_parameter q * chi_block_3 q
      + (1 / 2 - markov_parameter q) * chi_block_21 q
      + markov_parameter q * chi_block_111 q :=
  rfl

/-- **Theorem (explicit-instance vanishing at q = 1).** The canonical Δτ_M
at the explicit instance vanishes at the classical point. This is the
conditional `delta_tau_M_canonical_vanish_at_one` dispatched at the
explicit instance — confirming the conditional theorem is non-vacuous. -/
theorem delta_tau_M_canonical_explicit_vanish_at_one :
    @delta_tau_M_canonical CanonicalMarkovWeightsH3.explicitInstance 1 = 0 :=
  @delta_tau_M_canonical_vanish_at_one CanonicalMarkovWeightsH3.explicitInstance

/-- **Theorem (explicit-instance (q²−1) factor).** For `q > 0`, the
canonical Δτ_M at the explicit instance factors through `(q² − 1)`, so it
vanishes at the classical point `q = 1` for the structural reason (the
`(q²−1)` factor in every per-block character), independently of the
`√q`-bearing weights.

Proof: unfold to the `z`-weighted block sum
(`delta_tau_M_canonical_explicit_eq`), substitute the per-block
factorisations from `chi_blocks_have_q2_minus_1_factor`, and pull out the
common `(q²−1)`; the cofactor carries the weights `z = markov_parameter q`
as an opaque atom under `ring`. -/
theorem delta_tau_M_canonical_explicit_has_q2_minus_1_factor
    (q : ℝ) (hq : 0 < q) :
    ∃ P : ℝ, @delta_tau_M_canonical CanonicalMarkovWeightsH3.explicitInstance q
      = (q ^ 2 - 1) * P := by
  obtain ⟨P3, P21, P111, h3, h21, h111⟩ := chi_blocks_have_q2_minus_1_factor q hq
  refine ⟨markov_parameter q * P3 q
          + (1 / 2 - markov_parameter q) * P21 q
          + markov_parameter q * P111 q, ?_⟩
  rw [delta_tau_M_canonical_explicit_eq, h3, h21, h111]
  ring

end QOU.BraidKnot
