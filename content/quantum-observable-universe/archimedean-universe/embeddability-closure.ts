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
  lean: { ref: "qou:QOU.Torsion.embeddability_closure",
    validation: "not_checked",
  },
  uses: ["prop:torus-knot-generators"],
  proofs: ["prf:embeddability-closure"],
});
