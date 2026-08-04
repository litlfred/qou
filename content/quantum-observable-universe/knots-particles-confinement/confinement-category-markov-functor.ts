import { remark } from "../../schema/builders";

/**
 * The Markov trace as a functor out of the confinement category:
 * invariant under folding/unfolding, multiplicative under dressing.
 */
export default remark({
  label: "rem:confinement-category-markov-functor",
  title: "Functoriality of the Markov trace on $\\mathbf{Conf}$",
  interprets: "def:confinement-category",
  uses: ["def:confinement-category"],
  tags: [
    "markov-trace",
    "functor",
    "confinement",
    "category",
  ],
});
