import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:atom-knot-unique",
  title: "Uniqueness of the atom-knot up to Markov equivalence",
  lean: {
    decl: "QOU.BraidKnot.AtomKnot.unique",
    validation: "not_checked",
  },
  uses: [
    "def:atom-knot",
    "prop:atom-knot-exists",
    "thm:jones-markov-trace",
    "def:hecke-normal-form",
  ],
  tags: ["uniqueness", "atom-knot", "markov-equivalence"],
});
