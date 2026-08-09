import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:coulomb-charge",
  title: "Coulomb charge of a knot composite",
  tags: ["coulomb", "charge", "crossing", "asymmetry", "skein"],
  lean: { ref: "qou:QOU.Braiding.CoulombCharge",
    validation: "not_checked",
  },
  uses: [
    "def:crossing-energy",
  ],
});
