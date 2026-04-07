import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:knot-eigenbasis-complete",
  label: "rem:knot-exhaustiveness",
  title: "Open question: are the QOU knots exhaustive in the Descartes space?",
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
