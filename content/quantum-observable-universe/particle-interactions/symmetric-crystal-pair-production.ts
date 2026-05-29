import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:symmetric-crystal-pair-production",
  title:
    "Type-B folding forces matter/antimatter to be created in conjugate-operator pairs",
  lean: { ref: "qou:QOU.BraidKnot.SymmetricCrystalPairProduction", validation: "stub" },
  uses: [
    "prop:crystal-graph-realization",
    "def:hecke-normal-form",
    "def:cemetery-group",
  ],
  cites: [
    "kashiwara1991",
    "lecouvey2007",
    "khovanovlauda2009",
    "brundankleshchev2009",
  ],
  tags: [
    "symmetric-crystal",
    "type-b-folding",
    "bar-involution",
    "pair-production",
    "chirality",
    "cpt",
    "computational-shortcut",
  ],
});
