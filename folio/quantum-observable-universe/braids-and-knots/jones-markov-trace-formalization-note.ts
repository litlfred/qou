import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:jones-markov-trace",
  label: "rem:jones-markov-trace-formalization-note",
  title:
    "Formalization strategy for the Markov trace: axiomatic encoding of the three Jones properties",
  tags: [
    "markov-trace",
    "jones-polynomial",
    "formalization-note",
    "external-proof",
  ],
  uses: ["thm:jones-markov-trace"],
});
