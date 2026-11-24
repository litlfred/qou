import { definition } from "../../schema/builders";

export default definition({
  label: "def:confined-particle",
  title: "Confined particle",
  lean: { ref: "qou:QOU.BraidsAndKnots.ConfinedParticle",
    validation: "not_checked",
  },
  uses: [],
  tags: [
    "confinement",
    "particle",
    "markov-class",
    "groebner-shirshov",
    "naming",
  ],
});
