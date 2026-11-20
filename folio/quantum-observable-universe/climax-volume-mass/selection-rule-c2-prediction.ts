import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:selection-rule-c2-prediction",
  title:
    "Per-component selection rule at c=2: $\\mathrm{lw}(2) = (q+1)^2/(3q)$",
  tags: [
    "selection-rule",
    "linking-weight",
    "wedderburn",
    "gelfand",
    "prediction",
    "hopf",
    "c2",
    "lean",
  ],
  lean: {
    ref: "qou:QOU.Mass.selection_rule_c2_prediction_derived",
    validation: "validated",
  },
  uses: ["prop:selection-rule-anchors-c1-c3"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): This proposition Lean-formalises the closed form for c=2 *from the hook-length formula itself*: [`QOU.Mass.selection_rule_c2_real`](../lean/QOU/Mass/QHookDimension.lean) states the sum over `dimQ` of the three partitions of 3, with `dim_q V_{(2,1)} = [2]_q` derived from the hook multiset `[3,1,1]` rather than asserted." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Lean proof structure | We rely on a single algebraic identity | This constitutes a pure polynomial-ring identity once we clear $q^{-1}$ denominators. We close it by `field_simp; ring` over $\\mathbb{R}_{>0}$." },
    {
      kind: "status",
      body: "- **c=1 anchor** ($\\mathrm{lw}(1) = 1$): proved in\n  [`prop:selection-rule-anchors-c1-c3`](#prop:selection-rule-anchors-c1-c3) (this branch).\n- **c=3 anchor** ($\\mathrm{lw}(3) = 5/2 + (3/4)h^2$): proved in\n  [`prop:selection-rule-anchors-c1-c3`](#prop:selection-rule-anchors-c1-c3) (this branch).\n- **c=2 prediction** ($\\mathrm{lw}(2) = (q+1)^2/(3q)$): proved here.\n- **General $c \\geq 4$ prediction**: requires a q-deformed hook-length\n  identity in Lean; out of scope for this proposition.",
    },
  ],
});
