import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:jones-markov-trace",
  label: "rem:markov-lambda-knot-operations",
  title: "Wedderburn $\\lambda$-block decomposition of the Markov chain",
  tags: [
    "markov-chain",
    "young-graph",
    "syt",
    "wedderburn",
    "markov-moves",
    "reidemeister",
    "plancherel",
  ],
  cites: ["diaconis-ram2000", "jones1987"],
  uses: ["rem:hecke-markov-interpretation"],
});
