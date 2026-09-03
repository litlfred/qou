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

/-! ### The CANONICAL inhabitant

The instance above is a valid inhabitant and was never claimed to be the
canonical one — the accompanying `.md` says so, and records that
"identifying the canonical inhabitant remains open".  It is no longer open.

The canonical Wenzl–Markov weights of the production trace (convention D)
are the `U_q(𝔰𝔩₂)` quantum dimensions normalised by `[2]_q³`:

  `y_(3)   = [4]_q/[2]_q³ = (q⁴+1)/(q²+1)²`
  `y_(2,1) = 1/[2]_q²     = q²/(q²+1)²`
  `y_(1³)  = 0`

**Why these and not others.** Convention D is the `N = 2` member of the
Ocneanu family `z_N = q^N/[N]_q`: its framing ratio `a² = z/z₋` is the
monomial `q⁴`, which collapses every Ocneanu numerator into quantum
integers and turns the weight product into the hook-content formula
`w_λ = dim_q(V_λ^{𝔰𝔩_N})/[N]_q^n`.  So these three values are *derived*
from the trace, not fitted to it
(`computations/probes/ocneanu_weights_are_sl_n_quantum_dimensions.py`,
13/13; `QOU.Information.markov_framing_ratio_eq` and
`markovZ_eq_qsq_div_qDimTwo`, sorry-free).

The `y_(1³) = 0` is not a coincidence either: it is the `𝔰𝔩₂` **row
bound**.  A partition with more than `N` rows contains a cell of content
`-N`, whose Ocneanu numerator factor vanishes identically
(`QOU.Information.ocneanu_numerator_vanishes_at_content_neg`).  Three
rows, `N = 2`.

The numerical values at the substrate `q₀ ≈ 1.10998` are
`0.5054042, 0.2472979, 0` — exactly what the accompanying `.md` records
as the canonical convention-D weights. -/

/-- The canonical weight on `V_(3)`: `[4]_q/[2]_q³ = (q⁴+1)/(q²+1)²`. -/
noncomputable def canonical_y3 (q : ℝ) : ℝ := (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2

/-- The canonical weight on `V_(2,1)`: `1/[2]_q² = q²/(q²+1)²`. -/
noncomputable def canonical_y21 (q : ℝ) : ℝ := q ^ 2 / (q ^ 2 + 1) ^ 2

/-- **The canonical inhabitant of `CanonicalMarkovWeightsH3`.**

The `𝔰𝔩₂` quantum dimensions of the production trace.  Unlike
`explicitInstance`, this is not merely *an* inhabitant: it is the one the
convention-D Markov trace actually carries, derived from the framing
ratio rather than chosen to satisfy the normalisation.

The normalisation is an identity rather than a constraint that had to be
arranged: `(q⁴+1) + 2q² = (q²+1)²`.

⚠ **Declared as a `def`, not an `instance`, deliberately.** The class already
has one global instance (`explicitInstance`), and a second one would silently
become the resolution default for any future bare `delta_tau_M_canonical q` —
later instances win.  Every present use either takes the instance as a
hypothesis binder or names `explicitInstance` with `@`, so nothing changes
today; but promoting this to the default is a decision whose blast radius
across the `[CanonicalMarkovWeightsH3]` consumers a per-file `lean`-direct
check cannot verify.  It is the *canonical* weight set and arguably *should*
be the default — that promotion is left as an explicit follow-up rather than
taken as a side effect of adding it. -/
noncomputable def CanonicalMarkovWeightsH3.canonicalInstance :
    CanonicalMarkovWeightsH3 where
  y3   := canonical_y3
  y21  := canonical_y21
  y111 := fun _ => 0
  sum_dim_normalised := by
    intro q hq
    have hd : (q ^ 2 + 1) ≠ 0 := by positivity
    unfold canonical_y3 canonical_y21
    field_simp
    ring

/-- **The `(1³)` block carries zero weight** at the canonical instance —
    the `𝔰𝔩₂` row bound, stated where downstream consumers can use it. -/
theorem canonical_y111_eq_zero (q : ℝ) :
    CanonicalMarkovWeightsH3.canonicalInstance.y111 q = 0 := rfl

/-- **The canonical weight set is a genuine inhabitant of the class**, so the
    `[CanonicalMarkovWeightsH3]`-conditional theorems are non-vacuous at the
    weights the production trace actually carries — not only at the
    `√q`-bearing `explicitInstance`. -/
theorem canonical_is_inhabitant : Nonempty CanonicalMarkovWeightsH3 :=
  ⟨CanonicalMarkovWeightsH3.canonicalInstance⟩

/-- **Δτ_M at the canonical instance**, unfolded to the `𝔰𝔩₂`-weighted block
    sum with the `(1³)` block dropping out by the row bound. -/
theorem delta_tau_M_canonical_at_canonical_eq (q : ℝ) :
    @delta_tau_M_canonical CanonicalMarkovWeightsH3.canonicalInstance q
      = canonical_y3 q * chi_block_3 q
      + canonical_y21 q * chi_block_21 q
      + 0 * chi_block_111 q :=
  rfl

/-- **The two nonzero canonical weights sum with their dimensions to one**,
    with the `(1³)` block contributing nothing. -/
theorem canonical_two_block_normalisation {q : ℝ} (hq : 0 < q) :
    canonical_y3 q + 2 * canonical_y21 q = 1 := by
  have hd : (q ^ 2 + 1) ≠ 0 := by positivity
  unfold canonical_y3 canonical_y21
  field_simp
  ring

/-- **Witness (sanity check): the class is inhabited.** This is
syntactic; it confirms that subsequent conditional theorems
`[CanonicalMarkovWeightsH3]` have at least one concrete dispatch
target. -/
theorem is_inhabited :
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
