import { example } from "../../schema/builders";

export default example({
  label: "ex:hydrogen-derived-nf",
  title: "Hydrogen: full normal form from pair production",
  interprets: "prop:four-term-pair-nucleon",
  tags: ["hydrogen", "atom", "normal-form", "derived", "hopf-link"],
  uses: [
    "descartes-universe:def:categorical-proton",
    "descartes-universe:prop:frobenius-gram-matrix",
    "descartes-universe:def:electron-knot",
    "descartes-universe:ex:hydrogen-knot-structure",
  ],
});
