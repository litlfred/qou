import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-beta-categorical-precision-ladder-context",
  title:
    "Per-rung sources, truncation-order analysis, and open questions for the Q_beta precision ladder",
  interprets: "prop:q-beta-categorical-precision-ladder",
  tags: [
    "q-beta",
    "precision-ladder",
    "truncation-order",
    "habiro",
    "hoefsmit",
    "jones",
  ],
  uses: ["prop:q-beta-categorical-precision-ladder"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational provenance: computations/qbeta/qbeta_precision_ladder_n5.py (superseding N<=3 script probe_q_beta_operator_valued_N3.py and irreproducible legacy -0.0066 ppm / 7.133 ppb-shifted figures).",
    },
    {
      kind: "refined-framing",
      body: "An earlier draft of the non-monotonicity paragraph read the signed residual column and reached the reverse conclusion.",
    },
    {
      kind: "deprecated",
      body: "The precision ladder is superseded by the Habiro-ring identification (prop:habiro-precision-ladder-equivalence). The per-rung content is retained for historical reference and for the derivation narrative.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/qbeta/qbeta_precision_ladder_n5.py",
    witness: [
      "computations/qbeta/qbeta-precision-ladder-n5.witness.json",
      "computations/q-beta-operator-valued-N3.witness.json",
      "computations/qbeta/qbeta-ck-truncation-order-analysis.witness.json",
      "computations/gram-matrix-dual.witness.json",
      "computations/qbeta/qbeta-ck-c5-slot-and-size-mismatch.witness.json",
      "computations/cyclotomic-trilog-imaginary.witness.json",
    ],
    status: "verified",
  },
});
