import QOU.BraidKnot.QBetaCanonicalMarkovWeightsInstance
import QOU.SchurWeyl.OcneanuWeightMarkov3

/-!
# QOU.BraidKnot.QBetaCanonicalMarkovWeightsDerived — the H₃ instance IS the derived Markov weights

`QBetaCanonicalMarkovWeightsInstance` (PR #6487) makes `canonicalInstance` — the weights
`y₍₃₎ = (q⁴+1)/(q²+1)²`, `y₍₂,₁₎ = q²/(q²+1)²`, `y₍₁³₎ = 0` — the default inhabitant of
`CanonicalMarkovWeightsH3`.  That PR justified the three values by a probe
(`canonical_markov_weights_h3_are_sl2_dimensions.py`, exact sympy) against the Ocneanu
product at `z_D`.  A probe is a check, not a derivation, and the corpus already holds the
derivation: `HeckeMarkov3.markovWeight0/1/2` are the `n = 3` Markov weights **solved from the
defining conditions** `tr_M(1) = 1`, `tr_M(σ₁) = z`, and the Markov relation
(derive-then-check, SW-8), and `OcneanuWeightMarkov3` proves the general-`n` closed form
`ocneanuWeight` reproduces them.

This file closes the loop: at convention D's `z_D = q³/(q²+1)` the instance's three values
**are** `markovWeight0`, `markovWeight2`, `markovWeight1` (in the block order `(3)`, `(2,1)`,
`(1³)`), hence are the `n = 3` slice of `ocneanuWeight q z_D`.  So the default instance is
now *proved equal to the derived object*, and nothing about it rests on the probe.

## Credit — this arc re-derived prior art

The "Ocneanu family `z_N = q^N/[N]_q`, D is its `N = 2` point, C is in no member" story told in
`rem:markov-z-reconciliation` and PR #6370 was **already in Lean**, and that PR did not cite
it.  The record, so the next reader does not repeat the omission:

* `QOU.QBeta.WenzlWeight.wenzlLevel_conventionD`, `level_eq_two_of_conventionD` (PR #5242,
  2026-08-16): D is Wenzl level `r = 2`.
* `QOU.SchurWeyl.OcneanuWeight` (PR #5575, 2026-08-23): the general-`n` cell product, the
  `z_D` row cap, and "`z_D` is the `k = 2` member of `z = q^{2k+1}/(1+q²+⋯+q^{2k})`, C in no
  member" — that family is `z_N` with `N = k`, written with the geometric sum in place of
  `[N]_q`.
* `QOU.SchurWeyl.WenzlWeightLevelR.wenzlMarkovParam`: the level-`r` family itself; the Toffoli
  file's `markovZAt N q` is `wenzlMarkovParam N (q²) / q` (Hecke normalisation).
* `QOU.SchurWeyl.OcneanuWeightWenzl.ocneanuWeight_conventionD_eq_schurPrincipal`: the
  hook-content identification at every `μ` — the bridge #6370 presented as new.
* `QOU.MassTheory.TwoRowCapDerived.traceSum_eq_twoRow_of_wenzl`: the mass channel's trace
  restricts exactly to two-row partitions, `χ` free — the "push into the mass channel" that
  motivated this file, closed before it was proposed.

What #6370 adds beyond those is the framing-ratio *mechanism* (a monomial `a = q^N` collapses
each Ocneanu numerator into a quantum integer) and the log-derivative argument that C is in no
member for any real exponent, not only no integer one.

## Base ring (§7c)

`ℝ`, forced: `markovWeight0/1/2` and `canonical_y3/y21` are `ℝ`-valued, and the
`positivity` discharges of `q² + 1 ≠ 0` / `q⁴ + q² + 1 ≠ 0` are archimedean.

LaTeX label: `prop:qbeta-canonical-markov-weights-explicit-instance`
-/

namespace QOU.BraidKnot

open QOU.SchurWeyl YoungDiagram

/-- Convention D's Markov parameter, `z_D = q³/(q²+1)`, as a named function of `q`. -/
noncomputable def markovZD (q : ℝ) : ℝ := q ^ 3 / (q ^ 2 + 1)

/-- **`y₍₃₎` is the derived trivial-block weight.**  `canonical_y3 q = markovWeight0 q z_D`. -/
theorem canonical_y3_eq_markovWeight0 (q : ℝ) :
    canonical_y3 q = markovWeight0 q (markovZD q) := by
  have hp : (q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  have hp' : (q ^ 4 + q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  unfold canonical_y3 markovWeight0 markovZD
  field_simp
  ring

/-- **`y₍₂,₁₎` is the derived two-dimensional-block weight.**
`canonical_y21 q = markovWeight2 q z_D`. -/
theorem canonical_y21_eq_markovWeight2 (q : ℝ) :
    canonical_y21 q = markovWeight2 q (markovZD q) := by
  have hp : (q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  have hp' : (q ^ 4 + q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  unfold canonical_y21 markovWeight2 markovZD
  field_simp
  ring

/-- **`y₍₁³₎ = 0` is the derived sign-block weight at `z_D`.**  The vanishing is not imposed:
`markovWeight1` carries the factor `z(q²+1) − q³`, which is zero exactly at `z_D`. -/
theorem markovWeight1_at_markovZD (q : ℝ) :
    markovWeight1 q (markovZD q) = 0 := by
  have hp : (q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  have hp' : (q ^ 4 + q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  unfold markovWeight1 markovZD
  field_simp
  ring

/-- **The default instance resolves to the derived weights**, field by field.  The left sides
elaborate through instance resolution; the right sides are `HeckeMarkov3`'s solved weights at
`z_D`.  Block order: `y3 ↔ (3) ↔ markovWeight0`, `y21 ↔ (2,1) ↔ markovWeight2`,
`y111 ↔ (1³) ↔ markovWeight1`. -/
theorem canonicalInstance_eq_markovWeights (q : ℝ) :
    CanonicalMarkovWeightsH3.y3 q = markovWeight0 q (markovZD q)
      ∧ CanonicalMarkovWeightsH3.y21 q = markovWeight2 q (markovZD q)
      ∧ CanonicalMarkovWeightsH3.y111 q = markovWeight1 q (markovZD q) :=
  ⟨canonical_y3_eq_markovWeight0 q, canonical_y21_eq_markovWeight2 q,
    by rw [markovWeight1_at_markovZD]; rfl⟩

/-- **The instance is the `n = 3` slice of the general-`n` Ocneanu weight at `z_D`**, on all three
partitions of `3`.  Chained through `OcneanuWeightMarkov3`, which needs `q² ≠ 1` for its hook
denominators. -/
theorem canonicalInstance_eq_ocneanuWeight (q : ℝ) (hq2 : q ^ 2 ≠ 1) :
    CanonicalMarkovWeightsH3.y3 q = ocneanuWeight q (markovZD q) (ofRowLens [3] (by decide))
      ∧ CanonicalMarkovWeightsH3.y21 q
          = ocneanuWeight q (markovZD q) (ofRowLens [2, 1] (by decide))
      ∧ CanonicalMarkovWeightsH3.y111 q
          = ocneanuWeight q (markovZD q) (ofRowLens [1, 1, 1] (by decide)) := by
  rw [ocneanuWeight_rowLens_three q _ hq2, ocneanuWeight_rowLens_twoOne q _ hq2,
    ocneanuWeight_rowLens_oneCubed q _ hq2]
  exact canonicalInstance_eq_markovWeights q

/-- Total weight normalisation `y_3(q) + 2 * y_{2,1}(q) = 1` of the canonical
three-strand weights across all `q : ℝ`. -/
theorem canonical_y3_add_two_y21_eq_one (q : ℝ) :
    canonical_y3 q + 2 * canonical_y21 q = 1 := by
  have hp : (q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  unfold canonical_y3 canonical_y21
  field_simp
  ring

end QOU.BraidKnot
