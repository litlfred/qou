import { proof } from "../../schema/builders";

export default proof({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prf:non-self-intersection",
  title: "Proof of Obstruction to self-intersection",
  uses: ["cor:non-self-intersection", "lem:nsi-q-deformed-kernel"],
  lean: { ref: "qou:QOU.NonSelfIntersection",
    validation: "not_checked",
  },
});
