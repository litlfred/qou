import { prose } from "../../schema/builders";

export default prose({
  label: "sec:collatz-intro",
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-28",
      body:
        "Section intro written on owner request (project thread, 2026-11-28: " +
        "'not separate write-ups, just clear in the intros for the book'). " +
        "Sorts every Collatz claim into proved (Lean) / provable now / open / " +
        "out of reach. New proved result: the q→1 specialisation is the " +
        "Syracuse map, so classical no-divergence implies q-Collatz " +
        "convergence (QOU/Observations/collatz_syracuse_lift.lean).",
    },
  ],
});
