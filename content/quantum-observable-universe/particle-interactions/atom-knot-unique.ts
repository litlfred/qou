import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:atom-knot-unique",
  proofs: ["prf:atom-knot-unique"],
  title: "Uniqueness of the atom-knot up to Markov equivalence",
  lean: { ref: "qou:QOU.BraidKnot.AtomKnot.unique",
    validation: "not_checked",
  },
  uses: ["prop:atom-knot-exists"],
  tags: ["uniqueness", "atom-knot", "markov-equivalence"],
});
