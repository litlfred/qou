import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:jones-markov-trace",
  label: "rem:markov-lambda-knot-operations",
  title: "Knot operations, Markov chain, and the partition $\\lambda$",
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
  uses: [
    "prop:hecke-markov-transition",
    "prop:hoefsmit-seminormal-form",
    "thm:jones-markov-trace",
    "thm:markov-trace-product",
    "rem:hecke-markov-interpretation",
  ],
});
