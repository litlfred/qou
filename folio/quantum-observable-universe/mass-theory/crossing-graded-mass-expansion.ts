import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:crossing-graded-mass-expansion",
  title:
    "Crossing-graded expansion of the categorical mass endomorphism",
  tags: [
    "tier:S",
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
  uses: [],
  cites: ["thurston1978"],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
