import { definition } from "../../schema/builders";

export default definition({
  label: "def:derived-atom",
  title: "Derived atom $\\mathcal{A}(Z, N)$ from pair production",
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
    "descartes-universe:def:stable-nucleus",
    "descartes-universe:conj:electron-shells-hopf",
  ],
});
