import { remark } from "../../schema/builders";

export default remark({
  label: "rem:nucleon-from-photons-summary",
  title: "The full photon-to-atom derivation chain",
  interprets: "conj:four-term-pair-nucleon",
  tags: [
    "derivation-chain",
    "summary",
    "pair-production",
    "confinement",
    "atom",
    "conservation",
  ],
  uses: ["conj:four-term-pair-nucleon"],
});
