import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-universality",
  title: "Confinement universality: nucleon NF independent of photon polarization",
  tags: [
    "confinement",
    "universality",
    "photon",
    "polarization",
    "independence",
    "strong-force",
  ],
  lean: {
    decl: "QOU.Interactions.confinement_universality",
    validation: "not_checked",
  },
  uses: [
    "prop:four-term-pair-nucleon",
    "prop:confinement-operator-selection",
    "def:breit-wheeler-pair-production",
  ],
});
