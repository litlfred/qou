import QOU.Braiding.WeakVertexJonesMarkov

/-!
# Numerical envelopes for the Jones–Markov derivation, at the proton pin

`WeakVertexJonesMarkov` is entirely generic-field algebra: the normalisation, the
factorisation `J − 1 = −h₄h₆/q¹⁰`, and the exact ratio `couplingRatio q =
−G₈(q)G₁₂(q)/q¹⁹` need no ordering and no square root. What genuinely needs `ℝ`
is *evaluating* those at the substrate anchor, and per AGENTS.md §7c that lives
here rather than in the generic file.

Anchor: the experimental (proton) pin `q₀ = 1.1099785827513808…`
(`qou_substrate.constants.Q`), the default for all production compute.

Two envelopes, both from the producer's numbers:

* `couplingRatio_near_q0` — the ratio has **run from `−96` to `−37.09`** by the
  time it reaches `q₀`. This is the archimedean face of
  `couplingRatio_not_constant`: the framing `q^{-19}` and the size of the Jones
  exponents suppress the ratio away from `q = 1`, which is *why* no rescaling
  constant exists.
* `substitutionRateFactor_overshoot_of_leading_square` — the measured
  substitution factor `|W(q₀)|²/s(q₀)⁴ = 11875.4418936763` against the derived
  leading square `96² = 9216`: the **overshoot is `1.2885679138`**, and the
  theorem brackets that measured number rather than a round window around it.
  That is the falsifiable content of "the order is derived", with the residual
  stated instead of absorbed.

  The first form of this theorem said the factor lies between `96²` and `2·96²`.
  It is **withdrawn**: the `2` is round only because the measurement happens to
  fit under it, i.e. a window chosen against the target — which the no-fitting
  directive of 2026-09-05 counts as a fit even though no continuous parameter is
  tuned. A tolerance sized to contain its own miss hides the miss; a reported
  ratio does not, and `1.2885679138` is a number the next agent can attack.

Producer: `computations/markov/weak_vertex_jones_markov_normalisation.py` (13/13)
Witness: `computations/weak-vertex-jones-markov-normalisation.witness.json`
Bean: `qou-q2l7`.
-/

namespace QOU.Braiding.WeakVertexT35

/-- **The ratio runs.** At the proton pin the exact ratio `−G₈G₁₂/q¹⁹` has already fallen
from its classical value `−96` (`couplingRatio_one`) to `≈ −37.0915`. Since the two
couplings differ by a *function*, no constant relates them — this is the numerical face of
`couplingRatio_not_constant`. -/
theorem couplingRatio_near_q0 :
    (-37.10 : ℝ) < couplingRatio (1.1099785827513808 : ℝ) ∧
      couplingRatio (1.1099785827513808 : ℝ) < -37.08 := by
  simp only [couplingRatio, geomCofactor, Finset.sum_range_succ, Finset.sum_range_zero]
  constructor <;> norm_num

/-- **The order of the `≈ 10⁴` substitution factor is derived, and the residual is
reported.** The coupling ratio's classical value is `−96` (`couplingRatio_one`), so a
coupling carrying the trace's Jones content sits `≈ 10²` above `s²` and its square
`≈ 10⁴` above `s⁴`. Measured against `substitutionRateFactor`, the derived leading
square `96² = 9216` undershoots the actual `11875.4418936763` by the factor

`|W(q₀)|²/s(q₀)⁴ / 96² = 1.2885679138…`

and *that* is what this theorem brackets — the measured overshoot to three decimals,
not a round tolerance around it. The overshoot is nonzero because `couplingRatio` runs
from `−96` to `−37.09` on the way to `q₀`; it is the size of what the leading term
misses, and it is stated rather than absorbed. -/
theorem substitutionRateFactor_overshoot_of_leading_square :
    1.288 * ((96 : ℝ)) ^ 2 < substitutionRateFactor (1.1099785827513808 : ℝ) ∧
      substitutionRateFactor (1.1099785827513808 : ℝ) < 1.289 * ((96 : ℝ)) ^ 2 := by
  rw [substitutionRateFactor_eq _ (by norm_num) (by norm_num) (by positivity)]
  constructor <;> norm_num

end QOU.Braiding.WeakVertexT35
