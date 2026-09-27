import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:strangelet-double-beta",
  title:
    "Strangelet interactions descend from the degree-2 fiber via double beta decay",
  tags: [
    "strangelet",
    "double-beta-decay",
    "degree-2-fiber",
    "cinquefoil",
    "skein-amplitude",
    "crossing-change",
    "electromagnetic-signature",
    "falsifiability",
  ],
  lean: { ref: "qou:QOU.Archimedean.strangelet_double_beta",
    validation: "not_checked",
  },
  uses: ["rem:strangelet-witten-stability"],
});
