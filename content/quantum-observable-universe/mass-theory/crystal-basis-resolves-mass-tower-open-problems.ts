import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:crystal-basis-resolves-mass-tower-open-problems",
  title:
    "Crystal-basis correspondence (Brundan-Kleshchev + Type-B folding) reduces three mass-tower open problems to crystal-graph combinatorics",
  uses: [
    "conj:kazhdan-lusztig-classical-limit",
  ],
  cites: [
    "brundankleshchev2009",
    "kashiwara1991",
    "khovanovlauda2009",
    "lecouvey2007",
    "mayer1949",
  ],
  tags: [
    "crystal-basis",
    "klr-algebra",
    "kashiwara-crystal",
    "brundan-kleshchev",
    "type-b-folding",
    "kazhdan-lusztig",
    "chirality-factor",
    "term-7",
    "z-habiro",
    "open-problem-reduction",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.crystal_basis_reduction",
    validation: "not_checked",
  },
  authorNotes: [
    {
      kind: "status",
      body:
        "**Structural reduction (sorry-free conditional).** This proposition does *not* close the four open problems. It reduces three of them — chirality, Term 7, z-Habiro — to finite-graph computations on Kashiwara crystals already documented in the repository. Each reduction is sorry-free conditional on the upstream Brundan-Kleshchev / Lecouvey conjectures; the residual open content is the explicit crystal-graph computation per problem.",
    },
  ],
});
