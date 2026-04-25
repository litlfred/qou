import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:hecke-markov-transition",
  label: "rem:hecke-markov-interpretation",
  title: "Markov chain validation of the algebraic framework",
  tags: [
    "markov-chain",
    "information-theory",
    "entanglement",
    "asep",
    "boltzmann-weight",
    "memoryless",
    "syt",
    "young-graph",
    "amplitudes",
  ],
  cites: ["diaconis-ram2000", "bufetov2020"],
  uses: [
    "prop:hecke-markov-transition",
    "prop:hoefsmit-seminormal-form",
    "thm:jones-markov-trace",
    "def:information-theoretic-time",
    "thm:markov-trace-product",
    "rem:markov-trace-product-interpretation",
  ],
});
