import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:tau-leptonic-universality",
  proofs: ["prf:tau-leptonic-universality"],
  title:
    "Lepton universality from the $T_{3,5}$ weak vertex",
  tags: [
    "tau-decay",
    "lepton-universality",
    "weak-vertex",
    "branching-ratio",
    "hecke-algebra",
    "markov-trace",
    "T35",
    "factorized-model",
  ],
  lean: { ref: "qou:QOU.Archimedean.tau_leptonic_universality",
    validation: "not_checked",
  },
  uses: ["prop:lepton-continuant-recurrence"],
});
