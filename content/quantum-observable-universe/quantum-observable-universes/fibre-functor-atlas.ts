import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:fibre-functor-atlas",
  proofs: ["prf:fibre-functor-atlas"],
  lean: { ref: "qou:QOU.QuantumObservableUniverse.fibre_functor_atlas", validation: "not_checked" },
  title:
    "Fibre functors as an affine atlas with $G$-torsor transitions",
  tags: [
    "fibre-functor",
    "affine-chart",
    "atlas",
    "tannaka-krein",
    "G-torsor",
    "cocycle",
  ],
  uses: [
    "def:contact-affine-chart",
    "rem:tannaka-krein-overview",
  ],
});
