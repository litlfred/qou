import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-sdp",
  title:
    "Confinement as semidefinite program with matrix Frobenius positivity",
  lean: { ref: "qou:QOU.ParticleInteractions.ConfinementSDP",
    validation: "not_checked",
  },
  uses: [
    "prop:confinement-operator-selection",
    "prop:frobenius-gram-matrix",
    "prop:confinement-lp",
    "prop:knot-operator-selection",
    "def:crossing-energy",
    "rem:hecke-algebra-from-braiding",
    "thm:jones-markov-trace",
    "def:substrate-parameter",
  ],
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
});
