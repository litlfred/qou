import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:tower-binding-energy",
  title:
    "Nuclear binding energy from the $3$-channel brane tower",
  tags: [
    "binding-energy",
    "brane-tower",
    "wedderburn",
    "three-channel",
    "partition-function",
    "zero-fitting",
    "analytic-continuation",
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.towerBinding",
    validation: "not_checked",
  },
  uses: [
        "rem:hecke-charge-mass-duality",
  ],
});
