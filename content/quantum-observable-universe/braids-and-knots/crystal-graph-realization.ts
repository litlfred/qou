import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:crystal-graph-realization",
  title:
    "Hecke normal forms realise crystal highest-weight vectors",
  uses: [
    "def:hecke-normal-form",
    "def:knot-operator-energy",
  ],
  cites: [
    "brundankleshchev2009",
    "kashiwara1991",
    "lecouvey2007",
    "khovanovlauda2009",
  ],
  tags: [
    "crystal-graph",
    "kashiwara-operator",
    "highest-weight",
    "klr",
    "computational-shortcut",
    "audit-flag-13a",
  ],
});
