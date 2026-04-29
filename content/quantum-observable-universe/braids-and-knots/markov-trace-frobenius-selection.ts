import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:markov-trace-frobenius-selection",
  title: "Markov trace selection from Frobenius pairing non-degeneracy",
  chapter: "braids-and-knots",
  cites: ["jones1987", "wenzl1988", "yekutieli2015"],
  uses: [
    "prop:atom-knot-mass-derivation",
    "thm:frobenius-codim-universal",
    "prop:schur-weyl-vanishing",
    "prop:categorical-mass-markov",
  ],
  defines: [],
  tags: ["normalization", "frobenius", "no-fitting", "selection"],
  lean: { ref: "qou:QOU.BraidKnot.qou_markov_trace_is_jones_markov" },
});
