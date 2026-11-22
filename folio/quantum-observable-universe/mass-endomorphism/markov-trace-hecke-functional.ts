import { proposition } from "../../schema/builders";

/**
 * The Markov trace as a linear functional on the Hecke algebra, and the
 * connected-sum rule. Lifts the word evaluator `trWord` of
 * `prop:markov-trace-recursive-reducer` from positive braid words to the
 * presented Hecke tower, then to `QOU.Hecke.IwahoriHecke K q n`.
 */
export default proposition({
  label: "prop:markov-trace-hecke-functional",
  title:
    "The Markov trace is a linear functional on $H_n(q)$, and the connected-sum rule",
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-22",
      body: "Proved in Lean, sorry-free (axioms propext, Classical.choice, Quot.sound): `towerTr`, `towerTr_mul_comm`, `towerTr_markov`, `towerTr_disjoint`, `towerTr_connectedSum`, `towerTr_interface`, `heckeMarkovTrace`, `heckeMarkovTrace_mul_comm`, `heckeMarkovTrace_σ`, `markovKnotFactor`, `markov_trace_eq_tau_mul_knotFactor`. Also proved: `heckeIncl`, `heckeShift`, `heckeMarkovTrace_heckeIncl` (coherence along inclusions), `heckeMarkovTrace_disjoint` and `heckeMarkovTrace_connectedSum` on the finite algebras (factor s z). Bond words: `towerTr_interfaceWord` (a block bond B gives the factor tr B), `towerTr_vertexCube_block`, `towerTr_overlapBond` and `towerTr_gammaGammaBond` (the overlapping γγ bond gives tr X · tr(V³ Y↑¹), independent of the first nucleon). This is a candidate mechanism for the measured fact in `gamma-gamma-bond-is-pair-independent.witness.json` that μ depends only on the second nucleon; it applies only if that probe's weighted H₆ trace equals `towerTr` at z_D on these words, which is not checked. Issue #8960.",
    },
  ],
  uses: ["prop:markov-trace-recursive-reducer"],
  cites: ["jones1987"],
  lean: {
    ref: "qou:QOU.BraidKnot.HeckeFunctional.towerTr_connectedSum",
    validation: "not_checked",
  },
  tags: ["markov-trace", "connected-sum", "linear-functional", "knot-factor"],
});
