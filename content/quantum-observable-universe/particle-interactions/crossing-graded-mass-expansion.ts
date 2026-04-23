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
  lean: {
    decl: "QOU.ParticleInteractions.CrossingGradedMassExpansion",
    validation: "not_checked",
  },
  uses: [
    "conj:mass-volume-factorization",
    "conj:lifted-crossing-locality",
    "rem:kashaev-volume-density",
    "def:crossing-energy",
    "def:algebraic-quantum-volume",
    "prop:descartes-elliptic-curve",
    "prop:thurston-volume-additivity",
    "prop:tower-binding-energy",
  ],
  cites: ["thurston1978"],
});
