import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-universality",
  proofs: ["prf:confinement-universality"],
  title: "Confinement universality: nucleon NF independent of photon polarization",
  tags: [
    "confinement",
    "universality",
    "photon",
    "polarization",
    "independence",
    "strong-force",
  ],
  lean: { ref: "qou:QOU.Interactions.confinementUniversality",
    validation: "not_checked",
  },
  uses: ["prop:four-term-pair-nucleon"],
});
