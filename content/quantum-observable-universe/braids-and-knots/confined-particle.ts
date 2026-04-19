import { definition } from "../../schema/builders";

export default definition({
  label: "def:confined-particle",
  title: "Confined particle",
  lean: {
    decl: "QOU.BraidKnot.ConfinedParticle",
    validation: "not_checked",
  },
  uses: [
    "def:hecke-normal-form",
    "def:confinement-level",
    "prop:confinement-sdp",
    "prop:confinement-phase-stratification",
  ],
  tags: [
    "confinement",
    "particle",
    "markov-class",
    "groebner-shirshov",
    "naming",
  ],
});
