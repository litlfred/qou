import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-c-2-eq-neg-one-structural",
  title:
    "$c_2 = -1$ in the $\\mathfrak{Q}_\\beta$ precision ladder is structural — the $(1 - b^2 \\cdot \\hbar_q^4)$ N=2 factor IS $(1 - u^2)$ with $u = b \\cdot \\hbar_q^2$, hence the $(1 + c_2 \\cdot u^2)$ coefficient is exactly $-1$ by ring identity",
  lean: {
    ref: "qou:QOU.QBeta.C2Structural.c_2_eq_neg_one_structural",
    validation: "not_checked",
  },
  uses: [
    "prop:q-beta-c-k-recursion-from-habiro-q-difference",
    "prop:q-beta-over-e0-classical-vanishing",
    "prop:t-beta-markov-frobenius-collapse",
  ],
  cites: ["jones1987", "wenzl1988"],
  computation: {
    engine: "sympy",
    script:
      "computations/qbeta/qbeta_symbolic_chain_alpha_b.py",
    witness:
      "computations/qbeta/qbeta-symbolic-chain-alpha-b.witness.json",
    status: "verified",
  },
  tags: [
    "q-beta",
    "precision-ladder",
    "structural",
    "c-2",
    "categorical-derivation",
    "no-fit",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**Theorem (this proposition).** Sorry-free Lean proof\n([`q-beta-c-2-eq-neg-one-structural.lean`](q-beta-c-2-eq-neg-one-structural.lean))\n— one-line `ring` identity in `CommRing R`.\n\n**Compute (sympy).** Verified in\n[`qbeta_symbolic_chain_alpha_b.py`](https://github.com/litlfred/qou/blob/main/computations/qbeta/qbeta_symbolic_chain_alpha_b.py)\nwitness `qbeta-symbolic-chain-alpha-b.witness.json`, assertion\n`N2_factor_equals_one_minus_u_squared` (passing, tolerance $10^{-20}$).",
    },
  ],
});
