import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:crystal-graph-realization",
  title:
    "Hecke normal forms realise crystal highest-weight vectors",
  lean: { ref: "qou:QOU.BraidKnot.CrystalGraphRealization", validation: "stub" },
  uses: [
    "def:hecke-normal-form",
  ],
  cites: [
    "brundankleshchev2009",
    "kashiwara1991",
    "lecouvey2007",
    "khovanovlauda2009",
    "marsh2000",
  ],
  tags: [
    "tier:S",
    "crystal-graph",
    "kashiwara-operator",
    "highest-weight",
    "klr",
    "computational-shortcut",
    "audit-flag-13a",
  ],
});
