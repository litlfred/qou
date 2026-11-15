import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:q-energy",
  title:
    "$q$-Deformed Energy",
  tags: [
    "energy",
    "q-deformed",
    "categorical-action",
    "momentum",
    "angular-momentum",
    "crossing",
    "mass-energy",
    "kinematic",
  ],
  lean: { ref: "qou:QOU.Archimedean.QEnergy",
    validation: "not_checked",
  },
  uses: ["def:q-angular-momentum"],
});
