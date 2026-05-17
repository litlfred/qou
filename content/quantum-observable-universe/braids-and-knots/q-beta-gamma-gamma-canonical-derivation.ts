import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-beta-gamma-gamma-canonical-derivation",
  title:
    "Story B selected as canonical $Q_\\beta$ interpretation by tracing the cat-action → Frobenius → Wedderburn → Wenzl bridge chain on canonical typed-$B_3$ braids; the $c_3 = -2$ Hopf-Jones identification is empirically observable at 112× residual reduction vs CODATA $Q_\\beta$ floor",
  interprets: "prop:q-beta-categorical-precision-ladder",
  uses: [
    "prop:q-beta-categorical-precision-ladder",
    "prop:hoefsmit-V21-cos-symmetrization",
    "prop:markov-trace-frobenius-selection",
    "prop:hecke-1d-irrep-closed-form-character",
    "prop:tau-M-asymptotic-rep-theory",
    "rem:kashiwara-jones-alternation-interpretation",
  ],
  cites: [
    "wenzl1988",
    "jones1985",
    "hoefsmit1974",
  ],
  tags: [
    "gamma-gamma",
    "categorical-derivation",
    "story-A-vs-B",
    "wenzl-bridge",
    "story-B-canonical",
    "1ppb-roadmap",
  ],
  computation: {
    engine: "python+mpmath",
    script: "folio-assistant/computations/probe_q_beta_high_precision_ck.py",
    witness: [
      "folio-assistant/computations/q-beta-gamma-gamma-derivation.witness.json",
      "folio-assistant/computations/q-beta-high-precision-ck.witness.json",
    ],
    status: "experimental",
  },
});
