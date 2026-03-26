import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:embeddability-closure",
  title: "Embeddability closure under knot-particle generation",
  tags: [
    "embeddability",
    "genus",
    "torus-knot",
    "generation",
    "descent",
    "localized-knot",
    "spectral-filter",
  ],
  lean: {
    decl: "QOU.Torsion.embeddability_closure",
    validation: "not_checked",
  },
  uses: [
    "def:knot-particle-generation",
    "prop:torus-knot-generators",
    "def:localized-knot",
    "def:hadron",
    "rem:hadron-operations",
    "prop:skein-generation",
    "prop:euler-char-stability",
  ],
  proofs: ["prf:embeddability-closure"],
});
