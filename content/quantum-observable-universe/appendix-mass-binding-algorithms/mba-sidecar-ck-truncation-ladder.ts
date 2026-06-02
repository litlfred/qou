import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:ck-truncation-ladder",
  title: "$c_k$ truncation ladder — tiered classification",
  uses: [
    "prop:q-beta-categorical-precision-ladder",
  ],
  computation: {
    engine: "python+mpmath",
    script: "folio-assistant/computations/q_beta_predicted.py",
    witness: "folio-assistant/computations/q-beta-predicted.witness.json",
    status: "verified",
  },
  tags: [
    "mba",
    "sidecar",
    "ck-truncation",
    "q-beta",
    "tiered-coefficients",
  ],
});
