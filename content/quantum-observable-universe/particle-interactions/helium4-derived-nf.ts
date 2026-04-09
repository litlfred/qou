import { example } from "../../schema/builders";

export default example({
  label: "ex:helium4-derived-nf",
  title: "He-4: alpha particle from pair production",
  interprets: "prop:four-term-pair-nucleon",
  tags: [
    "helium",
    "alpha-particle",
    "doubly-magic",
    "normal-form",
    "derived",
    "shell-closure",
  ],
  uses: [
    "def:categorical-proton",
    "def:categorical-neutron",
    "prop:confinement-operator-selection",
    "ex:helium-hopf-diagram",
  ],
});
