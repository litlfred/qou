import { example } from "../../schema/builders";

export default example({
  label: "ex:hydrogen-derived-nf",
  title: "Hydrogen: full normal form from pair production",
  interprets: "prop:four-term-pair-nucleon",
  tags: ["hydrogen", "atom", "normal-form", "derived", "hopf-link"],
  uses: [
    "def:categorical-proton",
    "prop:frobenius-gram-matrix",
    "def:electron-knot",
    "ex:hydrogen-knot-structure",
  ],
});
