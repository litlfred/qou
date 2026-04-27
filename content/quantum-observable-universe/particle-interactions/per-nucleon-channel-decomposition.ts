import { definition } from "../../schema/builders";

export default definition({
  label: "def:per-nucleon-channel-decomposition",
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
