import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:parity-violation-skein",
  title:
    "Parity non-conservation from the Skein relation at $q \\neq 1$",
  tags: [
    "parity",
    "weak-force",
    "skein-relation",
    "lee-yang",
    "wu-experiment",
    "mirror",
    "crossing-chirality",
    "symmetry-breaking",
  ],
  lean: { ref: "qou:QOU.Archimedean.parity_violation_skein",
    validation: "not_checked",
  },
  uses: [
    "def:beta-decay-skein",
    "prop:reidemeister-action-table",
  ],
});
