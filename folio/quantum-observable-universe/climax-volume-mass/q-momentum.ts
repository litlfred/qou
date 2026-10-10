import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:q-momentum",
  title: "$q$-Momentum from the braid writhe",
  tags: [
    "momentum",
    "q-deformed",
    "writhe",
    "braid",
    "hecke",
    "crossing",
    "kinematic",
  ],
  lean: { ref: "qou:QOU.Archimedean.QMomentum",
    validation: "not_checked",
  },
  uses: [],
});
