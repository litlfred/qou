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
      kind: "refined-framing",
      body: "An earlier draft of the non-monotonicity paragraph read the signed residual column and reached the reverse conclusion.",
    },
    {
      kind: "deprecated",
      body: "The precision ladder is superseded by the Habiro-ring identification (prop:habiro-precision-ladder-equivalence). The per-rung content is retained for historical reference and for the derivation narrative.",
    },
  ],
});
