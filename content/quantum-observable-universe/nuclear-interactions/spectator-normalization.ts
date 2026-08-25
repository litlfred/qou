import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:spectator-normalization",
  title:
    "Spectator normalization factor",
  tags: [
    "spectator",
    "normalization",
    "fermionic",
    "factorization",
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.SpectatorNormalization",
    validation: "not_checked",
  },
  uses: [
    "def:per-nucleon-channel-decomposition",
  ],
});
