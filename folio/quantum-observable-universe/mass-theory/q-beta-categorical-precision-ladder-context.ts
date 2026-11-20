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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Tables 2 and 3 above are computed by [`qbeta_precision_ladder_n5.py`](../../../computations/qbeta/qbeta_precision_ladder_n5.py) ... the block's previously declared producer, `probe_q_beta_operator_valued_N3.py`, stops at $N=3$" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): It is not **proved**: the Lean re-reads the $N{=}2$ factor rather than deriving it." },
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
