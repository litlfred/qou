import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:briggs-klein-chart",
  lean: { ref: "qou:QOU.BriggsKleinChart", validation: "not_checked" },
  title: "Briggs--Klein affine chart",
  tags: ["brings-surface", "coordinate-chart"],
  uses: ["def:brings-surface"],
});
