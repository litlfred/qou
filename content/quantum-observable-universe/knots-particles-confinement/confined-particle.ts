import { definition } from "../../schema/builders";

export default definition({
  label: "def:confined-particle",
  title: "Confined particle",
  lean: { ref: "qou:QOU.BraidKnot.ConfinedParticle",
    validation: "not_checked",
  },
  uses: ["prop:confinement-phase-stratification"],
  tags: [
    "confinement",
    "particle",
    "markov-class",
    "groebner-shirshov",
    "naming",
  ],
});
