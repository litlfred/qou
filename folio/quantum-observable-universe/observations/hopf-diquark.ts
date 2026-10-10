import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:hopf-diquark",
  title: "Hopf diquark",
  tags: [
    "diquark",
    "hopf",
    "cooper-pair",
    "color-superconductivity",
    "color-antitriplet",
  ],
  lean: { ref: "qou:QOU.Archimedean.HopfDiquark",
    validation: "not_checked",
  },
});
