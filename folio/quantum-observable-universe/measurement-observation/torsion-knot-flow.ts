import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:torsion-knot-flow",
  title: "Torsion-driven knot flow",
  tags: ["torsion", "flow", "knot", "geodesic", "categorical"],
  lean: { ref: "qou:QOU.ParticleState",
    validation: "not_checked",
  },
  uses: [
    "def:bundle-initial-conditions",
    "def:categorical-q-reeb-flow",
  ],
});
