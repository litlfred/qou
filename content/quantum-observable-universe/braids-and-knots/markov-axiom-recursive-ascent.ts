import { definition } from "../../schema/builders";

export default definition({
  label: "def:markov-axiom-recursive-ascent",
  title:
    "Markov-axiom recursive ascent for atomic $\\mathrm{tr}_M$",
  defines: ["markov-axiom-recursive-ascent"],
  lean: {
    ref: "qou:QOU.Interactions.markov_peel",
    validation: "not_checked",
  },
  uses: [
    "prop:markov-pair-z2",
    "thm:topological-mass",
  ],
  tags: ["markov-trace", "computation", "algorithm"],
});
