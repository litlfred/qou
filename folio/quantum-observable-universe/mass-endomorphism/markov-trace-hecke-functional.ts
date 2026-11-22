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
      body: "Proved in Lean, sorry-free (axioms propext, Classical.choice, Quot.sound): `towerTr`, `towerTr_mul_comm`, `towerTr_markov`, `towerTr_disjoint`, `towerTr_connectedSum`, `towerTr_interface`, `heckeMarkovTrace`, `heckeMarkovTrace_mul_comm`, `heckeMarkovTrace_σ`, `markovKnotFactor`, `markov_trace_eq_tau_mul_knotFactor`. Also proved: `heckeIncl`, `heckeShift`, `heckeMarkovTrace_heckeIncl` (coherence along inclusions), `heckeMarkovTrace_disjoint` and `heckeMarkovTrace_connectedSum` on the finite algebras (factor s z). Bond words: `towerTr_interfaceWord` (a block bond B gives the factor tr B), `towerTr_vertexCube_block`, `towerTr_overlapBond` and `towerTr_gammaGammaBond` (the overlapping γγ bond gives tr X · tr(V³ Y↑¹), independent of the first nucleon). This is the mechanism for the measured fact in `gamma-gamma-bond-is-pair-independent.witness.json` that μ depends only on the second nucleon. Checked 2026-11-22: the probe's trace (Σ_λ y_λ χ_λ over λ ⊢ 6, `y_lambda_su_n`, zero on three-row shapes) equals an independent exact Markov trace at z_D, proton pin, to ~3e-60 relative on W_free and W_atom for all four pairs, and μ = tr(V³·Y↑¹)/tr Y holds exactly. The probe's layout (bond appended after both nucleons) is `towerTr_overlapBond_appended` with m = 2. The independent trace was not ported line by line from `trWord`; both satisfy the Markov axioms, so they agree by `markovTrace_unique`. Issue #8960.",
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
