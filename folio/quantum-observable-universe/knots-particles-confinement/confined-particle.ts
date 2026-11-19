import { definition } from "../../schema/builders";

export default definition({
  label: "def:confined-particle",
  title: "Confined particle",
  lean: { ref: "qou:QOU.BraidKnot.ConfinedParticle",
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
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
    {
      kind: "note",
      body: "Archimedean specialisation over R (\u00a77c).",
    },
  ],
});
