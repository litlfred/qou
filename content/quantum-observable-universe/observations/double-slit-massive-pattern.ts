import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:double-slit-massive-pattern",
  lean: { ref: "qou:QOU.Experimental.double_slit_massive_pattern",
    validation: "not_checked",
  },
  title: "Massive-particle interference pattern",
  uses: [
    "def:double-slit-q-phase",
    "rem:q-laplacian-expansion",
    "def:q-hodge-star",
  ],
  tags: ["double-slit", "interference", "massive-particle", "q-laplacian"],
  cites: [
    "bach2013",
  ],
});
