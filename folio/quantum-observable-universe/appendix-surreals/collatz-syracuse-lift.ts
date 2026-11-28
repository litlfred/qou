import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:collatz-syracuse-lift",
  lean: {
    ref: "qou:QOU.AppendixSurreals.CollatzSyracuseLift.qCollatzConvergence_of_syracuseNoDivergence",
    validation: "leanok",
  },
  title: "The $q$-Collatz orbit lifts the Syracuse orbit",
  uses: ["conj:q-collatz", "prop:collatz-no-cycles"],
  tags: ["collatz", "syracuse", "specialisation", "classical-limit", "periodic-cycle"],
  cites: ["lagarias2010"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-28",
      body:
        "New, sorry-free in QOU/Observations/collatz_syracuse_lift.lean (axioms: propext, " +
        "Classical.choice, Quot.sound). Statements there: syracuse_of_step (item 1), " +
        "periodic_of_word_periodic (item 2), reaches_cycle_of_classical_periodic (item 3), " +
        "QCollatzConvergence / SyracuseNoDivergence and the implication between them (item 4).",
    },
  ],
});
