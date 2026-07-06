import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:knot-particle-generation",
  defines: ["torus-knot-generators", "linking-operations"],
  title: "Knot-particle generation from $T_{m,n}$ torus knot generators",
  tags: [
    "knot",
    "particle",
    "generation",
    "torus-knot",
    "hopf-link",
    "color-tube",
    "skein",
    "exceptional-divisor",
  ],
  lean: { ref: "qou:QOU.Torsion.KnotParticleGeneration",
    validation: "not_checked",
  },
  uses: [
    "prop:skein-generation",
    "rem:knot-particle-dictionary",
    "rem:color-tube-interpretation",
  ],
});
