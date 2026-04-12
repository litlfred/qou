import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hecke-markov-transition",
  title: "Hecke generator as stochastic transition operator",
  tags: [
    "hecke-algebra",
    "markov-chain",
    "transition-probability",
    "idempotent",
    "memoryless",
  ],
  cites: ["diaconis-ram2000", "bufetov2020"],
  uses: [
    "rem:hecke-algebra-from-braiding",
    "thm:jones-markov-trace",
    "prop:feynman-categorical-trace",
    "thm:markov-trace-product",
  ],
});
