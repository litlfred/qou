import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:collatz-bounded-window",
  lean: {
    ref: "qou:QOU.AppendixSurreals.CollatzBoundedWindow.reaches_cycle_of_bounded_window",
    validation: "leanok",
  },
  title: "A $q$-Collatz orbit with bounded support converges",
  uses: ["conj:q-collatz", "prop:collatz-no-cycles", "prop:collatz-syracuse-lift"],
  tags: ["collatz", "pigeonhole", "mod-2-reduction", "periodic-cycle"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-28",
      body:
        "New, sorry-free in QOU/Observations/collatz_bounded_window.lean (axioms: propext, " +
        "Classical.choice, Quot.sound): reaches_cycle_of_bounded_window (item 1) and " +
        "counterexample_shape (item 2). The hypothesis is the Prop BoundedWindow.",
    },
  ],
});
