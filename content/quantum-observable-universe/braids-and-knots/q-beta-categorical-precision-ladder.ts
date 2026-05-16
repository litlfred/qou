import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-categorical-precision-ladder",
  lean: {
    ref: "qou:QOU.BraidKnot.q_beta_categorical_precision_ladder",
    validation: "not_checked",
  },
  title:
    "$Q_\\beta$ categorical-derivation precision ladder: $Q_\\beta^A \\cdot \\cos(\\alpha - b\\hbar_q^2/2) \\cdot (1 - b^2 \\hbar_q^4) \\cdot (1 - 2 b^3 \\hbar_q^6) \\cdot (1 + (b^2 + 1/2) b^4 \\hbar_q^8)$ from Kashiwara crystal + Hopf-Jones at q=1, $-0.0066$ ppm against CODATA at $N=3$",
  uses: [
    "prop:neutron-qvalue-symbolic",
    "prop:q-beta-spectral-bridge",
    "prop:q-beta-cos-resummation",
    "prop:hoefsmit-V21-cos-symmetrization",
    "prop:hecke-1d-irrep-closed-form-character",
    "prop:tau-M-asymptotic-rep-theory",
    "conj:archimedean-remainder-exponential-decay",
  ],
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
    witness: [
      "../../folio-assistant/computations/q-beta-tightening-landscape.witness.json",
      "../../folio-assistant/computations/q-beta-operator-valued-N1.witness.json",
      "../../folio-assistant/computations/q-beta-operator-valued-N2.witness.json",
      "../../folio-assistant/computations/q-beta-operator-valued-N3.witness.json",
      "../../folio-assistant/computations/tau-M-four-anchors.witness.json",
      "../../folio-assistant/computations/delta-S-chain-audit.witness.json",
    ],
  },
});
