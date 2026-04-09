import { example } from "../../schema/builders";

export default example({
  label: "ex:deuterium-derived-nf",
  title: "Deuterium: proton--neutron binding normal form",
  interprets: "prop:four-term-pair-nucleon",
  tags: ["deuterium", "nucleus", "normal-form", "derived", "binding"],
  uses: [
    "descartes-universe:def:categorical-proton",
    "descartes-universe:def:categorical-neutron",
    "prop:confinement-operator-selection",
  ],
});
