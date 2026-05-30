import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:crossing-graded-mass-expansion",
  title:
    "Crossing-graded expansion of the categorical mass endomorphism",
  tags: [
    "crossing-expansion",
    "skein",
    "quantum-dilogarithm",
    "perturbative",
    "groebner-shirshov",
    "mass-endomorphism",
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.CrossingGradedMassExpansion",
    validation: "not_checked",
  },
  uses: ["conj:lifted-crossing-locality"],
  cites: ["thurston1978"],
});
