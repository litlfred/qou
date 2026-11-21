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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Hecke monodromy conjecture](#conj:hecke-monodromy-step-two))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Hecke monodromy conjecture](#conj:hecke-monodromy-step-two))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ([`QOU.Mass.KZFlatnessLevelIndependent`](#conj:hecke-monodromy-step-two))" },
  ],
});
