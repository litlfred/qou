import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:tmli-constituent-composite-agreement",
  lean: { ref: "qou:QOU.BraidsKnots.tmli_constituent_composite_agreement",
    validation: "not_checked",
  },
  title: "Constituent and composite Markov-trace evaluations agree exactly",
  tags: ["markov-trace", "iwahori-hecke", "pawlei-basis", "exact-identity"],
  uses: ["rem:knot-factorization", "thm:markov-trace-product"],
  proofs: ["prf:tmli-constituent-composite-agreement"],
});
