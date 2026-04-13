import { remark } from "../../schema/builders";

export default remark({
  label: "rem:markov-z-reconciliation",
  title: "Reconciliation of the Markov parameter $z$",
  interprets: "prop:categorical-mass-markov",
  uses: [
    "thm:jones-markov-trace",
    "prop:categorical-mass-markov",
  ],
  tags: [
    "markov-trace",
    "normalization",
    "convention",
  ],
});
