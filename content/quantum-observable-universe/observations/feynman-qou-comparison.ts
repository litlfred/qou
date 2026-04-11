import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:atom-mass-full-hecke",
  label: "rem:feynman-qou-comparison",
  title:
    "Feynman vs QOU: term-by-term atomic mass comparison",
  tags: [
    "mass",
    "feynman",
    "bethe-weizsacker",
    "SEMF",
    "wedderburn",
    "binding-energy",
    "comparison",
  ],
  uses: [
    "rem:atom-mass-full-hecke",
    "rem:mass-comparison-table",
    "prop:wedderburn-mass-formula",
    "def:hecke-mass-element",
    "def:algebraic-quantum-volume",
  ],
  cites: [
    "jones1985",
  ],
});
