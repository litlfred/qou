import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:lifted-crossing-locality",
  title:
    "Locality of lifted-crossing contributions in the mass expansion",
  tags: [
    "locality",
    "crossing-expansion",
    "quantum-dilogarithm",
    "factorization",
    "kz-connection",
    "flatness",
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.LiftedCrossingLocality",
    validation: "not_checked",
  },
  uses: ["prop:crossing-graded-mass-expansion"],
  cites: ["kohno1987"],
});
