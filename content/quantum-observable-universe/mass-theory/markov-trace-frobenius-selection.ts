import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:markov-trace-frobenius-selection",
  title: "Markov-trace selection on H_n(R, q) — the row cap, not non-degeneracy",
  cites: ["jones1987", "wenzl1988", "yekutieli2015"],
  uses: [
    "lem:feynman-eigenbasis-decomposition",
    "prop:convention-d-kills-antisymmetriser",
  ],
  defines: [],
  tags: [
    "normalization",
    "frobenius",
    "no-fitting",
    "uniqueness",
    "trace-convention",
    "conditional",
  ],
  lean: {
    ref: "qou:QOU.BraidsAndKnots.markovWeights_eq_jones_of_fibre_categorical",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "Wired to the derived characterisation (detangler decision 7). The replacement " +
        "criterion is faithfulness on the non-radical blocks together with the row cap, and " +
        "it is now backed by an exposition block rather than by this note alone: " +
        "prop:convention-d-kills-antisymmetriser, carrying " +
        "qou:QOU.QBeta.TemperleyLiebTower.antisym_vanishes_only_at_two_roots (the antisymmetric " +
        "weight vanishes at exactly two values of z) and z_eq_q_forces_trivial (the branch z = q " +
        "collapses the trace to the one-dimensional character). Convention D is thereby the " +
        "UNIQUE non-trivial Markov trace on H_3(q) killing the three-strand antisymmetriser, " +
        "and convention C is excluded by derivation rather than by ruling. The uses[] edge " +
        "added here is the editorial one: a reader needs the characterisation to see why the " +
        "row cap selects rather than merely describes.",
    },
    {
      kind: "note",
      date: "2026-08-09",
      body: "Restated (detangler decision 2). The selection criterion was NON-DEGENERACY, which convention D provably violates: y_(1^3) = 0 exactly, so the block published a derivation arguing against the convention it adopted. Criterion replaced by {row cap: y_lambda = 0 for l(lambda) >= 3} + {faithfulness: y_lambda != 0 for l(lambda) <= 2}, which — unlike non-degeneracy — DERIVES z*[2]_q = q^2. The hypotheses bite at level 3: at n <= 2 the row cap is vacuous and z is genuinely free, so the selection theorem is stated with its level-3 weight vector rather than at an arbitrary n; stated at arbitrary n it would be false, since at n = 2 the two hypotheses hold for a one-parameter family of traces. Uniqueness at fixed z was never a consequence of non-degeneracy and is unchanged. The pairing is degenerate on H_n with radical exactly the Temperley-Lieb ideal, and non-degenerate on TL_n. lean.ref repointed off qou_markov_trace_is_jones_markov, whose MarkovTraceUniqueness class is unsatisfiable over any field with an element outside {0,1}.",
    },
    {
      kind: "note",
      date: "2026-05-29",
      body: "The degenerate Schur–Weyl candidate τ_SW was purged per owner decision A' (PR #1422). An earlier 2026-05-11 escalation framed the from-scratch result as a τ_M / τ_SW conflation; it is read instead as a different braid's τ_M.",
    },
  ],
});
