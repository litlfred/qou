import { remark } from "../../schema/builders";

export default remark({
  label: "rem:nucleon-from-photons-summary",
  title: "The full photon-to-atom derivation chain",
  interprets: "prop:four-term-pair-nucleon",
  tags: [
    "derivation-chain",
    "summary",
    "pair-production",
    "confinement",
    "atom",
    "conservation",
  ],
  uses: [
    "descartes-universe:def:breit-wheeler-pair-production",
    "descartes-universe:def:quark-antiquark-production",
    "prop:confinement-operator-selection",
    "prop:four-term-pair-nucleon",
  ],
});
