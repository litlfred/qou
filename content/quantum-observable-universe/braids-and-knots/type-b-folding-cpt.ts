import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:type-b-folding-cpt",
  title:
    "Type-B Cartan folding realises CPT via symmetric-crystal $\\mathbb{Z}/2$ fixed points",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.TypeBFoldingCPT",
    validation: "not_checked",
  },
  uses: [
    "def:bar-involution",
    "prop:cpt-orbit-closure-density",
    "conj:c-from-color-flavor-swap",
    "conj:p-from-braid-mirror",
    "conj:t-from-trace-cyclicity",
    "def:hecke-normal-form",
  ],
  cites: [
    "kashiwara1991",
    "khovanov-lauda2009",
    "brundan-kleshchev2009",
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
    "non-scholarly-voice-exception",
  ],
});
