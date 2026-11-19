import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:markov-trace-ratio-exact",
  title:
    "Ratios of Markov traces are normalization-independent",
  uses: ["prop:markov-trace-axiomatic-closed-form"],
  cites: ["jones1987"],
  tags: [
    "normalization",
    "markov-trace",
    "jones-polynomial",
    "optimization",
    "gram-matrix",
  ],
  lean: {
    ref: "qou:QOU.BraidsKnots.markov_trace_ratio_exact",
  },
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
