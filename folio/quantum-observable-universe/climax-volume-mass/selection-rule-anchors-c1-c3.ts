import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:selection-rule-anchors-c1-c3",
  title:
    "Per-component selection rule $\\frac{1}{c+1}\\sum_{\\lambda\\vdash c+1} \\dim_q V_\\lambda$ at c=1, c=3",
  tags: [
    "selection-rule",
    "linking-weight",
    "wedderburn",
    "gelfand",
    "family-a",
    "lean",
  ],
  lean: {
    ref: "qou:QOU.Mass.selection_rule_c3_anchor_derived",
    validation: "validated",
  },
  uses: [],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-08-29",
      body: "**What the earlier formalisation did and did not do.** Until 2026-08-29 the Lean here proved `((1 : R) + 1) / 2 = 1` for c=1 and the corresponding Laurent identity for c=3 — true statements, but arithmetic over q-dimension values typed in by hand, with no partition, hook length or `dim_q` occurring in any *statement*. The hook-length step lived in a docstring. Those theorems remain in `selection-rule-anchors-c1-c3.lean` and are still true; what was missing, and is now supplied, is the derivation of their left-hand sides (bean `qou-lx7k`).",
    },
  ],
});
