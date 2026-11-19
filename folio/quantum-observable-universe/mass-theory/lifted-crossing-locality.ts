import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:lifted-crossing-locality",
  title:
    "Locality of lifted-crossing contributions in the mass expansion",
  tags: [
    "tier:E",
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
  uses: ["conj:crossing-graded-mass-expansion"],
  cites: ["kohno1987"],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
