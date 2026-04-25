import { definition } from "../../schema/builders";

export default definition({
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
