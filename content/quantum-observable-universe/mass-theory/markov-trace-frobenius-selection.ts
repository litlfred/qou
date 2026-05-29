import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:markov-trace-frobenius-selection",
  title: "Markov trace uniqueness on H_n(R, q) — the Jones–Markov form τ_M",
  chapter: "mass-theory",
  cites: ["jones1987", "wenzl1988", "yekutieli2015"],
  uses: [],
  defines: [],
  tags: ["normalization", "frobenius", "no-fitting", "uniqueness"],
  lean: { ref: "qou:QOU.BraidKnot.qou_markov_trace_is_jones_markov" },
});
