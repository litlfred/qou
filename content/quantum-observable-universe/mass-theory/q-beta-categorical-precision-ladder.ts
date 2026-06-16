import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-categorical-precision-ladder",
  lean: {
    ref: "qou:QOU.BraidKnot.q_beta_categorical_precision_ladder",
    validation: "not_checked",
  },
  title:
    "$\\mathfrak{Q}_\\beta$ categorical-derivation precision ladder: $\\mathfrak{Q}_\\beta^A \\cdot \\cos(\\alpha - b\\hbar_q^2/2) \\cdot (1 - b^2 \\hbar_q^4) \\cdot (1 - 2 b^3 \\hbar_q^6) \\cdot (1 + (b^2 + 1/2) b^4 \\hbar_q^8)$ from Kashiwara crystal + Hopf-Jones at q=1, $-0.0066$ ppm against CODATA at $N=3$",
  uses: ["prop:tau-M-asymptotic-rep-theory"],
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
    script: "folio-assistant/computations/probe_q_beta_operator_valued_N3.py",
    witness: [
      "folio-assistant/computations/q-beta-operator-valued-N3.witness.json",
      "folio-assistant/computations/delta-S-chain-audit.witness.json"
    ],
    status: "experimental",
  },
});
