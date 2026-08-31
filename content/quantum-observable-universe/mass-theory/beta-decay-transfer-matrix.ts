import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:beta-decay-transfer-matrix",
  title:
    "Beta decay as a universal matrix-valued polynomial in $q$",
  tags: [
    "beta-decay",
    "transfer-matrix",
    "polynomial",
    "q-deformed",
    "skein",
    "hecke",
    "universal",
    "matrix",
  ],
  lean: { ref: "qou:QOU.Archimedean.BetaDecayTransfer.beta_decay_transfer_matrix",
    validation: "not_checked",
  },
  uses: ["prop:skein-polynomial-transfer-matrix"],
});
