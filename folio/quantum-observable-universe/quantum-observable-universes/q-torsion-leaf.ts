import { example } from "../../schema/builders";

export default example({
  interprets: "def:categorical-q-connection",
  label: "ex:q-torsion-leaf",
  title: "$q$-Torsion leaf",
  lean: { ref: "qou:QOU.QTorsionLeaf", validation: "not_checked" },
  uses: ["ex:q-reeb-flow"],
  tags: ["torsion-leaf", "archimedean"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (deliberate two-sided placement).** This file " +
        "carries both signals on purpose, and the split is the one §7c asks " +
        "for: the q-side is generic — `q_param`/`q_inv_param` over " +
        "`R_q = LaurentPolynomial ℤ` — while the archimedean side (`ReebDecomposition` " +
        "components `M → ℝ`, and flow invariance quantified over $t \\in \\mathbb{R}$) " +
        "is `ℝ` because Reeb flow time has no generic-ring counterpart. " +
        "Specialise via $\\iota : R_q \\to \\mathbb{R}$, $q \\mapsto q_0$. The " +
        "`wall-side-correct` mixed-signal flag here is the criterion detecting " +
        "the coexistence, not a misplacement to repair.",
    },
  ],
});
