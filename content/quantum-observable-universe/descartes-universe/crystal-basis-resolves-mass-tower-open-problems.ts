import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:crystal-basis-resolves-mass-tower-open-problems",
  title:
    "Crystal-basis correspondence (Brundan-Kleshchev + Type-B folding) reduces three mass-tower open problems to crystal-graph combinatorics",
  uses: [
    "conj:crystal-graph-realization",
    "conj:kazhdan-lusztig-classical-limit",
    "conj:hecke-anyonic-substrate",
    "prop:em-coupling-bring-zero-mode",
    "prop:archimedean-functor-uniqueness",
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
    ref: "qou:QOU.Descartes.crystal_basis_reduction",
    validation: "not_checked",
  },
});
