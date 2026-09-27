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
* **🛑 `substitutionRateFactor_overshoot_of_leading_square` is WITHDRAWN
  (2026-09-05, bean `qou-xql6`)** and is replaced by
  `substitutionRateFactor_has_no_classical_leading_value`. It claimed the *order*
  of the substitution factor was derived, bracketing `|W(q₀)|²/s(q₀)⁴` against
  `96²`. Two things were wrong with it, and the retraction is not a re-scoping.

  **It compared two different ratios.** `−96` is the classical value of
  `(J − 1)/s²` (`couplingRatio_one`), where the *numerator vanishes* — `J(1) = 1`
  because `V_K(1) = 1` for every knot. The substitution factor's numerator does
  **not** vanish: `W(1) = 1/4` is the Markov rank factor. So `|W|²/s^k` diverges
  as `q → 1` for every `k ≥ 1` and has no leading constant at all; `−96` was
  never its leading value, and there was nothing to derive to order.

  **And the power was wrong.** `sSq` *is* `s²`, so the merged
  `substitutionRateFactor = (W)²/(sSq)²` was `|W|²/s⁴`, while the rate carries
  `s²` once (`prf:trace-ratio-observable`). The factor is `129.405107404`, not
  `11875.44`.

  Every exact identity of this arc survives untouched — the Jones–Markov
  relation, `J − 1 = −h₄h₆/q¹⁰`, `(J−1)/s² = −G₈G₁₂/q¹⁹`, `couplingRatio_one`.
  Only the bridge from `−96` to the rate is gone. Producer
  `beta_rate_skein_power_audit.py` (9/9).

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

/-- **The substitution factor has no classical leading value**, which is why the
`≈ 10⁴`-order claim this file used to carry is withdrawn rather than re-scoped.

`substitutionRateFactor_denominator_vanishes_numerator_does_not` gives the reason at
`q = 1`: `s²(1) = 0` while `W(1)² = 1/16`. Here is the archimedean consequence at the
anchor — the factor is `≈ 129.4`, i.e. `|W|²/s²` and *not* `|W|²/s⁴`, and it is nowhere
near any multiple of `couplingRatio_one`'s `−96`. `−96` is the classical value of
`(J − 1)/s²`, a ratio whose numerator vanishes (`V_K(1) = 1` for every knot); this one's
does not, so the two are not comparable. Bean `qou-xql6`. -/
theorem substitutionRateFactor_has_no_classical_leading_value :
    (129 : ℝ) < substitutionRateFactor (1.1099785827513808 : ℝ) ∧
      substitutionRateFactor (1.1099785827513808 : ℝ) < 130 ∧
      sSq (1 : ℝ) = 0 ∧ weakVertexTrace (1 : ℝ) ^ 2 = 1 / 16 := by
  refine ⟨?_, ?_, by simp [sSq], by rw [weakVertexTrace_one]; norm_num⟩
  · rw [substitutionRateFactor_eq _ (by norm_num) (by norm_num) (by positivity)]
    norm_num
  · rw [substitutionRateFactor_eq _ (by norm_num) (by norm_num) (by positivity)]
    norm_num

end QOU.Braiding.WeakVertexT35
