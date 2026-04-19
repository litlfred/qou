import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:four-term-pair-nucleon",
  lean: {
    decl: "QOU.ParticleInteractions.four_term_pair_nucleon",
    file: "QOU/ParticleInteractions.lean",
    validation: "not_checked",
  },
  title: "Nucleon derivation from 4-term photon pair production",
  tags: [
    "pair-production",
    "nucleon",
    "proton",
    "neutron",
    "4-term-photon",
    "color-content",
    "borromean",
    "derivation",
  ],
  uses: [
    "def:breit-wheeler-pair-production",
    "def:quark-antiquark-production",
    "prop:confinement-operator-selection",
    "prop:frobenius-gram-matrix",
    "def:categorical-proton",
    "def:categorical-neutron",
  ],
});
