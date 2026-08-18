import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-categorical-precision-ladder",
  lean: {
    ref: "qou:QOU.BraidKnot.q_beta_categorical_precision_ladder",
    validation: "not_checked",
  },
  title:
    "$\\mathfrak{Q}_\\beta$ categorical-derivation precision ladder",
  uses: [],
  cites: [
    "jones1985",
    "wenzl1988",
    "kashiwara1990",
    "hoefsmit1974",
  ],
  tags: [
    "q-beta",
    "categorical-derivation",
    "precision-ladder",
    "kashiwara-crystal",
    "hopf-jones",
    "classical-limit",
    "KL-decategorification",
    "1ppb-roadmap",
    "n-p-mass-split",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/probe_q_beta_operator_valued_N3.py",
    witness: [
      "computations/q-beta-operator-valued-N3.witness.json",
      "computations/delta-S-chain-audit.witness.json"
    ],
    status: "experimental",
  },
});
