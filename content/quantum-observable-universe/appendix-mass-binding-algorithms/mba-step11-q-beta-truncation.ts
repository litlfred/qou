import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:q-beta-truncation",
  title: "$\\beta$-decay $\\mathfrak{Q}_\\beta = Q_{\\mathrm{base}} \\cdot \\prod_k (1 + c_k\\, u^k)$",
  uses: [
    "prop:q-beta-categorical-precision-ladder",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_beta_predicted.py",
    witness: "computations/cal-3-q-beta.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "status",
      body:
        "Superseded status figures, moved out of the published prose during " +
        "the one-voice pass: the earlier note read \"164.0x as of 2026-05-31 " +
        "/ Habiro-exact 5.7 ppb at the pre-re-pin muon anchor\". Those " +
        "numbers describe the pre-re-pin muon anchor, not the current pin; " +
        "the live figures are in the block's Status paragraph.",
    },
  ],
  tags: [
    "mba",
    "step-11",
    "q-beta",
    "ck-truncation",
    "kashiwara-b2",
    "beta-decay",
    "canonical-chain",
  ],
});
