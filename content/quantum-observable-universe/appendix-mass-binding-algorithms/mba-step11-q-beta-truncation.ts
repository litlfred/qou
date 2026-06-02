import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:q-beta-truncation",
  title: "$\\beta$-decay $Q_\\beta = Q_{\\mathrm{base}} \\cdot \\prod_k (1 + c_k\\, u^k)$",
  uses: [
    "prop:q-beta-categorical-precision-ladder",
  ],
  computation: {
    engine: "python+mpmath",
    script: "qou-mass/src/qou_mass/q_beta.py",
    witness: "folio-assistant/computations/cal-3-q-beta.witness.json",
    status: "verified",
  },
  tags: [
    "mba",
    "step-11",
    "q-beta",
    "ck-truncation",
    "beta-decay",
    "canonical-chain",
  ],
});
