import { definition } from "../../schema/builders";

export default definition({
  label: "def:derived-atom",
  title: "Derived atom $\\mathcal{A}(Z, N)$ from pair production",
  lean: {
    ref: "qou:QOU.Interactions.DerivedAtom",
    validation: "not_checked",
  },
  tags: [
    "atom",
    "derived",
    "pair-production",
    "nucleon",
    "confinement",
    "normal-form",
    "general",
  ],
  uses: [
    "prop:four-term-pair-nucleon",
    "prop:confinement-operator-selection",
    "def:stable-nucleus",
    "conj:electron-shells-hopf",
  ],
});
