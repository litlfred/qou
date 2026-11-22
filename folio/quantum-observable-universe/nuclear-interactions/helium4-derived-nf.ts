import { example } from "../../schema/builders";

export default example({
  label: "ex:helium4-derived-nf",
  title: "He-4: alpha particle from pair production",
  interprets: "conj:four-term-pair-nucleon",
  tags: [
    "helium",
    "alpha-particle",
    "doubly-magic",
    "normal-form",
    "derived",
    "shell-closure",
  ],
  uses: [
    "prop:confinement-operator-selection",
    "rem:helium-hopf-diagram",
  ],
});
