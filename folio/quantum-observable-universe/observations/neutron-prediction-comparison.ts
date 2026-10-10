import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:neutron-prediction-comparison",
  title:
    "Comparison of predicted and observed stable neutron numbers for $p \\leq 103$",
  tags: [
    "stability-cubic",
    "neutron-number",
    "codata",
    "comparison",
    "beta-stability",
  ],
  lean: { ref: "qou:QOU.Archimedean.stable_neutron_max_error",
    validation: "not_checked",
  },
  uses: ["prop:integer-stability"],
});
