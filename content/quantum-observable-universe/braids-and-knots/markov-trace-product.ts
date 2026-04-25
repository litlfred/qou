import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:markov-trace-product",
  title:
    "Product factorization of the Markov trace",
  tags: [
    "markov-trace",
    "factorization",
    "jones-polynomial",
    "hecke-algebra",
    "vertex-operator",
  ],
  lean: { ref: "qou:QOU.markov_trace_product",
    validation: "not_checked",
  },
  uses: [
    "thm:jones-markov-trace",
    "def:vertex-operator",
  ],
});
