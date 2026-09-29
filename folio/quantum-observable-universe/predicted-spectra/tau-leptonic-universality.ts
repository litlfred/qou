import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:tau-leptonic-universality",
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
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`lean/QOU/Archimedean/tau_leptonic_universality.lean` uses " +
        "`Real.log`. These are real-analytic constructs with no " +
        "generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
  ],
});
