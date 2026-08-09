import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:chirality-writhe-ribbon-derivation",
  title:
    "Chirality factor $1 + w \\cdot h$ from ribbon-twist framing (writhe $w$)",
  lean: {
    ref: "qou:QOU.BraidKnot.ChiralityWritheRibbon.chirality_writhe_ribbon",
    validation: "not_checked",
  },
  uses: ["prop:e-infinity-page-identifications"],
  computation: {
    engine: "mpmath",
    script: "computations/chirality_avg_content.py",
    witness: "computations/chirality-avg-content.witness.json",
    status: "experimental",
  },
  tags: [
    "chirality",
    "writhe",
    "ribbon",
    "kauffman-framing",
    "derivation",
    "term-5",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body: `**Base ring (§7c) — \`ℝ\` is load-bearing.** \`RibbonTwistEigenvalue\` carries \`q_pos : 0 < q\` as a class field, and \`log_q_first_order\` takes \`0 < q\` and expands a logarithm to first order. An ordering hypothesis in the class signature and a \`log\` in the statement are archimedean by construction; the \`linarith\` / \`nlinarith\` in the proofs consume that order.`,
    },
  ],
});
