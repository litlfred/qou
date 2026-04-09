import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:four-term-pair-nucleon",
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
    "descartes-universe:def:breit-wheeler-pair-production",
    "descartes-universe:def:quark-antiquark-production",
    "prop:confinement-operator-selection",
    "descartes-universe:prop:frobenius-gram-matrix",
    "descartes-universe:def:categorical-proton",
    "descartes-universe:def:categorical-neutron",
  ],
});
