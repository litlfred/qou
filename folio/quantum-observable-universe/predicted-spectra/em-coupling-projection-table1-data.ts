import { table } from "../../schema/builders";
export default table({ label: "tbl:em-coupling-projection-table1-data", title: "Evaluation of bare, Chern–Simons-resummed, and Bring–Schwinger forms of $\\alpha_{\\mathrm{EM}}^{-1}(q_0)$ against CODATA 2022", uses: ["prop:em-coupling-projection", "prop:local-substrate-q"], tags: ["extracted-table"],
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: [
      "computations/meson-em-sinh-closed-form.witness.json",
      "computations/alpha-em-form-ladder.witness.json",
      "computations/alpha-em-schwinger-ladder.witness.json",
    ],
    status: "verified",
  },
  authorNotes: [
    {
      kind: "note",
      body: "Computational provenance: computations/alpha/alpha_em_form_comparison_probe.py.",
    },
  ],
});
