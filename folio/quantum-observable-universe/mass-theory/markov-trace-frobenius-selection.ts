import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:markov-trace-frobenius-selection",
  title: "Markov-trace selection on H_n(R, q) — the row cap, not non-degeneracy",
  cites: ["jones1987", "wenzl1988", "yekutieli2015", "kimlee2018", "webster-williamson-2014-markov"],
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
  // The numerical-verification table in the .md reads this witness
  // (validator val-block-computation, 2026-11-15); same pairing as
  // q-hecke-seminormal-character-closure.ts.
  computation: {
    engine: "mpmath",
    script: "computations/atomic_tr_m_mpfr_50dps.py",
    witness: "computations/atomic-tr-m-mpfr-50dps-proton.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-21",
      body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner: fix issues): The QOU mass identity uses the Frobenius co-Casimir trace identity ([Frobenius co-Casimir universal](#thm:frobenius-codim-universal)):",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): in [Gram-matrix spectral connection](#rem:gram-matrix-spectral-connection)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): *Formalised at $n = 3$, division-free, over a generic commutative domain: `QOU.BraidsAndKnots.markovWeights_eq_jones_of_threeRow_eq_zero` ([`MarkovTraceTLUniqueness.lean`](../lean/QOU/BraidsAndKnots/MarkovTraceTLUniqueness.lean)), with the fibre-side antecedent in `markovWeights_eq_jones_of_fibre_categorical` ([`FibreCategoricalTraceForcesJones.lean`](../lean/QOU/BraidsAndKnots/FibreCategoricalTraceForcesJones.lean)).*" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ... and proved in Lean only as fixed-$n$ instances of the recursion ..." },
    {
      kind: "caveat",
      body: "**Still open, and not repaired here.** The narrative *derivation-chain* documents for these atoms (`{p,n,D}-tr-M-q0`, `markov-trace-assembly-*`) derive their characters by reading a **crossing number** off `atom_braid_word_3A`, whose own docstring states that it returns Hecke elements rather than a braid word and that no topological quantity may be read off it. The live producers do not take that route — they evaluate $\\chi^\\lambda$ as a matrix product in the seminormal representation — so the numbers above are unaffected, but those documents describe a computation nobody performs. Tracked in `qou-1ucq`. A separate open point: the deuteron's bridge leg is recorded `bridge_is_color_blind: true`, the mixed-nucleus colour-blindness of bean `qou-fv0s`.",
    },
    {
      kind: "note",
      date: "2026-08-30",
      body: "**Provenance (regenerated 2026-08-30, bean `qou-1ucq`).** The values above are read from the committed proton-anchored witnesses [`computations/markov/markov-peel-atomic-tr-m.witness.json`](../../../computations/markov/markov-peel-atomic-tr-m.witness.json) and [`computations/canonical-tr-m-via-chi-cache.witness.json`](../../../computations/canonical-tr-m-via-chi-cache.witness.json), not hand-computed. They **replace** a convention-C table (proton $1.0653061442544499$, neutron $0.9232332299116371$, deuteron $0.3882864240747888$) that had been flagged stale on 2026-08-09 and left in place; the correction is $+7.55\\,\\%$, $+6.99\\,\\%$ and $+48.1\\,\\%$ respectively, so the deuteron row in particular was not a rounding-level defect. Its superseded error column, $\\leq 8.16\\times 10^{-16}$, measured agreement among paths that were all in the same convention — it was never a bound on the quantity.",
    },
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
