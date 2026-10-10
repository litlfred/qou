import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:knot-eigenbasis-complete",
  label: "rem:knot-exhaustiveness",
  title: "Exhaustiveness of the QOU knots in the Descartes space (open)",
  tags: [
    "knot",
    "completeness",
    "exhaustive",
    "jones-polynomial",
    "open-question",
    "descartes",
  ],
  uses: [
    "prop:knot-eigenbasis-complete",
    "thm:jones-markov-trace",
  ],
});
