import { remark } from "../../schema/builders";

export default remark({
  label: "rem:markov-axiom-recursive-ascent-remark",
  title: "Cost of the recursive ascent",
  interprets: "def:markov-axiom-recursive-ascent",
  uses: [
    "def:markov-axiom-recursive-ascent",
    "prop:markov-pair-z2",
    "thm:topological-mass",
  ],
});
