import { proof } from "../../schema/builders";

export default proof({
  label: "prf:h3-frobenius-casimir-markov-trace",
  title: "Proof of the H_3 Frobenius Casimir trace formulas",
  uses: ["prop:h3-frobenius-casimir-markov-trace"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Lean.** The sibling file proves, over an arbitrary field: `sigma1_quad`, `sigma2_quad`, `braid`, `tau0_dual`, `casimir_coords`, `casimir_central`, `tr_comm`, `tr_markov`, `markov_weights`, `ySign_D`, `yTriv_D`, `yRefl_D`, `tr_casimir`, `tr_casimir_D`, `tr_casimir_D_sub`, `tr_casimir_D_ne`, `tr_casimir_blocks`, `tau0_schur`, `inv_qdim_eq_schur_sum`, `inv_qdim_sum_three`, `inv_qdim_sum_three_D` and `cdimq_tautology`. There $H_3$ is $K^6$ with the basis multiplication above; associativity of that product, which is the statement that it is $H_3$ with its standard basis, is the textbook fact and is not re-proved, and uniqueness of the Ocneanu trace is cited [Jones 1987]. Sorry-free, lean-direct exit 0. $\\blacksquare$" },
  ],
});
