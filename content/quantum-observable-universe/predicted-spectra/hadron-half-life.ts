import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "While the resulting decay structure follows the standard weak-decay formulation, the novelty lies in successfully re-deriving this empirical structure purely categorically, unifying the Fermi golden rule and Sargent's rule within a fundamental Markov-trace matrix element." },
  ],
  label: "prop:hadron-half-life",
  title:
    "Hadron half-life from the $q$-deformed transition amplitude",
  tags: [
    "half-life",
    "beta-decay",
    "hadron",
    "transition-amplitude",
    "substrate-parameter",
    "valley-of-stability",
  ],
  lean: { ref: "qou:QOU.Archimedean.hadron_half_life",
    validation: "not_checked",
  },
  uses: ["prop:integer-stability"],
});
