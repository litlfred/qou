import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:jones-markov-trace",
  label: "rem:markov-lambda-knot-operations-moves",
  title:
    "Knot operations split into $\\lambda$-preserving and $\\lambda$-changing moves",
  tags: [
    "markov-moves",
    "reidemeister",
    "young-graph",
    "stabilization",
    "q-plancherel",
  ],
  cites: ["diaconis-ram2000", "jones1987"],
  uses: ["rem:markov-lambda-knot-operations"],
});
