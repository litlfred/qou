import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:type-b-folding-cpt",
  title:
    "Type-B Cartan folding realises CPT via symmetric-crystal $\\mathbb{Z}/2$ fixed points",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.TypeBFoldingCpt",
    validation: "not_checked",
  },
  uses: [
    "conj:cpt-d6-d7-d8-closure",
    "conj:c-from-color-flavor-swap",
    "conj:p-from-braid-mirror",
    "conj:t-from-trace-cyclicity",
  ],
  cites: [
    "kashiwara1991",
    "khovanovlauda2009",
    "brundankleshchev2009",
    "lecouvey2007",
  ],
  tags: [
    "type-b-folding",
    "duality-d22",
    "symmetric-crystal",
    "cpt",
    "matter-antimatter",
    "claude-md-7b",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
  ],
});
