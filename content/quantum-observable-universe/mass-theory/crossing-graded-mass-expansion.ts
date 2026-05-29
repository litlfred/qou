import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:crossing-graded-mass-expansion",
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
  uses: ["prop:lifted-crossing-locality"],
  cites: ["thurston1978"],
});
