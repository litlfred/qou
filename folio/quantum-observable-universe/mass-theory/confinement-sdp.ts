import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-sdp",
  title:
    "Confinement as semidefinite program with matrix Frobenius positivity",
  lean: { ref: "qou:QOU.ParticleInteractions.ConfinementSDP",
    validation: "not_checked",
  },
  uses: ["prop:confinement-lp"],
  tags: [
    "semidefinite-programming",
    "confinement",
    "psd-cone",
    "matrix-frobenius",
    "cross-channel-coupling",
    "multi-operator-binding",
    "sdp-duality",
    "spectral-gap",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
