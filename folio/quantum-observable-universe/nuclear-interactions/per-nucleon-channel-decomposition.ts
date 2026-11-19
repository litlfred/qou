import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:per-nucleon-channel-decomposition",
  examples: ["ex:per-nucleon-channel-decomposition"],
  defines: ["per-nucleon-channel-decomposition"],
  title:
    "Per-nucleon channel decomposition via $S_3^A$ branching",
  tags: [
    "branching",
    "channel-decomposition",
    "garside",
    "hecke-algebra",
    "per-nucleon",
    "torus-knot",
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.PerNucleonChannelDecomposition",
    validation: "not_checked",
  },
  uses: ["def:typed-crossing-operator"],
});
