import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:markov-trace-product",
  proofs: ["prf:markov-trace-product"],
  title:
    "Product factorization of the Markov trace",
  tags: [
    "markov-trace",
    "factorization",
    "jones-polynomial",
    "hecke-algebra",
    "vertex-operator",
  ],
  lean: { ref: "qou:QOU.Hecke.markov_trace_product",
    validation: "not_checked",
  },
  uses: ["def:vertex-operator"],
});
